Example for Configuring PPPoE Dual-Stack User Access (ND Unshared+PD) in a Dual-Device Hot Backup Scenario with Distributed CGN and EDSG Service Configured
===========================================================================================================================================================

In a dual-device hot backup scenario, dual-stack users connect to the master and backup BRASs using PPPoE. The BRASs assign IPv6 addresses to the users in ND unshared+PD mode to implement user access.

#### Networking Requirements

On the network shown in [Figure 1](dc_ne_cfg_rui_0064.html#EN-US_TASK_0210982515__fig_dc_ne_cfg_rui_003101), User1 and User2 access BRAS1 and BRAS2 through SW1. The BRASs use RADIUS authentication and accounting. They assign to the users IPv4 addresses through the local address pool, IPv6 prefixes through DHCPv6 IA\_PD, and IPv6 addresses through ND.

To enable private network users to access the Internet, distributed CGN needs to be deployed on the network to translate private addresses into public addresses. In addition, User1 and User2 have different requirements for network service traffic. As such, EDSG services need to be deployed. ACLs also need to be used to match the destination addresses and distinguish the network segments for user access so that independent rate limiting and accounting can be implemented for different network segments. Further to this, dual-device hot backup needs to be deployed to improve network reliability. If a fault occurs, a master/backup switchover can be triggered to ensure the normal running of services.

**Figure 1** Configuring PPPoE dual-stack user access (ND unshared+PD) in a dual-device hot backup scenario with distributed CGN and EDSG service configured  
![](figure/en-us_image_0000001360795709.png)

**Table 1** Interfaces and IP addresses
| **Device** | **Interface Name** | **Interface Number** | **IP Address** |
| --- | --- | --- | --- |
| BRAS1 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.129/29 |
| interface2 | GE0/1/0 | 10.2.1.1/24, 2001:db8:8::7/128 |
| interface3 | Eth-trunk4 | - |
| interface3 | Eth-trunk4.1 | 192.168.5.97/29 |
| - | Loopback1 | 10.2.2.2/24, 2001:db8::2:2/64 |
| - | Loopback2 | 10.3.3.3/24 |
| BRAS2 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.130/29 |
| interface2 | GE0/1/0 | 10.4.1.1/24, 2001:db8:9::7/128 |
| interface3 | Eth-trunk4 | - |
| interface3 | Eth-trunk4.1 | 192.168.5.98/29 |
| - | Loopback1 | 10.4.4.4/24, 2001:db8::3:3/64 |
| - | Loopback2 | 10.13.13.13/24 |

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure a routing protocol.
3. Configure AAA schemes.
4. Configure RADIUS.
5. Configure address pools.
6. Configure a domain.
7. Configure a BAS interface.
8. Configure a BFD session and VRRP on the access side of the master and backup BRASs.
9. Configure an RBS and an RBP.
10. Configure the EDSG service.
11. Configure the distributed CGN service.
12. Enable the function to advertise public routes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of BRAS2 is similar to the configuration of BRAS1. The following uses the configuration on BRAS1 as an example. For configuration details on BRAS2, see the BRAS2 configuration file.




#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (such as the VRRP ID and preemption delay)
* BFD parameters (such as the local and remote discriminators of a BFD session and the expected minimum intervals at which BFD Control packets are sent and received)

* IP addresses of interfaces on BRAS1 and BRAS2.
* User access parameters
* CGN service parameters
* EDSG service parameters
* User authentication mode (RADIUS authentication)

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure IP addresses for network-side interfaces.
   
   
   
   ```
   [~BRAS1] interface gigabitEthernet 0/1/0
   [*BRAS1-GigabitEthernet0/1/0] ipv6 enable 
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address 2001:db8:8::7 128
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1-GigabitEthernet0/1/0] commit
   [*BRAS1] interface Loopback1
   [*BRAS1-Loopback1] ipv6 enable
   [*BRAS1-Loopback1] ipv6 address 2001:db8::2:2 64
   [*BRAS1-Loopback1] ipv6 address auto link-local
   [*BRAS1-Loopback1] ip address 10.2.2.2 24
   [*BRAS1-Loopback1] quit
   [*BRAS1] commit
   ```
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS1] interface loopback2
   [*BRAS1-Loopback2] ip address 10.3.3.3 24
   [*BRAS1-Loopback2] quit
   [*BRAS1] commit
   ```
2. Configure a routing protocol.
   
   
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~BRAS1] peer-backup route-cost auto-advertising
   [*BRAS1] commit
   ```
   
   # Configure MPLS.
   
   ```
   [~BRAS1] mpls
   [~BRAS1-mpls] mpls ldp
   [~BRAS1-mpls] quit
   [~BRAS1] mpls lsr-id 10.3.3.3
   [*BRAS1] interface GigabitEthernet0/1/0
   [*BRAS1-GigabitEthernet0/1/0] mpls
   [*BRAS1-GigabitEthernet0/1/0] mpls ldp
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1] commit
   ```
   
   # Configure OSPF to import UNRs.
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] default cost inherit-metric
   [*BRAS1-ospf-1] import-route unr
   [*BRAS1-ospf-1] area 0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] quit
   [*BRAS1-ospf-1] quit
   [*BRAS1] commit
   ```
3. Configure AAA schemes.
   
   
   
   # Configure authentication schemes and set the authentication mode to RADIUS and none, respectively.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*HUAWEI] commit
   [~BRAS1] aaa
   [~BRAS1-aaa] authentication-scheme auth1
   [*BRAS1-aaa-authen-auth1] authentication-mode radius
   [*BRAS1-aaa-authen-auth1] quit
   [*BRAS1-aaa] authentication-scheme none
   [*BRAS1-aaa-authen-auth1] authentication-mode none
   [*BRAS1-aaa-authen-auth1] quit
   [*BRAS1-aaa] commit
   ```
   
   # Configure an accounting scheme that uses the RADIUS accounting mode.
   
   ```
   [~BRAS1-aaa] accounting-scheme acct1
   [*BRAS1-aaa-accounting-acct1] accounting-mode radius
   [*BRAS1-aaa-accounting-acct1] quit
   [*BRAS1-aaa] commit
   [*BRAS1-aaa] quit
   ```
4. Configure RADIUS.
   
   
   
   # Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
   
   ```
   [~BRAS1] radius local-ip all
   [*BRAS1] commit
   ```
   
   # Configure a RADIUS server group.
   
   
   
   ```
   [~BRAS1] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*BRAS1-radius-rd1] radius-server source interface Loopback1
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] radius-server calling-station-id include mac
   [~BRAS1-radius-rd1] radius-server user-name original
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] radius-server class-as-car
   [*BRAS1-radius-rd1] quit
   [*BRAS1] commit
   ```
   
   
   
   # Configure a RADIUS authorization server.
   
   ```
   [~BRAS1] radius-server authorization 192.168.8.249 shared-key-cipher YsHsjx_202206 server-group rd1
   [*BRAS1] commit
   ```
5. Configure address pools.
   
   
   
   # Configure a user-side local IPv4 address pool.
   
   ```
   [~BRAS1] ip pool pool_v4 bas local
   [*BRAS1-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0
   [*BRAS1-ip-pool-pool_v4] commit
   [~BRAS1-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   [~BRAS1-ip-pool-pool_v4] dns-server 10.179.155.161 10.179.155.177
   [*BRAS1-ip-pool-pool_v4] quit
   [*BRAS1] commit
   ```
   
   # Configure an IPv6 address pool.
   
   ```
   [~BRAS1] ipv6 prefix pre_nd_1 delegation
   [*BRAS1-ipv6-prefix-pre_nd_1] prefix 2001:db8:1::/48
   [*BRAS1-ipv6-prefix-pre_nd_1] slaac-unshare-only
   [*BRAS1-ipv6-prefix-pre_nd_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_nd_1 bas delegation
   [*BRAS1-ipv6-pool-pool_nd_1] prefix pre_nd_1
   [*BRAS1-ipv6-pool-pool_nd_1] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_nd_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_pd_1 delegation
   [*BRAS1-ipv6-prefix-pre_pd_1] prefix 2001:db8:2::/48
   [*BRAS1-ipv6-prefix-pre_pd_1] commit
   [~BRAS1-ipv6-prefix-pre_pd_1] pd-unshare-only
   [~BRAS1-ipv6-prefix-pre_pd_1] quit
   [~BRAS1] ipv6 pool pool_pd_1 bas delegation
   [*BRAS1-ipv6-pool-pool_pd_1] prefix pre_pd_1
   [*BRAS1-ipv6-pool-pool_pd_1] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_pd_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_nd_2 delegation
   [*BRAS1-ipv6-prefix-pre_nd_2] prefix 2001:db8:3::/48
   [*BRAS1-ipv6-prefix-pre_nd_2] slaac-unshare-only
   [*BRAS1-ipv6-prefix-pre_nd_2] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_nd_2 bas delegation rui-slave
   [*BRAS1-ipv6-pool-pool_nd_2] prefix pre_nd_2
   [*BRAS1-ipv6-pool-pool_nd_2] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_nd_2] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_pd_2 delegation 
   [*BRAS1-ipv6-prefix-pre_pd_2] prefix 2001:db8:4::/48
   [*BRAS1-ipv6-prefix-pre_pd_2] commit
   [~BRAS1-ipv6-prefix-pre_pd_2] pd-unshare-only
   [~BRAS1-ipv6-prefix-pre_pd_2] quit
   [~BRAS1] ipv6 pool pool_pd_2 bas delegation rui-slave
   [*BRAS1-ipv6-pool-pool_pd_2] prefix pre_pd_2 
   [*BRAS1-ipv6-pool-pool_pd_2] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_pd_2] quit
   [*BRAS1] commit
   ```
   
   # Configure the DHCPv6 device to generate a DUID in DUID-LLT mode. (This step is not required if a DUID has been configured on BRAS1.)
   
   
   
   ```
   [~BRAS1] dhcpv6 duid llt
   [*BRAS1] commit
   ```
6. Configure a domain.
   
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain isp1
   [*BRAS1-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS1-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS1-aaa-domain-isp1] radius-server group rd1
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] prefix-assign-mode unshared  
   [~BRAS1-aaa-domain-isp1] ip-pool pool_v4
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_nd_1
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_pd_1
   [~BRAS1-aaa-domain-isp1] accounting-start-delay 10 online user-type ppp
   [*BRAS1-aaa-domain-isp1] accounting-start-delay traffic-forward before-start-accounting
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] user-basic-service-ip-type ipv4
   [~BRAS1-aaa-domain-isp1] quit
   [~BRAS1-aaa] quit
   ```
7. Configure a BAS interface.
   
   
   
   # Configure a VT.
   
   ```
   [~BRAS1] interface virtual-template 5
   [*BRAS1-virtual-template5] ppp authentication-mode chap
   [*BRAS1-virtual-template5] quit
   [*BRAS1] commit
   ```
   
   # Configure the Eth-Trunk interface to work in static LACP mode and set a timeout period for the interface to receive LACPDUs.
   
   ```
   [~BRAS1] interface Eth-Trunk2
   [*BRAS1-Eth-Trunk2] mode lacp-static
   [*BRAS1-Eth-Trunk2] lacp timeout fast
   [*BRAS1-Eth-Trunk2] commit
   ```
   
   # Enable the IPv6 function on the interface and specify the VT.
   
   ```
   [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.10
   [*BRAS1-Eth-Trunk2.10] ipv6 enable
   [*BRAS1-Eth-Trunk2.10] ipv6 address auto link-local
   [*BRAS1-Eth-Trunk2.10] pppoe-server bind virtual-template 5
   [*BRAS1-Eth-Trunk2.10] commit
   [~BRAS1-Eth-Trunk2.10] user-vlan 1000 4000 qinq 2000 2001
   [~BRAS1-Eth-Trunk2.10-user-vlan-1000-4000-qinq-2000-2001] quit
   ```
   
   # Configure BAS interfaces.
   
   ```
   [~BRAS1-Eth-Trunk2.1] bas
   [~BRAS1-Eth-Trunk2.1-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS1-Eth-Trunk2.1-bas] client-option82 basinfo-insert cn-telecom
   [*BRAS1-Eth-Trunk2.1-bas] commit
   [~BRAS1-Eth-Trunk2.1-bas] quit
   [~BRAS1-Eth-Trunk2.1] quit
   ```
   
   # Configure the network-side interfaces.
8. Configure a BFD session and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
   # Configure a BFD session on the access side to allow the device to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
   
   ```
   [~BRAS1] bfd
   [*BRAS1-bfd] quit
   [*BRAS1] bfd bfd bind peer-ip 192.168.4.130
   [*BRAS1-bfd-session-bfd1] discriminator local 1
   [*BRAS1-bfd-session-bfd1] discriminator remote 1
   [*BRAS1-bfd-session-bfd1] quit 
   [*BRAS1] commit
   ```
   
   # Configure a VRRP group on an interface/sub-interface (sub-interface Eth-Trunk2.1 is used in this example), and configure VRRP to track the BFD session and network-side interface. Set the VRRP status recovery delay to 300s.
   
   ```
   [~BRAS1] interface Eth-Trunk2.1              
   [*BRAS1-Eth-Trunk2.1] vlan-type dot1q 96                           
   [*BRAS1-Eth-Trunk2.1] ip address 192.168.4.129 255.255.255.248            
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 virtual-ip 192.168.4.131
   [*BRAS1-Eth-Trunk2.1] admin-vrrp vrid 5              
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 priority 120 
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 preempt-mode timer delay 1800 
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track interface GigabitEthernet 0/1/0 reduced 50 
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track bfd-session session-name bfd1 link
   [*BRAS1-Eth-Trunk2.1] commit
   [~BRAS1-Eth-Trunk2.1] quit
   [~BRAS1] vrrp recover-delay 300
   [*BRAS1] commit
   ```
9. Configure an RBS and an RBP.
   
   
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] peer 10.13.13.13 source 10.3.3.3 port 6001
   [*BRAS1-rm-backup-srv-s1] track interface GigabitEthernet 0/1/0
   [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
   [*BRAS1-rm-backup-srv-s1] ip-pool pool_v4 metric 10
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_nd_1 metric 10
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_pd_1 metric 10
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_nd_2 metric 20
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_pd_2 metric 20
   [*BRAS1-rm-backup-srv-s1] radius-authorization source same-as nas-logic-ip
   [*BRAS1-rm-backup-srv-s1] quit
   [*BRAS1] commit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS1] remote-backup-profile p1
   [*BRAS1-rm-backup-prf-p1] service-type bras
   [*BRAS1-rm-backup-prf-p1] peer-backup hot
   [*BRAS1-rm-backup-prf-p1] backup-id 5 remote-backup-service s1
   [*BRAS1-rm-backup-prf-p1] vrrp-id 5 interface Eth-Trunk2.1
   [*BRAS1-rm-backup-prf-p1] nas logic-port Eth-Trunk2 
   [*BRAS1-rm-backup-prf-p1] nas logic-ip 10.10.1.1
   [*BRAS1-rm-backup-prf-p1] nas logic-sysname huawei
   [*BRAS1-rm-backup-prf-p1] quit
   [*BRAS1] commit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface Eth-Trunk2.10
   [*BRAS1-Eth-Trunk2.10] remote-backup-profile p1
   [*BRAS1-Eth-Trunk2.10] quit
   [*BRAS1] commit
   ```
10. Configure the EDSG service.
    
    
    
    # Enable the value-added service function.
    
    ```
    [~BRAS1] value-added-service enable
    [*BRAS1] commit
    ```
    
    # Configure the HW-Policy-Name attribute to support EDSG service delivery.
    
    ```
    [~BRAS1] radius-attribute hw-policy-name support-type edsg
    [*BRAS1] commit
    ```
    
    # Configure an EDSG traffic policy.
    
    1. Create a service group.
       ```
       [~BRAS1] service-group edsg
       [*BRAS1] commit
       ```
    2. Configure ACL rules for the service group.
       ```
       [~BRAS1] acl number 6100
       [*BRAS1-acl4-basic-6100] description edsg
       [*BRAS1-acl4-basic-6100] rule 5 permit ip source service-group edsg destination ip-address 192.168.100.0 0.0.0.255
       [*BRAS1-acl4-basic-6100] rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group edsg
       [*BRAS1-acl4-basic-6100] quit
       [*BRAS1] commit
       [~BRAS1] acl ipv6 number 6100
       [*BRAS1-acl6-basic-6100] rule 5 permit ipv6 source service-group edsg destination ipv6-address 2001:db8::3:2/32
       [*BRAS1-acl6-basic-6100] rule 10 permit ipv6 source ipv6-address 2001:db8::3:2/32 destination service-group edsg
       [*BRAS1-acl6-basic-6100] quit
       [*BRAS1] commit
       ```
    3. Configure a traffic classifier.
       ```
       [~BRAS1] traffic classifier edsg-c1
       [*BRAS1-classifier-edsg-c1] if-match acl 6100
       [*BRAS1-classifier-edsg-c1] if-match ipv6 acl 6100
       [*BRAS1-classifier-edsg-c1] quit
       [*BRAS1] commit
       ```
    4. Configure a traffic behavior.
       ```
       [~BRAS1] traffic behavior edsg-b1
       [*BRAS1-edsg-b1] quit
       [*BRAS1] commit
       ```
    5. Configure a traffic policy.
       ```
       [~BRAS1] traffic policy p1
       [*BRAS1-traffic-policy-p1] classifier edsg-c1 behavior edsg-b1 precedence 1
       [*BRAS1-traffic-policy-p1] quit
       [*BRAS1] commit
       ```
    6. Apply the EDSG traffic policy globally.
       ```
       [~BRAS1] traffic-policy p1 inbound
       [*BRAS1] traffic-policy p1 outbound
       [*BRAS1] commit
       ```
    
    # Configure an EDSG service policy.
    
    ```
    [~BRAS1] service-policy name service_edsg1 edsg
    [*BRAS1-service-policy-service_edsg1] commit
    [~BRAS1-service-policy-service_edsg1] radius-server group rd1
    [~BRAS1-service-policy-service_edsg1] authentication-scheme none
    [*BRAS1-service-policy-service_edsg1] accounting-scheme acct1
    [*BRAS1-service-policy-service_edsg1] service-group edsg
    [*BRAS1-service-policy-service_edsg1] rate-limit cir 100000 pir 100000 inbound
    [*BRAS1-service-policy-service_edsg1] rate-limit cir 100000 pir 100000 outbound
    [*BRAS1-service-policy-service_edsg1] quit
    [*BRAS1-service-policy-service_edsg1] commit
    ```
11. Configure the distributed CGN service.
    
    
    
    # Set the session table sizes of the CPUs on the NAT service boards in slots 3 and 2 to 16M.
    
    ```
    [~BRAS1] license
    [*BRAS1-license] active nat session-table size 16 slot 3 engine 0
    [*BRAS1-license] active nat session-table size 16 slot 2 engine 0
    [*BRAS1-license] active nat bandwidth-enhance slot 3 engine 0
    [*BRAS1-license] active nat bandwidth-enhance slot 2 engine 0
    [*BRAS1-license] quit
    [*BRAS1] commit
    ```
    
    # Create service-location group 1 and bind it to service boards.
    
    ```
    [~BRAS1] service-location 1
    [*BRAS1-service-location-1] location slot 3 engine 0
    [*BRAS1-service-location-1] remote-backup interface Eth-Trunk4.1 peer 192.168.5.98
    [*BRAS1-service-location-1] vrrp vrid 101 interface Eth-Trunk4.1
    [*BRAS1-service-location-1] quit
    [*BRAS1] commit
    ```
    
    # Create service-location group 2 and bind it to service boards.
    
    ```
    [~BRAS1] service-location 2
    [*BRAS1-service-location-2] location slot 2 engine 0 
    [*BRAS1-service-location-2] remote-backup interface Eth-Trunk4.1 peer 192.168.5.98
    [*BRAS1-service-location-2] vrrp vrid 101 interface Eth-Trunk4.1
    [*BRAS1-service-location-2] quit
    [*BRAS1] commit
    ```
    
    # Configure VRRP group 5 to monitor the service-location groups.
    
    ```
    [~BRAS1] interface Eth-Trunk2.1   
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track service-location 1 reduced  50
    [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track service-location 2 reduced  50
    [~BRAS1-Eth-Trunk2.1] quit
    [*BRAS1] commit
    ```
    
    # Create VRRP group 101 on Eth-Trunk 4.1, set the virtual IP address of the VRRP group to 192.168.5.99, configure the VRRP group as an mVRRP group, set BRAS1's priority in the VRRP group to 120, and set the VRRP preemption delay to 1800s.
    
    ```
    [~BRAS1] interface Eth-Trunk4.1
    [~BRAS1-Eth-Trunk4.1] vlan-type dot1q 101
    [~BRAS1-Eth-Trunk4.1] ip address 192.168.5.97 255.255.255.248
    [~BRAS1-Eth-Trunk4.1] vrrp vrid 101 virtual-ip 192.168.5.99
    [*BRAS1-Eth-Trunk4.1] admin-vrrp vrid 101 ignore-if-down
    [*BRAS1-Eth-Trunk4.1] vrrp vrid 101 priority 120
    [*BRAS1-Eth-Trunk4.1] vrrp vrid 101 preempt-mode timer delay 1800 
    [*BRAS1-Eth-Trunk4.1] vrrp vrid 101 track interface GigabitEthernet 0/1/0 reduced 50
    [*BRAS1-Eth-Trunk4.1] vrrp vrid 101 track service-location 1 reduced  50
    [*BRAS1-Eth-Trunk4.1] vrrp vrid 101 track service-location 2 reduced  50
    [*BRAS1-Eth-Trunk4.1] quit
    [*BRAS1] commit
    ```
    
    # Create service-instance groups and bind each to a created service-location group.
    
    ```
    [~BRAS1] service-instance-group nat444-group1
    [*BRAS1-service-instance-group-nat444-1] service-location 1
    [*BRAS1-service-instance-group-nat444-1] remote-backup-service s1
    [*BRAS1-service-instance-group-nat444-1] quit
    [*BRAS1-service-instance-group-nat444-1] commit
    [~BRAS1] service-instance-group nat444-group2
    [*BRAS1-service-instance-group-nat444-2] service-location 2
    [*BRAS1-service-instance-group-nat444-2] remote-backup-service s1
    [*BRAS1-service-instance-group-nat444-2] quit
    [*BRAS1-service-instance-group-nat444-2] commit
    ```
    
    # Create a NAT instance named **nat444-1**, bind service-instance group **nat444-group1** to it to specify the corresponding service board resources, and configure a port range.
    
    ```
    [~BRAS1] nat instance nat444-1 id 1
    [*BRAS1-nat-instance-nat444-1] service-instance-group nat444-group1
    [*BRAS1-nat-instance-nat444-1] port-range 4096 
    ```
    
    # Configure public addresses.
    
    ```
    [*BRAS1-nat-instance-nat444-1] nat address-group pppoe-public-1 group-id 1
    [*BRAS1-nat-instance-nat444-1-nat-address-group-pppoe-public-1] section 0 10.1.1.0 mask 24
    [*BRAS1-nat-instance-nat444-1-nat-address-group-pppoe-public-1] section 1 10.3.1.0 mask 24
    [*BRAS1-nat-instance-nat444-1-nat-address-group-pppoe-public-1] quit
    ```
    
    # Enable ALG for all protocols and configure the 3-tuple mode.
    
    ```
    [*BRAS1-nat-instance-nat444-1] nat alg all
    [*BRAS1-nat-instance-nat444-1] nat filter mode full-cone
    [*BRAS1-nat-instance-nat444-1] quit
    [*BRAS1] commit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Create a NAT instance named **nat444-2** and bind service-instance group named **nat444-group2** to it. The remaining configuration procedure is the same as that of NAT instance **nat444-1**, and is omitted here.
    
    # Configure user groups from which the users go online.
    
    ```
    [~BRAS1] user-group pppoe-nat-1
    [*BRAS1] user-group pppoe-nat-2
    [*BRAS1] commit
    ```
    
    # Bind the NAT instances to the user groups in the AAA domain.
    
    ```
    [~BRAS1] aaa
    [~BRAS1-aaa] domain isp1
    [~BRAS1-aaa-domain-isp1] user-group pppoe-nat-1 bind nat instance nat444-1
    [*BRAS1-aaa-domain-isp1] user-group pppoe-nat-2 bind nat instance nat444-2
    [*BRAS1-aaa-domain-isp1] quit
    [*BRAS1-aaa] quit
    [*BRAS1] commit
    ```
    
    # Configure a NAT traffic diversion policy.
    
    1. Define ACL rules for specified user groups.
       ```
       [~BRAS1] acl number 6000
       [*BRAS1-acl4-basic-6000] description for_pppoe-nat-1
       [*BRAS1-acl4-basic-6000] rule 5 permit ip source user-group pppoe-nat-1
       [*BRAS1-acl4-basic-6000] quit
       [*BRAS1] commit
       [~BRAS1] acl number 6001
       [*BRAS1-acl4-basic-6001] description for_pppoe-nat-2
       [*BRAS1-acl4-basic-6001] rule 5 permit ip source user-group pppoe-nat-2
       [*BRAS1-acl4-basic-6001] quit
       [*BRAS1] commit
       [~BRAS1] acl number 6002
       [*BRAS1-acl4-basic-6002] description for_pppoe-no-nat
       [*BRAS1-acl4-basic-6002] rule 5 permit ip source user-group pppoe-nat-2 destination ip-address 192.168.200.0 0.0.0.255
       [*BRAS1-acl4-basic-6002] rule 10 permit ip source user-group pppoe-nat-2 destination ip-address 10.168.200.0 0.0.0.255
       [*BRAS1-acl4-basic-6002] quit
       [*BRAS1] commit
       ```
    2. Configure traffic classifiers.
       ```
       [~BRAS1] traffic classifier nat-c1
       [*BRAS1-classifier-nat-c1] if-match acl 6000
       [[*BRAS1-classifier-nat-c1] quit
       [*BRAS1] commit
       [~BRAS1] traffic classifier nat-c2
       [*BRAS1-classifier-nat-c2] if-match acl 6001
       [*BRAS1-classifier-nat-c2] quit
       [*BRAS1] commit
       [~BRAS1] traffic classifier no-nat
       [*BRAS1-classifier-no-nat] if-match acl 6002
       [*BRAS1-classifier-no-nat] quit
       [*BRAS1] commit
       ```
    3. Configure traffic behaviors.
       ```
       [~BRAS1] traffic behavior nat-b1
       [*BRAS1-nat-b1] nat bind instance nat444-1
       [*BRAS1-nat-b1] quit
       [*BRAS1] commit
       [~BRAS1] traffic behavior nat-b2
       [*BRAS1-nat-b2] nat bind instance nat444-2
       [*BRAS1-nat-b2] quit
       [*BRAS1] commit
       [~BRAS1] traffic behavior no-nat
       [*BRAS1-no-nat] quit
       [*BRAS1] commit
       ```
    4. Configure a traffic policy.
       ```
       [~BRAS1] traffic policy p1
       [~BRAS1-traffic-policy-p1] classifier no-nat behavior no-nat precedence 2
       [*BRAS1-traffic-policy-p1] classifier nat-c1 behavior nat-b1 precedence 3
       [*BRAS1-traffic-policy-p1] classifier nat-c2 behavior nat-b2 precedence 4
       [*BRAS1-traffic-policy-p1] quit
       [*BRAS1] commit
       ```
    5. Apply the NAT traffic policy in the inbound direction.
       ```
       [~BRAS1] traffic-policy p1 inbound
       [*BRAS1] commit
       ```
    
    
    
    # Configure a NAT conversion policy.
    
    1. Configures an ACL rule.
       ```
       [~BRAS1] acl number 3000
       [*BRAS1-acl4-basic-3000] description for_nat-source
       [*BRAS1-acl4-basic-3000] rule 5 permit ip source 172.16.0.0 255.255.255.0
       [*BRAS1-acl4-basic-3000] quit
       [*BRAS1] commit
       ```
    2. Configure a NAT conversion policy to perform NAT for user traffic.
       ```
       [~BRAS1] nat instance nat444-1
       [~BRAS1-nat-instance-nat444-1] nat outbound 3000 address-group pppoe-public-1
       [~BRAS1-nat-instance-nat444-1] quit 
       [*BRAS1] commit
       [~BRAS1] nat instance nat444-2
       [~BRAS1-nat-instance-nat444-2] nat outbound 3000 address-group pppoe-public-2
       [~BRAS1-nat-instance-nat444-2] quit 
       [*BRAS1] commit
       ```
12. Enable the function to advertise public routes.
    
    
    ```
    [~BRAS1] bgp 65008
    [~BRAS1-bgp] ipv4-family unicast
    [~BRAS1-bg-af-ipv4] network 0 10.1.1.0 255.255.255.0
    [~BRAS1-bg-af-ipv4] network 0 10.3.1.0 255.255.255.0
    [~BRAS1-bg-af-ipv4] quit
    [~BRAS1-bg] quit
    [~BRAS1] commit
    ```

#### Configuration Files

* BRAS1 configuration file

```
#
sysname BRAS1
#
vrrp recover-delay 300
# 
license  
 active nat session-table size 16 slot 3 engine 0  
 active nat session-table size 16 slot 2 engine 0  
 active nat bandwidth-enhance slot 3 engine 0
 active nat bandwidth-enhance slot 2 engine 0
#
radius local-ip all
#
radius-attribute hw-policy-name support-type edsg
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% 
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server class-as-car
 radius-server source interface LoopBack1                                                     
 radius-server calling-station-id include mac                                   
 radius-server user-name original                                               
# 
radius-server authorization 192.168.8.249 shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% server-group rd1
#
user-group pppoe-nat-1 
user-group pppoe-nat-2
#
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_nd_1 delegation                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_1 bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd_1                                                                 
#                                                                               
ipv6 prefix pre_pd_1 delegation                                                   
 prefix 2001:DB8:2::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd_1 bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd_1
#                                                                               
ipv6 prefix pre_nd_2 delegation                                                   
 prefix 2001:DB8:3::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_2 bas delegation rui-slave                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd_2                                                                  
#                                                                               
ipv6 prefix pre_pd_2 delegation                                                   
 prefix 2001:DB8:4::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd_2 bas delegation rui-slave                                              
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd_2 
#
remote-backup-service s1
 peer 10.13.13.13 source 10.3.3.3 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
 ip-pool pool_v4 metric 10
 ipv6-pool pool_nd_1 metric 10
 ipv6-pool pool_pd_1 metric 10
 ipv6-pool pool_nd_2 metric 20
 ipv6-pool pool_pd_2 metric 20
 radius-authorization source same-as nas-logic-ip
#
remote-backup-profile p1
 service-type bras
 backup-id 5 remote-backup-service s1
 peer-backup hot
 vrrp-id 5 interface Eth-Trunk2.1
 nas logic-port Eth-Trunk2 
 nas logic-ip 10.10.1.1
 nas logic-sysname huawei
#
bfd
#
bfd bfd bind peer-ip 192.168.4.130
 discriminator local 1 
 discriminator remote 1
#
mpls lsr-id 10.3.3.3
#
mpls
#
mpls ldp
#
acl number 3000                                                                 
 description for_nat-source                                                               
 rule 5 permit ip source 172.16.0.0 255.255.255.0 
#
service-location 1  
 location slot 3 engine 0
 remote-backup interface Eth-Trunk4.1 peer 192.168.5.98
 vrrp vrid 101 interface Eth-Trunk4.1 
# 
service-location 2  
 location slot 2 engine 0 backup slot 3 engine 0
 remote-backup interface Eth-Trunk4.1 peer 192.168.5.98
 vrrp vrid 101 interface Eth-Trunk4.1 
# 
service-instance-group nat444-group1  
 service-location 1
 remote-backup-service s1
#
service-instance-group nat444-group2  
 service-location 2
 remote-backup-service s1 
# 
nat instance nat444-1 id 1  
 service-instance-group nat444-group1  
 port-range 4096  
 nat address-group pppoe-public-1 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-1  
 nat alg all  
 nat filter mode full-cone 
#
nat instance nat444-2 id 1  
 service-instance-group nat444-group2  
 port-range 4096  
 nat address-group pppoe-public-2 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-2  
 nat alg all  
 nat filter mode full-cone 
# 
aaa
 #
 authentication-scheme auth1
 #
 authentication-scheme none
  authentication-scheme none
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1                                                     
  prefix-assign-mode unshared                                                   
  ip-pool pool_v4                                                               
  ipv6-pool pool_nd_1                                                            
  ipv6-pool pool_pd_1
  user-group pppoe-nat-1 bind nat instance nat444-1
  user-group pppoe-nat-2 bind nat instance nat444-2
  accounting-start-delay 10 online user-type ppp  
  accounting-start-delay traffic-forward before-start-accounting                
  user-basic-service-ip-type ipv4                                               
#
value-added-service enable
#
service-group edsg
#                                                                               
acl number 6100                                                                 
 description edsg                                                               
 rule 5 permit ip source service-group edsg destination ip-address 192.168.100.0 0.0.0.255 
 rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group edsg
#                                                                                
acl ipv6 number 6100                                                            
 rule 5 permit ipv6 source service-group edsg destination ipv6-address 2001:DB8::3:2/32  
 rule 10 permit ipv6 source ipv6-address 2001:DB8::3:2/32 destination service-group edsg 
#
acl number 6000                                                                 
 description for_pppoe-nat-1                                                               
 rule 5 permit ip source user-group pppoe-nat-1 
#
acl number 6001                                                                 
 description for_pppoe-nat-2                                                               
 rule 5 permit ip source user-group pppoe-nat-2
#
acl number 6002                                                                 
 description for_pppoe-no-nat                                                             
 rule 5 permit ip source user-group pppoe-nat-2 destination ip-address 192.168.200.0 0.0.0.255
 rule 10 permit ip source user-group pppoe-nat-2 destination ip-address 10.168.200.0 0.0.0.255
#
dhcpv6 duid 00010001280ef7a400e0fc904b50
#                                                                               
traffic classifier edsg-c1 operator or                                          
 if-match acl 6100 precedence 1                                                 
 if-match ipv6 acl 6100 precedence 2                                            
#
traffic classifier nat-c1 operator or                                          
 if-match acl 6000                                                                                  
# 
traffic classifier nat-c2 operator or                                          
 if-match acl 6001                                                                                  
# 
traffic classifier no-nat operator or                                          
 if-match acl 6002                                                                                  
# 
traffic behavior edsg-b1
#
traffic behavior nat-b1
 nat bind instance nat444-1
#
traffic behavior nat-b2
 nat bind instance nat444-2
# 
traffic behavior no-nat
# 
traffic policy p1                                                               
 share-mode                                                                     
 classifier edsg-c1 behavior edsg-b1 precedence 1
 classifier no-nat behavior no-nat precedence 2
 classifier nat-c1 behavior nat-b1 precedence 3
 classifier nat-c2 behavior nat-b2 precedence 4
#                                                                              
service-policy name service_edsg1 edsg                                          
 authentication-scheme none  
 accounting-scheme acct1                                                 
 radius-server group rd1   
 service-group edsg                                                
 rate-limit cir 100000 pir 100000 inbound                                       
 rate-limit cir 100000 pir 100000 outbound                                      
#     
interface Virtual-Template5
 ppp authentication-mode chap
#
interface LoopBack1
 ipv6 enable
 ip address 10.2.2.2 255.255.255.0
 ipv6 address 2001:DB8::2:2/64
 ipv6 address auto link-local
#
interface LoopBack2
 ip address 10.3.3.3 255.255.255.0
#
interface Eth-Trunk2
 mode lacp-static                                                               
 lacp timeout fast                                                              
#
interface  Eth-Trunk2.1
 vlan-type dot1q 96
 ip address 192.168.4.129 255.255.255.248
 vrrp vrid 5 virtual-ip 192.168.4.131
 admin-vrrp vrid 5
 vrrp vrid 5 priority 120
 vrrp vrid 5 preempt-mode timer delay 1800
 vrrp vrid 5 track interface GigabitEthernet0/1/0 reduced 50
 vrrp vrid 5 track bfd-session session-name bfd1 link
 vrrp vrid 5 track service-location 1 reduced 50
 vrrp vrid 5 track service-location 2 reduced 50
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                   
 statistic enable                                                               
 user-vlan 1000 4000 qinq 2000 2001
 remote-backup-profile p1
 pppoe-server bind Virtual-Template 5                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  client-option82 basinfo-insert cn-telecom  
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.2.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:8::7/128                                                 
 ipv6 address auto link-local
 mpls
 mpls ldp
#
interface Eth-Trunk4.1
 vlan-type dot1q 101
 ip address 192.168.5.97 255.255.255.248
 vrrp vrid 101 virtual-ip 192.168.5.99
 admin-vrrp vrid 101 ignore-if-down
 vrrp vrid 101 priority 120
 vrrp vrid 101 preempt-mode timer delay 1800
 vrrp vrid 101 track interface GigabitEthernet0/1/0 reduced 50
 vrrp vrid 101 track service-location 1 reduced 50
 vrrp vrid 101 track service-location 2 reduced 50
#
traffic-policy p1 inbound
traffic-policy p1 outbound
#
peer-backup route-cost auto-advertising
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.2.1.0 0.0.0.255
  network 10.3.3.3 0.0.0.0
#
bgp 65008 
 #  
  ipv4-family unicast     
  network 0 10.1.1.0 255.255.255.0   
  network 0 10.3.1.0 255.255.255.0   
#
return
```

* BRAS2 configuration file

```
#
sysname BRAS2
#
vrrp recover-delay 300
# 
license  
 active nat session-table size 16 slot 3 engine 0  
 active nat session-table size 16 slot 2 engine 0  
 active nat bandwidth-enhance slot 3 engine 0
 active nat bandwidth-enhance slot 2 engine 0
#
radius local-ip all
#
radius-attribute hw-policy-name support-type edsg
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% 
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server class-as-car
 radius-server source interface LoopBack1                                                     
 radius-server calling-station-id include mac                                   
 radius-server user-name original                                               
# 
radius-server authorization 192.168.8.249 shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% server-group rd1
#
user-group pppoe-nat-1 
user-group pppoe-nat-2
#
ip pool pool_v4 bas local rui-slave                                                      
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_nd_1 delegation                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_1 bas delegation rui-slave                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd_1                                                                  
#                                                                               
ipv6 prefix pre_pd_1 delegation                                                   
 prefix 2001:DB8:2::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd_1 bas delegation rui-slave                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd_1
#                                                                               
ipv6 prefix pre_nd_2 delegation                                                   
 prefix 2001:DB8:3::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd_2 bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd_2                                                                  
#                                                                               
ipv6 prefix pre_pd_2 delegation                                                   
 prefix 2001:DB8:4::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd_2 bas delegation                                               
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd_2 
#
remote-backup-service s1
 peer 10.3.3.3 source 10.13.13.13 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.3.3.3
 ip-pool pool_v4 metric 10
 ipv6-pool pool_nd_1 metric 20
 ipv6-pool pool_pd_1 metric 20
 ipv6-pool pool_nd_2 metric 10
 ipv6-pool pool_pd_2 metric 10
 radius-authorization source same-as nas-logic-ip
#
remote-backup-profile p1
 service-type bras
 backup-id 5 remote-backup-service s1
 peer-backup hot
 vrrp-id 5 interface Eth-Trunk2.1
 nas logic-port Eth-Trunk2 
 nas logic-ip 10.10.1.1
 nas logic-sysname huawei
#
bfd
#
bfd bfd bind peer-ip 192.168.4.129
 discriminator local 1 
 discriminator remote 1
#
#
mpls lsr-id 10.13.13.13
#
mpls
#
mpls ldp
#
acl number 3000                                                                 
 description for_nat-source                                                               
 rule 5 permit ip source 172.16.0.0 255.255.255.0 
#
service-location 1  
 location slot 3 engine 0
 remote-backup interface Eth-Trunk4.1 peer 192.168.5.97
 vrrp vrid 101 interface Eth-Trunk4.1 
# 
service-location 2  
 location slot 2 engine 0 backup slot 3 engine 0
 remote-backup interface Eth-Trunk4.1 peer 192.168.5.97
 vrrp vrid 101 interface Eth-Trunk4.1 
# 
service-instance-group nat444-group1  
 service-location 1
 remote-backup-service s1
#
service-instance-group nat444-group2  
 service-location 2
 remote-backup-service s1 
# 
nat instance nat444-1 id 1  
 service-instance-group nat444-group1  
 port-range 4096  
 nat address-group pppoe-public-1 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-1  
 nat alg all  
 nat filter mode full-cone 
#
nat instance nat444-2 id 1  
 service-instance-group nat444-group2  
 port-range 4096  
 nat address-group pppoe-public-2 group-id 1   
 section 0 10.1.1.0 mask 24
 section 1 10.3.1.0 mask 24  
 nat outbound 3000 address-group pppoe-public-2  
 nat alg all  
 nat filter mode full-cone 
# 
aaa
 #
 authentication-scheme auth1
 #
 authentication-scheme none
  authentication-scheme none
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1                                                     
  prefix-assign-mode unshared                                                   
  ip-pool pool_v4                                                               
  ipv6-pool pool_nd_2                                                             
  ipv6-pool pool_pd_2
  user-group pppoe-nat-1 bind nat instance nat444-1
  user-group pppoe-nat-2 bind nat instance nat444-2
  accounting-start-delay 10 online user-type ppp  
  accounting-start-delay traffic-forward before-start-accounting                
  user-basic-service-ip-type ipv4                                               
#  
value-added-service enable
#
service-group edsg
#                                                                               
acl number 6100                                                                 
 description edsg                                                               
 rule 5 permit ip source service-group edsg destination ip-address 192.168.100.0 0.0.0.255 
 rule 10 permit ip source ip-address 192.168.100.0 0.0.0.255 destination service-group edsg
#                                                                                
acl ipv6 number 6100                                                            
 rule 5 permit ipv6 source service-group edsg destination ipv6-address 2001:DB8::/32  
 rule 10 permit ipv6 source ipv6-address 2001:DB8::/32 destination service-group edsg 
#
acl number 6000                                                                 
 description for_pppoe-nat-1                                                               
 rule 5 permit ip source user-group pppoe-nat-1
#
acl number 6001                                                                 
 description for_pppoe-nat-2                                                               
 rule 5 permit ip source user-group pppoe-nat-2 
#
acl number 6002                                                                 
 description for_pppoe-no-nat                                                             
 rule 5 permit ip source user-group pppoe-nat-2 destination ip-address 192.168.200.0 0.0.0.255
 rule 10 permit ip source user-group pppoe-nat-2 destination ip-address 10.168.200.0 0.0.0.255  
#
dhcpv6 duid 00010001280ef7a400e0fc904b50
#                                                                               
traffic classifier edsg-c1 operator or                                          
 if-match acl 6100 precedence 1                                                 
 if-match ipv6 acl 6100 precedence 2                                            
#
traffic classifier nat-c1 operator or                                          
 if-match acl 6000                                                                                  
# 
traffic classifier nat-c2 operator or                                          
 if-match acl 6001                                                                                  
# 
traffic classifier no-nat operator or                                          
 if-match acl 6002                                                                                  
# 
traffic behavior edsg-b1
#
traffic behavior nat-b1
 nat bind instance nat444-1
#
traffic behavior nat-b2
 nat bind instance nat444-2
# 
traffic behavior no-nat
# 
traffic policy p1                                                               
 share-mode                                                                     
 classifier edsg-c1 behavior edsg-b1 precedence 1
 classifier no-nat behavior no-nat precedence 2
 classifier nat-c1 behavior nat-b1 precedence 3
 classifier nat-c2 behavior nat-b2 precedence 4
#                                                                              
service-policy name service_edsg1 edsg                                          
 authentication-scheme none  
 accounting-scheme acct1                                                 
 radius-server group rd1   
 service-group edsg                                                
 rate-limit cir 100000 pir 100000 inbound                                       
 rate-limit cir 100000 pir 100000 outbound                                      
#   
interface Virtual-Template5
 ppp authentication-mode chap
#
interface LoopBack1
 ipv6 enable
 ip address 10.4.4.4 255.255.255.0
 ipv6 address 2001:DB8::3:3/64
 ipv6 address auto link-local
#      
interface LoopBack2
 ip address 10.13.13.13 255.255.255.0
#  
interface Eth-Trunk2
 mode lacp-static                                                               
 lacp timeout fast                                                              
#
interface Eth-Trunk2.1
 vlan-type dot1q 96
 ip address 192.168.4.130 255.255.255.248
 vrrp vrid 5 virtual-ip 192.168.4.131
 admin-vrrp vrid 5
 vrrp vrid 5 priority 100
 vrrp vrid 5 track bfd-session session-name bfd1 peer
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                   
 statistic enable                                                               
 user-vlan 1000 4000 qinq 2000 2001
 remote-backup-profile p1
 pppoe-server bind Virtual-Template 5                                                
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  client-option82 basinfo-insert cn-telecom  
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.4.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:9::7/128                                                 
 ipv6 address auto link-local
 mpls
 mpls ldp
#
interface Eth-Trunk4.1
 vlan-type dot1q 101
 ip address 192.168.5.98 255.255.255.248
 vrrp vrid 101 virtual-ip 192.168.5.99
 admin-vrrp vrid 101 ignore-if-down
 vrrp vrid 101 priority 100
#
traffic-policy p1 inbound
traffic-policy p1 outbound
#
peer-backup route-cost auto-advertising
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.4.1.0 0.0.0.255
  network 10.13.13.13 0.0.0.0
#
bgp 65008 
 #  
  ipv4-family unicast     
  network 0 10.1.1.0 255.255.255.0   
  network 0 10.3.1.0 255.255.255.0   
#
return
```