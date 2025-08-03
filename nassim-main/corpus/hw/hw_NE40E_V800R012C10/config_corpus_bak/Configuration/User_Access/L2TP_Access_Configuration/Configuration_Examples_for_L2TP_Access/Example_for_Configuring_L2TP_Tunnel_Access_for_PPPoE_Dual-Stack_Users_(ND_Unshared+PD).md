Example for Configuring L2TP Tunnel Access for PPPoE Dual-Stack Users (ND Unshared+PD)
======================================================================================

Example_for_Configuring_L2TP_Tunnel_Access_for_PPPoE_Dual-Stack_Users_(ND_Unshared+PD)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001201216870__fig_dc_ne_l2tp_cfg_01350701), users want to remotely access an enterprise's private network. As such, a point-to-point L2TP tunnel is established on the public network. The LAC and LNS are connected through a WAN. PPP data frames are encapsulated and transmitted through the L2TP tunnel. RADIUS authentication and accounting are used on both the LAC and LNS. After accessing the public network, remote users access internal network resources through the L2TP tunnel. To allow the users to access IPv4 and IPv6 networks, configure the LNS to use a local address pool to assign IPv4 addresses to the users, use DHCPv6 IA\_PD to assign IPv6 prefixes to them, and use ND to assign IPv6 addresses to them.

**Figure 1** Configuring L2TP tunnel access for PPPoE dual-stack users (ND unshared+PD)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/1/0.

![](figure/en-us_image_0000001201376838.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the LAC.
   
   * Configure an interface address for the LAC.
   * Enable basic L2TP functions.
   * Configure an L2TP tunnel connection on the LAC.
   * Configure a tunnel authentication mode.
   * Configure the PPPoE access service for the LAC.
2. Configure the LNS.
   
   * Configure an interface address for the LNS and enable IPv6 on the interface.
   * Configure a VT.
   * Enable basic L2TP functions.
   * Configure an L2TP tunnel connection on the LNS.
   * Configure a tunnel authentication mode and user authentication mode.
   * Configure LNS-side tunnel parameters.
   * Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   * Configure address pools, including a local IPv4 address pool and an IPv6 delegation prefix pool.
   * Configure an L2TP user domain and specify address pools in the domain.
   * Configure a RADIUS server group.

#### Data Preparation

To complete the configuration, you need the following data:

* Identical domain names, usernames, and passwords on the LAC and LNS
* LNS-side tunnel authentication mode (CHAP is used in this example) and tunnel password
* LNS-side local and remote tunnel names
* VT number
* L2TP group ID
* Names and address ranges of address pools
* AAA domain name
* User authentication mode on DeviceA/DeviceB (RADIUS authentication)

#### Procedure

1. Configure DeviceA that functions as the LAC.
   
   
   
   # Configure network-side interfaces.
   
   ```
   <Device> system-view
   [~Device] sysname DeviceA
   [*Device] commit
   [~DeviceA] interface gigabitethernet 0/1/0
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.38.160.1 255.255.255.0
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/0] commit
   [~DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] ip address 10.1.1.1 255.255.255.0
   [*DeviceA-LoopBack1] ipv6 enable
   [*DeviceA-LoopBack1] ipv6 address auto link-local
   [*DeviceA-LoopBack1] commit
   [~DeviceA-LoopBack1] quit
   [*DeviceA] interface Loopback2
   [*DeviceA-LoopBack2] ipv6 enable
   [*DeviceA-LoopBack2] ipv6 address 2001:db8::2:2 64
   [*DeviceA-LoopBack2] ipv6 address auto link-local
   [*DeviceA-LoopBack2] ip address 10.2.2.2 255.255.255.0
   [*DeviceA-LoopBack2] quit
   [*DeviceA] commit
   ```
   
   # Enable basic L2TP functions and configure an L2TP connection on the LAC.
   
   ```
   [~DeviceA] l2tp enable
   [*DeviceA] l2tp-group group1
   [*DeviceA-l2tp-group1] tunnel name LAC
   [*DeviceA-l2tp-group1] start l2tp ip 10.38.160.2
   [*DeviceA-l2tp-group1] tunnel source loopback1
   [*DeviceA-l2tp-group1] commit
   ```
   
   # Configure a tunnel authentication mode.
   
   ```
   [~DeviceA-l2tp-group1] tunnel authentication
   [*DeviceA-l2tp-group1] tunnel password cipher YsHsjx_202206
   [*DeviceA-l2tp-group1] commit
   [~DeviceA-l2tp-group1] quit
   ```
   
   # Configure the PPPoE access service.
   
   1. # Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
      ```
      [~DeviceA] radius local-ip all
      [~DeviceA] commit
      ```
   2. Configure AAA schemes.
      ```
      [~DeviceA] aaa
      [~DeviceA-aaa] authentication-scheme auth1
      [*DeviceA-aaa-authen-radius] authentication-mode radius
      [*DeviceA-aaa-authen-radius] commit
      [~DeviceA-aaa-authen-radius] quit
      [~DeviceA-aaa] accounting-scheme acct1
      [*DeviceA-aaa-accounting-acct1] accounting-mode radius
      [*DeviceA-aaa-accounting-acct1] quit
      [*DeviceA-aaa] commit
      [*DeviceA-aaa] quit
      ```
   3. Configure a RADIUS server group.
      ```
      [~DeviceA] radius-server group rd1
      [*DeviceA-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
      [*DeviceA-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
      [*DeviceA-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
      [*DeviceA-radius-rd1] radius-server source interface Loopback2
      [*DeviceA-radius-rd1] commit 
      [~DeviceA-radius-rd1] radius-server calling-station-id include mac
      [~DeviceA-radius-rd1] radius-server user-name original
      [*DeviceA-radius-rd1] commit 
      [~DeviceA-radius-rd1] radius-server class-as-car
      [*DeviceA-radius-rd1] quit
      [*DeviceA] commit
      ```
   4. # Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode. (This step is not required if a DUID has been configured on DeviceA.)
      ```
      [~DeviceA] dhcpv6 duid llt
      [*DeviceA] commit
      ```
   5. Configure a user access domain.
      ```
      [~DeviceA] aaa
      [~DeviceA-aaa] domain isp1
      [*DeviceA-aaa-domain-isp1] authentication-scheme auth1 
      [*DeviceA-aaa-domain-isp1] accounting-scheme acct1
      [*DeviceA-aaa-domain-isp1] radius-server group rd1
      [*DeviceA-aaa-domain-isp1] commit
      [*DeviceA-aaa-domain-isp1] idle-cut 60 500
      [~DeviceA-aaa-domain-isp1] l2tp-group group1
      [*DeviceA-aaa-domain-isp1] commit
      [~DeviceA-aaa-domain-isp1] quit
      [~DeviceA-aaa] quit
      ```
   6. Configure a VT.
      ```
      [~DeviceA] interface virtual-template 1
      [*DeviceA-Virtual-Template1] ppp authentication-mode chap
      [*DeviceA-Virtual-Template1] commit
      [~DeviceA-Virtual-Template1] quit
      ```
   7. # Configure the Eth-Trunk interface to work in static LACP mode, set a timeout period for the interface to receive LACPDUs, and specify the VT.
      ```
      [~DeviceA] interface Eth-Trunk2
      [*DeviceA-Eth-Trunk2] mode lacp-static
      [*DeviceA-Eth-Trunk2] lacp timeout fast
      [*DeviceA-Eth-Trunk2] commit
      ```
   8. Bind VT1 to Eth-Trunk2.10.
      ```
      [~DeviceA-Eth-Trunk2] interface Eth-Trunk2.10
      [*DeviceA-Eth-Trunk2.10] ipv6 enable
      [*DeviceA-Eth-Trunk2.10] ipv6 address auto link-local
      [*DeviceA-Eth-Trunk2.10] pppoe-server bind virtual-template 1
      [*DeviceA-Eth-Trunk2.10] commit
      [~DeviceA-Eth-Trunk2.10] user-vlan 1000 4000 qinq 2000 2001
      [~DeviceA-Eth-Trunk2.10-user-vlan-1000-4000-qinq-2000-2001] quit
      ```
   9. Configure a BAS interface.
      ```
      [~DeviceA-Eth-Trunk2.10] bas
      [~DeviceA-Eth-Trunk2.10-bas] access-type layer2-subscriber default-domain authentication isp1
      [*DeviceA-Eth-Trunk2.10-bas] commit
      [~DeviceA-Eth-Trunk2.10-bas] quit
      ```
   
   Configure a routing protocol.
   1. Enable the function to automatically control a route's cost preference.
      ```
      [~DeviceA] peer-backup route-cost auto-advertising
      [*DeviceA] commit
      ```
   2. Configure MPLS.
      ```
      [~DeviceA] mpls
      [~DeviceA-mpls] mpls ldp
      [~DeviceA-mpls] quit
      [~DeviceA] mpls lsr-id 10.1.1.1
      [*DeviceA] interface GigabitEthernet0/1/0
      [*DeviceA-GigabitEthernet0/1/0] mpls
      [*DeviceA-GigabitEthernet0/1/0] mpls ldp
      [*DeviceA-GigabitEthernet0/1/0] quit
      [*DeviceA ] commit
      ```
   3. # Configure OSPF to import UNRs.
      ```
      [~DeviceA] ospf 1
      [*DeviceA-ospf-1] default cost inherit-metric
      [*DeviceA-ospf-1] import-route unr
      [*DeviceA-ospf-1] area 0
      [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
      [*DeviceA-ospf-1-area-0.0.0.0] network 10.38.160.1 0.0.0.255
      [*DeviceA-ospf-1-area-0.0.0.0] quit
      [*DeviceA-ospf-1] quit
      [*DeviceA] commit
      ```
2. Configure DeviceB that functions as the LNS.
   
   
   
   # Assign an IP address to the interface connected to the tunnel and enable IPv6 on the interface.
   
   ```
   <Device> system-view
   [~Device] sysname DeviceB
   [*Device] commit
   [~DeviceB] interface gigabitethernet 0/1/0
   [*DeviceB-gigabitethernet0/1/0] ip address 10.38.160.2 255.255.255.0
   [*DeviceB-gigabitethernet0/1/0] ipv6 enable
   [*DeviceB-gigabitethernet0/1/0] ipv6 address auto link-local
   [*DeviceB-gigabitethernet0/1/0] commit
   [~DeviceB-gigabitethernet0/1/0] quit
   ```
   
   # Configure the LNS-side source interface.
   
   ```
   [~DeviceB] interface loopback1
   [*DeviceB-LoopBack1] ip address 10.3.3.3 255.255.255.0
   [*DeviceB-LoopBack1] ipv6 enable
   [*DeviceB-LoopBack1] ipv6 address auto link-local
   [*DeviceB-LoopBack1] commit
   [~DeviceB-LoopBack1] quit
   ```
   
   # Configure a source interface for RADIUS servers.
   
   ```
   [*DeviceB] interface Loopback2
   [*DeviceB-LoopBack1] ipv6 enable
   [*DeviceB-LoopBack1] ipv6 address 2001:db8::3:2 64
   [*DeviceB-LoopBack1] ipv6 address auto link-local
   [*DeviceB-LoopBack1] ip address 10.4.4.4 255.255.255.0
   [*DeviceB-LoopBack1] quit
   [*DeviceB] commit
   ```
   
   # Create a VT and configure related information.
   
   ```
   [~DeviceB] interface virtual-template 1
   [*DeviceB-Virtual-Template1] ppp authentication-mode chap
   [*DeviceB-Virtual-Template1] commit
   [~DeviceB-Virtual-Template1] quit
   ```
   
   # Enable basic L2TP functions and configure an L2TP group.
   
   ```
   [~DeviceB] l2tp enable
   [*DeviceB] l2tp-group group1
   [*DeviceB-l2tp-group1] commit
   [~DeviceB-l2tp-group1] tunnel name LNS
   [*DeviceB-l2tp-group1] allow l2tp virtual-template 1 remote LAC
   [*DeviceB-l2tp-group1] tunnel authentication
   [*DeviceB-l2tp-group1] tunnel password cipher YsHsjx_202206
   [*DeviceB-l2tp-group1] qos scheduling-mode session 
   [*DeviceB-l2tp-group1] commit
   [~DeviceB-l2tp-group1] quit
   ```
   
   # Disable automatic user bandwidth adjustment on the board in slot 1.
   
   ```
   [~DeviceB] slot 1
   [~DeviceB] undo hostcar drop-rate enable
   [*DeviceB] commit
   ```
   # Configure an LNS group named **group1**.
   ```
   [~DeviceB] lns-group group1
   [*DeviceB-lns-group-group1] bind slot 1 
   [*DeviceB-lns-group-group1] commit
   [~DeviceB-lns-group-group1] bind source loopback1
   [*DeviceB-lns-group-group1] commit
   [~DeviceB-lns-group-group1] quit
   ```
   
   # Configure the DHCPv6 device to generate DUIDs in DUID-LLT mode.
   ```
   [~DeviceB] dhcpv6 duid llt
   [*DeviceB] commit
   ```
   
   # Configure address pools.
   
   1. Configure an IPv6 delegation prefix pool named **pre\_nd** for ND users.
      ```
      [~DeviceB] ipv6 prefix pre_nd delegation
      [*DeviceB-ipv6-prefix-pre_nd] prefix 2001:db8:1::/48
      [*DeviceB-ipv6-prefix-pre_nd] slaac-unshare-only
      [*DeviceB-ipv6-prefix-pre_nd] quit
      [*DeviceB] commit
      ```
   2. Configure an IPv6 delegation prefix pool named **pre\_pd** for PD users.
      ```
      [~DeviceB] ipv6 prefix pre_pd delegation
      [*DeviceB-ipv6-prefix-pre_pd] prefix 2001:db8:2::/48
      [*DeviceB-ipv6-prefix-pre_pd] commit
      [~DeviceB-ipv6-prefix-pre_pd] pd-unshare-only
      [~DeviceB-ipv6-prefix-pre_pd] quit
      ```
   3. Configure an IPv6 delegation address pool named **pool\_nd** and bind the IPv6 delegation prefix pool **pre\_nd** to it.
      ```
      [~DeviceB] ipv6 pool pool_nd bas delegation
      [*DeviceB-ipv6-pool-pool_nd] prefix pre_nd
      [*DeviceB-ipv6-pool-pool_nd] dns-server 2001:db8::2:2 2001:db8::2:3
      [*DeviceB-ipv6-pool-pool_nd] quit
      [*DeviceB] commit
      ```
   4. Configure an IPv6 delegation address pool named **pool\_pd** and bind the IPv6 delegation prefix pool **pre\_pd** to it.
      ```
      [~DeviceB] ipv6 pool pool_pd bas delegation
      [*DeviceB-ipv6-pool-pool_pd] prefix pre_pd
      [*DeviceB-ipv6-pool-pool_pd] dns-server 2001:db8::2:2 2001:db8::2:3
      [*DeviceB-ipv6-pool-pool_pd] quit
      [*DeviceB] commit
      ```
   5. Configure a local IPv4 address pool named **pool\_v4**.
      ```
      [~DeviceB] ip pool pool_v4 bas local
      [*DeviceB-ip-pool-pool_v4] gateway 172.16.0.1 255.255.255.0
      [*DeviceB-ip-pool-pool_v4] commit
      [~DeviceB-ip-pool-pool_v4] section 0 172.16.0.2 172.16.0.200 
      [~DeviceB-ip-pool-pool_v4] dns-server 10.179.155.161 10.179.155.177
      [*DeviceB-ip-pool-pool_v4] quit
      [*DeviceB] commit
      ```# Create UDP sockets with the local port numbers 1645, 1646, and 3799 and with any local IP address.
   ```
   [~DeviceB] radius local-ip all
   [~DeviceB] commit
   ```
   
   # Configure AAA schemes.
   ```
   [~DeviceB] aaa
   [~DeviceB-aaa] authentication-scheme auth1
   [*DeviceB-aaa-authen-radius] authentication-mode radius
   [*DeviceB-aaa-authen-radius] commit
   [~DeviceB-aaa-authen-radius] quit
   [~DeviceB-aaa] accounting-scheme acct1
   [*DeviceB-aaa-accounting-acct1] accounting-mode radius
   [*DeviceB-aaa-accounting-acct1] quit
   [*DeviceB-aaa] commit
   [*DeviceB-aaa] quit
   ```
   
   # Configure a RADIUS server group.
   ```
   [~DeviceB] radius-server group rd1
   [*DeviceB-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
   [*DeviceB-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
   [*DeviceB-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   [*DeviceB-radius-rd1] commit 
   [~DeviceB-radius-rd1] radius-server calling-station-id include mac
   [~DeviceB-radius-rd1] radius-server user-name original
   [*DeviceB-radius-rd1] commit 
   [~DeviceB-radius-rd1] radius-server class-as-car
   [*DeviceB-radius-rd1] quit
   [*DeviceB] commit
   ```
   
   # Configure a user access domain.
   ```
   [~Device] aaa
   [~Device-aaa] domain isp1
   [*Device-aaa-domain-isp1] authentication-scheme auth1
   [*Device-aaa-domain-isp1] accounting-scheme acct1
   [*Device-aaa-domain-isp1] radius-server group rd1
   [*Device-aaa-domain-isp1] commit
   [~Device-aaa-domain-isp1] prefix-assign-mode unshared  
   [~Device-aaa-domain-isp1] ip-pool pool_v4
   [~Device-aaa-domain-isp1] ipv6-pool pool_nd
   [~Device-aaa-domain-isp1] ipv6-pool pool_pd
   [~Device-aaa-domain-isp1] accounting-start-delay 10 online user-type l2tp
   [*Device-aaa-domain-isp1] accounting-start-delay traffic-forward before-start-accounting
   [*Device-aaa-domain-isp1] commit
   [~Device-aaa-domain-isp1] user-basic-service-ip-type ipv4
   [~Device-aaa-domain-isp1] quit
   [~Device-aaa] quit
   ```
   
   
   Configure a routing protocol.
   1. Enable the function to automatically control a route's cost preference.
      ```
      [~DeviceB] peer-backup route-cost auto-advertising
      [*DeviceB] commit
      ```
   2. Configure MPLS.
      ```
      [~DeviceB] mpls
      [~DeviceB-mpls] mpls ldp
      [~DeviceB-mpls] quit
      [~DeviceB] mpls lsr-id 10.3.3.3
      [*DeviceB] interface GigabitEthernet0/1/0
      [*DeviceB-GigabitEthernet0/1/0] mpls
      [*DeviceB-GigabitEthernet0/1/0] mpls ldp
      [*DeviceB-GigabitEthernet0/1/0] quit
      [*DeviceB] commit
      ```
   3. Configure OSPF to import UNRs.
      ```
      [~DeviceB] ospf 1
      [*DeviceB-ospf-1] default cost inherit-metric
      [*DeviceB-ospf-1] import-route unr
      [*DeviceB-ospf-1] area 0
      [*DeviceB-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.255
      [*DeviceB-ospf-1-area-0.0.0.0] network 10.38.160.1 0.0.0.255
      [*DeviceB-ospf-1-area-0.0.0.0] quit
      [*DeviceB-ospf-1] quit
      [*DeviceB] commit
      ```

#### Configuration Files

* DeviceA configuration file

```
#
sysname DeviceA
# 
radius local-ip all
#
l2tp enable
#
mpls lsr-id 10.1.1.1
#
mpls
#
mpls ldp
#
dhcpv6 duid 0001000124fbc193dc99141ea1e9
#
radius-server group rd1
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^%
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server class-as-car  
 radius-server source interface LoopBack2                                             
 radius-server calling-station-id include mac                                   
 radius-server user-name original                                               
# 
interface Virtual-Template1
 ppp authentication-mode chap
#                                                                               
interface Eth-Trunk2                                                                                                 
 mode lacp-static                                                               
 lacp timeout fast                                                              
#                                                                               
interface Eth-Trunk2.10  
 pppoe-server bind Virtual-Template 1                                                       
 ipv6 enable                                                                    
 ipv6 address auto link-local                                                                                                                  
 user-vlan 1000 4000 qinq 2000 2001                                             
 bas                                                                            
 #                                                                              
  access-type layer2-subscriber default-domain authentication isp1                                                           
 #                                                                              
#
interface gigabitethernet0/1/0
 undo shutdown
 ip address 10.38.160.1 255.255.255.0
 ipv6 enable
 mpls 
 mpls ldp
#
interface LoopBack1
 ip address 10.1.1.1 255.255.255.0
 ipv6 enable
 ipv6 address auto link-local 
#
interface LoopBack2
 ipv6 enable
 ip address 10.2.2.2 255.255.255.0
 ipv6 address 2001:DB8::2:2/64
 ipv6 address auto link-local
#
l2tp-group group1
 tunnel name LAC
 start l2tp ip 10.38.160.2
 tunnel source LoopBack1
 tunnel authentication
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
#
aaa
 #
 authentication-scheme auth1
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1 
  idle-cut 60 500
  l2tp-group group1                                            
#
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.38.160.0 0.0.0.255
  network 10.1.1.1 0.0.0.255
#
peer-backup route-cost auto-advertising 
#
return
```

* DeviceB configuration file

```
#
sysname DeviceB
# 
radius local-ip all
#
mpls lsr-id 10.3.3.3
#
mpls
#
mpls ldp
#
l2tp enable
#
dhcpv6 duid 0001000124fbc193dc99141ea1e9
#
radius-server group rd1
 radius-server shared-key-cipher %^%#e,yC%f9z4M2)b)2~r+lA{$g*Fzc+5/bu7VHAN<%(%^%
 radius-server authentication 192.168.7.249 1812 weight 0                       
 radius-server accounting 192.168.7.249 1813 weight 0                           
 radius-server class-as-car  
 radius-server source interface LoopBack2                                             
 radius-server calling-station-id include mac                                   
 radius-server user-name original                                               
# 
slot 1
 undo hostcar drop-rate enable
#
interface Virtual-Template1
 ppp authentication-mode chap
#                                                                               
interface Eth-Trunk2                                                                                                 
 mode lacp-static                                                               
 lacp timeout fast                                                              
#                                                                               
interface gigabitethernet0/1/0
 undo shutdown
 ip address 10.38.160.2 255.255.255.0
 ipv6 enable
 mpls
 mpls ldp
#
interface LoopBack1
 ip address 10.3.3.3 255.255.255.0
 ipv6 enable
 ipv6 address auto link-local 
#
interface LoopBack2
 ipv6 enable
 ip address 10.4.4.4 255.255.255.0
 ipv6 address 2001:DB8::3:2/64
 ipv6 address auto link-local
#
l2tp-group group1
 tunnel name LNS
 allow l2tp virtual-template 1 remote LAC
 tunnel authentication
 tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
 qos scheduling-mode session 
#
lns-group group1
 bind slot 1
 bind source loopback1
#                                                                               
ip pool pool_v4 bas local                                                       
 gateway 172.16.0.1 255.255.255.0                                               
 section 0 172.16.0.2 172.16.0.200                                              
 dns-server 10.179.155.161 10.179.155.177                                       
#                                                                               
ipv6 prefix pre_nd delegation                                                   
 prefix 2001:DB8:1::/48                                                         
 slaac-unshare-only                                                             
#                                                                               
ipv6 pool pool_nd bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_nd                                                                  
#                                                                               
ipv6 prefix pre_pd delegation                                                   
 prefix 2001:DB8:2::/48                                                         
 pd-unshare-only                                                                
#                                                                               
ipv6 pool pool_pd bas delegation                                                
 dns-server 2001:DB8::2:2 2001:DB8::2:3                                         
 prefix pre_pd                                                                  
# 
aaa
 #
 authentication-scheme auth1
 #
 accounting-scheme acct1
 #                                                                              
 domain isp1                                                                  
  authentication-scheme auth1                                                 
  accounting-scheme acct1                                                     
  radius-server group rd1                                                     
  prefix-assign-mode unshared                                                   
  ip-pool pool_v4                                                               
  ipv6-pool pool_nd                                                             
  ipv6-pool pool_pd 
  accounting-start-delay 10 online user-type l2tp                                
  accounting-start-delay traffic-forward before-start-accounting                
  user-basic-service-ip-type ipv4                                               
# 
ospf 1
 default cost inherit-metric
 import-route unr
 opaque-capability enable
 area 0.0.0.0
  network 10.38.160.0 0.0.0.255
  network 10.3.3.3 0.0.0.255
#
peer-backup route-cost auto-advertising
#
return
```