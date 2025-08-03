Example for Configuring Dual-Homing Single-Active EVPN VPWS over MPLS (Active/Standby Status Determined by the DF Election Result)
==================================================================================================================================

This section provides an example for configuring dual-homing PEs to determine the active/standby status of PEs based on the DF election result in a scenario where a CE is dual-homed to PEs and accesses an EVPN VPWS over MPLS in single-active mode.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0289729494__fig14388142633716), PE1, PE2, the RR, and PE3 belong to the same AS. They need to communicate using OSPF, and MPLS tunnels need to be deployed to carry EVPN VPWS services. CE1 is dual-homed to PE1 and PE2 in single-active mode. PE1 and PE2 are configured to determine the active/standby status based on the DF election result. To improve reliability, associate CFM with the EVPN DF election function and configure local-remote FRR.

**Figure 1** Configuring dual-homing single-active EVPN VPWS over MPLS (active/standby status determined by the DF election result)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](figure/en-us_image_0289738377.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the backbone network to enable PEs and the RR to communicate.
2. Configure basic MPLS functions and enable MPLS LDP to establish MPLS LSPs on the backbone network.
3. Configure EVPN VPWS and an EVPL instance and bind an access-side sub-interface to the EVPL instance on each PE.
4. Configure an ESI and the dual-homing single-active mode; configure the PEs to determine their active/standby status based on the DF election result.
5. Configure local-remote FRR.
6. Establish BGP EVPN peer relationships between PEs and the RR. On the RR, configure the PEs as RR clients.
7. Configure CEs to access PEs through physical interfaces.
8. Associate CFM with EVPN DF election.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* EVPN instance RDs: 100:1, 100:2, and 100:3; RTs: 1:1

#### Procedure

1. Configure interface addresses on the RR and PEs according to [Figure 1](#EN-US_TASK_0289729494__fig14388142633716). For detailed configurations, see Configuration Files.
2. Configure an IGP on the backbone network to enable PEs and the RR to communicate. OSPF is used as an IGP in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE1-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE2-ospf-1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ospf 1
   ```
   ```
   [*PE3-ospf-1] area 0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   ```
   ```
   [*PE3-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE3-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE3-ospf-1] quit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] ospf 1
   ```
   ```
   [*RR-ospf-1] area 0
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*RR-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~RR-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~RR-ospf-1] quit
   ```
3. Configure basic MPLS functions and enable MPLS LDP to establish LDP LSPs on the MPLS backbone network.
   
   
   
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
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
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
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] mpls lsr-id 3.3.3.3
   ```
   ```
   [*RR] mpls
   ```
   ```
   [*RR-mpls] quit
   ```
   ```
   [*RR] mpls ldp
   ```
   ```
   [*RR-mpls-ldp] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/1/0
   ```
   ```
   [*RR-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/2/0
   ```
   ```
   [*RR-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*RR] interface gigabitethernet 0/3/0
   ```
   ```
   [*RR-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*RR-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*RR-GigabitEthernet0/3/0] commit
   ```
   ```
   [~RR-GigabitEthernet0/3/0] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 4.4.4.4
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE3-GigabitEthernet0/1/0] quit
   ```
4. Configure EVPN VPWS and an EVPL instance and bind an access-side sub-interface to the EVPL instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 vpws
   [*PE1-vpws-evpn-instance-evrf1] route-distinguisher 100:1
   [*PE1-vpws-evpn-instance-evrf1] vpn-target 1:1
   [*PE1-vpws-evpn-instance-evrf1] quit
   [*PE1] evpl instance 1
   [*PE1-evpl1] evpn binding vpn-instance evrf1
   [*PE1-evpl1] local-service-id 100 remote-service-id 200
   [*PE1-evpl1] quit
   [*PE1] interface gigabitethernet 0/1/0.1 mode l2
   [*PE1-GigabitEthernet 0/1/0.1] evpl instance 1
   [*PE1-GigabitEthernet 0/1/0.1] encapsulation dot1q vid 10
   [*PE1-GigabitEthernet 0/1/0.1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 vpws
   [*PE2-vpws-evpn-instance-evrf1] route-distinguisher 100:2
   [*PE2-vpws-evpn-instance-evrf1] vpn-target 1:1
   [*PE2-vpws-evpn-instance-evrf1] quit
   [*PE2] evpl instance 1
   [*PE2-evpl1] evpn binding vpn-instance evrf1
   [*PE2-evpl1] local-service-id 100 remote-service-id 200
   [*PE2-evpl1] quit
   [*PE2] interface gigabitethernet 0/1/0.1 mode l2
   [*PE2-GigabitEthernet 0/1/0.1] evpl instance 1
   [*PE2-GigabitEthernet 0/1/0.1] encapsulation dot1q vid 10
   [*PE2-GigabitEthernet 0/1/0.1] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 vpws
   [*PE3-vpws-evpn-instance-evrf1] route-distinguisher 100:3
   [*PE3-vpws-evpn-instance-evrf1] vpn-target 1:1
   [*PE3-vpws-evpn-instance-evrf1] quit
   [*PE3] evpl instance 1
   [*PE3-evpl1] evpn binding vpn-instance evrf1
   [*PE3-evpl1] local-service-id 200 remote-service-id 100
   [*PE3-evpl1] quit
   [*PE3] interface gigabitethernet 0/2/0.1 mode l2
   [*PE3-GigabitEthernet 0/2/0.1] evpl instance 1
   [*PE3-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 10
   [*PE3-GigabitEthernet 0/2/0.1] quit
   [*PE3] commit
   ```
5. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 4.4.4.4
   ```
   ```
   [*PE3] commit
   ```
6. Configure an ESI and the dual-homing single-active mode; configure the PEs to determine their active/standby status based on the DF election result.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] esi 0000.1111.2222.1111.1111
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] evpn
   [*PE1-evpn] vpws-df-election type service-id
   [*PE1-evpn] esi 0000.1111.2222.1111.1111
   [*PE1-evpn-esi-0000.1111.2222.1111.1111] evpn redundancy-mode single-active df-election
   [*PE1-evpn-esi-0000.1111.2222.1111.1111] quit
   [*PE1-evpn] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/1/0
   [~PE2-GigabitEthernet0/1/0] esi 0000.1111.2222.1111.1111
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] evpn
   [*PE2-evpn] vpws-df-election type service-id
   [*PE2-evpn] esi 0000.1111.2222.1111.1111
   [*PE2-evpn-esi-0000.1111.2222.1111.1111] evpn redundancy-mode single-active df-election
   [*PE2-evpn-esi-0000.1111.2222.1111.1111] quit
   [*PE2-evpn] quit
   [*PE2] commit
   ```
7. Configure local-remote FRR on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] local-remote frr enable
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] local-remote frr enable
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] remote frr enable
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] commit
   ```
8. Establish BGP EVPN peer relationships between PEs and the RR. On the RR, configure the PEs as RR clients.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE3-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE3-bgp-af-evpn] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] bgp 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*RR-bgp] l2vpn-family evpn
   ```
   ```
   [*RR-bgp-af-evpn] undo policy vpn-target
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] quit
   ```
   ```
   [*RR-bgp] quit
   ```
   ```
   [*RR] commit
   ```
   
   After completing the configurations, run the **display bgp evpn peer** command on the RR. The command output shows that BGP peer relationships are in the **Established** state, indicating that BGP peer relationships have been successfully established between the PEs and RR.
   
   ```
   [~RR] display bgp evpn peer
   ```
   ```
    
    BGP local router ID : 3.3.3.3
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.1         4         100        9       15     0 00:03:41 Established        1
     2.2.2.2         4         100        9       15     0 00:03:42 Established        1
     4.4.4.4         4         100        8       15     0 00:03:42 Established        1
   ```
9. Configure CEs to access PEs through physical interfaces.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] vlan 10
   [*CE1-vlan10] quit
   [*CE1] interface gigabitethernet0/1/0
   [*CE1-GigabitEthernet0/1/0] portswitch
   [*CE1-GigabitEthernet0/1/0] port link-type trunk
   [*CE1-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   [*CE1-GigabitEthernet0/1/0] quit
   [*CE1] interface gigabitethernet0/2/0
   [*CE1-GigabitEthernet0/2/0] portswitch
   [*CE1-GigabitEthernet0/2/0] port link-type trunk
   [*CE1-GigabitEthernet0/2/0] port trunk allow-pass vlan 10
   [*CE1-GigabitEthernet0/2/0] quit
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] vlan 10
   [*CE2-vlan10] quit
   [*CE2] interface gigabitethernet0/1/0
   [*CE2-GigabitEthernet0/1/0] portswitch
   [*CE2-GigabitEthernet0/1/0] port link-type trunk
   [*CE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   [*CE2-GigabitEthernet0/1/0] quit
   [*CE2] commit
   ```
10. Associate CFM with EVPN DF election.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] cfm enable
    [*CE1] cfm md 1001
    [*CE1-md-1001] ma 4000
    [*CE1-md-1001-ma-4000] map vlan 10
    [*CE1-md-1001-ma-4000] ccm-interval 10
    [*CE1-md-1001-ma-4000] mep mep-id 2000 interface GigabitEthernet0/1/0 outward
    [*CE1-md-1001-ma-4000] mep ccm-send mep-id 2000 enable
    [*CE1-md-1001-ma-4000] remote-mep mep-id 4000
    [*CE1-md-1001-ma-4000] remote-mep ccm-receive mep-id 4000 enable
    [*CE1-md-1001-ma-4000] quit
    [*CE1-md-1001] ma 6000
    [*CE1-md-1001-ma-6000] map vlan 10
    [*CE1-md-1001-ma-6000] ccm-interval 10
    [*CE1-md-1001-ma-6000] mep mep-id 6000 interface GigabitEthernet0/2/0 outward
    [*CE1-md-1001-ma-6000] mep ccm-send mep-id 6000 enable
    [*CE1-md-1001-ma-6000] remote-mep mep-id 8000
    [*CE1-md-1001-ma-6000] remote-mep ccm-receive mep-id 8000 enable
    [*CE1-md-1001-ma-6000] quit
    [*CE1-md-1001] quit
    [*CE1] cfm trigger vlan 10 mac-renew
    [*CE1] commit
    ```
    
    # Configure PE1.
    
    ```
    [~PE1] cfm enable
    [*PE1] cfm md 1001
    [*PE1-md-1001] ma 4000
    [*PE1-md-1001-ma-4000] map evpn vpn-instance evrf1
    [*PE1-md-1001-ma-4000] ccm-interval 10
    [*PE1-md-1001-ma-4000] mep mep-id 4000 interface GigabitEthernet0/1/0.1 vlan 10 outward
    [*PE1-md-1001-ma-4000] mep ccm-send mep-id 4000 enable
    [*PE1-md-1001-ma-4000] remote-mep mep-id 2000
    [*PE1-md-1001-ma-4000] remote-mep ccm-receive mep-id 2000 enable
    [*PE1-md-1001-ma-4000] quit
    [*PE1-md-1001] quit
    [*PE1] oam-mgr
    [*PE1-oam-mgr] oam-bind ingress evpn df interface GigabitEthernet0/1/0.1 egress cfm md 1001 ma 4000
    [*PE1-oam-mgr] quit
    [*PE1] commit
    ```
    
    # Configure PE2.
    
    ```
    [~PE2] cfm enable
    [*PE2] cfm md 1001
    [*PE2-md-1001] ma 6000
    [*PE2-md-1001-ma-6000] map evpn vpn-instance evrf1
    [*PE2-md-1001-ma-6000] ccm-interval 10
    [*PE2-md-1001-ma-6000] mep mep-id 8000 interface GigabitEthernet0/1/0.1 vlan 10 outward
    [*PE2-md-1001-ma-6000] mep ccm-send mep-id 8000 enable
    [*PE2-md-1001-ma-6000] remote-mep mep-id 6000
    [*PE2-md-1001-ma-6000] remote-mep ccm-receive mep-id 6000 enable
    [*PE2-md-1001-ma-6000] quit
    [*PE2-md-1001] quit
    [*PE2] oam-mgr
    [*PE2-oam-mgr] oam-bind ingress evpn df interface GigabitEthernet0/1/0.1 egress cfm md 1001 ma 6000
    [*PE2-oam-mgr] quit
    [*PE2] commit
    ```
11. Verify the configuration.
    
    
    
    # Run the **display evpn vpn-instance name** *vpn-instance-name* **df** **result** command on PE1 and PE2 to check the DF election result. The command output shows that PE1 is the DF and PE2 is a non-DF.
    
    ```
    [~PE1] display evpn vpn-instance name evrf1 df result
    ESI Count: 1
    
    ESI: 0000.1111.2222.1111.1111
    
     IFName GigabitEthernet 0/1/0:
      DF Result    : Primary
    ```
    ```
    [~PE2] display evpn vpn-instance name evrf1 df result
    ESI Count: 1
    
    ESI: 0000.1111.2222.1111.1111
    
     IFName GigabitEthernet 0/1/0:
      DF Result    : Backup
    ```
    
    # Run the **display bgp evpn vpn-instance evrf1 routing-table ad-route 0000.1111.2222.1111.1111:100** command on PE3. The command output shows detailed information about the EVPN A-D routes sent by PE1 and PE2. The route sent by PE1 is selected, and the route sent by PE2 is a backup route.
    
    
    
    ```
    [~PE3] display bgp evpn vpn-instance evrf1 routing-table ad-route 0000.1111.2222.1111.1111:100
    ```
    ```
     BGP local router ID : 4.4.4.4
     Local AS number : 100
     
     EVPN-Instance evrf1:
     Number of A-D Routes: 2
     BGP routing table entry information of 0000.1111.2222.1111.1111:100:
     Route Distinguisher: 100:1
     Remote-Cross route
     Label information (Received/Applied): 48123/NULL
     From: 3.3.3.3 (3.3.3.3) 
     Route Duration: 0d00h21m10s
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 1.1.1.1
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <1.1.1.1 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>, Bypass Label<0 : 0 : 48124>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2
     Originator: 1.1.1.1
     Cluster list: 3.3.3.3
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
     ESI: 0000.1111.2222.1111.1111, Ethernet Tag ID: 100
     Not advertised to any peer yet
     
     BGP routing table entry information of 0000.1111.2222.1111.1111:100:
     Route Distinguisher: 100:2
     Remote-Cross route
     Label information (Received/Applied): 48123/NULL
     From: 3.3.3.3 (3.3.3.3) 
     Route Duration: 0d00h20m53s
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 2.2.2.2
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:0 B:1>, Bypass Label<0 : 0 : 48124>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, backup, pre 255, IGP cost 2, not preferred for L2 ext-community
     Originator: 2.2.2.2
     Cluster list: 3.3.3.3
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
     ESI: 0000.1111.2222.1111.1111, Ethernet Tag ID: 100
     Not advertised to any peer yet
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  cfm enable
  #
  evpn
   vpws-df-election type service-id
   #
   mac-duplication
   #
   esi 0000.1111.2222.1111.1111
    evpn redundancy-mode single-active df-election
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:1
   local-remote frr enable
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 100 remote-service-id 200
  #
  mpls lsr-id 1.1.1.1
  #               
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   esi 0000.1111.2222.1111.1111
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  cfm md 1001
   ma 4000
    map evpn vpn-instance evrf1
    ccm-interval 10
    mep mep-id 4000 interface GigabitEthernet0/1/0.1 vlan 10 outward
    mep ccm-send mep-id 4000 enable
    remote-mep mep-id 2000
    remote-mep ccm-receive mep-id 2000 enable
  #
  oam-mgr
   oam-bind ingress evpn df interface GigabitEthernet0/1/0.1 egress cfm md 1001 ma 4000
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  cfm enable
  #
  evpn
   vpws-df-election type service-id
   #
   mac-duplication
   #
   esi 0000.1111.2222.1111.1111
    evpn redundancy-mode single-active df-election
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:2
   local-remote frr enable
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 100 remote-service-id 200
  #
  mpls lsr-id 2.2.2.2
  #               
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   esi 0000.1111.2222.1111.1111
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  cfm md 1001
   ma 6000
    map evpn vpn-instance evrf1
    ccm-interval 10
    mep mep-id 8000 interface GigabitEthernet0/1/0.1 vlan 10 outward
    mep ccm-send mep-id 8000 enable
    remote-mep mep-id 6000
    remote-mep ccm-receive mep-id 6000 enable
  #
  oam-mgr
   oam-bind ingress evpn df interface GigabitEthernet0/1/0.1 egress cfm md 1001 ma 6000
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  evpn vpn-instance evrf1 vpws
   route-distinguisher 100:3
   remote frr enable
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpl instance 1
   evpn binding vpn-instance evrf1
   local-service-id 200 remote-service-id 100
  #
  mpls lsr-id 4.4.4.4
  #               
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 4.4.4.4
  #
  return
  ```
* RR configuration file
  
  ```
  #
  sysname RR
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls           
   mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
  #
  ospf 1
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan batch 10
  #
  vlan 10
  #
  cfm enable
  cfm trigger vlan 10 mac-renew
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10  
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10 
  #
  cfm md 1001
   ma 4000
    map vlan 10
    ccm-interval 10
    mep mep-id 2000 interface GigabitEthernet0/1/0 outward
    mep ccm-send mep-id 2000 enable
    remote-mep mep-id 4000
    remote-mep ccm-receive mep-id 4000 enable
   ma 6000
    map vlan 10
    ccm-interval 10
    mep mep-id 6000 interface GigabitEthernet0/2/0 outward
    mep ccm-send mep-id 6000 enable
    remote-mep mep-id 8000
    remote-mep ccm-receive mep-id 8000 enable
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan batch 10
  #
  vlan 10
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```