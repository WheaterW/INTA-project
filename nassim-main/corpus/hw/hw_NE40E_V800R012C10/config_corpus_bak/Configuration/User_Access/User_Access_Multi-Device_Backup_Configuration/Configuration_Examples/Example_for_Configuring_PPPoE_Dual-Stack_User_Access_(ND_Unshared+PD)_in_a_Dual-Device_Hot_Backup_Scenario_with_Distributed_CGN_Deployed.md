Example for Configuring PPPoE Dual-Stack User Access (ND Unshared+PD) in a Dual-Device Hot Backup Scenario with Distributed CGN Deployed
========================================================================================================================================

Distributed CGN is deployed on the network to translate a large number of user addresses. In a distributed CGN+dual-device hot backup scenario, users access the master and backup BRASs in PPPoE+dual-stack mode. The BRASs assign IPv6 addresses to users in ND unshared+PD mode to implement user access.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001169340179__fig_dc_ne_cfg_rui_003101), user 1 and user 2 access BRAS1 and BRAS2 through SW1. RADIUS authentication and accounting are configured on the BRASs. The BRASs use a local address pool to assign IPv4 addresses to users, use DHCPv6 IA\_PD to assign the IPv6 prefixes to be used on the network to users, and use DHCPv6 ND to assign IPv6 addresses to users. To enable private network users to access the Internet, distributed CGN is deployed on the network to translate private addresses into public addresses. In addition, dual-device hot backup is deployed to improve network reliability. If a fault occurs, a master/backup switchover is triggered to ensure normal service running and prevent users from perceiving the fault.

**Figure 1** Configuring PPPoE dual-stack user access (ND unshared+PD) in a dual-device hot backup scenario with distributed CGN deployed![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 stand for GE0/1/0, GE0/2/0, and GE0/3/0, respectively.

![](figure/en-us_image_0000001172079321.png)


**Table 1** Interfaces and IP addresses
| **Device** | **Interface Name** | **Interface Number** | **IP Address** |
| --- | --- | --- | --- |
| BRAS1 | interface1 | GE0/1/0.1 | 192.168.1.1 |
| interface1 | GE0/1/0.2 | BAS interface |
| interface2 | GE0/2/0 | 10.0.0.1, 2001:db8:1:: /120 |
| interface3 | GE0/3/0 | 10.1.1.1 |
| - | Loopback1 | 10.2.2.2, 2001:db8:3::3 |
| - | Loopback2 | 10.3.3.3 |
| BRAS2 | interface1 | GE0/1/0.1 | 192.168.1.2 |
| interface1 | GE0/1/0.2 | BAS interface |
| interface2 | GE0/1/1 | 10.12.12.2, 2001:db8:2:: /120 |
| interface3 | GE0/1/2 | 10.1.1.2 |
| - | Loopback1 | 10.4.4.4, 2001:db8:4::4 |
| - | Loopback2 | 10.5.5.5 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure BFD sessions and VRRP on the access side of the master and backup BRASs.
3. Configure an RBS and an RBP.
4. Configure a routing protocol.
5. Configure address pools.
6. Configure AAA schemes.
7. Configure a RADIUS server group.
8. Configure a domain.
9. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
10. Configure a BAS interface.
11. Configure the CGN service.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of BRAS2 is similar to the configuration of BRAS1. The following uses the configuration on BRAS1 as an example. For configuration details on BRAS2, see the BRAS2 configuration file.



#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (such as the VRRP ID and preemption delay)
* BFD parameters (such as the local and remote discriminators of a BFD session and the expected minimum intervals at which BFD Control packets are sent and received)
* IP address of each interface on BRAS1 and BRAS2
* User access parameters
* CGN service parameters
* User authentication mode (RADIUS authentication)

#### Procedure

1. Configure IP addresses for interfaces. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
   # Configure a BFD session on the access side to allow the device to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*BRAS1] commit
   [~BRAS1] interface GigabitEthernet0/2/0
   [~BRAS1-GigabitEthernet0/2/0] ip address 10.11.11.1 24
   [*BRAS1-GigabitEthernet0/2/0] ipv6 enable
   [*BRAS1-GigabitEthernet0/2/0] ipv6 address 2001:db8:1:: 120
   [*BRAS1-GigabitEthernet0/2/0] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/2/0] commit
   [~BRAS1-GigabitEthernet0/2/0] quit
   [~BRAS1] interface LoopBack0
   [*BRAS1-LoopBack0] ipv6 enable
   [*BRAS1-LoopBack0] ipv6 address 2001:db8:3::3 128
   [*BRAS1-LoopBack0] ipv6 address auto link-local
   [*BRAS1-LoopBack0] ip address 10.2.2.2 32
   [*BRAS1-LoopBack0] commit
   [~BRAS1-LoopBack0] quit
   ```
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS1] interface LoopBack1
   [*BRAS1-LoopBack1] ip address 10.3.3.3 32
   [*BRAS1-LoopBack1] commit
   [~BRAS1-LoopBack1] quit
   ```
2. Configure BFD sessions and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
   # Configure a BFD session on the access side to allow the device to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
   
   ```
   [~BRAS1] bfd
   [*BRAS1-bfd] quit
   [*BRAS1] bfd bfd1 bind peer-ip 192.168.1.2
   [*BRAS1-bfd-session-bfd1] discriminator local 8
   [*BRAS1-bfd-session-bfd1] discriminator remote 6
   [*BRAS1-bfd-session-bfd1] commit
   [~BRAS1-bfd-session-bfd1] quit 
   ```
   
   # Configure a VRRP group on an interface (GE0/1/0.1 is used as an example), and configure VRRP to track the BFD session and network-side interface status.
   
   ```
   [~BRAS1] interface GigabitEthernet0/1/0.1
   [*BRAS1-GigabitEthernet0/1/0.1] commit
   [~BRAS1-GigabitEthernet0/1/0.1] vlan-type dot1q 400
   [*BRAS1-GigabitEthernet0/1/0.1] ip address 192.168.1.1 255.255.255.0
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 virtual-ip 192.168.1.100
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 priority 120
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 preempt-mode timer delay 60
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 track interface GigabitEthernet 0/2/0 reduced 50
   [*BRAS1-GigabitEthernet0/1/0.1] vrrp vrid 1 track bfd-session session-name bfd1 link
   [*BRAS1-GigabitEthernet0/1/0.1] commit
   [~BRAS1-GigabitEthernet0/1/0.1] quit
   [~BRAS1] vrrp recover-delay 60
   [*BRAS1] commit
   ```
3. Configure an RBS and an RBP.
   
   
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] peer 10.5.5.5 source 10.3.3.3 port 11000
   [*BRAS1-rm-backup-srv-s1] track interface GigabitEthernet 0/1/0
   [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.5.5.5
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS1] remote-backup-profile p1
   [*BRAS1-rm-backup-prf-p1] service-type bras
   [*BRAS1-rm-backup-prf-p1] peer-backup hot
   [*BRAS1-rm-backup-prf-p1] backup-id 1 remote-backup-service s1
   [*BRAS1-rm-backup-prf-p1] vrrp-id 1 interface GigabitEthernet 0/1/0.1
   [*BRAS1-rm-backup-prf-p1] commit
   [~BRAS1-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface GigabitEthernet 0/1/0.2
   [*BRAS1-GigabitEthernet0/1/0.2] remote-backup-profile p1
   [*BRAS1-GigabitEthernet0/1/0.2] commit
   [~BRAS1-GigabitEthernet0/1/0.2] quit
   ```
4. Configure a routing protocol.
   
   
   
   # Enable the function to automatically control a route's cost preference.
   
   ```
   [~BRAS1] peer-backup route-cost auto-advertising
   [*BRAS1] commit
   ```
   
   # Configure MPLS.
   
   ```
   [~BRAS1] mpls
   [*BRAS1-mpls] mpls ldp
   [*BRAS1-mpls-ldp] commit
   [~BRAS1-mpls-ldp] quit
   [~BRAS1] mpls lsr-id 10.3.3.3
   [*BRAS1] commit
   [~BRAS1] interface GigabitEthernet0/2/0
   [~BRAS1-GigabitEthernet0/2/0] mpls
   [*BRAS1-GigabitEthernet0/2/0] mpls ldp
   [*BRAS1-GigabitEthernet0/2/0] commit
   [~BRAS1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure OSPF to import UNRs.
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] default cost inherit-metric
   [*BRAS1-ospf-1] import-route unr
   [*BRAS1-ospf-1] area 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.11.11.0 0.0.0.255
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] commit
   [~BRAS1-ospf-1-area-0.0.0.0] quit
   [~BRAS1-ospf-1] quit
   ```
5. Configure address pools.
   
   
   
   # Configure the DHCP server.
   
   
   
   ```
   [~BRAS1] dhcp check-server-pkt loose include option 3
   [*BRAS1] dhcp-server group pppoe-v4
   [*BRAS1-dhcp-server-group-pppoe-v4] dhcp-server 10.111.1.1
   [*BRAS1-dhcp-server-group-pppoe-v4] dhcp-server source interface LoopBack0
   [*BRAS1-dhcp-server-group-pppoe-v4] undo release-agent
   [*BRAS1-dhcp-server-group-pppoe-v4] commit
   [~BRAS1-dhcp-server-group-pppoe-v4] quit
   ```
   
   # Configure an IPv4 address pool.
   
   ```
   [~BRAS1] ip pool test bas remote
   [*BRAS1-ip-pool-test] gateway 172.16.1.1 255.255.0.0
   [*BRAS1-ip-pool-test] commit
   [~BRAS1-ip-pool-test] dhcp-server group pppoe-v4
   [*BRAS1-ip-pool-test] commit
   [~BRAS1-ip-pool-test] quit
   ```
   
   # Configure the DHCPv6 server.
   
   ```
   [~BRAS1] dhcpv6-server group pppoe-v6
   [*BRAS1-dhcpv6-server-group-pppoe-v6] dhcpv6-server destination 2001:db8::1:1
   [*BRAS1-dhcpv6-server-group-pppoe-v6] dhcpv6-server source interface LoopBack0
   [*BRAS1-dhcpv6-server-group-pppoe-v6] commit
   [~BRAS1-dhcpv6-server-group-pppoe-v6] quit
   ```
   
   # Configure IPv6 address pools.
   
   ```
   [~BRAS1] ipv6 prefix nd remote
   [*BRAS1-ipv6-prefix-nd] link-address 2001:db8:10::10/128
   [*BRAS1-ipv6-prefix-nd] commit
   [~BRAS1-ipv6-prefix-nd] quit
   [~BRAS1] ipv6 prefix pd remote
   [*BRAS1-ipv6-prefix-pd] link-address 2001:db8:11::11/128
   [*BRAS1-ipv6-prefix-pd] commit
   [~BRAS1-ipv6-prefix-pd] quit
   [~BRAS1] ipv6 pool nd bas remote
   [*BRAS1-ipv6-pool-nd] prefix nd
   [*BRAS1-ipv6-pool-nd] dhcpv6-server group pppoe-v6
   [*BRAS1-ipv6-pool-nd] commit
   [~BRAS1-ipv6-pool-nd] quit
   [~BRAS1] ipv6 pool pd bas remote
   [*BRAS1-ipv6-pool-pd] prefix pd
   [*BRAS1-ipv6-pool-nd] dhcpv6-server group pppoe-v6
   [*BRAS1-ipv6-pool-nd] commit
   [~BRAS1-ipv6-pool-pd] quit
   ```
   
   # Bind the RBS to the address pools.
   
   ```
   [~BRAS1] remote-backup-service s1
   [~BRAS1-rm-backup-srv-s1] ip-pool test 
   [*BRAS1-rm-backup-srv-s1] ipv6-pool nd 
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pd 
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
6. Configure AAA schemes.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Configure an authentication scheme.
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] authentication-scheme auth1
   [*BRAS1-aaa-authen-auth1] authentication-mode radius
   [*BRAS1-aaa-authen-auth1] commit
   [~BRAS1-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS1-aaa] accounting-scheme acct1
   [*BRAS1-aaa-accounting-acct1] accounting-mode radius
   [*BRAS1-aaa-accounting-acct1] commit
   [~BRAS1-aaa-accounting-acct1] quit
   ```
7. Configure a RADIUS server group.
   
   
   ```
   [~BRAS1] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1645
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1646
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   [*BRAS1-radius-rd1] radius-server source interface LoopBack0
   [*BRAS1-radius-rd1] radius-server calling-station-id include mac 
   [*BRAS1-radius-rd1] commit
   [~BRAS1-radius-rd1] quit
   ```
8. Configure a domain.
   
   
   
   The configurations on BRAS1 are as follows:
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain test
   [*BRAS1-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS1-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS1-aaa-domain-isp1] radius-server group rd1
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] prefix-assign-mode unshared  
   [*BRAS1-aaa-domain-isp1] ip-pool test
   [*BRAS1-aaa-domain-isp1] ipv6-pool nd
   [*BRAS1-aaa-domain-isp1] ipv6-pool pd
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] quit
   [~BRAS1-aaa] quit
   ```
9. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   
   
   ```
   [~BRAS1] dhcpv6 duid llt
   [*BRAS1] commit
   ```
10. Configure a BAS interface.
    
    
    
    # Configure a VT.
    
    ```
    [~BRAS1] interface Virtual-Template1
    [*BRAS1-Virtual-Template1] ppp authentication-mode chap
    [*BRAS1-Virtual-Template1] commit
    [~BRAS1-Virtual-Template1] quit
    ```
    
    # Bind the VT to a sub-interface and enable IPv6 on the sub-interface.
    
    ```
    [~BRAS1] interface GigabitEthernet 0/1/0.2
    [*BRAS1-GigabitEthernet0/1/0.2] pppoe-server bind virtual-template 1
    [*BRAS1-GigabitEthernet0/1/0.2] ipv6 enable
    [*BRAS1-GigabitEthernet0/1/0.2] ipv6 address auto link-local
    [*BRAS1-GigabitEthernet0/1/0.2] commit
    [~BRAS1-GigabitEthernet0/1/0.2] user-vlan 5
    [~BRAS1-GigabitEthernet0/1/0.2-vlan-5] quit
    [~BRAS1-GigabitEthernet0/1/0.2] bas
    [*BRAS1-GigabitEthernet0/1/0.2-bas] access-type layer2-subscriber default-domain authentication test
    [*BRAS1-GigabitEthernet0/1/0.2-bas] client-option82
    [*BRAS1-GigabitEthernet0/1/0.2-bas] authentication-method ppp
    [*BRAS1-GigabitEthernet0/1/0.2-bas] authentication-method-ipv6 ppp
    [*BRAS1-GigabitEthernet0/1/0.2-bas] commit
    [~BRAS1-GigabitEthernet0/1/0.2-bas] quit
    [~BRAS1-GigabitEthernet0/1/0.2] quit
    ```
11. Configure the CGN service.
    
    
    
    # Enable the HA hot backup function.
    
    
    
    ```
    [~BRAS1] service-ha hot-backup enable
    [*BRAS1] commit
    ```
    
    # Set the number of session table resources to 6M for CPU 3 on the NAT service board.
    
    ```
    [~BRAS1] license
    [~BRAS1-license] active nat session-table size 6 slot 3 engine 0
    [*BRAS1-license] active nat bandwidth-enhance slot 3 engine 0
    [*BRAS1-license] commit
    [~BRAS1-license] quit
    ```
    
    # Create service location group 1, configure CPU 0 in slot 3 as a member for dual-device inter-chassis backup, and set the VRRP outbound interface of the local device to GigabitEthernet 0/3/0 and the peer IP address to 10.1.1.2.
    
    ```
    [~BRAS1] service-location 1 
    [*BRAS1-service-location-1] location slot 3 engine 0
    [*BRAS1-service-location-1] remote-backup interface GigabitEthernet 0/3/0 peer 10.1.1.2
    [*BRAS1-service-location-1] commit
    [~BRAS1-service-location-1] quit
    ```
    
    # Enter the GE0/3/0 interface view, create VRRP group 2, set the virtual IP address of the VRRP group to 10.1.1.3, and configure the VRRP group as an mVRRP backup group.
    
    ```
    [~BRAS1] interface GigabitEthernet 0/3/0
    [~BRAS1-GigabitEthernet0/3/0] ip address 10.1.1.1 24
    [~BRAS1-GigabitEthernet0/3/0] vrrp vrid 2 virtual-ip 10.1.1.3
    [*BRAS1-GigabitEthernet0/3/0] admin-vrrp vrid 2 ignore-if-down
    [*BRAS1-GigabitEthernet0/3/0] vrrp vrid 2 priority 200
    [*BRAS1-GigabitEthernet0/3/0] vrrp vrid 2 preempt-mode timer delay 400
    [*BRAS1-GigabitEthernet0/3/0] vrrp recover-delay 15
    [*BRAS1-GigabitEthernet0/3/0] commit
    [~BRAS1-GigabitEthernet0/3/0] quit
    ```
    
    # Associate HA with VRRP on the direct-connect interfaces on the active and standby devices.
    
    ```
    [~BRAS1] interface GigabitEthernet 0/3/0
    [~BRAS1-GigabitEthernet0/3/0] vrrp vrid 2 track service-location 1 reduced 60
    [*BRAS1-GigabitEthernet0/3/0] commit
    [~BRAS1-GigabitEthernet0/3/0] quit
    ```
    
    # Bind the service location group to the VRRP group on both the active and standby devices.
    
    ```
    [~BRAS1] service-location 1
    [*BRAS1-service-location-1] vrrp vrid 2 interface GigabitEthernet 0/3/0
    [*BRAS1-service-location-1] commit
    [~BRAS1-service-location-1] quit
    ```
    
    # Create a service instance group and bind it to the service location group.
    
    ```
    [~BRAS1] service-instance-group group1
    [*BRAS1-service-instance-group-group1] service-location 1
    [*BRAS1-service-instance-group-group1] remote-backup-service s1
    [*BRAS1-service-instance-group-group1] commit
    [~BRAS1-service-instance-group-group1] quit
    ```
    
    # Create a NAT instance on both the active and standby devices and bind it to the service instance group and NAT address pool.
    
    ```
    [~BRAS1] nat instance nat id 1
    [*BRAS1-nat-instance-nat] service-instance-group group1
    [*BRAS1-nat-instance-nat] nat address-group group1 group-id 1 10.11.11.100 10.11.11.105
    [*BRAS1-nat-instance-nat] nat outbound any address-group group1
    [*BRAS1-nat-instance-nat] nat alg all
    [*BRAS1-nat-instance-nat] nat filter mode full-cone
    [*BRAS1-nat-instance-nat] commit
    [~BRAS1-nat-instance-nat] quit
    ```
    
    # Configure a user group named **natbras**.
    
    ```
    [~BRAS1] user-group natbras
    [*BRAS1] commit
    ```
    
    # Bind the NAT instance to the domain.
    
    ```
    [~BRAS1] aaa
    [~BRAS1-aaa] domain test
    [*BRAS1-aaa-domain-test] user-group natbras bind nat instance nat
    [*BRAS1-aaa-domain-test] quit
    [*BRAS1-aaa] commit
    [~BRAS1-aaa] quit
    ```
    
    # Configure a NAT translation policy, including the traffic classification rule, NAT action, and NAT traffic policy, and apply the NAT traffic policy.
    
    1. Configure an ACL numbered 6001 and an ACL rule numbered 1.
       ```
       [~BRAS1] acl 6001
       [*BRAS1-ucl-6001] rule 1 permit ip source user-group natbras
       [*BRAS1-ucl-6001] commit
       [~BRAS1-ucl-6001] quit
       ```
    2. Configure a traffic classifier.
       ```
       [~BRAS1] traffic classifier c1
       [*BRAS1-classifier-c1] if-match acl 6001
       [*BRAS1-classifier-c1] commit
       [~BRAS1-classifier-c1] quit
       ```
    3. Configure a traffic behavior.
       ```
       [~BRAS1] traffic behavior b1 
       [*BRAS1-behavior-b1] nat bind instance nat
       [*BRAS1-behavior-b1] commit
       [~BRAS1-behavior-b1] quit
       ```
    4. Define a NAT traffic policy and associate the traffic classifier with the traffic behavior.
       ```
       [~BRAS1] traffic policy p1
       [*BRAS1-trafficpolicy-p1] classifier c1 behavior b1
       [*BRAS1-trafficpolicy-p1] commit
       [~BRAS1-trafficpolicy-p1] quit
       ```
    5. Apply the NAT traffic diversion policy in the system view.
       ```
       [~BRAS1] traffic-policy p1 inbound
       [*BRAS1] commit
       ```
    6. Configure the NAT address pool route as a static route, specify NULL0 as the outbound interface, and advertise the route to a routing protocol.
       ```
       [~BRAS1] ip route-static 10.11.11.0 27 null 0
       [*BRAS1] commit
       [~BRAS1-ospf-1] ospf 1
       [~BRAS1-ospf-1] import-route static
       [~BRAS1-ospf-1] quit
       ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  vrrp recover-delay 60
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#b-SAV,j)4#)Ez2TokT,%2z'sNM~0@4h~G.KsQhz)%^%#
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server source interface LoopBack0
   radius-server calling-station-id include mac 
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 3 engine 0
   remote-backup interface GigabitEthernet0/3/0 peer 10.1.1.2
   vrrp vrid 2 interface GigabitEthernet0/3/0
  #
  service-instance-group group1
   service-location 1
   remote-backup-service s1
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group group1 group-id 1 10.11.11.100 10.11.11.105 
   nat outbound any address-group group1
   nat alg all
   nat filter mode full-cone
  #
  bfd
  #
  mpls lsr-id 10.3.3.3
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  ip pool test bas remote
   gateway 172.16.1.1 255.255.0.0
   dhcp-server group pppoe-v4
  #
  dhcp-server group pppoe-v4
   dhcp-server 10.111.1.1
   dhcp-server source interface LoopBack0
   dhcp-server giaddr ip-address 172.16.1.2
   undo release-agent
  #
  dhcpv6-server group pppoe-v6
   dhcpv6-server destination 2001:db8::1:1
   dhcpv6-server source interface LoopBack0
  #
  ipv6 prefix nd remote
   link-address 2001:db8:10::10/128
  #
  ipv6 prefix pd remote
   link-address 2001:db8:11::11/128
  #
  ipv6 pool nd bas remote
   prefix nd
   dhcpv6-server group pppoe-v6
  #
  ipv6 pool pd bas remote
   prefix pd
   dhcpv6-server group pppoe-v6
  #
  dhcp check-server-pkt loose include option 3
  #
  user-group natbras
  #
  remote-backup-service s1
   peer 10.5.5.5 source 10.3.3.3 port 11000
   track interface GigabitEthernet0/1/0
   protect lsp-tunnel for-all-instance peer-ip 10.5.5.5
   ip-pool test metric 10
   ipv6-pool nd metric 10
   ipv6-pool pd metric 10
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/1/0.1
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  dhcpv6 duid 00010001280ef7a400e0fc904b50
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  aaa
  #
   authentication-scheme auth1
    authentication-mode radius
   #
   accounting-scheme acct1
    accounting-mode radius
   #
   domain test
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    prefix-assign-mode unshared
    ip-pool test
    ipv6-pool nd
    ipv6-pool pd
    user-group natbras bind nat instance nat
  #
  license
   active nat session-table size 6 slot 3 engine 0
   active nat bandwidth-enhance slot 3 engine 0
  #
  interface Virtual-Template1
   ppp authentication-mode chap
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ip address 10.11.11.1 255.255.255.0
   ipv6 address 2001:db8:1::/120
   ipv6 address auto link-local
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.1.3
   admin-vrrp vrid 2 ignore-if-down
   vrrp vrid 2 priority 200
   vrrp vrid 2 preempt-mode timer delay 400
   vrrp vrid 2 track service-location 1 reduced 60
   vrrp recover-delay 15
   dcn
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 400
   ip address 192.168.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 192.168.1.100
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 60
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50
   vrrp vrid 1 track bfd-session session-name bfd1 link
  #
  interface GigabitEthernet0/1/0.2
   ipv6 enable
   ipv6 address auto link-local
   statistic enable
   user-vlan 5
   pppoe-server bind Virtual-Template 1
   remote-backup-profile p1
   bas
   #
    access-type layer2-subscriber default-domain authentication test
    client-option82
    authentication-method ppp
    authentication-method-ipv6 ppp
   #
  #
  interface LoopBack0
   ipv6 enable
   ip address 10.2.2.2 255.255.255.255
   ipv6 address 2001:db8:3::3/128
   ipv6 address auto link-local
  #
  interface LoopBack1
   ip address 10.3.3.3 255.255.255.255
  #
  bfd bfd1 bind peer-ip 192.168.1.2
   discriminator local 8
   discriminator remote 6
  #
  ospf 1
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 10.11.11.0 0.0.0.255
    network 10.3.3.3 0.0.0.0
  #
  ip route-static 10.11.11.0 255.255.255.224 NULL0
  #
  peer-backup route-cost auto-advertising 
  #
  traffic-policy p1 inbound
  #
  return
  ```
* BRAS2 configuration file
  
  ```
  #
  sysname BRAS2
  #
  vrrp recover-delay 60
  #
  radius-server group rd1
   radius-server shared-key-cipher %^%#b-SAV,j)4#)Ez2TokT,%2z'sNM~0@4h~G.KsQhz)%^%#
   radius-server authentication 192.168.7.249 1645 weight 0
   radius-server accounting 192.168.7.249 1646 weight 0
   radius-server source interface LoopBack0
   radius-server calling-station-id include mac 
  #
  service-ha hot-backup enable
  #
  service-location 1
   location slot 3 engine 0
   remote-backup interface GigabitEthernet0/3/0 peer 10.1.1.1
   vrrp vrid 2 interface GigabitEthernet0/3/0
  #
  service-instance-group group1
   service-location 1
   remote-backup-service s1
  #
  nat instance nat id 1
   service-instance-group group1
   nat address-group group1 group-id 1 10.11.11.100 10.11.11.105 
   nat outbound any address-group group1
   nat alg all
   nat filter mode full-cone
  #
  bfd
  #
  mpls lsr-id 10.3.3.3
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  ip pool test bas remote rui-slave
   gateway 172.16.1.1 255.255.0.0
   dhcp-server group pppoe-v4
  #
  dhcp-server group pppoe-v4
   dhcp-server 10.111.1.1
   dhcp-server source interface LoopBack0
   dhcp-server giaddr ip-address 172.16.1.3
   undo release-agent
  #
  dhcpv6-server group pppoe-v6
   dhcpv6-server destination 2001:db8::1:1
   dhcpv6-server source interface LoopBack0
  #
  ipv6 prefix nd remote
   link-address 2001:db8:20::20/128
  #
  ipv6 prefix pd remote
   link-address 2001:db8:21::21/128
  #
  ipv6 pool nd bas remote rui-slave
   prefix nd
   dhcpv6-server group pppoe-v6
  #
  ipv6 pool pd bas remote rui-slave
   prefix pd
   dhcpv6-server group pppoe-v6
  #
  dhcp check-server-pkt loose include option 3
  #
  user-group natbras
  #
  remote-backup-service s1
   peer 10.3.3.3 source 10.5.5.5 port 11000
   track interface GigabitEthernet0/1/0
   protect lsp-tunnel for-all-instance peer-ip 10.3.3.3
   ip-pool test metric 20
   ipv6-pool nd metric 20
   ipv6-pool pd metric 20
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/1/0.1
  #
  acl number 6001
   rule 1 permit ip source user-group natbras
  #
  dhcpv6 duid 00010001280ef7a400e0fc904b50
  #
  traffic classifier c1 operator or
   if-match acl 6001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat
  #
  traffic policy p1
   share-mode
   classifier c1 behavior b1 precedence 1
  #
  aaa
   #
   authentication-scheme auth1
    authentication-mode radius
   #
   accounting-scheme acct1
    accounting-mode radius
   #
   domain test
    authentication-scheme auth1
    accounting-scheme acct1
    radius-server group rd1
    prefix-assign-mode unshared
    ip-pool test
    ipv6-pool nd
    ipv6-pool pd
    user-group natbras bind nat instance nat
  #
  license
   active nat session-table size 6 slot 3 engine 0
   active nat bandwidth-enhance slot 3 engine 0
  #
  interface Virtual-Template1
   ppp authentication-mode chap
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ip address 10.12.12.2 255.255.255.0
   ipv6 address 2001:db8:2::/120
   ipv6 address auto link-local
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 2 virtual-ip 10.1.1.3
   admin-vrrp vrid 2 ignore-if-down
   vrrp vrid 2 priority 150
   vrrp vrid 2 track service-location 1 reduced 60
   vrrp recover-delay 15
   dcn
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 400
   ip address 192.168.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 192.168.1.100
   vrrp vrid 1 priority 100
   vrrp vrid 1 preempt-mode timer delay 60
   vrrp vrid 1 track interface GigabitEthernet0/2/0 reduced 50
   vrrp vrid 1 track bfd-session session-name bfd1 link
  #
  interface GigabitEthernet0/1/0.2
   ipv6 enable
   ipv6 address auto link-local
   statistic enable
   user-vlan 5
   pppoe-server bind Virtual-Template 1
   remote-backup-profile p1
   bas
   #
    access-type layer2-subscriber default-domain authentication test
    client-option82
   #
  #
  interface LoopBack0
   ipv6 enable
   ip address 10.4.4.4 255.255.255.255
   ipv6 address 2001:db8:4::4/128
   ipv6 address auto link-local
  #
  interface LoopBack1
   ip address 10.5.5.5 255.255.255.255
  #
  bfd bfd1 bind peer-ip 192.168.1.1
   discriminator local 6
   discriminator remote 8
  #
  ospf 1
   default cost inherit-metric
   import-route unr
   opaque-capability enable
   area 0.0.0.0
    network 10.12.12.1 0.0.0.255
    network 10.5.5.5 0.0.0.0
  #
  ip route-static 10.11.11.0 255.255.255.224 NULL0
  #
  peer-backup route-cost auto-advertising 
  #
  traffic-policy p1 inbound
  #
  return                           
  ```