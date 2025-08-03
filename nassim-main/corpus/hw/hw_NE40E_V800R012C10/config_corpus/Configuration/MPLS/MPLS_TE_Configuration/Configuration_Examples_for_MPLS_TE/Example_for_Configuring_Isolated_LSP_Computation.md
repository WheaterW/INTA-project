Example for Configuring Isolated LSP Computation
================================================

This section provides an example for configuring isolated label switched path (LSP) computation.

#### Networking Requirements

Isolated primary and hot-standby LSPs are necessary to improve the LSP reliability on IP radio access networks (IP RANs) that use Multiprotocol Label Switching (MPLS) Traffic Engineering (TE). The constrained shortest path first (CSPF) algorithm does not meet this reliability requirement because CSPF may compute two LSPs that intersect at aggregation nodes. Specifying explicit paths for LSPs can improve reliability but this method does not adapt to topology changes. Each time a node is added to or deleted from the IP RAN, operators must configure new explicit paths, which is time-consuming and laborious. Isolated LSP computation is another method to improve reliability. After this function is configured, the device uses both the disjoint and CSPF algorithms to compute isolated primary and hot-standby LSPs.

[Figure 1](#EN-US_TASK_0172368354__fig_dc_vrp_te-p2p_cfg_017201) illustrates an IP RAN that uses a Resource Reservation Protocol - Traffic Engineering (RSVP-TE) tunnel. Devices on this network use the Open Shortest Path First (OSPF) protocol for communication. The numeral on each link represents the link TE metric. An RSVP-TE tunnel needs to be established between LSRA and LSRF. The constraint-based routed label switched path (CR-LSP) hot standby function needs to be enabled.

Two isolated LSPs exist on this topology: LSRA -> LSRC -> LSRE -> LSRF and LSRA -> LSRB -> LSRD -> LSRF. However, if the disjoint algorithm is not enabled, CSPF computes LSRA -> LSRC-> LSRD-> LSRF as the primary LSP and cannot compute an isolated hot-standby LSP. To improve LSP reliability, configure isolated LSP computation.

**Figure 1** RSVP-TE tunnel networking  
![](images/fig_dc_vrp_te-p2p_cfg_017201.png "Click to enlarge")

**Table 1** Interfaces and IP addresses
| Device Name | Interface Name | IP Address and Mask | Device Name | Interface Name | IP Address and Mask |
| --- | --- | --- | --- | --- | --- |
| LSRA | Loopback1 | 1.1.1.1/32 | LSRB | Loopback1 | 2.2.2.2/32 |
| GE 0/1/0 | 10.1.1.1/24 | GE 0/1/0 | 10.1.2.2/24 |
| GE 0/1/1 | 10.1.2.1/24 | GE 0/1/1 | 10.1.6.1/24 |
| LSRC | Loopback1 | 3.3.3.3/32 | LSRD | Loopback1 | 4.4.4.4/32 |
| GE 0/1/0 | 10.1.1.2/24 | GE 0/1/0 | 10.1.6.2/24 |
| GE 0/1/1 | 10.1.3.1/24 | GE 0/1/1 | 10.1.3.2/24 |
| GE 0/1/2 | 10.1.4.1/24 | GE 0/1/2 | 10.1.7.1/24 |
| LSRE | Loopback1 | 5.5.5.5/32 | LSRF | Loopback1 | 6.6.6.6/32 |
| GE 0/1/0 | 10.1.4.2/24 | GE 0/1/0 | 10.1.7.2/24 |
| GE 0/1/1 | 10.1.5.1/24 | GE 0/1/1 | 10.1.5.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign addresses to all physical and loopback interfaces listed in [Table 1](#EN-US_TASK_0172368354__tab_01).
2. Globally enable OSPF on each device so that OSPF advertises segment routes of each physical and loopback interface. Enable OSPF TE in the area where the devices reside.
3. Set MPLS label switching router (LSR) IDs for all devices and globally enable MPLS, TE, RSVP-TE, and CSPF.
4. Enable MPLS, TE, and RSVP-TE on the outbound interfaces of all links along the TE tunnel. Set a TE metric for each link according to [Figure 1](#EN-US_TASK_0172368354__fig_dc_vrp_te-p2p_cfg_017201).
5. Create a tunnel interface on LSRA and specify the IP address, tunnel protocol, destination address, tunnel ID, and signaling protocol RSVP-TE for the tunnel interface.
6. Enable the CR-LSP hot standby function and the disjoint algorithm on the tunnel interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address for each interface (see [Table 1](#EN-US_TASK_0172368354__tab_01).)
* OSPF process ID (1) and area ID (0.0.0.0)
* TE metric for each link (see [Figure 1](#EN-US_TASK_0172368354__fig_dc_vrp_te-p2p_cfg_017201).)
* Loopback interface address for each MPLS LSR ID
* Tunnel interface number (Tunnel1), tunnel ID (1), loopback interface address to be borrowed, destination address (6.6.6.6), and signaling protocol (RSVP-TE)

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface and create a loopback interface on each device, according to [Table 1](#EN-US_TASK_0172368354__tab_01). For configuration details, see [Configuration Files](#EN-US_TASK_0172368354__section_05) in this section.
2. Enable OSPF on each device.
   
   
   
   Enable basic OSPF functions and MPLS TE on each device.
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view
   ```
   ```
   [~LSRA] ospf 1
   ```
   ```
   [*LSRA-ospf-1] opaque-capability enable
   ```
   ```
   [*LSRA-ospf-1] area 0.0.0.0
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] mpls-te enable
   ```
   ```
   [*LSRA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~LSRA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~LSRA-ospf-1] quit
   ```
   
   Repeat this step for LSRB, LSRC, LSRD, LSRE, and LSRF. For configuration details, see [Configuration Files](#EN-US_TASK_0172368354__section_05) in this section.
3. Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
   
   
   
   Enable MPLS, MPLS TE, RSVP-TE, and CSPF on each device. Enable MPLS, TE, and RSVP-TE on the outbound interface of each link. Set a TE metric for each link.
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls lsr-id 1.1.1.1
   ```
   ```
   [*LSRA] mpls
   ```
   ```
   [*LSRA-mpls] mpls te
   ```
   ```
   [*LSRA-mpls] mpls rsvp-te
   ```
   ```
   [*LSRA-mpls] mpls te cspf
   ```
   ```
   [*LSRA-mpls] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls te metric 1
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls rsvp-te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls te metric 10
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRA] commit
   ```
   
   Repeat this step for LSRB, LSRC, LSRD, LSRE, and LSRF. For configuration details, see [Configuration Files](#EN-US_TASK_0172368354__section_05) in this section.
4. Configure an MPLS TE tunnel interface.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] interface tunnel1
   ```
   ```
   [*LSRA-Tunnel1] ip address unnumbered interface LoopBack1
   ```
   ```
   [*LSRA-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*LSRA-Tunnel1] destination 6.6.6.6
   ```
   ```
   [*LSRA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*LSRA-Tunnel1] mpls te signal-protocol rsvp-te
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
5. Configure isolated LSP computation.
   
   
   
   Enable the CR-LSP hot standby function and then the disjoint algorithm on the tunnel interface.
   
   # Configure LSRA.
   
   ```
   [~LSRA-Tunnel1] mpls te backup hot-standby
   ```
   ```
   [*LSRA-Tunnel1] mpls te cspf disjoint
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display mpls te cspf destination 6.6.6.6 computation-mode disjoint** command on LSRA. The command output shows that the primary LSP is LSRA -> LSRC -> LSRE -> LSRF and the hot-standby LSP is LSRA-> LSRB-> LSRD-> LSRF. The two LSPs do not intersect.
   
   ```
   [~LSRA] display mpls te cspf destination 6.6.6.6 computation-mode disjoint
   ```
   ```
   Main path for the given constraints is:
   1.1.1.1                          Include          LSR-ID
   10.1.1.1                         Include 
   10.1.1.2                         Include 
   3.3.3.3                          Include          LSR-ID
   10.1.4.1                         Include 
   10.1.4.2                         Include 
   5.5.5.5                          Include          LSR-ID
   10.1.5.1                         Include 
   10.1.5.2                         Include 
   6.6.6.6                          Include          LSR-ID
   The total metrics of the calculated path is :   16
     
   Hot-standby path for the given constraints is:
   1.1.1.1                          Include          LSR-ID
   10.1.2.1                         Include 
   10.1.2.2                         Include 
   2.2.2.2                          Include          LSR-ID
   10.1.6.1                         Include 
   10.1.6.2                         Include 
   4.4.4.4                          Include          LSR-ID
   10.1.7.1                         Include 
   10.1.7.2                         Include 
   6.6.6.6                          Include          LSR-ID
   Complete disjoint path computed and the total metrics of the calculated path is :   21
   ```
   
   # Run the **display mpls te tunnel-interface Tunnel1** and **display mpls te tunnel path Tunnel1** commands on LSRA to view information about the primary and hot-standby LSPs.
   
   ```
   [~LSRA] display mpls te tunnel-interface Tunnel1
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP                                       
       Traffic Switch      : - 
       Session ID          : 1
       Ingress LSR ID      : 1.1.1.1               Egress LSR ID: 6.6.6.6
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : RSVP
       FTid                : 1
       Tie-Breaking Policy : None                  Metric Type  : None
       Bfd Cap             : None                  
       Reopt               : Disabled              Reopt Freq   : -              
       Inter-area Reopt    : Disabled 
       Auto BW             : Disabled              Threshold    : 0 percent
       Current Collected BW: 0 kbps                Auto BW Freq : 0
       Min BW              : 0 kbps                Max BW       : 0 kbps
       Offload             : Disabled              Offload Freq : - 
       Low Value           : -                     High Value   : - 
       Readjust Value      : - 
       Offload Explicit Path Name: 
       Tunnel Group        : -                                              
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0  
       Primary Tunnel      : -                     Pri Tunn Sum : -              
       Backup Tunnel       : -                                                    
       Group Status        : Up                    Oam Status   : -             
       IPTN InLabel        : -                     Tunnel BFD Status : -                               
       BackUp LSP Type     : Hot-Standby           BestEffort   : Enabled
       Secondary HopLimit  : -
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: -
       Secondary Affinity Prop/Mask: 0x0/0x0
       BestEffort Affinity Prop/Mask: 0x0/0x0  
       IsConfigLspConstraint: -
       Hot-Standby Revertive Mode:  Revertive
       Hot-Standby Overlap-path:  Disabled
       Hot-Standby Switch State:  CLEAR
       Bit Error Detection:  Disabled
       Bit Error Detection Switch Threshold:  -
       Bit Error Detection Resume Threshold:  -
       Ip-Prefix Name    : -
       P2p-Template Name : -
       PCE Delegate      : No            LSP Control Status : Local control
       Path Verification : --
       Entropy Label     : None 
       Auto BW Remain Time : 200 s               Reopt Remain Time  : 100 s
       Metric Inherit IGP : None
       Binding Sid       : -                     Reverse Binding Sid : - 
       Self-Ping         : Disable               Self-Ping Duration : 1800 sec
       FRR Attr Source   : -                     Is FRR degrade down : No
       
       Primary LSP ID      : 1.1.1.1:19
       LSP State           : UP                    LSP Type     : Primary
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       Configured Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 10000           CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Actual Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 10000           CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Explicit Path Name  : -                                Hop Limit: -
       Record Route        : Disabled              Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled 
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : CSPF
       Create Modify LSP Reason: -
       Self-Ping Status    : -
       
       Backup LSP ID       : 1.1.1.9:46945
       IsBestEffortPath    : No
       LSP State           : UP                    LSP Type     : Hot-Standby
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
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
       Explicit Path Name  : -                                Hop Limit: -
       Record Route        : Enabled               Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled
       Reroute Flag        : Enabled
       Pce Flag            : Normal
       Path Setup Type     : CSPF
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   ```
   ```
   [~LSRA] display mpls te tunnel path Tunnel1
   ```
   ```
    Tunnel Interface Name : Tunnel1
    Lsp ID : 1.1.1.1 :1 :2
    Hop Information
     Hop 0   10.1.1.1
     Hop 1   10.1.1.2
     Hop 2   3.3.3.3
     Hop 3   10.1.4.1
     Hop 4   10.1.4.2
     Hop 5   5.5.5.5
     Hop 6   10.1.5.1
     Hop 7   10.1.5.2
     Hop 8   6.6.6.6
     
    Tunnel Interface Name : Tunnel1
    Lsp ID : 1.1.1.1 :1 :3
    Hop Information
     Hop 0   10.1.2.1
     Hop 1   10.1.2.2
     Hop 2   2.2.2.2
     Hop 3   10.1.6.1
     Hop 4   10.1.6.2
     Hop 5   4.4.4.4
     Hop 6   10.1.7.1
     Hop 7   10.1.7.2
     Hop 8   6.6.6.6
   ```
   
   The command outputs show that the computed primary and hot-standby LSPs are the same as the actual primary and hot-standby LSPs, indicating that the device has computed two isolated LSPs.

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #                                         
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 1
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.2.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 10
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #                                                                               
  interface Tunnel1                                                           
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 6.6.6.6
   mpls te signal-protocol rsvp-te
   mpls te backup hot-standby 
   mpls te tunnel-id 1
   mpls te cspf disjoint
  #                                                                               
  ospf 1          
   opaque-capability enable
   area 0.0.0.0   
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    mpls-te enable
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #                                         
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.2.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.6.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 10
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0   
    network 2.2.2.2 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.6.0 0.0.0.255
    mpls-te enable
  #
  return
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.3.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 1
   mpls rsvp-te 
  #
  interface GigabitEthernet0/1/2
   undo shutdown  
   ip address 10.1.4.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 5
   mpls rsvp-te 
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0   
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
    mpls-te enable
  #                                         
  return
  ```
* LSRD configuration file
  
  ```
  #
  sysname LSRD
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #                                         
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.6.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te 
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.3.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te 
  #
  interface GigabitEthernet0/1/2
   undo shutdown  
   ip address 10.1.7.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 1
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0   
    network 4.4.4.4 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.6.0 0.0.0.255
    network 10.1.7.0 0.0.0.255
    mpls-te enable
  #                                         
  return
  ```
* LSRE configuration file
  
  ```
  #
  sysname LSRE
  #
  mpls lsr-id 5.5.5.5
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #                                         
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.4.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.5.1 255.255.255.0
   mpls           
   mpls te        
   mpls te metric 10
   mpls rsvp-te 
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0   
    network 5.5.5.5 0.0.0.0
    network 10.1.4.0 0.0.0.255
    network 10.1.5.0 0.0.0.255
    mpls-te enable
  #                                         
  return
  ```
* LSRF configuration file
  
  ```
  #
  sysname LSRF
  #
  mpls lsr-id 6.6.6.6
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #                                         
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.7.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te 
  #
  interface GigabitEthernet0/1/1
   undo shutdown  
   ip address 10.1.5.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te 
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0   
    network 6.6.6.6 0.0.0.0
    network 10.1.5.0 0.0.0.255
    network 10.1.7.0 0.0.0.255
    mpls-te enable
  #                                         
  return
  ```