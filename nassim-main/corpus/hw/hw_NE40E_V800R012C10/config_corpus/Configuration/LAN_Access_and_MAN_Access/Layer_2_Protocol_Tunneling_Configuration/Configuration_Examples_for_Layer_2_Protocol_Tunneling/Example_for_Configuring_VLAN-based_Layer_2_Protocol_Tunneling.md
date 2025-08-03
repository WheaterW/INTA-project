Example for Configuring VLAN-based Layer 2 Protocol Tunneling
=============================================================

When backbone network edge devices receive Layer 2 protocol data units (PDUs) that carry a single VLAN tag from user networks, configure VLAN-based Layer 2 protocol tunneling to allow the Layer 2 PDUs to be tunneled across the backbone network. Layer 2 PDUs from the user networks then travel through different Layer 2 tunnels to reach the destinations to perform Layer 2 protocol calculation. This example uses the Spanning Tree Protocol (STP).

#### Networking Requirements

When each edge device interface on a backbone network connects to more than one user network and Layer 2 PDUs from the user networks carry a single VLAN tag, configure VLAN-based Layer 2 protocol tunneling to allow the Layer 2 PDUs from the user networks to be tunneled across the backbone network. Layer 2 PDUs from the user networks then travel through different Layer 2 tunnels to reach the destinations to perform Layer 2 protocol calculation.

On the network shown in [Figure 1](#EN-US_TASK_0172363036__fig_dc_vrp_l2bptnl_cfg_002801), CEs are connected to PEs and run STP. Bridge protocol data units (BPDUs) from the CEs must traverse the backbone network on which the PEs reside. PE interfaces are aggregation interfaces, and the PEs use VLAN tags carried in BPDUs to identify users. To achieve the following requirements, configure VLAN-based Layer 2 protocol tunneling on the PEs:

* Devices in VLAN 100 build a spanning tree.
* Devices in VLAN 200 build a spanning tree.

The default multicast destination MAC address 0180-C200-0000 of BPDUs is used in this example.

**Figure 1** VLAN-based Layer 2 protocol tunneling networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/1, GE0/1/2, GE0/1/3, respectively.


  
![](images/fig_dc_vrp_l2bptnl_cfg_001901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Switch the interfaces on the CEs, Ls, PEs, and the P to Layer 2 interfaces.
2. Enable STP on the CEs and PEs.
3. Configure Layer 2 forwarding on the CEs so that the CEs send tagged BPDUs to the PEs.
4. Configure Layer 2 forwarding on the aggregation devices L1 and L2 to allow BPDUs that carry specific VLAN IDs to pass through.
5. Configure VLAN-based Layer 2 protocol tunneling on the PEs:
   
   1. Configure Layer 2 forwarding on the PEs to allow BPDUs that carry specific VLAN IDs to pass through.
   2. Disable STP on PEs' user-side interfaces and enable Layer 2 protocol tunneling on tagged interfaces.
   3. Configure the PEs to replace the multicast destination MAC address in the BPDUs from the CEs.
6. Configure Layer 2 forwarding on the P to allow BPDUs that carry specific VLAN IDs to pass through.

#### Data Preparation

To complete the configuration, you need the following data:

* Types and numbers of the interfaces that connect the CEs and Ls, that connect the PEs and Ls, and that connect the PEs and the P
* VLAN IDs of the CEs
* VLAN IDs of BPDUs that are allowed to pass through the Ls and PEs
* Specified multicast MAC address to replace the multicast destination MAC address in BPDUs

#### Procedure

1. Run the [**portswitch**](cmdqueryname=portswitch) command to switch each involved interface from Layer 3 mode to Layer 2 mode.
   
   
   
   Switch all interfaces on the CEs, Ls, PEs, and the P in the [Figure 1](#EN-US_TASK_0172363036__fig_dc_vrp_l2bptnl_cfg_002801) to Layer 2 interfaces.
2. Enable STP on the CEs and PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] stp enable
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] stp enable
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] stp enable
   ```
   ```
   [*CE3] commit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] stp enable
   ```
   ```
   [*CE4] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] stp enable
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] stp enable
   ```
   ```
   [*PE2] commit
   ```
3. Configure Layer 2 forwarding on the CEs so that the CEs send tagged BPDUs to the PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] vlan 100
   ```
   ```
   [*CE1-vlan100] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 100
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] stp bpdu vlan 100
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] vlan 100
   ```
   ```
   [*CE2-vlan100] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 100
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] stp bpdu vlan 100
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] vlan 200
   ```
   ```
   [*CE3-vlan200] quit
   ```
   ```
   [*CE3] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] port trunk allow-pass vlan 200
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] stp bpdu vlan 200
   ```
   ```
   [*CE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE3] commit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] vlan 200
   ```
   ```
   [*CE4-vlan200] quit
   ```
   ```
   [*CE4] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] port trunk allow-pass vlan 200
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] stp bpdu vlan 200
   ```
   ```
   [*CE4-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE4] commit
   ```
4. Configure Layer 2 forwarding on the aggregation devices L1 and L2 to allow BPDUs that carry specific VLAN IDs to pass through.
   
   
   
   # Configure L1.
   
   ```
   [~L1] vlan batch 100 200
   ```
   ```
   [*L1] interface gigabitethernet 0/1/3
   ```
   ```
   [*L1-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*L1-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*L1-GigabitEthernet0/1/3] port trunk allow-pass vlan 100 200
   ```
   ```
   [*L1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*L1] interface gigabitethernet 0/1/1
   ```
   ```
   [*L1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*L1-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*L1-GigabitEthernet0/1/1] port trunk allow-pass vlan 100
   ```
   ```
   [*L1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*L1] interface gigabitethernet 0/1/2
   ```
   ```
   [*L1-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*L1-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*L1-GigabitEthernet0/1/2] port trunk allow-pass vlan 200
   ```
   ```
   [*L1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*L1] commit
   ```
   
   # Configure L2.
   
   ```
   [~L2] vlan batch 100 200
   ```
   ```
   [*L2] interface gigabitethernet 0/1/3
   ```
   ```
   [*L2-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*L2-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*L2-GigabitEthernet0/1/3] port trunk allow-pass vlan 100 200
   ```
   ```
   [*L2-GigabitEthernet0/1/3] quit
   ```
   ```
   [*L2] interface gigabitethernet 0/1/1
   ```
   ```
   [*L2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*L2-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*L2-GigabitEthernet0/1/1] port trunk allow-pass vlan 100
   ```
   ```
   [*L2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*L2] interface gigabitethernet 0/1/2
   ```
   ```
   [*L2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*L2-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*L2-GigabitEthernet0/1/2] port trunk allow-pass vlan 200
   ```
   ```
   [*L2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*L2] commit
   ```
5. Configure VLAN-based Layer 2 protocol tunneling on the PEs.
   
   
   1. Configure Layer 2 forwarding on the PEs.
      
      # Configure PE1.
      
      ```
      [~PE1] vlan batch 100 200
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] port link-type trunk
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 200
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] port link-type trunk
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 100 200
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] vlan batch 100 200
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] port link-type trunk
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 200
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] port link-type trunk
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 100 200
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] commit
      ```
   2. Disable STP on PEs' user-side interfaces and enable Layer 2 protocol tunneling on tagged interfaces.
      
      # Configure PE1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] stp disable
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] l2protocol-tunnel stp enable
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] stp disable
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] l2protocol-tunnel stp enable
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] commit
      ```
   3. Configure the PEs to replace the multicast destination MAC address in the BPDUs from the CEs.
      
      # Configure PE1.
      
      ```
      [~PE1] l2protocol-tunnel stp group-mac 0100-5e00-0011
      ```
      ```
      [*PE1] commit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] l2protocol-tunnel stp group-mac 0100-5e00-0011
      ```
      ```
      [*PE2] commit
      ```
6. Configure Layer 2 forwarding on the P.
   
   
   ```
   [~P] vlan batch 100 200
   ```
   ```
   [*P] interface gigabitethernet 0/1/2
   ```
   ```
   [*P-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*P-GigabitEthernet0/1/2] port trunk allow-pass vlan 100 200
   ```
   ```
   [*P-GigabitEthernet0/1/2] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/1
   ```
   ```
   [*P-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*P-GigabitEthernet0/1/1] port trunk allow-pass vlan 100 200
   ```
   ```
   [*P-GigabitEthernet0/1/1] quit
   ```
   ```
   [*P] commit
   ```
7. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display l2protocol-tunnel group-mac**](cmdqueryname=display+l2protocol-tunnel+group-mac) command on the PEs to view Layer 2 protocol tunneling information, such as the tunneled Layer 2 protocol names, protocol types, multicast destination MAC addresses, and specified multicast MAC addresses (group MAC addresses).
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display l2protocol-tunnel group-mac stp
   ```
   ```
   Protocol         Protocol-MAC   Group-MAC       
   -----------------------------------------------------------------------------
   stp              0180-c200-0000 0100-5e00-0011 
   ```
   
   After completing the configurations, run the [**display stp**](cmdqueryname=display+stp) **brief** command on the CEs to view the MSTP port role. The following example uses the command output on CE3 and CE4. The command output shows that GE 0/1/1 on CE3 is the root port and GE 0/1/1 on CE4 is the designated port.
   
   ```
   [~CE3] display stp brief
   ```
   ```
    MSTID  Port                        Role  STP State     Protection   Cost   Edged
        0  GigabitEthernet0/1/1        ROOT  forwarding    none       199999   disable
   ```
   ```
   [~CE4] display stp brief
   ```
   ```
    MSTID  Port                        Role  STP State     Protection   Cost   Edged
        0  GigabitEthernet0/1/1        DESI  forwarding    none       199999   disable
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan batch 100
  #
  stp enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100
   stp bpdu vlan 100
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan batch 100
  #
  stp enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100
   stp bpdu vlan 100
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  vlan batch 200
  #
  stp enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 200
   stp bpdu vlan 200
  #
  return
  ```
* CE4 configuration file
  
  ```
  #
  sysname CE4
  #
  vlan batch 200
  #
  stp enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 200
   stp bpdu vlan 200
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  vlan batch 100 200
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type dot1q-tunnel
   port default vlan 100 200
   stp disable
   l2protocol-tunnel stp enable
  #
  interface GigabitEthernet0/1/2
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  vlan batch 100 200
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  interface GigabitEthernet0/1/2
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  vlan batch 100 200
  #
  l2protocol-tunnel stp group-mac 0100-5e00-0011
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
   stp disable
   l2protocol-tunnel stp enable
  #
  interface GigabitEthernet0/1/2
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```
* L1 configuration file
  
  ```
  #
  sysname L1
  #
  vlan batch 100 200
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100
  #
  interface GigabitEthernet0/1/2
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 200
  #
  interface GigabitEthernet0/1/3
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```
* L2 configuration file
  
  ```
  #
  sysname L2
  #
  vlan batch 100 200
  #
  interface GigabitEthernet0/1/1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100
  #
  interface GigabitEthernet0/1/2
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 200
  #
  interface GigabitEthernet0/1/3
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```