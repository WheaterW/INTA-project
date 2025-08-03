Example for Configuring PPPoE Dual-Stack Home User Access (ND Unshared+PD) to a VPN
===================================================================================

This section provides an example for configuring PPPoE dual-stack home user access to a VPN in ND unshared+PD mode. The BRAS implements RADIUS authentication and accounting and assigns IPv6 addresses to users through ND. This allows users to access the network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0249630694__fig_dc_ne_pppox_cfg_0287), home users belong to the domain **isp1**, and each user uses the dual-stack access mode. Only IPv4 users, but not IPv6 users, are connected to the VPN. Users are connected to DeviceA through a CPE. After the CPE initiates a PPPoE connection, DeviceA implements RADIUS authentication and accounting, as well as assigns IPv4 addresses to users from the local address pool and an IPv6 address to the CPE through ND. DeviceA authenticates and manages the CPE, which manages home terminals.

**Figure 1** Configuring PPPoE dual-stack home user access (ND unshared+PD) to a VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent Eth-Trunk 2.10 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0249630695.png "Click to enlarge")

#### Configuration Roadmap

1. Configure AAA schemes.
2. Configure a RADIUS server group.
3. Configure a VPN instance.
4. Configure a user-side local IPv4 address pool.
5. Configure IPv6 address pools.
6. Configure a user access domain.
7. Configure the BRAS to generate DUIDs.
8. Configure a virtual template.
9. Configure interfaces.
10. Configure routing protocols.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server addresses
* DNS server address
* Name, address prefix, and prefix length of the IPv6 delegation prefix pool
* Name of the IPv6 delegation address pool
* Domain to which users belong
* Interface IPv4 and IPv6 addresses

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] authentication-scheme auth1
   ```
   ```
   [*DeviceA-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*DeviceA-aaa-authen-auth1] quit
   ```
   ```
   [*DeviceA-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~DeviceA-aaa] accounting-scheme acct1
   ```
   ```
   [*DeviceA-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*DeviceA-aaa-accounting-acct1] quit
   ```
   ```
   [*DeviceA-aaa] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~DeviceA] radius-server group rd1
   ```
   ```
   [*DeviceA-radius-rd1] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*DeviceA-radius-rd1] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*DeviceA-radius-rd1] commit
   ```
   ```
   [~DeviceA-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*DeviceA-radius-rd1] commit
   ```
   ```
   [~DeviceA-radius-rd1] quit
   ```
3. Configure a VPN instance.
   
   
   ```
   [~DeviceA] ip vpn-instance vpn1
   ```
   ```
   [*DeviceA-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DeviceA-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:200
   ```
   ```
   [*DeviceA-vpn-instance-vpn1-af-ipv4] vpn-target 100:100 export-extcommunity
   ```
   ```
   [*DeviceA-vpn-instance-vpn1-af-ipv4] vpn-target 100:100 import-extcommunity
   ```
   ```
   [*DeviceA-vpn-instance-vpn1-af-ipv4] commit
   ```
   ```
   [~DeviceA-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [~DeviceA-vpn-instance-vpn1] quit
   ```
4. Configure a user-side local IPv4 address pool.
   
   
   ```
   [~DeviceA] ip pool pool_v4 bas local
   ```
   ```
   [*DeviceA-ip-pool-pool_v4] vpn-instance vpn1
   ```
   ```
   [*DeviceA-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0 
   ```
   ```
   [*DeviceA-ip-pool-pool_v4] commit
   ```
   ```
   [~DeviceA-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   ```
   ```
   [~DeviceA-ip-pool-pool_v4] dns-server 10.179.155.161 10.179.155.177
   ```
   ```
   [*DeviceA-ip-pool-pool_v4] commit
   ```
   ```
   [~DeviceA-ip-pool-pool_v4] quit
   ```
5. Configure IPv6 address pools.
   
   
   1. Configure a delegation prefix pool for ND users.
      
      ```
      [~DeviceA] ipv6 prefix pre_nd delegation
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48 delegating-prefix-length 64
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_nd] slaac-unshare-only
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_nd] commit
      ```
      ```
      [~DeviceA-ipv6-prefix-pre_nd] quit
      ```
   2. Configure a delegation address pool for ND users.
      ```
      [~DeviceA] ipv6 pool pool_nd bas delegation
      ```
      ```
      [*DeviceA-ipv6-pool-pool_nd] prefix pre_nd
      ```
      ```
      [*DeviceA-ipv6-pool-pool_nd] dns-server 2001:db8::2:2 2001:db8::2:3
      ```
      ```
      [*DeviceA-ipv6-pool-pool_nd] commit
      ```
      ```
      [~DeviceA-ipv6-pool-pool_nd] quit
      ```
   3. Configure a delegation prefix pool for PD users.
      ```
      [~DeviceA] ipv6 prefix pre_pd delegation
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
      ```
      ```
      [*DeviceA-ipv6-prefix-pre_pd] commit
      ```
      ```
      [~DeviceA-ipv6-prefix-pre_pd] pd-unshare-only
      ```
      ```
      [~DeviceA-ipv6-prefix-pre_pd] quit
      ```
   4. Configure a delegation address pool for PD users.
      ```
      [~DeviceA] ipv6 pool pool_pd bas delegation
      ```
      ```
      [*DeviceA-ipv6-pool-pool_pd] prefix pre_pd
      ```
      ```
      [*DeviceA-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
      ```
      ```
      [*DeviceA-ipv6-pool-pool_pd] commit
      ```
      ```
      [~DeviceA-ipv6-pool-pool_pd] quit
      ```
6. Configure a user access domain named **isp1**.
   
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [~DeviceA-aaa] domain isp1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceA-aaa-domain-isp1] prefix-assign-mode unshared  
   ```
   ```
   [~DeviceA-aaa-domain-isp1] ip-pool pool_v4
   ```
   ```
   [~DeviceA-aaa-domain-isp1] ipv6-pool pool_nd
   ```
   ```
   [~DeviceA-aaa-domain-isp1] ipv6-pool pool_pd
   ```
   ```
   [~DeviceA-aaa-domain-isp1] vpn-instance vpn1
   ```
   ```
   [~DeviceA-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
7. Configure DeviceA to generate DUIDs in DUID-LLT mode. (This step is not required if a DUID has been configured on DeviceA.)
   
   
   ```
   [~DeviceA] dhcpv6 duid llt
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure a virtual template.
   
   
   ```
   [~DeviceA] interface Virtual-Template1
   ```
   ```
   [*DeviceA-Virtual-Template1] ppp authentication-mode pap chap
   ```
   ```
   [*DeviceA-Virtual-Template1] commit
   ```
   ```
   [~DeviceA-Virtual-Template1] quit
   ```
9. Configure interfaces.
   1. Configure a sub-interface and bind the virtual template to the sub-interface.
      
      
      ```
      [~DeviceA] interface Eth-Trunk 2
      ```
      ```
      [*DeviceA-Eth-Trunk2] interface Eth-Trunk 2.10
      ```
      ```
      [*DeviceA-Eth-Trunk2.10] pppoe-server bind virtual-template 1
      ```
   2. Enable IPv6 on the sub-interface.
      
      
      ```
      [*DeviceA-Eth-Trunk2.10] ipv6 enable
      ```
      ```
      [*DeviceA-Eth-Trunk2.10] ipv6 address auto link-local
      ```
      ```
      [*DeviceA-Eth-Trunk2.10] commit
      ```
      ```
      [~DeviceA-Eth-Trunk2.10] user-vlan 3000 3799 qinq 2700 2955
      ```
      ```
      [~DeviceA-Eth-Trunk2.10-vlan-3000-3799-QinQ-2700-2955] quit
      ```
   3. Configure a BAS interface.
      
      
      ```
      [~DeviceA-Eth-Trunk2.10] bas
      ```
      ```
      [~DeviceA-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
      ```
      ```
      [*DeviceA-Eth-Trunk2.10-bas] commit
      ```
      ```
      [~DeviceA-Eth-Trunk2.10-bas] quit
      ```
   4. Configure a network-side interface on DeviceA.
      
      
      ```
      [~DeviceA] interface gigabitethernet 0/1/1
      ```
      ```
      [*DeviceA-GigabitEthernet0/1/1] ipv6 enable 
      ```
      ```
      [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8:8::7 128
      ```
      ```
      [*DeviceA-GigabitEthernet0/1/1] ipv6 address auto link-local
      ```
      ```
      [*DeviceA-GigabitEthernet0/1/1] ip address 10.2.1.1 24
      ```
      ```
      [*DeviceA-GigabitEthernet0/1/1] commit
      ```

#### Configuration Files

```
#
sysname DeviceA                                                         
#                                                                               
radius-server group rd1                                                         
 radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
#  
 radius-server authentication 192.168.7.249 1645 weight 0                       
 radius-server accounting 192.168.7.249 1646 weight 0
#                                                                               
ip vpn-instance vpn1                                                            
 ipv4-family                                                                    
  route-distinguisher 200:200                                                   
  apply-label per-route                                                         
  vpn-target 100:100 export-extcommunity                                        
  vpn-target 100:100 import-extcommunity  
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 accounting-scheme acct1  
  accounting-mode radius
#                                                                               
ip pool pool_v4 bas local                                                         
 vpn-instance vpn1 
 gateway 172.16.0.1 255.255.255.0                                                
 section 0 172.16.0.2 172.16.0.200  
 dns-server 10.179.155.161 10.179.155.177                                                
#
ipv6 prefix pre_nd delegation
 prefix 2001:db8:1::/48 delegating-prefix-length 64
 slaac-unshare-only
#
ipv6 pool pool_nd bas delegation
 prefix pre_nd
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
  prefix-assign-mode unshared  
  ip-pool pool_v4
  ipv6-pool pool_nd
  ipv6-pool pool_pd
  vpn-instance vpn1
#
dhcpv6 duid 0001000125a7625df063f9761497
#                                                                               
interface Virtual-Template1                                                     
 ppp authentication-mode pap chap                                                   
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
interface GigabitEthernet0/1/1
 ipv6 enable
 ipv6 address 2001:db8:8::7 128
 ipv6 address auto link-local
 ip address 10.2.1.1 24
 #
#
return                                       
```