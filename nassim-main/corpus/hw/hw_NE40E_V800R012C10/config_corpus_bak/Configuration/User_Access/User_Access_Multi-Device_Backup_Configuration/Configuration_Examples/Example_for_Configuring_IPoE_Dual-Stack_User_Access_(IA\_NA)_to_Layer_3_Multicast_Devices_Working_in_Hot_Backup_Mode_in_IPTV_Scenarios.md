Example for Configuring IPoE Dual-Stack User Access (IA\_NA) to Layer 3 Multicast Devices Working in Hot Backup Mode in IPTV Scenarios
======================================================================================================================================

This section provides an example for configuring IPoE dual-stack user access (IA\_NA) to Layer 3 multicast devices working in hot backup mode in IPTV scenarios. This example covers networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

In an IPTV scenario shown in [Figure 1](#EN-US_TASK_0000001205614756__fig_dc_ne_bras-multicast_cac_cfg_000201), a user (STB) accesses BRAS1 and BRAS2 using IPoE. The devices (BRASs) use RADIUS for authentication and accounting. To allow the user to access IPv4 and IPv6 networks, configure the devices to assign an IPv4 address to the user from a local address pool and assign an IPv6 address to the user using the DHCPv6 IA\_NA option (carrying an IA address). The devices use the binding authentication mode. Specifically, the Option field is filled in the password during user authentication, and a character string in the format of *MAC address@IPTV domain name* is generated as the username. The username and password are then sent to the RADIUS server for authentication.

The user wants to access IPTV services. As such, Layer 3 multicast needs to be deployed on the devices. To improve network reliability, dual-device hot backup also needs to be deployed. When a fault occurs, an active/standby device switchover is triggered to ensure that IPTV services are not interrupted.

**Figure 1** Configuring IPoE dual-stack user access (IA\_NA) to Layer 3 multicast devices working in hot backup mode in IPTV scenarios![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent Eth-Trunk2, GE0/1/0, and GE0/1/1, respectively.


![](figure/en-us_image_0000001251113833.png)

**Table 1** Interfaces and IP addresses
| **Device** | **Interface Name** | **Interface Number** | **IP Address** |
| --- | --- | --- | --- |
| BRAS1 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.129/29 |
| interface2 | GE0/1/0 | 10.2.1.1/24, 2001:db8:8::7/128 |
| interface3 | GE0/1/1 | 10.5.1.1/24 |
| - | Loopback1 | 10.2.2.2/24, 2001:db8::2:2/64 |
| - | Loopback2 | 10.3.3.3/24 |
| BRAS2 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.130/29 |
| interface2 | GE0/1/0 | 10.12.1.1/24, 2001:db8:9::7/128 |
| interface3 | GE0/1/1 | 10.15.1.1/24 |
| - | Loopback1 | 10.4.4.4/24, 2001:db8::3:3/64 |
| - | Loopback2 | 10.13.13.13/24 |





#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes.
2. Configure RADIUS.
3. Configure address pools.
4. Configure a domain.
5. Configure the user password generation mode.
6. Configure interfaces.
7. Configure basic multicast functions.
8. Configure static multicast.
9. Configure an RP.
10. Configure a BFD session and VRRP on the access side of the master and backup BRASs.
11. Configure an RBS and an RBP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of BRAS2 is similar to the configuration of BRAS1. The following uses the configuration on BRAS1 as an example. For configuration details on BRAS2, see the BRAS2 configuration file.



#### Data Preparation

* Address pool names, address ranges, and gateway addresses
* Authentication and accounting schemes
* Name of the domain to which the user belongs
* BAS interface parameters
* Multicast-related parameters
* VRRP parameters (such as the VRRP ID and preemption delay)
* BFD parameters (such as the local and remote discriminators of a BFD session and the expected minimum intervals at which BFD Control packets are sent and received)
* User authentication mode (RADIUS authentication)

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme that uses the RADIUS authentication mode.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*HUAWEI] commit
   [~BRAS1] aaa
   [~BRAS1-aaa] authentication-scheme auth1
   [*BRAS1-aaa-authen-auth1] authentication-mode radius
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
2. Configure RADIUS.
   
   
   
   # Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
   
   ```
   [~BRAS1] radius local-ip all
   [~BRAS1] commit
   ```
   
   # Configure a RADIUS server group.
   
   
   
   ```
   [~BRAS1] radius-server group rd1
   [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*BRAS1-radius-rd1] radius-server source interface loopback1
   [*BRAS1-radius-rd1] commit 
   [*BRAS1-radius-rd1] radius-attribute apply user-name match user-type ipoe
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] radius-server class-as-car
   [*BRAS1-radius-rd1] commit 
   [~BRAS1-radius-rd1] quit
   ```
3. Configure address pools.
   
   
   
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
   [~BRAS1] ipv6 prefix pre_na_1 local
   [*BRAS1-ipv6-prefix-pre_na_1] prefix 2001:db8:1::/48
   [*BRAS1-ipv6-prefix-pre_na_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_na_1 bas local
   [*BRAS1-ipv6-pool-pool_na_1] prefix pre_na_1
   [*BRAS1-ipv6-pool-pool_na_1] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_na_1] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_na_2 local
   [*BRAS1-ipv6-prefix-pre_na_2] prefix 2001:db8:2::/48
   [*BRAS1-ipv6-prefix-pre_na_2] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 pool pool_na_2 bas local rui-slave
   [*BRAS1-ipv6-pool-pool_na_2] prefix pre_na_2
   [*BRAS1-ipv6-pool-pool_na_2] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS1-ipv6-pool-pool_na_2] quit
   [*BRAS1] commit
   ```
4. Configure a domain.
   
   
   ```
   [~BRAS1] aaa
   [~BRAS1-aaa] domain isp1
   [*BRAS1-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS1-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS1-aaa-domain-isp1] radius-server group rd1
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] ip-pool pool_v4
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_na_1
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] quit
   [~BRAS1-aaa] quit
   ```
5. Configure the user password generation mode.
   
   
   ```
   [~BRAS1] aaa
   [*BRAS1-aaa] default-password template iptv option60 sub-option 31 md5-encrypt support hex
   [*BRAS1-aaa] default-user-name include mac-address -
   [*BRAS1-aaa] commit
   [~BRAS1-aaa] quit
   ```
6. Configure interfaces.
   
   
   
   # Configure the Eth-Trunk interface to work in static LACP mode and set a timeout period for the interface to receive LACPDUs.
   
   ```
   [~BRAS1] interface Eth-Trunk2
   [*BRAS1-Eth-Trunk2] mode lacp-static
   [*BRAS1-Eth-Trunk2] lacp timeout fast
   [*BRAS1-Eth-Trunk2] commit
   ```
   
   # Enable IPv6 on the interface.
   
   ```
   [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.10
   [*BRAS1-Eth-Trunk2.10] ipv6 enable
   [*BRAS1-Eth-Trunk2.10] ipv6 address auto link-local
   [*BRAS1-Eth-Trunk2.10] ipv6 nd autoconfig managed-address-flag
   [*BRAS1-Eth-Trunk2.10] ipv6 nd autoconfig other-flag
   [*BRAS1-Eth-Trunk2.10] commit
   [~BRAS1-Eth-Trunk2.10] user-vlan 1000 4000 qinq 2000 2001
   [~BRAS1-Eth-Trunk2.10-user-vlan-1000-4000-qinq-2000-2001] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~BRAS1-Eth-Trunk2.10] bas
   [~BRAS1-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS1-Eth-Trunk2.10-bas] authentication-method bind 
   [*BRAS1-Eth-Trunk2.10-bas] authentication-method-ipv6 bind
   [*BRAS1-Eth-Trunk2.10-bas] client-option82
   [*BRAS1-Eth-Trunk2.10-bas] client-option60
   [*BRAS1-Eth-Trunk2.10-bas] client-option18
   [*BRAS1-Eth-Trunk2.10-bas] client-option37
   [*BRAS1-Eth-Trunk2.10-bas] ip-trigger
   [*BRAS1-Eth-Trunk2.10-bas] arp-trigger
   [*BRAS1-Eth-Trunk2.10-bas] commit
   [~BRAS1-Eth-Trunk2.10-bas] ipv6-trigger
   [~BRAS1-Eth-Trunk2.10-bas] nd-trigger
   [~BRAS1-Eth-Trunk2.10-bas] default-password-template iptv
   [*BRAS1-Eth-Trunk2.10-bas] commit
   [~BRAS1-Eth-Trunk2.10-bas] quit
   ```
   
   # Configure the network-side interfaces connected to the PIM-SM network.
   
   ```
   [~BRAS1] interface gigabitEthernet 0/1/0
   [*BRAS1-GigabitEthernet0/1/0] ipv6 enable 
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address 2001:db8:8::7 128
   [*BRAS1-GigabitEthernet0/1/0] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1-GigabitEthernet0/1/0] commit
   [~BRAS1] interface gigabitEthernet 0/1/1
   [*BRAS1-GigabitEthernet0/1/1] ipv6 enable 
   [*BRAS1-GigabitEthernet0/1/1] ipv6 address 2001:db8:10::7 128
   [*BRAS1-GigabitEthernet0/1/1] ipv6 address auto link-local
   [*BRAS1-GigabitEthernet0/1/1] ip address 10.5.1.1 24
   [*BRAS1-GigabitEthernet0/1/1] quit
   [*BRAS1-GigabitEthernet0/1/1] commit
   [*BRAS1] interface Loopback1
   [*BRAS1-LoopBack1] ipv6 enable
   [*BRAS1-LoopBack1] ipv6 address 2001:db8::2:2 64
   [*BRAS1-LoopBack1] ipv6 address auto link-local
   [*BRAS1-LoopBack1] ip address 10.2.2.2 24
   [*BRAS1-LoopBack1] quit
   [*BRAS1] commit
   ```
7. Configure basic multicast functions.
   
   
   ```
   [~BRAS1] multicast routing-enable
   [*BRAS1] multicast load-splitting source-group
   [*BRAS1] commit
   [~BRAS1] interface gigabitEthernet 0/1/0
   [~BRAS1-GigabitEthernet0/1/0] pim sm
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1] commit
   [~BRAS1] interface gigabitEthernet 0/1/1
   [~BRAS1-GigabitEthernet0/1/0] pim sm
   [*BRAS1-GigabitEthernet0/1/0] quit
   [*BRAS1] commit
   ```
8. Configure Layer 3 multicast.
   
   
   
   # Configure the range of multicast groups that an interface can join.
   
   
   
   ```
   [~BRAS1] acl number 2999
   [*BRAS1-acl4-basic-2239] description For:Permit-Pim-RP-Policy&Igmp-Group-Policy
   [*BRAS1-acl4-basic-2239] rule 10 permit source 227.1.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2239] rule 20 permit source 228.1.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2239] rule 1000 deny
   [*BRAS1-acl4-basic-2239] quit
   [*BRAS1] commit
   ```
   
   # Configure Layer 3 multicast on the interface connected to user hosts.
   
   ```
   [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.11
   [*BRAS1-Eth-Trunk2.11] vlan-type dot1q 1100
   [*BRAS1-Eth-Trunk2.11] description to_IPTV_multicast
   [*BRAS1-Eth-Trunk2.11] ip address 192.168.9.5 255.255.255.252
   [*BRAS1-Eth-Trunk2.11] pim hello-option dr-priority 100
   [*BRAS1-Eth-Trunk2.11] pim sm
   [*BRAS1-Eth-Trunk2.11] igmp enable
   [*BRAS1-Eth-Trunk2.11] igmp group-policy 2999
   [*BRAS1-Eth-Trunk2.11] quit
   [*BRAS1] commit
   ```
9. Configure an RP.
   
   # Configure the range of multicast groups that the static RP serves.
   ```
   [~BRAS1] acl number 2239
   [*BRAS1-acl4-basic-2239] description this acl is used pim rp group limit
   [*BRAS1-acl4-basic-2239] rule 10 permit source 227.1.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2239] rule 20 permit source 228.1.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2239] rule 100 deny
   [*BRAS1-acl4-basic-2239] quit
   [*BRAS1] commit
   ```
   
   
   # Configure the source address of multicast data packets.
   ```
   [~BRAS1] acl number 2101
   [*BRAS1-acl4-basic-2101] description For:Permit-Pim-source-policy
   [*BRAS1-acl4-basic-2101] rule 10 permit source 10.10.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2101] rule 20 permit source 10.20.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2101] rule 30 permit source 10.30.0.0 0.0.255.255
   [*BRAS1-acl4-basic-2101] rule 1000 deny
   [*BRAS1-acl4-basic-2101] quit
   [*BRAS1] commit
   ```
   
   
   # Configure a static RP.
   ```
   [~BRAS1] pim
   [*BRAS1-pim] static-rp 192.168.0.6 2239 preferred
   [*BRAS1-pim] source-policy 2101
   [*BRAS1-pim] quit
   [*BRAS1] commit
   ```
10. Configure a BFD session and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
    
    
    
    # Configure a BFD session on the access side to allow the device to rapidly detect interface or link faults and trigger a master/backup VRRP switchover upon such a fault.
    
    ```
    [~BRAS1] bfd
    [*BRAS1-bfd] quit
    [*BRAS1] bfd bfd1 bind peer-ip 192.168.4.130
    [*BRAS1-bfd-session-bfd1] discriminator local 1
    [*BRAS1-bfd-session-bfd1] discriminator remote 1
    [*BRAS1-bfd-session-bfd1] quit 
    [*BRAS1] commit
    ```
    
    # Configure a VRRP group on an interface/sub-interface (sub-interface Eth-Trunk2.1 is used in this example), and configure VRRP to track the BFD session and network-side interface. Set the VRRP preemption delay to 1800s.
    
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
11. Configure an RBS and an RBP.
    
    
    
    # Configure an RBS, and configure the device to use the NAS IP address as the source IP address in packets replied to the RADIUS server.
    
    ```
    [~BRAS1] peer-backup route-cost auto-advertising
    [~BRAS1] remote-backup-service s1
    [*BRAS1-rm-backup-srv-s1] peer 10.13.13.13 source 10.3.3.3 port 6001
    [*BRAS1-rm-backup-srv-s1] track interface GigabitEthernet 0/1/0
    [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
    [*BRAS1-rm-backup-srv-s1] ip-pool pool_v4 metric 10
    [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_na_1 metric 10
    [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_na_2 metric 20
    [*BRAS1-rm-backup-srv-s1] radius-authorization source same-as nas-logic-ip
    [*BRAS1-rm-backup-srv-s1] quit
    [*BRAS1] commit
    ```
    
    # Configure an RBP, and configure a logical IP address, logical interface, and logical hostname, so that the active and standby devices use the same NAS-IP-Address, NAS-Port, NAS-Port-ID, and Option 82 information in the packets sent to the RADIUS and DHCP servers.
    
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
    
    # Bind the RBP to the interface through which the user goes online.
    
    ```
    [~BRAS1] interface Eth-Trunk2.10
    [*BRAS1-Eth-Trunk2.10] remote-backup-profile p1
    [*BRAS1-Eth-Trunk2.10] quit
    [*BRAS1] commit
    ```

#### Configuration Files

* BRAS1 configuration file

```
#
sysname BRAS1
#
multicast routing-enable
#
multicast load-splitting source-group
#
acl number 2999
 description For:Permit-Pim-RP-Policy&Igmp-Group-Policy
 rule 10 permit source 227.1.0.0 0.0.255.255
 rule 20 permit source 228.1.0.0 0.0.255.255
 rule 1000 deny
#
acl number 2239
 description this acl is used pim rp group limit
 rule 10 permit source 227.1.0.0 0.0.255.255
 rule 20 permit source 228.1.0.0 0.0.255.255
 rule 100 deny
#
acl number 2101
 description For:Permit-Pim-source-policy
 rule 10 permit source  10.10.0.0 0.0.255.255
 rule 20 permit source  10.20.0.0 0.0.255.255
 rule 30 permit source  10.30.0.0 0.0.255.255
 rule 1000 deny
#
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_na_1 local                                                   
 prefix 2001:DB8:1::/48                                                                                                                     
#                                                                               
ipv6 pool pool_na_1 bas local                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_na_1                                                                  
#
ipv6 prefix pre_na_2 local                                                   
 prefix 2001:DB8:2::/48                                                                                                                     
#                                                                               
ipv6 pool pool_na_2 bas local rui-slave                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_na_2                                                                  
#
radius local-ip all
#
bfd
#
bfd bfd1 bind peer-ip 192.168.4.130
 discriminator local 1 
 discriminator remote 1
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% 
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server source interface LoopBack1
 radius-server class-as-car
 radius-attribute apply user-name match user-type ipoe
#
aaa
 default-password template iptv option60 sub-option 31 md5-encrypt support hex
 default-user-name include mac-address -
 #
 authentication-scheme auth1
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1
  ip-pool pool_v4                                                               
  ipv6-pool pool_na_1
#
interface Eth-Trunk2.1
 vlan-type dot1q 96
 ip address 192.168.4.129 255.255.255.248
 vrrp vrid 5 virtual-ip 192.168.4.131
 admin-vrrp vrid 5
 vrrp vrid 5 priority 120
 vrrp recover-delay 300
 vrrp vrid 5 preempt-mode timer delay 60
 vrrp vrid 5 preempt-mode timer delay 1800
 vrrp vrid 5 track interface GigabitEthernet0/1/0 reduced 50
 vrrp vrid 5 track bfd-session session-name bfd1 link
#
peer-backup route-cost auto-advertising
#
remote-backup-service s1
 peer 10.13.13.13 source 10.3.3.3 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
 ip-pool pool_v4 metric 10
 ipv6-pool pool_na_1 metric 10
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
#
interface LoopBack1
 ipv6 enable
 ip address 10.2.2.2 255.255.255.0
 ipv6 address 2001:DB8::2:2/64
 ipv6 address auto link-local
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
 vrrp vrid 5 preempt-mode timer delay 60
 vrrp vrid 5 track interface GigabitEthernet0/1/0 reduced 50
 vrrp vrid 5 track bfd-session session-name bfd1 link
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                               
 user-vlan 1000 4000 qinq 2000 2001
 ipv6 nd autoconfig managed-address-flag
 ipv6 nd autoconfig other-flag
 remote-backup-profile p1
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  client-option82
  client-option60
  client-option37
  client-option18
  authentication-method bind                                                    
  authentication-method-ipv6 bind
  ip-trigger
  arp-trigger
  ipv6-trigger 
  nd-trigger
  default-password-template iptv                                                     
 #
#
interface Eth-Trunk2.11
 vlan-type dot1q 1100
 description to_IPTV_multicast
 ip address 192.168.9.5 255.255.255.252
 pim hello-option dr-priority 100
 pim sm
 igmp enable
 igmp group-policy 2999
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.2.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:8::7/128                                                 
 ipv6 address auto link-local
 pim sm
# 
interface GigabitEthernet0/1/1                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.5.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:10::7/128                                                 
 ipv6 address auto link-local
 pim sm
# 
pim 
 static-rp 192.168.0.6 2239 preferred
 source-policy 2101
#     
return
```

* BRAS2 configuration file

```
#
sysname BRAS2
#
multicast routing-enable
#
multicast load-splitting source-group
#
acl number 2999
 description For:Permit-Pim-RP-Policy&Igmp-Group-Policy
 rule 10 permit source 227.1.0.0 0.0.255.255
 rule 20 permit source 228.1.0.0 0.0.255.255
 rule 1000 deny
#
acl number 2239
 description this acl is used pim rp group limit
 rule 10 permit source 225.1.0.0 0.0.255.255
 rule 20 permit source 226.1.0.0 0.0.255.255
 rule 100 deny
#
acl number 2101
 description For:Permit-Pim-source-policy
 rule 10 permit source  10.10.0.0 0.0.255.255
 rule 20 permit source  10.20.0.0 0.0.255.255
 rule 30 permit source  10.30.0.0 0.0.255.255
 rule 1000 deny
#
ip pool pool_v4 bas local rui-slave                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_na_1 local                                                   
 prefix 2001:DB8:1::/48                                                                                                                     
#                                                                               
ipv6 pool pool_na_1 bas local rui-slave                                               
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_na_1                                                                  
#
ipv6 prefix pre_na_2 local                                                   
 prefix 2001:DB8:2::/48                                                                                                                     
#                                                                               
ipv6 pool pool_na_2 bas local                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_na_2                                                                  
#
radius local-ip all
#
bfd
#
bfd bfd1 bind peer-ip 192.168.5.129
 discriminator local 1 
 discriminator remote 1
#
radius-server group rd1                                                       
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^% 
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server source interface LoopBack1
 radius-server class-as-car
 radius-attribute apply user-name match user-type ipoe
#
aaa
 default-password template iptv option60 sub-option 31 md5-encrypt support hex
 default-user-name include mac-address -
 #
 authentication-scheme auth1
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1
  ip-pool pool_v4                                                               
  ipv6-pool pool_na_2
#
interface  Eth-Trunk2.1
 vlan-type dot1q 96
 ip address 192.168.4.129 255.255.255.248
 vrrp vrid 5 virtual-ip 192.168.4.131
 admin-vrrp vrid 5
 vrrp vrid 5 priority 120
 vrrp vrid 5 track bfd-session session-name bfd1 peer
#
peer-backup route-cost auto-advertising
#
remote-backup-service s1
 peer 10.3.3.3 source 10.13.13.13 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.3.3.3
 ip-pool pool_v4 metric 20
 ipv6-pool pool_na_1 metric 20
 ipv6-pool pool_na_2 metric 10
 radius-authorization source same-as nas-logic-ip
#
remote-backup-profile p1
 service-type bras
 backup-id 5 remote-backup-service s1
 peer-backup hot
 vrrp-id 5 interface Eth-Trunk2.1
 nas logic-sysname huawei
 nas logic-port Eth-Trunk2
 nas logic-ip 10.10.1.1
#
interface LoopBack1
 ipv6 enable
 ip address 10.2.2.2 255.255.255.0
 ipv6 address 2001:DB8::2:2/64
 ipv6 address auto link-local
#
interface Eth-Trunk2                                          
 mode lacp-static                                                               
 lacp timeout fast                                                              
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                               
 user-vlan 1000 4000 qinq 2000 2001
 ipv6 nd autoconfig managed-address-flag
 ipv6 nd autoconfig other-flag
 remote-backup-profile p1
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  client-option82
  client-option60
  client-option37
  client-option18
  authentication-method bind                                                    
  authentication-method-ipv6 bind
  ip-trigger
  arp-trigger
  ipv6-trigger 
  nd-trigger
  default-password-template iptv                                                     
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.12.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:18::7/128                                                 
 ipv6 address auto link-local
 pim sm
# 
interface GigabitEthernet0/1/1                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ip address 10.15.1.1 255.255.255.0                                              
 ipv6 address 2001:DB8:20::7/128                                                 
 ipv6 address auto link-local
 pim sm
# 
pim 
 static-rp 192.168.0.6 2239 preferred
 source-policy 2101
#     
return
```