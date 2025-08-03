Example for Configuring Three-Segment VXLAN to Implement Layer 2 Interworking
=============================================================================

This section provides an example for configuring three-segment VXLAN tunnels to enable Layer 2 communication between VMs that belong to the different DCs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363836__fig_dc_vrp_vxlan_cfg_120501), BGP EVPN is configured within DC A and DC B to establish VXLAN tunnels. BGP EVPN is also configured on Leaf2 and Leaf3 to establish a VXLAN tunnel between them. To enable communication between VM1 and VM2, implement Layer 2 interworking between DC A and DC B. In this example, the VXLAN tunnel in DC A uses VNI 10, and that in DC B uses VNI 20. VNI conversion must be performed before a VXLAN tunnel is established between Transit Leaf1 and Transit Leaf2.

**Figure 1** Network diagram of configuring three-segment VXLAN to implement Layer 2 interworking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.

![](images/fig_dc_vrp_vxlan_cfg_120401.png)


**Table 1** Interface IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Spine1 | GE0/1/0 | 192.168.10.1/24 | Spine2 | GE0/1/0 | 192.168.30.1/24 |
| GE0/2/0 | 192.168.20.1/24 | GE0/2/0 | 192.168.40.1/24 |
| Leaf1 | GE0/1/0 | 192.168.10.2/24 | Leaf4 | GE0/1/0 | 192.168.40.2/24 |
| GE0/2/0 | - | GE0/2/0 | - |
| LoopBack1 | 1.1.1.1/32 | LoopBack1 | 4.4.4.4/32 |
| Leaf2 | GE0/1/0 | 192.168.20.2/24 | Leaf3 | GE0/1/0 | 192.168.30.2/24 |
| GE0/2/0 | 192.168.50.1/24 | GE0/2/0 | 192.168.50.2/24 |
| LoopBack1 | 2.2.2.2/32 | LoopBack1 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface.
2. Configure an IGP to allow devices to communicate with each other.
3. Configure static routes to achieve interworking between DCs.
4. Configure BGP EVPN within DC A and DC B to establish VXLAN tunnels.
5. Configure BGP EVPN on Leaf2 and Leaf3 to establish a VXLAN tunnel between them.
6. Configure Leaf2 and Leaf3 to advertise routes that are re-originated by the EVPN address family to BGP EVPN peers.

#### Data Preparation

To complete the configuration, you need the following data:

* VLAN IDs of the VMs
* BD IDs
* VNI IDs associated with BDs within DC A and DC B
* Number of the AS to which DC A and DC B belong
* Name of the SHG to which Leaf2 and Leaf3 belong

#### Procedure

1. Assign an IP address to each interface (including the loopback interface) on each node.
   
   
   
   For details about how to configure interface IP addresses and masks, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
2. Configure an IGP. In this example, OSPF is used.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
3. Configure static routes to achieve interworking between DCs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
4. Configure BGP EVPN within DC A and DC B to create VXLAN tunnels.
   1. Configuring service access points on Leaf1 and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bridge-domain 10
      ```
      ```
      [*Leaf1-bd10] quit
      ```
      ```
      [*Leaf1] interface GE 0/2/0.1 mode l2
      ```
      ```
      [*Leaf1-GE0/2/0.1] encapsulation dot1q vid 10
      ```
      ```
      [*Leaf1-GE0/2/0.1] rewrite pop single
      ```
      ```
      [*Leaf1-GE0/2/0.1] bridge-domain 10
      ```
      ```
      [*Leaf1-GE0/2/0.1] quit
      ```
      ```
      [*Leaf1] commit
      ```
      
      The configuration of Leaf4 is similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
   2. Configure BGP EVPN peer relationships between Leaf1 and Leaf2 in DC A and between Leaf3 and Leaf4 in DC B.
      
      
      
      # Configure a BGP EVPN peer relationship on Leaf1.
      
      ```
      [~Leaf1] bgp 100
      ```
      ```
      [*Leaf1-bgp] peer 2.2.2.2 as-number 100
      ```
      ```
      [*Leaf1-bgp] peer 2.2.2.2 connect-interface LoopBack 1
      ```
      ```
      [*Leaf1-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf1-bgp-af-evpn] peer 2.2.2.2 enable
      ```
      ```
      [*Leaf1-bgp-af-evpn] peer 2.2.2.2 advertise encap-type vxlan
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
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
   3. Configure an EVPN instance on each leaf node.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] evpn vpn-instance evrf1 bd-mode
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
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
   4. Configure an ingress replication list on each leaf node.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface nve 1
      ```
      ```
      [*Leaf1-Nve1] source 1.1.1.1
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
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to that of Leaf1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363836__dc_vrp_vxlan_cfg_1205_section).
5. Configure BGP EVPN on Leaf2 and Leaf3 to establish a VXLAN tunnel between them.
   1. Configure a BGP EVPN peer relationship.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100
      ```
      ```
      [*Leaf2-bgp] peer 3.3.3.3 as-number 200
      ```
      ```
      [*Leaf2-bgp] peer 3.3.3.3 connect-interface LoopBack 1
      ```
      ```
      [*Leaf2-bgp] peer 3.3.3.3 ebgp-max-hop 255
      ```
      ```
      [*Leaf2-bgp] network 2.2.2.2 32
      ```
      ```
      [*Leaf2-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 3.3.3.3 enable
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 3.3.3.3 advertise encap-type vxlan
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
      [*Leaf3-bgp] peer 2.2.2.2 as-number 100
      ```
      ```
      [*Leaf3-bgp] peer 2.2.2.2 connect-interface LoopBack 1
      ```
      ```
      [*Leaf3-bgp] peer 2.2.2.2 ebgp-max-hop 255
      ```
      ```
      [*Leaf3-bgp] network 3.3.3.3 32
      ```
      ```
      [*Leaf3-bgp] l2vpn-family evpn
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 2.2.2.2 enable
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 2.2.2.2 advertise encap-type vxlan
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
6. Configure Leaf2 and Leaf3 to advertise routes that are re-originated by the EVPN address family to BGP EVPN peers.
   1. Configure an SHG to which the BGP EVPN peers belong.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100
      ```
      ```
      [~Leaf2-bgp] l2vpn-family evpn
      ```
      ```
      [~Leaf2-bgp-af-evpn] peer 3.3.3.3 split-group sg1
      ```
      ```
      [*Leaf2-bgp-af-evpn] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 200
      ```
      ```
      [~Leaf3-bgp] l2vpn-family evpn
      ```
      ```
      [~Leaf3-bgp-af-evpn] peer 2.2.2.2 split-group sg1
      ```
      ```
      [*Leaf3-bgp-af-evpn] commit
      ```
   2. Enable the function of re-originating EVPN MAC routes.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2-bgp-af-evpn] peer 1.1.1.1 import reoriginate
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 1.1.1.1 advertise route-reoriginated evpn mac
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 3.3.3.3 import reoriginate
      ```
      ```
      [*Leaf2-bgp-af-evpn] peer 3.3.3.3 advertise route-reoriginated evpn mac
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
      [~Leaf3-bgp-af-evpn] peer 4.4.4.4 import reoriginate
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 4.4.4.4 advertise route-reoriginated evpn mac
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 2.2.2.2 import reoriginate
      ```
      ```
      [*Leaf3-bgp-af-evpn] peer 2.2.2.2 advertise route-reoriginated evpn mac
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
7. Verify the configuration.
   
   
   
   Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on each leaf node to view information about the VXLAN tunnels. The following example uses the command output on Leaf2. The command output shows that the VXLAN tunnels are up.
   
   ```
   [~Leaf2] display vxlan tunnel
   ```
   ```
   Number of vxlan tunnel : 2
   Tunnel ID   Source                Destination           State  Type     Uptime
   -----------------------------------------------------------------------------------
   4026531924  2.2.2.2               1.1.1.1               up     dynamic  00:39:19  
   4026531925  2.2.2.2               3.3.3.3               up     dynamic  00:39:09 
   ```
   
   Run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) command on Leaf2 to check information about VXLAN peers.
   
   ```
   [~Leaf2] display vxlan peer
   ```
   ```
   Number of peers : 2
   Vni ID    Source                  Destination            Type      Out Vni ID
   -------------------------------------------------------------------------------
   10        2.2.2.2                 1.1.1.1                dynamic   10         
   10        2.2.2.2                 3.3.3.3                dynamic   20
   ```
   
   After the preceding configurations are complete, Layer 2 communication can be implemented between VM 1 and VM 2.

#### Configuration Files

* Spine 1 configuration file
  
  ```
  #
  sysname Spine1
  #
  interface GE0/1/0
   undo shutdown  
   ip address 192.168.10.1 255.255.255.0
  #               
  interface GE0/2/0
   undo shutdown  
   ip address 192.168.20.1 255.255.255.0
  #               
  ospf 1          
   area 0.0.0.0   
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
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf1
  #               
  interface GE0/1/0
   undo shutdown  
   ip address 192.168.10.2 255.255.255.0
  #               
  interface GE0/2/0
   undo shutdown       
  #               
  interface GE0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #               
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #               
  interface Nve1  
   source 1.1.1.1 
   vni 10 head-end peer-list protocol bgp
  #               
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 2.2.2.2 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise encap-type vxlan
  #               
  ospf 1          
   area 0.0.0.0   
    network 1.1.1.1 0.0.0.0
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
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf1
  #                         
  interface GE0/1/0
   undo shutdown  
   ip address 192.168.20.2 255.255.255.0
  #               
  interface GE0/2/0
   undo shutdown  
   ip address 192.168.50.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #               
  interface Nve1  
   source 2.2.2.2 
   vni 10 head-end peer-list protocol bgp
  #               
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 ebgp-max-hop 255
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise encap-type vxlan
    peer 1.1.1.1 import reoriginate
    peer 1.1.1.1 advertise route-reoriginated evpn mac
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise encap-type vxlan
    peer 3.3.3.3 import reoriginate
    peer 3.3.3.3 advertise route-reoriginated evpn mac
    peer 3.3.3.3 split-group sg1
  #
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.2 0.0.0.0
    network 192.168.20.0 0.0.0.255
  #
  ip route-static 3.3.3.3 255.255.255.255 192.168.50.2
  #               
  return  
  ```
* Spine 2 configuration file
  
  ```
  #
  sysname Spine2
  #
  interface GE0/1/0
   undo shutdown  
   ip address 192.168.30.1 255.255.255.0
  #               
  interface GE0/2/0
   undo shutdown  
   ip address 192.168.40.1 255.255.255.0
  #               
  ospf 1          
   area 0.0.0.0   
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
  bridge-domain 10
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf1
  #               
  interface GE0/1/0
   undo shutdown  
   ip address 192.168.30.2 255.255.255.0
  #               
  interface GE0/2/0
   undo shutdown  
   ip address 192.168.50.2 255.255.255.0
  
  #               
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #               
  interface Nve1  
   source 3.3.3.3 
   vni 20 head-end peer-list protocol bgp
  #               
  bgp 200
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 ebgp-max-hop 255
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise encap-type vxlan
    peer 2.2.2.2 import reoriginate
    peer 2.2.2.2 advertise route-reoriginated evpn mac
    peer 2.2.2.2 split-group sg1
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise encap-type vxlan
    peer 4.4.4.4 import reoriginate
    peer 4.4.4.4 advertise route-reoriginated evpn mac
  #               
  ospf 1          
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 192.168.30.0 0.0.0.255
  #
  ip route-static 2.2.2.2 255.255.255.255 192.168.50.1
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
  bridge-domain 10
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf1
  #               
  interface GE0/1/0
   undo shutdown  
   ip address 192.168.40.2 255.255.255.0
  #                              
  interface GE0/2/0
   undo shutdown       
  #               
  interface GE0/2/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #               
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #               
  interface Nve1  
   source 4.4.4.4 
   vni 20 head-end peer-list protocol bgp
  #               
  bgp 200
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 3.3.3.3 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise encap-type vxlan
  #               
  ospf 1          
   area 0.0.0.0   
    network 4.4.4.4 0.0.0.0
    network 192.168.40.0 0.0.0.255
  #               
  return
  ```