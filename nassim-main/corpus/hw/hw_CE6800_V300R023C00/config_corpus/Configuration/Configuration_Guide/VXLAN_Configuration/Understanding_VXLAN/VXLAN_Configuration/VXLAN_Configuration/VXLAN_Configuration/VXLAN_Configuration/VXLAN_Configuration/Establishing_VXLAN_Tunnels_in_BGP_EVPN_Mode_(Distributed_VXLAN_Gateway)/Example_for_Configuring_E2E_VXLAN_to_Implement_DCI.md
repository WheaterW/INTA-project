Example for Configuring E2E VXLAN to Implement DCI
==================================================

Example for Configuring E2E VXLAN to Implement DCI

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001568297137__fig_dc_cfg_vxlan_cfgcase_001601), an enterprise has VMs deployed in different DCs. VMa1 on Server1 belongs to VLAN 10 and resides in DC A. VMb2 on Server2 belongs to VLAN 20 and resides in DC B. The two VMs belong to different network segments. To implement E2E communication between the two VMs, create a VXLAN tunnel in distributed VXLAN gateway mode by configuring BGP EVPN on Leaf1 in DC A and Leaf4 in DC B.

**Figure 1** Configuring an E2E VXLAN tunnel![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](images/fig_dc_cfg_vxlan_cfgcase_001601.png)

**Table 1** Interface IP addresses
| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| Device1 | 100GE1/0/1 | 192.168.50.1/24 | Device2 | 100GE1/0/1 | 192.168.60.1/24 |
| 100GE1/0/2 | 192.168.1.1/24 | 100GE1/0/2 | 192.168.1.2/24 |
| Loopback0 | 1.1.1.1/32 | Loopback0 | 2.2.2.2/32 |
| Spine1 | 100GE1/0/1 | 192.168.10.1/24 | Spine2 | 100GE1/0/1 | 192.168.30.1/24 |
| 100GE1/0/2 | 192.168.20.1/24 | 100GE1/0/2 | 192.168.40.1/24 |
| Loopback0 | 3.3.3.3/32 | Loopback0 | 4.4.4.4/32 |
| Leaf1 | 100GE1/0/1 | 192.168.10.2/24 | Leaf4 | 100GE1/0/1 | 192.168.40.2/24 |
| 100GE1/0/2 | - | 100GE1/0/2 | - |
| Loopback0 | 5.5.5.5/32 | Loopback0 | 8.8.8.8/32 |
| Leaf2 | 100GE1/0/1 | 192.168.20.2/24 | Leaf3 | 100GE1/0/1 | 192.168.30.2/24 |
| 100GE1/0/3 | 192.168.50.2/24 | 100GE1/0/3 | 192.168.60.2/24 |
| Loopback0 | 6.6.6.6/32 | Loopback0 | 7.7.7.7/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses for devices.
2. Configure routing protocols to ensure that devices can communicate with each other.
3. Configure VXLAN service access points.
4. Configure VXLAN tunnels.
5. Configure Layer 3 VXLAN gateways.
6. Configure the type of route to be advertised between VXLAN gateways.

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
2. Configure OSPF in DCs and BGP between DCs to implement route interworking.
   
   
   
   # Configure Device1. The configuration of Device2 is similar to the configuration of Device1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Device1] bgp 10
   [*Device1-bgp] peer 192.168.1.2 as-number 10
   [*Device1-bgp] peer 192.168.50.2 as-number 20
   [*Device1-bgp] ipv4-family unicast
   [*Device1-bgp-af-ipv4] peer 192.168.1.2 enable
   [*Device1-bgp-af-ipv4] peer 192.168.1.2 next-hop-local
   [*Device1-bgp-af-ipv4] peer 192.168.50.2 enable
   [*Device1-bgp-af-ipv4] quit
   [*Device1-bgp] quit
   [*Device1] commit
   ```
   
   # Configure Spine1. The configuration of Spine2 is similar to the configuration of Spine1. For detailed configurations, see Configuration Scripts.
   
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
   
   # Configure Leaf1. The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   
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
   [*Leaf1] commit
   ```
   
   
   
   # Configure Leaf2. The configuration of Leaf3 is similar to the configuration of Leaf2. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf2
   [*HUAWEI] commit
   [~Leaf2] ospf 1
   [*Leaf2-ospf-1] import-route bgp
   [*Leaf2-ospf-1] area 0
   [*Leaf2-ospf-1-area-0.0.0.0] network 6.6.6.6 0.0.0.0
   [*Leaf2-ospf-1-area-0.0.0.0] network 192.168.20.0 0.0.0.255
   [*Leaf2-ospf-1-area-0.0.0.0] quit
   [*Leaf2-ospf-1] quit
   [*Leaf2] commit
   [~Leaf2] bgp 20
   [*Leaf2-bgp] peer 192.168.50.1 as-number 10
   [*Leaf2-bgp] ipv4-family unicast
   [*Leaf2-bgp-af-ipv4] network 5.5.5.5 255.255.255.255
   [*Leaf2-bgp-af-ipv4] network 6.6.6.6 255.255.255.255
   [*Leaf2-bgp-af-ipv4] peer 192.168.50.1 enable
   [*Leaf2-bgp-af-ipv4] quit
   [*Leaf2-bgp] quit
   [*Leaf2] commit
   ```
3. Configure VXLAN service access points. 
   
   
   
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
   
   The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
4. Configure VXLAN tunnels.
   1. Configure EVPN as the VXLAN control plane on Leaf1, Leaf2, Leaf3, and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] evpn-overlay enable
      [*Leaf1] commit
      ```
      
      The configurations of Leaf2, Leaf3, and Leaf4 are similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   2. Establish an IBGP EVPN peer relationship between Leaf1 and Leaf2, and another one between Leaf3 and Leaf4.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] bgp 100 instance evpn1
      [*Leaf1-bgp-instance-evpn1] peer 6.6.6.6 as-number 100
      [*Leaf1-bgp-instance-evpn1] peer 6.6.6.6 connect-interface LoopBack 0
      [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf1-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf1-bgp-instance-evpn1-af-evpn] quit
      [*Leaf1-bgp-instance-evpn1] quit
      [*Leaf1] commit
      ```
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100 instance evpn1
      [*Leaf2-bgp-instance-evpn1] peer 5.5.5.5 as-number 100
      [*Leaf2-bgp-instance-evpn1] peer 5.5.5.5 connect-interface LoopBack 0
      [*Leaf2-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 next-hop-invariable
      [*Leaf2-bgp-instance-evpn1-af-evpn] quit
      [*Leaf2-bgp-instance-evpn1] quit
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 200 instance evpn1
      [*Leaf3-bgp-instance-evpn1] peer 8.8.8.8 as-number 200
      [*Leaf3-bgp-instance-evpn1] peer 8.8.8.8 connect-interface LoopBack 0
      [*Leaf3-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 8.8.8.8 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 8.8.8.8 next-hop-invariable
      [*Leaf3-bgp-instance-evpn1-af-evpn] quit
      [*Leaf3-bgp-instance-evpn1] quit
      [*Leaf3] commit
      ```
      
      # Configure Leaf4.
      
      ```
      [~Leaf4] bgp 200 instance evpn1
      [*Leaf4-bgp-instance-evpn1] peer 7.7.7.7 as-number 200
      [*Leaf4-bgp-instance-evpn1] peer 7.7.7.7 connect-interface LoopBack 0
      [*Leaf4-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf4-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf4-bgp-instance-evpn1-af-evpn] quit
      [*Leaf4-bgp-instance-evpn1] quit
      [*Leaf4] commit
      ```
   3. Configure an EBGP EVPN peer relationship between Leaf2 and Leaf3.
      
      
      
      # Configure Leaf2.
      
      ```
      [~Leaf2] bgp 100 instance evpn1
      [*Leaf2-bgp-instance-evpn1] peer 7.7.7.7 as-number 200
      [*Leaf2-bgp-instance-evpn1] peer 7.7.7.7 connect-interface LoopBack 0
      [*Leaf2-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf2-bgp-instance-evpn1-af-evpn] undo policy vpn-target
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 next-hop-invariable
      [*Leaf2-bgp-instance-evpn1-af-evpn] quit
      [*Leaf2-bgp-instance-evpn1] quit
      [*Leaf2] commit
      ```
      
      # Configure Leaf3.
      
      ```
      [~Leaf3] bgp 200 instance evpn1
      [*Leaf3-bgp-instance-evpn1] peer 6.6.6.6 as-number 100
      [*Leaf3-bgp-instance-evpn1] peer 6.6.6.6 connect-interface LoopBack0
      [*Leaf3-bgp-instance-evpn1] l2vpn-family evpn
      [*Leaf3-bgp-instance-evpn1-af-evpn] undo policy vpn-target
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 enable
      Warning: This operation will reset the peer session. Continue? [Y/N]: y
      [*Leaf3-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 next-hop-invariable
      [*Leaf3-bgp-instance-evpn1-af-evpn] quit
      [*Leaf3-bgp-instance-evpn1] quit
      [*Leaf3] commit
      ```
   4. Configure EVPN instances.
      
      
      
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
      
      The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
   5. Enable ingress replication on leaf nodes.
      
      
      
      # Configure Leaf1.
      
      ```
      [~Leaf1] interface nve 1
      [*Leaf1-Nve1] source 5.5.5.5
      [*Leaf1-Nve1] vni 10 head-end peer-list protocol bgp
      [*Leaf1-Nve1] quit
      [*Leaf1] commit
      ```
      
      The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
5. Configure Layer 3 VXLAN gateways.
   
   
   
   # Configure Leaf1.
   
   ```
   [~Leaf1] interface vbdif 10
   [*Leaf1-Vbdif10] ip binding vpn-instance vpn1
   [*Leaf1-Vbdif10] ip address 10.1.1.1 24
   [*Leaf1-Vbdif10] arp collect host enable
   [*Leaf1-Vbdif10] vxlan anycast-gateway enable
   [*Leaf1-Vbdif10] quit
   [*Leaf1] commit
   ```
   
   The configuration of Leaf4 is similar to the configuration of Leaf1. For detailed configurations, see Configuration Scripts.
6. Configure the type of route to be advertised between VXLAN gateways. 
   
   
   
   # Configure Leaf1.
   
   ```
   [~Leaf1] bgp 100 instance evpn1
   [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf1-bgp-instance-evpn1-af-evpn] peer 6.6.6.6 advertise irb
   [*Leaf1-bgp-instance-evpn1-af-evpn] quit
   [*Leaf1-bgp-instance-evpn1] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf2.
   
   ```
   [~Leaf2] bgp 100 instance evpn1
   [*Leaf2-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf2-bgp-instance-evpn1-af-evpn] peer 5.5.5.5 advertise irb
   [*Leaf2-bgp-instance-evpn1-af-evpn] peer 7.7.7.7 advertise irb
   [*Leaf2-bgp-instance-evpn1-af-evpn] quit
   [*Leaf2-bgp-instance-evpn1] quit
   [*Leaf2] commit
   ```
   
   The configurations of Leaf4 and Leaf3 are similar to the configurations of Leaf1 and Leaf2, respectively. For detailed configurations, see Configuration Scripts.

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
   ip address 10.1.1.1 255.255.255.0
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
  interface LoopBack0
   ip address 5.5.5.5 255.255.255.255
  #
  interface Nve1
   source 5.5.5.5
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100 instance evpn1
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack0
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
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.20.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.50.2 255.255.255.0
  #
  interface LoopBack0
   ip address 6.6.6.6 255.255.255.255
  #
  bgp 20
   peer 192.168.50.1 as-number 10
   #
   ipv4-family unicast
    network 5.5.5.5 255.255.255.255
    network 6.6.6.6 255.255.255.255
    peer 192.168.50.1 enable
  #
  bgp 100 instance evpn1
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack0
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 connect-interface LoopBack0
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 5.5.5.5 enable
    peer 5.5.5.5 advertise irb
    peer 5.5.5.5 next-hop-invariable
    peer 7.7.7.7 enable
    peer 7.7.7.7 advertise irb
    peer 7.7.7.7 next-hop-invariable
  #
  ospf 1
   import-route bgp
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
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.30.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.60.2 255.255.255.0
  #
  interface LoopBack0
   ip address 7.7.7.7 255.255.255.255
  #
  bgp 30
   peer 192.168.60.1 as-number 10
   #
   ipv4-family unicast
    network 7.7.7.7 255.255.255.255
    network 8.8.8.8 255.255.255.255
    peer 192.168.60.1 enable
  #
  bgp 200 instance evpn1
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack0
   peer 8.8.8.8 as-number 200
   peer 8.8.8.8 connect-interface LoopBack0
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 6.6.6.6 enable
    peer 6.6.6.6 advertise irb
    peer 6.6.6.6 next-hop-invariable
    peer 8.8.8.8 enable
    peer 8.8.8.8 advertise irb
    peer 8.8.8.8 next-hop-invariable
  #
  ospf 1
   import-route bgp
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:4
    vpn-target 100:5010 export-extcommunity evpn
    vpn-target 100:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20
   #
   evpn
    route-distinguisher 10:4
    vpn-target 100:20 export-extcommunity
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:20 import-extcommunity
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
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
  interface LoopBack0
   ip address 8.8.8.8 255.255.255.255
  #
  interface Nve1
   source 8.8.8.8
   vni 20 head-end peer-list protocol bgp
  #
  bgp 200 instance evpn1
   peer 7.7.7.7 as-number 200
   peer 7.7.7.7 connect-interface LoopBack0
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
  interface LoopBack0
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