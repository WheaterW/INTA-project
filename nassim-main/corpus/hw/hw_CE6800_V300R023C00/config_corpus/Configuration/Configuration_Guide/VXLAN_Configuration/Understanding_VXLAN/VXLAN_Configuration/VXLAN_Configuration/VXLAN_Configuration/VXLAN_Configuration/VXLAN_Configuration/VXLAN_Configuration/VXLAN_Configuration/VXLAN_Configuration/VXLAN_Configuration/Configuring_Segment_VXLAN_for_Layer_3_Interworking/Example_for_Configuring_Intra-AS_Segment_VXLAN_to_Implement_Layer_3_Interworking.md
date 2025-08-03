Example for Configuring Intra-AS Segment VXLAN to Implement Layer 3 Interworking
================================================================================

Example for Configuring Intra-AS Segment VXLAN to Implement Layer 3 Interworking

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001561023064__fig_dc_vrp_vxlan_cfg_108501), DC A and DC B are planned in the same BGP AS. To allow VMs in the same DC (VMa1 and VMa2 in DC A, and VMb1 and VMb2 in DC B) to communicate with each other, create a VXLAN tunnel in distributed gateway mode by configuring BGP EVPN in each DC. And to allow VMs in different DCs (for example, VMa1 and VMb2) to communicate with each other, create another VXLAN tunnel by configuring BGP EVPN on Leaf2 and Leaf3. Because Leaf2 and Leaf3 do not send EVPN routes received from an IBGP EVPN peer to other IBGP EVPN peers, they need to be configured as RRs.

**Figure 1** Configuring intra-AS segment VXLAN for Layer 3 interworking![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](images/fig_dc_cfg_vxlan_cfgcase_001701dcf.png)


**Table 1** Interface IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Device1 | 100GE1/0/1 | 192.168.50.1/24 | Device2 | 100GE1/0/1 | 192.168.60.1/24 |
| 100GE1/0/2 | 192.168.1.1/24 | 100GE1/0/2 | 192.168.1.2/24 |
| Loopback1 | 1.1.1.1/32 | Loopback1 | 2.2.2.2/32 |
| Spine1 | 100GE1/0/1 | 192.168.10.1/24 | Spine2 | 100GE1/0/1 | 192.168.30.1/24 |
| 100GE1/0/2 | 192.168.20.1/24 | 100GE1/0/2 | 192.168.40.1/24 |
| Loopback1 | 3.3.3.3/32 | Loopback1 | 4.4.4.4/32 |
| Leaf1 | 100GE1/0/1 | 192.168.10.2/24 | Leaf4 | 100GE1/0/1 | 192.168.40.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| Loopback1 | 5.5.5.5/32 | Loopback1 | 8.8.8.8/32 |
| Leaf2 | 100GE1/0/1 | 192.168.20.2/24 | Leaf3 | 100GE1/0/1 | 192.168.30.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| 100GE1/0/3 | 192.168.50.2/24 | 100GE1/0/3 | 192.168.60.2/24 |
| Loopback1 | 6.6.6.6/32 | Loopback1 | 7.7.7.7/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses for devices.
2. Configure routing protocols to ensure that devices can communicate with each other.
3. Configure BGP EVPN within DC A and DC B to establish VXLAN tunnels for intra-DC communication.
4. Configure BGP EVPN on Leaf2 in DC A and Leaf3 in DC B to create a VXLAN tunnel for inter-DC communication.
5. Configure Leaf2 and Leaf3 as RRs.
6. Configure and apply a routing policy on each leaf node.


#### Procedure

1. Configure interface IP addresses for devices.
   
   
   
   # Configure Device1. The configurations of other devices are similar to the configuration of Device1. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] interface loopback 1
   [*Device1-LoopBack1] ip address 1.1.1.1 32
   [*Device1-LoopBack1] quit
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
2. Configure routing protocols to ensure that devices can communicate with each other.
   
   
   
   # Configure Spine1. The configurations of Spine2, Leaf1, and Leaf4 are similar to the configuration of Spine1. For detailed configurations, see Configuration Scripts.
   
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
   
   # Configure Leaf2. The configurations of Leaf3, Device1, and Device2 are similar to the configuration of Leaf2. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf2
   [*HUAWEI] commit
   [~Leaf2] ospf 1
   [*Leaf2-ospf-1] area 0
   [*Leaf2-ospf-1-area-0.0.0.0] network 6.6.6.6 0.0.0.0
   [*Leaf2-ospf-1-area-0.0.0.0] network 192.168.20.0 0.0.0.255
   [*Leaf2-ospf-1-area-0.0.0.0] quit
   [*Leaf2-ospf-1] quit
   [*Leaf2] bgp 20
   [*Leaf2-bgp] peer 192.168.50.1 as-number 10
   [*Leaf2-bgp] ipv4-family unicast
   [*Leaf2-bgp-af-ipv4] network 6.6.6.6 255.255.255.255
   [*Leaf2-bgp-af-ipv4] peer 192.168.50.1 enable
   [*Leaf2-bgp-af-ipv4] quit
   [*Leaf2-bgp] quit
   [*Leaf2] commit
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
   2. Configure EVPN as the VXLAN control plane on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] evpn-overlay enable
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   3. Establish a BGP EVPN peer relationship between Leaf1 and Leaf2, and another one between Leaf3 and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bgp 100 instance evpn1
      [*Leaf1-bgp-instance-evpn1] peer 6.6.6.6 as-number 100
      [*Leaf1-bgp-instance-evpn1] peer 6.6.6.6 connect-interface LoopBack 1
      [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf1-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf1-bgp-instance-evpn1-af-evpn] quit
      [*Leaf1-bgp-instance-evpn1] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   4. Configure an EVPN instance on Leaf1.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] ip vpn-instance vpn1
      [*Leaf1-vpn-instance-vpn1] vxlan vni 5010
      [*Leaf1-vpn-instance-vpn1] ipv4-family
      [*Leaf1-vpn-instance-vpn1-af-ipv4] route-distinguisher 20:1
      [*Leaf1-vpn-instance-vpn1-af-ipv4] vpn-target 100:5010 evpn
      [*Leaf1-vpn-instance-vpn1-af-ipv4] quit
      [*Leaf1-vpn-instance-vpn1] quit
      [*Leaf1] bridge-domain 10
      [*Leaf1-bd10] vxlan vni 10
      [*Leaf1-bd10] evpn
      [*Leaf1-bd10-evpn] route-distinguisher 10:1
      [*Leaf1-bd10-evpn] vpn-target 100:10
      [*Leaf1-bd10-evpn] vpn-target 100:5010 export-extcommunity
      [*Leaf1-bd10-evpn] quit
      [*Leaf1-bd10] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   5. Enable ingress replication on each leaf node.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface nve 1
      [*Leaf1-Nve1] source 5.5.5.5
      [*Leaf1-Nve1] vni 10 head-end peer-list protocol bgp
      [*Leaf1-Nve1] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   6. Configure leaf nodes as Layer 3 VXLAN gateways.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface vbdif 10
      [*Leaf1-Vbdif10] ip binding vpn-instance vpn1
      [*Leaf1-Vbdif10] ip address 10.10.1.1 24
      [*Leaf1-Vbdif10] arp collect host enable
      [*Leaf1-Vbdif10] vxlan anycast-gateway enable
      [*Leaf1-Vbdif10] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   7. Configure the type of route to be advertised between VXLAN gateways. 
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bgp 100 instance evpn1
      [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf1-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 advertise irb
      [*Leaf1-bgp-instance-evpn1-af-evpn] quit
      [*Leaf1-bgp-instance-evpn1] quit
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
4. Configure BGP EVPN on Leaf2 and Leaf3 to create a VXLAN tunnel.
   1. Configure BGP EVPN peer relationships on leaf nodes.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100 instance evpn1
      [*Leaf2-bgp-instance-evpn1] peer 7.7.7.7 as-number 100
      [*Leaf2-bgp-instance-evpn1] peer 7.7.7.7 connect-interface LoopBack1
      [*Leaf2-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 advertise irb
      [*Leaf2-bgp-instance-evpn1-af-evpn] quit
      [*Leaf2-bgp-instance-evpn1] quit
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 100 instance evpn1
      [*Leaf3-bgp-instance-evpn1] peer 6.6.6.6 as-number 100
      [*Leaf3-bgp-instance-evpn1] peer 6.6.6.6 connect-interface LoopBack1
      [*Leaf3-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 advertise irb
      [*Leaf3-bgp-instance-evpn1-af-evpn] quit
      [*Leaf3-bgp-instance-evpn1] quit
      [*Leaf3] commit
      ```
   2. Configure the function to advertise the re-originated EVPN IRB routes and IP prefix routes.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100 instance evpn1
      [~Leaf2-bgp-instance-evpn1] l2vpn-family evpn
      [~Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 import reoriginate
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 advertise route-reoriginated evpn mac-ip
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 advertise route-reoriginated evpn ip
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 import reoriginate
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 advertise route-reoriginated evpn mac-ip
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 advertise route-reoriginated evpn ip
      [*Leaf2-bgp-instance-evpn1-af-evpn] quit
      [*Leaf2-bgp-instance-evpn1] quit
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 100 instance evpn1
      [*Leaf3-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 8.8.8.8 import reoriginate
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 8.8.8.8 advertise route-reoriginated evpn mac-ip
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 8.8.8.8 advertise route-reoriginated evpn ip
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 import reoriginate
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 advertise route-reoriginated evpn mac-ip
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 advertise route-reoriginated evpn ip
      [*Leaf3-bgp-instance-evpn1-af-evpn] quit
      [*Leaf3-bgp-instance-evpn1] quit
      [*Leaf3] commit
      ```
5. Specify Leaf1 and Leaf3 as RR clients of Leaf2. Specify Leaf4 and Leaf2 as RR clients of Leaf3.
   
   
   
   Configure Leaf2.
   
   ```
   [~Leaf2] bgp 100 instance evpn1
   [~Leaf2-bgp-instance-evpn1] l2vpn-family evpn
   [~Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 reflect-client
   [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 reflect-client
   [*Leaf2-bgp-instance-evpn1-af-evpn] undo policy vpn-target
   [*Leaf2-bgp-instance-evpn1-af-evpn] quit
   [*Leaf2-bgp-instance-evpn1] quit
   [*Leaf2] commit
   ```
   
   Configure Leaf3.
   
   ```
   [~Leaf3] bgp 100 instance evpn1
   [~Leaf3-bgp-instance-evpn1] l2vpn-family evpn
   [~Leaf3-bgp-instance-evpn1-af-evpn] peer 8.8.8.8 reflect-client
   [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 reflect-client
   [*Leaf3-bgp-instance-evpn1-af-evpn] undo policy vpn-target
   [*Leaf3-bgp-instance-evpn1-af-evpn] quit
   [*Leaf3-bgp-instance-evpn1] quit
   [*Leaf3] commit
   ```
6. Configure and apply a routing policy on each leaf node.
   
   
   
   Configure a routing policy on Leaf1 to accept only the routes whose next hop is a local DCI leaf node (Leaf2), and apply the routing policy. The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] ip ip-prefix DCI index 10 permit 6.6.6.6 32
   [*Leaf1] route-policy DCI permit node 10
   [*Leaf1-route-policy] if-match ip next-hop ip-prefix DCI
   [*Leaf1-route-policy] quit
   [*Leaf1] bgp 100 instance evpn1
   [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf1-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 route-policy DCI import
   [*Leaf1-bgp-instance-evpn1-af-evpn] quit
   [*Leaf1-bgp-instance-evpn1] quit
   [*Leaf1] commit
   ```
   
   Configure a routing policy on Leaf2 to accept only the routes whose next hop is a remote DCI leaf node (Leaf3), and apply the routing policy. The configuration of Leaf3 is similar to the configuration of Leaf2. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf2] ip ip-prefix DCI index 10 permit 7.7.7.7 32
   [*Leaf2] route-policy DCI permit node 10
   [*Leaf2-route-policy] if-match ip next-hop ip-prefix DCI
   [*Leaf2-route-policy] quit
   [*Leaf2] bgp 100 instance evpn1
   [*Leaf2-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 route-policy DCI import
   [*Leaf2-bgp-instance-evpn1-af-evpn] quit
   [*Leaf2-bgp-instance-evpn1] quit
   [*Leaf2] commit
   ```

#### Verifying the Configuration

Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on leaf nodes to check information about the VXLAN tunnels. The following uses the command output on Leaf2 as an example.

```
[~Leaf2] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531841  6.6.6.6               5.5.5.5               up     dynamic  0035h21m
4026531842  6.6.6.6               7.7.7.7               up     dynamic  0035h25m
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
* Leaf1
  
  ```
  #
  sysname Leaf1
  #
  evpn-overlay enable
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:1
    vpn-target 100:5010 export-extcommunity evpn
    vpn-target 100:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:1
    vpn-target 100:10 export-extcommunity
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:10 import-extcommunity
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.10.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
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
   ip address 5.5.5.5 255.255.255.255
  #
  interface Nve1
   source 5.5.5.5
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100 instance evpn1
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack1
   #
   l2vpn-family evpn
    policy vpn-target
    peer 6.6.6.6 enable
    peer 6.6.6.6 route-policy DCI import
    peer 6.6.6.6 advertise irb
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 192.168.10.0 0.0.0.255
  #
  ip ip-prefix DCI index 10 permit 6.6.6.6 32                                 
  # 
  route-policy DCI permit node 10                                                 
   if-match ip next-hop ip-prefix DCI                                             
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:2
    vpn-target 100:5010 export-extcommunity evpn
    vpn-target 300:5010 export-extcommunity evpn
    vpn-target 100:5010 import-extcommunity evpn
    vpn-target 300:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20
   #
   evpn
    route-distinguisher 10:2
    vpn-target 100:20 export-extcommunity
    vpn-target 100:5010 export-extcommunity
    vpn-target 300:5010 export-extcommunity
    vpn-target 100:20 import-extcommunity
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.20.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.20.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.50.2 255.255.255.0
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  interface Nve1
   source 6.6.6.6
   vni 20 head-end peer-list protocol bgp
  #
  bgp 20
   peer 192.168.50.1 as-number 10
   #
   ipv4-family unicast
    network 6.6.6.6 255.255.255.255
    peer 192.168.50.1 enable
  #
  bgp 100 instance evpn1
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack1
   peer 7.7.7.7 as-number 100
   peer 7.7.7.7 connect-interface LoopBack1
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 5.5.5.5 enable
    peer 5.5.5.5 advertise irb
    peer 5.5.5.5 reflect-client
    peer 5.5.5.5 import reoriginate
    peer 5.5.5.5 advertise route-reoriginated evpn mac-ip
    peer 5.5.5.5 advertise route-reoriginated evpn ip
    peer 7.7.7.7 enable
    peer 7.7.7.7 route-policy DCI import  
    peer 7.7.7.7 advertise irb
    peer 7.7.7.7 reflect-client
    peer 7.7.7.7 import reoriginate
    peer 7.7.7.7 advertise route-reoriginated evpn mac-ip
    peer 7.7.7.7 advertise route-reoriginated evpn ip
  #
  ospf 1          
   area 0.0.0.0   
    network 6.6.6.6 0.0.0.0
    network 192.168.20.0 0.0.0.255
  #
  ip ip-prefix DCI index 10 permit 7.7.7.7 32                                 
  # 
  route-policy DCI permit node 10                                                 
   if-match ip next-hop ip-prefix DCI                                             
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
* Leaf3
  
  ```
  #
  sysname Leaf3
  #
  evpn-overlay enable
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:3
    vpn-target 200:5010 export-extcommunity evpn
    vpn-target 300:5010 export-extcommunity evpn
    vpn-target 200:5010 import-extcommunity evpn
    vpn-target 300:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn 
    route-distinguisher 10:3
    vpn-target 200:10 export-extcommunity
    vpn-target 200:5010 export-extcommunity
    vpn-target 300:5010 export-extcommunity
    vpn-target 200:10 import-extcommunity
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.30.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.30.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.60.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 7.7.7.7 255.255.255.255
  #               
  interface Nve1  
   source 7.7.7.7 
   vni 10 head-end peer-list protocol bgp
  #
  bgp 30
   peer 192.168.60.1 as-number 10
  #
   ipv4-family unicast
    network 7.7.7.7 255.255.255.255
    peer 192.168.60.1 enable
  #
  bgp 100 instance evpn1
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack1
   peer 8.8.8.8 as-number 100
   peer 8.8.8.8 connect-interface LoopBack1
  #
   l2vpn-family evpn
    undo policy vpn-target
    peer 6.6.6.6 enable
    peer 6.6.6.6 route-policy DCI import
    peer 6.6.6.6 advertise irb
    peer 6.6.6.6 reflect-client
    peer 6.6.6.6 import reoriginate
    peer 6.6.6.6 advertise route-reoriginated evpn mac-ip
    peer 6.6.6.6 advertise route-reoriginated evpn ip
    peer 8.8.8.8 enable
    peer 8.8.8.8 advertise irb
    peer 8.8.8.8 reflect-client
    peer 8.8.8.8 import reoriginate
    peer 8.8.8.8 advertise route-reoriginated evpn mac-ip
    peer 8.8.8.8 advertise route-reoriginated evpn ip
  #
  ospf 1          
   area 0.0.0.0   
    network 7.7.7.7 0.0.0.0
    network 192.168.30.0 0.0.0.255
  #
  ip ip-prefix DCI index 10 permit 6.6.6.6 32                                 
  # 
  route-policy DCI permit node 10                                                 
   if-match ip next-hop ip-prefix DCI                                             
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:4
    vpn-target 200:5010 export-extcommunity evpn
    vpn-target 200:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20
   #
   evpn 
    route-distinguisher 10:4
    vpn-target 200:20 export-extcommunity
    vpn-target 200:5010 export-extcommunity
    vpn-target 200:20 import-extcommunity
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.40.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.40.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #               
  interface LoopBack1
   ip address 8.8.8.8 255.255.255.255
  #               
  interface Nve1  
   source 8.8.8.8 
   vni 20 head-end peer-list protocol bgp
  #               
  bgp 100 instance evpn1
   peer 7.7.7.7 as-number 100
   peer 7.7.7.7 connect-interface LoopBack1
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 7.7.7.7 enable
    peer 7.7.7.7 route-policy DCI import
    peer 7.7.7.7 advertise irb
  #               
  ospf 1          
   area 0.0.0.0   
    network 8.8.8.8 0.0.0.0
    network 192.168.40.0 0.0.0.255
  #
  ip ip-prefix DCI index 10 permit 7.7.7.7 32 
  #
  route-policy DCI permit node 10                                                 
   if-match ip next-hop ip-prefix DCI                                             
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
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 10
   peer 192.168.1.2 as-number 10
   peer 192.168.50.2 as-number 20
  #
   ipv4-family unicast
    peer 192.168.1.2 enable
    peer 192.168.1.2 next-hop-local
    peer 192.168.50.2 enable
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
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 10
   peer 192.168.1.1 as-number 10
   peer 192.168.60.2 as-number 30
  #
   ipv4-family unicast
    peer 192.168.1.1 enable
    peer 192.168.1.1 next-hop-local
    peer 192.168.60.2 enable
  #
  return 
  ```