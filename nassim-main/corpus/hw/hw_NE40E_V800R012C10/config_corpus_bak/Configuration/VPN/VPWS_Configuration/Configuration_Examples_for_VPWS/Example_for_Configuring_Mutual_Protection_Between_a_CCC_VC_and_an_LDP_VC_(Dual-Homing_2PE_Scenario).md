Example for Configuring Mutual Protection Between a CCC VC and an LDP VC (Dual-Homing 2PE Scenario)
===================================================================================================

This section provides an example for configuring mutual protection between a CCC VC and an LDP VC. Specifying the master/backup status of PEs allows for mutual protection between a CCC VC and an LDP VC.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369914__fig_dc_vrp_vpws_cfg_607401), CE1 accesses CE2 through PE1. If the AC functioning as the active link between CE2 and PE1 fails, CE1 cannot be authenticated. To resolve this issue, you can deploy a PW between PE1 and PE2 to protect the active AC. Under normal circumstances, CE1 accesses CE2 for authentication through PE1. If the AC between PE1 and CE2 fails, CE1 accesses CE2 through the PW between PE1 and PE2 to prevent a service interruption.

**Figure 1** Mutual protection between a CCC VC and an LDP VC![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 and interface2 represent GE0/1/0 and GE0/1/1, respectively.

  
![](images/fig_dc_vrp_vpws_cfg_607401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the backbone network to achieve connectivity between devices.
2. Configure basic MPLS functions on PEs.
3. Configure a CCC that allows CE1 and CE2 to communicate and a protection PW for the CCC on PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP addresses and VLAN IDs
* Basic MPLS capabilities of peers
* CCC VC and LDP VC services on the peers


#### Procedure

1. Configure CEs.
   
   
   
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
   [~CE1] interface Eth-Trunk 10
   ```
   ```
   [*CE1-Eth-Trunk10] mode lacp-static
   ```
   ```
   [*CE1-Eth-Trunk10] quit
   ```
   ```
   [*CE1] interface Eth-Trunk10.100
   ```
   ```
   [*CE1-Eth-Trunk10.100] undo shutdown
   ```
   ```
   [*CE1-Eth-Trunk10.100] vlan-type dot1q 100
   ```
   ```
   [*CE1-Eth-Trunk10.100] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*CE1-Eth-Trunk10.100] quit
   ```
   ```
   [*CE1] interface gigabitethernet0/1/1
   ```
   ```
   [*CE1-Gigabitethernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] eth-trunk 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] interface gigabitethernet0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] eth-trunk 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE2] interface Eth-Trunk 20
   ```
   ```
   [*CE2-Eth-Trunk20] mode lacp-static
   ```
   ```
   [*CE2-Eth-Trunk20] quit
   ```
   ```
   [*CE2] interface Eth-Trunk20.100
   ```
   ```
   [*CE2-Eth-Trunk20.100] undo shutdown
   ```
   ```
   [*CE2-Eth-Trunk20.100] vlan-type dot1q 100
   ```
   ```
   [*CE2-Eth-Trunk20.100] ip address 10.1.1.2 255.255.255.0
   ```
   ```
   [*CE2-Eth-Trunk20.100] quit
   ```
   ```
   [*CE2] interface gigabitethernet0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] eth-trunk 20
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] interface gigabitethernet0/1/0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] eth-trunk 20
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE2] commit
   ```
2. Configure IP addresses for the interfaces on the backbone network.
   
   
   
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
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ip address 192.168.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
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
   [*PE2-LoopBack1] ip address 2.2.2.2 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] ip address 192.168.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
3. Enable MPLS and establish LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 2.2.2.2
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
4. Configure an IGP (OSPF in this example).
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 192.168.1.1 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE1-ospf-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 192.168.1.2 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-1] quit
   ```
   ```
   [*PE2] commit
   ```
5. Enable MPLS L2VPN on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] commit
   ```
6. Configure an E-Trunk to determine the primary/secondary status of PWs.
   1. Configure an E-Trunk.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] lacp e-trunk system-id 00e0-fc00-0000
      ```
      ```
      [*PE1] lacp e-trunk priority 100
      ```
      ```
      [*PE1] e-trunk 10
      ```
      ```
      [*PE1-e-trunk-10] priority 10
      ```
      ```
      [*PE1-e-trunk-10] peer-address 2.2.2.2 source-address 1.1.1.1
      ```
      ```
      [*PE1-e-trunk-10] quit
      ```
      ```
      [*PE1] interface eth-trunk 10
      ```
      ```
      [*PE1-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*PE1-Eth-Trunk10] e-trunk 10
      ```
      ```
      [*PE1-Eth-Trunk10] quit
      ```
      ```
      [*PE1] e-trunk 20
      ```
      ```
      [*PE1-e-trunk-20] priority 20
      ```
      ```
      [*PE1-e-trunk-20] peer-address 2.2.2.2 source-address 1.1.1.1
      ```
      ```
      [*PE1-e-trunk-20] quit
      ```
      ```
      [*PE1] interface eth-trunk 20
      ```
      ```
      [*PE1-Eth-Trunk20] mode lacp-static
      ```
      ```
      [*PE1-Eth-Trunk20] e-trunk 20
      ```
      ```
      [*PE1-Eth-Trunk20] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] eth-trunk 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] eth-trunk 20
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] lacp e-trunk system-id 00e0-fc00-0000
      ```
      ```
      [*PE2] lacp e-trunk priority 100
      ```
      ```
      [*PE2] e-trunk 10
      ```
      ```
      [*PE2-e-trunk-10] priority 20
      ```
      ```
      [*PE2-e-trunk-10] peer-address 1.1.1.1 source-address 2.2.2.2
      ```
      ```
      [*PE2-e-trunk-10] quit
      ```
      ```
      [*PE2] interface eth-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] mode lacp-static
      ```
      ```
      [*PE2-Eth-Trunk10] e-trunk 10
      ```
      ```
      [*PE2-Eth-Trunk10] quit
      ```
      ```
      [*PE2] e-trunk 20
      ```
      ```
      [*PE2-e-trunk-20] priority 30
      ```
      ```
      [*PE2-e-trunk-20] peer-address 1.1.1.1 source-address 2.2.2.2
      ```
      ```
      [*PE2-e-trunk-20] quit
      ```
      ```
      [*PE2] interface eth-trunk 20
      ```
      ```
      [*PE2-Eth-Trunk20] mode lacp-static
      ```
      ```
      [*PE2-Eth-Trunk20] e-trunk 20
      ```
      ```
      [*PE2-Eth-Trunk20] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/0
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] eth-trunk 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] eth-trunk 20
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] commit
      ```
   2. Bind BFD to the E-Trunk.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] bfd
      ```
      ```
      [*PE1-bfd] quit
      ```
      ```
      [*PE1] bfd hello bind peer-ip 2.2.2.2 source-ip 1.1.1.1
      ```
      ```
      [*PE1-bfd-session-hello] discriminator local 100
      ```
      ```
      [*PE1-bfd-session-hello] discriminator remote 101
      ```
      ```
      [*PE1-bfd-session-hello] quit
      ```
      ```
      [*PE1] bfd hi bind peer-ip 2.2.2.2 source-ip 1.1.1.1
      ```
      ```
      [*PE1-bfd-session-hi] discriminator local 200
      ```
      ```
      [*PE1-bfd-session-hi] discriminator remote 201
      ```
      ```
      [*PE1-bfd-session-hi] quit
      ```
      ```
      [*PE1] e-trunk 10
      ```
      ```
      [*PE1-e-trunk-10] e-trunk track bfd-session session-name hello
      ```
      ```
      [*PE1-e-trunk-10] quit
      ```
      ```
      [*PE1] e-trunk 20
      ```
      ```
      [*PE1-e-trunk-20] e-trunk track bfd-session session-name hi
      ```
      ```
      [*PE1-e-trunk-20] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] bfd
      ```
      ```
      [*PE2-bfd] quit
      ```
      ```
      [*PE2] bfd hello bind peer-ip 1.1.1.1 source-ip 2.2.2.2
      ```
      ```
      [*PE2-bfd-session-hello] discriminator local 101
      ```
      ```
      [*PE2-bfd-session-hello] discriminator remote 100
      ```
      ```
      [*PE2-bfd-session-hello] quit
      ```
      ```
      [*PE2] bfd hi bind peer-ip 1.1.1.1 source-ip 2.2.2.2
      ```
      ```
      [*PE2-bfd-session-hi] discriminator local 201
      ```
      ```
      [*PE2-bfd-session-hi] discriminator remote 200
      ```
      ```
      [*PE2-bfd-session-hi] quit
      ```
      ```
      [*PE2] e-trunk 10
      ```
      ```
      [*PE2-e-trunk-10] e-trunk track bfd-session session-name hello
      ```
      ```
      [*PE2-e-trunk-10] quit
      ```
      ```
      [*PE2] e-trunk 20
      ```
      ```
      [*PE2-e-trunk-20] e-trunk track bfd-session session-name hi
      ```
      ```
      [*PE2-e-trunk-20] quit
      ```
      ```
      [*PE2] commit
      ```
7. Create a CCC VC and LDP VCs on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface Eth-Trunk10.100
   ```
   ```
   [*PE1-Eth-Trunk10.100] vlan-type dot1q 100
   ```
   ```
   [*PE1-Eth-Trunk10.100] quit
   ```
   ```
   [*PE1] interface Eth-Trunk20.100
   ```
   ```
   [*PE1-Eth-Trunk20.100] vlan-type dot1q 100
   ```
   ```
   [*PE1-Eth-Trunk20.100] mpls ccc out-interface Eth-Trunk10.100
   ```
   ```
   [*PE1-Eth-Trunk20.100] mpls l2vc 2.2.2.2 200 secondary
   ```
   ```
   [*PE1-Eth-Trunk20.100] mpls l2vpn redundancy independent
   ```
   ```
   [*PE1-Eth-Trunk20.100] quit
   ```
   ```
   [*PE1] interface Eth-Trunk10.100
   ```
   ```
   [*PE1-Eth-Trunk10.100] mpls ccc out-interface Eth-Trunk20.100
   ```
   ```
   [*PE1-Eth-Trunk10.100] mpls l2vc 2.2.2.2 100 secondary
   ```
   ```
   [*PE1-Eth-Trunk10.100] mpls l2vpn redundancy independent
   ```
   ```
   [*PE1-Eth-Trunk10.100] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface Eth-Trunk10.100
   ```
   ```
   [*PE2-Eth-Trunk10.100] vlan-type dot1q 100
   ```
   ```
   [*PE2-Eth-Trunk10.100] quit
   ```
   ```
   [*PE2] interface Eth-Trunk20.100
   ```
   ```
   [*PE2-Eth-Trunk20.100] vlan-type dot1q 100
   ```
   ```
   [*PE2-Eth-Trunk20.100] mpls ccc out-interface Eth-Trunk10.100
   ```
   ```
   [*PE2-Eth-Trunk20.100] mpls l2vc 1.1.1.1 100 secondary
   ```
   ```
   [*PE2-Eth-Trunk20.100] mpls l2vpn redundancy independent
   ```
   ```
   [*PE2-Eth-Trunk20.100] quit
   ```
   ```
   [*PE2] interface Eth-Trunk10.100
   ```
   ```
   [*PE2-Eth-Trunk10.100] mpls ccc out-interface Eth-Trunk20.100
   ```
   ```
   [*PE2-Eth-Trunk10.100] mpls l2vc 1.1.1.1 200 secondary
   ```
   ```
   [*PE2-Eth-Trunk10.100] mpls l2vpn redundancy independent
   ```
   ```
   [*PE2-Eth-Trunk10.100] quit
   ```
   ```
   [*PE2] commit
   ```
8. Verify the configuration.
   
   
   
   After the configurations are complete, check the VPWS status on PE1. The command output shows that the CCC and LDP VCs have been established and are in the up state. The role of the CCC VC is primary, and that of the LDP VC is secondary.
   
   ```
   <PE1> display mpls l2vpn vpws
   ```
   ```
   Pri : Primary            Sec : Secondary            Byp : Bypass
   PWb : PW-bypass          ACb : AC-bypass
   
   Access Circuit                     Virtual Circuit               States Active   Role
   Eth-Trunk10.100                    Eth-Trunk20.100               Up     Active   Pri
                                      2.2.2.2:100                   Up     Inactive Sec
   Eth-Trunk20.100                    Eth-Trunk10.100               Up     Active   Pri
                                      2.2.2.2:200                   Up     Inactive Sec
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface Eth-Trunk10                                                           
    mode lacp-static                                                               
  #                                                                               
  interface Eth-Trunk10.100                                                       
   vlan-type dot1q 100                                                            
   ip address 10.1.1.1 255.255.255.0                                             
  #                                                                               
  interface GigabitEthernet0/1/0                                                         
   undo shutdown                                                                  
   eth-trunk 10  
  #                                                                 
  interface GigabitEthernet0/1/1                                                        
   undo shutdown                                                                  
   eth-trunk 10                                                                              
  #                                                                 
  #return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface Eth-Trunk20                                                           
   mode lacp-static                                                               
  #                                                                               
  interface Eth-Trunk20.100                                                       
   vlan-type dot1q 100                                                            
   ip address 10.1.1.2 255.255.255.0                                             
  #                                                                               
  interface GigabitEthernet0/1/0                                                         
   undo shutdown                                                                  
   eth-trunk 20  
  #                                                                 
  interface GigabitEthernet0/1/1                                                        
   undo shutdown                                                                  
   eth-trunk 20
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 100
  #
  e-trunk 10
  #
  e-trunk 20
  #
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  mpls l2vpn
  #
  interface Eth-Trunk10                                                           
    mode lacp-static   
    e-trunk 10                                                            
  # 
  interface Eth-Trunk10.100
   vlan-type dot1q 100                                                            
   mpls ccc out-interface Eth-Trunk20.100
   mpls l2vc 2.2.2.2 100 secondary                                                
   mpls l2vpn redundancy independent                                                   
  #
  interface Eth-Trunk20                                                           
    mode lacp-static     
    e-trunk 20                                                            
  #                                                                                
  interface Eth-Trunk20.100
   vlan-type dot1q 100                                                            
   mpls ccc out-interface Eth-Trunk10.100
   mpls l2vc 2.2.2.2 200 secondary                                                
   mpls l2vpn redundancy independent                                                   
  #                                                                            
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 20                                                            
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1                                                                                                            
   area 0.0.0.0                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 192.168.1.1 0.0.0.255
  #
  bfd hello bind peer-ip 2.2.2.2 source-ip 1.1.1.1
   discriminator local 100
   discriminator remote 101
  #
  bfd hi bind peer-ip 2.2.2.2 source-ip 1.1.1.1
   discriminator local 200
   discriminator remote 201
  #
  e-trunk 10
   priority 10
   peer-address 2.2.2.2 source-address 1.1.1.1
   e-trunk track bfd-session session-name hello
  #
  e-trunk 20
   priority 20
   peer-address 2.2.2.2 source-address 1.1.1.1
   e-trunk track bfd-session session-name hi
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  lacp e-trunk system-id 00e0-fc00-0000
  lacp e-trunk priority 100
  #
  e-trunk 10
  #
  e-trunk 20
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  mpls l2vpn
  #
  interface Eth-Trunk10                                                           
    mode lacp-static  
    e-trunk 10                                                             
  #
  interface Eth-Trunk10.100
   vlan-type dot1q 100                                                            
   mpls ccc out-interface Eth-Trunk20.100
   mpls l2vc 1.1.1.1 200 secondary                                                
   mpls l2vpn redundancy independent                                                   
  #
  interface Eth-Trunk20                                                           
    mode lacp-static 
    e-trunk 20                                                              
  #                                                                                
  interface Eth-Trunk20.100
   vlan-type dot1q 100                                                            
   mpls ccc out-interface Eth-Trunk10.100
   mpls l2vc 1.1.1.1 100 secondary                                                
   mpls l2vpn redundancy independent                                                   
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10  
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 20                                                            
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1                                                                                                            
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 192.168.1.2 0.0.0.255
  #
  bfd hello bind peer-ip 1.1.1.1 source-ip 2.2.2.2
   discriminator local 101
   discriminator remote 100
  #
  bfd hi bind peer-ip 1.1.1.1 source-ip 2.2.2.2
   discriminator local 201
   discriminator remote 200
  #
  e-trunk 10
   priority 20
   peer-address 1.1.1.1 source-address 2.2.2.2
   e-trunk track bfd-session session-name hello
  #
  e-trunk 20
   priority 30
   peer-address 1.1.1.1 source-address 2.2.2.2
   e-trunk track bfd-session session-name hi
  #
  return
  ```