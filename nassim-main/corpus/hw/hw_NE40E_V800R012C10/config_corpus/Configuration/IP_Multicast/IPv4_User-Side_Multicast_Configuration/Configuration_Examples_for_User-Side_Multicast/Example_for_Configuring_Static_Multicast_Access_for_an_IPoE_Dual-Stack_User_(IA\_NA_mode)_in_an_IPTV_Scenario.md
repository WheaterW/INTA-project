Example for Configuring Static Multicast Access for an IPoE Dual-Stack User (IA\_NA mode) in an IPTV Scenario
=============================================================================================================

This section provides an example for configuring static multicast access for an IPoE dual-stack user (IA\_NA mode). The example covers networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

In an IPTV scenario shown in [Figure 1](#EN-US_TASK_0000001204956416__fig_dc_ne_bras-multicast_cac_cfg_000201), a user (STB) accesses a BRAS using IPoE. The BRAS uses RADIUS authentication and accounting. The user wants to join multicast groups 225.1.1.1 and 227.1.1.1 after going online. Therefore, the static multicast function needs to be configured on the BRAS to connect to the PIM-SM network. To allow the user to access IPv4 and IPv6 networks, configure the device to assign an IPv4 address to the user from a local address pool and assign an IPv6 address to the user using the DHCPv6 IA\_NA option (carrying an IA address). The BRAS uses the binding authentication mode. Specifically, the Option field is filled in the password during user authentication, and a character string in the format of *MAC address@IPTV domain name* is generated as the username. The username and password are then sent to the RADIUS server for authentication.

**Figure 1** Configuring static multicast access for an IPoE dual-stack user (IA\_NA mode) in an IPTV scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent Eth-Trunk2, GE0/1/0, and GE0/1/1, respectively.

![](figure/en-us_image_0000001335548261.png)



#### Configuration Roadmap

The configuration roadmap (on the BRAS) is as follows:

1. Configure AAA schemes.
2. Configure RADIUS.
3. Configure address pools.
4. Configure a domain.
5. Configure the user password generation mode.
6. Configure interfaces.
7. Configure basic multicast functions.
8. Configure static multicast.
9. Configure an RP.

#### Data Preparation

* Address pool names, address ranges, and gateway addresses
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* Name of the domain to which the user belongs
* BAS interface parameters
* Multicast-related parameters

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme that uses the RADIUS authentication mode.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS
   [*HUAWEI] commit
   [~BRAS] aaa
   [~BRAS-aaa] authentication-scheme auth1
   [*BRAS-aaa-authen-auth1] authentication-mode radius
   [*BRAS-aaa-authen-auth1] quit
   [*BRAS-aaa] commit
   ```
   
   # Configure an accounting scheme that uses the RADIUS accounting mode.
   
   ```
   [~BRAS-aaa] accounting-scheme acct1
   [*BRAS-aaa-accounting-acct1] accounting-mode radius
   [*BRAS-aaa-accounting-acct1] quit
   [*BRAS-aaa] commit
   [*BRAS-aaa] quit
   ```
2. Configure RADIUS.
   
   
   
   # Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
   
   ```
   [~BRAS] radius local-ip all
   [~BRAS] commit
   ```
   
   # Configure a RADIUS server group.
   
   
   
   ```
   [~BRAS] radius-server group rd1
   [*BRAS-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*BRAS-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*BRAS-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
   [*BRAS-radius-rd1] radius-server source interface loopback1
   [*BRAS-radius-rd1] commit 
   [*BRAS-radius-rd1] radius-attribute apply user-name match user-type ipoe
   [*BRAS-radius-rd1] commit 
   [~BRAS-radius-rd1] radius-server class-as-car
   [*BRAS-radius-rd1] commit 
   [~BRAS-radius-rd1] quit
   ```
3. Configure address pools.
   
   
   
   # Configure a user-side local IPv4 address pool.
   
   ```
   [~BRAS] ip pool pool_v4 bas local
   [*BRAS-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0
   [*BRAS-ip-pool-pool_v4] commit
   [~BRAS-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   [~BRAS-ip-pool-pool_v4] dns-server 10.179.155.161 10.179.155.177
   [*BRAS-ip-pool-pool_v4] quit
   [*BRAS] commit
   ```
   
   # Configure an IPv6 address pool.
   
   ```
   [~BRAS] ipv6 prefix pre_na delegation
   [*BRAS-ipv6-prefix-pre_na] prefix 2001:db8:1::/48
   [*BRAS-ipv6-prefix-pre_na] quit
   [*BRAS] commit
   [~BRAS] ipv6 pool pool_na bas delegation
   [*BRAS-ipv6-pool-pool_na] prefix pre_na
   [*BRAS-ipv6-pool-pool_na] dns-server 2001:db8::2:2 2001:db8::2:3
   [*BRAS-ipv6-pool-pool_na] quit
   [*BRAS] commit
   ```
4. Configure a domain.
   
   
   ```
   [~BRAS] aaa
   [~BRAS-aaa] domain isp1
   [*BRAS-aaa-domain-isp1] authentication-scheme auth1
   [*BRAS-aaa-domain-isp1] accounting-scheme acct1
   [*BRAS-aaa-domain-isp1] radius-server group rd1
   [*BRAS-aaa-domain-isp1] commit
   [~BRAS-aaa-domain-isp1] ip-pool pool_v4
   [~BRAS-aaa-domain-isp1] ipv6-pool pool_na
   [*BRAS-aaa-domain-isp1] commit
   [~BRAS-aaa-domain-isp1] quit
   [~BRAS-aaa] quit
   ```
5. Configure the user password generation mode.
   
   
   ```
   [~BRAS] aaa
   [*BRAS-aaa] default-password template iptv option60 sub-option 31 support hex
   [*BRAS-aaa] default-user-name include mac-address -
   [*BRAS-aaa] commit
   [~BRAS-aaa] quit
   ```
6. Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode. (This step is not required if a DUID has been configured on the BRAS.)
   
   
   ```
   [~BRAS] dhcpv6 duid llt
   [*BRAS] commit
   ```
7. Configure interfaces.
   
   
   
   # Configure the Eth-Trunk interface to work in static LACP mode and set a protocol packet timeout period.
   
   
   
   ```
   [~BRAS] interface Eth-Trunk2
   [*BRAS-Eth-Trunk2] mode lacp-static
   [*BRAS-Eth-Trunk2] lacp timeout fast
   [*BRAS-Eth-Trunk2] commit
   ```
   
   # Enable IPv6 on an interface.
   
   ```
   [~BRAS-Eth-Trunk2] interface Eth-Trunk2.10
   [*BRAS-Eth-Trunk2.10] ipv6 enable
   [*BRAS-Eth-Trunk2.10] ipv6 address auto link-local
   [*BRAS-Eth-Trunk2.10] ipv6 nd autoconfig managed-address-flag
   [*BRAS-Eth-Trunk2.10] ipv6 nd autoconfig other-flag
   [*BRAS-Eth-Trunk2.10] commit
   [~BRAS-Eth-Trunk2.10] user-vlan 1000 4000 qinq 2000 2001
   [~BRAS-Eth-Trunk2.10-user-vlan-1000-4000-qinq-2000-2001] quit
   ```
   
   # Configure a BAS interface, enable multicast replication by session, and enable controllable multicast on the interface.
   
   ```
   [~BRAS-Eth-Trunk2.10] bas
   [~BRAS-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
   [*BRAS-Eth-Trunk2.10-bas] authentication-method bind 
   [*BRAS-Eth-Trunk2.10-bas] authentication-method-ipv6 bind
   [*BRAS-Eth-Trunk2.10-bas] client-option82
   [*BRAS-Eth-Trunk2.10-bas] client-option60
   [*BRAS-Eth-Trunk2.10-bas] client-option18
   [*BRAS-Eth-Trunk2.10-bas] client-option37
   [*BRAS-Eth-Trunk2.10-bas] ip-trigger
   [*BRAS-Eth-Trunk2.10-bas] arp-trigger
   [*BRAS-Eth-Trunk2.10-bas] commit
   [~BRAS-Eth-Trunk2.10-bas] ipv6-trigger
   [~BRAS-Eth-Trunk2.10-bas] nd-trigger
   [~BRAS-Eth-Trunk2.10-bas] default-password-template iptv
   [*BRAS-Eth-Trunk2.10-bas] multicast copy by-session
   [*BRAS-Eth-Trunk2.10-bas] commit
   [~BRAS-Eth-Trunk2.10-bas] quit
   [~BRAS-Eth-Trunk2.10] multicast authorization-enable
   [*BRAS-Eth-Trunk2.10] quit
   [*BRAS] commit
   ```
   
   # Configure the network-side interfaces connected to the PIM-SM network.
   
   ```
   [~BRAS] interface gigabitEthernet 0/1/0
   [*BRAS-GigabitEthernet0/1/0] ipv6 enable 
   [*BRAS-GigabitEthernet0/1/0] ipv6 address 2001:db8:8::7 128
   [*BRAS-GigabitEthernet0/1/0] ipv6 address auto link-local
   [*BRAS-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   [*BRAS-GigabitEthernet0/1/0] quit
   [*BRAS-GigabitEthernet0/1/0] commit
   [~BRAS] interface gigabitEthernet 0/1/1
   [*BRAS-GigabitEthernet0/1/1] ipv6 enable 
   [*BRAS-GigabitEthernet0/1/1] ipv6 address 2001:db8:10::7 128
   [*BRAS-GigabitEthernet0/1/1] ipv6 address auto link-local
   [*BRAS-GigabitEthernet0/1/1] ip address 10.5.1.1 24
   [*BRAS-GigabitEthernet0/1/1] quit
   [*BRAS-GigabitEthernet0/1/1] commit
   [*BRAS] interface Loopback1
   [*BRAS-LoopBack1] ipv6 enable
   [*BRAS-LoopBack1] ipv6 address 2001:db8::2:2 64
   [*BRAS-LoopBack1] ipv6 address auto link-local
   [*BRAS-LoopBack1] ip address 10.2.2.2 24
   [*BRAS-LoopBack1] quit
   [*BRAS] commit
   ```
8. Configure basic multicast functions and load splitting based on source and group addresses.
   
   
   ```
   [~BRAS] multicast routing-enable
   [*BRAS] multicast load-splitting source-group
   [*BRAS] commit
   [~BRAS] interface Eth-Trunk2.10
   [~BRAS-Eth-Trunk2.10] pim sm
   [*BRAS-Eth-Trunk2.10] igmp enable
   [*BRAS-Eth-Trunk2.10] igmp prompt-leave
   [*BRAS-Eth-Trunk2.10] quit
   [*BRAS] commit
   [~BRAS] interface gigabitEthernet 0/1/0
   [~BRAS-GigabitEthernet0/1/0] pim sm
   [*BRAS-GigabitEthernet0/1/0] quit
   [*BRAS] commit
   [~BRAS] interface gigabitEthernet 0/1/1
   [~BRAS-GigabitEthernet0/1/0] pim sm
   [*BRAS-GigabitEthernet0/1/0] quit
   [*BRAS] commit
   ```
9. Configure multicast.
   
   
   
   # Configure multicast program lists.
   
   ```
   [~BRAS] aaa
   [~BRAS-aaa] multicast-list list1 group-address 225.1.1.1
   [~BRAS-aaa] multicast-list list2 group-address 227.1.1.1
   ```
   
   # Configure a multicast profile.
   
   ```
   [~BRAS-aaa] multicast-profile profile1
   [~BRAS-aaa-mprofile-profile1] multicast-list name list1 static
   [~BRAS-aaa-mprofile-profile1] multicast-list name list2 static
   [~BRAS-aaa-mprofile-profile1] quit
   ```
   
   # Apply the multicast profile to the domain.
   
   ```
   [~BRAS-aaa] domain isp1
   [*BRAS-aaa-domain-isp1] commit
   [~BRAS-aaa-domain-isp1] multicast-profile profile1
   [*BRAS-aaa-domain-isp1] commit
   [~BRAS-aaa-domain-isp1] quit
   [~BRAS-aaa] quit
   ```
10. Configure an RP.
    
    # Configure the range of multicast groups that the static RP serves.
    ```
    [~BRAS] acl number 2239
    [*BRAS-acl4-basic-2239] description this acl is used pim rp group limit
    [*BRAS-acl4-basic-2239] rule 10 permit source 225.1.1.1 0.0.255.255
    [*BRAS-acl4-basic-2239] rule 20 permit source 227.1.1.1 0.0.255.255
    [*BRAS-acl4-basic-2239] rule 100 deny
    [*BRAS-acl4-basic-2239] quit
    [*BRAS] commit
    ```
    
    
    # Configure the source addresses of multicast data packets.
    ```
    [~BRAS] acl number 2101
    [*BRAS-acl4-basic-2101] description For:Permit-Pim-source-policy
    [*BRAS-acl4-basic-2101] rule 10 permit source 10.10.0.0 0.0.255.255
    [*BRAS-acl4-basic-2101] rule 20 permit source 10.20.0.0 0.0.255.255
    [*BRAS-acl4-basic-2101] rule 30 permit source 10.30.0.0 0.0.255.255
    [*BRAS-acl4-basic-2101] rule 1000 deny
    [*BRAS-acl4-basic-2101] quit
    [*BRAS] commit
    ```
    
    
    # Configure a static RP.
    ```
    [~BRAS] pim
    [*BRAS-pim] static-rp 192.168.0.6 2239 preferred
    [*BRAS-pim] source-policy 2101
    [*BRAS-pim] quit
    [*BRAS] commit
    ```

#### Configuration Files

```
#
sysname BRAS
#
multicast routing-enable
#
multicast load-splitting source-group
#
dhcpv6 duid llt
# 
acl number 2239
 description this acl is used pim rp group limit
 rule 10 permit source 225.1.1.1 0.0.255.255
 rule 20 permit source 227.1.1.1 0.0.255.255
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
ipv6 prefix pre_na delegation                                                   
 prefix 2001:DB8:1::/48                                                                                                                     
#                                                                               
ipv6 pool pool_na bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_na                                                                  
#                                                                               
radius local-ip all
#
interface LoopBack1
 ipv6 enable
 ip address 10.2.2.2 255.255.255.0
 ipv6 address 2001:DB8::2:2/64
 ipv6 address auto link-local
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
 multicast-list list1 group-address 225.1.1.1 
 multicast-list list2 group-address 227.1.1.1 
 multicast-profile profile1  
  multicast-list name list1 static
  multicast-list name list2 static
 default-password template iptv option60 sub-option 31 support hex
 default-user-name include mac-address -
 #
 authentication-scheme auth1
  authentication-mode radius
 #
 accounting-scheme acct1
  accounting-mode radius
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1                                                                                                    
  ip-pool pool_v4                                                               
  ipv6-pool pool_na                                                              
  multicast-profile profile1                                               
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
 pim sm
 igmp enable
 igmp prompt-leave
 multicast authorization-enable
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
  multicast copy by-session                                                     
 #                                                                              
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