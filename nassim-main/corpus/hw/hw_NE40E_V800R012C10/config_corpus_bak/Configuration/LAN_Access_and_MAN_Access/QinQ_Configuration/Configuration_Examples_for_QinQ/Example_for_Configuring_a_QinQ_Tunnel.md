Example for Configuring a QinQ Tunnel
=====================================

After Layer 2 QinQ tunneling is configured, an enterprise can plan its own VLANs. Branch offices of the same enterprise in different locations can communicate with each other through the VLANs. Offices of different enterprises cannot communicate.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363292__en-us_task_0172363199_fig_dc_vrp_qinq_cfg_002401), company 1 has three offices and company 2 has two offices. Offices of company 1 and company 2 are connected to PE1 and PE2 on the carrier network. Company 1 and company 2 can plan their own VLANs as required.

You can configure Layer 2 QinQ tunneling on PE1 and PE2 so that offices of the same company can interwork but offices of different companies cannot interwork.

**Figure 1** Typical networking of Layer 2 QinQ tunneling![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/1, GE0/2/1, GE0/3/1, and GE0/1/4, respectively.


  
![](figure/en-us_image_0000001505509640.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure outer VLAN tags for QinQ packets.
2. Configure Layer 2 QinQ tunneling so that packets exchanged between VLAN users become double-tagged QinQ packets after passing through the QinQ tunnel.
3. Configure interfaces on which Layer 2 QinQ tunneling is not configured. These interfaces allow packets carrying the specified outer VLAN tags to pass through so that users of the same company from different VLANs can communicate.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of the access interfaces of company 1 and company 2
* Outer VLAN IDs of the QinQ interfaces for company 1 and company 2 access

#### Procedure

1. Create outer VLAN tags for Layer 2 QinQ tunneling.
   
   
   
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
   [~PE1] vlan batch 10 20
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
   [~PE2] vlan batch 10 20
   ```
2. Configure Layer 2 QinQ tunneling.
   
   
   
   # Configure PE1.
   
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port link-type dot1q-tunnel
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port default vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] port link-type dot1q-tunnel
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] port default vlan 20
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/3/1
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] port link-type dot1q-tunnel
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] port default vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/3/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port link-type dot1q-tunnel
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port default vlan 20
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] port link-type dot1q-tunnel
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] port default vlan 10
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE2] commit
   ```
3. Configure other interfaces.
   
   
   
   # Configure GE0/1/4 on PE1 to allow packets from VLAN 10 and VLAN 20 to pass through.
   
   ```
   [~PE1] interface gigabitethernet 0/1/4
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] port link-type trunk
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] port trunk allow-pass vlan 10 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/4] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure GE0/3/1 on PE2 to allow packets from VLAN 10 and VLAN 20 to pass through.
   
   ```
   [~PE2] interface gigabitethernet 0/3/1
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] port link-type trunk
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] port trunk allow-pass vlan 10 20
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/3/1] quit
   ```
   ```
   [*PE2] commit
   ```
4. Verify the configuration.
   
   
   
   Hosts of company 1 in different offices but the same VLAN can ping each other.
   
   Hosts of company 2 in different offices but the same VLAN can ping each other.
   
   Hosts of company 1 cannot ping hosts of company 2.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
   sysname PE1
  #
   vlan batch 10 20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   portswitch
   port link-type dot1q-tunnel
   port default vlan 10
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   portswitch
   port link-type dot1q-tunnel
   port default vlan 20
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   portswitch
   port link-type dot1q-tunnel
   port default vlan 10
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10 20
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
   sysname PE2
  #
   vlan batch 10 20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   portswitch
   port link-type dot1q-tunnel
   port default vlan 20
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   portswitch
   port link-type dot1q-tunnel
   port default vlan 10
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10 20
  #
  return
  ```