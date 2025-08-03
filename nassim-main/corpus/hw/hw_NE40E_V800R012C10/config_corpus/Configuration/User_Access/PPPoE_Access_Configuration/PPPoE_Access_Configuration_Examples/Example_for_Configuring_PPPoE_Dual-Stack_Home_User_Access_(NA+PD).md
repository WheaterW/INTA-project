Example for Configuring PPPoE Dual-Stack Home User Access (NA+PD)
=================================================================

This section provides an example for configuring PPPoE dual-stack home user access in NA+PD mode. When a PPPoE dual-stack home user connects to a BRAS through a CPE, the BRAS implements RADIUS authentication and accounting and assigns IPv6 addresses in NA+PD mode to achieve user access.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0188720391__fig15251021112012), home users belong to the domain **isp1**, and each user uses the dual-stack access mode (NA+PD) and is connected to the Device through a CPE. After the CPE initiates a PPPoE connection request, the Device uses RADIUS for authentication and accounting, assigns an IPv4 address from a local address pool to the user, assigns an IPv6 prefix to the CPE through DHCPv6 IA\_PD, and assigns an IPv6 address to the CPE through DHCPv6 IA\_NA.

**Figure 1** Configuring PPPoE dual-stack home user access (NA+PD)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](figure/en-us_image_0193934244.png "Click to enlarge")
#### Configuration Roadmap

1. Configure AAA schemes.
2. Configure a RADIUS server group.
3. Configure an IPv4 address pool.
4. Configure IPv6 address pools.
5. Configure a user access domain.
6. Configure the BRAS to generate DUIDs for the DHCPv6 server.
7. Configure a virtual template.
8. Configure interfaces.
9. Configure routing protocols.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server addresses
* DNS server address
* IPv6 delegation prefix pool name, address prefix, and prefix length
* Names of IPv6 address pools
* User access domain name
* Interface IPv4 and IPv6 addresses

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] aaa
   ```
   ```
   [*Device-aaa] authentication-scheme auth1
   ```
   ```
   [*Device-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*Device-aaa-authen-auth1] quit
   ```
   ```
   [*Device-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~Device-aaa] accounting-scheme acct1
   ```
   ```
   [*Device-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*Device-aaa-accounting-acct1] quit
   ```
   ```
   [*Device-aaa] quit
   ```
   ```
   [*Device] commit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~Device] radius-server group rd1
   ```
   ```
   [*Device-radius-rd1] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*Device-radius-rd1] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*Device-radius-rd1] commit
   ```
   ```
   [~Device-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*Device-radius-rd1] commit
   ```
   ```
   [~Device-radius-rd1] quit
   ```
3. Configure a user-side local IPv4 address pool.
   
   
   ```
   [~Device] ip pool pool_v4 bas local
   ```
   ```
   [*Device-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0 
   ```
   ```
   [*Device-ip-pool-pool_v4] commit
   ```
   ```
   [~Device-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   ```
   ```
   [~Device-ip-pool-pool_v4] dns-server 10.179.155.161 10.179.155.177
   ```
   ```
   [*Device-ip-pool-pool_v4] commit
   ```
   ```
   [~Device-ip-pool-pool_v4] quit
   ```
4. Configure IPv6 address pools.
   
   
   1. Configure a local prefix pool for NA users.
      
      ```
      [~Device] ipv6 prefix ipv6_na local
      ```
      ```
      [*Device-ipv6-prefix-ipv6_na] prefix 2001:db8:1::/48
      ```
      ```
      [*Device-ipv6-prefix-ipv6_na] commit
      ```
      ```
      [~Device-ipv6-prefix-ipv6_na] quit
      ```
   2. Configure a user-side local address pool for NA users.
      ```
      [~Device] ipv6 pool ipv6_na bas local
      ```
      ```
      [*Device-ipv6-pool-ipv6_na] prefix ipv6_na
      ```
      ```
      [*Device-ipv6-pool-ipv6_na] dns-server 2001:db8::2:2 2001:db8::2:3
      ```
      ```
      [*Device-ipv6-pool-ipv6_na] commit
      ```
      ```
      [~Device-ipv6-pool-ipv6_na] quit
      ```
   3. Configure a delegation prefix pool for PD users.
      ```
      [~Device] ipv6 prefix pre_pd delegation
      ```
      ```
      [*Device-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
      ```
      ```
      [*Device-ipv6-prefix-pre_pd] commit
      ```
      ```
      [~Device-ipv6-prefix-pre_pd] pd-unshare-only
      ```
      ```
      [~Device-ipv6-prefix-pre_pd] quit
      ```
   4. Configure a delegation address pool for PD users.
      ```
      [~Device] ipv6 pool pool_pd bas delegation
      ```
      ```
      [*Device-ipv6-pool-pool_pd] prefix pre_pd
      ```
      ```
      [*Device-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
      ```
      ```
      [*Device-ipv6-pool-pool_pd] commit
      ```
      ```
      [~Device-ipv6-pool-pool_pd] quit
      ```
5. Configure a user access domain named **isp1**.
   
   
   ```
   [~Device] aaa
   ```
   ```
   [~Device-aaa] domain isp1
   ```
   ```
   [*Device-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*Device-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*Device-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*Device-aaa-domain-isp1] commit
   ```
   ```
   [~Device-aaa-domain-isp1] ipv6 nd autoconfig managed-address-flag  
   ```
   ```
   [~Device-aaa-domain-isp1] ip-pool pool_v4
   ```
   ```
   [~Device-aaa-domain-isp1] ipv6-pool ipv6_na
   ```
   ```
   [~Device-aaa-domain-isp1] ipv6-pool pool_pd
   ```
   ```
   [~Device-aaa-domain-isp1] quit
   ```
   ```
   [~Device-aaa] quit
   ```
6. Configure the BRAS to generate DUIDs for the DHCPv6 server.
   
   
   ```
   [~Device] dhcpv6 duid llt
   ```
   ```
   [*Device] commit
   ```
7. Configure a virtual template.
   
   
   ```
   [~Device] interface Virtual-Template1
   ```
   ```
   [*Device-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*Device-Virtual-Template1] commit
   ```
   ```
   [~Device-Virtual-Template1] quit
   ```
8. Configure interfaces.
   1. Configure a sub-interface and bind the virtual template to the sub-interface.
      
      
      ```
      [~Device] interface Eth-Trunk 2
      ```
      ```
      [*Device-Eth-Trunk2] interface Eth-Trunk 2.10
      ```
      ```
      [*Device-Eth-Trunk2.10] pppoe-server bind virtual-template 1
      ```
   2. Enable IPv6 on the sub-interface.
      
      
      ```
      [*Device-Eth-Trunk2.10] ipv6 enable
      ```
      ```
      [*Device-Eth-Trunk2.10] ipv6 address auto link-local
      ```
      ```
      [*Device-Eth-Trunk2.10] commit
      ```
      ```
      [~Device-Eth-Trunk2.10] user-vlan 3000 3799 qinq 2700 2955
      ```
      ```
      [~Device-Eth-Trunk2.10-vlan-3000-3799-QinQ-2700-2955] quit
      ```
   3. Configure a BAS interface.
      
      
      ```
      [~Device-Eth-Trunk2.10] bas
      ```
      ```
      [~Device-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
      ```
      ```
      [*Device-Eth-Trunk2.10-bas] commit
      ```
      ```
      [~Device-Eth-Trunk2.10-bas] quit
      ```
   4. Configure a network-side interface on the BRAS.
      
      
      ```
      [~Device] interface gigabitethernet 0/1/1
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ipv6 enable 
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ipv6 address 2001:db8:8::7 128
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ipv6 address auto link-local
      ```
      ```
      [*Device-GigabitEthernet0/1/1] ip address 10.2.1.1 24
      ```
   5. Configure loopback 100.
      
      
      ```
      [~Device] interface LoopBack100
      ```
      ```
      [*Device-LoopBack100] ipv6 enable
      ```
      ```
      [*Device-LoopBack100] ipv6 address 2001:db8:7::7 127
      ```
      ```
      [*Device-LoopBack100] ipv6 address auto link-local
      ```
      ```
      [*Device-LoopBack100] ip address 10.2.1.2 24
      ```
      ```
      [*Device-LoopBack100] isis enable 100
      ```
      ```
      [*Device-LoopBack100] isis ipv6 enable 100
      ```
      ```
      [*Device-LoopBack100] quit
      ```
      ```
      [*Device] commit
      ```
9. Configure routing protocols.
   1. Create an IS-IS process, and enable IPv6 for it.
      
      
      ```
      [~Device] isis 100
      ```
      ```
      [*Device-isis-100] is-level level-2
      ```
      ```
      [*Device-isis-100] cost-style wide
      ```
      ```
      [*Device-isis-100] network-entity 86.0451.1720.2803.5003.00
      ```
      ```
      [*Device-isis-100] ipv6 enable topology ipv6                
      ```
      ```
      [*Device-isis-100] ipv6 preference 20
      ```
      ```
      [*Device-isis-100] commit
      ```
      ```
      [~Device-isis-100] quit
      ```
      ```
      [~Device] interface gigabitethernet 0/1/1
      ```
      ```
      [~Device-GigabitEthernet0/1/1] isis enable 100 
      ```
      ```
      [*Device-GigabitEthernet0/1/1] isis ipv6 enable 100
      ```
      ```
      [*Device-GigabitEthernet0/1/1] isis ipv6 cost 50 level-2 
      ```
      ```
      [*Device-GigabitEthernet0/1/1] quit
      ```
      ```
      [*Device] commit
      ```
   2. Configure BGP.
      
      
      ```
      [~Device] bgp 100
      ```
      ```
      [*Device-bgp] group group1 internal
      ```
      ```
      [*Device-bgp] peer group1 connect-interface LoopBack100
      ```
      ```
      [*Device-bgp] group group2 external
      ```
      ```
      [*Device-bgp] peer group2 connect-interface LoopBack100
      ```
      ```
      [*Device-bgp] peer 2001:db8:7::2101 as-number 100 
      ```
      ```
      [*Device-bgp] peer 2001:db8:7::2101 group group1 
      ```
      ```
      [*Device-bgp] peer 2001:db8:7::2102 as-number 100 
      ```
      ```
      [*Device-bgp] peer 2001:db8:7::2102 group group1 
      ```
      ```
      [*Device-bgp] peer 2.2.2.2 as-number 101
      ```
      ```
      [*Device-bgp] peer 2.2.2.2 group group2 
      ```
      ```
      [*Device-bgp] peer 3.3.3.3 as-number 101 
      ```
      ```
      [*Device-bgp] peer 3.3.3.3 group group2 
      ```
      
      
      ```
      [*Device-bgp] ipv4-family unicast
      ```
      ```
      [*Device-bgp-af-ipv4] import-route unr
      ```
      ```
      [*Device-bgp-af-ipv4] quit 
      ```
      ```
      [*Device-bgp] ipv6-family unicast
      ```
      ```
      [*Device-bgp-af-ipv6] import-route unr  
      ```
      ```
      [*Device-bgp-af-ipv6] quit
      ```
      ```
      [*Device-bgp] quit
      ```
      ```
      [~Device] commit
      ```

#### Configuration Files

```
#
sysname Device
#                                                                               
radius-server group rd1                                                         
 radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
#
 radius-server authentication 192.168.7.249 1645 weight 0                       
 radius-server accounting 192.168.7.249 1646 weight 0                                                                                                                                                              #
aaa
 authentication-scheme auth1
  authentication-mode radius
 accounting-scheme acct1  
  accounting-mode radius
#                                                                               
ip pool pool_v4 bas local                                                         
 gateway 172.16.0.1 255.255.255.0                                                
 section 0 172.16.0.2 172.16.0.200    
 dns-server 10.179.155.161 10.179.155.177                                             
#
ipv6 prefix ipv6_na delegation
 prefix 2001:db8:1::/48
#
ipv6 pool ipv6_na bas local
 prefix ipv6_na
 dns-server 2001:db8::2:2 2001:db8::2:3
#
ipv6 prefix pre_pd delegation
 prefix 2001:db8:2::/48 delegating-prefix-length 60
 pd-unshare-only
#
ipv6 pool pool_pd bas delegation
 prefix pre_pd
 dns-server 2001:db8::2:2 2001:db8::2:3
# 
aaa                                                                             
 domain isp1                                                                    
  authentication-scheme auth1                                                   
  accounting-scheme acct1                                                       
  radius-server group rd1
  ipv6 nd autoconfig managed-address-flag  
  ip-pool pool_v4
  ipv6-pool ipv6_na
  ipv6-pool pool_pd
#
dhcpv6 duid 0001000125a7625df063f9761497  
#                                                                            
interface Virtual-Template1                                                     
 ppp authentication-mode chap                                                   
#
isis 100
 is-level level-2
 cost-style wide
 network-entity 86.0451.1720.2803.5003.00
 #
 ipv6 enable topology ipv6                
 ipv6 preference 20
#
interface Eth-Trunk 2
#
interface Eth-Trunk2.10                                                            
 pppoe-server bind Virtual-Template 1
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 3000 3799 qinq 2700 2955
 bas 
  #                                                                           
  access-type layer2-subscriber default-domain authentication isp1              
#
interface GigabitEthernet 0/1/1
 ipv6 enable
 ipv6 address 2001:db8:8::7 128
 ipv6 address auto link-local
 ip address 10.2.1.1 24
 isis enable 100
 isis ipv6 enable 100
 isis ipv6 cost 50 level-2 
 #
#                                                                               
interface LoopBack100                                                           
 ipv6 enable
 ipv6 address 2001:db8:7::7 127
 ipv6 address auto link-local
 ip address 10.2.1.2 24
 isis enable 100
 isis ipv6 enable 100
#                                                                               
bgp 100
 group group1 internal
 peer group1 connect-interface LoopBack100
 group group2 external
 peer group2 connect-interface LoopBack100
 peer 2001:db8:7::2101 as-number 100
 peer 2001:db8:7::2101 group group1 
 peer 2001:db8:7::2102 as-number 100 
 peer 2001:db8:7::2102 group group1 
 peer 2.2.2.2 as-number 101
 peer 2.2.2.2 group group2 
 peer 3.3.3.3 as-number 101 
 peer 3.3.3.3 group group2 
 #
 ipv4-family unicast
  import-route unr 
 # 
 ipv6-family unicast
  import-route unr
#
return                                       
```