Example for Configuring Dual-Homing Active-Active EVPN VPWS over MPLS (Eth-Trunk Sub-interface Access)
======================================================================================================

This section provides an example for configuring EVPN VPWS services on a dual-homing active-active network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001964722825__fig_dc_vrp_evpn_cfg_015301), PE1, PE2, the RR, and PE3 belong to the same AS. They need to communicate with each other using OSPF, and MPLS tunnels need to be deployed to carry EVPN VPWS services.

**Figure 1** Configuring dual-homing active-active EVPN VPWS over MPLS (Eth-Trunk sub-interface access)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_evpn_cfg_015301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the backbone network to allow PEs to communicate with each other and with the RR.
2. Configure basic MPLS functions and enable MPLS LDP to establish MPLS LSPs on the backbone network.
3. Configure EVPN VPWS and EVPL instances on each PE and bind an access-side sub-interface to the EVPL instance.
4. Establish BGP EVPN peer relationships between PEs and the RR. On the RR, configure the PEs as RR clients.
5. Configure a redundancy mode on a per-ESI basis on PEs.
6. Configure FRR on PEs.
7. Configure CEs to access PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name (evrf1)
* EVPN instance RDs (100:1, 100:2, and 100:3) and RTs (1:1)

#### Procedure

1. Configure interface addresses on the RR and PEs according to [Figure 1](#EN-US_TASK_0000001964722825__fig_dc_vrp_evpn_cfg_015301). For detailed configurations, see Configuration Files.
2. Configure an IGP on the backbone network to allow PEs to communicate with each other and with the RR. OSPF is used as the IGP in this example.
   
   
   
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
4. Configure EVPN VPWS and EVPL instances on each PE and bind an access-side sub-interface to the EVPL instance.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] evpl instance 1
   ```
   ```
   [*PE1-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-evpl1] local-service-id 100 remote-service-id 200
   ```
   ```
   [*PE1-evpl1] quit
   ```
   ```
   [*PE1] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE1] e-trunk 1
   ```
   ```
   [*PE1-e-trunk-1] priority 10
   ```
   ```
   [*PE1-e-trunk-1] security-key cipher YsHsjx_202206
   ```
   ```
   [*PE1-e-trunk-1] peer-address 2.2.2.2 source-address 1.1.1.1  
   ```
   ```
   [*PE1-e-trunk-1] quit
   ```
   ```
   [*PE1] interface eth-trunk 10
   ```
   ```
   [*PE1-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*PE1-Eth-Trunk10] e-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk10] quit
   ```
   ```
   [*PE1] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE1-Eth-Trunk1.1] encapsulation dot1q vid 10  
   ```
   ```
   [*PE1-Eth-Trunk1.1] evpl instance 1
   ```
   ```
   [*PE1-Eth-Trunk1.1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet 0/1/0] eth-trunk 10
   ```
   ```
   [*PE1-GigabitEthernet 0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] route-distinguisher 100:2
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] evpl instance 1
   ```
   ```
   [*PE2-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-evpl1] local-service-id 100 remote-service-id 200
   ```
   ```
   [*PE2-evpl1] quit
   ```
   ```
   [*PE2] lacp e-trunk system-id 00e0-fc00-0000
   ```
   ```
   [*PE2] e-trunk 1
   ```
   ```
   [*PE2-e-trunk-1] priority 10
   ```
   ```
   [*PE2-e-trunk-1] security-key cipher YsHsjx_202206
   ```
   ```
   [*PE2-e-trunk-1] peer-address 1.1.1.1 source-address 2.2.2.2 
   ```
   ```
   [*PE2-e-trunk-1] quit
   ```
   ```
   [*PE2] interface eth-trunk 10
   ```
   ```
   [*PE2-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*PE2-Eth-Trunk10] e-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] interface eth-trunk 10.1 mode l2
   ```
   ```
   [*PE2-Eth-Trunk1.1] encapsulation dot1q vid 10  
   ```
   ```
   [*PE2-Eth-Trunk1.1] evpl instance 1
   ```
   ```
   [*PE2-Eth-Trunk1.1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet 0/1/0] eth-trunk 10
   ```
   ```
   [*PE2-GigabitEthernet 0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 vpws
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] route-distinguisher 100:3
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE3-vpws-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] evpl instance 1
   ```
   ```
   [*PE3-evpl1] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE3-evpl1] local-service-id 200 remote-service-id 100
   ```
   ```
   [*PE3-evpl1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0.1 mode l2
   ```
   ```
   [*PE3-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 1
   ```
   ```
   [*PE3-GigabitEthernet 0/2/0.1] evpl instance 1
   ```
   ```
   [*PE3-GigabitEthernet 0/2/0.1] quit
   ```
   ```
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
6. Establish BGP EVPN peer relationships between PEs and the RR. On the RR, configure the PEs as RR clients.
   
   
   
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
   [*PE3-bgp-af-evpn] undo policy vpn-target
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
   
   After the configuration is complete, run the **display bgp evpn peer** command on the RR. The command output shows that BGP peer relationships are in the **Established** state, indicating that BGP peer relationships have been successfully established between the RR and PEs.
   
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
7. Configure a redundancy mode on a per-ESI basis on PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn
   ```
   ```
   [*PE1-evpn] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE1-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode all-active
   ```
   ```
   [*PE1-evpn-esi-0001.0002.0003.0004.0005] quit
   ```
   ```
   [*PE1-evpn] quit
   ```
   ```
   [*PE1] interface eth-trunk 10
   ```
   ```
   [*PE1-Eth-Trunk10] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE1-Eth-Trunk10] e-trunk mode force-master
   ```
   ```
   [*PE1-Eth-Trunk10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn
   ```
   ```
   [*PE2-evpn] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE2-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode all-active
   ```
   ```
   [*PE2-evpn-esi-0001.0002.0003.0004.0005] quit
   ```
   ```
   [*PE2-evpn] quit
   ```
   ```
   [*PE2] interface eth-trunk 10
   ```
   ```
   [*PE2-Eth-Trunk10] esi 0001.0002.0003.0004.0005
   ```
   ```
   [*PE2-Eth-Trunk10] e-trunk mode force-master
   ```
   ```
   [*PE2-Eth-Trunk10] quit
   ```
   ```
   [*PE2] commit
   ```
8. Configure FRR on PEs.
   
   
   
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
9. Configure CEs to access PEs.
   
   
   
   # Configure CE1 and enable intra-VLAN trunk load balancing.
   
   ```
   <CE1> system-view
   [~CE1] vlan 10
   [*CE1-vlan10] trunk multicast load-balance enable
   [*CE1-vlan10] quit 
   [*CE1] interface Eth-Trunk10
   [*CE1-Eth-Trunk10] portswitch
   [*CE1-Eth-Trunk10] mode lacp-static
   [*CE1-Eth-Trunk10] undo shutdown
   [*CE1-Eth-Trunk10] port link-type trunk
   [*CE1-Eth-Trunk10] port trunk allow-pass vlan 10
   [*CE1-Eth-Trunk10] quit
   [*CE1] interface gigabitethernet 0/1/0
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   [*CE1-GigabitEthernet0/1/0] eth-trunk 10
   [*CE1-GigabitEthernet0/1/0] quit
   [*CE1] interface gigabitethernet 0/2/0
   [*CE1-GigabitEthernet0/2/0] undo shutdown
   [*CE1-GigabitEthernet0/2/0] eth-trunk 10
   [*CE1-GigabitEthernet0/2/0] quit
   [*CE1] commit
   ```
   
   
   
   # Configure CE2.
   
   ```
   <CE2> system-view
   [~CE2] vlan 10 
   [*CE2-vlan10] quit           
   [*CE2] interface gigabitethernet 0/1/0
   [*CE2-GigabitEthernet0/1/0] portswitch
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   [*CE2-GigabitEthernet0/1/0] port link-type trunk
   [*CE2-GigabitEthernet0/1/0] port trunk allow-pass vlan 10
   [*CE2-GigabitEthernet0/1/0] commit
   [~CE2-GigabitEthernet0/1/0] quit
   ```
   
   After the configuration is complete, the corresponding Eth-Trunk should be up. Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on PE1 and PE2 to check the Eth-Trunk status.
   
   Command output on PE1:
   
   ```
   [~PE1] display eth-trunk 10                              
   Eth-Trunk10's state information is:    
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 10                      WorkingMode: STATIC
   Preempt Delay: Disabled         Hash arithmetic: According to flow
   System Priority: 32768          System ID: 00e0-fc00-0000(Local)
   Least Active-linknumber: 1      Max Active-linknumber: 32
   Operate status: up              Number Of Up Ports In Trunk: 1
   Timeout Period: Slow
   PortKeyMode: Auto                  
   ------------------------------------------------------------------------------------
   ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
   GigabitEthernet0/1/0(hr)   Selected 100M     32768   1      2593    10111100  1
   
   Partner:
   ------------------------------------------------------------------------------------
   ActorPortName              SysPri   SystemID        PortPri PortNo PortKey PortState
   GigabitEthernet0/1/0       32768    38ba-8c91-2005  32768   1      2593    10111100
   --------------------------------------------------------------------------------        
   ```
   
   Command output on PE2:
   
   ```
   [~PE2] display eth-trunk 10
   Eth-Trunk10's state information is:    
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 10                      WorkingMode: STATIC
   Preempt Delay: Disabled         Hash arithmetic: According to flow
   System Priority: 32768          System ID: 00e0-fc00-0000(Local)
   Least Active-linknumber: 1      Max Active-linknumber: 32
   Operate status: up              Number Of Up Ports In Trunk: 1
   Timeout Period: Slow
   PortKeyMode: Auto                  
   ------------------------------------------------------------------------------------
   ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
   GigabitEthernet0/1/0(hr)   Selected 100M     32768   1      2593    10111100  1
   
   Partner:
   ------------------------------------------------------------------------------------
   ActorPortName              SysPri   SystemID        PortPri PortNo PortKey PortState
   GigabitEthernet0/1/0       32768    38ba-8c91-2005  32768   1      2593    10111100
   --------------------------------------------------------------------------------        
   ```
   
   The command output shows that PE1 and PE2 are in the active-active state for Eth-Trunk 10.
10. Verify the configuration.
    
    
    
    Run the **display bgp evpn all routing-table ad-route** command on PE3 to check EVPN Ethernet A-D route information.
    
    ```
    [~PE3] display bgp evpn all routing-table ad-route
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 4.4.4.4
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of A-D Routes: 3
     Route Distinguisher: 100:1
           Network(ESI/EthTagId)                                  NextHop
     *>i   0001.0002.0003.0004.0005:100                           1.1.1.1
     Route Distinguisher: 100:2
           Network(ESI/EthTagId)                                  NextHop
     *>i   0001.0002.0003.0004.0005:100                           2.2.2.2
     Route Distinguisher: 100:3
           Network(ESI/EthTagId)                                  NextHop
     *>    0000.0000.0000.0000.0000:200                           127.0.0.1
     Route Distinguisher: 1.1.1.1:0
           Network(ESI/EthTagId)                                  NextHop
     *>i   0001.0002.0003.0004.0005:4294967295                    1.1.1.1
     Route Distinguisher: 2.2.2.2:0
           Network(ESI/EthTagId)                                  NextHop
     *>i   0001.0002.0003.0004.0005:4294967295                    2.2.2.2
    
    
     EVPN-Instance evrf1:
     Number of A-D Routes: 3
           Network(ESI/EthTagId)                                  NextHop
     *>    0000.0000.0000.0000.0000:200                           127.0.0.1
     *>i   0001.0002.0003.0004.0005:100                           1.1.1.1
     * i                                                          2.2.2.2
     *>i   0001.0002.0003.0004.0005:4294967295                    1.1.1.1
     * i                                                          2.2.2.2
    ```
    
    Run the **display bgp evpn all routing-table ad-route 0001.0002.0003.0004.0005:100** command on PE3. The command output shows detailed information about the EVPN Ethernet A-D routes sent by PE1 and PE2 and label information about the bypass tunnel after FRR is configured.
    
    ```
    [~PE3] display bgp evpn all routing-table ad-route 0001.0002.0003.0004.0005:100
    ```
    ```
     BGP local router ID : 4.4.4.4
     Local AS number : 100
     Total routes of Route Distinguisher(100:1): 1
     BGP routing table entry information of 0001.0002.0003.0004.0005:100:
     Label information (Received/Applied): 48123/NULL
     From: 3.3.3.3 (3.3.3.3) 
     Route Duration: 0d00h21m09s
     Relay IP Nexthop: 10.3.1.1
     Relay IP Out-Interface:GigabitEthernet0/1/0
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 1.1.1.1
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <1.1.1.1 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>, Bypass Label<0 : 0 : 48124>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2
     Originator: 1.1.1.1
     Cluster list: 3.3.3.3
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 100
     Not advertised to any peer yet
     
     Total routes of Route Distinguisher(100:2): 1
     BGP routing table entry information of 0001.0002.0003.0004.0005:100:
     Label information (Received/Applied): 48123/NULL
     From: 3.3.3.3 (3.3.3.3) 
     Route Duration: 0d00h20m52s
     Relay IP Nexthop: 10.3.1.1
     Relay IP Out-Interface:GigabitEthernet0/1/0
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 2.2.2.2
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>, Bypass Label<0 : 0 : 48124>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 2
     Originator: 2.2.2.2
     Cluster list: 3.3.3.3
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 100
     Not advertised to any peer yet
     
        
    
     EVPN-Instance evrf1:
     Number of A-D Routes: 2
     BGP routing table entry information of 0001.0002.0003.0004.0005:100:
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
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 100
     Not advertised to any peer yet
     
     BGP routing table entry information of 0001.0002.0003.0004.0005:100:
     Route Distinguisher: 100:2
     Remote-Cross route
     Label information (Received/Applied): 48123/NULL
     From: 3.3.3.3 (3.3.3.3) 
     Route Duration: 0d00h20m53s
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 2.2.2.2
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, EVPN L2 Attributes <MTU:1500 C:0 P:1 B:0>, Bypass Label<0 : 0 : 48124>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, pre 255, IGP cost 2, not preferred for router ID
     Originator: 2.2.2.2
     Cluster list: 3.3.3.3
     Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
     ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 100
     Not advertised to any peer yet
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  lacp e-trunk system-id 00e0-fc00-0000
  #
  evpn
   #  
   mac-duplication 
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode all-active
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
  e-trunk 1
   priority 10
   peer-address 2.2.2.2 source-address 1.1.1.1
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%#
  #
  mpls lsr-id 1.1.1.1
  #               
  mpls
  #
  mpls ldp
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  # 
  interface GigabitEthernet0/1/0  
   undo shutdown
   eth-trunk 10
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
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  lacp e-trunk system-id 00e0-fc00-0000
  #
  evpn
   #  
   mac-duplication 
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode all-active
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
  e-trunk 1
   priority 10
   peer-address 1.1.1.1 source-address 2.2.2.2
   security-key cipher %^%#!8C!"bAoc~O}UW2)%$HP4%.G9179.;&Yr[GmV.PN%^%#
  #               
  mpls lsr-id 2.2.2.2
  #               
  mpls
  #
  mpls ldp
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   evpl instance 1
  # 
  interface GigabitEthernet0/1/0  
   undo shutdown
   eth-trunk 10
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
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
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
    undo policy vpn-target
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
  vlan 10
   trunk multicast load-balance enable
  #
  interface Eth-Trunk10
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10
   mode lacp-static
  #   
  interface GigabitEthernet0/1/0 
   undo shutdown
   eth-trunk 10
  #                    
  interface GigabitEthernet0/2/0 
   undo shutdown
   eth-trunk 10
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  vlan 10
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```