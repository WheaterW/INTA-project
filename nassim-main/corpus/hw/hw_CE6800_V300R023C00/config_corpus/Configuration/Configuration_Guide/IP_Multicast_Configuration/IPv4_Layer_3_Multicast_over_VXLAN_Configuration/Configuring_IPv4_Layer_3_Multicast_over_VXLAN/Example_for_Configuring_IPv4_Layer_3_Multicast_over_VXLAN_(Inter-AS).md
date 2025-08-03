Example for Configuring IPv4 Layer 3 Multicast over VXLAN (Inter-AS)
====================================================================

Example for Configuring IPv4 Layer 3 Multicast over VXLAN (Inter-AS)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001136013618__fig_dc_vrp_multicast_cfg_007401), Leaf 1, Leaf 2, and Leaf 3 are deployed as distributed VXLAN gateways on the IPv4 network. Leaf 1 is in AS 100, whereas Leaf 2 and Leaf 3 are in AS 200. The three leaf nodes all use AS 300 as the BGP EVPN multi-instance process ID to establish BGP EVPN peer relationships.

The multicast source accesses the VXLAN network through a Layer 2 sub-interface that belongs to BD10 on Leaf 1. Receiver 1 accesses the VXLAN network through a Layer 2 sub-interface that belongs to BD20 on Leaf 1. Receiver 2 accesses Leaf 2 through a CE. VPN Layer 3 multicast is deployed between the CE and Leaf 2. Leaf 2 is directly connected to the CE through a common Layer 3 interface. Receivers 3 and 4 access the VXLAN network through Layer 2 sub-interfaces on Leaf 3, which belong to BD10 and BD20, respectively. The source, Receiver 1, Receiver 3, and Receiver 4 are on the VXLAN overlay network, and Receiver 2 is on an external network. Receiver 1, receiver 2, and receiver 3 each order a program with a multicast source specified, and the related multicast group addresses are 232.1.1.1, 232.1.1.2, and 232.1.1.3, respectively. Receiver 4 orders a program with no multicast source specified, and the related multicast group address is 225.1.1.1.

In this case, you need to configure IPv4 Layer 3 multicast on the VXLAN network where distributed gateways are deployed.

**Figure 1** Configuring IPv4 Layer 3 multicast over VXLAN (inter-AS)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001211800308.png)

**Table 1** Device interface information
| Device | Interface | IP Address |
| --- | --- | --- |
| Leaf1 | 100GE1/0/1 | 10.1.1.1/24 |
| 100GE1/0/2 | 10.1.2.1/24 |
| VBDIF10 | 192.168.10.1/24 |
| VBDIF20 | 192.168.20.1/24 |
| LoopBack1 | 1.1.1.1/32 |
| LoopBack2 | 1.1.1.9/32 |
| LoopBack3 | 1.1.1.10/32 |
| Leaf2 | 100GE1/0/1 | 10.1.1.2/24 |
| 100GE1/0/2 | 10.1.3.1/24 |
| 100GE1/0/3 | 192.168.30.1/24 |
| VBDIF10 | 192.168.10.2/24 |
| LoopBack1 | 2.2.2.2/32 |
| LoopBack2 | 2.2.2.9/32 |
| Leaf3 | 100GE1/0/1 | 10.1.2.2/24 |
| 100GE1/0/2 | 10.1.3.2/24 |
| VBDIF10 | 192.168.10.3/24 |
| VBDIF20 | 192.168.20.2/24 |
| LoopBack1 | 3.3.3.3/32 |
| LoopBack2 | 3.3.3.9/32 |
| CE | 100GE1/0/1 | 192.168.30.2/24 |
| 100GE1/0/2 | 192.168.40.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure each leaf node to set up VXLAN tunnels using BGP EVPN, deploy distributed gateways, and implement Layer 3 communication between Leaf-side hosts through VPN routes.
2. Configure BUM multicast replication for the Layer 3 VNI of the L3VPN instance on each leaf.
3. Establish a BGP MVPN peer relationship between any two of Leaf 1, Leaf 2, and Leaf 3.
4. Configure a VXLAN I-PMSI tunnel on each leaf node.
5. Enable PIM-SM on the interface bound to the L3VPN instance on each leaf node to establish a C-multicast routing table.
6. Configure IGMP on each VBDIF interface, and on each physical interface connected to user network segments.
7. Configure VPN Layer 3 multicast between Leaf 2 and the CE.


#### Procedure

1. Configure IP addresses for interfaces on each device. The configurations of Leaf 2, Leaf 3, and CE are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf1
   [*HUAWEI] commit
   [~Leaf1] interface loopback 1
   [*Leaf1-LoopBack1] ip address 1.1.1.1 32
   [*Leaf1-LoopBack1] quit
   [*Leaf1] interface loopback 2
   [*Leaf1-LoopBack2] ip address 1.1.1.9 32
   [*Leaf1-LoopBack2] quit
   [*Leaf1] interface loopback 3
   [*Leaf1-LoopBack3] ip address 1.1.1.10 32
   [*Leaf1-LoopBack3] quit
   [*Leaf1] interface 100ge 1/0/1
   [*Leaf1-100GE1/0/1] undo portswitch
   [*Leaf1-100GE1/0/1] ip address 10.1.1.1 24
   [*Leaf1-100GE1/0/1] quit
   [*Leaf1] interface 100ge 1/0/2
   [*Leaf1-100GE1/0/2] undo portswitch
   [*Leaf1-100GE1/0/2] ip address 10.1.2.1 24
   [*Leaf1-100GE1/0/2] quit
   [*Leaf1] commit
   ```
2. Configure VXLAN.
   
   
   
   # Configure BGP on the VXLAN underlay network.
   
   * Configure Leaf 1.
     ```
     [~Leaf1] bgp 100
     [*Leaf1-bgp] peer 10.1.1.2 as-number 200
     [*Leaf1-bgp] peer 10.1.2.2 as-number 200
     [*Leaf1-bgp] network 1.1.1.1 32
     [*Leaf1-bgp] network 1.1.1.9 32
     [*Leaf1-bgp] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 2.
     ```
     [~Leaf2] bgp 200
     [*Leaf2-bgp] peer 10.1.1.1 as-number 100
     [*Leaf2-bgp] peer 10.1.3.2 as-number 200
     [*Leaf2-bgp] network 2.2.2.2 32
     [*Leaf2-bgp] network 2.2.2.9 32
     [*Leaf2-bgp] quit
     [*Leaf2] commit
     ```
   * Configure Leaf 3.
     ```
     [~Leaf3] bgp 200
     [*Leaf3-bgp] peer 10.1.2.1 as-number 100
     [*Leaf3-bgp] peer 10.1.3.1 as-number 200
     [*Leaf3-bgp] network 3.3.3.3 32
     [*Leaf3-bgp] network 3.3.3.9 32
     [*Leaf3-bgp] quit
     [*Leaf3] commit
     ```
   
   # Configure service access points on Leaf 1 and Leaf 3. The configuration of Leaf 3 is similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts. Because Leaf 2 is directly connected to the CE through a common Layer 3 interface, you do not need to configure a service access point on Leaf 2.
   
   ```
   [~Leaf1] bridge-domain 10
   [*Leaf1-bd10] quit
   [*Leaf1] interface 100ge 1/0/3.1 mode l2
   [*Leaf1-100GE1/0/3.1] undo portswitch
   [*Leaf1-100GE1/0/3.1] encapsulation dot1q vid 10
   [*Leaf1-100GE1/0/3.1] bridge-domain 10
   [*Leaf1-100GE1/0/3.1] quit
   [*Leaf1] bridge-domain 20
   [*Leaf1-bd20] quit
   [*Leaf1] interface 100ge 1/0/4.1 mode l2
   [*Leaf1-100GE1/0/4.1] undo portswitch
   [*Leaf1-100GE1/0/4.1] encapsulation dot1q vid 20
   [*Leaf1-100GE1/0/4.1] bridge-domain 20
   [*Leaf1-100GE1/0/4.1] quit
   [*Leaf1] commit
   ```
   
   Configure BGP EVPN on each leaf node as a VXLAN control plane protocol. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] evpn-overlay enable
   [*Leaf1] commit
   ```
   
   # Establish BGP EVPN peer relationships between the leaf nodes. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] bgp 300 instance evpn1
   [*Leaf1-bgp-instance-evpn1] peer 2.2.2.9 as-number 300
   [*Leaf1-bgp-instance-evpn1] peer 2.2.2.9 connect-interface LoopBack2
   [*Leaf1-bgp-instance-evpn1] peer 3.3.3.9 as-number 300
   [*Leaf1-bgp-instance-evpn1] peer 3.3.3.9 connect-interface LoopBack2
   [*Leaf1-bgp-instance-evpn1] l2vpn-family evpn
   [*Leaf1-bgp-instance-evpn1-af-evpn] peer 2.2.2.9 enable
   [*Leaf1-bgp-instance-evpn1-af-evpn] peer 3.3.3.9 enable
   [*Leaf1-bgp-instance-evpn1-af-evpn] quit
   [*Leaf1-bgp-instance-evpn1] quit
   [*Leaf1] commit
   ```
   
   # Configure L3VPN and EVPN instances on each leaf node. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] ip vpn-instance mcast1
   [*Leaf1-vpn-instance-mcast1] vxlan vni 5010
   [*Leaf1-vpn-instance-mcast1] ipv4-family
   [*Leaf1-vpn-instance-mcast1-af-ipv4] route-distinguisher 1:1
   [*Leaf1-vpn-instance-mcast1-af-ipv4] vpn-target 1:1
   [*Leaf1-vpn-instance-mcast1-af-ipv4] vpn-target 13:1 evpn
   [*Leaf1-vpn-instance-mcast1-af-ipv4] quit
   [*Leaf1-vpn-instance-mcast1] quit
   [*Leaf1] bridge-domain 10
   [*Leaf1-bd10] vxlan vni 10
   [*Leaf1-bd10] evpn
   [*Leaf1-bd10-evpn] route-distinguisher 11:1
   [*Leaf1-bd10-evpn] vpn-target 12:1
   [*Leaf1-bd10-evpn] vpn-target 13:1
   [*Leaf1-bd10-evpn] quit
   [*Leaf1-bd10] quit
   [*Leaf1] bridge-domain 20
   [*Leaf1-bd20] vxlan vni 20
   [*Leaf1-bd20] evpn
   [*Leaf1-bd20-evpn] route-distinguisher 11:2
   [*Leaf1-bd20-evpn] vpn-target 12:2
   [*Leaf1-bd20-evpn] vpn-target 13:1
   [*Leaf1-bd20-evpn] quit
   [*Leaf1-bd20] quit
   [*Leaf1] commit
   ```
   
   # Configure ingress replication on each leaf node. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] interface nve 1
   [*Leaf1-Nve1] source 1.1.1.9
   [*Leaf1-Nve1] vni 10 head-end peer-list protocol bgp
   [*Leaf1-Nve1] vni 20 head-end peer-list protocol bgp
   [*Leaf1-Nve1] quit
   [*Leaf1] commit
   ```
   
   # Configure a Layer 3 VXLAN gateway on each leaf node.
   
   * Configure Leaf 1 as a Layer 3 VXLAN gateway.
     ```
     [~Leaf1] interface vbdif 10
     [*Leaf1-Vbdif10] ip binding vpn-instance mcast1
     [*Leaf1-Vbdif10] ip address 192.168.10.1 24
     [*Leaf1-Vbdif10] vxlan anycast-gateway enable
     [*Leaf1-Vbdif10] arp collect host enable
     [*Leaf1-Vbdif10] quit
     [*Leaf1] interface vbdif 20
     [*Leaf1-Vbdif20] ip binding vpn-instance mcast1
     [*Leaf1-Vbdif20] ip address 192.168.20.1 24
     [*Leaf1-Vbdif20] vxlan anycast-gateway enable
     [*Leaf1-Vbdif20] arp collect host enable
     [*Leaf1-Vbdif20] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 2 as a Layer 3 VXLAN gateway. Because Receiver 2 accesses Leaf 2 through the CE, Leaf 2 does not need to advertise host routes. As such, the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) command does not need to be run on Leaf 2 for host information collection.
     ```
     [~Leaf2] interface vbdif 10
     [*Leaf2-Vbdif10] ip binding vpn-instance mcast1
     [*Leaf2-Vbdif10] ip address 192.168.10.2 24
     [*Leaf2-Vbdif10] vxlan anycast-gateway enable
     [*Leaf2-Vbdif10] quit
     [*Leaf2] commit
     ```
   * Configure Leaf 3 as a Layer 3 VXLAN gateway.
     ```
     [~Leaf3] interface vbdif 10
     [*Leaf3-Vbdif10] ip binding vpn-instance mcast1
     [*Leaf3-Vbdif10] ip address 192.168.10.3 24
     [*Leaf3-Vbdif10] vxlan anycast-gateway enable
     [*Leaf3-Vbdif10] arp collect host enable
     [*Leaf3-Vbdif10] quit
     [*Leaf3] interface vbdif 20
     [*Leaf3-Vbdif20] ip binding vpn-instance mcast1
     [*Leaf3-Vbdif20] ip address 192.168.20.2 24
     [*Leaf3-Vbdif20] vxlan anycast-gateway enable
     [*Leaf3-Vbdif20] arp collect host enable
     [*Leaf3-Vbdif20] quit
     [*Leaf3] commit
     ```
   
   # Configure Leaf 1 and Leaf 3 to advertise IRB routes to their BGP peers.
   
   * Configure Leaf 1.
     ```
     [~Leaf1] bgp 300 instance evpn1
     [~Leaf1-bgp-instance-evpn1] l2vpn-family evpn
     [~Leaf1-bgp-instance-evpn1-af-evpn] peer 2.2.2.9 advertise irb
     [*Leaf1-bgp-instance-evpn1-af-evpn] peer 3.3.3.9 advertise irb
     [*Leaf1-bgp-instance-evpn1-af-evpn] quit
     [*Leaf1-bgp-instance-evpn1] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 3.
     ```
     [~Leaf3] bgp 300 instance evpn1
     [~Leaf3-bgp-instance-evpn1] l2vpn-family evpn
     [~Leaf3-bgp-instance-evpn1-af-evpn] peer 1.1.1.9 advertise irb
     [*Leaf3-bgp-instance-evpn1-af-evpn] peer 2.2.2.9 advertise irb
     [*Leaf3-bgp-instance-evpn1-af-evpn] quit
     [*Leaf3-bgp-instance-evpn1] quit
     [*Leaf3] commit
     ```
   
   # Configure Leaf 1 and Leaf 2 to advertise prefix routes to their BGP peers.
   
   * Configure Leaf 1.
     ```
     [~Leaf1] bgp 100
     [~Leaf1-bgp] ipv4-family vpn-instance mcast1
     [*Leaf1-bgp-mcast1] import-route direct
     [*Leaf1-bgp-mcast1] advertise l2vpn evpn
     [*Leaf1-bgp-mcast1] quit
     [*Leaf1-bgp] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 2.
     ```
     [~Leaf2] bgp 200
     [~Leaf2-bgp] ipv4-family vpn-instance mcast1
     [*Leaf2-bgp-mcast1] advertise l2vpn evpn
     [*Leaf2-bgp-mcast1] quit
     [*Leaf2-bgp] quit
     [*Leaf2] commit
     ```# Configure public network Layer 3 multicast on each leaf node. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   ```
   [~Leaf1] multicast routing-enable
   [*Leaf1] interface loopback 1
   [*Leaf1-LoopBack1] pim sm
   [*Leaf1-LoopBack1] quit
   [*Leaf1] interface 100ge 1/0/1
   [*Leaf1-100GE1/0/1] pim sm
   [*Leaf1-100GE1/0/1] quit
   [*Leaf1] interface 100ge 1/0/2
   [*Leaf1-100GE1/0/2] pim sm
   [*Leaf1-100GE1/0/2] quit
   [*Leaf1] pim
   [*Leaf1-pim] static-rp 1.1.1.1
   [*Leaf1-pim] quit
   [*Leaf1] commit
   ```
   
   # Configure BUM multicast replication for the Layer 3 VNI of the L3VPN instance on each leaf node. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   ```
   [~Leaf1] interface nve 1
   [~Leaf1-Nve1] vni 5010 mcast-group 225.0.0.1
   [*Leaf1-Nve1] quit
   [*Leaf1] commit
   ```
   
   After the preceding configurations are complete, VXLAN tunnels can be established between the leaf nodes. You can run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command to view VXLAN tunnel information. For example, in the command output on Leaf 1, the **State** field is **up**, indicating that the VXLAN tunnel is reachable. If the value of the **Type** field is **static**, the destination IP address is statically configured. If the value is **dynamic**, the destination IP address is dynamically learned through a protocol.
   
   ```
   [~Leaf1] display vxlan tunnel
   Number of vxlan tunnel : 3
   Tunnel ID   Source                Destination           State  Type     Uptime
   -----------------------------------------------------------------------------------
   4026531841  1.1.1.9               225.0.0.1             up     static   04:30:52  
   4026531843  1.1.1.9               3.3.3.9               up     dynamic  04:30:52  
   4026531845  1.1.1.9               2.2.2.9               up     dynamic  04:30:52 
   ```
3. Establish BGP MVPN peer relationships on each leaf node.
   
   
   
   # Configure Leaf 1.
   
   ```
   [~Leaf1] bgp 100
   [~Leaf1-bgp] peer 2.2.2.2 as-number 200
   [*Leaf1-bgp] peer 2.2.2.2 connect-interface LoopBack1
   [*Leaf1-bgp] peer 2.2.2.2 ebgp-max-hop 255
   [*Leaf1-bgp] peer 3.3.3.3 as-number 200
   [*Leaf1-bgp] peer 3.3.3.3 connect-interface LoopBack1
   [*Leaf1-bgp] peer 3.3.3.3 ebgp-max-hop 255
   [*Leaf1-bgp] ipv4-family mvpn
   [*Leaf1-bgp-af-mvpn] peer 2.2.2.2 enable
   [*Leaf1-bgp-af-mvpn] peer 3.3.3.3 enable
   [*Leaf1-bgp-af-mvpn] quit
   [*Leaf1-bgp] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf 2.
   
   ```
   [~Leaf2] bgp 200
   [~Leaf2-bgp] peer 1.1.1.1 as-number 100
   [*Leaf2-bgp] peer 1.1.1.1 connect-interface LoopBack1
   [*Leaf2-bgp] peer 1.1.1.1 ebgp-max-hop 255
   [*Leaf2-bgp] peer 3.3.3.3 as-number 200
   [*Leaf2-bgp] peer 3.3.3.3 connect-interface LoopBack1
   [*Leaf2-bgp] ipv4-family mvpn
   [*Leaf2-bgp-af-mvpn] peer 1.1.1.1 enable
   [*Leaf2-bgp-af-mvpn] peer 3.3.3.3 enable
   [*Leaf2-bgp-af-mvpn] quit
   [*Leaf2-bgp] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf 3.
   
   ```
   [~Leaf3] bgp 200
   [~Leaf3-bgp] peer 1.1.1.1 as-number 100
   [*Leaf3-bgp] peer 1.1.1.1 connect-interface LoopBack1
   [*Leaf3-bgp] peer 1.1.1.1 ebgp-max-hop 255
   [*Leaf3-bgp] peer 2.2.2.2 as-number 200
   [*Leaf3-bgp] peer 2.2.2.2 connect-interface LoopBack1
   [*Leaf3-bgp] ipv4-family mvpn
   [*Leaf3-bgp-af-mvpn] peer 1.1.1.1 enable
   [*Leaf3-bgp-af-mvpn] peer 2.2.2.2 enable
   [*Leaf3-bgp-af-mvpn] quit
   [*Leaf3-bgp] quit
   [*Leaf3] commit
   ```
4. Configure a VXLAN I-PMSI tunnel on each leaf node.
   
   
   
   # Configure Leaf 1. The MVPN ID configured on a distributed VXLAN gateway must be the VTEP IP address of the gateway.
   
   ```
   [~Leaf1] multicast mvpn 1.1.1.9
   [*Leaf1] ip vpn-instance mcast1
   [*Leaf1-vpn-instance-mcast1] ipv4-family
   [*Leaf1-vpn-instance-mcast1-af-ipv4] multicast routing-enable
   [*Leaf1-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
   [*Leaf1-vpn-instance-mcast1-af-ipv4] mvpn
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn] auto-discovery inter-as
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn] spt-only mode
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] quit
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn] quit
   [*Leaf1-vpn-instance-mcast1-af-ipv4] quit
   [*Leaf1-vpn-instance-mcast1] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf 2.
   
   ```
   [~Leaf2] multicast mvpn 2.2.2.9
   [*Leaf2] ip vpn-instance mcast1
   [*Leaf2-vpn-instance-mcast1] ipv4-family
   [*Leaf2-vpn-instance-mcast1-af-ipv4] multicast routing-enable
   [*Leaf2-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
   [*Leaf2-vpn-instance-mcast1-af-ipv4] mvpn
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] auto-discovery inter-as
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] quit
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] quit
   [*Leaf2-vpn-instance-mcast1-af-ipv4] quit
   [*Leaf2-vpn-instance-mcast1] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf 3. Because Leaf 3-side Receiver 4 has no multicast source specified, Receiver 4 uses the (\*, G) mode to join a multicast group. In this case, a PIM-SM RPT setup mode must be specified for Leaf 3 and source-side Leaf 1. In this example, the setup mode is not across the public network (**spt-only mode**).
   
   ```
   [~Leaf3] multicast mvpn 3.3.3.9
   [*Leaf3] ip vpn-instance mcast1
   [*Leaf3-vpn-instance-mcast1] ipv4-family
   [*Leaf3-vpn-instance-mcast1-af-ipv4] multicast routing-enable
   [*Leaf3-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
   [*Leaf3-vpn-instance-mcast1-af-ipv4] mvpn
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] auto-discovery inter-as
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] spt-only mode
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] quit
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] quit
   [*Leaf3-vpn-instance-mcast1-af-ipv4] quit
   [*Leaf3-vpn-instance-mcast1] quit
   [*Leaf3] commit
   ```
5. Configure PIM-SM and IGMP on VBDIF interfaces.
   
   
   
   # Configure Leaf 1.
   
   ```
   [~Leaf1] interface vbdif 10
   [~Leaf1-Vbdif10] pim sm
   [*Leaf1-Vbdif10] igmp enable
   [*Leaf1-Vbdif10] quit
   [*Leaf1] interface vbdif 20
   [*Leaf1-Vbdif20] pim sm
   [*Leaf1-Vbdif20] igmp enable
   [*Leaf1-Vbdif20] igmp version 3
   [*Leaf1-Vbdif20] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf 2.
   
   ```
   [~Leaf2] interface vbdif 10
   [~Leaf2-Vbdif10] pim sm
   [*Leaf2-Vbdif10] igmp enable
   [*Leaf2-Vbdif10] igmp version 3
   [*Leaf2-Vbdif10] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf 3.
   
   ```
   [~Leaf3] interface vbdif 10
   [~Leaf3-Vbdif10] pim sm
   [*Leaf3-Vbdif10] igmp enable
   [*Leaf3-Vbdif10] igmp version 3
   [*Leaf3-Vbdif10] quit
   [*Leaf3] interface vbdif 20
   [*Leaf3-Vbdif20] pim sm
   [*Leaf3-Vbdif20] igmp enable
   [*Leaf3-Vbdif20] quit
   [*Leaf3] commit
   ```
6. Configure Leaf 1 and Leaf 3 as VPN static RPs.
   
   # Configure Leaf 1.
   ```
   [~Leaf1] interface loopback 3
   [~Leaf1-LoopBack3] ip binding vpn-instance mcast1
   [*Leaf1-LoopBack3] ip address 1.1.1.10 32
   [*Leaf1-LoopBack3] pim sm
   [*Leaf1-LoopBack3] quit
   [*Leaf1] pim vpn-instance mcast1
   [*Leaf1-pim-mcast1] static-rp 1.1.1.10
   [*Leaf1-pim-mcast1] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf 3.
   ```
   [~Leaf3] pim vpn-instance mcast1
   [*Leaf3-pim-mcast1] static-rp 1.1.1.10
   [*Leaf3-pim-mcast1] quit
   [*Leaf3] commit
   ```
7. Configure VPN Layer 3 multicast between Leaf 2 and the CE connected to it.
   
   # Configure Leaf 2.
   ```
   [~Leaf2] interface 100ge 1/0/3
   [~Leaf2-100GE1/0/3] undo portswitch
   [~Leaf2-100GE1/0/3] ip binding vpn-instance mcast1
   [*Leaf2-100GE1/0/3] ip address 192.168.30.1 24
   [*Leaf2-100GE1/0/3] pim sm
   [*Leaf2-100GE1/0/3] igmp enable
   [*Leaf2-100GE1/0/3] igmp version 3
   [*Leaf2-100GE1/0/3] quit
   [*Leaf2] ip route-static vpn-instance mcast1 192.168.40.1 24 100ge 1/0/3
   [*Leaf2] bgp 200
   [*Leaf2-bgp] ipv4-family vpn-instance mcast1
   [*Leaf2-bgp-mcast1] import-route static
   [*Leaf2-bgp-mcast1] quit
   [*Leaf2-bgp] quit
   [*Leaf2] commit
   ```
   
   # Configure the CE.
   
   
   
   ```
   [~CE] multicast routing-enable
   [*CE] interface 100ge 1/0/1
   [*CE-100GE1/0/1] undo portswitch
   [*CE-100GE1/0/1] pim sm
   [*CE-100GE1/0/1] quit
   [*CE] interface 100ge 1/0/2
   [*CE-100GE1/0/2] undo portswitch
   [*CE-100GE1/0/2] pim sm
   [*CE-100GE1/0/2] igmp enable
   [*CE-100GE1/0/2] igmp version 3
   [*CE-100GE1/0/2] quit
   [*CE] ip route-static 192.168.10.1 24 100ge 1/0/1
   [*CE] commit
   ```

#### Verifying the Configuration

# Run the **display bgp mvpn all peer** command on each leaf node to query BGP MVPN peer information. For example, the command output on Leaf 1 is as follows:

```
[~Leaf1] display bgp mvpn all peer
 BGP local router ID        : 1.1.1.1
 Local AS number            : 100
 Total number of peers      : 2
 Peers in established state : 2

  Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
  2.2.2.2         4         100     1860     1859     0 04:43:30 Established        1
  3.3.3.3         4         100     3219     3221     0 04:43:39 Established        1
```

# After the receivers initiate requests to join a multicast group, run the **display pim vpn-instance mcast1 routing-table** command on each leaf node to query information about its VPN instance PIM routing table.

* According to the command output on Leaf 1, Receiver 1 joins a multicast group through IGMP, and Receivers 2 and 3 join multicast groups through BGP.
  ```
  [~Leaf1] display pim vpn-instance mcast1 routing-table
   VPN-Instance: mcast1
   Total 1 (*, G) entry; 4 (S, G) entries
  
   (*, 225.1.1.1)
       RP: 1.1.1.10 (local)
       Protocol: pim-sm, Flag: WC
       UpTime: 04:43:57
       Upstream interface: Register
           Upstream neighbor: NULL
           RPF prime neighbor: NULL
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: pseudo
               Protocol: BGP, UpTime: 04:43:57, Expires: -
   
   (192.168.10.9, 225.1.1.1)
       RP: 1.1.1.10 (local)
       Protocol: pim-sm, Flag: SPT LOC ACT
       UpTime: 04:43:57
       Upstream interface: 100GE1/0/3.1
           Upstream neighbor: NULL
           RPF prime neighbor: NULL
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: pseudo
               Protocol: pim-sm, UpTime: 04:43:57, Expires: -
  
   (192.168.10.9, 232.1.1.1)
       Protocol: pim-ssm, Flag: SPT LOC ACT SG_RCVR 
       UpTime: 04:44:12
       Upstream interface: Vbdif10
           Upstream neighbor: NULL
           RPF prime neighbor: NULL
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: Vbdif20
               Protocol: igmp, UpTime: 04:44:12, Expires: -
  
   (192.168.10.9, 232.1.1.2)
       Protocol: pim-ssm, Flag: SPT LOC ACT
       UpTime: 04:44:12
       Upstream interface: Vbdif10
           Upstream neighbor: NULL
           RPF prime neighbor: NULL
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: pseudo
               Protocol: BGP, UpTime: 04:44:12, Expires: -
                  
   (192.168.10.9, 232.1.1.3)
       Protocol: pim-ssm, Flag: SPT LOC ACT
       UpTime: 04:43:52
       Upstream interface: Vbdif10
           Upstream neighbor: NULL
           RPF prime neighbor: NULL
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: pseudo
               Protocol: BGP, UpTime: 04:43:52, Expires: -
  ```
* According to Leaf 2's PIM VPN routing entry that corresponds to Receiver 2, the upstream interface is Through-BGP and the downstream outbound interface is 100GE1/0/3.
  ```
  [~Leaf2] display pim vpn-instance mcast1 routing-table
   VPN-Instance: mcast1
   Total 1 (S, G) entry
   
   (192.168.10.9, 232.1.1.2)
       Protocol: pim-ssm, Flag: SPT ACT 
       UpTime: 04:43:52
       Upstream interface: through-BGP
           Upstream neighbor: 1.1.1.1
           RPF prime neighbor: 1.1.1.1
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: 100GE1/0/3
               Protocol: igmp, UpTime: 04:43:52, Expires: -
  ```
* According to Leaf 3's PIM VPN routing entry for Receiver 3, the upstream interface is Through-BGP and the downstream outbound interface is VBDIF10. Receiver 4 has no multicast source specified. Therefore, the PIM VPN routing entry for Receiver 4 is an (\*, G) entry, with the downstream outbound interface being VBDIF20.
  ```
  [~Leaf3] display pim vpn-instance mcast1 routing-table
   VPN-Instance: mcast1
   Total 1 (*, G) entry; 2 (S, G) entries
   
   (*, 225.1.1.1)
       RP: 1.1.1.10 
       Protocol: pim-sm, Flag: WC
       UpTime: 04:43:57
       Upstream interface: through-BGP
           Upstream neighbor: 1.1.1.1
           RPF prime neighbor: 1.1.1.1
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: Vbdif20
               Protocol: igmp, UpTime: 04:43:57, Expires: -
   
   (192.168.10.9, 225.1.1.1)
       RP: 1.1.1.10 
       Protocol: pim-sm, Flag: SPT ACT
       UpTime: 04:43:57
       Upstream interface: through-BGP
           Upstream neighbor: 1.1.1.1
           RPF prime neighbor: 1.1.1.1
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: Vbdif20
               Protocol: pim-sm, UpTime: 04:43:57, Expires: -
   
   (192.168.10.9, 232.1.1.3)
       Protocol: pim-ssm, Flag: SPT ACT
       UpTime: 104:44:50
       Upstream interface: through-BGP
           Upstream neighbor: 1.1.1.1
           RPF prime neighbor: 1.1.1.1
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: Vbdif10
               Protocol: igmp, UpTime: 04:44:50, Expires: -
  ```

#### Configuration Scripts

* Leaf1
  
  ```
  #
  sysname Leaf1
  #
  evpn-overlay enable
  #
  multicast routing-enable
  #
  multicast mvpn 1.1.1.9
  #
  ip vpn-instance mcast1
   ipv4-family
    route-distinguisher 1:1
    vpn-target 1:1 export-extcommunity
    vpn-target 13:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 13:1 import-extcommunity evpn
    multicast routing-enable
    multicast mvpn route-import local-admin-id 1
    mvpn          
     c-multicast signaling bgp
     spt-only mode
     auto-discovery inter-as
     ipmsi-tunnel 
      vxlan static
   vxlan vni 5010 
  #               
  bridge-domain 10
   vxlan vni 10   
   evpn           
    route-distinguisher 11:1
    vpn-target 12:1 export-extcommunity
    vpn-target 13:1 export-extcommunity
    vpn-target 12:1 import-extcommunity
    vpn-target 13:1 import-extcommunity
  #               
  bridge-domain 20
   vxlan vni 20   
   evpn           
    route-distinguisher 11:2
    vpn-target 12:2 export-extcommunity
    vpn-target 13:1 export-extcommunity
    vpn-target 12:2 import-extcommunity
    vpn-target 13:1 import-extcommunity
  #
  interface Vbdif10
   ip binding vpn-instance mcast1
   ip address 192.168.10.1 255.255.255.0
   pim sm         
   igmp enable    
   vxlan anycast-gateway enable
   arp collect host enable
  #               
  interface Vbdif20
   ip binding vpn-instance mcast1
   ip address 192.168.20.1 255.255.255.0
   pim sm         
   igmp enable    
   igmp version 3    
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/4.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   pim sm
  #
  interface LoopBack2
   ip address 1.1.1.9 255.255.255.255
  #
  interface LoopBack3
   ip binding vpn-instance mcast1
   ip address 1.1.1.10 255.255.255.255
   pim sm
  #                
  interface Nve1  
   source 1.1.1.9 
   vni 10 head-end peer-list protocol bgp
   vni 20 head-end peer-list protocol bgp
   vni 5010 mcast-group 225.0.0.1
  #
  bgp 100         
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 ebgp-max-hop 255
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 ebgp-max-hop 255
   peer 3.3.3.3 connect-interface LoopBack1
   peer 10.1.1.2 as-number 200
   peer 10.1.2.2 as-number 200
   #              
   ipv4-family unicast
    network 1.1.1.1 255.255.255.255
    network 1.1.1.9 255.255.255.255
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
    peer 10.1.1.2 enable
    peer 10.1.2.2 enable
   #              
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #               
   ipv4-family vpn-instance mcast1
    import-route direct
    advertise l2vpn evpn
   #              
  bgp 300 instance evpn1
   peer 2.2.2.9 as-number 300
   peer 2.2.2.9 connect-interface LoopBack2
   peer 3.3.3.9 as-number 300
   peer 3.3.3.9 connect-interface LoopBack2
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2.2.2.9 enable
    peer 2.2.2.9 advertise irb
    peer 3.3.3.9 enable
    peer 3.3.3.9 advertise irb
  #
  pim
   static-rp 1.1.1.1
  #
  pim vpn-instance mcast1
   static-rp 1.1.1.10
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
  multicast routing-enable
  #
  multicast mvpn 2.2.2.9
  #
  ip vpn-instance mcast1
   ipv4-family
    route-distinguisher 1:1
    vpn-target 1:1 export-extcommunity
    vpn-target 13:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 13:1 import-extcommunity evpn
    multicast routing-enable
    multicast mvpn route-import local-admin-id 1
    mvpn          
     c-multicast signaling bgp
     auto-discovery inter-as
     ipmsi-tunnel 
      vxlan static
   vxlan vni 5010 
  #               
  bridge-domain 10
   vxlan vni 10   
   evpn           
    route-distinguisher 11:1
    vpn-target 12:1 export-extcommunity
    vpn-target 13:1 export-extcommunity
    vpn-target 12:1 import-extcommunity
    vpn-target 13:1 import-extcommunity
  #               
  interface Vbdif10
   ip binding vpn-instance mcast1
   ip address 192.168.10.2 255.255.255.0
   pim sm         
   igmp enable    
   igmp version 3    
   vxlan anycast-gateway enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/3
   undo portswitch
   ip binding vpn-instance mcast1
   ip address 192.168.30.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3    
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #               
  interface LoopBack2
   ip address 2.2.2.9 255.255.255.255
  #
  interface Nve1  
   source 2.2.2.9 
   vni 10 head-end peer-list protocol bgp
   vni 5010 mcast-group 225.0.0.1
  #
  bgp 200         
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 ebgp-max-hop 255
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   peer 10.1.1.1 as-number 100
   peer 10.1.3.2 as-number 200
   #              
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    network 2.2.2.9 255.255.255.255
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 10.1.1.1 enable
    peer 10.1.3.2 enable
   #              
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #              
   ipv4-family vpn-instance mcast1
    import-route static
    advertise l2vpn evpn
   #              
  bgp 300 instance evpn1
   peer 1.1.1.9 as-number 300
   peer 1.1.1.9 connect-interface LoopBack2
   peer 3.3.3.9 as-number 300
   peer 3.3.3.9 connect-interface LoopBack2
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.9 enable
    peer 3.3.3.9 enable
  #
  pim
   static-rp 1.1.1.1
  #               
  ip route-static vpn-instance mcast1 192.168.40.0 255.255.255.0 100GE1/0/3
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
  multicast routing-enable
  #
  multicast mvpn 3.3.3.9
  #
  ip vpn-instance mcast1
   ipv4-family
    route-distinguisher 1:1
    vpn-target 1:1 export-extcommunity
    vpn-target 13:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 13:1 import-extcommunity evpn
    multicast routing-enable
    multicast mvpn route-import local-admin-id 1
    mvpn          
     c-multicast signaling bgp
     spt-only mode
     auto-discovery inter-as
     ipmsi-tunnel 
      vxlan static
   vxlan vni 5010 
  #
  bridge-domain 10
   vxlan vni 10   
   evpn           
    route-distinguisher 11:1
    vpn-target 12:1 export-extcommunity
    vpn-target 13:1 export-extcommunity
    vpn-target 12:1 import-extcommunity
    vpn-target 13:1 import-extcommunity
  #               
  bridge-domain 20
   vxlan vni 20   
   evpn           
    route-distinguisher 11:2
    vpn-target 12:2 export-extcommunity
    vpn-target 13:1 export-extcommunity
    vpn-target 12:2 import-extcommunity
    vpn-target 13:1 import-extcommunity
  #
  interface Vbdif10
   ip binding vpn-instance mcast1
   ip address 192.168.10.3 255.255.255.0
   pim sm         
   igmp enable
   igmp version 3    
   vxlan anycast-gateway enable
   arp collect host enable
  #               
  interface Vbdif20
   ip binding vpn-instance mcast1
   ip address 192.168.20.2 255.255.255.0
   pim sm         
   igmp enable    
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/4.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #               
  interface LoopBack2
   ip address 3.3.3.9 255.255.255.255
  #
  interface Nve1  
   source 3.3.3.9 
   vni 10 head-end peer-list protocol bgp
   vni 20 head-end peer-list protocol bgp
   vni 5010 mcast-group 225.0.0.1
  #               
  bgp 200         
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 ebgp-max-hop 255
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 connect-interface LoopBack1
   peer 10.1.2.1 as-number 100
   peer 10.1.3.1 as-number 200
   #              
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    network 3.3.3.9 255.255.255.255
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 10.1.2.1 enable
    peer 10.1.3.1 enable
   #              
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #              
  bgp 300 instance evpn1
   peer 1.1.1.9 as-number 300
   peer 1.1.1.9 connect-interface LoopBack2
   peer 2.2.2.9 as-number 300
   peer 2.2.2.9 connect-interface LoopBack2
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.9 enable
    peer 1.1.1.9 advertise irb
    peer 2.2.2.9 enable
    peer 2.2.2.9 advertise irb
  #               
  pim
   static-rp 1.1.1.1
  #
  pim vpn-instance mcast1
   static-rp 1.1.1.10
  #
  return
  ```
* CE
  
  ```
  #
  sysname CE
  #
  multicast routing-enable
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.30.2 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.40.1 255.255.255.0
   pim sm         
   igmp enable
   igmp version 3    
  #
  ip route-static 192.168.10.0 255.255.255.0 100GE1/0/3
  #
  return
  ```