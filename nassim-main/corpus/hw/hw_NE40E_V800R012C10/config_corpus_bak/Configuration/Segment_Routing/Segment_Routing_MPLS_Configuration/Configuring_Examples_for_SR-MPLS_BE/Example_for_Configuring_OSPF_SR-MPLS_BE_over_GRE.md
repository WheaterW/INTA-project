Example for Configuring OSPF SR-MPLS BE over GRE
================================================

This section provides an example for configuring OSPF SR-MPLS BE over GRE, which involves enabling OSPF on each device, specifying network segments in different areas, and configuring GRE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001367303394__fig127031455165813), enable OSPF and configure SR-MPLS BE. In addition, set the cost of the GRE tunnel between DeviceA and DeviceB to 100 and that of the other links to 10. The optimal path from DeviceA to DeviceD is DeviceA â DeviceD. Configure TI-LFA FRR on DeviceA to implement local protection. In this way, if the link between DeviceA and DeviceD fails, traffic can be rapidly switched to the backup path DeviceA â DeviceB â DeviceC â DeviceD. The traffic between DeviceA and DeviceB is forwarded over a GRE tunnel, which is bound to the link DeviceA â DeviceE â DeviceF â DeviceB.

**Figure 1** Configuring OSPF SR-MPLS BE over GRE![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001418710713.png "Click to enlarge")

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on the entire network to implement interworking between devices.
2. Configure SR and establish an SR-MPLS BE tunnel.
3. Establish a GRE tunnel between DeviceA and DeviceB and bind the tunnel to another area.
4. Set costs for links to ensure that the link DeviceA â DeviceD is preferentially used for traffic forwarding.
5. Configure TI-LFA FRR.

#### Data Preparation

To complete the configuration, you need the following data:

* DeviceA: router ID 1.1.1.1, OSPF process ID 1, area 0's network segment 10.2.1.0/24, and area 1's network segments 10.1.1.0/24 and 10.7.1.0/24
* DeviceB: router ID 2.2.2.2, OSPF process ID 1, area 0's network segment 10.4.1.0/24, and area 1's network segments 10.6.1.0/24 and 10.7.1.0/24
* DeviceC: router ID 3.3.3.3, OSPF process ID 1, and area 1's network segments 10.6.1.0/24 and 10.5.1.0/24
* DeviceD: router ID 4.4.4.4, OSPF process ID 1, and area 1's network segments 10.1.1.0/24 and 10.5.1.0/24
* DeviceE: router ID 5.5.5.5, OSPF process ID 1, and area 0's network segments 10.2.1.0/24 and 10.3.1.0/24
* DeviceF: router ID 6.6.6.6, OSPF process ID 1, and area 0's network segments 10.3.1.0/24 and 10.4.1.0/24

#### Procedure

1. Configure interface IP addresses.
   
   
   
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
2. Configure OSPF to implement interworking.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospf-1] area 0.0.0.0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] area 0.0.0.1
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] network 10.1.1.0 0.0.0.255 
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] network 10.7.1.0 0.0.0.255 
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.1] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
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
   [*DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] segment-routing mpls
   ```
   ```
   [*DeviceA-ospf-1] segment-routing global-block 16000 16999 
   ```
   ```
   [*DeviceA-ospf-1] quit 
   ```
   ```
   [*DeviceA] interface LoopBack0
   ```
   ```
   [*DeviceA-LoopBack0] ospf enable 1 area 0.0.0.1
   ```
   ```
   [*DeviceA-LoopBack0] ospf prefix-sid index 100
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
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
   2.2.2.9/32        16100      NULL       Loop0             127.0.0.1        E     ---       1500    Active          
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
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ospf cost 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface Tunnel1
   ```
   ```
   [~DeviceA-Tunnel1] ospf cost 100
   ```
   ```
   [*DeviceA-Tunnel1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For configuration details, see the configuration file.
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ospf cost 10
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] ospf cost 10
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   The configuration of DeviceD is similar to that of DeviceC. For configuration details, see the configuration file.
6. Configure TI-LFA FRR.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [~DeviceA-ospf-1] avoid-microloop frr-protected
   ```
   ```
   [*DeviceA-ospf-1] avoid-microloop frr-protected rib-update-delay 5000
   ```
   ```
   [*DeviceA-ospf-1] avoid-microloop segment-routing
   ```
   ```
   [*DeviceA-ospf-1] avoid-microloop segment-routing rib-update-delay 10000
   ```
   ```
   [*DeviceA-ospf-1] frr
   ```
   ```
   [*DeviceA-ospf-1-frr] loop-free-alternate
   ```
   ```
   [*DeviceA-ospf-1-frr] ti-lfa enable
   ```
   ```
   [*DeviceA-ospf-1-frr] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   After completing the configuration, run the [**display ospf routing**](cmdqueryname=display+ospf+routing) command on DeviceA to check route information.
   
   ```
   [~DeviceA] display ospf 1 routing 1.1.1.9
   ```
   ```
           OSPF Process 1 with Router ID 1.1.1.1
    
    Destination    : 1.1.1.9/32
    AdverRouter    : 4.4.4.4                  Area                : 0.0.0.1
    Cost           : 10                       Type                : Stub
    NextHop        : 10.1.1.1                 Interface           : GE0/2/0
    Priority       : Medium                   Age                 : 00h28m04s
    Backup NextHop : 10.7.1.2                 Backup Interface    : Tun1
    Backup Type    : TI-LFA LINK              
    BakLabelStack  : -   
   ```
   
   The command output shows that DeviceA has generated a backup link â which uses a GRE tunnel interface as the outbound interface â through FRR computation.
   
   # Run the **display ospf segment-routing routing** command on DeviceA to check route information.
   
   ```
   [~DeviceA] display ospf 1 segment-routing routing 1.1.1.9
   ```
   ```
           OSPF Process 1 with Router ID 1.1.1.1
    
    Destination      : 1.1.1.9/32              
    AdverRouter      : 4.4.4.4                  Area             : 0.0.0.1
    In-Label         : 16400                    Out-Label        : 3                         
    Type             : Stub                     Age              : 00h01m15s
    Prefix-sid       : 400                      Flags            : -|N|-|-|-|-|-|-
    SR-Flags         : -|-|-|-|-|-|-|-           
    NextHop          : 10.1.1.1                 Interface        : GE0/2/0                  
    Backup NextHop   : 10.7.1.2                 Backup Interface : Tun1                      
    Backup Type      : TI-LFA LINK              
    BakLabelStack    : -                                                                        
    BakOutLabel      : 17400
   ```
   
   The command output shows that DeviceA has generated a backup link â which uses a GRE tunnel interface as the outbound interface â through FRR computation.
7. Configure SR-MPLS BE over GRE.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] segment-routing mpls over gre
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For configuration details, see the configuration file.
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
   
   # Run the **shutdown** command on GE 0/2/0 of DeviceA to simulate a link failure between DeviceA and DeviceD.
   
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
  ospf 1
   router-id 1.1.1.1
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 16000 16999
   segment-routing mpls over gre
   avoid-microloop frr-protected
   avoid-microloop frr-protected rib-update-delay 5000
   avoid-microloop segment-routing
   avoid-microloop segment-routing rib-update-delay 10000
   frr
    loop-free-alternate
    ti-lfa enable
   area 0.0.0.0
    network 10.2.1.0 0.0.0.255
   area 0.0.0.1
    network 10.1.1.0 0.0.0.255
    network 10.7.1.0 0.0.0.255
  #
  interface Tunnel1
   ip address 10.7.1.1 255.255.255.0
   tunnel-protocol gre
   source 10.2.1.1
   destination 10.4.1.2
   ospf cost 100
  #
  interface LoopBack0
   ip address 2.2.2.9 255.255.255.255
   ospf enable 1 area 0.0.0.1
   ospf prefix-sid index 100
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   binding tunnel gre
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   ospf cost 10
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
  ospf 1
   router-id 2.2.2.2
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 17000 17999
   segment-routing mpls over gre
   area 0.0.0.0
    network 10.4.1.0 0.0.0.255
   area 0.0.0.1
    network 10.6.1.0 0.0.0.255
    network 10.7.1.0 0.0.0.255
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.4.1.2 255.255.255.0
   ospf cost 10
  binding tunnel gre
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.6.1.1 255.255.255.0
   ospf cost 10
  #
  interface Tunnel1
   ip address 10.7.1.2 255.255.255.0
   tunnel-protocol gre
   source 10.4.1.2
   destination 10.2.1.1
   ospf cost 100
  #
  interface LoopBack0
   ip address 5.5.5.9 255.255.255.255
   ospf enable 1 area 0.0.0.1
   ospf prefix-sid index 200
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
  ospf 1 router-id 3.3.3.3
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 18000 18999
   area 0.0.0.1
    network 10.6.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.6.1.2 255.255.255.0
   ospf cost 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.5.1.2 255.255.255.0
   ospf cost 10
  #
  interface LoopBack0
   ip address 6.6.6.9 255.255.255.255
   ospf enable 1 area 0.0.0.1
   ospf prefix-sid index 300
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
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   ospf cost 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.5.1.1 255.255.255.0
   ospf cost 10
  #
  interface LoopBack0
   ip address 1.1.1.9 255.255.255.0
   ospf enable 1 area 0.0.0.1
   ospf prefix-sid index 400
  #
  ospf 1 router-id 4.4.4.4
   opaque-capability enable
   segment-routing mpls
   segment-routing global-block 19000 19999
   area 0.0.0.1
    network 10.1.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
  #
  return
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
  #
  ospf 1 router-id 5.5.5.5
   opaque-capability enable
   area 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* DeviceF configuration file
  
  ```
  #
  sysname DeviceF
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
  #
  ospf 1 router-id 6.6.6.6
   opaque-capability enable
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.4.1.0 0.0.0.255
  #
  return
  ```