Example for Configuring Layer 2 Static Dual-Stack User Access (NA+PD) in a Dual-Device Hot Backup Scenario
==========================================================================================================

When the OLT is connected to the BRASs as a static user, the BRASs assign an IPv6 address to it in NA+PD mode to implement user access.

#### Networking Requirements

On the network shown in [Figure 1](dc_ne_cfg_rui_0064.html#EN-US_TASK_0210982515__fig_dc_ne_cfg_rui_003101), the OLT is connected to BRAS1 and BRAS2 as a static user, and common static users are connected to BRAS1 and BRAS2 through SW1. To allow the users to access IPv4 and IPv6 networks, configure the BRASs to use a local address pool to assign IPv4 addresses to the users, use DHCPv6 IA\_PD to assign IPv6 prefixes to them, and use DHCPv6 IA\_NA to assign IPv6 addresses to them. To improve network reliability, dual-device hot backup also needs to be deployed. If a fault occurs, a master/backup switchover can be triggered to ensure the normal running of services.

**Figure 1** Configuring Layer 2 static dual-stack user access in a dual-device hot backup scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent Eth-Trunk2 and GE0/1/0, respectively.


  
![](figure/en-us_image_0000001203403086.png)

**Table 1** Interfaces and IP addresses
| **Device** | **Interface Name** | **Interface Number** | **IP Address** |
| --- | --- | --- | --- |
| BRAS1 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.129/29 |
| interface2 | GE0/1/0 | 10.2.1.1/24, 2001:db8:8::7/128 |
| - | Loopback1 | 10.2.2.2/24, 2001:db8::2:2/64 |
| - | Loopback2 | 10.3.3.3/24 |
| BRAS2 | interface1 | Eth-trunk2 | - |
| interface1 | Eth-trunk2.1 | 192.168.4.130/29 |
| interface2 | GE0/1/0 | 10.4.1.1/24, 2001:db8:9::7/128 |
| - | Loopback1 | 10.4.4.4/24, 2001:db8::3:3/64 |
| - | Loopback2 | 10.13.13.13/24 |

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure a routing protocol.
3. Configure AAA schemes.
4. Configure address pools.
5. Configure a domain.
6. Configure a BFD session and VRRP on the access side of the master and backup BRASs.
7. Configure an RBS and an RBP.
8. Configure BAS interfaces.
9. Configure static users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of BRAS2 is similar to the configuration of BRAS1. The following uses the configuration on BRAS1 as an example. For configuration details on BRAS2, see the BRAS2 configuration file.




#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (such as the VRRP ID and preemption delay)
* BFD parameters (such as the local and remote discriminators of a BFD session and the expected minimum intervals at which BFD Control packets are sent and received)
* IP addresses of interfaces on BRAS1 and BRAS2.
* User access parameters

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
   
   
   
   # Configure an authentication scheme.
   
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
   
   # Configure an accounting scheme and set the accounting mode to none.
   
   ```
   [~BRAS1-aaa] accounting-scheme acct1
   [*BRAS1-aaa-accounting-acct1] accounting-mode none
   [*BRAS1-aaa-accounting-acct1] quit
   [*BRAS1-aaa] commit
   [~BRAS1-aaa] quit
   [~BRAS1] quit
   ```
4. Configure a RADIUS server group.
   
   
   ```
   [~BRAS1] radius-server group rd
   [*BRAS1-radius-rd] radius-server authentication 10.7.66.66 1812
   [*BRAS1-radius-rd] radius-server accounting 10.7.66.66 1813
   [*BRAS1-radius-rd] radius-server shared-key-cipher YsHsjx_202206
   [*BRAS1-radius-rd] radius-server retransmit 2
   [*BRAS1-radius-rd] commit
   [~BRAS1-radius-rd] quit
   ```
5. Configure address pools.
   
   
   
   # Configure a user-side local IPv4 address pool.
   
   ```
   [~BRAS1] ip pool pool_v4 bas local
   [*BRAS1-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0
   [*BRAS1-ip-pool-pool_v4] commit
   [~BRAS1-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.255 
   [~BRAS1-ip-pool-pool_v4] excluded-ip-address 172.16.0.2 172.16.0.255
   [*BRAS1-ip-pool-pool_v4] quit
   [*BRAS1] commit
   ```
   
   # Configure an IPv6 address pool.
   
   ```
   [~BRAS1] ipv6 prefix pre_na local
   [*BRAS1-ipv6-prefix-pre_na] prefix 2001:db8:1::/48
   [*BRAS1-ipv6-prefix-pre_pa] commit
   [~BRAS1-ipv6-prefix-pre_na] lock
   [*BRAS1-ipv6-prefix-pre_na] commit
   [~BRAS1-ipv6-prefix-pre_na] quit
   [~BRAS1] ipv6 pool pool_na bas local
   [*BRAS1-ipv6-pool-pool_na] prefix pre_na 
   [*BRAS1-ipv6-pool-pool_na] quit
   [*BRAS1] commit
   [~BRAS1] ipv6 prefix pre_pd delegation
   [*BRAS1-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
   [*BRAS1-ipv6-prefix-pre_pd] commit
   [~BRAS1-ipv6-prefix-pre_pd] lock
   [*BRAS1-ipv6-prefix-pre_pd] commit
   [~BRAS1-ipv6-prefix-pre_pd] quit
   [~BRAS1] ipv6 pool pool_pd bas delegation
   [*BRAS1-ipv6-pool-pool_pd] prefix pre_pd
   [*BRAS1-ipv6-pool-pool_pd] quit
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
   [*BRAS1-aaa-domain-isp1] radius-server group rd
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] ip-pool pool_v4
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_na
   [~BRAS1-aaa-domain-isp1] ipv6-pool pool_pd
   [*BRAS1-aaa-domain-isp1] commit
   [~BRAS1-aaa-domain-isp1] quit
   [~BRAS1-aaa] quit
   ```
7. Configure a BFD session and VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
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
   
   # Configure a VRRP group on an interface/sub-interface (sub-interface Eth-Trunk2.1 is used in this example), and configure VRRP to track the BFD session and network-side interface.
   
   ```
   [~BRAS1] interface Eth-Trunk2.1              
   [*BRAS1-Eth-Trunk2.1] vlan-type dot1q 96                           
   [*BRAS1-Eth-Trunk2.1] ip address 192.168.4.129 255.255.255.248            
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 virtual-ip 192.168.4.131   
   [*BRAS1-Eth-Trunk2.1] admin-vrrp vrid 5           
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 priority 120 
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 preempt-mode timer delay 60 
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track interface GigabitEthernet 0/1/0 reduced 50 
   [*BRAS1-Eth-Trunk2.1] vrrp vrid 5 track bfd-session session-name bfd1 link      
   [*BRAS1-Eth-Trunk2.1] commit
   [~BRAS1-Eth-Trunk2.1] quit
   ```
   
   # Set a status recovery delay for a VRRP group to suppress VRRP flapping.
   
   ```
   [~BRAS1] vrrp recover-delay 60
   [*BRAS1] commit
   ```
8. Configure an RBS and an RBP.
   
   
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] peer 10.13.13.13 source 10.3.3.3 port 6001
   [*BRAS1-rm-backup-srv-s1] track interface GigabitEthernet 0/1/0
   [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
   [*BRAS1-rm-backup-srv-s1] ip-pool pool_v4 metric 10
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_na metric 10
   [*BRAS1-rm-backup-srv-s1] ipv6-pool pool_pd metric 10
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
9. Configure a BAS interface.
   
   
   
   # Configure the Eth-Trunk interface to work in static LACP mode and set a timeout period for the interface to receive LACPDUs.
   
   ```
   [~BRAS1] interface Eth-Trunk2
   [*BRAS1-Eth-Trunk2] mode lacp-static
   [*BRAS1-Eth-Trunk2] lacp timeout fast
   [*BRAS1-Eth-Trunk2] commit
   ```
   
   # Configure a BAS interface for the common Layer 2 static users.
   
   ```
   [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.10
   [*BRAS1-Eth-Trunk2.10] ipv6 enable
   [*BRAS1-Eth-Trunk2.10] ipv6 address auto link-local
   [*BRAS1-Eth-Trunk2.10] commit
   [~BRAS1-Eth-Trunk2.10] user-vlan 1 10 qinq 100
   [~BRAS1-Eth-Trunk2.10-user-vlan-1-10-qinq-100] quit
   [~BRAS1-Eth-Trunk2.10] bas
   [~BRAS1-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS1-Eth-Trunk2.10-bas] authentication-method bind
   [*BRAS1-Eth-Trunk2.10-bas] authentication-method-ipv6 bind
   [*BRAS1-Eth-Trunk2.10-bas] ip-trigger
   [*BRAS1-Eth-Trunk2.10-bas] arp-trigger
   [*BRAS1-Eth-Trunk2.10-bas] ipv6-trigger
   [*BRAS1-Eth-Trunk2.10-bas] nd-trigger
   [*BRAS1-Eth-Trunk2.10-bas] commit
   [~BRAS1-Eth-Trunk2.10-bas] quit
   [~BRAS1-Eth-Trunk2.10] quit
   ```
   
   # Configure a BAS interface to manage the OLT that functions as a static user.
   
   ```
   [~BRAS1-Eth-Trunk2] interface Eth-Trunk2.2
   [~BRAS1-Eth-Trunk2.2] user-vlan 1 10
   [~BRAS1-Eth-Trunk2.21-user-vlan-1-10] quit
   [~BRAS1-Eth-Trunk2.2] bas
   [~BRAS1-Eth-Trunk2.1-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS1-Eth-Trunk2.1-bas] user-policy interface-down online
   [*BRAS1-Eth-Trunk2.1-bas] authentication-method bind
   [*BRAS1-Eth-Trunk2.1-bas] ip-trigger
   [*BRAS1-Eth-Trunk2.1-bas] arp-trigger
   [*BRAS1-Eth-Trunk2.1-bas] commit
   [~BRAS1-Eth-Trunk2.1-bas] quit
   [~BRAS1-Eth-Trunk2.1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface Eth-Trunk2.10
   [*BRAS1-Eth-Trunk2.10] remote-backup-profile p1
   [*BRAS1-Eth-Trunk2.10] quit
   [*BRAS1] commit
   [~BRAS1] interface Eth-Trunk2.2
   [*BRAS1-Eth-Trunk2.2] remote-backup-profile p1
   [*BRAS1-Eth-Trunk2.2] quit
   [*BRAS1] commit
   ```
10. Configure static users.
    
    
    
    # Configure common Layer 2 static users. The VLANs configured here must be within the VLAN range configured on the BAS interface.
    
    
    
    ```
    [~BRAS1] static-user 172.16.1.253 172.16.1.253 gateway 172.16.1.1 2001:db8:1::1 2001:db8:1::1 delegation-prefix 2001:db8:2:: 2001:db8:2:: 60 ipv6-gateway 2001:db8:1::1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
    [~BRAS1] static-user 172.16.1.252 172.16.1.252 gateway 172.16.1.1 2001:db8:1::3 2001:db8:1::3 ipv6-gateway 2001:db8:1::1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
    [~BRAS1] static-user 172.16.1.251 172.16.1.251 gateway 172.16.1.1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
    ```
    
    Configure the static user that the OLT functions as. The VLAN configured here must be within the VLAN range configured on the BAS interface.
    
    ```
    [~BRAS1] static-user 172.16.1.250 172.16.1.250 gateway 172.16.1.1 interface Eth-Trunk2.2 vlan 1 domain-name isp1 detect
    ```

#### Configuration Files

* BRAS1 configuration file

```
#
sysname BRAS1
#
vrrp recover-delay 60
#
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.255                                              
 excluded-ip-address 172.16.0.2 172.16.0.255                                      
#                                                                               
ipv6 prefix pre_na local                                                   
 prefix 2001:DB8:1::/48                                                         
 lock                                                             
#                                                                               
ipv6 pool pool_na bas local                                         
 prefix pre_na                                                                  
#                                                                               
ipv6 prefix pre_pd delegation                                                   
 prefix 2001:DB8:2::/48 delegating-prefix-length 60
 lock                                                               
#                                                                               
ipv6 pool pool_pd bas delegation                                         
 prefix pre_pd
#                                                                               
bfd
#
bfd bfd1 bind peer-ip 192.168.4.130
 discriminator local 1 
 discriminator remote 1
#
mpls lsr-id 10.3.3.3
#
mpls
#
mpls ldp
#
dhcpv6 duid 0001000124fbc193dc99141ea1e9
#
radius-server group rd                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                                             
 radius-server accounting 10.7.66.66 1813 weight 0                                                        
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
# 
aaa
 #
 authentication-scheme auth1
  authentication-mode radius
 #
 accounting-scheme acct1
  accounting-mode none
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1
  radius-server group rd
  ip-pool pool_v4                                                               
  ipv6-pool pool_na                                                             
  ipv6-pool pool_pd                                           
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
 user-vlan 1 10 qinq 100
 remote-backup-profile p1                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  authentication-method bind
  authentication-method-ipv6 bind
  ip-trigger
  arp-trigger
  ipv6-trigger
  nd-trigger 
 #                                                                              
#
interface Eth-Trunk2.2                                                         
 user-vlan 1 10
 remote-backup-profile p1                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1
  user-policy interface-down online            
  authentication-method bind
  ip-trigger
  arp-trigger
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
interface LoopBack2
 ip address 10.3.3.3 255.255.255.0
#
peer-backup route-cost auto-advertising
#
remote-backup-service s1
 peer 10.13.13.13 source 10.3.3.3 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.13.13.13
 ip-pool pool_v4 metric 10
 ipv6-pool pool_na metric 10
 ipv6-pool pool_pd metric 10
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
static-user 172.16.1.253 172.16.1.253 gateway 172.16.1.1 2001:db8:1::1 2001:db8:1::1 delegation-prefix 2001:db8:2:: 2001:db8:2:: 60 ipv6-gateway 2001:db8:1::1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
static-user 172.16.1.252 172.16.1.252 gateway 172.16.1.1 2001:db8:1::3 2001:db8:1::3 ipv6-gateway 2001:db8:1::1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
static-user 172.16.1.251 172.16.1.251 gateway 172.16.1.1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
static-user 172.16.1.250 172.16.1.250 gateway 172.16.1.1 interface Eth-Trunk2.2 vlan 1 domain-name isp1 detect
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.2.1.0 0.0.0.255
  network 10.3.3.3 0.0.0.0
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
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.255                                             
 excluded-ip-address 172.16.0.2 172.16.0.255                                      
#                                                                               
ipv6 prefix pre_na local                                                   
 prefix 2001:DB8:1::/48                                                         
 lock                                                             
#                                                                               
ipv6 pool pool_na bas local                                         
 prefix pre_na                                                                  
#                                                                               
ipv6 prefix pre_pd delegation                                                   
 prefix 2001:DB8:2::/48 delegating-prefix-length 60
 lock                                                               
#                                                                               
ipv6 pool pool_pd bas delegation                                         
 prefix pre_pd
#                                                                               
bfd
#
bfd bfd1 bind peer-ip 192.168.4.130
 discriminator local 1 
 discriminator remote 1
#
mpls lsr-id 10.13.13.13
#
mpls
#
mpls ldp
#
dhcpv6 duid 0001000124fbc193dc99141ea1e9
#
radius-server group rd                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                                             
 radius-server accounting 10.7.66.66 1813 weight 0                                                        
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
# 
aaa
 #
 authentication-scheme auth1
  authentication-mode radius
 #
 accounting-scheme acct1
  accounting-mode none
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1
  radius-server group rd
  ip-pool pool_v4                                                               
  ipv6-pool pool_na                                                             
  ipv6-pool pool_pd                                           
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
 vrrp vrid 5 track bfd-session session-name bfd1 peer
#
interface Eth-Trunk2.10                                                         
 ipv6 enable                                                                    
 ipv6 address auto link-local
 user-vlan 1 10 qinq 100
 remote-backup-profile p1                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1            
  authentication-method bind
  authentication-method-ipv6 bind
  ip-trigger
  arp-trigger
  ipv6-trigger
  nd-trigger 
 #                                                                              
#
interface Eth-Trunk2.2                                                         
 user-vlan 1 10
 remote-backup-profile p1                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1
  user-policy interface-down online            
  authentication-method bind
  ip-trigger
  arp-trigger
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
interface LoopBack2
 ip address 10.13.13.13 255.255.255.0
#
peer-backup route-cost auto-advertising
#
remote-backup-service s1
 peer 10.3.3.3 source 10.13.13.13 port 6001
 track interface GigabitEthernet0/1/0
 protect lsp-tunnel for-all-instance peer-ip 10.3.3.3
 ip-pool pool_v4 metric 20
 ipv6-pool pool_na metric 20
 ipv6-pool pool_pd metric 20
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
static-user 172.16.1.253 172.16.1.253 gateway 172.16.1.1 2001:db8:1::1 2001:db8:1::1 delegation-prefix 2001:db8:2:: 2001:db8:2:: 60 ipv6-gateway 2001:db8:1::1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
static-user 172.16.1.252 172.16.1.252 gateway 172.16.1.1 2001:db8:1::3 2001:db8:1::3 ipv6-gateway 2001:db8:1::1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
static-user 172.16.1.251 172.16.1.251 gateway 172.16.1.1 interface Eth-Trunk2.10 vlan 1 qinq 100 domain-name isp1 detect
static-user 172.16.1.250 172.16.1.250 gateway 172.16.1.1 interface Eth-Trunk2.2 vlan 1 domain-name isp1 detect
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.4.1.0 0.0.0.255
  network 10.13.13.13 0.0.0.0
#
return
```