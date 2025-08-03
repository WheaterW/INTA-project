Example for Configuring Three-Segment VXLAN to Implement Layer 3 Interworking (IPv6 Services)
=============================================================================================

This section provides an example for configuring three-segment VXLAN to implement Layer 3 interworking between VMs in different DCs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363855__fig_dc_vrp_vxlan_cfg_108801), DC A and DC B reside in different BGP ASs. To allow intra-DC VM communication (VMa1 and VMa2 in DC A, and VMb1 and VMb2 in DC B), configure BGP EVPN on the devices in each DC to create VXLAN tunnels between distributed gateways. To allow IPv6 service communication between DC A and DC B (for example, IPv6 service communication between VMa1 and VMb2), configure BGP EVPN on Leaf2 and Leaf3 to create a VXLAN tunnel between them.

**Figure 1** Network diagram of configuring three-segment VXLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.

  
![](images/fig_dc_vrp_vxlan_cfg_108801.png)  



**Table 1** Interface IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Device1 | GE0/1/0 | 192.168.50.1/24 | Device2 | GE0/1/0 | 192.168.60.1/24 |
| GE0/2/0 | 192.168.1.1/24 | GE0/2/0 | 192.168.1.2/24 |
| LoopBack1 | 1.1.1.1/32 | LoopBack1 | 2.2.2.2/32 |
| Spine1 | GE0/1/0 | 192.168.10.1/24 | Spine2 | GE0/1/0 | 192.168.30.1/24 |
| GE0/2/0 | 192.168.20.1/24 | GE0/2/0 | 192.168.40.1/24 |
| LoopBack1 | 3.3.3.3/32 | LoopBack1 | 4.4.4.4/32 |
| Leaf1 | GE0/1/0 | 192.168.10.2/24 | Leaf4 | GE0/1/0 | 192.168.40.2/24 |
| GE0/2/0 | - | GE0/2/0 | - |
| LoopBack1 | 5.5.5.5/32 | LoopBack1 | 8.8.8.8/32 |
| Leaf2 | GE0/1/0 | 192.168.20.2/24 | Leaf3 | GE0/1/0 | 192.168.30.2/24 |
| GE0/2/0 | - | GE0/2/0 | - |
| GE0/3/0 | 192.168.50.2/24 | GE0/3/0 | 192.168.60.2/24 |
| LoopBack1 | 6.6.6.6/32 | LoopBack1 | 7.7.7.7/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for each node.
2. Configure an IGP for nodes to communicate with each other.
3. Configure static routes for DCs to communicate with each other.
4. Configure BGP EVPN on DC A and DC B to create VXLAN tunnels between distributed gateways.
5. Configure BGP EVPN on Leaf2 and Leaf3 to create a VXLAN tunnel.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN IDs of VMs
* BD IDs
* VNI IDs of BDs and VPN instances

#### Procedure

1. Assign an IP address to each node interface, including the loopback interface.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
2. Configure an IGP. In this example, OSPF is used.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
3. Configure static routes for DCs to communicate with each other.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
4. Configure BGP EVPN on DC A and DC B to create VXLAN tunnels between distributed gateways.
   1. Configure service access points on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bridge-domain 10
      ```
      ```
      [*Leaf1-bd10] quit
      ```
      ```
      [*Leaf1] interface GigabitEthernet 0/2/0.1 mode l2
      ```
      ```
      [*Leaf1-GigabitEthernet0/2/0.1] encapsulation dot1q vid 10
      ```
      ```
      [*Leaf1-GigabitEthernet0/2/0.1] rewrite pop single
      ```
      ```
      [*Leaf1-GigabitEthernet0/2/0.1] bridge-domain 10
      ```
      ```
      [*Leaf1-GigabitEthernet0/2/0.1] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
   2. Configure IBGP EVPN peer relationships between Leaf1 and Leaf2 in DC A and between Leaf3 and Leaf4 in DC B.
      
      
      
      # Configure an IBGP EVPN peer relationship on Leaf1.
      
      ```
      [~Leaf1] bgp 100
      ```
      ```
      [*Leaf1-bgp] peer 6.6.6.6 as-number 100
      ```
      ```
      [*Leaf1-bgp] peer 6.6.6.6 connect-interface LoopBack 1
      ```
      ```
      [*Leaf1-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf1-bgp-af-evpn] peer 6.6.6.6 enable
      ```
      ```
      [*Leaf1-bgp-af-evpn] peer 6.6.6.6 advertise encap-type vxlan
      ```
      ```
      [*Leaf1-bgp-af-evpn] quit
      ```
      ```
      [*Leaf1-bgp] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
   3. Configure VPN and EVPN instances on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] ip vpn-instance vpn1
      ```
      ```
      [*Leaf1-vpn-instance-vpn1] vxlan vni 5010
      ```
      ```
      [*Leaf1-vpn-instance-vpn1] ipv6-family
      ```
      ```
      [*Leaf1-vpn-instance-vpn1-af-ipv6] route-distinguisher 11:11
      ```
      ```
      [*Leaf1-vpn-instance-vpn1-af-ipv6] vpn-target 11:1 evpn
      ```
      ```
      [*Leaf1-vpn-instance-vpn1-af-ipv6] quit
      ```
      ```
      [*Leaf1-vpn-instance-vpn1] quit
      ```
      ```
      [*Leaf1] evpn vpn-instance evrf1 bd-mode
      ```
      ```
      [*Leaf1-evpn-instance-evrf1] route-distinguisher 10:1
      ```
      ```
      [*Leaf1-evpn-instance-evrf1] vpn-target 11:1
      ```
      ```
      [*Leaf1-evpn-instance-evrf1] quit
      ```
      ```
      [*Leaf1] bridge-domain 10
      ```
      ```
      [*Leaf1-bd10] vxlan vni 10 split-horizon-mode
      ```
      ```
      [*Leaf1-bd10] evpn binding vpn-instance evrf1
      ```
      ```
      [*Leaf1-bd10] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
   4. Enable ingress replication on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface nve 1
      ```
      ```
      [*Leaf1-Nve1] source 5.5.5.5
      ```
      ```
      [*Leaf1-Nve1] vni 10 head-end peer-list protocol bgp
      ```
      ```
      [*Leaf1-Nve1] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
   5. Configure Layer 3 VXLAN gateway information on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface vbdif10
      ```
      ```
      [*Leaf1-Vbdif10] ip binding vpn-instance vpn1
      ```
      ```
      [*Leaf1-Vbdif10] ipv6 enable
      ```
      ```
      [*Leaf1-Vbdif10] ipv6 address 2001:DB8:10::1 64
      ```
      ```
      [*Leaf1-Vbdif10] vxlan anycast-gateway enable
      ```
      ```
      [*Leaf1-Vbdif10] ipv6 nd collect host enable
      ```
      ```
      [*Leaf1-Vbdif10] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
   6. Configure IRB route advertisement between Leaf1 and Leaf2 in DC A, between Leaf3 and Leaf4 in DC B, and between Leaf2 and Leaf3.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bgp 100
      ```
      ```
      [*Leaf1-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf1-bgp-af-evpn] peer 6.6.6.6 advertise irbv6
      ```
      ```
      [*Leaf1-bgp-af-evpn] quit
      ```
      ```
      [*Leaf1-bgp] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100
      ```
      ```
      [*Leaf2-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 5.5.5.5 advertise irbv6
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 7.7.7.7 advertise irbv6
      ```
      ```
      [*Leaf2-bgp-af-evpn] quit
      ```
      ```
      [*Leaf2-bgp] quit
      ```
      ```
      [*Leaf2] commit
      ```
      
      The configurations of Leaf4 and Leaf3 are similar to those of Leaf1 and Leaf2, respectively. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363855__dc_vrp_vxlan_cfg_1088_section).
      
      Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on a leaf node to check VXLAN tunnel information. The following example uses the command output on Leaf1.
      ```
      [~Leaf1] display vxlan tunnel
      ```
      ```
      Number of vxlan tunnel : 1
      Tunnel ID   Source           Destination      State  Type    Uptime
      ---------------------------------------------------------------------
      4026531841  5.5.5.5          6.6.6.6          up     dynamic 00:05:36
      ```
5. Configure BGP EVPN on Leaf2 and Leaf3 to create a VXLAN tunnel.
   1. Configure an EBGP EVPN peer relationship between Leaf2 and Leaf3.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      As VPN and EVPN instances have been configured on Leaf2 and Leaf3, you only need to configure an EBGP EVPN peer relationship between Leaf2 and Leaf3 to ensure IP route reachability.
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100
      ```
      ```
      [*Leaf2-bgp] peer 7.7.7.7 as-number 200
      ```
      ```
      [*Leaf2-bgp] peer 7.7.7.7 connect-interface LoopBack1
      ```
      ```
      [*Leaf2-bgp] peer 7.7.7.7 ebgp-max-hop 255
      ```
      ```
      [*Leaf2-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 7.7.7.7 enable
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 7.7.7.7 advertise encap-type vxlan
      ```
      ```
      [*Leaf2-bgp-af-evpn] quit
      ```
      ```
      [*Leaf2-bgp] quit
      ```
      ```
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 200
      ```
      ```
      [*Leaf3-bgp] peer 6.6.6.6 as-number 100
      ```
      ```
      [*Leaf3-bgp] peer 6.6.6.6 connect-interface LoopBack1
      ```
      ```
      [*Leaf3-bgp] peer 6.6.6.6 ebgp-max-hop 255
      ```
      ```
      [*Leaf3-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 6.6.6.6 enable
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 6.6.6.6 advertise encap-type vxlan
      ```
      ```
      [*Leaf3-bgp-af-evpn] quit
      ```
      ```
      [*Leaf3-bgp] quit
      ```
      ```
      [*Leaf3] commit
      ```
   2. Configure the regeneration of IRB routes and IP prefix routes in EVPN routing tables.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100
      ```
      ```
      [*Leaf2-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 5.5.5.5 import reoriginate
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 5.5.5.5 advertise route-reoriginated evpn ipv6
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 7.7.7.7 import reoriginate
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 7.7.7.7 advertise route-reoriginated evpn ipv6
      ```
      ```
      [*Leaf2-bgp-af-evpn] quit
      ```
      ```
      [*Leaf2-bgp] quit
      ```
      ```
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 200
      ```
      ```
      [*Leaf3-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 8.8.8.8 import reoriginate
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 8.8.8.8 advertise route-reoriginated evpn ipv6
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 6.6.6.6 import reoriginate
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 6.6.6.6 advertise route-reoriginated evpn ipv6
      ```
      ```
      [*Leaf3-bgp-af-evpn] quit
      ```
      ```
      [*Leaf3-bgp] quit
      ```
      ```
      [*Leaf3] commit
      ```
6. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on each leaf node to view VXLAN tunnel information. The following example uses the command output on Leaf2.
   
   ```
   [~Leaf2] display vxlan tunnel
   ```
   ```
   Number of vxlan tunnel : 2
   Tunnel ID   Source           Destination      State  Type    Uptime
   ---------------------------------------------------------------------
   4026531841  6.6.6.6          5.5.5.5          up     dynamic 00:11:01
   4026531842  6.6.6.6          7.7.7.7          up     dynamic 00:12:11
   ```
   
   Run the [**display ipv6 routing-table vpn-instance vpn1**](cmdqueryname=display+ipv6+routing-table+vpn-instance+vpn1) command on each leaf node to view IP route information. The following example uses the command output on Leaf1.
   
   ```
   [~Leaf1] display ipv6 routing-table vpn-instance vpn1
   ```
   ```
   Routing Table : vpn1
            Destinations : 6        Routes : 6         
   
   Destination  : 2001:DB8:10::                           PrefixLength : 64
   NextHop      : 2001:DB8:10::1                          Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Vbdif10                                 Flags        : D
   
   Destination  : 2001:DB8:10::1                          PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Vbdif10                                 Flags        : D
   
   Destination  : 2001:DB8:20::                           PrefixLength : 64
   NextHop      : ::FFFF:6.6.6.6                          Preference   : 255
   Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::                                      TunnelID     : 0x0000000027f0000001
   Interface    : VXLAN                                   Flags        : RD
   
   Destination  : 2001:DB8:30::                           PrefixLength : 64
   NextHop      : ::FFFF:6.6.6.6                          Preference   : 255
   Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::                                      TunnelID     : 0x0000000027f0000001
   Interface    : VXLAN                                   Flags        : RD
   
   Destination  : 2001:DB8:40::                           PrefixLength : 64
   NextHop      : ::FFFF:6.6.6.6                          Preference   : 255
   Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::                                      TunnelID     : 0x0000000027f0000001
   Interface    : VXLAN                                   Flags        : RD
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : DB
   ```
   
   After configurations are complete, VMa1 and VMb2 can communicate with each other.

#### Configuration Files

* Spine 1 configuration file
  
  ```
  #
  sysname Spine1
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.10.1 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.20.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #               
  ospf 1          
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 192.168.10.0 0.0.0.255
    network 192.168.20.0 0.0.0.255
  #               
  return 
  ```
* Leaf1 configuration file
  
  ```
  #
  sysname Leaf1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   ipv6 nd collect host enable
   vxlan anycast-gateway enable
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.10.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown       
  #               
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  interface Nve1
   source 5.5.5.5
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
    peer 6.6.6.6 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 6.6.6.6 enable
    peer 6.6.6.6 advertise irbv6
    peer 6.6.6.6 advertise encap-type vxlan
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 192.168.10.0 0.0.0.255
  #
  return
  ```
* Leaf2 configuration file
  
  ```
  #
  sysname Leaf2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   ipv6 nd collect host enable
   vxlan anycast-gateway enable
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.20.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown       
  #               
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 192.168.50.2 255.255.255.0
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  interface Nve1
   source 6.6.6.6
   vni 20 head-end peer-list protocol bgp
  #
  bgp 100
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack1
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 ebgp-max-hop 255
   peer 7.7.7.7 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 5.5.5.5 enable
    peer 7.7.7.7 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 5.5.5.5 enable
    peer 5.5.5.5 advertise irbv6
    peer 5.5.5.5 advertise encap-type vxlan
    peer 5.5.5.5 import reoriginate
    peer 5.5.5.5 advertise route-reoriginated evpn ipv6
    peer 7.7.7.7 enable
    peer 7.7.7.7 advertise irbv6
    peer 7.7.7.7 advertise encap-type vxlan
    peer 7.7.7.7 import reoriginate
    peer 7.7.7.7 advertise route-reoriginated evpn ipv6
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.6 0.0.0.0
    network 192.168.20.0 0.0.0.255
  #
  ip route-static 7.7.7.7 255.255.255.255 192.168.50.1
  ip route-static 192.168.1.0 255.255.255.0 192.168.50.1
  ip route-static 192.168.60.0 255.255.255.0 192.168.50.1
  #
  return
  ```
* Spine 2 configuration file
  
  ```
  #
  sysname Spine2
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.30.1 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.40.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #               
  ospf 1          
   area 0.0.0.0   
    network 4.4.4.4 0.0.0.0
    network 192.168.30.0 0.0.0.255
    network 192.168.40.0 0.0.0.255
  #               
  return
  ```
* Leaf3 configuration file
  
  ```
  #
  sysname Leaf3
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:30::1/64
   ipv6 nd collect host enable
   vxlan anycast-gateway enable
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.30.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown       
  #               
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 192.168.60.2 255.255.255.0
  #
  interface LoopBack1
   ip address 7.7.7.7 255.255.255.255
  #
  interface Nve1
   source 7.7.7.7
   vni 10 head-end peer-list protocol bgp
  #
  bgp 200
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 ebgp-max-hop 255
   peer 6.6.6.6 connect-interface LoopBack1
   peer 8.8.8.8 as-number 200
   peer 8.8.8.8 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 6.6.6.6 enable
    peer 8.8.8.8 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 6.6.6.6 enable
    peer 6.6.6.6 advertise irbv6
    peer 6.6.6.6 advertise encap-type vxlan
    peer 6.6.6.6 import reoriginate
    peer 6.6.6.6 advertise route-reoriginated evpn ipv6
    peer 8.8.8.8 enable
    peer 8.8.8.8 advertise irbv6
    peer 8.8.8.8 advertise encap-type vxlan
    peer 8.8.8.8 import reoriginate
    peer 8.8.8.8 advertise route-reoriginated evpn ipv6
  #
  ospf 1
   area 0.0.0.0
    network 7.7.7.7 0.0.0.0
    network 192.168.30.0 0.0.0.255
  #
  ip route-static 6.6.6.6 255.255.255.255 192.168.60.1
  ip route-static 192.168.1.0 255.255.255.0 192.168.60.1
  ip route-static 192.168.50.0 255.255.255.0 192.168.60.1
  #
  return
  ```
* Leaf4 configuration file
  
  ```
  #
  sysname Leaf4
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:40::1/64
   ipv6 nd collect host enable
   vxlan anycast-gateway enable
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.40.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown       
  #               
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack1
   ip address 8.8.8.8 255.255.255.255
  #
  interface Nve1
   source 8.8.8.8
   vni 20 head-end peer-list protocol bgp
  #
  bgp 200
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 7.7.7.7 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 7.7.7.7 enable
    peer 7.7.7.7 advertise irbv6
    peer 7.7.7.7 advertise encap-type vxlan
  #
  ospf 1
   area 0.0.0.0
    network 8.8.8.8 0.0.0.0
    network 192.168.40.0 0.0.0.255
  #
  return
  ```
* Device 1 configuration file
  
  ```
  #
  sysname Device1
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.50.1 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.1.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ip route-static 6.6.6.6 255.255.255.255 192.168.50.2
  ip route-static 7.7.7.7 255.255.255.255 192.168.1.2
  ip route-static 192.168.60.0 255.255.255.0 192.168.1.2
  #               
  return 
  ```
* Device 2 configuration file
  
  ```
  #
  sysname Device2
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 192.168.60.1 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 192.168.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ip route-static 6.6.6.6 255.255.255.255 192.168.1.1
  ip route-static 7.7.7.7 255.255.255.255 192.168.60.2
  ip route-static 192.168.50.0 255.255.255.0 192.168.1.1
  #               
  return 
  ```