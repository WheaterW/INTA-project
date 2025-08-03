Example for Configuring IPv4 Layer 3 Multicast over VXLAN in an M-LAG Active-Active Gateway Scenario
====================================================================================================

Example for Configuring IPv4 Layer 3 Multicast over VXLAN in an M-LAG Active-Active Gateway Scenario

#### Networking Requirements

In the IPv4 networking shown in [Figure 1](#EN-US_TASK_0000001136175960__fig_dc_vrp_multicast_cfg_007401), Leaf1, Leaf2, and Leaf3 are deployed as distributed VXLAN gateways, and Leaf2 and Leaf3 form M-LAG active-active gateways. Both the multicast source and receiver are on the VXLAN overlay network. The source accesses the VXLAN network through a Layer 2 sub-interface on Leaf 1 and belongs to BD20. The receiver accesses the VXLAN network through Layer 2 sub-interfaces on the active-active gateways Leaf 2 and Leaf 3 and belongs to BD10. The receiver requests to receive programs from (192.168.20.9, 232.1.1.1), with the multicast source specified.

In this case, you need to configure IPv4 Layer 3 multicast on the VXLAN network where distributed gateways are deployed.

**Figure 1** Configuring IPv4 Layer 3 multicast over VXLAN in an M-LAG active-active gateway scenario![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001261119081.png)

**Table 1** Device interface information
| Device | Interface | IP Address |
| --- | --- | --- |
| Leaf1 | 100GE1/0/1 | 10.1.1.1/24 |
| VBDIF20 | 192.168.20.1/24 |
| LoopBack1 | 1.1.1.1/32 |
| LoopBack2 | 1.1.1.10/32 |
| Leaf2 | 100GE1/0/1 | 10.1.2.1/24 |
| VBDIF10 | 192.168.10.1/24 |
| LoopBack1 | 2.2.2.2/32 |
| LoopBack2 | 2.2.2.210/32 |
| MEth0/0/0 | 10.10.10.1/24 |
| VLANIF4000 | 10.10.20.1/24 |
| Leaf3 | 100GE1/0/1 | 10.1.3.1/24 |
| VBDIF10 | 192.168.10.1/24 |
| LoopBack1 | 3.3.3.3/32 |
| LoopBack2 | 2.2.2.210/32 |
| MEth0/0/0 | 10.10.10.2/24 |
| VLANIF4000 | 10.10.20.2/24 |
| Spine | 100GE1/0/1 | 10.1.1.2/24 |
| 100GE1/0/2 | 10.1.2.2/24 |
| 100GE1/0/3 | 10.1.3.2/24 |
| LoopBack1 | 4.4.4.4/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an M-LAG between Leaf 2 and Leaf 3.
2. Configure each leaf node to set up VXLAN tunnels using BGP EVPN, deploy distributed gateways, and implement inter-device Layer 3 communication between hosts through VPN routes.
3. Configure BUM multicast replication for the Layer 3 VNI of the L3VPN instance on each leaf node.
4. Establish a BGP MVPN peer relationship between any two of Leaf 1, Leaf 2, and Leaf 3.
5. Configure a VXLAN I-PMSI tunnel on each leaf node.
6. Enable PIM-SM on the interface bound to the L3VPN instance on each leaf node to establish a C-multicast routing table.
7. Configure IGMP on the interfaces that connect multicast devices to user network segments.


#### Procedure

1. Configure IP addresses and a unicast routing protocol for interfaces on each device. In this example, OSPF is used for interworking to implement communication between devices at the network layer. The configurations of Leaf 2, Leaf 3, and Spine are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf1
   [*HUAWEI] commit
   [~Leaf1] interface loopback 1
   [*Leaf1-LoopBack1] ip address 1.1.1.1 32
   [*Leaf1-LoopBack1] quit
   [*Leaf1] interface 100ge 1/0/1
   [*Leaf1-100GE1/0/1] undo portswitch
   [*Leaf1-100GE1/0/1] ip address 10.1.1.1 24
   [*Leaf1-100GE1/0/1] quit
   [*Leaf1] ospf
   [*Leaf1-ospf-1] area 0
   [*Leaf1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   [*Leaf1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*Leaf1-ospf-1-area-0.0.0.0] quit
   [*Leaf1-ospf-1] quit
   [*Leaf1] commit
   ```
   
   After OSPF is configured, the devices can use it to learn the interface IP address of each other and ping one another. For example, the command output when Leaf 1 pings the IP address of Loopback 1 on Leaf 2 is as follows:
   
   ```
   [~Leaf1] ping 2.2.2.2
     PING 2.2.2.2: 56  data bytes, press CTRL_C to break                           
       Reply from 2.2.2.2: bytes=56 Sequence=1 ttl=254 time=2 ms                   
       Reply from 2.2.2.2: bytes=56 Sequence=2 ttl=254 time=1 ms                   
       Reply from 2.2.2.2: bytes=56 Sequence=3 ttl=254 time=1 ms                   
       Reply from 2.2.2.2: bytes=56 Sequence=4 ttl=254 time=1 ms                   
       Reply from 2.2.2.2: bytes=56 Sequence=5 ttl=254 time=1 ms                   
                                                                                   
     --- 2.2.2.2 ping statistics ---                                               
       5 packet(s) transmitted                                                     
       5 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max = 1/1/1 ms 
   ```
2. Configure a V-STP-based M-LAG on Leaf 2 and Leaf 3.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the link between Leaf 2 and the VXLAN network fails, Leaf 2 will discard all the traffic from the receiver because no upstream outbound interface is available. To prevent this problem, configure a monitor-link group to associate the upstream and downstream interfaces of Leaf 2. When the upstream interface of Leaf 2 goes down, the downstream interface will be shut down. As a result, traffic from the receiver is not forwarded through Leaf 2, preventing the traffic loss.
   
   ```
   [~Leaf2] interface meth 0/0/0
   [*Leaf2-MEth0/0/0] ip address 10.10.10.1 24
   [*Leaf2-MEth0/0/0] quit
   [*Leaf2] stp mode rstp
   [*Leaf2] stp v-stp enable
   [*Leaf2] dfs-group 1
   [*Leaf2-dfs-group-1] dual-active detection source ip 10.10.10.1 peer 10.10.10.2
   [*Leaf2-dfs-group-1] quit
   [*Leaf2] interface eth-trunk 1
   [*Leaf2-Eth-Trunk1] trunkport 100ge 1/0/4 to 1/0/5
   [*Leaf2-Eth-Trunk1] mode lacp-static
   [*Leaf2-Eth-Trunk1] peer-link 1
   [*Leaf2-Eth-Trunk1] quit
   [*Leaf2] interface eth-trunk 10
   [*Leaf2-Eth-Trunk10] trunkport 100ge 1/0/2 to 1/0/3
   [*Leaf2-Eth-Trunk10] mode lacp-static
   [*Leaf2-Eth-Trunk10] dfs-group 1 m-lag 1
   [*Leaf2-Eth-Trunk10] stp edged-port enable
   [*Leaf2-Eth-Trunk10] quit
   [*Leaf2] commit
   [~Leaf2] monitor-link group 1
   [*Leaf2-mtlk-group1] port 100GE1/0/1 uplink
   [*Leaf2-mtlk-group1] port eth-trunk 10 downlink 1
   [*Leaf2-mtlk-group1] quit
   [*Leaf2] commit
   ```
3. Configure VXLAN.
   
   # Configure service access points on leaf nodes.
   * Configure Leaf 1.
     ```
     [~Leaf1] bridge-domain 20
     [*Leaf1-bd20] quit
     [*Leaf1] interface 100ge 1/0/2.1 mode l2
     [*Leaf1-100GE1/0/2.1] undo portswitch
     [*Leaf1-100GE1/0/2.1] encapsulation dot1q vid 20
     [*Leaf1-100GE1/0/2.1] bridge-domain 20
     [*Leaf1-100GE1/0/2.1] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 2. The configuration of Leaf 3 is similar to the configuration of Leaf 2. For detailed configurations, see Configuration Scripts.
     ```
     [~Leaf2] bridge-domain 10
     [*Leaf2-bd10] quit
     [*Leaf2] interface eth-trunk 10.1 mode l2
     [*Leaf2-Eth-Trunk10.1] encapsulation dot1q vid 10
     [*Leaf2-Eth-Trunk10.1] bridge-domain 10
     [*Leaf2-Eth-Trunk10.1] quit
     [*Leaf2] commit
     ```
   
   # Configure BGP EVPN on each leaf node as the VXLAN control plane protocol and establish BGP EVPN peer relationships. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] evpn-overlay enable
   [*Leaf1] bgp 100
   [*Leaf1-bgp] peer 2.2.2.2 as-number 100
   [*Leaf1-bgp] peer 2.2.2.2 connect-interface LoopBack1
   [*Leaf1-bgp] peer 3.3.3.3 as-number 100
   [*Leaf1-bgp] peer 3.3.3.3 connect-interface LoopBack1
   [*Leaf1-bgp] l2vpn-family evpn
   [*Leaf1-bgp-af-evpn] peer 2.2.2.2 enable
   [*Leaf1-bgp-af-evpn] peer 3.3.3.3 enable
   [*Leaf1-bgp-af-evpn] quit
   [*Leaf1-bgp] quit
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
   
   # Configure ingress replication on each leaf node.
   * Configure Leaf 1.
     ```
     [~Leaf1] interface nve 1
     [*Leaf1-Nve1] source 1.1.1.1
     [*Leaf1-Nve1] vni 5010 head-end peer-list protocol bgp
     [*Leaf1-Nve1] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 2.
     ```
     [~Leaf2] interface nve 1
     [*Leaf2-Nve1] source 2.2.2.210
     [*Leaf2-Nve1] mac-address 00e0-fc12-3456
     [*Leaf2-Nve1] vni 5010 head-end peer-list protocol bgp
     [*Leaf2-Nve1] quit
     [*Leaf2] commit
     ```
   * Configure Leaf 3. Because Leaf 2 and Leaf 3 are active-active gateways, ensure that the IP addresses and MAC addresses of NVE interfaces on the two gateways are the same.
     ```
     [~Leaf3] interface nve 1
     [*Leaf3-Nve1] source 2.2.2.210
     [*Leaf3-Nve1] mac-address 00e0-fc12-3456
     [*Leaf3-Nve1] vni 5010 head-end peer-list protocol bgp
     [*Leaf3-Nve1] quit
     [*Leaf3] commit
     ```
   
   # Configure a Layer 3 VXLAN gateway on each leaf node.
   
   * Configure Leaf 1 as a Layer 3 VXLAN gateway.
     ```
     [~Leaf1] interface vbdif 20
     [*Leaf1-Vbdif20] ip binding vpn-instance mcast1
     [*Leaf1-Vbdif20] ip address 192.168.20.1 24
     [*Leaf1-Vbdif20] vxlan anycast-gateway enable
     [*Leaf1-Vbdif20] arp collect host enable
     [*Leaf1-Vbdif20] quit
     [*Leaf1] commit
     ```
   * Configure Leaf 2 as a Layer 3 VXLAN gateway.
     ```
     [~Leaf2] interface vbdif 10
     [*Leaf2-Vbdif10] ip binding vpn-instance mcast1
     [*Leaf2-Vbdif10] ip address 192.168.10.1 24
     [*Leaf2-Vbdif10] vxlan anycast-gateway enable
     [*Leaf2-Vbdif10] arp collect host enable
     [*Leaf2-Vbdif10] quit
     [*Leaf2] commit
     ```
   * Configure Leaf 3 as a Layer 3 VXLAN gateway. Because Leaf 2 and Leaf 3 are active-active gateways, ensure that the IP addresses of their VBDIF interfaces are the same.
     ```
     [~Leaf3] interface vbdif 10
     [*Leaf3-Vbdif10] ip binding vpn-instance mcast1
     [*Leaf3-Vbdif10] ip address 192.168.10.1 24
     [*Leaf3-Vbdif10] vxlan anycast-gateway enable
     [*Leaf3-Vbdif10] arp collect host enable
     [*Leaf3-Vbdif10] quit
     [*Leaf3] commit
     ```
   
   # Configure BGP on each leaf node to advertise IRB routes to its peers. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] bgp 100
   [~Leaf1-bgp] l2vpn-family evpn
   [~Leaf1-bgp-af-evpn] peer 2.2.2.2 advertise irb
   [*Leaf1-bgp-af-evpn] peer 3.3.3.3 advertise irb
   [*Leaf1-bgp-af-evpn] quit
   [*Leaf1-bgp] quit
   [*Leaf1] commit
   ```
   
   # Configure BGP on Leaf 1 to advertise IP prefix routes to its peers.
   
   ```
   [~Leaf1] bgp 100
   [~Leaf1-bgp] ipv4-family vpn-instance mcast1
   [*Leaf1-bgp-mcast1] import-route direct
   [*Leaf1-bgp-mcast1] advertise l2vpn evpn
   [*Leaf1-bgp-mcast1] quit
   [*Leaf1-bgp] quit
   [*Leaf1] commit
   ```
   
   # Configure public network Layer 3 multicast on each leaf node and Spine. The configurations of Leaf 1, Leaf 2, and Leaf 3 are similar to the configuration of Spine. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Spine] multicast routing-enable
   [*Spine] interface loopback 1
   [*Spine-LoopBack1] pim sm
   [*Spine-LoopBack1] quit
   [*Spine] interface 100ge 1/0/1
   [*Spine-100GE1/0/1] undo portswitch
   [*Spine-100GE1/0/1] pim sm
   [*Spine-100GE1/0/1] quit
   [*Spine] interface 100ge 1/0/2
   [*Spine-100GE1/0/2] undo portswitch
   [*Spine-100GE1/0/2] pim sm
   [*Spine-100GE1/0/2] quit
   [*Spine] interface 100ge 1/0/3
   [*Spine-100GE1/0/3] undo portswitch
   [*Spine-100GE1/0/3] pim sm
   [*Spine-100GE1/0/3] quit
   [*Spine] pim
   [*Spine-pim] static-rp 4.4.4.4
   [*Spine-pim] quit
   [*Spine] commit
   ```
   
   # Configure BUM multicast replication for the Layer 3 VNI of the L3VPN instance on each leaf node. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] interface nve 1
   [*Leaf1-Nve1] vni 5010 mcast-group 225.0.0.1
   [*Leaf1-Nve1] quit
   [*Leaf1] commit
   ```
   
   # Add VLANIF interfaces on Leaf2 and Leaf3 to multicast groups so that the M-LAG master and backup devices can synchronize VXLAN-encapsulated multicast packets through the peer-link. The configuration of Leaf 3 is similar to the configuration of Leaf 2. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf2] vlan 4000
   [*Leaf2-vlan4000] quit
   [*Leaf2] interface vlanif 4000
   [*Leaf2-Vlanif4000] ip address 10.10.20.1 24
   [*Leaf2-Vlanif4000] vxlan multicast-group member enable
   [*Leaf2-Vlanif4000] pim sm
   [*Leaf2-Vlanif4000] quit
   [*Leaf2] commit
   ```
   
   After the preceding configurations are complete, VXLAN tunnels can be established between the leaf nodes. You can run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command to view VXLAN tunnel information. For example, in the command output on Leaf 1, the **State** field is **up**, indicating that the VXLAN tunnel is reachable. If the value of the **Type** field is **static**, the destination IP address is statically configured. If the value is **dynamic**, the destination IP address is dynamically learned through a protocol.
   
   ```
   [~Leaf1] display vxlan tunnel
   Number of vxlan tunnel : 2
   Tunnel ID   Source                Destination           State  Type     Uptime
   -----------------------------------------------------------------------------------
   4026531841  1.1.1.1               225.0.0.1             up     static   04:44:52  
   4026531845  1.1.1.1               2.2.2.210             up     dynamic  04:40:52 
   ```
4. Establish BGP MVPN peer relationships on each leaf node.
   
   
   
   # Configure Leaf 1. The configurations of Leaf 2 and Leaf 3 are similar to the configuration of Leaf 1. For detailed configurations, see Configuration Scripts.
   
   ```
   [~Leaf1] bgp 100
   [~Leaf1-bgp] ipv4-family mvpn
   [*Leaf1-bgp-af-mvpn] peer 2.2.2.2 enable
   [*Leaf1-bgp-af-mvpn] peer 3.3.3.3 enable
   [*Leaf1-bgp-af-mvpn] quit
   [*Leaf1-bgp] quit
   [*Leaf1] commit
   ```
5. Configure a VXLAN I-PMSI tunnel on each leaf node.
   
   
   
   # Configure Leaf 1. The MVPN ID configured on a distributed VXLAN gateway must be the VTEP IP address of the gateway.
   
   ```
   [~Leaf1] multicast mvpn 1.1.1.1
   [*Leaf1] ip vpn-instance mcast1
   [*Leaf1-vpn-instance-mcast1] ipv4-family
   [*Leaf1-vpn-instance-mcast1-af-ipv4] multicast routing-enable
   [*Leaf1-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
   [*Leaf1-vpn-instance-mcast1-af-ipv4] mvpn
   [*Leaf1-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp
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
   [~Leaf2] multicast mvpn 2.2.2.210
   [*Leaf2] ip vpn-instance mcast1
   [*Leaf2-vpn-instance-mcast1] ipv4-family
   [*Leaf2-vpn-instance-mcast1-af-ipv4] multicast routing-enable
   [*Leaf2-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
   [*Leaf2-vpn-instance-mcast1-af-ipv4] mvpn
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] quit
   [*Leaf2-vpn-instance-mcast1-af-ipv4-mvpn] quit
   [*Leaf2-vpn-instance-mcast1-af-ipv4] quit
   [*Leaf2-vpn-instance-mcast1] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf 3. Because Leaf 2 and Leaf 3 are active-active gateways, ensure that the same MVPN ID is configured for them and that the MVPN ID is set to the VTEP IP address.
   
   ```
   [~Leaf3] multicast mvpn 2.2.2.210
   [*Leaf3] ip vpn-instance mcast1
   [*Leaf3-vpn-instance-mcast1] ipv4-family
   [*Leaf3-vpn-instance-mcast1-af-ipv4] multicast routing-enable
   [*Leaf3-vpn-instance-mcast1-af-ipv4] multicast mvpn route-import local-admin-id 1
   [*Leaf3-vpn-instance-mcast1-af-ipv4] mvpn
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] c-multicast signaling bgp
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] ipmsi-tunnel
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] vxlan static
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn-ipmsi] quit
   [*Leaf3-vpn-instance-mcast1-af-ipv4-mvpn] quit
   [*Leaf3-vpn-instance-mcast1-af-ipv4] quit
   [*Leaf3-vpn-instance-mcast1] quit
   [*Leaf3] commit
   ```
6. Configure PIM-SM and IGMP on VBDIF interfaces.
   
   
   
   # Configure Leaf 1.
   
   ```
   [~Leaf1] interface vbdif 20
   [~Leaf1-Vbdif20] pim sm
   [*Leaf1-Vbdif20] igmp enable
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
   [*Leaf3] commit
   ```
7. Configure the leaf nodes as VPN static RPs.
   
   
   
   # Configure Leaf 1.
   
   ```
   [~Leaf1] interface loopback 2
   [~Leaf1-LoopBack2] ip binding vpn-instance mcast1
   [*Leaf1-LoopBack2] ip address 1.1.1.10 32
   [*Leaf1-LoopBack2] pim sm
   [*Leaf1-LoopBack2] quit
   [*Leaf1] pim vpn-instance mcast1
   [*Leaf1-pim-mcast1] static-rp 1.1.1.10
   [*Leaf1-pim-mcast1] quit
   [*Leaf1] commit
   ```
   
   # Configure Leaf 2.
   
   ```
   [~Leaf2] pim vpn-instance mcast1
   [*Leaf2-pim-mcast1] static-rp 1.1.1.10
   [*Leaf2-pim-mcast1] quit
   [*Leaf2] commit
   ```
   
   # Configure Leaf 3.
   
   ```
   [~Leaf3] pim vpn-instance mcast1
   [*Leaf3-pim-mcast1] static-rp 1.1.1.10
   [*Leaf3-pim-mcast1] quit
   [*Leaf3] commit
   ```

#### Verifying the Configuration

# Run the **display bgp mvpn all peer** command on each leaf node to query BGP MVPN peer information. For example, the command output on Leaf 1 is as follows:

```
[~Leaf1] display bgp mvpn all peer
 BGP local router ID        : 1.1.1.1
 Local AS number            : 100
 Total number of peers      : 2
 Peers in established state : 2

  Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State         PrefRcv
  2.2.2.2         4         100     1860     1859     0 04:43:30     Established        1
  3.3.3.3         4         100     3219     3221     0 04:43:39     Established        1
```

# After the receivers initiate requests to join a multicast group, run the **display pim vpn-instance mcast1 routing-table** command on each leaf node to query information about its VPN instance PIM routing table.

* The command output on Leaf 1 shows that the multicast receiver joins the multicast group through BGP.
  ```
  [~Leaf1] display pim vpn-instance mcast1 routing-table
   VPN-Instance: mcast1
   Total 1 (S, G) entry
  
   (192.168.20.9, 232.1.1.1)
       Protocol: pim-ssm, Flag: SPT LOC ACT
       UpTime: 04:44:39
       Upstream interface: Vbdif20
           Upstream neighbor: NULL
           RPF prime neighbor: NULL
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: pseudo
               Protocol: BGP, UpTime: 04:44:39, Expires: -
  
  ```
* According to Leaf 2's PIM VPN routing entry for the receiver, the upstream interface is Through-BGP and the downstream outbound interface is VBDIF10.
  ```
  [~Leaf2] display pim vpn-instance mcast1 routing-table
   VPN-Instance: mcast1
   Total 1 (S, G) entry
   
   (192.168.20.9, 232.1.1.1)
       Protocol: pim-ssm, Flag: SPT ACT 
       UpTime: 04:44:18
       Upstream interface: through-BGP
           Upstream neighbor: 1.1.1.1
           RPF prime neighbor: 1.1.1.1
       Downstream interface(s) information:
       Total number of downstreams: 1
          1: Vbdif10
               Protocol: igmp, UpTime: 04:44:18, Expires: -
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
  multicast mvpn 1.1.1.1
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
     ipmsi-tunnel 
      vxlan static
   vxlan vni 5010 
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
  interface Vbdif20
   ip binding vpn-instance mcast1
   ip address 192.168.20.1 255.255.255.0
   pim sm         
   igmp enable    
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #               
  interface LoopBack2
   ip binding vpn-instance mcast1
   ip address 1.1.1.10 255.255.255.255
   pim sm
  #
  interface Nve1  
   source 1.1.1.1 
   vni 5010 head-end peer-list protocol bgp
   vni 5010 mcast-group 225.0.0.1
  #
  bgp 100         
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
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
   l2vpn-family evpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
  #               
  ospf 1          
   area 0.0.0.0   
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #               
  pim
   static-rp 4.4.4.4
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
  dfs-group 1
   dual-active detection source ip 10.10.10.1 peer 10.10.10.2
  #
  vlan batch 4000
  #
  stp mode rstp
  stp v-stp enable
  #
  evpn-overlay enable
  #
  multicast routing-enable
  #
  multicast mvpn 2.2.2.210
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
   ip address 192.168.10.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3    
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vlanif4000
   ip address 10.10.20.1 255.255.255.0
   pim sm
   vxlan multicast-group member enable
  #
  interface MEth0/0/0
   ip address 10.10.10.1 255.255.255.0
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
  #
  interface Eth-Trunk10
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #               
  interface LoopBack2
   ip address 2.2.2.210 255.255.255.255
  #               
  interface Nve1  
   source 2.2.2.210 
   vni 5010 head-end peer-list protocol bgp
   vni 5010 mcast-group 225.0.0.1
   mac-address 00e0-fc12-3456
  #
  monitor-link group 1
   port 100GE1/0/1 uplink
   port eth-trunk 10 downlink 1
  #
  bgp 100         
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #              
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
  #               
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.2 0.0.0.0
    network 2.2.2.210 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4
  #
  pim vpn-instance mcast1
   static-rp 1.1.1.10
  #
  return
  ```
* Leaf3
  
  ```
  #
  sysname Leaf3
  #
  dfs-group 1
   dual-active detection source ip 10.10.10.2 peer 10.10.10.1
  #
  vlan batch 4000
  #
  stp mode rstp
  stp v-stp enable
  #
  evpn-overlay enable
  #
  multicast routing-enable
  #
  multicast mvpn 2.2.2.210
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
   ip address 192.168.10.1 255.255.255.0
   pim sm         
   igmp enable
   igmp version 3    
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vlanif4000
   ip address 10.10.20.2 255.255.255.0
   pim sm
   vxlan multicast-group member enable
  #
  interface MEth0/0/0
   ip address 10.10.10.2 255.255.255.0
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
  #
  interface Eth-Trunk10
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface LoopBack2
   ip address 2.2.2.210 255.255.255.255
  #
  interface Nve1  
   source 2.2.2.210 
   vni 5010 head-end peer-list protocol bgp
   vni 5010 mcast-group 225.0.0.1
   mac-address 00e0-fc12-3456
  #
  monitor-link group 1
   port 100GE1/0/1 uplink
   port eth-trunk 10 downlink 1
  #               
  bgp 100         
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #              
   ipv4-family unicast
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #              
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
  #               
  ospf 1          
   area 0.0.0.0   
    network 2.2.2.210 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.3.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4
  #
  pim vpn-instance mcast1
   static-rp 1.1.1.10
  #
  return
  ```
* Spine
  
  ```
  #
  sysname Spine
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   pim sm         
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   pim sm
  #
  ospf 1          
   area 0.0.0.0   
    network 4.4.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  pim
   static-rp 4.4.4.4
  #
  return
  ```