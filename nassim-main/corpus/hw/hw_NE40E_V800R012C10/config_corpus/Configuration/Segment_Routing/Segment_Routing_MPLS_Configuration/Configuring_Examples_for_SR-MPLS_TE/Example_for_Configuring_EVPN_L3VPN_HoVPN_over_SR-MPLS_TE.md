Example for Configuring EVPN L3VPN HoVPN over SR-MPLS TE
========================================================

This section provides an example for configuring EVPN L3VPN HoVPN over SR-MPLS TE to achieve network connectivity.

#### Networking Requirements

At present, an IP transport network uses L2VPN and L3VPN (HVPN) to carry Layer 2 and Layer 3 services, respectively. These protocols are complex. EVPN can carry both Layer 2 and Layer 3 services. To simplify service transport protocols, many IP transport networks will evolve to EVPN. Specifically, L3VPN HVPN, which carries Layer 3 services, needs to evolve to EVPN L3VPN HVPN. On the network shown in [Figure 1](#EN-US_TASK_0000001381329102__fig126551753125815), the UPE and SPE are connected at the access layer, and the SPE and NPE are connected at the aggregation layer. Before EVPN L3VPN HoVPN is deployed to implement E2E interworking, IGP is deployed separately at the access and aggregation layers for communication at each layer. In an EVPN L3VPN HoVPN scenario, the UPE does not have specific routes to the NPE and can only send service data to the SPE over default routes. In this way, route isolation is implemented. An HoVPN can use devices with relatively poor route management capabilities as UPEs, reducing network deployment costs.

**Figure 1** EVPN L3VPN HoVPN over SR-MPLS TE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001431449369.png "Click to enlarge")

#### Precautions

During the configuration, note the following:

* Using the local loopback address of each PE as the source address of the PE is recommended.
* This example uses an explicit path with specified adjacency SIDs to establish the SR-MPLS TE tunnel. Adjacency SIDs that are dynamically generated may change after a device restart, meaning that they need to be reconfigured if adjacency SIDs are specified for the involved explicit path and the involved device is restarted. To facilitate the use of explicit paths, you are advised to run the **ipv4 adjacency** command to manually configure adjacency SIDs for such paths.
* In this example, prefix SIDs are configured on involved loopback interfaces to generate an SR-MPLS BE path, which functions as the best-effort path when the SR-MPLS TE tunnel fails.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Deploy IGP between the UPE and SPE and also between the SPE and NPE. IS-IS is used in this example.
2. Configure SR-MPLS TE on the UPE, SPE, P, and NPE.
3. Create VPN instances on the UPE, SPE, and NPE.
4. Bind access-side interfaces to the VPN instances on the UPE and NPE.
5. Configure a default static VPN route on the SPE.
6. Configure a route-policy on the NPE to prevent the NPE from receiving default routes.
7. Establish a BGP EVPN peer relationship between the UPE and SPE and also between the SPE and NPE. In addition, perform configuration on the SPE to specify the UPE.
8. Establish an EBGP peer relationship between CE1 and the UPE and also between CE2 and the NPE.
9. Configure a tunnel policy on each PE to allow VPN routes to preferentially select SR-MPLS TE tunnels for forwarding.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the UPE, SPE, P, and NPE: 1.1.1.9, 2.2.2.9, 3.3.3.9, and 4.4.4.9, respectively
* EVPN instance name (vpn1) and RDs (100:1, 200:1, and 300:1) on the UPE, SPE, and NPE
* VPN target of the EVPN instance: 2:2

#### Procedure

1. Configure IP addresses (including loopback interface addresses) for the UPE, SPE, P, and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname UPE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~UPE] interface loopback 1
   ```
   ```
   [*UPE-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*UPE-LoopBack1] quit
   ```
   ```
   [*UPE] interface gigabitethernet0/2/0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ip address 10.0.1.1 24
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname SPE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~SPE] interface loopback 1
   ```
   ```
   [*SPE-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*SPE-LoopBack1] quit
   ```
   ```
   [~SPE] interface loopback 10
   ```
   ```
   [*SPE-LoopBack10] ip address 2.2.2.10 32
   ```
   ```
   [*SPE-LoopBack10] quit
   ```
   ```
   [*SPE] interface gigabitethernet0/1/0
   ```
   ```
   [*SPE-GigabitEthernet0/1/0] ip address 10.0.1.2 24
   ```
   ```
   [*SPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*SPE] interface gigabitethernet0/2/0
   ```
   ```
   [*SPE-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   ```
   ```
   [*SPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*SPE] commit
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
   [*P-LoopBack1] ip address 3.3.3.9 32
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
   
   # Configure the NPE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname NPE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NPE] interface loopback 1
   ```
   ```
   [*NPE-LoopBack1] ip address 4.4.4.9 32
   ```
   ```
   [*NPE-LoopBack1] quit
   ```
   ```
   [*NPE] interface gigabitethernet0/2/0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
2. Deploy IGP. This example uses IS-IS. The UPE and SPE belong to IS-IS process 100, and the SPE, P, and NPE belong to IS-IS process 1.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] isis 100
   ```
   ```
   [*UPE-isis-100] is-level level-1
   ```
   ```
   [*UPE-isis-100] network-entity 00.1111.1111.0000.00
   ```
   ```
   [*UPE-isis-100] quit
   ```
   ```
   [*UPE] interface loopback 1
   ```
   ```
   [*UPE-LoopBack1] isis enable 100
   ```
   ```
   [*UPE-LoopBack1] quit
   ```
   ```
   [*UPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] isis enable 100
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] isis 1
   ```
   ```
   [*SPE-isis-1] is-level level-2
   ```
   ```
   [*SPE-isis-1] network-entity 00.1111.1111.1111.00
   ```
   ```
   [*SPE-isis-1] quit
   ```
   ```
   [*SPE] interface loopback 1
   ```
   ```
   [*SPE-LoopBack1] isis enable 1
   ```
   ```
   [*SPE-LoopBack1] quit
   ```
   ```
   [*SPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*SPE-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*SPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*SPE] isis 100
   ```
   ```
   [*SPE-isis-100] is-level level-1
   ```
   ```
   [*SPE-isis-100] network-entity 00.1111.1111.0001.00
   ```
   ```
   [*SPE-isis-100] quit
   ```
   ```
   [*SPE] interface loopback 10
   ```
   ```
   [*SPE-LoopBack10] isis enable 100
   ```
   ```
   [*SPE-LoopBack10] quit
   ```
   ```
   [*SPE] interface GigabitEthernet 0/1/0
   ```
   ```
   [*SPE-GigabitEthernet0/1/0] isis enable 100
   ```
   ```
   [*SPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*SPE] commit
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
   
   # Configure the NPE.
   
   ```
   [~NPE] isis 1
   ```
   ```
   [*NPE-isis-1] is-level level-2
   ```
   ```
   [*NPE-isis-1] network-entity 00.1111.1111.3333.00
   ```
   ```
   [*NPE-isis-1] quit
   ```
   ```
   [*NPE] interface loopback 1
   ```
   ```
   [*NPE-LoopBack1] isis enable 1
   ```
   ```
   [*NPE-LoopBack1] quit
   ```
   ```
   [*NPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
   
   After the configuration is complete, run the **display isis route** command. The command output shows that routes are learned properly. The following example uses the command output on the SPE.
   
   ```
   [~SPE] display isis 1 route 
   
                            Route information for ISIS(1)      
                            -----------------------------      
   
                           ISIS(1) Level-2 Forwarding Table    
                           --------------------------------    
   
   IPV4 Destination   IntCost    ExtCost ExitInterface     NextHop         Flags     
   -------------------------------------------------------------------------------   
   2.2.2.9/32         0          NULL    Loop1             Direct          D/-/L/-   
   3.3.3.9/32         10         NULL    GE0/2/0           10.1.1.2        A/-/-/-   
   4.4.4.9/32         20         NULL    GE0/2/0           10.1.1.2        A/-/-/-   
   10.1.1.0/24        10         NULL    GE0/2/0           Direct          D/-/L/-   
   10.2.1.0/24        20         NULL    GE0/2/0           10.1.1.2        A/-/-/-   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,       
               U-Up/Down Bit Set, LP-Local Prefix-Sid          
        Protect Type: L-Link Protect, N-Node Protect 
   ```
   ```
   [~SPE] display isis 100 route                                
   
                            Route information for ISIS(100)    
                            -----------------------------      
   
                           ISIS(100) Level-1 Forwarding Table  
                           --------------------------------    
   
   IPV4 Destination   IntCost    ExtCost ExitInterface     NextHop         Flags     
   -------------------------------------------------------------------------------   
   1.1.1.9/32         10         NULL    GE0/1/0           10.0.1.1        A/-/-/-   
   2.2.2.10/32        0          NULL    Loop10            Direct          D/-/L/-   
   10.0.1.0/24        10         NULL    GE0/1/0           Direct          D/-/L/-   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,       
               U-Up/Down Bit Set, LP-Local Prefix-Sid          
        Protect Type: L-Link Protect, N-Node Protect 
   ```
   
   The preceding command output shows that the routing information of IS-IS process 1 is isolated from that of IS-IS process 100.
   
   Run the **display ip routing-table** command. The command output shows information about the IP routing table. The following example uses the command output on the SPE.
   
   ```
   [~SPE] display ip routing-table  
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route       
   ------------------------------------------------------------------------------ 
   Routing Table : _public_  
            Destinations : 16       Routes : 16                                   
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface   
   
           1.1.1.9/32  ISIS-L1 15   10            D   10.0.1.1        GigabitEthernet0/1/0 
           2.2.2.9/32  Direct  0    0             D   127.0.0.1       LoopBack1   
          2.2.2.10/32  Direct  0    0             D   127.0.0.1       LoopBack10  
           3.3.3.9/32  ISIS-L2 15   10            D   10.1.1.2        GigabitEthernet0/2/0 
           4.4.4.9/32  ISIS-L2 15   20            D   10.1.1.2        GigabitEthernet0/2/0 
          10.0.1.0/24  Direct  0    0             D   10.0.1.2        GigabitEthernet0/1/0 
          10.0.1.2/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
        10.0.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
          10.1.1.0/24  Direct  0    0             D   10.1.1.1        GigabitEthernet0/2/0 
          10.1.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0 
        10.1.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0 
          10.2.1.0/24  ISIS-L2 15   20            D   10.1.1.2        GigabitEthernet0/2/0 
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0 
         127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   ```
3. Configure SR-MPLS TE tunnel functions between the SPE and NPE.
   
   
   
   # Configure the SPE.
   
   ```
   [~SPE] mpls lsr-id 2.2.2.9
   ```
   ```
   [*SPE] mpls
   ```
   ```
   [*SPE-mpls] mpls te
   ```
   ```
   [*SPE-mpls] quit
   ```
   ```
   [*SPE] segment-routing
   ```
   ```
   [*SPE-segment-routing] quit
   ```
   ```
   [*SPE] isis 1
   ```
   ```
   [*SPE-isis-1] cost-style wide
   ```
   ```
   [*SPE-isis-1] traffic-eng level-2
   ```
   ```
   [*SPE-isis-1] segment-routing mpls
   ```
   ```
   [*SPE-isis-1] segment-routing global-block 153616 153800
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*SPE-isis-1] quit
   ```
   ```
   [*SPE] segment-routing
   ```
   ```
   [*SPE-segment-routing] ipv4 adjacency local-ip-addr 10.1.1.1 remote-ip-addr 10.1.1.2 sid 330121
   ```
   ```
   [*SPE-segment-routing] quit
   ```
   ```
   [*SPE] interface loopback 1
   ```
   ```
   [*SPE-LoopBack1] isis prefix-sid absolute 153711
   ```
   ```
   [*SPE-LoopBack1] quit
   ```
   ```
   [*SPE] explicit-path p1
   ```
   ```
   [*SPE-explicit-path-p1] next sid label 330121 type adjacency
   ```
   ```
   [*SPE-explicit-path-p1] next sid label 330120 type adjacency
   ```
   ```
   [*SPE-explicit-path-p1] quit
   ```
   ```
   [*SPE] interface tunnel1
   ```
   ```
   [*SPE-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*SPE-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*SPE-Tunnel1] destination 4.4.4.9
   ```
   ```
   [*SPE-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*SPE-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*SPE-Tunnel1] mpls te path explicit-path p1
   ```
   ```
   [*SPE-Tunnel1] quit
   ```
   ```
   [*SPE] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] mpls lsr-id 3.3.3.9
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
   [*P] interface loopback 1
   ```
   ```
   [*P-LoopBack1] isis prefix-sid absolute 153721
   ```
   ```
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] mpls lsr-id 4.4.4.9
   ```
   ```
   [*NPE] mpls
   ```
   ```
   [*NPE-mpls] mpls te
   ```
   ```
   [*NPE-mpls] quit
   ```
   ```
   [*NPE] segment-routing
   ```
   ```
   [*NPE-segment-routing] quit
   ```
   ```
   [*NPE] isis 1
   ```
   ```
   [*NPE-isis-1] cost-style wide
   ```
   ```
   [*NPE-isis-1] traffic-eng level-2
   ```
   ```
   [*NPE-isis-1] segment-routing mpls
   ```
   ```
   [*NPE-isis-1] segment-routing global-block 153616 153800
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*NPE-isis-1] quit
   ```
   ```
   [*NPE] segment-routing
   ```
   ```
   [*NPE-segment-routing] ipv4 adjacency local-ip-addr 10.2.1.2 remote-ip-addr 10.2.1.1 sid 330220
   ```
   ```
   [*NPE-segment-routing] quit
   ```
   ```
   [*NPE] interface loopback 1
   ```
   ```
   [*NPE-LoopBack1] isis prefix-sid absolute 153731
   ```
   ```
   [*NPE-LoopBack1] quit
   ```
   ```
   [*NPE] explicit-path p1
   ```
   ```
   [*NPE-explicit-path-p1] next sid label 330220 type adjacency
   ```
   ```
   [*NPE-explicit-path-p1] next sid label 330221 type adjacency
   ```
   ```
   [*NPE-explicit-path-p1] quit
   ```
   ```
   [*NPE] interface tunnel1
   ```
   ```
   [*NPE-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*NPE-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*NPE-Tunnel1] destination 2.2.2.9
   ```
   ```
   [*NPE-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*NPE-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*NPE-Tunnel1] mpls te path explicit-path p1
   ```
   ```
   [*NPE-Tunnel1] quit
   ```
   ```
   [*NPE] commit
   ```
   
   After the configuration is complete, run the **display mpls te tunnel-interface** command to check the tunnel interface status. The command output shows that the status is up.
   
   The following example uses the command output on the SPE.
   
   ```
   [~SPE] display mpls te tunnel-interface Tunnel 1  
       Tunnel Name       : Tunnel1           
       Signalled Tunnel Name: -              
       Tunnel State Desc : CR-LSP is Up      
       Tunnel Attributes   :                 
       Active LSP          : Primary LSP     
       Traffic Switch      : -               
       Session ID          : 1               
       Ingress LSR ID      : 2.2.2.9               Egress LSR ID: 4.4.4.9        
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
   
       Primary LSP ID      : 2.2.2.9:1       
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
       Explicit Path Name  : p1                               Hop Limit: -       
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
4. Configure SR-MPLS TE tunnel functions between the UPE and SPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] mpls lsr-id 1.1.1.9
   ```
   ```
   [*UPE] mpls
   ```
   ```
   [*UPE-mpls] mpls te
   ```
   ```
   [*UPE-mpls] quit
   ```
   ```
   [*UPE] segment-routing
   ```
   ```
   [*UPE-segment-routing] quit
   ```
   ```
   [*UPE] isis 100
   ```
   ```
   [*UPE-isis-100] cost-style wide
   ```
   ```
   [*UPE-isis-100] traffic-eng level-1
   ```
   ```
   [*UPE-isis-100] segment-routing mpls
   ```
   ```
   [*UPE-isis-100] segment-routing global-block 153801 154000
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*UPE-isis-100] quit
   ```
   ```
   [*UPE] segment-routing
   ```
   ```
   [*UPE-segment-routing] ipv4 adjacency local-ip-addr 10.0.1.1 remote-ip-addr 10.0.1.2 sid 330122
   ```
   ```
   [*UPE-segment-routing] quit
   ```
   ```
   [*UPE] interface loopback 1
   ```
   ```
   [*UPE-LoopBack1] isis prefix-sid absolute 153900
   ```
   ```
   [*UPE-LoopBack1] quit
   ```
   ```
   [*UPE] explicit-path p2
   ```
   ```
   [*UPE-explicit-path-p2] next sid label 330122 type adjacency
   ```
   ```
   [*UPE-explicit-path-p2] quit
   ```
   ```
   [*UPE] interface tunnel10
   ```
   ```
   [*UPE-Tunnel10] ip address unnumbered interface loopback 1
   ```
   ```
   [*UPE-Tunnel10] tunnel-protocol mpls te
   ```
   ```
   [*UPE-Tunnel10] destination 2.2.2.10
   ```
   ```
   [*UPE-Tunnel10] mpls te tunnel-id 10
   ```
   ```
   [*UPE-Tunnel10] mpls te signal-protocol segment-routing
   ```
   ```
   [*UPE-Tunnel10] mpls te path explicit-path p2
   ```
   ```
   [*UPE-Tunnel10] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] isis 100
   ```
   ```
   [~SPE-isis-100] cost-style wide
   ```
   ```
   [*SPE-isis-100] traffic-eng level-1
   ```
   ```
   [*SPE-isis-100] segment-routing mpls
   ```
   ```
   [*SPE-isis-100] segment-routing global-block 153801 154000
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*SPE-isis-1] quit
   ```
   ```
   [*SPE] segment-routing
   ```
   ```
   [*SPE-segment-routing] ipv4 adjacency local-ip-addr 10.0.1.2 remote-ip-addr 10.0.1.1 sid 330222
   ```
   ```
   [*SPE-segment-routing] quit
   ```
   ```
   [*SPE] interface loopback 10
   ```
   ```
   [*SPE-LoopBack10] isis prefix-sid absolute 153910
   ```
   ```
   [*SPE-LoopBack10] quit
   ```
   ```
   [*SPE] explicit-path p2
   ```
   ```
   [*SPE-explicit-path-p2] next sid label 330222 type adjacency
   ```
   ```
   [*SPE-explicit-path-p2] quit
   ```
   ```
   [*SPE] interface tunnel10
   ```
   ```
   [*SPE-Tunnel10] ip address unnumbered interface loopback 1
   ```
   ```
   [*SPE-Tunnel10] tunnel-protocol mpls te
   ```
   ```
   [*SPE-Tunnel10] destination 1.1.1.9
   ```
   ```
   [*SPE-Tunnel10] mpls te tunnel-id 10
   ```
   ```
   [*SPE-Tunnel10] mpls te signal-protocol segment-routing
   ```
   ```
   [*SPE-Tunnel10] mpls te path explicit-path p2
   ```
   ```
   [*SPE-Tunnel10] quit
   ```
   ```
   [*SPE] commit
   ```
   
   After the configuration is complete, run the **display mpls te tunnel-interface** command to check the tunnel interface status. The command output shows that the status is up.
   
   Run the **display tunnel-info all** command to check information about all tunnels, including SR-MPLS TE and SR-MPLS BE tunnels, which are respectively indicated by **sr-te** and **srbe-lsp** in the command output.
   
   The following example uses the command output on the SPE.
   
   ```
   [~SPE] display tunnel-info all   
   Tunnel ID            Type                Destination            Status
   -----------------------------------------------------------------------
   0x000000000300000001 sr-te               4.4.4.9                UP 
   0x000000000300000002 sr-te               1.1.1.9                UP 
   0x000000002900000006 srbe-lsp            1.1.1.9                UP 
   0x000000002900000008 srbe-lsp            3.3.3.9                UP 
   0x000000002900000009 srbe-lsp            4.4.4.9                UP
   ```
5. Create VPN instances on the UPE, SPE, and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpn1
   ```
   ```
   [*UPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*UPE-vpn-instance-vpn1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] ip vpn-instance vpn1
   ```
   ```
   [*SPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*SPE-vpn-instance-vpn1] quit
   ```
   ```
   [*SPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] ip vpn-instance vpn1
   ```
   ```
   [*NPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 300:1
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*NPE-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE] commit
   ```
6. Bind access-side interfaces to the VPN instances on the UPE and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ip address 172.16.1.2 255.255.255.0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] ip address 172.17.1.2 255.255.255.0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
7. Configure a default static route on the SPE.
   
   
   ```
   [~SPE] ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0
   ```
   ```
   [*SPE] commit
   ```
8. Configure a route-policy on the NPE to prevent the NPE from receiving default routes.
   
   
   ```
   [~NPE] ip ip-prefix default index 10 permit 0.0.0.0 0
   ```
   ```
   [*NPE] route-policy SPE deny node 10
   ```
   ```
   [*NPE-route-policy] if-match ip-prefix default
   ```
   ```
   [*NPE-route-policy] quit
   ```
   ```
   [*NPE] route-policy SPE permit node 20
   ```
   ```
   [*NPE-route-policy] quit
   ```
   ```
   [*NPE] ip vpn-instance vpn1
   ```
   ```
   [*NPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] import route-policy SPE evpn
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*NPE-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE] commit
   ```
9. Establish a BGP EVPN peer relationship between the UPE and SPE and also between the SPE and NPE. In addition, perform configuration on the SPE to specify the UPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bgp 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.10 as-number 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.10 connect-interface LoopBack1
   ```
   ```
   [*UPE-bgp] l2vpn-family evpn
   ```
   ```
   [*UPE-bgp-af-evpn] peer 2.2.2.10 enable
   ```
   ```
   [*UPE-bgp-af-evpn] quit
   ```
   ```
   [*UPE-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*UPE-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*UPE-bgp-vpn1] import-route direct
   ```
   ```
   [*UPE-bgp-vpn1] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] bgp 100
   ```
   ```
   [*SPE-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*SPE-bgp] peer 1.1.1.9 connect-interface LoopBack10
   ```
   ```
   [*SPE-bgp] peer 4.4.4.9 as-number 100
   ```
   ```
   [*SPE-bgp] peer 4.4.4.9 connect-interface LoopBack1
   ```
   ```
   [*SPE-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE-bgp-af-evpn] undo policy vpn-target
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.9 enable
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.9 upe
   ```
   ```
   [*SPE-bgp-af-evpn] peer 4.4.4.9 enable
   ```
   ```
   [*SPE-bgp-af-evpn] quit
   ```
   ```
   [*SPE-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*SPE-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*SPE-bgp-vpn1] network 0.0.0.0 0
   ```
   ```
   [*SPE-bgp-vpn1] quit
   ```
   ```
   [*SPE-bgp] quit
   ```
   ```
   [*SPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] bgp 100
   ```
   ```
   [*NPE-bgp] peer 2.2.2.9 as-number 100
   ```
   ```
   [*NPE-bgp] peer 2.2.2.9 connect-interface LoopBack1
   ```
   ```
   [*NPE-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2.2.2.9 enable
   ```
   ```
   [*NPE-bgp-af-evpn] quit
   ```
   ```
   [*NPE-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*NPE-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*NPE-bgp-vpn1] import-route direct
   ```
   ```
   [*NPE-bgp-vpn1] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
10. Establish an EBGP peer relationship between CE1 and the UPE and also between CE2 and the NPE.
    
    
    
    # Configure CE1.
    
    ```
    [~CE1] interface loopback 1
    ```
    ```
    [*CE1-LoopBack1] ip address 10.11.1.1 32
    ```
    ```
    [*CE1-LoopBack1] quit
    ```
    ```
    [*CE1] interface gigabitethernet0/1/0
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] ip address 172.16.1.1 24
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] quit
    ```
    ```
    [*CE1] bgp 65410
    ```
    ```
    [*CE1-bgp] peer 172.16.1.2 as-number 100
    ```
    ```
    [*CE1-bgp] network 10.11.1.1 32
    ```
    ```
    [*CE1-bgp] quit
    ```
    ```
    [*CE1] commit
    ```
    
    # Configure the UPE.
    
    ```
    [~UPE] bgp 100
    ```
    ```
    [*UPE-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*UPE-bgp-vpn1] peer 172.16.1.1 as-number 65410
    ```
    ```
    [*UPE-bgp-vpn1] commit
    ```
    ```
    [~UPE-bgp-vpn1] quit
    ```
    
    # Configure CE2.
    
    ```
    [~CE2] interface loopback 1
    ```
    ```
    [*CE2-LoopBack1] ip address 10.22.1.1 32
    ```
    ```
    [*CE2-LoopBack1] quit
    ```
    ```
    [*CE2] interface gigabitethernet0/1/0
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] ip address 172.17.1.1 24
    ```
    ```
    [*CE2-GigabitEthernet0/1/0] quit
    ```
    ```
    [*CE2] bgp 65420
    ```
    ```
    [*CE2-bgp] peer 172.17.1.2 as-number 100
    ```
    ```
    [*CE2-bgp] network 10.22.1.1 32
    ```
    ```
    [*CE2-bgp] quit
    ```
    ```
    [*CE2] commit
    ```
    
    # Configure the NPE.
    
    ```
    [~NPE] bgp 100
    ```
    ```
    [*NPE-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*NPE-bgp-vpn1] peer 172.17.1.1 as-number 65420
    ```
    ```
    [*NPE-bgp-vpn1] commit
    ```
    ```
    [~NPE-bgp-vpn1] quit
    ```
    
    After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between CE1 and the UPE and also between CE2 and the NPE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
    
    The following example uses the peer relationship between CE1 and the UPE.
    
    ```
    [~UPE] display bgp vpnv4 vpn-instance vpn1 peer
     
     BGP local router ID : 10.0.1.1     
     Local AS number : 100
    
     VPN-Instance vpn1, Router ID 10.0.1.1:
     Total number of peers : 1                 Peers in established state : 1
    
      Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv 
      172.16.1.1                       4       65410        5        6     0 00:01:15 Established        1
    ```
11. Configure a tunnel policy on each PE to allow VPN routes to preferentially select SR-MPLS TE tunnels for forwarding.
    
    
    
    # Configure the UPE.
    
    ```
    [~UPE] tunnel-policy p1
    ```
    ```
    [*UPE-tunnel-policy-p1] tunnel select-seq sr-te load-balance-number 1 unmix
    ```
    ```
    [*UPE-tunnel-policy-p1] quit
    ```
    ```
    [*UPE] ip vpn-instance vpn1 
    ```
    ```
    [*UPE-vpn-instance-vpn1] tnl-policy p1 evpn
    ```
    ```
    [*UPE-vpn-instance-vpn1] quit
    ```
    ```
    [*UPE] commit
    ```
    
    
    
    # Configure the SPE.
    
    ```
    [~SPE] tunnel-policy p1
    ```
    ```
    [*SPE-tunnel-policy-p1] tunnel select-seq sr-te load-balance-number 1 unmix
    ```
    ```
    [*SPE-tunnel-policy-p1] quit
    ```
    
    
    ```
    [*SPE] ip vpn-instance vpn1 
    ```
    ```
    [*SPE-vpn-instance-vpn1] tnl-policy p1 evpn
    ```
    ```
    [*SPE-vpn-instance-vpn1] quit
    ```
    ```
    [*SPE] commit
    ```
    
    # Configure the NPE.
    
    ```
    [~NPE] tunnel-policy p1
    ```
    ```
    [*NPE-tunnel-policy-p1] tunnel select-seq sr-te load-balance-number 1 unmix
    ```
    ```
    [*NPE-tunnel-policy-p1] quit
    ```
    ```
    [*NPE] ip vpn-instance vpn1 
    ```
    ```
    [*NPE-vpn-instance-vpn1] tnl-policy p1 evpn
    ```
    ```
    [*NPE-vpn-instance-vpn1] quit
    ```
    ```
    [*NPE] commit
    ```
    
    Run the **display bgp evpn all routing-table** command on the NPE. The command output shows EVPN routes received from the UPE.
    
    ```
    [~NPE] display bgp evpn all routing-table
    
     Local AS number : 100      
    
     BGP Local router ID is 10.2.1.2                                      
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,          
                   h - history,  i - internal, s - suppressed, S - Stale  
                   Origin : i - IGP, e - EGP, ? - incomplete              
    
    
     EVPN address family:       
     Number of Ip Prefix Routes: 5                                        
     Route Distinguisher: 100:1 
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop 
     *>i   0:172.16.1.0:24                                        2.2.2.9 
     *>i   0:10.11.1.1:32                                         2.2.2.9 
     Route Distinguisher: 300:1 
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop 
     *>    0:172.17.1.0:24                                        0.0.0.0 
     *                                                            172.17.1.1                  
     *>    0:10.22.2.2:32                                         172.17.1.1
    ```
    
    Run the **display ip routing-table vpn-instance** command on the NPE. The command output shows that routes have been added to the IP routing table of the corresponding VPN instance.
    
    ```
    [~NPE] display ip routing-table vpn-instance vpn1 
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
    ------------------------------------------------------------------------------   
    Routing Table : vpn1          
             Destinations : 8        Routes : 8                                      
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface     
    
          10.11.1.1/32  IBGP    255  0             RD  2.2.2.9         Tunnel1       
          10.22.2.2/32  EBGP    255  0             RD  172.17.1.1      GigabitEthernet0/1/0 
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0   
         172.16.1.0/24  IBGP    255  0             RD  2.2.2.9         Tunnel1       
         172.17.1.0/24  Direct  0    0             D   172.17.1.2      GigabitEthernet0/1/0 
         172.17.1.2/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
       172.17.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    
    Run the **display bgp evpn all routing-table** command on the UPE. The command output shows the default EVPN route received from the SPE.
    
    ```
    [~UPE] display bgp evpn all routing-table
    
     Local AS number : 100        
    
     BGP Local router ID is 10.1.1.10    
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path, 
                   h - history,  i - internal, s - suppressed, S - Stale             
                   Origin : i - IGP, e - EGP, ? - incomplete                         
    
    
     EVPN address family:         
     Number of Ip Prefix Routes: 4       
     Route Distinguisher: 100:1   
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop            
     *>    0:172.16.1.0:24                                        0.0.0.0  
     *                                                            172.16.1.1          
     *>    0:10.11.1.1:32                                         172.16.1.1         
     Route Distinguisher: 200:1   
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop            
     *>i   0:0.0.0.0:0                                            2.2.2.10 
    ```
    
    Run the **display ip routing-table vpn-instance** command on the UPE. The command output shows that routes have been added to the IP routing table of the corresponding VPN instance.
    
    ```
    [~UPE] display ip routing-table vpn-instance vpn1 
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                                              
    ------------------------------------------------------------------------------   
    Routing Table : vpn1          
             Destinations : 7        Routes : 7                                      
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface     
    
            0.0.0.0/0   IBGP    255  0             RD  2.2.2.10        Tunnel10      
          10.11.1.1/32  EBGP    255  0             RD  172.16.1.1      GigabitEthernet0/1/0
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0   
         172.16.1.0/24  Direct  0    0             D   172.16.1.2      GigabitEthernet0/1/0 
         172.16.1.2/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
       172.16.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    
    Note that there is a default route (0.0.0.0/0) in the IP routing table of the VPN instance on the UPE, and the recursion outbound interface of the route is Tunnel10.
12. Verify the configuration.
    
    
    
    Run the **display ip routing-table** command on the CE to check the routes to the peer CE.
    
    The command output on CE1 shows that the route on CE1 is the default route (0.0.0.0/0), not any specific route to CE2.
    
    ```
    [~CE1] display ip routing-table  
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route          
    ------------------------------------------------------------------------------ 
    Routing Table : _public_  
             Destinations : 9        Routes : 9                                    
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface   
    
            0.0.0.0/0   EBGP    255  0             RD  172.16.1.2      GigabitEthernet0/1/0     
          10.11.1.1/32  Direct  0    0             D   127.0.0.1       LoopBack1   
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0 
          127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
    127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
         172.16.1.0/24  Direct  0    0             D   172.16.1.1      GigabitEthernet0/1/0     
         172.16.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0     
       172.16.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0     
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
    ```
    
    The command output on CE2 shows that CE2 has a specific route (10.11.1.1/32) to CE1.
    
    ```
    [~CE2] display ip routing-table   
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route          
    ------------------------------------------------------------------------------ 
    Routing Table : _public_  
             Destinations : 10       Routes : 10                                   
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface   
    
          10.11.1.1/32  EBGP    255  0             RD  172.17.1.2      GigabitEthernet0/1/0     
          10.22.2.2/32  Direct  0    0             D   127.0.0.1       LoopBack1   
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0 
          127.0.0.1/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
    127.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0 
         172.16.1.0/24  EBGP    255  0             RD  172.17.1.2      GigabitEthernet0/1/0     
         172.17.1.0/24  Direct  0    0             D   172.17.1.1      GigabitEthernet0/1/0     
         172.17.1.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0     
       172.17.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0     
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    
    The CEs can ping each other. For example, CE1 can ping CE2 (10.22.2.2).
    
    ```
    [~CE1] ping 10.22.2.2
      PING 10.22.2.2: 56  data bytes, press CTRL_C to break   
        Reply from 10.22.2.2: bytes=56 Sequence=1 ttl=251 time=48 ms     
        Reply from 10.22.2.2: bytes=56 Sequence=2 ttl=251 time=36 ms     
        Reply from 10.22.2.2: bytes=56 Sequence=3 ttl=251 time=32 ms     
        Reply from 10.22.2.2: bytes=56 Sequence=4 ttl=251 time=30 ms     
        Reply from 10.22.2.2: bytes=56 Sequence=5 ttl=251 time=35 ms     
    
      --- 10.22.2.2 ping statistics ---                       
        5 packet(s) transmitted                               
        5 packet(s) received                                  
        0.00% packet loss                                     
        round-trip min/avg/max = 30/36/48 ms
    ```

#### Configuration Files

* UPE configuration file
  ```
  #
  sysname UPE
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
  #               
  mpls lsr-id 1.1.1.9
  #
  mpls
   mpls te
  #
  explicit-path p2
   next sid label 330122 type adjacency index 1
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.0.1.1 remote-ip-addr 10.0.1.2 sid 330122
  #
  isis 100
   is-level level-1
   cost-style wide
   network-entity 00.1111.1111.0000.00
   traffic-eng level-1
   segment-routing mpls
   segment-routing global-block 153801 154000
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 172.16.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.0.1.1 255.255.255.0
   isis enable 100
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 100
   isis prefix-sid absolute 153900
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.10
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 10
   mpls te path explicit-path p2
  #
  bgp 100
   peer 2.2.2.10 as-number 100
   peer 2.2.2.10 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.10 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    peer 172.16.1.1 as-number 65410
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.10 enable
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1 unmix
  #
  return
  ```
* SPE configuration file
  
  ```
  #
  sysname SPE
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
   mpls te
  #
  explicit-path p1
   next sid label 330121 type adjacency index 1
   next sid label 330120 type adjacency index 2
  #
  explicit-path p2
   next sid label 330222 type adjacency index 1
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.1.1.1 remote-ip-addr 10.1.1.2 sid 330121
   ipv4 adjacency local-ip-addr 10.0.1.2 remote-ip-addr 10.0.1.1 sid 330222
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.1111.1111.1111.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 153616 153800
  #
  isis 100
   is-level level-1
   cost-style wide
   network-entity 00.1111.1111.0001.00
   traffic-eng level-1
   segment-routing mpls
   segment-routing global-block 153801 154000
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.0.1.2 255.255.255.0
   isis enable 100
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 153711
  #               
  interface LoopBack10
   ip address 2.2.2.10 255.255.255.255
   isis enable 100
   isis prefix-sid absolute 153910
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.9
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path p1 
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack10
   tunnel-protocol mpls te
   destination 1.1.1.9
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 10
   mpls te path explicit-path p2 
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack10
   peer 4.4.4.9 as-number 100
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
    peer 4.4.4.9 enable
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.9 enable
    peer 1.1.1.9 upe
    peer 4.4.4.9 enable
  #
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1 unmix
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 3.3.3.9
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
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 153721
  #
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 300:1
    import route-policy SPE evpn
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
   mpls te
  #
  explicit-path p1
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
   ip binding vpn-instance vpn1
   ip address 172.17.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 153731
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.9
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path p1 
  #
  bgp 100
   private-4-byte-as enable
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
    peer 172.17.1.1 as-number 65420
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.9 enable
  #
  ip ip-prefix default index 10 permit 0.0.0.0 0
  #
  route-policy SPE deny node 10
   if-match ip-prefix default
  #
  route-policy SPE permit node 20
  #
  tunnel-policy p1
   tunnel select-seq sr-te load-balance-number 1 unmix
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
   ip address 172.16.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 10.11.1.1 255.255.255.255
  #
  bgp 65410
   peer 172.16.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 10.11.1.1 255.255.255.255
    peer 172.16.1.2 enable
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
   ip address 172.17.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 10.22.2.2 255.255.255.255
  #
  bgp 65420
   peer 172.17.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 10.22.2.2 255.255.255.255
    peer 172.17.1.2 enable
  #
  return
  ```