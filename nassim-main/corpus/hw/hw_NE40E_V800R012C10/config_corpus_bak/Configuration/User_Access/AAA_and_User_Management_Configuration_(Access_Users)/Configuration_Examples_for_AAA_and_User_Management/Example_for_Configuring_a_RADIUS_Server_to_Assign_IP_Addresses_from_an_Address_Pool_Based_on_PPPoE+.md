Example for Configuring a RADIUS Server to Assign IP Addresses from an Address Pool Based on PPPoE+
===================================================================================================

This section provides an example for configuring a RADIUS server to assign IP addresses from an address pool based on PPPoE+. With the Option 82 function enabled, a BRAS assigns IP addresses to PPPoE users based on the address pool information carried in an authentication response packet sent by the RADIUS server.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0210795990__fig1244122710413), a user initiates a PPPoE dialup. The PPPoE+ function is enabled on the OLT. When transparently transmitting PPPoE packets, the OLT inserts the access-line-id (PPPoE+) information that identifies the physical location of a user into the PPPoE packets. The Option 82 function is enabled on the BRAS. The BRAS trusts the access-line-id information in the packets sent by a client and does not change the access-line-id information before forwarding the packets from the client to the RADIUS server. The RADIUS attribute dictionary file needs to be loaded on the RADIUS server in advance. After receiving an authentication request packet from a user, the RADIUS server delivers the IPv4 address pool attribute through the Framed-Pool attribute in an authentication response packet based on the access-line-id information carried in the authentication request packet. Also, the RADIUS server delivers the IPv6 address pool attribute through the Framed-IPv6-Pool (100) and HW-Delegated-IPv6-Prefix-Pool (191) attributes in the authentication response packet. The address pool name configured on the BRAS must be the same as that on the RADIUS server. The BRAS assigns an IP address to the user based on the address pool information carried in the authentication response packet.

**Figure 1** Configuring a RADIUS server to assign IP addresses from an address pool based on PPPoE+![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/2 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0210942500.png)

#### Configuration Roadmap

1. Configure AAA schemes.
2. Configure a RADIUS server group.
3. Configure address pools.
4. Configure a user access domain.
5. Configure the BRAS to generate a DUID for the DHCPv6 server.
6. Configure a virtual template.
7. Configure interfaces.
8. Configure routing protocols.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names (RADIUS authentication is performed for users on the BRAS.)
* RADIUS server group name and RADIUS server addresses
* DNS server address
* Name of the delegation prefix pool for IPv6 users, assignable prefixes, and prefix lengths
* Name of the delegation address pool for IPv6 users
* User access domain
* IPv4 and IPv6 addresses of interfaces

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] quit
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd1
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*HUAWEI-radius-rd1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
3. Configure a local address pool for IPv4 users.
   
   
   ```
   [~HUAWEI] ip pool pool_v4 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0 
   ```
   ```
   [*HUAWEI-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
   ```
   ```
   [*HUAWEI-ip-pool-pool_v4] quit
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure address pools for IPv6 users.
   
   
   1. Configure a delegation prefix pool for ND users.
      
      ```
      [~HUAWEI] ipv6 prefix pre_nd delegation
      ```
      ```
      [*HUAWEI-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48 delegating-prefix-length 64
      ```
      ```
      [*HUAWEI-ipv6-prefix-pre_nd] slaac-unshare-only
      ```
      ```
      [*HUAWEI-ipv6-prefix-pre_nd] quit
      ```
   2. Configure a delegation address pool for ND users.
      ```
      [*HUAWEI] ipv6 pool pool_nd bas delegation
      ```
      ```
      [*HUAWEI-ipv6-pool-pool_nd] prefix pre_nd
      ```
      ```
      [*HUAWEI-ipv6-pool-pool_nd] dns-server 2001:db8:1::2 2001:db8:1::3
      ```
      ```
      [*HUAWEI-ipv6-pool-pool_nd] quit
      ```
   3. Configure a delegation prefix pool for PD users.
      ```
      [*HUAWEI] ipv6 prefix pre_pd delegation
      ```
      ```
      [*HUAWEI-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48 delegating-prefix-length 60
      ```
      ```
      [*HUAWEI-ipv6-prefix-pre_pd] pd-unshare-only
      ```
      ```
      [*HUAWEI-ipv6-prefix-pre_pd] quit
      ```
   4. Configure a delegation address pool for PD users.
      ```
      [*HUAWEI] ipv6 pool pool_pd bas delegation
      ```
      ```
      [*HUAWEI-ipv6-pool-pool_pd] prefix pre_pd
      ```
      ```
      [*HUAWEI-ipv6-pool-pool_pd] dns-server 2001:db8:1::2 2001:db8:1::3
      ```
      ```
      [*HUAWEI-ipv6-pool-pool_pd] quit
      ```
      ```
      [*HUAWEI] commit
      ```
5. Configure a user access domain named **isp1**.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] prefix-assign-mode unshared  
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] ip-pool pool_v4
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] ipv6-pool pool_nd
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] ipv6-pool pool_pd
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
   ```
   [*HUAWEI] commit
   ```
6. Configure the BRAS to generate a DUID for the DHCPv6 server.
   
   
   ```
   [~HUAWEI] dhcpv6 duid llt
   ```
   ```
   Warning:The change of DUID will cause the accessed user work abnormally.
   ```
7. Configure a virtual template.
   
   
   ```
   [*HUAWEI] interface Virtual-Template1
   ```
   ```
   [*HUAWEI-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*HUAWEI-Virtual-Template1] quit
   ```
   ```
   [*HUAWEI] commit
   ```
8. Configure interfaces.
   1. Bind the VT to a sub-interface.
      
      
      ```
      [~HUAWEI] interface GigabitEthernet0/1/2.10
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10] pppoe-server bind virtual-template 1
      ```
   2. Enable IPv6 on the interface.
      
      
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10] ipv6 enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10] ipv6 address auto link-local
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.10] user-vlan 4003
      ```
   3. Configure a BAS interface.
      
      
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10-vlan-4003-4003] bas
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10-bas] access-type layer2-subscriber default-domain authentication isp1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10-bas] client-option82
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10-bas] authentication-method ppp web 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10-bas] authentication-method-ipv6 ppp web
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.10-bas] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.10-bas] quit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.10] quit
      ```
   4. Configure the network-side interface of the BRAS.
      
      
      ```
      [~HUAWEI] interface gigabitethernet 0/1/1
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1] ipv6 enable 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] ipv6 address 2001:db8:8::7 128
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] ipv6 address auto link-local
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] ip address 10.2.1.1 24
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] quit
      ```
      ```
      [*HUAWEI] commit
      ```
   5. Configure loopback 100 as the source interface for sending BGP packets.
      
      
      ```
      [~HUAWEI] interface LoopBack100
      ```
      ```
      [*HUAWEI-LoopBack100] ipv6 enable
      ```
      ```
      [*HUAWEI-LoopBack100] ipv6 address 2001:db8:7::7 127
      ```
      ```
      [*HUAWEI-LoopBack100] ipv6 address auto link-local
      ```
      ```
      [*HUAWEI-LoopBack100] ip address 10.10.10.10 16
      ```
      ```
      [*HUAWEI-LoopBack100] quit
      ```
      ```
      [*HUAWEI] commit
      ```
9. Configure routing protocols.
   1. Create an IS-IS process and enable IS-IS on the network-side interface of the BRAS.
      
      
      ```
      [~HUAWEI] isis 100
      ```
      ```
      [*HUAWEI-isis-100] is-level level-2
      ```
      ```
      [*HUAWEI-isis-100] cost-style wide
      ```
      ```
      [*HUAWEI-isis-100] network-entity 86.0451.1720.2803.5003.00
      ```
      ```
      [*HUAWEI-isis-100] ipv6 enable topology ipv6                
      ```
      ```
      [*HUAWEI-isis-100] ipv6 preference 20
      ```
      ```
      [*HUAWEI-isis-100] quit
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~HUAWEI] interface GigabitEthernet 0/1/1
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1] isis enable 100
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] isis ipv6 enable 100
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] isis ipv6 cost 500 level-2
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1] quit
      ```
      ```
      [~HUAWEI] interface LoopBack100
      ```
      ```
      [~HUAWEI-LoopBack100] isis enable 100
      ```
      ```
      [*HUAWEI-LoopBack100] isis ipv6 enable 100
      ```
      ```
      [*HUAWEI-LoopBack100] commit
      ```
      ```
      [~HUAWEI-LoopBack100] quit
      ```
   2. Configure BGP.
      
      
      ```
      [~HUAWEI] bgp 100
      ```
      ```
      [*HUAWEI-bgp] group group1 internal
      ```
      ```
      [*HUAWEI-bgp] peer group1 connect-interface LoopBack100
      ```
      ```
      [*HUAWEI-bgp] group group2 external
      ```
      ```
      [*HUAWEI-bgp] peer group2 connect-interface LoopBack100
      ```
      ```
      [*HUAWEI-bgp] peer 2001:db8:7::2101 as-number 100 
      ```
      ```
      [*HUAWEI-bgp] peer 2001:db8:7::2101 group group1 
      ```
      ```
      [*HUAWEI-bgp] peer 2001:db8:7::2102 as-number 100 
      ```
      ```
      [*HUAWEI-bgp] peer 2001:db8:7::2102 group group1 
      ```
      ```
      [*HUAWEI-bgp] peer 2.2.2.2 as-number 101
      ```
      ```
      [*HUAWEI-bgp] peer 2.2.2.2 group group2 
      ```
      ```
      [*HUAWEI-bgp] peer 3.3.3.3 as-number 101 
      ```
      ```
      [*HUAWEI-bgp] peer 3.3.3.3 group group2 
      ```
      
      
      ```
      [*HUAWEI-bgp] ipv4-family unicast
      ```
      ```
      [*HUAWEI-bgp-af-ipv4] import-route unr
      ```
      ```
      [*HUAWEI-bgp-af-ipv4] quit 
      ```
      ```
      [*HUAWEI-bgp] ipv6-family unicast
      ```
      ```
      [*HUAWEI-bgp-af-ipv6] import-route unr
      ```
      ```
      [~HUAWEI-bgp-af-ipv6] quit
      ```
      ```
      [*HUAWEI-bgp] quit
      ```
      ```
      [*HUAWEI] commit
      ```

#### Configuration Files

```
#
sysname HUAWEI                                                         
#                                                                               
radius-server group rd1                                                         
 radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
 radius-server authentication 192.168.7.249 1645 weight 0                       
 radius-server accounting 192.168.7.249 1646 weight 0
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 accounting-scheme acct1  
  accounting-mode radius
#                                                                               
ip pool pool_v4 bas local                                                         
 gateway 172.16.0.1 255.255.255.0                                                
 section 0 172.16.0.2 172.16.0.200                                                 
#
ipv6 prefix pre_nd delegation
 prefix 2001:db8:1::/48 delegating-prefix-length 64
 slaac-unshare-only
#
ipv6 pool pool_nd bas delegation
 prefix pre_nd
 dns-server 2001:db8:1::2 2001:db8:1::3
#
ipv6 prefix pre_pd delegation
 prefix 2001:db8:2::/48 delegating-prefix-length 60
 pd-unshare-only
#
ipv6 pool pool_pd bas delegation
 prefix pre_pd
 dns-server 2001:db8:1::2 2001:db8:1::3
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
#
dhcpv6 duid llt
#                                                                               
interface Virtual-Template1                                                     
 ppp authentication-mode chap                                                   
#
isis 100
 is-level level-2
 cost-style wide
 network-entity 86.0451.1720.2803.5003.00
 ipv6 enable topology ipv6                
 ipv6 preference 20
#
interface GigabitEthernet0/1/2
#
interface GigabitEthernet0/1/2.10                                                            
 pppoe-server bind Virtual-Template 1
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 4003
 bas                                                                            
  access-type layer2-subscriber default-domain authentication isp1
  client-option82
  authentication-method ppp web
  authentication-method-ipv6 ppp web
#
interface GigabitEthernet0/1/1
 ipv6 enable
 ipv6 address 2001:db8:8::7 128
 ipv6 address auto link-local
 ip address 10.2.1.1 24
 isis enable 100
 isis ipv6 enable 100
 isis ipv6 cost 500 level-2 
#                                                                               
interface LoopBack100                                                           
 ipv6 enable
 ipv6 address 2001:db8:7::7 127
 ipv6 address auto link-local
 ip address 10.10.10.10 16
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
 ipv4-family unicast
  import-route unr
 # 
 ipv6-family unicast
  import-route unr
#
return                                       
```