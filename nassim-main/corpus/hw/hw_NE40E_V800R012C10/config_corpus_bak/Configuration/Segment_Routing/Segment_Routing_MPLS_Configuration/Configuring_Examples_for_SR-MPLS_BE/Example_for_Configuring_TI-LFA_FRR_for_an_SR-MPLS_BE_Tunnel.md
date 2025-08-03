Example for Configuring TI-LFA FRR for an SR-MPLS BE Tunnel
===========================================================

Topology-Independent Loop-Free Alternate (TI-LFA) FRR can be configured to enhance the reliability of an SR network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0174456729__fig19698696594), IS-IS is enabled, and the SR-MPLS BE function is configured. The cost of the link between Device C and Device D is 100, and the cost of other links is 10. The optimal path from Device A to Device F is Device A -> Device B -> Device E -> Device F. TI-LFA FRR can be configured on Device B to provide local protection, enabling traffic to be quickly switched to the backup path (Device A -> Device B -> Device C -> Device D -> Device E -> Device F) when the link between Device B and Device E fails.

**Figure 1** Configuring TI-LFA FRR for an SR-MPLS BE tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0000001418949325.png "Click to enlarge")

#### Precautions

In this example, TI-LFA FRR is configured on DeviceB to protect the link between DeviceB and DeviceE. On a live network, you are advised to configure TI-LFA FRR on all nodes in the SR domain.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS on the entire network to implement interworking between devices.
2. Enable MPLS on the entire network, configure SR, and establish an SR-MPLS BE tunnel.
3. Enable TI-LFA FRR and anti-microloop on Device B.

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
   
   Repeat this step for the other devices. For configuration details, see [Configuration Files](#EN-US_TASK_0174456729__example864047395214048) in this section.
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
   
   Repeat this step for the other devices. For configuration details, see [Configuration Files](#EN-US_TASK_0174456729__example864047395214048) in this section.
   
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
3. Configure basic MPLS functions on the backbone network.
   
   
   
   Because MPLS is automatically enabled on the interface where IS-IS has been enabled, you can ignore MPLS configuration on such an interface.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] mpls lsr-id 1.1.1.9
   ```
   ```
   [*DeviceA] mpls
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
   [*DeviceF-mpls] commit
   ```
   ```
   [~DeviceF-mpls] quit
   ```
4. Configure SR on the backbone network and establish an SR-MPLS BE tunnel.
   
   
   
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
   
   # After completing the configurations, run the **display segment-routing prefix mpls forwarding** command on each device. The command output shows that SR-MPLS BE label forwarding paths have been established. The following example uses the command output on Device A.
   
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
5. Configure TI-LFA FRR.
   
   
   
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
    Priority   : Medium             Age       : 04:35:30
    NextHop    :                    Interface :               ExitIndex :
       10.1.1.1                           GE0/1/0                    0x0000000e
    Prefix-sid : 16010              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.1.1.1                           GE0/1/0                    3
   
    IPV4 Dest  : 2.2.2.9/32         Int. Cost : 0             Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : D/-/L/-
    Priority   : -                  Age       : 04:35:30
    NextHop    :                    Interface :               ExitIndex :
       Direct                             Loop1                      0x00000000
    Prefix-sid : 16020              Weight    : 0             Flags     : -/N/-/-/-/-/A/L
    SR NextHop :                    Interface :               OutLabel  :
       Direct                             Loop1                      -
   
    IPV4 Dest  : 3.3.3.9/32         Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 04:09:15
    NextHop    :                    Interface :               ExitIndex :
       10.2.1.2                           GE0/2/0                     0x0000000a
    TI-LFA:        
    Interface  : GE0/3/0                                                              
    NextHop    : 10.5.1.2           LsIndex    : 0x00000002   ProtectType: L
    Backup Label Stack (Top -> Bottom): {16040, 48141}
    Prefix-sid : 16030              Weight    : 0             Flags     : -/N/-/-/-/-/A/-
    SR NextHop :                    Interface :               OutLabel  :
       10.2.1.2                           GE0/2/0                    3
    TI-LFA:        
    Interface  : GE0/3/0                                                              
    NextHop    : 10.5.1.2           LsIndex    : 0x00000002   ProtectType: L
    Backup Label Stack (Top -> Bottom): {16040, 48141}
   
    IPV4 Dest  : 4.4.4.9/32         Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/-/-
    Priority   : Medium             Age       : 04:09:15
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
    Priority   : Medium             Age       : 04:09:15
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
    Priority   : Medium             Age       : 04:09:15
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
    Priority   : -                  Age       : 04:35:30
    NextHop    :                    Interface :               ExitIndex :
       Direct                             GE0/1/0                    0x00000000
   
    IPV4 Dest  : 10.2.1.0/24        Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : D/-/L/-
    Priority   : -                  Age       : 04:35:30
    NextHop    :                    Interface :               ExitIndex :
       Direct                             GE0/2/0                    0x00000000
   
    IPV4 Dest  : 10.3.1.0/24        Int. Cost : 110           Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : A/-/-/-
    Priority   : Low                Age       : 04:09:15
    NextHop    :                    Interface :               ExitIndex :
       10.2.1.2                           GE0/2/0                    0x0000000a
    TI-LFA:        
    Interface  : GE0/3/0                                                            
    NextHop    : 10.5.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {}
   
    IPV4 Dest  : 10.4.1.0/24        Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : A/-/-/-
    Priority   : Low                Age       : 04:09:15
    NextHop    :                    Interface :               ExitIndex :
       10.5.1.2                           GE0/3/0                    0x00000007
    TI-LFA:        
    Interface  : GE0/2/0                                                               
    NextHop    : 10.2.1.2           LsIndex    : 0x00000003   ProtectType: L
    Backup Label Stack (Top -> Bottom): {48142}
   
    IPV4 Dest  : 10.5.1.0/24        Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : D/-/L/-
    Priority   : -                  Age       : 04:09:37
    NextHop    :                    Interface :               ExitIndex :
       Direct                             GE0/3/0                    0x00000000
   
    IPV4 Dest  : 10.6.1.0/24        Int. Cost : 20            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 2             Flags     : A/-/-/-
    Priority   : Low                Age       : 04:09:15
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
6. Verify the configuration.
   
   
   
   # Run a tracert command on Device A to check the connectivity of the SR-MPLS BE tunnel to Device F. For example:
   
   ```
   [~DeviceA] tracert lsp segment-routing ip 6.6.6.9 32 version draft2
   ```
   ```
     LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 6.6.6.9/32 , press CTRL_C to break.
     TTL    Replier            Time    Type      Downstream
     0                                 Ingress   10.1.1.2/[16060 ]
     1      10.1.1.2           291 ms  Transit   10.5.1.2/[16060 ]
     2      10.5.1.2           10 ms   Transit   10.6.1.2/[3 ]
     3      6.6.6.9            11 ms   Egress
   ```
   
   # Run the **shutdown** command on GE 0/3/0 of Device B to simulate a link fault between Device B and Device E.
   
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
   
   # Run the tracert command on Device A again to check the connectivity of the SR-MPLS BE tunnel. For example:
   
   ```
   [~DeviceA] tracert lsp segment-routing ip 6.6.6.9 32 version draft2
   ```
   ```
     LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 6.6.6.9/32 , press CTRL_C to break.
     TTL    Replier            Time    Type      Downstream
     0                                 Ingress   10.1.1.2/[16060 ]
     1      10.1.1.2           3 ms    Transit   10.2.1.2/[16060 ]
     2      10.2.1.2           46 ms   Transit   10.3.1.2/[16060 ]
     3      10.3.1.2           33 ms   Transit   10.4.1.2/[16060 ]
     4      10.4.1.2           48 ms   Transit   10.6.1.2/[3 ]
     5      6.6.6.9            4 ms    Egress
   ```
   
   The preceding command output shows that the SR-MPLS BE tunnel has been switched to the TI-LFA FRR backup path.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls            
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