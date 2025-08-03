Example for Configuring TI-LFA FRR for a Loose SR-MPLS TE Tunnel
================================================================

Topology-Independent Loop-Free Alternate (TI-LFA) FRR can be configured to enhance the reliability of a Segment Routing (SR) network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0174456730__fig_dc_vrp_sr-be_cfg_000501), IS-IS is enabled. The cost of the link between Device C and Device D is 100, and the cost of other links is 10. Based on node SIDs, an SR-MPLS TE tunnel (DeviceA -> DeviceB -> DeviceE -> DeviceF) is established from DeviceA to DeviceF through static explicit paths.

The SR-MPLS TE tunnel established based on node SIDs is a loose one that supports TI-LFA FRR. TI-LFA FRR can be configured on DeviceB to provide local protection, enabling traffic to be quickly switched to the backup path (DeviceA -> DeviceB -> DeviceC -> DeviceD -> DeviceE -> DeviceF) when the link between DeviceB and DeviceE fails.

**Figure 1** TI-LFA FRR for a loose SR-MPLS TE tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0174505857.png)

#### Precautions

In this example, TI-LFA FRR is configured on DeviceB to protect the link between DeviceB and DeviceE. On a live network, you are advised to configure TI-LFA FRR on all nodes in the SR domain.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS on the entire network to implement interworking between devices.
2. Enable MPLS on the entire network and configure SR.
3. Configure an explicit path on Device A and establish an SR-MPLS TE tunnel.
4. Enable TI-LFA FRR and anti-microloop on Device B.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR ID of each device
* SRGB range of each device

#### Procedure

1. Configure interface IP addresses.
   
   
   
   # Configure Device A.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface loopback 1
   ```
   ```
   [*DeviceA-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   Repeat this step for the other devices. For configuration details, see [Configuration Files](#EN-US_TASK_0174456730__example864047395214048) in this section.
2. Configure an IGP to implement interworking. IS-IS is used as an example.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] cost-style wide
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface loopback 1
   ```
   ```
   [*DeviceA-LoopBack1] isis enable 1
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   Repeat this step for the other devices. For configuration details, see [Configuration Files](#EN-US_TASK_0174456730__example864047395214048) in this section.
   
   Set the cost of the link between DeviceC and DeviceD to 100 to simulate a special network scenario.
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] isis cost 100
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] isis cost 100
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
3. Configure basic MPLS capabilities on the backbone network.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] mpls lsr-id 1.1.1.9
   ```
   ```
   [*DeviceA] mpls
   ```
   ```
   [*DeviceA-mpls] mpls te
   ```
   ```
   [*DeviceA-mpls] commit
   ```
   ```
   [~DeviceA-mpls] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] mpls lsr-id 2.2.2.9
   ```
   ```
   [*DeviceB] mpls
   ```
   ```
   [*DeviceB-mpls] mpls te
   ```
   ```
   [*DeviceB-mpls] commit
   ```
   ```
   [~DeviceB-mpls] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] mpls lsr-id 3.3.3.9
   ```
   ```
   [*DeviceC] mpls
   ```
   ```
   [*DeviceC-mpls] mpls te
   ```
   ```
   [*DeviceC-mpls] commit
   ```
   ```
   [~DeviceC-mpls] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] mpls lsr-id 4.4.4.9
   ```
   ```
   [*DeviceD] mpls
   ```
   ```
   [*DeviceD-mpls] mpls te
   ```
   ```
   [*DeviceD-mpls] commit
   ```
   ```
   [~DeviceD-mpls] quit
   ```
   
   # Configure Device E.
   
   ```
   [~DeviceE] mpls lsr-id 5.5.5.9
   ```
   ```
   [*DeviceE] mpls
   ```
   ```
   [*DeviceE-mpls] mpls te
   ```
   ```
   [*DeviceE-mpls] commit
   ```
   ```
   [~DeviceE-mpls] quit
   ```
   
   # Configure Device F.
   
   ```
   [~DeviceF] mpls lsr-id 6.6.6.9
   ```
   ```
   [*DeviceF] mpls
   ```
   ```
   [*DeviceF-mpls] mpls te
   ```
   ```
   [*DeviceF-mpls] commit
   ```
   ```
   [~DeviceF-mpls] quit
   ```
4. Configure basic SR functions on the backbone network.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] segment-routing
   ```
   ```
   [*DeviceA-segment-routing] quit
   ```
   ```
   [*DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceA-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface loopback 1
   ```
   ```
   [*DeviceA-LoopBack1] isis prefix-sid index 10
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] segment-routing
   ```
   ```
   [*DeviceB-segment-routing] quit
   ```
   ```
   [*DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceB-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface loopback 1
   ```
   ```
   [*DeviceB-LoopBack1] isis prefix-sid index 20
   ```
   ```
   [*DeviceB-LoopBack1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] segment-routing
   ```
   ```
   [*DeviceC-segment-routing] quit
   ```
   ```
   [*DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceC-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface loopback 1
   ```
   ```
   [*DeviceC-LoopBack1] isis prefix-sid index 30
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] segment-routing
   ```
   ```
   [*DeviceD-segment-routing] quit
   ```
   ```
   [*DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceD-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface loopback 1
   ```
   ```
   [*DeviceD-LoopBack1] isis prefix-sid index 40
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
   ```
   [*DeviceD] commit
   ```
   
   # Configure Device E.
   
   ```
   [~DeviceE] segment-routing
   ```
   ```
   [*DeviceE-segment-routing] quit
   ```
   ```
   [*DeviceE] isis 1
   ```
   ```
   [*DeviceE-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceE-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*DeviceE-isis-1] quit
   ```
   ```
   [*DeviceE] interface loopback 1
   ```
   ```
   [*DeviceE-LoopBack1] isis prefix-sid index 50
   ```
   ```
   [*DeviceE-LoopBack1] quit
   ```
   ```
   [*DeviceE] commit
   ```
   
   # Configure Device F.
   
   ```
   [~DeviceF] segment-routing
   ```
   ```
   [*DeviceF-segment-routing] quit
   ```
   ```
   [*DeviceF] isis 1
   ```
   ```
   [*DeviceF-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceF-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*DeviceF-isis-1] quit
   ```
   ```
   [*DeviceF] interface loopback 1
   ```
   ```
   [*DeviceF-LoopBack1] isis prefix-sid index 60
   ```
   ```
   [*DeviceF-LoopBack1] quit
   ```
   ```
   [*DeviceF] commit
   ```
   
   # After completing the configurations, run the **display segment-routing prefix mpls forwarding** command on each device. The command output shows that SR-MPLS BE LSPs have been established. The command output on DeviceA is used as an example.
   
   ```
   [~DeviceA] display segment-routing prefix mpls forwarding
   ```
   ```
                      Segment Routing Prefix MPLS Forwarding Information
                --------------------------------------------------------------
                Role : I-Ingress, T-Transit, E-Egress, I&T-Ingress And Transit
   
   Prefix             Label      OutLabel   Interface         NextHop          Role  MPLSMtu   Mtu     State          
   -----------------------------------------------------------------------------------------------------------------
   1.1.1.9/32         16010      NULL       Loop1             127.0.0.1        E     ---       1500    Active          
   2.2.2.9/32         16020      3          GE0/1/0           10.1.1.2         I&T   ---       1500    Active          
   3.3.3.9/32         16030      16030      GE0/1/0           10.1.1.2         I&T   ---       1500    Active          
   4.4.4.9/32         16040      16040      GE0/1/0           10.1.1.2         I&T   ---       1500    Active          
   5.5.5.9/32         16050      16050      GE0/1/0           10.1.1.2         I&T   ---       1500    Active          
   6.6.6.9/32         16060      16060      GE0/1/0           10.1.1.2         I&T   ---       1500    Active          
   
   Total information(s): 6
   ```
5. Configure an SR-MPLS TE tunnel.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] explicit-path p1
   ```
   ```
   [*DeviceA-explicit-path-p1] next sid label 16020 type prefix
   ```
   ```
   [*DeviceA-explicit-path-p1] next sid label 16050 type prefix
   ```
   ```
   [*DeviceA-explicit-path-p1] next sid label 16060 type prefix
   ```
   ```
   [*DeviceA-explicit-path-p1] quit
   ```
   ```
   [*DeviceA] interface tunnel1
   ```
   ```
   [*DeviceA-Tunnel1] ip address unnumbered interface LoopBack1
   ```
   ```
   [*DeviceA-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*DeviceA-Tunnel1] destination 6.6.6.9
   ```
   ```
   [*DeviceA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*DeviceA-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*DeviceA-Tunnel1] mpls te path explicit-path p1
   ```
   ```
   [*DeviceA-Tunnel1] commit
   ```
   ```
   [~DeviceA-Tunnel1] quit
   ```
   
   # After completing the configurations, run the **display mpls te tunnel destination** command on Device A. The command output shows that the SR-MPLS TE tunnel has been established.
   
   ```
   [~DeviceA] display mpls te tunnel destination 6.6.6.9
   ```
   ```
   * means the LSP is detour LSP
   -------------------------------------------------------------------------------
   Ingress LsrId   Destination     LSPID In/OutLabel     R Tunnel-name
   -------------------------------------------------------------------------------
   1.1.1.9         6.6.6.9         5     -/16020         I Tunnel1
   -------------------------------------------------------------------------------
   R: Role, I: Ingress, T: Transit, E: Egress
   ```
   
   # Run the **display mpls te tunnel-interface** command on Device A. The command output shows information about the SR-MPLS TE tunnel.
   
   ```
   [~DeviceA] display mpls te tunnel-interface Tunnel 1
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP
       Traffic Switch      : - 
       Session ID          : 1
       Ingress LSR ID      : 1.1.1.9               Egress LSR ID: 6.6.6.9
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : Segment-Routing
       FTid                : 8193
       Tie-Breaking Policy : None                  Metric Type  : TE
       Bfd Cap             : None                  
       Reopt               : Disabled              Reopt Freq   : -   
       Inter-area Reopt    : Disabled             
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
       Metric Inherit IGP : None
       Binding Sid       : -                     Reverse Binding Sid : - 
       FRR Attr Source   : -                     Is FRR degrade down : -
       Color             : - 
       
       Primary LSP ID      : 1.1.1.9:5
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
       Explicit Path Name  : p1                               Hop Limit: -
       Record Route        : -                            Record Label : -
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
6. Configure TI-LFA FRR.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [~DeviceB-isis-1] avoid-microloop frr-protected
   ```
   ```
   [*DeviceB-isis-1] avoid-microloop frr-protected rib-update-delay 5000
   ```
   ```
   [*DeviceB-isis-1] avoid-microloop segment-routing
   ```
   ```
   [*DeviceB-isis-1] avoid-microloop segment-routing rib-update-delay 10000
   ```
   ```
   [*DeviceB-isis-1] frr
   ```
   ```
   [*DeviceB-isis-1-frr] loop-free-alternate level-1
   ```
   ```
   [*DeviceB-isis-1-frr] ti-lfa level-1
   ```
   ```
   [*DeviceB-isis-1-frr] quit
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   After completing the configurations, run the [**display isis route**](cmdqueryname=display+isis+route) [ **level-1** | **level-2** ] [ *process-id* ] [ **verbose** ] command on Device B. The command output shows IS-IS TI-LFA FRR backup entries.
   
   ```
   [~DeviceB] display isis route level-1 verbose
   ```
   ```
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
   
    IPV4 Dest  : 1.1.1.9/32         Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 06:02:52
    NextHop    :                    Interface :               ExitIndex :
       10.1.1.1                           GE0/1/0                    0x0000000e
    Prefix-sid : 16010              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.1.1.1                           GE0/1/0                    3
   
    IPV4 Dest  : 2.2.2.9/32         Int. Cost : 0             Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : D/-/L/-
    Priority   : -                  Age       : 06:02:52
    NextHop    :                    Interface :               ExitIndex :
       Direct                             Loop1                      0x00000000
    Prefix-sid : 16020              Weight    : 0             Flags     : -/N/-/-/-/-/A/L
    SR NextHop :                    Interface :               OutLabel  :
       Direct                             Loop1                      -
   
    IPV4 Dest  : 3.3.3.9/32         Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.2.1.2                           GE0/2/0                   0x0000000a
    TI-LFA:        
    Interface  : GE0/3/0 
    NextHop    : 10.5.1.2           LsIndex    : 0x00000002   ProtectType: L
    Backup Label Stack (Top -> Bottom): {16040, 48141}
    Prefix-sid : 16030              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.2.1.2                           GE0/2/0                   3
    TI-LFA:        
    Interface  : GE0/3/0 
    NextHop    : 10.5.1.2           LsIndex    : 0x00000002   ProtectType: L
    Backup Label Stack (Top -> Bottom): {16040, 48141}
   
    IPV4 Dest  : 4.4.4.9/32         Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.5.1.2                           GE0/3/0                    0x00000007
    TI-LFA:        
    Interface  : GE0/2/0 
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: N
    Backup Label Stack (Top -> Bottom): {48142}
    Prefix-sid : 16040              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.5.1.2                           GE0/3/0                    16040
    TI-LFA:        
    Interface  : GE0/2/0                                                             
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: N
    Backup Label Stack (Top -> Bottom): {48142}
   
    IPV4 Dest  : 5.5.5.9/32         Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.5.1.2                           GE0/3/0                    0x00000007
    TI-LFA:        
    Interface  : GE0/2/0                                                              
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
    Prefix-sid : 16050              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.5.1.2                           GE0/3/0                    3
    TI-LFA:        
    Interface  : GE0/2/0                                                              
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
   
    IPV4 Dest  : 6.6.6.9/32         Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.5.1.2                           GE0/3/0                    0x00000007
    TI-LFA:        
    Interface  : GE0/2/0                                                             
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
    Prefix-sid : 16060              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.5.1.2                           GE0/3/0                    16060
    TI-LFA:        
    Interface  : GE0/2/0                                                              
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
   
    IPV4 Dest  : 10.1.1.0/24        Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : D/-/L/-
    Priority   : -                  Age       : 06:02:52
    NextHop    :                    Interface :               ExitIndex :
       Direct                             GE0/1/0                    0x00000000
   
    IPV4 Dest  : 10.2.1.0/24        Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : D/-/L/-
    Priority   : -                  Age       : 06:02:52
    NextHop    :                    Interface :               ExitIndex :
       Direct                             GE0/2/0                   0x00000000
   
    IPV4 Dest  : 10.3.1.0/24        Int. Cost : 110           Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : A/-/-/-
    Priority   : Low                Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.2.1.2                           GE0/2/0                   0x0000000a
    TI-LFA:        
    Interface  : GE0/3/0                                                              
    NextHop    : 10.5.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {}
   
    IPV4 Dest  : 10.4.1.0/24        Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : A/-/-/-
    Priority   : Low                Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.5.1.2                           GE0/3/0                    0x00000007
    TI-LFA:        
    Interface  : GE0/2/0                                                            
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
   
    IPV4 Dest  : 10.5.1.0/24        Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : D/-/L/-
    Priority   : -                  Age       : 00:03:44
    NextHop    :                    Interface :               ExitIndex :
       Direct                             GE0/3/0                    0x00000000
   
    IPV4 Dest  : 10.6.1.0/24        Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : A/-/-/-
    Priority   : Low                Age       : 00:03:21
    NextHop    :                    Interface :               ExitIndex :
       10.5.1.2                           GE0/3/0                    0x00000007
    TI-LFA:        
    Interface  : GE0/2/0                                                              
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
7. Verify the configuration.
   
   
   
   # Run a tracert command on Device A to check the connectivity of the SR-MPLS TE tunnel to Device F. For example:
   
   ```
   [~DeviceA] tracert lsp segment-routing te Tunnel 1
   ```
   ```
     LSP Trace Route FEC: SEGMENT ROUTING TE TUNNEL IPV4 SESSION QUERY Tunnel1 , press CTRL_C to break.
     TTL    Replier            Time    Type      Downstream
     0                                 Ingress   10.1.1.2/[16050 16060 ]
     1      10.1.1.2           2 ms    Transit   10.5.1.2/[3 ]
     2      10.5.1.2           3 ms    Transit   10.6.1.2/[3 ]
     3      6.6.6.9            3 ms    Egress 
   ```
   
   # Run the **shutdown** command on GE 0/3/0 of DeviceB to simulate a link fault between DeviceB and DeviceE.
   
   ```
   [~DeviceB] interface gigabitethernet0/3/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Run the tracert command on DeviceA again to check the connectivity of the SR-MPLS TE tunnel. For example:
   
   ```
   [~DeviceA] tracert lsp segment-routing te Tunnel 1
   ```
   ```
     LSP Trace Route FEC: SEGMENT ROUTING TE TUNNEL IPV4 SESSION QUERY Tunnel1 , press CTRL_C to break.
     TTL    Replier            Time    Type      Downstream
     0                                 Ingress   10.1.1.2/[16050 16060 ]
     1      10.1.1.2           3 ms    Transit   10.2.1.2/[16050 ]
     2      10.2.1.2           4 ms    Transit   10.3.1.2/[16050 ]
     3      10.3.1.2           4 ms    Transit   10.4.1.2/[3 ]
     4      10.4.1.2           3 ms    Transit   10.6.1.2/[3 ]
     5      6.6.6.9            5 ms    Egress 
   ```
   
   The preceding command output shows that the SR-MPLS TE tunnel has been switched to the TI-LFA FRR backup path.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls
   mpls te 
  #
  explicit-path p1
   next sid label 16020 type prefix index 1
   next sid label 16050 type prefix index 2
   next sid label 16060 type prefix index 3
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 10
  #               
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 6.6.6.9
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path p1 
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  mpls lsr-id 2.2.2.9
  #               
  mpls  
   mpls te          
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   avoid-microloop frr-protected
   avoid-microloop frr-protected rib-update-delay 5000
   segment-routing mpls
   segment-routing global-block 16000 23999
   avoid-microloop segment-routing
   avoid-microloop segment-routing rib-update-delay 10000
   frr
    loop-free-alternate level-1
    ti-lfa level-1
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
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.5.1.1 255.255.255.0
   isis enable 1 
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 20
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  mpls lsr-id 3.3.3.9
  #               
  mpls  
   mpls te          
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.2.1.2 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.3.1.1 255.255.255.0
   isis enable 1 
   isis cost 100
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 30
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  mpls lsr-id 4.4.4.9
  #               
  mpls  
   mpls te          
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.3.1.2 255.255.255.0
   isis enable 1  
   isis cost 100
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.4.1.1 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 40
  #
  return
  ```
* Device E configuration file
  
  ```
  #
  sysname DeviceE
  #
  mpls lsr-id 5.5.5.9
  #               
  mpls  
   mpls te          
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0005.00
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.6.1.1 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.4.1.2 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.5.1.2 255.255.255.0
   isis enable 1 
  #               
  interface LoopBack1
   ip address 5.5.5.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 50
  #
  return
  ```
* Device F configuration file
  
  ```
  #
  sysname DeviceF
  #
  mpls lsr-id 6.6.6.9
  #               
  mpls     
   mpls te       
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0006.00
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.6.1.2 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 6.6.6.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 60
  #
  return
  ```