Example for Configuring IS-IS Anycast FRR
=========================================

IS-IS anycast FRR can be configured to enhance the reliability of an SR network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172368870__fig_dc_vrp_sr_all_cfg_001901), CE1 can be reached through either PE2 and PE3. To enable PE2 and PE3 to protect each other, configure IS-IS anycast FRR. This improves network reliability.

**Figure 1** IS-IS anycast FRR protection networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_sr_all_cfg_001901.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IS-IS on the backbone network to ensure that PEs interwork with each other.
2. Enable MPLS on the backbone network, configure SR, and establish SR LSPs.
3. Enable TI-LFA FRR on PE1 and configure the delayed switchback function.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and P
* SRGB ranges on the PEs

#### Procedure

1. Assign an IP address to each interface.
   
   
   
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
   [*PE1-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 172.18.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 172.16.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
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
   [*PE2-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 172.16.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE3] interface loopback 0
   ```
   ```
   [*PE3-LoopBack0] ip address 4.4.4.9 32
   ```
   ```
   [*PE3-LoopBack0] quit
   ```
   ```
   [*PE3] interface loopback 1
   ```
   ```
   [*PE3-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*PE3-LoopBack1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] ip address 172.18.1.2 24
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE3] commit
   ```
2. Configure an IGP on the backbone network to enable the PEs to communicate. IS-IS is used as an example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
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
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
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
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0002.00
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
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] isis 1
   ```
   ```
   [*PE3-isis-1] is-level level-1
   ```
   ```
   [*PE3-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] interface loopback 1
   ```
   ```
   [*PE3-LoopBack1] isis enable 1
   ```
   ```
   [*PE3-LoopBack1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE3] commit
   ```
3. Configure basic MPLS functions on the backbone network.
   
   
   
   Because MPLS is automatically enabled on the interface where IS-IS has been enabled, you can ignore MPLS configuration on such an interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] commit
   ```
   ```
   [~PE1-mpls] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] commit
   ```
   ```
   [~PE2-mpls] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls lsr-id 4.4.4.9
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] commit
   ```
   ```
   [~PE3-mpls] quit
   ```
4. Configure SR, enable TI-LFA FRR, and configure microloop avoidance in traffic switchback scenarios on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] tunnel-prefer segment-routing
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
   [*PE1-isis-1] segment-routing mpls
   ```
   ```
   [*PE1-isis-1] segment-routing global-block 160000 161000
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range various according to a live network. Set the range as needed. The SRGB setting here is an example.
   
   ```
   [*PE1-isis-1] frr
   ```
   ```
   [*PE1-isis-1-frr] loop-free-alternate level-1
   ```
   ```
   [*PE1-isis-1-frr] ti-lfa level-1
   ```
   ```
   [*PE1-isis-1-frr] quit
   ```
   ```
   [*PE1-isis-1] avoid-microloop segment-routing
   ```
   ```
   [*PE1-isis-1] avoid-microloop segment-routing rib-update-delay 6000
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] isis prefix-sid index 10
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] tunnel-prefer segment-routing
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
   [*PE2-isis-1] segment-routing mpls
   ```
   ```
   [*PE2-isis-1] segment-routing global-block 160000 161000
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] isis prefix-sid index 20
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing
   ```
   ```
   [*PE3-segment-routing] tunnel-prefer segment-routing
   ```
   ```
   [*PE3-segment-routing] quit
   ```
   ```
   [*PE3] isis 1
   ```
   ```
   [*PE3-isis-1] cost-style wide
   ```
   ```
   [*PE3-isis-1] segment-routing mpls
   ```
   ```
   [*PE3-isis-1] segment-routing global-block 160000 161000
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The configuration in this example is for reference only.
   
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] interface loopback 1
   ```
   ```
   [*PE3-LoopBack1] isis prefix-sid index 20
   ```
   ```
   [*PE3-LoopBack1] quit
   ```
   ```
   [*PE3] commit
   ```
5. Checking the Configurations
   
   Run the **display segment-routing prefix mpls forwarding verbose** command on PE1 to check the SR label forwarding table. The command output shows FRR backup entry information.
   ```
   [~PE1] display segment-routing prefix mpls forwarding ip-prefix 2.2.2.9 32 verbose
   
                      Segment Routing Prefix MPLS Forwarding Information
                --------------------------------------------------------------
                Role : I-Ingress, T-Transit, E-Egress, I&T-Ingress And Transit
   
   Prefix             Label      OutLabel   Interface         NextHop          Role  MPLSMtu   Mtu     State          
   -----------------------------------------------------------------------------------------------------------------
   2.2.2.9/32         160020     3          GE0/1/0           172.16.1.2       I&T   ---       1500    Active         
   Protocol : ISIS          SubProtocol : Level-1       Process ID : 1         
   Cost     : 10            Weight      : 0             UpdateTime : 2018-12-11 06:46:33.920       
   BFD State: --            Favor       : Y
   Label Stack (Top -> Bottom): { 3 }
   
   Prefix             Label      OutLabel   Interface         NextHop          Role  MPLSMtu   Mtu     State          
   -----------------------------------------------------------------------------------------------------------------
   2.2.2.9/32         160020     3          GE0/2/0           172.18.1.2       I&T   ---       1500    Active          
   Protocol : ISIS          SubProtocol : Level-1       Process ID : 1         
   Cost     : 10            Weight      : 0             UpdateTime : 2018-12-11 06:47:21.478       
   BFD State: --            Favor       : Y
   Label Stack (Top -> Bottom): { 3 }
   
   Total information(s): 2
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls            
  #               
  segment-routing 
   tunnel-prefer segment-routing
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   segment-routing mpls
   segment-routing global-block 160000 161000
   avoid-microloop segment-routing
   avoid-microloop segment-routing rib-update-delay 6000
   frr
    loop-free-alternate level-1
    ti-lfa level-1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 172.18.1.1 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 172.16.1.1 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 10
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 2.2.2.9
  #               
  mpls            
  #               
  segment-routing 
   tunnel-prefer segment-routing
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   segment-routing mpls
   segment-routing global-block 160000 161000
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 172.16.1.2 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 20
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 4.4.4.9
  #               
  mpls            
  #               
  segment-routing 
   tunnel-prefer segment-routing
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   segment-routing mpls
   segment-routing global-block 160000 161000
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 172.18.1.2 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack0
   ip address 4.4.4.9 255.255.255.255
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 20
  #
  return
  ```