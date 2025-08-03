Example for Configuring IS-IS SR-MPLS BE over GRE
=================================================

This section provides an example for configuring IS-IS SR-MPLS BE over GRE, which involves enabling IS-IS on each device, specifying network segments in different processes, configuring GRE tunnels, and enabling IS-IS SR-MPLS BE over GRE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001478015170__fig127031455165813), enable IS-IS and configure SR-MPLS BE. In addition, set the cost of the GRE tunnel between DeviceA and DeviceB to 100 and that of the other links to 10. The optimal path from DeviceA to DeviceD is DeviceA â DeviceD. Configure TI-LFA FRR on DeviceA to implement local protection. In this way, if the link between DeviceA and DeviceD fails, traffic can be rapidly switched to the backup path DeviceA â DeviceB â DeviceC â DeviceD. The traffic between DeviceA and DeviceB is forwarded over a GRE tunnel, which is bound to the link DeviceA â DeviceE â DeviceF â DeviceB.

**Figure 1** Configuring IS-IS SR-MPLS BE over GRE![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001478174794.png "Click to enlarge")

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS on the entire network to implement interworking between devices.
2. Configure SR and establish an SR-MPLS BE tunnel.
3. Establish a GRE tunnel between DeviceA and DeviceB and bind the tunnel to the other process.
4. Set costs for links to ensure that the link DeviceA â DeviceD is preferentially used for traffic forwarding.
5. Configure TI-LFA FRR.
6. Configure IS-IS SR-MPLS BE over GRE.

#### Data Preparation

To complete the configuration, you need the following data:

* DeviceA: subnets 10.1.1.0/24 and 10.7.1.0/24 for IS-IS process 1 and subnet 10.2.1.0/24 for IS-IS process 2
* DeviceB: subnets 10.6.1.0/24 and 10.7.1.0/24 for IS-IS process 1 and subnet 10.4.1.0/24 for IS-IS process 2
* DeviceC: subnets 10.6.1.0/24 and 10.5.1.0/24 for IS-IS process 1
* DeviceD: subnets 10.1.1.0/24 and 10.5.1.0/24 for IS-IS process 1
* DeviceE: subnets 10.2.1.0/24 and 10.3.1.0/24 for IS-IS process 2
* DeviceF: subnets 10.3.1.0/24 and 10.4.1.0/24 for IS-IS process 2

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
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
   [~DeviceA] interface loopback 0
   ```
   ```
   [*DeviceA-LoopBack0] ip address 2.2.2.9 32
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configurations of other devices are similar to the configuration of DeviceA. For configuration details, see the configuration files.
2. Configure IS-IS to implement interworking.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1 
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] isis 2 
   ```
   ```
   [*DeviceA-isis-2] network-entity 11.0000.0000.0021.00
   ```
   ```
   [*DeviceA-isis-2] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis enable 2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configurations of other devices are similar to the configuration of DeviceA. For configuration details, see the configuration files.
3. Configure SR and establish an SR-MPLS BE tunnel.
   
   
   
   # Configure DeviceA.
   
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
   [*DeviceA-isis-1] cost-style wide
   ```
   ```
   [*DeviceA-isis-1] segment-routing mpls
   ```
   ```
   [*DeviceA-isis-1] segment-routing global-block 16000 16999 
   ```
   ```
   [*DeviceA-isis-1] quit 
   ```
   ```
   [*DeviceA] interface LoopBack0
   ```
   ```
   [*DeviceA-LoopBack0] isis enable 1
   ```
   ```
   [*DeviceA-LoopBack0] isis prefix-sid index 100
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For configuration details, see the configuration files.
   
   # After completing the configuration, run the **display segment-routing prefix mpls forwarding** command on each device. The command output shows that SR-MPLS BE LSPs have been established. DeviceA is used as an example.
   
   ```
   [~DeviceA] display segment-routing prefix mpls forwarding
   ```
   ```
                    Segment Routing Prefix MPLS Forwarding Information
                --------------------------------------------------------------
                Role : I-Ingress, T-Transit, E-Egress, I&T-Ingress And Transit
    
   Prefix             Label      OutLabel   Interface         NextHop          Role  MPLSMtu   Mtu     State          
   ------------------------------------------------------------------------------------------------------------
   2.2.2.9/32        16100      NULL       Loop0            127.0.0.1        E     ---       1500    Active          
   5.5.5.9/32        16200      19200      GE0/2/0          10.1.1.1         I&T   ---       1500    Active          
   6.6.6.9/32        16300      19300      GE0/2/0          10.1.1.1         I&T   ---       1500    Active          
   1.1.1.9/32        16400      3          GE0/2/0          10.1.1.1         I&T   ---       1500    Active          
   ```
4. Establish a GRE tunnel.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface Tunnel1
   ```
   ```
   [*DeviceA-Tunnel1] ip address 10.7.1.1 24
   ```
   ```
   [*DeviceA-Tunnel1] tunnel-protocol gre
   ```
   ```
   [*DeviceA-Tunnel1] source 10.2.1.1
   ```
   ```
   [*DeviceA-Tunnel1] destination 10.4.1.2
   ```
   ```
   [*DeviceA-Tunnel1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] binding tunnel gre
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface Tunnel1
   ```
   ```
   [*DeviceB-Tunnel1] ip address 10.7.1.2 24
   ```
   ```
   [*DeviceB-Tunnel1] tunnel-protocol gre
   ```
   ```
   [*DeviceB-Tunnel1] source 10.4.1.2
   ```
   ```
   [*DeviceB-Tunnel1] destination 10.2.1.1
   ```
   ```
   [*DeviceB-Tunnel1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] binding tunnel gre
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
5. Set costs for links to ensure that the link DeviceA â DeviceD is preferentially used for traffic forwarding.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface Tunnel1
   ```
   ```
   [~DeviceA-Tunnel1] isis cost 100
   ```
   ```
   [*DeviceA-Tunnel1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For configuration details, see the configuration file.
6. Configure TI-LFA FRR.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] frr
   ```
   ```
   [*DeviceA-isis-1-frr] loop-free-alternate
   ```
   ```
   [*DeviceA-isis-1-frr] ti-lfa
   ```
   ```
   [*DeviceA-isis-1-frr] quit
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
7. Configure SR-MPLS BE over GRE.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] segment-routing mpls over gre
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For configuration details, see the configuration file.
   
   After completing the configuration, run the **display isis route** command on DeviceA to check route information.
   
   ```
   [~DeviceA] display isis 1 route 1.1.1.9 verbose
   
                           Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
   
    IPV4 Dest  : 1.1.1.9/32         Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 1             Flags     : A/-/L/-
    Priority   : Medium             Age       : 00:25:36
    NextHop    :                    Interface :               ExitIndex :
       10.1.1.1                           GE0/2/0                   0x00000009
    TI-LFA:
    Interface  : Tun2
    NextHop    : 10.7.1.2            LsIndex    : --          ProtectType: L
    Backup Label Stack (Top -> Bottom): {}
   
   
    Prefix-sid : 16400              Weight    : 0             Flags     : -/N/-/-/-/-/A/L
    SR NextHop :                    Interface :               OutLabel  :
       10.1.1.1                           GE0/2/0                   3
    TI-LFA:
    Interface  : Tun2
    NextHop    : 10.7.1.2            LsIndex    : --          ProtectType: L
    Backup Label Stack (Top -> Bottom): {}
   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
   
   
    IPV4 Dest  : 1.1.1.9/32         Int. Cost : 10            Ext. Cost : NULL
    Admin Tag  : -                  Src Count : 3             Flags     : -/-/-/-
    Priority   : Medium             Age       : 00:00:00
    NextHop    :                    Interface :               ExitIndex :
                                          -                
   
   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
   
   The command output shows that DeviceA has generated a backup link â which uses a GRE tunnel interface as the outbound interface â through FRR computation.
8. Verify the configuration.
   
   
   
   # Run the **tracert** command on DeviceA to check the connectivity of the SR-MPLS BE tunnel to DeviceD. For example:
   
   ```
   [~DeviceA] tracert lsp segment-routing ip 1.1.1.9 32 version draft2
   ```
   ```
    LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 1.1.1.9/32 , press CTRL_C to break.
     TTL    Replier            Time    Type      Downstream
     0                                 Ingress   10.1.1.1/[3 ]
     1      1.1.1.9           9 ms    Egress  
   ```
   
   # Run the **shutdown** command on GE0/2/0 of DeviceA to simulate a link failure between DeviceA and DeviceD.
   
   ```
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Run the **tracert** command on DeviceA again to check the connectivity of the SR-MPLS BE tunnel. For example:
   
   ```
   [~DeviceA] tracert lsp segment-routing ip 1.1.1.9 32 version draft2
   ```
   ```
    LSP Trace Route FEC: SEGMENT ROUTING IPV4 PREFIX 1.1.1.9/32 , press CTRL_C to break.
     TTL    Replier            Time    Type      Downstream
     0                                 Ingress   10.7.1.2/[17400 ]
     1      10.7.1.2           125 ms  Transit   10.6.1.2/[18400 ]
     2      10.6.1.2           130 ms  Transit   10.5.1.1/[3 ]
     3      1.1.1.9            24 ms   Egress  
   ```
   
   The preceding command output shows that the SR-MPLS BE tunnel has been switched to the TI-LFA FRR backup path, which uses a GRE tunnel interface as the outbound interface.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  # 
  segment-routing 
  # 
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   segment-routing mpls
   segment-routing global-block 16000 16999
   segment-routing mpls over gre
   frr
    loop-free-alternate level-1
    loop-free-alternate level-2
    ti-lfa level-1
    ti-lfa level-2
  # 
  isis 2
   network-entity 11.0000.0000.0021.00
  #
  interface Tunnel1 
   ip address 10.7.1.1 255.255.255.0 
   tunnel-protocol gre 
   source 10.2.1.1 
   destination 10.4.1.2 
   isis enable 1
   isis cost 100 
  # 
  interface LoopBack0 
   ip address 2.2.2.9 255.255.255.255 
   isis enable 1
   isis prefix-sid index 100 
  # 
  interface GigabitEthernet0/1/0
   undo shutdown 
   ip address 10.2.1.1 255.255.255.0 
   isis enable 2 
   binding tunnel gre 
  #
  interface GigabitEthernet0/2/0
   undo shutdown 
   ip address 10.1.1.2 255.255.255.0 
   isis enable 1
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  # 
  segment-routing 
  # 
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   segment-routing mpls
   segment-routing global-block 17000 17999
   segment-routing mpls over gre
  # 
  isis 2
   network-entity 11.0000.0000.0022.00
  #
  interface GigabitEthernet0/1/0 
   undo shutdown 
   ip address 10.4.1.2 255.255.255.0 
   isis enable 2
   binding tunnel gre 
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown 
   ip address 10.6.1.1 255.255.255.0 
   isis enable 1
  # 
  interface Tunnel1 
   ip address 10.7.1.2 255.255.255.0 
   tunnel-protocol gre 
   source 10.4.1.2 
   destination 10.2.1.1 
   isis enable 1
   isis cost 100 
  # 
  interface LoopBack0 
   ip address 5.5.5.9 255.255.255.255 
   isis enable 1 
   isis prefix-sid index 200 
  # 
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #                
  segment-routing 
  # 
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   segment-routing mpls
   segment-routing global-block 18000 18999 
  # 
  interface GigabitEthernet0/1/0 
   undo shutdown 
   ip address 10.6.1.2 255.255.255.0 
   isis enable 1
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown 
   ip address 10.5.1.2 255.255.255.0 
   isis enable 1
  # 
  interface LoopBack0 
   ip address 6.6.6.9 255.255.255.255 
   isis enable 1
   isis prefix-sid index 300 
  # 
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  # 
  segment-routing 
  # 
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   segment-routing mpls
   segment-routing global-block 19000 19999 
  #
  interface GigabitEthernet0/1/0 
   undo shutdown 
   ip address 10.1.1.1 255.255.255.0 
   isis enable 1 
  # 
  interface GigabitEthernet0/2/0 
   undo shutdown 
   ip address 10.5.1.1 255.255.255.0 
   isis enable 1 
  # 
  interface LoopBack0 
   ip address 1.1.1.9 255.255.255.0 
   isis enable 1 
   isis prefix-sid index 400 
  # 
  return
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  isis 2
  network-entity 11.0000.0000.0005.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   isis enable 2
  #
  return
  ```
* DeviceF configuration file
  
  ```
  #
  sysname DeviceF
  #
  isis 2
   network-entity 11.0000.0000.0006.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   isis enable 2
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
   isis enable 2
  #
  return
  ```