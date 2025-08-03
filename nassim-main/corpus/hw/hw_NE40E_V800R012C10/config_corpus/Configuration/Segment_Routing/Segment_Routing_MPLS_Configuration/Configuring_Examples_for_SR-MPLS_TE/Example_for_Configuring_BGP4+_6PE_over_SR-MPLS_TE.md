Example for Configuring BGP4+ 6PE over SR-MPLS TE
=================================================

This section provides an example for configuring an SR-MPLS TE tunnel to carry BGP4+ 6PE services.

#### Networking Requirements

BGP4+ 6PE over SR-MPLS TE enables non-contiguous IPv6 networks to communicate over an SR network.

As shown in [Figure 1](#EN-US_TASK_0000001939977813__en-us_task_0172370670_fig_dc_vrp_dci_cfg_003501), there is no direct link between the IPv6 networks where CE1 and CE2 reside. CE1 and CE2 are expected to communicate over an SR network. To achieve this, you can establish a 6PE peer relationship between PE1 and PE2. The 6PE peers use MP-BGP to send IPv6 routes learned from their respective CEs and use SR-MPLS TE tunnels to forward IPv6 data.

**Figure 1** BGP4+ 6PE over SR-MPLS TE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GigabitEthernet0/1/0 and GigabitEthernet0/2/0, respectively.


  
![](figure/en-us_image_0000001902018642.png "Click to enlarge")

#### Precautions

During the configuration, note the following:

* Using the local loopback address of each PE as the source address of the PE is recommended.
* This example uses an explicit path with specified adjacency SIDs to establish the SR-MPLS TE tunnel. Adjacency SIDs that are dynamically generated may change after a device restart, meaning that they need to be reconfigured if adjacency SIDs are specified for the involved explicit path and the involved device is restarted. To facilitate the use of explicit paths, you are advised to run the **ipv4 adjacency** command to manually configure adjacency SIDs for such paths.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure an IGP to enable PE1, PE2, and the P to communicate with each other.
3. Configure an SR-MPLS TE tunnel on the backbone network.
4. Establish an MP-IBGP peer relationship between the PEs and enable them to advertise labeled routes.
5. Configure a tunnel selection policy on each PE.
6. Establish EBGP peer relationships between the CEs and PEs for them to exchange routing information.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs on the PEs and P

#### Procedure

1. Configure addresses for interfaces connecting the PEs and the P according to [Figure 1](#EN-US_TASK_0000001939977813__en-us_task_0172370670_fig_dc_vrp_dci_cfg_003501).
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
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
   <HUAWEI> system-view
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
   <HUAWEI> system-view
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
2. Configure an IGP to enable PE1, PE2, and the P to communicate with each other. IS-IS is used as the IGP in this example.
   
   
   
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
   
   After completing the configuration, run the **display isis peer** command to check whether an IS-IS neighbor relationship has been established between PE1 and the P and between PE2 and the P. If the **Up** state is displayed in the command output, the neighbor relationship has been successfully established. Run the **display ip routing-table** command. The command output shows that the PEs have learned the routes to Loopback1 of each other.
   
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
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
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
   [*PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] ipv4 adjacency local-ip-addr 10.1.1.1 remote-ip-addr 10.1.1.2 sid 330121
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] explicit-path pe1tope2
   ```
   ```
   [*PE1-explicit-path-pe1tope2] next sid label 330121 type adjacency
   ```
   ```
   [*PE1-explicit-path-pe1tope2] next sid label 330120 type adjacency
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
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
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
   [*P] segment-routing
   ```
   ```
   [*P-segment-routing] ipv4 adjacency local-ip-addr 10.1.1.2 remote-ip-addr 10.1.1.1 sid 330221
   ```
   ```
   [*P-segment-routing] ipv4 adjacency local-ip-addr 10.2.1.1 remote-ip-addr 10.2.1.2 sid 330120
   ```
   ```
   [*P-segment-routing] quit
   ```
   ```
   [*P] commit
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
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
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
   [*PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] ipv4 adjacency local-ip-addr 10.2.1.2 remote-ip-addr 10.2.1.1 sid 330220
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] explicit-path pe2tope1
   ```
   ```
   [*PE2-explicit-path-pe2tope1] next sid label 330220 type adjacency
   ```
   ```
   [*PE2-explicit-path-pe2tope1] next sid label 330221 type adjacency
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
   
   After completing the configuration, run the **display tunnel-info all** command. The command output shows that an SR-MPLS TE tunnel has been established. The following example uses the command output on PE1.
   
   ```
   [~PE1] display tunnel-info all
   Tunnel ID            Type                Destination                             Status   
   ----------------------------------------------------------------------------------------
   0x000000000300000001 sr-te               3.3.3.3                                 UP
   ```
   
   Run the **display mpls te tunnel-interface** command. The command output shows that the tunnel status is up. The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls te tunnel-interface
   
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
       Tie-Breaking Policy : None                  Metric Type  : TE 
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
       PCE Delegate      : No                     LSP Control Status : Local control
       Path Verification : No                                     
       Entropy Label     : -                                      
       Associated Tunnel Group ID: -              Associated Tunnel Group Type: -
       Auto BW Remain Time   : -                  Reopt Remain Time     : - 
       Segment-Routing Remote Label   : -                         
       Binding Sid       : -                     Reverse Binding Sid : - 
       FRR Attr Source   : -                     Is FRR degrade down : -
       Color             : - 
   
       Primary LSP ID      : 1.1.1.1:1                            
       LSP State           : UP                    LSP Type     : Primary 
       Configured Attribute Information: 
       Setup Priority      : 7                     Hold Priority: 7 
       IncludeAll          : 0x0                                  
       IncludeAny          : 0x0                                  
       ExcludeAny          : 0x0                                  
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       SidProtectType      : - 
       Actual Attribute Information: 
       Setup Priority      : 7                     Hold Priority: 7 
       IncludeAll          : 0x0  
       IncludeAny          : 0x0   
       ExcludeAny          : 0x0   
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
       Record Route        : -                     Record Label : -
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
4. Establish an MP-IBGP peer relationship between the PEs and enable them to advertise labeled routes.
   
   
   
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
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.3 label-route-capability
   ```
   ```
   [*PE1-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
   ```
   ```
   [~PE1-bgp] quit
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
   [*PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.1 label-route-capability
   ```
   ```
   [*PE2-bgp-af-ipv6] commit
   ```
   ```
   [~PE2-bgp-af-ipv6] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After completing the configuration, run the **display bgp ipv6 peer** command on the PEs to check whether the BGP peer relationship has been established. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp ipv6 peer
   ```
   ```
    BGP local router ID : 10.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.3         4         100        6        7     0 00:01:16 Established        0
   ```
5. Configure a tunnel selection policy on the PEs so that the specified SR-MPLS TE tunnel can be preferentially selected.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy p1
   ```
   ```
   [*PE1-tunnel-policy-p1] tunnel binding destination 3.3.3.3 te Tunnel1
   ```
   ```
   [*PE1-tunnel-policy-p1] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.3 tnl-policy p1
   ```
   ```
   [*PE1-bgp-af-ipv6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] tunnel-policy p1
   ```
   ```
   [*PE2-tunnel-policy-p1] tunnel binding destination 1.1.1.1 te Tunnel1
   ```
   ```
   [*PE2-tunnel-policy-p1] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.1 tnl-policy p1
   ```
   ```
   [*PE2-bgp-af-ipv6] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
6. Establish an EBGP peer relationship between each CE-PE pair.
   
   
   
   # Configure CE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ipv6 enable
   ```
   ```
   [*CE1-LoopBack1] ipv6 address 2001:db8:1:1::1 128
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] interface gigabitethernet0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] ipv6 address 2001:db8::1:1 96
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 10.10.10.10
   ```
   ```
   [*CE1-bgp] peer 2001:db8::1:2 as-number 100
   ```
   ```
   [*CE1-bgp] ipv6-family unicast
   ```
   ```
   [*CE1-bgp-af-ipv6] peer 2001:db8::1:2 enable
   ```
   ```
   [*CE1-bgp-af-ipv6] network 2001:db8:1:1::1 128
   ```
   ```
   [*CE1-bgp-af-ipv6] quit
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of CE2 is similar to the configuration of CE1. For detailed configurations, see Configuration Files.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:db8::1:1 as-number 65410
   ```
   ```
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 2001:db8::1:1 enable
   ```
   ```
   [*PE1-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of PE2 is similar to the configuration of PE1. For detailed configurations, see Configuration Files.
   
   After completing the configuration, run the **display bgp ipv6 peer** command on the PEs to check whether the BGP4+ peer relationships have been established between the PEs and CEs. If the **Established** state is displayed in the command output, the BGP4+ peer relationships have been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp ipv6 peer
    BGP local router ID : 10.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
   
     Peer                   V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.3                4         100     1074     1069     0 15:26:52 Established        1
     2001:DB8::1:1          4       65410     1073     1079     0 15:28:39 Established        1
   ```
7. Verify the configuration.
   
   
   
   After completing the configuration, run the **display ipv6 routing-table** command on each PE to check information about the loopback interface route toward a CE.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ipv6 routing-table
   Routing Table : _public_                                                
            Destinations : 8        Routes : 8                             
   
   Destination  : ::1                                     PrefixLength : 128       
   NextHop      : ::1                                     Preference   : 0 
   Cost         : 0                                       Protocol     : Direct    
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : InLoopBack0                             Flags        : D 
   
   Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104       
   NextHop      : ::FFFF:127.0.0.1                        Preference   : 0 
   Cost         : 0                                       Protocol     : Direct    
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : InLoopBack0                             Flags        : D 
   
   Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128       
   NextHop      : ::1                                     Preference   : 0 
   Cost         : 0                                       Protocol     : Direct    
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : InLoopBack0                             Flags        : D 
   
   
   Destination  : 2001:DB8::                              PrefixLength : 96
   NextHop      : 2001:DB8::1:2                           Preference   : 0 
   Cost         : 0                                       Protocol     : Direct    
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : GigabitEthernet0/2/0                    Flags        : D 
   
   Destination  : 2001:DB8::1:2                           PrefixLength : 128       
   NextHop      : ::1                                     Preference   : 0 
   Cost         : 0                                       Protocol     : Direct    
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : GigabitEthernet0/2/0                    Flags        : D 
   
   Destination  : 2001:DB8:1:1::1                         PrefixLength : 128       
   NextHop      : 2001:DB8::1:1                           Preference   : 255       
   Cost         : 0                                       Protocol     : EBGP      
   RelayNextHop : 2001:DB8::1:1                           TunnelID     : 0x0       
   Interface    : GigabitEthernet0/2/0                    Flags        : RD
   
   Destination  : 2001:DB8:2:2::2                         PrefixLength : 128       
   NextHop      : ::FFFF:3.3.3.3                          Preference   : 255       
   Cost         : 0                                       Protocol     : IBGP      
   RelayNextHop : ::FFFF:0.0.0.0                          TunnelID     : 0x000000000300000001
   Interface    : Tunnel1                                 Flags        : RD
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0 
   Cost         : 0                                       Protocol     : Direct    
   RelayNextHop : ::                                      TunnelID     : 0x0       
   Interface    : NULL0                                   Flags        : DB
   ```
   
   Run the **display ipv6 routing-table verbose** command on each PE to check details about the loopback interface route toward a CE.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ipv6 routing-table 2001:db8:2:2::2 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------  
   Routing Table : _public_    
   Summary Count : 1           
   
   Destination  : 2001:DB8:2:2::2                         PrefixLength : 128       
   NextHop      : ::FFFF:3.3.3.3                          Preference   : 255       
   Neighbour    : ::3.3.3.3                               ProcessID    : 0         
   Label        : 48122                                   Protocol     : IBGP      
   State        : Active Adv Relied                       Cost         : 0         
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0         
   Priority     : low                                     Age          : 2012sec   
   IndirectID   : 0x10000C2                               Instance     :           
   RelayNextHop : ::FFFF:0.0.0.0                          TunnelID     : 0x000000000300000001                                          
   Interface    : Tunnel1                              Flags        : RD        
   RouteColor   : 0                                       QoSInfo      : 0x0 
   ```
   
   The preceding command output shows that the BGP4+ route has successfully recursed to the SR-MPLS TE tunnel.
   
   Check that the CEs can ping each other. For example, CE1 can ping CE2 at 2001:db8:2:2::2.
   
   ```
   [~CE1] ping ipv6 -a 2001:db8:1:1::1 2001:db8:2:2::2
     PING 2001:DB8:2:2::2 : 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:2:2::2  
       bytes=56 Sequence=1 hop limit=61 time=3 ms
       Reply from 2001:DB8:2:2::2  
       bytes=56 Sequence=2 hop limit=61 time=3 ms
       Reply from 2001:DB8:2:2::2  
       bytes=56 Sequence=3 hop limit=61 time=3 ms
       Reply from 2001:DB8:2:2::2  
       bytes=56 Sequence=4 hop limit=61 time=3 ms
       Reply from 2001:DB8:2:2::2  
       bytes=56 Sequence=5 hop limit=61 time=3 ms
   
     --- 2001:DB8:2:2::2 ping statistics---      
       5 packet(s) transmitted     
       5 packet(s) received        
       0.00% packet loss           
       round-trip min/avg/max=3/3/3 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
  #
  explicit-path pe1tope2
   next sid label 330121 type adjacency index 1
   next sid label 330120 type adjacency index 2
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.1.1.1 remote-ip-addr 10.1.1.2 sid 330121
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.1111.1111.1111.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 153616 153800
  #
  interface GigabitEthernet0/1/0
   undo shutdown 
   ipv6 enable
   ipv6 address 2001:DB8::1:2/96
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
   peer 2001:DB8::1:1 as-number 65410
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #              
   ipv6-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 3.3.3.3 label-route-capability
    peer 3.3.3.3 tnl-policy p1
    peer 2001:DB8::1:1 enable
  #
  tunnel-policy p1
   tunnel binding destination 3.3.3.3 te Tunnel1
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
   ipv4 adjacency local-ip-addr 10.1.1.2 remote-ip-addr 10.1.1.1 sid 330221
   ipv4 adjacency local-ip-addr 10.2.1.1 remote-ip-addr 10.2.1.2 sid 330120
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
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
  #
  explicit-path pe2tope1
   next sid label 330220 type adjacency index 1
   next sid label 330221 type adjacency index 2
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.2.1.2 remote-ip-addr 10.2.1.1 sid 330220
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.1111.1111.3333.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 153616 153800
  #
  interface GigabitEthernet0/1/0
   undo shutdown 
   ipv6 enable
   ipv6 address 2001:DB8::2:2/96
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
   peer 2001:DB8::2:1 as-number 65420
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #              
   ipv6-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 1.1.1.1 label-route-capability
    peer 1.1.1.1 tnl-policy p1
    peer 2001:DB8::2:1 enable
  #
  tunnel-policy p1
   tunnel binding destination 1.1.1.1 te Tunnel1
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
   ipv6 enable
   ipv6 address 2001:DB8::1:1/96
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1:1::1/128
  #
  bgp 65410
   router-id 10.10.10.10
   peer 2001:DB8::1:2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:DB8:1:1::1 128
    peer 2001:DB8::1:2 enable
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
   ipv6 enable
   ipv6 address 2001:DB8::2:1/96
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2:2::2/128
  #
  bgp 65420
   router-id 10.20.20.20
   peer 2001:DB8::2:2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:DB8:2:2::2 128
    peer 2001:DB8::2:2 enable
  #
  return
  ```