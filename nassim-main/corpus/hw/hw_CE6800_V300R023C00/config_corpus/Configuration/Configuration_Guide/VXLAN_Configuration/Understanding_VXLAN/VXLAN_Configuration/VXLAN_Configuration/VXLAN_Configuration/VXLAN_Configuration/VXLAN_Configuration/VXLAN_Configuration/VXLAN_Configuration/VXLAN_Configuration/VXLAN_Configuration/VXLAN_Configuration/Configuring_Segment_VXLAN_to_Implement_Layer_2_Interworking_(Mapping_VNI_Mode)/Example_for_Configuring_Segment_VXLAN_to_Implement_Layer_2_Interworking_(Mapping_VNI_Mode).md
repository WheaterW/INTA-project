Example for Configuring Segment VXLAN to Implement Layer 2 Interworking (Mapping VNI Mode)
==========================================================================================

Example for Configuring Segment VXLAN to Implement Layer 2 Interworking (Mapping VNI Mode)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001259787949__fig_dc_cfg_vxlan_cfgcase_002101), BGP EVPN is used to configure one VXLAN tunnel within DC A, one within DC B, and one between Leaf2 and Leaf3. To enable communication between VM1 and VM2, Layer 2 connectivity must be established between DC A and DC B. In this example, the VXLAN tunnel in DC A and that in DC B use VNI 10 and VNI 20, respectively. To establish a VXLAN tunnel between Leaf2 and Leaf3, segment VXLAN must be configured for VNI conversion.

**Figure 1** Configuring segment VXLAN for Layer 2 interworking![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001215311494.png)

**Table 1** Interface IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Spine1 | 100GE1/0/1 | 192.168.10.1/24 | Spine2 | 100GE1/0/1 | 192.168.30.1/24 |
| 100GE1/0/2 | 192.168.20.1/24 | 100GE1/0/2 | 192.168.40.1/24 |
| Leaf1 | 100GE1/0/1 | 192.168.10.2/24 | Leaf4 | 100GE1/0/1 | 192.168.40.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| LoopBack1 | 1.1.1.1/32 | LoopBack1 | 4.4.4.4/32 |
| Leaf2 | 100GE1/0/1 | 192.168.20.2/24 | Leaf3 | 100GE1/0/1 | 192.168.30.2/24 |
| 100GE1/0/2 | 192.168.50.1/24 | 100GE1/0/2 | 192.168.50.2/24 |
| LoopBack1 | 2.2.2.2/32 | LoopBack1 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses on devices.
2. Configure routing protocols to ensure that devices can communicate with each other.
3. Configure BGP EVPN to establish one VXLAN tunnel in DC A and another one in DC B.
4. Configure EBGP EVPN on Leaf2 and Leaf3 to establish an inter-DC VXLAN tunnel.
5. Configure segment VXLAN on Leaf2 and Leaf3.


#### Procedure

1. Configure interface IP addresses on devices.
   
   
   
   Configure interface IP addresses on the involved devices according to [Figure 1](#EN-US_TASK_0000001259787949__fig_dc_cfg_vxlan_cfgcase_002101).
2. Configure a routing protocol.
   
   
   
   Configure an IGP within DCs. OSPF is used in this example. Configure EBGP between DCs. For detailed configurations, see Configuration Scripts.
3. Configure BGP EVPN to establish one VXLAN tunnel in DC A and another one in DC B.
   1. Configure a service access point on Leaf1 and Leaf4.
      
      
      
      # Configure Leaf1. The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
      
      ```
      <Leaf1> system-view
      [~Leaf1] bridge-domain 10
      [*Leaf1-bd10] quit
      [*Leaf1] interface 100ge 1/0/2.1 mode l2
      [*Leaf1-100GE1/0/2.1] encapsulation dot1q vid 10
      [*Leaf1-100GE1/0/2.1] bridge-domain 10
      [*Leaf1-100GE1/0/2.1] quit
      [*Leaf1] commit
      ```
   2. Enable EVPN as the VXLAN control plane on each leaf.
      
      
      
      # Configure Leaf1. The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
      
      ```
      [~Leaf1] evpn-overlay enable
      [*Leaf1] commit
      ```
   3. Establish a BGP EVPN peer relationship between Leaf1 and Leaf2 in DC A and between Leaf3 and Leaf4 in DC B.
      
      
      
      # Configure a BGP EVPN peer relationship on Leaf1. The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
      
      ```
      [~Leaf1] bgp 100 instance evpn1
      [*Leaf1-bgp-instance-evpn1] peer 2.2.2.2 as-number 100
      [*Leaf1-bgp-instance-evpn1] peer 2.2.2.2 connect-interface LoopBack1
      [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf1-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf1-bgp-instance-evpn1-af-evpn] quit
      [*Leaf1-bgp-instance-evpn1] quit
      [*Leaf1] commit
      ```
   4. Configure an EVPN instance on Leaf1 and Leaf4.
      
      
      
      # Configure Leaf1. The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
      
      ```
      [~Leaf1] bridge-domain 10
      [~Leaf1-bd10] vxlan vni 10
      [*Leaf1-bd10] evpn
      [*Leaf1-bd10-evpn] route-distinguisher 10:1
      [*Leaf1-bd10-evpn] vpn-target 300:30
      [*Leaf1-bd10-evpn] quit
      [*Leaf1-bd10] quit
      [*Leaf1] commit
      ```
   5. Enable ingress replication on each leaf node.
      
      
      
      # Configure Leaf1. The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
      
      ```
      [~Leaf1] interface nve 1
      [*Leaf1-Nve1] source 1.1.1.1
      [*Leaf1-Nve1] vni 10 head-end peer-list protocol bgp
      [*Leaf1-Nve1] quit
      [*Leaf1] commit
      ```
4. Configure an EBGP EVPN peer relationship between Leaf2 and Leaf3.
   
   
   
   # Configure Leaf2.
   
   ```
   [~Leaf2] bgp 100 instance evpn1
   [*Leaf2-bgp-instance-evpn1] peer 3.3.3.3 as-number 200
   [*Leaf2-bgp-instance-evpn1] peer 3.3.3.3 connect-interface LoopBack1
   [*Leaf2-bgp-instance-evpn1] peer 3.3.3.3 ebgp-max-hop 255
   [*Leaf2-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf2-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: y
   [*Leaf2-bgp-instance-evpn1-af-evpn] quit
   [*Leaf2-bgp-instance-evpn1] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf3.
   
   ```
   [~Leaf3] bgp 200 instance evpn1
   [*Leaf3-bgp-instance-evpn1] peer 2.2.2.2 as-number 100
   [*Leaf3-bgp-instance-evpn1] peer 2.2.2.2 connect-interface LoopBack1
   [*Leaf3-bgp-instance-evpn1] peer 2.2.2.2 ebgp-max-hop 255
   [*Leaf3-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf3-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: y
   [*Leaf3-bgp-instance-evpn1-af-evpn] quit
   [*Leaf3-bgp-instance-evpn1] quit
   [*Leaf3] commit
   ```
5. Configure segment VXLAN on Leaf2 and Leaf3.
   1. Configure a split horizon group to which BGP EVPN peers belong.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] evpn
      [*Leaf2-evpn] irb-reoriginated without-split-group disable
      [*Leaf2-evpn] l3-reoriginate different-split-group
      [*Leaf2-evpn] mac-duplication
      [*Leaf2-evpn-mac-dup] quit
      [*Leaf2-evpn] quit
      [*Leaf2] bgp 100 instance evpn1
      [~Leaf2-bgp-instance-evpn1] l2vpn-family evpn
      [~Leaf2-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 split-group sg1
      [*Leaf2-bgp-instance-evpn1-af-evpn] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] evpn
      [*Leaf3-evpn] irb-reoriginated without-split-group disable
      [*Leaf3-evpn] l3-reoriginate different-split-group
      [*Leaf3-evpn] mac-duplication
      [*Leaf3-evpn-mac-dup] quit
      [*Leaf3-evpn] quit
      [*Leaf3] bgp 200 instance evpn1
      [~Leaf3-bgp-instance-evpn1] l2vpn-family evpn
      [~Leaf3-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 split-group sg1
      [*Leaf3-bgp-instance-evpn1-af-evpn] commit
      ```
   2. Configure the function to advertise re-originated MAC routes to BGP EVPN peers.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2-bgp-instance-evpn1-af-evpn] peer 1.1.1.1 import reoriginate
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 1.1.1.1 advertise route-reoriginated evpn mac
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 import reoriginate
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 advertise route-reoriginated evpn mac
      [*Leaf2-bgp-instance-evpn1-af-evpn] quit
      [*Leaf2-bgp-instance-evpn1] quit
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3-bgp-instance-evpn1-af-evpn] peer 4.4.4.4 import reoriginate
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 4.4.4.4 advertise route-reoriginated evpn mac
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 import reoriginate
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 advertise route-reoriginated evpn mac
      [*Leaf3-bgp-instance-evpn1-af-evpn] quit
      [*Leaf3-bgp-instance-evpn1] quit
      [*Leaf3] commit
      ```
   3. Configure a mapping VNI associated with a BD, and specify the split horizon group to which the mapping VNI belongs.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bridge-domain 10
      [~Leaf2-bd10] vxlan vni 30 split-group sg1
      [*Leaf2-bd10] quit
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bridge-domain 10
      [~Leaf3-bd10] vxlan vni 30 split-group sg1
      [*Leaf3-bd10] quit
      [*Leaf3] commit
      ```
6. Configure an EVPN instance on Leaf2 and Leaf3.
   
   
   
   # Configure Leaf2.
   
   ```
   [~Leaf2] bridge-domain 10
   [~Leaf2-bd10] vxlan vni 10
   [*Leaf2-bd10] evpn
   [*Leaf2-bd10-evpn] route-distinguisher 10:2
   [*Leaf2-bd10-evpn] vpn-target 300:30
   [*Leaf2-bd10-evpn] quit
   [*Leaf2-bd10] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf3.
   
   ```
   [~Leaf3] bridge-domain 10
   [~Leaf3-bd10] vxlan vni 20
   [*Leaf3-bd10] evpn
   [*Leaf3-bd10-evpn] route-distinguisher 10:3
   [*Leaf3-bd10-evpn] vpn-target 300:30
   [*Leaf3-bd10-evpn] quit
   [*Leaf3-bd10] quit
   [*Leaf3] commit
   ```
7. Configure ingress replication for the mapping VNI on Leaf2 and Leaf3.
   
   
   
   # Configure Leaf2.
   
   ```
   [~Leaf2] interface nve 1
   [*Leaf2-Nve1] vni 30 head-end peer-list protocol bgp
   [*Leaf2-Nve1] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf3.
   
   ```
   [~Leaf3] interface nve 1
   [*Leaf3-Nve1] vni 30 head-end peer-list protocol bgp
   [*Leaf3-Nve1] quit
   [*Leaf3] commit
   ```

#### Verifying the Configuration

After completing the configurations, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on leaf nodes to check VXLAN tunnel information and run the [**display vxlan peer**](cmdqueryname=display+vxlan+peer) command to check VXLAN peer information. The following uses the command output on Leaf2 as an example.

```
[~Leaf2] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531924  2.2.2.2               1.1.1.1               up     dynamic  00:39:19
4026531925  2.2.2.2               3.3.3.3               up     dynamic  00:39:09
```
```
[~Leaf2] display vxlan peer
Number of peers : 2
Vni ID    Source                  Destination            Type      Out Vni ID    Creation Mode
----------------------------------------------------------------------------------------------
10        2.2.2.2                 1.1.1.1                dynamic   10            implicit
30        2.2.2.2                 3.3.3.3                dynamic   30            implicit
```

After the configuration is complete, VM1 and VM2 can communicate at Layer 2.


#### Configuration Scripts

* Spine1
  
  ```
  #
  sysname Spine1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.10.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.20.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.10.0 0.0.0.255
    network 192.168.20.0 0.0.0.255
  #
  return 
  ```
* Leaf1
  
  ```
  #
  sysname Leaf1
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:1
    vpn-target 300:30 export-extcommunity
    vpn-target 300:30 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.10.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100 instance evpn1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.10.0 0.0.0.255
  #
  return
  ```
* Leaf2
  
  ```
  #
  sysname Leaf2
  #                                                                                                                                   
  evpn                                                                                                                                
   irb-reoriginated without-split-group disable 
   l3-reoriginate different-split-group 
   mac-duplication
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 10
   vxlan vni 30 split-group sg1
   #
   evpn
    route-distinguisher 10:2
    vpn-target 300:30 export-extcommunity
    vpn-target 300:30 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.20.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.50.1 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 10 head-end peer-list protocol bgp
   vni 30 head-end peer-list protocol bgp
  #
  bgp 10
   peer 192.168.50.2 as-number 20
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    peer 192.168.50.2 enable
  #
  bgp 100 instance evpn1
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 ebgp-max-hop 255
   peer 3.3.3.3 connect-interface LoopBack1
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 import reoriginate
    peer 1.1.1.1 advertise route-reoriginated evpn mac
    peer 3.3.3.3 enable
    peer 3.3.3.3 split-group sg1
    peer 3.3.3.3 import reoriginate
    peer 3.3.3.3 advertise route-reoriginated evpn mac
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.20.0 0.0.0.255
  #
  return  
  ```
* Spine2
  
  ```
  #
  sysname Spine2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.30.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.40.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.30.0 0.0.0.255
    network 192.168.40.0 0.0.0.255
  #
  return
  
  ```
* Leaf3
  
  ```
  #
  sysname Leaf3
  #                                                                                                                                   
  evpn                                                                                                                                
   irb-reoriginated without-split-group disable 
   l3-reoriginate different-split-group 
   mac-duplication
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 20
   vxlan vni 30 split-group sg1
   #
   evpn
    route-distinguisher 10:3
    vpn-target 300:30 export-extcommunity
    vpn-target 300:30 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.30.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.50.2 255.255.255.0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3
   vni 20 head-end peer-list protocol bgp
   vni 30 head-end peer-list protocol bgp
  #
  bgp 20
   peer 192.168.50.1 as-number 10
   #
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    peer 192.168.50.1 enable
  #
  bgp 200 instance evpn1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 ebgp-max-hop 255
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 split-group sg1
    peer 2.2.2.2 import reoriginate
    peer 2.2.2.2 advertise route-reoriginated evpn mac
    peer 4.4.4.4 enable
    peer 4.4.4.4 import reoriginate
    peer 4.4.4.4 advertise route-reoriginated evpn mac
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.30.0 0.0.0.255
  #
  return
  ```
* Leaf4
  
  ```
  #
  sysname Leaf4
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 20
   #
   evpn
    route-distinguisher 10:4
    vpn-target 300:30 export-extcommunity
    vpn-target 300:30 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.40.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  interface Nve1
   source 4.4.4.4
   vni 20 head-end peer-list protocol bgp
  #
  bgp 200 instance evpn1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 192.168.40.0 0.0.0.255
  #
  return
  ```