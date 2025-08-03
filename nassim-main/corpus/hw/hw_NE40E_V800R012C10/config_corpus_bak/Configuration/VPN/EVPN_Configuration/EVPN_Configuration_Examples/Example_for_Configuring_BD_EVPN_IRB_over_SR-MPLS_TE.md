Example for Configuring BD EVPN IRB over SR-MPLS TE
===================================================

This section provides an example for configuring BD EVPN IRB over SR-MPLS TE to transmit services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370670__fig117545811214), to allow different sites to communicate over the backbone network, configure EVPN and VPN to transmit Layer 2 and Layer 3 services. If sites belong to the same subnet, create an EVPN instance on each PE to store EVPN routes and implement Layer 2 forwarding based on MAC addresses. If sites belong to different subnets, create a VPN instance on each PE to store VPN routes. In this situation, Layer 2 traffic is terminated, and Layer 3 traffic is forwarded through a Layer 3 gateway. In this example, an SR-MPLS TE tunnel needs to be used to transmit services between the PEs.

**Figure 1** Configuring BD EVPN IRB over SR-MPLS TE![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, and sub-interface1.1 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/1/0.1, respectively.


  
![](figure/en-us_image_0000001182556270.png "Click to enlarge")

#### Configuration Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using each PE's local loopback interface address as its EVPN source address is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP for PE1, PE2, and the P to communicate.
2. Configure an SR-MPLS TE tunnel on the backbone network.
3. Configure an EVPN instance and a VPN instance on each PE.
4. Configure a source address on each PE.
5. Configure Layer 2 Ethernet sub-interfaces used by PEs to connect to CEs.
6. Bind the VBDIF interface to a VPN instance on each PE.
7. Configure and apply a tunnel policy to enable EVPN service recursion to the SR-MPLS TE tunnel.
8. Establish a BGP EVPN peer relationship between PEs.
9. Configure CEs and PEs to communicate.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance named evrf1 and VPN instance named vpn1
* RDs (100:1 and 200:1) and RT (1:1) of the EVPN instance evrf1 on PE1 and PE2 vpn1 RDs (100:2 and 200:2) and RT 2:2

#### Procedure

1. Configure addresses for interfaces connecting the PEs and P according to [Example for Configuring BD EVPN IRB over SR-MPLS TE](dc_vrp_dci_cfg_0035.html).
   
   
   
   # Configure PE1.
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] ip address 2.2.2.2 32
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] interface gigabitethernet0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   <~HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] ip address 3.3.3.3 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
2. Configure an IGP for PE1, PE2, and the P to communicate. IS-IS is used as the IGP in this example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-2
   ```
   ```
   [*PE1-isis-1] network-entity 00.1111.1111.1111.00
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] isis enable 1
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1
   ```
   ```
   [*P-isis-1] is-level level-2
   ```
   ```
   [*P-isis-1] network-entity 00.1111.1111.2222.00
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] isis enable 1
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-2
   ```
   ```
   [*PE2-isis-1] network-entity 00.1111.1111.3333.00
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] isis enable 1
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configurations, run the **display isis peer** command to check whether an IS-IS neighbor relationship has been established between PE1 and the P and between PE2 and the P. If the **Up** state is displayed in the command output, the neighbor relationship has been successfully established. Run the **display ip routing-table** command. The command output shows that the PEs have learned the route to each other's Loopback1 interface.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   1111.1111.2222  GE0/2/0            1111.1111.2222.01  Up   8s       L2       64 
   
   Total Peer(s): 1
   ```
   ```
   [~PE1] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 11       Routes : 11        
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Direct  0    0             D   127.0.0.1       LoopBack1
           2.2.2.2/32  ISIS-L2 15   10            D   10.1.1.2        GigabitEthernet0/2/0
           3.3.3.3/32  ISIS-L2 15   20            D   10.1.1.2        GigabitEthernet0/2/0
          10.1.1.0/24  Direct  0    0             D   10.1.1.1        GigabitEthernet0/2/0
          10.1.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
        10.1.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
          10.2.1.0/24  ISIS-L2 15   20            D   10.1.1.2        GigabitEthernet0/2/0
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   ```
3. Configure an SR-MPLS TE tunnel on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls te
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] traffic-eng level-2
   ```
   ```
   [*PE1-isis-1] segment-routing mpls
   ```
   ```
   [*PE1-isis-1] segment-routing global-block 153616 153800
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. This example is for reference only. In this example, the adjacency label is a dynamic one.
   
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] isis prefix-sid absolute 153700
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] explicit-path pe1tope2
   ```
   ```
   [*PE1-explicit-path-pe1tope2] next sid label 48121 type adjacency
   ```
   ```
   [*PE1-explicit-path-pe1tope2] next sid label 48120 type adjacency
   ```
   ```
   [*PE1-explicit-path-pe1tope2] quit
   ```
   ```
   [*PE1] interface tunnel1
   ```
   ```
   [*PE1-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*PE1-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*PE1-Tunnel1] destination 3.3.3.3
   ```
   ```
   [*PE1-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*PE1-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE1-Tunnel1] mpls te path explicit-path pe1tope2
   ```
   ```
   [*PE1-Tunnel1] mpls te reserved-for-binding
   ```
   ```
   [*PE1-Tunnel1] quit
   ```
   ```
   [*PE1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding steps, the [**next sid label**](cmdqueryname=next+sid+label) command uses the adjacency labels of PE1 â> P and P â> PE2, which are dynamically generated through IS-IS. Before the configuration, you can run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command to query the label value. For example:
   
   ```
   [~PE1] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------
   48121     GE0/2/0           10.1.1.2         ISIS-V4     ---       1500      _public_      
   ```
   
   # Configure the P.
   
   ```
   [~P] mpls lsr-id 2.2.2.2
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls]  mpls te
   ```
   ```
   [*P-mpls] quit
   ```
   ```
   [*P] segment-routing
   ```
   ```
   [*P-segment-routing] quit
   ```
   ```
   [*P] isis 1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] traffic-eng level-2
   ```
   ```
   [*P-isis-1] segment-routing mpls
   ```
   ```
   [*P-isis-1] segment-routing global-block 153616 153800
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. This example is for reference only.
   
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] isis prefix-sid absolute 153710
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the configuration is complete, run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command to query the automatically generated adjacency label. For example:
   
   ```
   [~P] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------
   48221     GE0/1/0           10.1.1.1         ISIS-V4     ---       1500      _public_ 
   48120     GE0/2/0           10.2.1.2         ISIS-V4     ---       1500      _public_      
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.3
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls te
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] traffic-eng level-2
   ```
   ```
   [*PE2-isis-1] segment-routing mpls
   ```
   ```
   [*PE2-isis-1] segment-routing global-block 153616 153800
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. This example is for reference only. In this example, the adjacency label is a dynamic one.
   
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] isis prefix-sid absolute 153720
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] explicit-path pe2tope1
   ```
   ```
   [*PE2-explicit-path-pe2tope1] next sid label 48220 type adjacency
   ```
   ```
   [*PE2-explicit-path-pe2tope1] next sid label 48221 type adjacency
   ```
   ```
   [*PE2-explicit-path-pe2tope1] quit
   ```
   ```
   [*PE2] interface tunnel1
   ```
   ```
   [*PE2-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*PE2-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*PE2-Tunnel1] destination 1.1.1.1
   ```
   ```
   [*PE2-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*PE2-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE2-Tunnel1] mpls te path explicit-path pe2tope1
   ```
   ```
   [*PE2-Tunnel1] mpls te reserved-for-binding
   ```
   ```
   [*PE2-Tunnel1] quit
   ```
   ```
   [*PE2] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding steps, the [**next sid label**](cmdqueryname=next+sid+label) command uses the adjacency labels of PE2 â> P and P â> PE1, which are dynamically generated through IS-IS. Before the configuration, you can run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command to query the label value. For example:
   
   ```
   [~PE1] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------
   48220     GE0/2/0           10.2.1.1         ISIS-V4     ---       1500      _public_      
   ```
   
   After completing the configurations, run the **display mpls te tunnel-interface** command. The command output shows that the tunnel status is **Up**.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls te tunnel-interface
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP
       Traffic Switch      : - 
       Session ID          : 1
       Ingress LSR ID      : 1.1.1.1               Egress LSR ID: 3.3.3.3
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : Segment-Routing
       FTid                : 1
       Tie-Breaking Policy : None                  Metric Type  : None
       Bfd Cap             : None                  
       Reopt               : Disabled              Reopt Freq   : -              
       Auto BW             : Disabled              Threshold    : - 
       Current Collected BW: -                     Auto BW Freq : -
       Min BW              : -                     Max BW       : -
       Offload             : Disabled              Offload Freq : - 
       Low Value           : -                     High Value   : - 
       Readjust Value      : - 
       Offload Explicit Path Name: -
       Tunnel Group        : Primary
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0
       Primary Tunnel      : -                     Pri Tunn Sum : -
       Backup Tunnel       : -
       Group Status        : Up                    Oam Status   : None
       IPTN InLabel        : -                     Tunnel BFD Status : -
       BackUp LSP Type     : None                  BestEffort   : -
       Secondary HopLimit  : -
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: -
       Secondary Affinity Prop/Mask: 0x0/0x0
       BestEffort Affinity Prop/Mask: -  
       IsConfigLspConstraint: -
       Hot-Standby Revertive Mode:  Revertive
       Hot-Standby Overlap-path:  Disabled
       Hot-Standby Switch State:  CLEAR
       Bit Error Detection:  Disabled
       Bit Error Detection Switch Threshold:  -
       Bit Error Detection Resume Threshold:  -
       Ip-Prefix Name    : -
       P2p-Template Name : -
       PCE Delegate      : No                    LSP Control Status : Local control
   
       Path Verification : No
       Entropy Label     : -
       Associated Tunnel Group ID: -             Associated Tunnel Group Type: -
       Auto BW Remain Time   : -                 Reopt Remain Time     : - 
       Segment-Routing Remote Label   : -
       Binding Sid       : -                     Reverse Binding Sid : - 
       FRR Attr Source   : -                     Is FRR degrade down : No
       Color             : - 
   
       Primary LSP ID      : 1.1.1.1:2
       LSP State           : UP                    LSP Type     : Primary
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       SidProtectType      : - 
       Configured Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Actual Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Explicit Path Name  : pe1tope2                         Hop Limit: -
       Record Route        : -                            Record Label : Disabled
       Route Pinning       : -
       FRR Flag            : -
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : -
       Reroute Flag        : -
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
   ```
4. Configure an EVPN instance and a VPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] evpn mpls routing-enable
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:2
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 evpn
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] evpn mpls routing-enable
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] bridge-domain 10
   ```
   ```
   [*PE2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-bd10] quit
   ```
   ```
   [*PE2] commit
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
   [~PE2] evpn source-address 3.3.3.3
   ```
   ```
   [*PE2] commit
   ```
6. Configure Layer 2 Ethernet sub-interfaces used by PEs to connect to CEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface GigabitEthernet 0/1/0
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] esi 0011.1111.1111.1111.1111
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/1/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet 0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-GigabitEthernet 0/1/0.1] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet 0/1/0.1] bridge-domain 10
   ```
   ```
   [*PE1-GigabitEthernet 0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface GigabitEthernet 0/1/0
   ```
   ```
   [*PE2-Gigabitethernet0/1/0] esi 0011.1111.1111.1111.2222
   ```
   ```
   [*PE2-Gigabitethernet0/1/0] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/1/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet 0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE2-GigabitEthernet 0/1/0.1] rewrite pop single
   ```
   ```
   [*PE2-GigabitEthernet 0/1/0.1] bridge-domain 10
   ```
   ```
   [*PE2-GigabitEthernet 0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
7. Bind the VBDIF interface to a VPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface Vbdif10
   ```
   ```
   [*PE1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-Vbdif10] ip address 192.168.1.1 255.255.255.0
   ```
   ```
   [*PE1-Vbdif10] arp collect host enable
   ```
   ```
   [*PE1-Vbdif10] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface Vbdif10
   ```
   ```
   [*PE2-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-Vbdif10] ip address 192.168.2.1 255.255.255.0
   ```
   ```
   [*PE2-Vbdif10] arp collect host enable
   ```
   ```
   [*PE2-Vbdif10] quit
   ```
   ```
   [*PE2] commit
   ```
8. Configure and apply a tunnel policy to enable EVPN service recursion to the SR-MPLS TE tunnel.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy srte
   ```
   ```
   [*PE1-tunnel-policy-srte] tunnel binding destination 3.3.3.3 te Tunnel1
   ```
   ```
   [*PE1-tunnel-policy-srte] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] tnl-policy srte
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] tnl-policy srte evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] tunnel-policy srte
   ```
   ```
   [*PE2-tunnel-policy-srte] tunnel binding destination 1.1.1.1 te Tunnel1
   ```
   ```
   [*PE2-tunnel-policy-srte] quit
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] tnl-policy srte
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] tnl-policy srte evpn
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] commit
   ```
9. Establish a BGP EVPN peer relationship between PEs.
   
   
   
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
   [*PE1-bgp-af-evpn] peer 3.3.3.3 advertise irb
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpn1] quit
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
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 1.1.1.1 advertise irb
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] import-route direct
   ```
   ```
   [*PE2-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE2-bgp-vpn1] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configurations, run the **display bgp evpn peer** command. The command output shows that the BGP peer relationships are in the **Established** state, indicating that BGP peer relationships have been successfully established between the PEs. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   ```
   ```
    
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.3         4         100        9        9     0 00:00:02 Established        5
   ```
10. Configure CEs and PEs to communicate.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] interface GigabitEthernet 0/1/0.1 mode l2
    ```
    ```
    [*CE1-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
    ```
    ```
    [*CE1-GigabitEthernet0/1/0.1] rewrite pop single
    ```
    ```
    [*CE1-GigabitEthernet0/1/0.1] quit
    ```
    ```
    [*CE1] commit
    ```
    
    # Configure CE2.
    
    ```
    [~CE2] interface GigabitEthernet 0/1/0.1 mode l2
    ```
    ```
    [*CE2-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
    ```
    ```
    [*CE2-GigabitEthernet0/1/0.1] rewrite pop single
    ```
    ```
    [*CE2-GigabitEthernet0/1/0.1] quit
    ```
    ```
    [*CE2] commit
    ```
11. Verify the configuration.
    
    
    
    Run the **display bgp evpn all routing-table** command on each PE. The command output shows EVPN routes sent from the remote PE. The following example uses the command output on PE1.
    
    ```
    [~PE1] display bgp evpn all routing-table
    
     Local AS number : 100
    
     BGP Local router ID is 1.1.1.1
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of A-D Routes: 4
     Route Distinguisher: 100:1
           Network(ESI/EthTagId)                                  NextHop
     *>    0011.1111.1111.1111.1111:0                             127.0.0.1
     Route Distinguisher: 200:1
           Network(ESI/EthTagId)                                  NextHop
     *>i   0011.1111.1111.1111.2222:0                             3.3.3.3
     Route Distinguisher: 1.1.1.1:0
           Network(ESI/EthTagId)                                  NextHop
     *>    0011.1111.1111.1111.1111:4294967295                    127.0.0.1
     Route Distinguisher: 3.3.3.3:0
           Network(ESI/EthTagId)                                  NextHop
     *>i   0011.1111.1111.1111.2222:4294967295                    3.3.3.3
        
    
     EVPN-Instance evrf1:
     Number of A-D Routes: 3
           Network(ESI/EthTagId)                                  NextHop
     *>    0011.1111.1111.1111.1111:0                             127.0.0.1
     *>i   0011.1111.1111.1111.2222:0                             3.3.3.3
     *>i   0011.1111.1111.1111.2222:4294967295                    3.3.3.3
     
     EVPN address family:
     Number of Mac Routes: 2
     Route Distinguisher: 100:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>    0:48:00e0-fc12-7890:0:0.0.0.0                          0.0.0.0
     Route Distinguisher: 200:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:00e0-fc12-3456:0:0.0.0.0                          3.3.3.3
        
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 2
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:00e0-fc12-3456:0:0.0.0.0                          3.3.3.3
     *>    0:48:00e0-fc12-7890:0:0.0.0.0                          0.0.0.0
     
     EVPN address family:
     Number of Inclusive Multicast Routes: 2
     Route Distinguisher: 100:1
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>    0:32:1.1.1.1                                           127.0.0.1
     Route Distinguisher: 200:1
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>i   0:32:3.3.3.3                                           3.3.3.3
        
    
     EVPN-Instance evrf1:
     Number of Inclusive Multicast Routes: 2
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>    0:32:1.1.1.1                                           127.0.0.1
     *>i   0:32:3.3.3.3                                           3.3.3.3
     
     EVPN address family:
     Number of ES Routes: 2
     Route Distinguisher: 1.1.1.1:0
           Network(ESI)                                           NextHop
     *>    0011.1111.1111.1111.1111                               127.0.0.1
     Route Distinguisher: 3.3.3.3:0
           Network(ESI)                                           NextHop
     *>i   0011.1111.1111.1111.2222                               3.3.3.3
        
    
     EVPN-Instance evrf1:
     Number of ES Routes: 1
           Network(ESI)                                           NextHop
     *>    0011.1111.1111.1111.1111                               127.0.0.1
     
     EVPN address family:
     Number of Ip Prefix Routes: 2
     Route Distinguisher: 100:2
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
     *>    0:192.168.1.0:24                                       0.0.0.0
     Route Distinguisher: 200:2
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
     *>i   0:192.168.2.0:24                                       3.3.3.3
    ```
    
    Run the **display bgp evpn all routing-table mac-route 0:48:00e0-fc12-3456:0:0.0.0.0** or **display bgp evpn all routing-table prefix-route 0:192.168.2.0:24** command on PE1 to check detailed information about MAC routes or IP prefix routes. The command output shows the name of the tunnel interfaces to which the routes recurse.
    
    ```
    [~PE1] display bgp evpn all routing-table mac-route 0:48:00e0-fc12-3456:0:0.0.0.0
    
     BGP local router ID : 1.1.1.1
     Local AS number : 100
     Total routes of Route Distinguisher(200:1): 1
     BGP routing table entry information of 0:48:00e0-fc12-3456:0:0.0.0.0:
     Label information (Received/Applied): 54011 48182/NULL
     From: 3.3.3.3 (10.2.1.2) 
     Route Duration: 0d20h42m36s
     Relay IP Nexthop: 10.1.1.2
     Relay IP Out-Interface: GigabitEthernet0/2/0
     Relay Tunnel Out-Interface: GigabitEthernet0/2/0
     Original nexthop: 3.3.3.3
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, Mac Mobility <flag:1 seq:0 res:0>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20
     Route Type: 2 (MAC Advertisement Route)
     Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc12-3456/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000
     Not advertised to any peer yet
     
        
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 1
     BGP routing table entry information of 0:48:00e0-fc12-3456:0:0.0.0.0:
     Route Distinguisher: 200:1
     Remote-Cross route
     Label information (Received/Applied): 54011 48182/NULL
     From: 3.3.3.3 (10.2.1.2) 
     Route Duration: 0d20h42m36s
     Relay Tunnel Out-Interface: Tunnel1
     Original nexthop: 3.3.3.3
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, Mac Mobility <flag:1 seq:0 res:0>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255
     Route Type: 2 (MAC Advertisement Route)
     Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc12-3456/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000
     Not advertised to any peer yet
    ```
    ```
    [~PE1] display bgp evpn all routing-table prefix-route 0:192.168.2.0:24
    
     BGP local router ID : 1.1.1.1
     Local AS number : 100
     Total routes of Route Distinguisher(200:2): 1
     BGP routing table entry information of 0:192.168.2.0:24:
     Label information (Received/Applied): 48185/NULL
     From: 3.3.3.3 (10.2.1.2) 
     Route Duration: 0d20h38m31s
     Relay IP Nexthop: 10.1.1.2
     Relay IP Out-Interface: GigabitEthernet0/2/0
     Relay Tunnel Out-Interface: GigabitEthernet0/2/0
     Original nexthop: 3.3.3.3
     Qos information : 0x0
     Ext-Community: RT <2 : 2>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20
     Route Type: 5 (Ip Prefix Route)
     Ethernet Tag ID: 0, IP Prefix/Len: 192.168.2.0/24, ESI: 0000.0000.0000.0000.0000, GW IP Address: 0.0.0.0
     Not advertised to any peer yet
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   tnl-policy srte
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy srte evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  explicit-path pe1tope2
   next sid label 48121 type adjacency index 1
   next sid label 48120 type adjacency index 2
  #
  segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.1111.1111.1111.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 153616 153800
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 192.168.1.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   esi 0011.1111.1111.1111.1111
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 153700 
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te reserved-for-binding
   mpls te tunnel-id 1
   mpls te path explicit-path pe1tope2  
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
  #
  tunnel-policy srte
   tunnel binding destination 3.3.3.3 te Tunnel1
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
  #
  segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.1111.1111.2222.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 153616 153800
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   isis enable 1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 153710 
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   tnl-policy srte
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy srte evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  explicit-path pe2tope1
   next sid label 48220 type adjacency index 1
   next sid label 48221 type adjacency index 2
  #
  segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.1111.1111.3333.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 153616 153800
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 192.168.2.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   esi 0011.1111.1111.1111.2222
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 153720 
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol segment-routing
   mpls te reserved-for-binding
   mpls te tunnel-id 1
   mpls te path explicit-path pe2tope1  
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
  #
  tunnel-policy srte
   tunnel binding destination 1.1.1.1 te Tunnel1
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
  #
  return
  ```