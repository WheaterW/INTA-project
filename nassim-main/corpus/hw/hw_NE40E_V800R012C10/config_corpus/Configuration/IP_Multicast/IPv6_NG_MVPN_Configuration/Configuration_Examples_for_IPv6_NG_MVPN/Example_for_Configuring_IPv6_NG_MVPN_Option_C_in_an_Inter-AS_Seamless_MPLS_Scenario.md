Example for Configuring IPv6 NG MVPN Option C in an Inter-AS Seamless MPLS Scenario
===================================================================================

When devices are deployed in different ASs, you can deploy IPv6 NG MVPN in an inter-AS seamless MPLS scenario to implement end-to-end service interworking.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172367596__fig_dc_vrp_cfg_ngmvpn_027601), the PEs, ABR, and ASBRs are in different ASs. To allow the PEs to communicate and provide VPN services, you can configure IPv6 NG MVPN in an inter-AS seamless MPLS scenario.

**Figure 1** Networking for IPv6 NG MVPN in an inter-AS seamless MPLS scenario  
![](images/fig_dc_vrp_cfg_ngmvpn_027601.png)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1, 2, 3, and 4 in this example represent GE 0/1/1, GE 0/1/2, GE 0/1/3, and GE 0/1/4, respectively.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP protocol on each network for connectivity.
2. Configure MPLS and MPLS LDP and establish MPLS LSPs on each network.
3. Establish IBGP peer relationships in each AS and enable devices to exchange labeled routes.
4. Establish an EBGP peer relationship between ASBRs and enable these devices to exchange labeled routes across ASs.
5. Configure the ABR as an RR to help PE1 and ASBR1 obtain the route destined for each other's loopback interface.
6. Configure a routing policy to control label distribution for a BGP LSP to be established on each device. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node.
7. Configure peers.
8. Configure a P2MP LSP to carry multicast traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of devices (1.1.1.1, 1.1.1.2, 1.1.1.3, 1.1.1.4, and 1.1.1.5)
* Name of a routing policy (policy1)

#### Procedure

1. Configure an IGP on the MPLS backbone networks in AS100 and AS200, so that the PE and ASBR on the same MPLS backbone network can communicate. OSPF is used between PE1 and the ABR; IS-IS is used between the ABR and ASBR1, between ASBR2 and PE2, and between PEs and CEs; a static route is configured between ASBRs. For configuration details, see Configuration Files in this example.
2. Enable MPLS and LDP globally on each device and configure LDP LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the ABR.
   
   ```
   <ABR> system-view 
   ```
   ```
   [~ABR] mpls lsr-id 1.1.1.2
   ```
   ```
   [*ABR] mpls
   ```
   ```
   [*ABR-mpls] quit
   ```
   ```
   [*ABR] mpls ldp
   ```
   ```
   [*ABR-mpls-ldp] quit
   ```
   ```
   [*ABR] interface GigabitEthernet 0/1/2
   ```
   ```
   [*ABR-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*ABR-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*ABR-GigabitEthernet0/1/2] quit
   ```
   ```
   [*ABR] interface GigabitEthernet 0/1/3
   ```
   ```
   [*ABR-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*ABR-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*ABR-GigabitEthernet0/1/3] quit
   ```
   ```
   [*ABR] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 1.1.1.3
   ```
   ```
   [*ASBR1] mpls
   ```
   ```
   [*ASBR1-mpls] quit
   ```
   ```
   [*ASBR1] mpls ldp
   ```
   ```
   [*ASBR1-mpls-ldp] quit
   ```
   ```
   [*ASBR1] interface GigabitEthernet 0/1/3
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*ASBR1] interface GigabitEthernet 0/1/4
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/4] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/4] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/4] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls lsr-id 1.1.1.4
   ```
   ```
   [*ASBR2] mpls
   ```
   ```
   [*ASBR2-mpls] quit
   ```
   ```
   [*ASBR2] mpls ldp
   ```
   ```
   [*ASBR2-mpls-ldp] quit
   ```
   ```
   [*ASBR2] interface GigabitEthernet 0/1/1
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*ABR] interface GigabitEthernet 0/1/3
   ```
   ```
   [*ABR-GigabitEthernet0/1/3] mpls
   ```
   ```
   [*ABR-GigabitEthernet0/1/3] mpls ldp
   ```
   ```
   [*ABR-GigabitEthernet0/1/3] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 1.1.1.5
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
3. Configure an automatic mLDP P2MP LSP.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp
   ```
   ```
   [~PE1-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE1-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   
   The procedure for configuring PE2 is similar to the procedure for configuring PE1. For configuration details, see Configuration Files in this example.
   
   # Configure the ABR.
   
   ```
   [~ABR] mpls ldp
   ```
   ```
   [~ABR-mpls-ldp] mldp p2mp
   ```
   ```
   [*ABR-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*ABR-mpls-ldp] commit
   ```
   ```
   [~ABR-mpls-ldp] quit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls ldp
   ```
   ```
   [~ASBR1-mpls-ldp] mldp p2mp
   ```
   ```
   [*ASBR1-mpls-ldp] mldp recursive-fec
   ```
   ```
   [*ASBR1-mpls-ldp] commit
   ```
   ```
   [~ASBR1-mpls-ldp] quit
   ```
   
   The procedure for configuring ASBR2 is similar to the procedure for configuring ASBR1. For configuration details, see Configuration Files in this example.
4. Establish the IBGP peer relationship in each AS and the EBGP peer relationship between ASBRs and between PE1 and PE2. Enable the devices to exchange labeled routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 1.0
   ```
   ```
   [*PE1-bgp] peer 1.1.1.2 as-number 1.0
   ```
   ```
   [*PE1-bgp] peer 1.1.1.2 connect-interface LoopBack 0
   ```
   ```
   [*PE1-bgp] peer 1.1.1.5 as-number 65535.65535
   ```
   ```
   [*PE1-bgp] peer 1.1.1.5 ebgp-max-hop 10
   ```
   ```
   [*PE1-bgp] peer 1.1.1.5 connect-interface LoopBack0
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 1.1.1.2 label-route-capability
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 1.1.1.2 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 1.1.1.5 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] network 1.1.1.1 32
   ```
   ```
   [*PE1-bgp-af-ipv4] quit
   ```
   ```
   [*PE1-bgp] ipv6-family mvpn
   ```
   ```
   [*PE1-bgp-af-mvpnv6] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-mvpnv6] peer 1.1.1.5 enable
   ```
   ```
   [*PE1-bgp-af-mvpnv6] quit
   ```
   ```
   [*PE1-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE1-bgp-af-vpnv6] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-vpnv6] peer 1.1.1.5 enable
   ```
   ```
   [*PE1-bgp-af-vpnv6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the ABR.
   
   ```
   [~ABR] bgp 1.0
   ```
   ```
   [*ABR-bgp] peer 1.1.1.1 as-number 1.0
   ```
   ```
   [*ABR-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   ```
   ```
   [*ABR-bgp] peer 1.1.1.3 as-number 1.0
   ```
   ```
   [*ABR-bgp] peer 1.1.1.3 connect-interface LoopBack 0
   ```
   ```
   [*ABR-bgp] ipv4-family unicast
   ```
   ```
   [*ABR-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.1 enable
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.1 label-route-capability
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.3 enable
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.3 label-route-capability
   ```
   ```
   [*ABR-bgp-af-ipv4] quit
   ```
   ```
   [*ABR-bgp] quit
   ```
   ```
   [*ABR] commit
   ```
   
   # Configure ASBR1.
   
   ```
   <ASBR1> system-view 
   ```
   ```
   [~ASBR1] bgp 1.0
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.2 as-number 1.0
   ```
   ```
   [~ASBR1-bgp] peer 10.0.16.2 as-number 65535.65535
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.2 connect-interface LoopBack 0
   ```
   ```
   [*ASBR1-bgp] ipv4-family unicast
   ```
   ```
   [*ASBR1-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 10.0.16.2 enable
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 1.1.1.2 enable
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 10.0.16.2 label-route-capability
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 1.1.1.2 label-route-capability
   ```
   ```
   [*ASBR1-bgp-af-ipv4] quit
   ```
   ```
   [*ASBR1-bgp] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   <ASBR2> system-view 
   ```
   ```
   [~ASBR2] bgp 65535.65535
   ```
   ```
   [*ASBR2-bgp] peer 1.1.1.5 as-number 65535.65535
   ```
   ```
   [*ASBR2-bgp] peer 10.0.16.1 as-number 1.0
   ```
   ```
   [*ASBR2-bgp] peer 1.1.1.5 connect-interface LoopBack 0
   ```
   ```
   [*ASBR2-bgp] ipv4-family unicast
   ```
   ```
   [*ASBR2-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*ASBR2-bgp-af-ipv4] peer 10.0.16.1 enable
   ```
   ```
   [*ASBR2-bgp-af-ipv4] peer 1.1.1.5 enable
   ```
   ```
   [*ASBR2-bgp-af-ipv4] peer 10.0.16.1 label-route-capability
   ```
   ```
   [*ASBR2-bgp-af-ipv4] peer 1.1.1.5 label-route-capability
   ```
   ```
   [*ASBR2-bgp-af-ipv4] network 1.1.1.5 32
   ```
   ```
   [*ASBR2-bgp-af-ipv4] quit
   ```
   ```
   [*ASBR2-bgp] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 65535.65535
   ```
   ```
   [*PE2-bgp] peer 1.1.1.4 as-number 65535.65535
   ```
   ```
   [*PE2-bgp] peer 1.1.1.4 connect-interface LoopBack 0
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 1.0
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 ebgp-max-hop 10
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface LoopBack 0
   ```
   ```
   [*PE2-bgp] ipv4-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv4] undo synchronization
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 1.1.1.4 enable
   ```
   ```
   [*PE2-bgp-af-ipv4] peer 1.1.1.4 label-route-capability
   ```
   ```
   [*PE2-bgp-af-ipv4] quit
   ```
   ```
   [*PE2-bgp] ipv6-family mvpn
   ```
   ```
   [*PE2-bgp-af-mvpnv6] policy vpn-target
   ```
   ```
   [*PE2-bgp-af-mvpnv6] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-mvpnv6] quit
   ```
   ```
   [*PE2-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE2-bgp-af-vpnv6] policy vpn-target
   ```
   ```
   [*PE2-bgp-af-vpnv6] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv6] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
5. Configure the ABR as an RR to reflect routes so that PE1 and PE2 can obtain the route destined for each other's loopback interface.
   
   
   
   # Configure the ABR.
   
   ```
   [~ABR] bgp 1.0
   ```
   ```
   [*ABR-bgp] ipv4-family unicast
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.1 reflect-client
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.1 next-hop-local
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.3 reflect-client
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.3 next-hop-local
   ```
   ```
   [*ABR-bgp-af-ipv4] quit
   ```
   ```
   [*ABR-bgp] quit
   ```
   ```
   [*ABR] commit
   ```
6. Configure a route-policy on each device to establish BGP LSPs.
   
   
   
   # Create a route-policy on PE1 and apply the route-policy to the routes to be advertised to a specified peer.
   
   ```
   [~PE1] route-policy policy1 permit node 1
   ```
   ```
   [*PE1-route-policy] apply mpls-label
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] bgp 1.0
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 1.1.1.2 route-policy policy1 export
   ```
   ```
   [*PE1-bgp-af-ipv4] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration on PE2 is similar to that on PE1. For configuration details, see Configuration Files in this example.
   
   # Create a route-policy on the ABR and apply the route-policy to the routes to be advertised to specified peers.
   
   ```
   [~ABR] route-policy policy1 permit node 1
   ```
   ```
   [*ABR-route-policy] apply mpls-label
   ```
   ```
   [*ABR-route-policy] quit
   ```
   ```
   [*ABR] bgp 1.0
   ```
   ```
   [*ABR-bgp] ipv4-family unicast
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.1 route-policy policy1 export
   ```
   ```
   [*ABR-bgp-af-ipv4] peer 1.1.1.3 route-policy policy1 export
   ```
   ```
   [*ABR-bgp-af-ipv4] quit
   ```
   ```
   [*ABR-bgp] quit
   ```
   ```
   [*ABR] commit
   ```
   
   # Create a route-policy on ASBR1 and apply the route-policy to the routes to be advertised to specified peers.
   
   ```
   [~ASBR1] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [~ASBR1] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR1-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] bgp 1.0
   ```
   ```
   [*ASBR1-bgp] ipv4-family unicast
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 10.0.16.2 route-policy policy1 export
   ```
   ```
   [*ASBR1-bgp-af-ipv4] peer 1.1.1.2 route-policy policy2 export
   ```
   ```
   [*ASBR1-bgp-af-ipv4] quit
   ```
   ```
   [*ASBR1-bgp] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   The configuration of ASBR2 is similar to that of ASBR1. For configuration details, see Configuration Files in this example.
7. Create VPN instances and configure unicast peers.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance ngv6
   ```
   ```
   [*PE1-vpn-instance-ngv6] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6] route-distinguisher 1.2.3.4:1
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6] vpn-target 1:1 both
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-ngv6] quit
   ```
   ```
   [*PE1] interface GigabitEthernet0/1/3
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] ip binding vpn-instance ngv6
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] ipv6 address 2001:db8:6::3 64
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*PE1] bgp 1.0
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance ngv6
   ```
   ```
   [*PE1-bgp-af-vpn-ngv6] import-route isis 2
   ```
   ```
   [*PE1-bgp-af-vpn-ngv6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configuration on PE2 is similar to that on PE1. For configuration details, see Configuration Files in this example.
8. Configure a P2MP LSP on PEs to carry multicast traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] multicast ipv6 mvpn 1.1.1.1
   ```
   ```
   [~PE1] ip vpn-instance ngv6
   ```
   ```
   [~PE1-vpn-instance-ngv6] ipv6-family
   ```
   ```
   [~PE1-vpn-instance-ngv6-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6] mvpn
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn] sender-enable
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn] auto-discovery inter-as
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn-ipmsi] mldp
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn-ipmsi] quit
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-ngv6-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-ngv6] commit
   ```
   ```
   [~PE1-vpn-instance-ngv6] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] multicast ipv6 mvpn 1.1.1.5
   ```
   ```
   [~PE2] ip vpn-instance ngv6
   ```
   ```
   [~PE2-vpn-instance-ngv6] ipv6-family
   ```
   ```
   [~PE2-vpn-instance-ngv6-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [~PE2-vpn-instance-ngv6-af-ipv6] mvpn
   ```
   ```
   [*PE2-vpn-instance-ngv6-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE2-vpn-instance-ngv6-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE2-vpn-instance-ngv6-af-ipv6-mvpn] auto-discovery inter-as
   ```
   ```
   [*PE2-vpn-instance-ngv6-af-ipv6-mvpn] quit
   ```
   ```
   [*PE2-vpn-instance-ngv6-af-ipv6] quit
   ```
   ```
   [*PE2-vpn-instance-ngv6] commit
   ```
   ```
   [~PE2-vpn-instance-ngv6] quit
   ```
9. Configure PIM.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] pim-ipv6 vpn-instance ngv6
   ```
   ```
   [~PE1-pim6-ngv6] static-rp 2001:db8:6::3
   ```
   ```
   [*PE1-pim6-ngv6] source-lifetime 60
   ```
   ```
   [*PE1-pim6-ngv6] commit
   ```
   ```
   [~PE1-pim6-ngv6] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/1/3
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] pim ipv6 sm
   ```
   ```
   [*PE1-GigabitEthernet0/1/3] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/3] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] pim-ipv6 vpn-instance ngv6
   ```
   ```
   [~PE2-pim6-ngv6] static-rp 2001:db8:6::3
   ```
   ```
   [*PE2-pim6-ngv6] source-lifetime 60
   ```
   ```
   [*PE2-pim6-ngv6] commit
   ```
   ```
   [~PE2-pim6-ngv6] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/1/4
   ```
   ```
   [*PE2-GigabitEthernet0/1/4] pim ipv6 sm
   ```
   ```
   [*PE2-GigabitEthernet0/1/4] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/4] quit
   ```
10. Verify the configuration.
    
    
    
    After the configuration is complete, CEs can learn the routes to each other's interfaces and ping each other.
    
    The following example uses the command output on CE1.
    
    ```
    [~CE1] ping ipv6 2001:db8:14::1
    ```
    ```
      PING 2001:DB8:14::1: 56  data bytes, press CTRL_C to break
    ```
    ```
        Reply from 2001:DB8:14::1: bytes=56 Sequence=1 ttl=252 time=102 ms
    ```
    ```
        Reply from 2001:DB8:14::1: bytes=56 Sequence=2 ttl=252 time=89 ms
    ```
    ```
        Reply from 2001:DB8:14::1: bytes=56 Sequence=3 ttl=252 time=106 ms
    ```
    ```
        Reply from 2001:DB8:14::1: bytes=56 Sequence=4 ttl=252 time=104 ms
    ```
    ```
        Reply from 2001:DB8:14::1: bytes=56 Sequence=5 ttl=252 time=56 ms
    ```
    ```
      --- 2001:DB8:14::1 ping statistics ---
    ```
    ```
        5 packet(s) transmitted
    ```
    ```
        5 packet(s) received
    ```
    ```
        0.00% packet loss
    ```
    ```
        round-trip min/avg/max = 56/91/106 ms
    ```
    
    Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) command on a PE to check its PIM routing table.
    
    The following example uses the command output on PE1.
    
    ```
    <PE1> display pim ipv6 vpn-instance ipv6 ngv6 routing-table
    ```
    ```
     VPN-Instance: ngv6
     Total 1 (S, G) entry
    
     (2001:DB8:5::2, FF3E::1)
         Protocol: pim-ssm, Flag:
         UpTime: 00:24:09
         Upstream interface: through-BGP, Refresh time: 00:24:09
             Upstream neighbor: ::FFFF:1.1.1.5
             RPF prime neighbor: ::FFFF:1.1.1.5
         Downstream interface(s) information:
         Total number of downstreams: 1
            1: GigabitEthernet0/1/3
                 Protocol: pim-ssm, UpTime: 00:24:09, Expires: 00:02:35
    
    ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast ipv6 routing-enable
  #
  isis 2
   is-level level-2
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:5::6 64
   isis ipv6 enable 2
   pim ipv6 sm
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:6::6 64
   isis ipv6 enable 2
   pim ipv6 sm
  #
  pim-ipv6
   static-rp 2001:DB8:6::3
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1 
  #
  multicast ipv6 mvpn 1.1.1.1 
  #
  ip vpn-instance ngv6 
   ipv6-family 
    route-distinguisher 1.2.3.4:1 
   apply-label per-instance
    vpn-target 1:1 export-extcommunity 
    vpn-target 1:1 import-extcommunity 
    multicast ipv6 routing-enable 
    mvpn 
     sender-enable 
     c-multicast signaling bgp 
     rpt-spt mode 
     auto-discovery inter-as 
     ipmsi-tunnel 
      mldp 
  #
  mpls lsr-id 1.1.1.1 
  #
  mpls 
  #
  mpls ldp 
   mldp p2mp
   mldp recursive-fec 
   #
   ipv4-family 
   
  #
  isis 2 vpn-instance ngv6
    is-level level-2
   network-entity 10.0000.0000.0006.00
   ipv6 enable topology ipv6
   ipv6 import-route bgp
  #
  route-policy policy1 permit node 1 
   apply mpls-label 
  #
  interface GigabitEthernet0/1/2
   undo shutdown 
   ip address 10.0.11.6 255.255.255.0 
   mpls 
   mpls ldp 
  #
  interface GigabitEthernet0/1/3
   undo shutdown 
   ip binding vpn-instance ngv6 
   ipv6 enable
   ipv6 address 2001:DB8:6::3 64
   isis ipv6 enable 2
   pim ipv6 sm
  #
  interface LoopBack0 
   ip address 1.1.1.1 255.255.255.255 
  # 
  interface NULL0 
  #
  bgp 1.0 
   peer 1.1.1.2 as-number 1.0  
   peer 1.1.1.2 connect-interface LoopBack0  
   peer 1.1.1.5 as-number 65535.65535  
   peer 1.1.1.5 ebgp-max-hop 10  
   peer 1.1.1.5 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.1 255.255.255.255
    peer 1.1.1.2 enable
    peer 1.1.1.2 route-policy policy1 export
    peer 1.1.1.2 label-route-capability
    peer 1.1.1.5 enable
   #
   ipv6-family mvpn
    policy vpn-target
    peer 1.1.1.5 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 1.1.1.5 enable
   #
   ipv6-family vpn-instance ngv6
    import-route isis 2
  #
  ospf 1
   area 0.0.0.0
   network 10.0.11.0 0.0.0.255
   network 1.1.1.1 0.0.0.0
  #
  pim-ipv6 vpn-instance ngv6
   static-rp 2001:DB8:6::3
   source-lifetime 60
  #
  return
  ```
* ABR configuration file
  
  ```
  # 
  sysname ABR 
  # 
  mpls lsr-id 1.1.1.2 
  # 
  mpls 
  # 
  mpls ldp 
   mldp p2mp 
   mldp recursive-fec 
   
   ipv4-family 
  # 
  isis 1 
   is-level level-2 
   cost-style wide 
   network-entity 10.0000.0000.000c.00 
  # 
  interface GigabitEthernet0/1/2
   undo shutdown 
   ip address 10.0.7.5 255.255.255.0 
   isis enable 1 
   mpls 
   mpls ldp 
  # 
  interface GigabitEthernet0/1/3
   undo shutdown 
   ip address 10.0.11.5 255.255.255.0 
   mpls 
   mpls ldp 
  # 
  interface LoopBack0 
   ip address 1.1.1.2 255.255.255.255 
   isis enable 1 
  # 
  interface NULL0 
  # 
  bgp 1.0 
   peer 1.1.1.1 as-number 1.0 
   peer 1.1.1.1 connect-interface LoopBack0 
   peer 1.1.1.3 as-number 1.0 
   peer 1.1.1.3 connect-interface LoopBack0 
   # 
   ipv4-family unicast 
    undo synchronization 
    peer 1.1.1.1 enable 
    peer 1.1.1.1 route-policy policy1 export 
    peer 1.1.1.1 reflect-client 
    peer 1.1.1.1 next-hop-local 
    peer 1.1.1.1 label-route-capability 
    peer 1.1.1.3 enable 
    peer 1.1.1.3 route-policy policy1 export 
    peer 1.1.1.3 reflect-client 
    peer 1.1.1.3 next-hop-local 
    peer 1.1.1.3 label-route-capability 
  # 
  ospf 1 
   area 0.0.0.0 
   network 10.0.11.0 0.0.0.255 
   network 1.1.1.2 0.0.0.0 
  # 
  route-policy policy1 permit node 1 
   apply mpls-label 
  # 
  return 
  ```
* ASBR1 configuration file
  
  ```
  # 
  sysname ASBR1 
  # 
  mpls lsr-id 1.1.1.3 
  # 
  mpls 
  # 
  mpls ldp 
   mldp p2mp 
   mldp recursive-fec 
  # 
   ipv4-family 
  # 
  isis 1 
   is-level level-2 
   cost-style wide 
   network-entity 10.0000.0000.000a.00 
  # 
  interface GigabitEthernet0/1/3
   undo shutdown 
   ip address 10.0.7.7 255.255.255.0 
   isis enable 1 
   mpls 
   mpls ldp 
  # 
  interface GigabitEthernet0/1/4
   undo shutdown 
   ip address 10.0.16.1 255.255.255.0 
   mpls 
   mpls ldp 
  # 
  interface Virtual-Template0 
   ppp authentication-mode auto 
  # 
  interface LoopBack0 
   ip address 1.1.1.3 255.255.255.255 
   isis enable 1 
  # 
  interface NULL0 
  # 
  bgp 1.0 
   peer 10.0.16.2 as-number 65535.65535 
   peer 1.1.1.2 as-number 1.0 
   peer 1.1.1.2 connect-interface LoopBack0 
   #
   ipv4-family unicast
    undo synchronization
    peer 10.0.16.2 enable
    peer 10.0.16.2 route-policy policy1 export
    peer 10.0.16.2 label-route-capability
    peer 1.1.1.2 enable
    peer 1.1.1.2 route-policy policy2 export
    peer 1.1.1.2 label-route-capability 
  # 
  route-policy policy1 permit node 1
   apply mpls-label
  #
  route-policy policy2 permit node 1
   if-match mpls-label
   apply mpls-label
  # 
  ip route-static 1.1.1.4 255.255.255.255 10.0.16.2 
  # 
  return 
  ```
* ASBR2 configuration file
  
  ```
  # 
  sysname ASBR2 
  # 
  mpls lsr-id 1.1.1.4 
  # 
  mpls 
  # 
  mpls ldp 
   mldp p2mp 
   mldp recursive-fec 
  # 
   ipv4-family 
  # 
  isis 1 
   is-level level-2 
   cost-style wide 
   network-entity 10.0000.0000.000b.00 
  # 
  interface GigabitEthernet0/1/1
   undo shutdown 
   ip address 10.0.10.4 255.255.255.0
   isis enable 1 
   mpls 
   mpls ldp 
  # 
  interface GigabitEthernet0/1/3
   undo shutdown 
   ip address 10.0.16.2 255.255.255.0 
   mpls 
   mpls ldp 
  # 
  interface Virtual-Template0 
   ppp authentication-mode auto 
  # 
  interface LoopBack0 
   ip address 1.1.1.4 255.255.255.255 
   isis enable 1 
  # 
  interface NULL0 
  # 
  bgp 65535.65535 
   peer 10.0.16.1 as-number 1.0 
   peer 1.1.1.5 as-number 65535.65535 
   peer 1.1.1.5 connect-interface LoopBack0 
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.5 255.255.255.255
    peer 10.0.16.1 enable
    peer 10.0.16.1 route-policy policy1 export
    peer 10.0.16.1 label-route-capability
    peer 1.1.1.5 enable
    peer 1.1.1.5 route-policy policy2 export
    peer 1.1.1.5 label-route-capability
  # 
  route-policy policy1 permit node 1
   apply mpls-label
  #
  route-policy policy2 permit node 1
   if-match mpls-label
   apply mpls-label
  # 
  ip route-static 1.1.1.3 255.255.255.255 10.0.16.1 
  # 
  return 
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2 
  #
  multicast ipv6 mvpn 1.1.1.5
  #
  ip vpn-instance ngv6
   ipv6-family
   route-distinguisher 2.3:1
   apply-label per-instance
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
   multicast ipv6 routing-enable
   mvpn
    c-multicast signaling bgp
    rpt-spt mode
    auto-discovery inter-as
    ipmsi-tunnel
     mldp
  #
  mpls lsr-id 1.1.1.5
  #
  mpls
  #
  mpls ldp
   mldp p2mp
   mldp recursive-fec
   #
   ipv4-family
  # 
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.000d.00
  #
  isis 2 vpn-instance ngv6
   is-level level-2
   network-entity 10.0000.0000.0007.00
   ipv6 enable topology ipv6
   ipv6 import-route bgp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.10.3 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip binding vpn-instance ngv6  
   ipv6 enable
   ipv6 address 2001:DB8:14::4 64
   isis ipv6 enable 2
   pim ipv6 sm
  #
  interface Virtual-Template0
   ppp authentication-mode auto
  #
  interface LoopBack0
   ip address 1.1.1.5 255.255.255.255
   isis enable 1
  #
  interface NULL0
  #
  bgp 65535.65535
   peer 1.1.1.1 as-number 1.0
   peer 1.1.1.1 ebgp-max-hop 10
   peer 1.1.1.1 connect-interface LoopBack0
   peer 1.1.1.4 as-number 65535.65535
   peer 1.1.1.4 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 1.1.1.4 enable
    peer 1.1.1.4 label-route-capability
   #
   ipv6-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv6-family vpn-instance ngv6
    import-route isis 2
  #  
  pim-ipv6 vpn-instance ngv6
   static-rp 2001:DB8:6::3
   source-lifetime 60
  #  
  return 
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast ipv6 routing-enable
  #
  isis 2
   is-level level-2
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6-enable
   ipv6 address 2001:DB8:3::1 64
   isis ipv6 enable 2
   pim ipv6 sm
   mld enable
   mld static-group FF3E::1 source 2001:DB8:5::2
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ipv6-enable
   ipv6 address 2001:DB8:14::1 64
   isis ipv6 enable 2
   pim ipv6 sm
  #
  pim-ipv6
   static-rp 2001:DB8:6::3
  #
  return
  ```