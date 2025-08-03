Example for Configuring VLAN Hand-off to Implement DCI
======================================================

Example for Configuring VLAN Hand-off to Implement DCI

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001589858129__fig_dc_cfg_vxlan_cfgcase_001601), an enterprise has VMs deployed in different DCs. To allow VMs in the same DC to communication with each other, configure BGP EVPN in each DC to create a VXLAN tunnel in distributed gateway mode. Through a Layer 2 sub-interface, Leaf2 accesses DCI-VTEP1, and Leaf 3 accesses DCI-VTEP2. To allow VMs in different DCs to communicate with each other, create a VXLAN tunnel by configuring BGP EVPN in each DC. In inter-DC communication, Leaf2 and Leaf3 decapsulate the VXLAN packets they receive from their own DCs and send them to their connected DCI-VTEPs. Upon receipt, the local DCI-VTEP re-encapsulates the packets into VXLAN packets and sends them to the peer DCI-VTEP. This process allows the VXLAN tunnel to transmit inter-DC packets end to end and ensures that the VMs in different DCs can communicate with each other.

**Figure 1** Network diagram for configuring VLAN hand-off to implement DCI![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](images/fig_dc_cfg_vxlan_cfgcase_001701dcf.png)


**Table 1** Interface IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Device1 | 100GE1/0/1 | 192.168.50.1/24 | Device2 | 100GE1/0/1 | 192.168.60.1/24 |
| 100GE1/0/2 | 192.168.1.1/24 | 100GE1/0/2 | 192.168.1.2/24 |
| Loopback0 | 1.1.1.1/32 | Loopback0 | 2.2.2.2/32 |
| DCI-VTEP1 | 100GE1/0/1 | 192.168.50.2/24 | DCI-VTEP2 | 100GE1/0/1 | 192.168.60.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| Loopback0 | 9.9.9.9/32 | Loopback0 | 10.10.10.10/32 |
| Spine1 | 100GE1/0/1 | 192.168.10.1/24 | Spine2 | 100GE1/0/1 | 192.168.30.1/24 |
| 100GE1/0/2 | 192.168.20.1/24 | 100GE1/0/2 | 192.168.40.1/24 |
| Loopback0 | 3.3.3.3/32 | Loopback0 | 4.4.4.4/32 |
| Leaf1 | 100GE1/0/1 | 192.168.10.2/24 | Leaf4 | 100GE1/0/1 | 192.168.40.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| Loopback0 | 5.5.5.5/32 | Loopback0 | 8.8.8.8/32 |
| Leaf2 | 100GE1/0/1 | 192.168.20.2/24 | Leaf3 | 100GE1/0/1 | 192.168.30.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| 100GE1/0/3 | - | 100GE1/0/3 | - |
| Loopback0 | 6.6.6.6/32 | Loopback0 | 7.7.7.7/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses for devices.
2. Configure routing protocols to ensure that devices can communicate with each other.
3. Configure BGP EVPN in DC A and DC B to create VXLAN tunnels and establish IBGP peer relationships in both DCs.
4. Configure BGP EVPN on DCI-VTEPs to create a VXLAN tunnel between them.
5. Configure Layer 2 sub-interfaces on Leaf2, Leaf3, DCI-VTEP1, and DCI-VTEP2 for DCI tunnel access.

#### Procedure

1. Configure interface IP addresses for devices.
   
   
   
   # Configure Device1. The configurations of other devices are similar to the configuration of Device1. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] interface loopback 0
   [*Device1-LoopBack0] ip address 1.1.1.1 32
   [*Device1-LoopBack0] quit
   [*Device1] interface 100ge 1/0/1
   [*Device1-100GE1/0/1] undo portswitch
   [*Device1-100GE1/0/1] ip address 192.168.50.1 24
   [*Device1-100GE1/0/1] quit
   [*Device1] interface 100ge 1/0/2
   [*Device1-100GE1/0/2] undo portswitch
   [*Device1-100GE1/0/2] ip address 192.168.1.1 24
   [*Device1-100GE1/0/2] quit
   [*Device1] commit
   ```
2. Configure a routing protocol to implement route reachability.
   
   
   
   # Configure Spine1. The configurations of Spine2, Device1, and Device2 are similar to the configuration of Spine1. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Spine1
   [*HUAWEI] commit
   [~Spine1] ospf 1
   [*Spine1-ospf-1] area 0
   [*Spine1-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   [*Spine1-ospf-1-area-0.0.0.0] network 192.168.10.0 0.0.0.255
   [*Spine1-ospf-1-area-0.0.0.0] network 192.168.20.0 0.0.0.255
   [*Spine1-ospf-1-area-0.0.0.0] quit
   [*Spine1-ospf-1] quit
   [*Spine1] commit
   ```
   
   # Configure Leaf1. The configurations of Leaf2, Leaf3, Leaf4, DCI-VTEP1, and DCI-VTEP2 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf1
   [*HUAWEI] commit
   [~Leaf1] ospf 1
   [*Leaf1-ospf-1] area 0
   [*Leaf1-ospf-1-area-0.0.0.0] network 5.5.5.5 0.0.0.0
   [*Leaf1-ospf-1-area-0.0.0.0] network 192.168.10.0 0.0.0.255
   [*Leaf1-ospf-1-area-0.0.0.0] quit
   [*Leaf1-ospf-1] quit
   [*Leaf1] bgp 100
   [*Leaf1-bgp] ipv4-family unicast
   [*Leaf1-bgp-af-ipv4] peer 6.6.6.6 enable
   [*Leaf1-bgp-af-ipv4] quit
   [*Leaf1-bgp] quit
   [*Leaf1] commit
   ```
3. Configure BGP EVPN to establish one VXLAN tunnel in DC A and another one in DC B.
   1. Configure VXLAN service access points. 
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bridge-domain 10
      [*Leaf1-bd10] quit
      [*Leaf1] interface 100GE 1/0/2.1 mode l2
      [*Leaf1-100GE1/0/2.1] encapsulation dot1q vid 10
      [*Leaf1-100GE1/0/2.1] bridge-domain 10
      [*Leaf1-100GE1/0/2.1] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   2. Configure EVPN as the VXLAN control plane on Leaf1, Leaf2, Leaf3, and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] evpn-overlay enable
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   3. Establish an IBGP EVPN peer relationship between Leaf1 and Leaf2, and another one between Leaf3 and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bgp 100
      [*Leaf1-bgp] peer 6.6.6.6 as-number 100
      [*Leaf1-bgp] peer 6.6.6.6 connect-interface LoopBack 0
      [*Leaf1-bgp] l2vpn-family evpn
      [*Leaf1-bgp-af-evpn] peer 6.6.6.6 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf1-bgp-af-evpn] quit
      [*Leaf1-bgp] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   4. Configure EVPN instances.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bridge-domain 10
      [~Leaf1-bd10] vxlan vni 10
      [*Leaf1-bd10] evpn
      [*Leaf1-bd10-evpn] route-distinguisher 10:1
      [*Leaf1-bd10-evpn] vpn-target 11:1
      [*Leaf1-bd10-evpn] quit
      [*Leaf1-bd10] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   5. Enable ingress replication on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface nve 1
      [*Leaf1-Nve1] source 5.5.5.5
      [*Leaf1-Nve1] vni 10 head-end peer-list protocol bgp
      [*Leaf1-Nve1] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   6. Configure IRB route advertisement between Leaf1 and Leaf2, and between Leaf3 and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bgp 100
      [~Leaf1-bgp] l2vpn-family evpn
      [~Leaf1-bgp-af-evpn] peer 6.6.6.6 advertise irb
      [*Leaf1-bgp-af-evpn] quit
      [*Leaf1-bgp] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
4. Configure BGP EVPN on DCI-VTEPs to create a VXLAN tunnel between them.
   1. Configure EVPN as the VXLAN control plane on DCI-VTEP1 and DCI-VTEP2.
      
      
      
      # Configure DCI-VTEP1.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DCI-VTEP1
      [*HUAWEI] commit
      [~DCI-VTEP1] evpn-overlay enable
      [*DCI-VTEP1] commit
      ```
      
      The configuration of DCI-VTEP2 is similar to the configuration of DCI-VTEP1. For detailed configurations, see Configuration Scripts.
   2. Establish an EBGP EVPN peer relationship between DCI-VTEP1 and DCI-VTEP2.
      
      
      
      # Configure DCI-VTEP1.
      
      ```
      [~DCI-VTEP1] bgp 100
      [*DCI-VTEP1-bgp] peer 10.10.10.10 as-number 200
      [*DCI-VTEP1-bgp] peer 10.10.10.10 connect-interface LoopBack 0
      [*DCI-VTEP1-bgp] peer 10.10.10.10 ebgp-max-hop 255
      [*DCI-VTEP1-bgp] l2vpn-family evpn
      [*DCI-VTEP1-bgp-af-evpn] peer 10.10.10.10 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*DCI-VTEP1-bgp-af-evpn] quit
      [*DCI-VTEP1-bgp] quit
      [*DCI-VTEP1] commit
      ```
      
      The configuration of DCI-VTEP2 is similar to the configuration of DCI-VTEP1. For detailed configurations, see Configuration Scripts.
   3. Configure EVPN instances on DCI-VTEPs.
      
      
      
      # Configure DCI-VTEP1.
      
      ```
      [~DCI-VTEP1] bridge-domain 10
      [*DCI-VTEP1-bd10] vxlan vni 10
      [*DCI-VTEP1-bd10] evpn
      [*DCI-VTEP1-bd10-evpn] route-distinguisher 10:5
      [*DCI-VTEP1-bd10-evpn] vpn-target 33:3
      [*DCI-VTEP1-bd10-evpn] quit
      [*DCI-VTEP1-bd10] quit
      [*DCI-VTEP1] commit
      ```
      
      The configuration of DCI-VTEP2 is similar to the configuration of DCI-VTEP1. For detailed configurations, see Configuration Scripts.
   4. Enable ingress replication on DCI-VTEPs.
      
      
      
      # Configure DCI-VTEP1.
      
      ```
      [~DCI-VTEP1] interface nve 1
      [*DCI-VTEP1-Nve1] source 9.9.9.9
      [*DCI-VTEP1-Nve1] vni 10 head-end peer-list protocol bgp
      [*DCI-VTEP1-Nve1] quit
      [*DCI-VTEP1] commit
      ```
      
      The configuration of DCI-VTEP2 is similar to the configuration of DCI-VTEP1. For detailed configurations, see Configuration Scripts.
   5. Configure IRB route advertisement between DCI-VTEP1 and DCI-VTEP2.
      
      
      
      # Configure DCI-VTEP1.
      
      ```
      [~DCI-VTEP1] bgp 100
      [~DCI-VTEP1-bgp] l2vpn-family evpn
      [~DCI-VTEP1-bgp-af-evpn] peer 10.10.10.10 advertise irb
      [*DCI-VTEP1-bgp-af-evpn] quit
      [*DCI-VTEP1-bgp] quit
      [*DCI-VTEP1] commit
      ```
      
      The configuration of DCI-VTEP2 is similar to the configuration of DCI-VTEP1. For detailed configurations, see Configuration Scripts.
5. Configure VLAN access to a VXLAN tunnel.
   
   
   
   # Configure Leaf2.
   
   ```
   [~Leaf2] interface 100GE 1/0/3.1 mode l2
   [*Leaf2-100GE1/0/3.1] encapsulation dot1q vid 10
   [*Leaf2-100GE1/0/3.1] bridge-domain 10
   [*Leaf2-100GE1/0/3.1] quit
   [*Leaf2] commit
   ```
   
   The configurations of Leaf3, DCI-VTEP1, and DCI-VTEP2 are similar to the configuration of Leaf2. For detailed configurations, see Configuration Scripts.

#### Verifying the Configuration

After the configurations are complete, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on each leaf node to check information about the established VXLAN tunnels. The following example uses the command output on Leaf1.
```
[~Leaf1] display vxlan tunnel
Number of vxlan tunnel : 1
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531842  5.5.5.5               8.8.8.8               up     dynamic  00:10:16
```

After the configurations are complete, VMa1 and VMb2 can communicate with each other.


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
  interface LoopBack0
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
    vpn-target 11:1 export-extcommunity
    vpn-target 11:1 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.10.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ip address 5.5.5.5 255.255.255.255
  #
  interface Nve1
   source 5.5.5.5
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack0
   #
   ipv4-family unicast
    peer 6.6.6.6 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 6.6.6.6 enable
    peer 6.6.6.6 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 192.168.10.0 0.0.0.255
  #
  return
  ```
* Leaf2
  
  ```
  #
  sysname Leaf2
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:2
    vpn-target 11:1 export-extcommunity
    vpn-target 11:1 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.20.2 255.255.255.0
  #               
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ip address 6.6.6.6 255.255.255.255
  #               
  interface Nve1  
   source 6.6.6.6 
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack0 
   #
   ipv4-family unicast
    peer 5.5.5.5 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 5.5.5.5 enable
    peer 5.5.5.5 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.6 0.0.0.0
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
  interface LoopBack0
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
* Leaf3
  
  ```
  #
  sysname Leaf3
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:3
    vpn-target 22:2 export-extcommunity
    vpn-target 22:2 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.30.2 255.255.255.0
  #               
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ip address 7.7.7.7 255.255.255.255
  #               
  interface Nve1  
   source 7.7.7.7 
   vni 10 head-end peer-list protocol bgp
  #
  bgp 200
   peer 8.8.8.8 as-number 200
   peer 8.8.8.8 connect-interface LoopBack0
   #
   ipv4-family unicast
    peer 8.8.8.8 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 8.8.8.8 enable
    peer 8.8.8.8 advertise irb
  #
  ospf 1
    area 0.0.0.0
    network 7.7.7.7 0.0.0.0
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
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:4
    vpn-target 22:2 export-extcommunity
    vpn-target 22:2 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.40.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ip address 8.8.8.8 255.255.255.255
  #
  interface Nve1
   source 8.8.8.8
   vni 10 head-end peer-list protocol bgp
  #
  bgp 200 
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 connect-interface LoopBack0
   #
   ipv4-family unicast
    peer 7.7.7.7 enable
   # 
   l2vpn-family evpn
    policy vpn-target
    peer 7.7.7.7 enable
    peer 7.7.7.7 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 8.8.8.8 0.0.0.0
    network 192.168.40.0 0.0.0.255
  #
  return
  ```
* DCI-VTEP1
  ```
  #
  sysname DCI-VTEP1
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:5
    vpn-target 33:3 export-extcommunity
    vpn-target 33:3 import-extcommunity
  #               
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.50.2 255.255.255.0
  #               
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #               
  interface LoopBack0
   ip address 9.9.9.9 255.255.255.255
  #               
  interface Nve1  
   source 9.9.9.9 
   vni 10 head-end peer-list protocol bgp
  #               
  bgp 100
   peer 10.10.10.10 as-number 200
   peer 10.10.10.10 connect-interface LoopBack0
   peer 10.10.10.10 ebgp-max-hop 255
   #
   ipv4-family unicast
    peer 10.10.10.10 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 10.10.10.10 enable
    peer 10.10.10.10 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 9.9.9.9 0.0.0.0
    network 192.168.50.0 0.0.0.255
  #
  return
  ```
* DCI-VTEP2
  ```
  #
  sysname DCI-VTEP2
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 11:6
    vpn-target 33:3 export-extcommunity
    vpn-target 33:3 import-extcommunity
  #               
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.60.2 255.255.255.0
  #               
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #               
  interface LoopBack0
   ip address 10.10.10.10 255.255.255.255
  #               
  interface Nve1  
   source 10.10.10.10 
   vni 10 head-end peer-list protocol bgp
  #               
  bgp 200
   peer 9.9.9.9 as-number 100
   peer 9.9.9.9 connect-interface LoopBack0
   peer 9.9.9.9 ebgp-max-hop 255
   #
   ipv4-family unicast
    peer 9.9.9.9 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 9.9.9.9 enable
    peer 9.9.9.9 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 10.10.10.10 0.0.0.0
    network 192.168.60.0 0.0.0.255
  #
  return
  ```
* Device1
  
  ```
  #
  sysname Device1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.50.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.50.0 0.0.0.255
  #
  return 
  ```
* Device2
  
  ```
  #
  sysname Device2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.60.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.60.0 0.0.0.255
  #
  return 
  ```