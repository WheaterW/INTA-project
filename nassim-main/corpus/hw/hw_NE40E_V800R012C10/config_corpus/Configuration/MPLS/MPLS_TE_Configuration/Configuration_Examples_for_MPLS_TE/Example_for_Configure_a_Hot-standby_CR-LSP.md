Example for Configure a Hot-standby CR-LSP
==========================================

Example for Configure a Hot-standby CR-LSP

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172368348__fig_dc_vrp_te-p2p_cfg_010901) illustrates an MPLS VPN network. A TE tunnel is established from PE1 to PE2. A hot-standby CR-LSP and a best-effort path are configured. The networking is as follows:

* The primary CR-LSP is along the path PE1 -> P1 -> PE2.
* The hot-standby CR-LSP is along the path PE1 -> P2 -> PE2.

If the primary CR-LSP fails, traffic switches to the backup CR-LSP. After the primary CR-LSP recovers, traffic switches back to the primary CR-LSP after a 15-second delay. If both the primary and backup CR-LSPs fail, traffic switches to the best-effort path. Explicit paths can be configured for the primary and backup CR-LSPs. A best-effort path can be generated automatically. In this example, the best-effort path is PE1 -> P2 -> P1 -> PE2. The calculated best-effort path varies according to the faulty node.

**Figure 1** Networking diagram for a hot-standby CR-LSP![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_010901.png)  


#### Precautions

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to every interface and configure an IGP to implement connectivity.
2. Configure basic MPLS and MPLS TE functions.
3. Configure explicit paths on PE1 for the primary and hot-standby CR-LSPs.
4. Create a tunnel destined for PE2; specify explicit paths; enable hot standby; configure a best-effort path; set the switchback delay time to 15 seconds on PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* IGP type and data
* MPLS LSR IDs
* Tunnel interface number and bandwidth
* Explicit paths for the primary and hot-standby CR-LSPs

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address and its mask to every interface and configure a loopback interface address as an LSR ID on every node. For configuration details, see [Configuration Files](#EN-US_TASK_0172368348__section_dc_vrp_te-p2p_cfg_010905) in this section.
2. Configure an IGP.
   
   
   
   Configure OSPF or IS-IS on every node to implement connectivity between them. IS-IS is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0172368348__section_dc_vrp_te-p2p_cfg_010905) in this section.
3. Configure basic MPLS functions.
   
   
   
   Configure the LSR ID and enable MPLS in the system and interface views on each node. For configuration details, see [Configuration Files](#EN-US_TASK_0172368348__section_dc_vrp_te-p2p_cfg_010905) in this section.
4. Configure basic MPLS TE functions.
   
   
   
   Enable MPLS TE and RSVP-TE in the MPLS and interface views on every node. For configuration details, see [Configuration Files](#EN-US_TASK_0172368348__section_dc_vrp_te-p2p_cfg_010905) in this section.
5. Configure IS-IS TE and CSPF.
   
   
   
   Configure IS-IS TE on all nodes and enable CSPF on PE1. For configuration details, see [Configuring an RSVP-TE Tunnel](dc_vrp_te-p2p_cfg_0094.html).
6. Configure explicit paths for the primary and hot-standby CR-LSPs.
   
   
   
   # Configure an explicit path for the primary CR-LSP on PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] explicit-path main
   ```
   ```
   [*PE1-explicit-path-main] next hop 10.4.1.2
   ```
   ```
   [*PE1-explicit-path-main] next hop 10.2.1.2
   ```
   ```
   [*PE1-explicit-path-main] next hop 3.3.3.3
   ```
   ```
   [*PE1-explicit-path-main] quit
   ```
   
   # Configure an explicit path for the hot-standby CR-LSP on PE1.
   
   ```
   [*PE1] explicit-path backup
   ```
   ```
   [*PE1-explicit-path-backup] next hop 10.3.1.2
   ```
   ```
   [*PE1-explicit-path-backup] next hop 10.5.1.2
   ```
   ```
   [*PE1-explicit-path-backup] next hop 3.3.3.3
   ```
   ```
   [*PE1-explicit-path-backup] commit
   ```
   ```
   [~PE1-explicit-path-backup] quit
   ```
   
   # After completing the configurations, run the **display explicit-path main** command on PE1. Information about the explicit paths for the primary and hot-standby CR-LSPs is displayed.
   
   ```
   [~PE1] display explicit-path main
   ```
   ```
   Path Name : main        Path Status : Enabled
   ```
   ```
    1      10.4.1.2          Strict      Include
   ```
   ```
    2      10.2.1.2          Strict      Include
   ```
   ```
    3      3.3.3.3           Strict      Include
   ```
   ```
   [~PE1] display explicit-path backup
   ```
   ```
   Path Name : backup      Path Status : Enabled
   ```
   ```
    1      10.3.1.2          Strict      Include
   ```
   ```
    2      10.5.1.2          Strict      Include
   ```
   ```
    3      3.3.3.3           Strict      Include
   ```
7. Configure tunnel interfaces.
   
   
   
   # Create a tunnel interface on PE1 and specify an explicit path on PE1.
   
   ```
   [~PE1] interface tunnel1
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
   [*PE1-Tunnel1] mpls te tunnel-id 502
   ```
   ```
   [*PE1-Tunnel1] mpls te path explicit-path main
   ```
   
   # Configure hot standby on the tunnel interface; set the switchback delay time to 15 seconds; specify an explicit path; configure a best-effort path.
   
   ```
   [*PE1-Tunnel1] mpls te backup hot-standby mode revertive wtr 15
   ```
   ```
   [*PE1-Tunnel1] mpls te path explicit-path backup secondary
   ```
   ```
   [*PE1-Tunnel1] mpls te backup ordinary best-effort
   ```
   ```
   [*PE1-Tunnel1] commit
   ```
   ```
   [~PE1-Tunnel1] quit
   ```
   
   After completing the configurations, run the **display mpls te tunnel-interface tunnel1** command on PE1. Both the primary and hot-standby CR-LSPs have been established.
   
   ```
   [~PE1] display mpls te tunnel-interface tunnel1
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : Primary CR-LSP Up and HotBackup CR-LSP Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP                                       
       Traffic Switch      : - 
       Session ID          : 502
       Ingress LSR ID      : 4.4.4.4               Egress LSR ID: 3.3.3.3
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : RSVP
       FTid                : 161
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
       Offload Explicit Path Name: -
       Tunnel Group        : -                                              
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0  
       Primary Tunnel      : -                     Pri Tunn Sum : -              
       Backup Tunnel       : -                                                    
       Group Status        : -                     Oam Status   : -             
       IPTN InLabel        : -                     Tunnel BFD Status : - 
       BackUp LSP Type     : Hot-Standby           BestEffort   : Enabled
       Secondary HopLimit  : 32
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: backup
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
       PCE Delegate      : No                    LSP Control Status : Local control
       Path Verification : --
       Entropy Label     : None 
       Associated Tunnel Group ID: -             Associated Tunnel Group Type: -
       Auto BW Remain Time : 200 s               Reopt Remain Time  : 100 s
       Metric Inherit IGP : None
       Binding Sid       : -                     Reverse Binding Sid : -
       Self-Ping         : Disable               Self-Ping Duration : 1800 sec
       FRR Attr Source   : -                     Is FRR degrade down : -
   
       Primary LSP ID      : 4.4.4.4:424
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
       Explicit Path Name  : main                             Hop Limit: 32
       Record Route        : Enabled               Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   
       Backup LSP ID       : 4.4.4.4:423
       IsBestEffortPath    : No
       LSP State           : UP                    LSP Type     : Hot-Standby
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
       Explicit Path Name  : backup                           Hop Limit: 32
       Record Route        : Enabled               Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   ```
   
   # Run the following command to check hot standby information.
   
   ```
   [~PE1] display mpls te hot-standby state interface Tunnel1
   ```
   ```
   ----------------------------------------------------------------
   Verbose information about the Tunnel1 hot-standby state
   ----------------------------------------------------------------
       Tunnel Name           : Tunnel1
       Session ID            : 502
       Main LSP index        : 0xC1
       Hot-Standby LSP index : 0xE1
       HSB switch result     : main LSP
       HSB switch reason     : -
       WTR config time       : 15 s
       WTR remain time       : -
       Using overlapped path : no 
       Fast switch status    : no
   ```
   # Run the **ping lsp te** command. The hot-standby CR-LSP is reachable.
   ```
   [~PE1] ping lsp te tunnel1 hot-standby
   ```
   ```
     LSP PING FEC: RSVP IPV4 SESSION QUERY Tunnel1 : 100  data bytes, press CTRL_C to break
     Reply from 3.3.3.3: bytes=100 Sequence=1 time = 4 ms
     Reply from 3.3.3.3: bytes=100 Sequence=2 time = 3 ms
     Reply from 3.3.3.3: bytes=100 Sequence=3 time = 3 ms
     Reply from 3.3.3.3: bytes=100 Sequence=4 time = 3 ms
     Reply from 3.3.3.3: bytes=100 Sequence=5 time = 6 ms
     --- FEC: RSVP IPV4 SESSION QUERY Tunnel1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 3/3/6 ms
   ```
   
   # Run the **tracert lsp te** command to check path of a hot-standby CR-LSP.
   ```
   [~PE1] tracert lsp te tunnel1 hot-standby
     LSP Trace Route FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel1 , press CTRL_C to break.
     TTL   Replier            Time    Type      Downstream
     0                                Ingress   10.3.1.2/[13313 ]
     1     10.3.1.2           90 ms   Transit   10.5.1.2/[3 ]
     2     3.3.3.3            130 ms  Egress
   ```
8. Verify the configuration.
   
   
   
   Connect port 1 and port 2 on a tester to PE1 and PE2, respectively. Set correct label values. Inject MPLS traffic from port 1 to port 2. After the cable is removed from GE 0/2/0 on PE1 or GE 0/2/0 on P1, traffic is restored within milliseconds. Run the **display mpls te hot-standby state interface tunnel1** command on PE1. Traffic has switched to the hot-standby CR-LSP.
   
   ```
   [~PE1] display mpls te hot-standby state interface tunnel1
   ```
   ```
   ----------------------------------------------------------------
   Verbose information about the Tunnel1 hot-standby state
   ----------------------------------------------------------------
       Tunnel Name           : Tunnel1
       Session ID            : 502
       Main LSP index        : 0x0
       Hot-Standby LSP index : 0xE1
       HSB switch result     : hot-standby LSP
       HSB switch reason     : signal fail
       WTR config time       : 10 s
       WTR remain time       : -
       Using overlapped path : no 
       Fast switch status    : no
   ```
   
   Insert the cable into GE 0/2/0 and wait 15 seconds. It can be seen that traffic switches back to the primary CR-LSP.
   
   If the cables to GE 0/2/0 on PE1 (or GE 0/2/0 on P1) and PE2 (or P2) are removed, the tunnel interface goes Down and then Up. A best-effort path is established and takes over traffic.
   
   ```
   [~PE1] display mpls te tunnel-interface tunnel1
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : Backup CR-LSP In use and Primary CR-LSP setting Up
       Tunnel Attributes   :     
       Active LSP          : BestEffort LSP                                       
       Traffic Switch      : - 
       Session ID          : 502
       Ingress LSR ID      : 4.4.4.4               Egress LSR ID: 3.3.3.3
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : RSVP
       FTid                : 161
       Tie-Breaking Policy : None                  Metric Type  : None
       Bfd Cap             : None                  
       Reopt               : Disabled              Reopt Freq   : -
       Inter-area Reopt    : Disabled              
       Auto BW             : Disabled              Threshold    : 0 percent
       Current Collected BW: 0 kbps                Auto BW Freq : 0
       Min BW              : 0 kbps                Max BW       : 0 kbps
       Offload             : Disabled              Offload Freq : 0 sec
       Low Value           : 0 kbps                High Value   : 0 kbps
       Readjust Value      : 0 kbps
       Offload Explicit Path Name: -
       Tunnel Group        : -                                              
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0  
       Primary Tunnel      : -                     Pri Tunn Sum : -              
       Backup Tunnel       : -                                                    
       Group Status        : -                     Oam Status   : -             
       IPTN InLabel        : -                     Tunnel BFD Status : -
       BackUp LSP Type     : BestEffort            BestEffort   : Enabled
       Secondary HopLimit  : 32
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: backup
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
       PCE Delegate      : No                    LSP Control Status : Local control
       Path Verification : --
       Entropy Label     : None 
       Associated Tunnel Group ID: -             Associated Tunnel Group Type: -
       Auto BW Remain Time : 200 s               Reopt Remain Time  : 100 s
       Metric Inherit IGP : None
       Binding Sid       : -                     Reverse Binding Sid : -
       Self-Ping         : Disable               Self-Ping Duration : 1800 sec
       FRR Attr Source   : -                     Is FRR degrade down : No
       
       Primary LSP ID      : 4.4.4.4:436
       LSP State           : DOWN                  LSP Type     : Primary
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
       Explicit Path Name  : main                             Hop Limit: 32
       Record Route        : Enabled               Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   
       Backup LSP ID       : 4.4.4.4:440
       IsBestEffortPath    : No
       LSP State           : DOWN                  LSP Type     : Hot-Standby
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
       Explicit Path Name  : backup                           Hop Limit: 32
       Record Route        : Enabled               Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   
       Backup LSP ID       : 4.4.4.4:439
       IsBestEffortPath    : Yes
       LSP State           : UP                    LSP Type     : BestEffort
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
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : CSPF
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   ```
   ```
   [~PE1] display mpls te tunnel path
   ```
   ```
    Tunnel Interface Name : Tunnel1
    Lsp ID : 4.4.4.4 :502 :32776
    Hop Information
     Hop 0   10.3.1.1
     Hop 1   10.3.1.2
     Hop 2   2.2.2.2
     Hop 3   10.1.1.2
     Hop 4   10.1.1.1
     Hop 5   1.1.1.1
     Hop 6   10.2.1.1
     Hop 7   10.2.1.2
     Hop 8   3.3.3.3
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  ```
  ```
  sysname PE1
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te cspf
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  explicit-path backup
  ```
  ```
   next hop 10.3.1.2
  ```
  ```
   next hop 10.5.1.2
  ```
  ```
   next hop 3.3.3.3
  ```
  ```
  #
  ```
  ```
  explicit-path main
  ```
  ```
   next hop 10.4.1.2
  ```
  ```
   next hop 10.2.1.2
  ```
  ```
   next hop 3.3.3.3
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1-2
  ```
  ```
   network-entity 10.0000.0000.0004.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.1 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 4.4.4.4 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Tunnel1
  ```
  ```
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te record-route      
   mpls te backup ordinary best-effort                                                                                                       
   mpls te backup hot-standby mode revertive wtr 15                                              
   mpls te tunnel-id 502                                           
   mpls te path explicit-path main                                                
   mpls te path explicit-path backup secondary                                    
  ```
  ```
  #
  ```
  ```
  return
  ```
* P1 configuration file
  
  ```
  #
  ```
  ```
  sysname P1
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1-2
  ```
  ```
   network-entity 10.0000.0000.0001.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.2 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   isis enable 1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* P2 configuration file
  
  ```
  #
  ```
  ```
  sysname P2
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1-2
  ```
  ```
   network-entity 10.0000.0000.0002.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.5.1.1 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.2 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
  sysname PE2
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1-2
  ```
  ```
   network-entity 10.0000.0000.0003.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.2 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.5.1.2 255.255.255.252
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.3 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```