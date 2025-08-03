Example for Configuring Eth-Trunk Interfaces in Manual 1:1 Master/Backup Mode
=============================================================================

An Eth-Trunk interface in manual 1:1 master/backup mode contains only two member interfaces: one master interface and one backup interface. In normal situations, only the master interface forwards traffic. If the master interface fails, the backup interface takes over traffic.

#### Networking Requirements

As the service volume expands, the bandwidth provided by a single P2P physical link working in full-duplex mode cannot meet the service requirement. Deploying Eth-Trunk interfaces to implement link aggregation provides higher bandwidth than each individual link and improves link reliability.

When intermediate devices exist between the devices at both ends of an Eth-Trunk link, Eth-Trunk interfaces in manual 1:1 master/backup mode can be configured to improve link reliability.

On the network shown in [Figure 1](#EN-US_TASK_0172362934__fig_dc_vrp_ethtrunk_cfg_005601), PE1 and PE2 are connected through PE3 and PE4. To improve link reliability between PE1 and PE2, configure Eth-Trunk interfaces in manual 1:1 master/backup mode on PE1 and PE2.

**Figure 1** Network diagram of configuring Eth-Trunk interfaces in manual 1:1 master/backup mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/2/1, respectively.


  
![](figure/en-us_image_0000001433660633.png)

#### Precautions

When configuring Eth-Trunk interfaces in manual 1:1 master/backup mode, note the following:

* The master member interface must be specified for each Eth-Trunk interface to forward data.
* The devices on the two ends of the Eth-Trunk link must be enabled to send Flush packets. After the master and backup interfaces are switched in an Eth-Trunk interface, the new master interface sends Flush packets to instruct the peer end to age MAC addresses. This function prevents data interruption caused by asynchronous MAC addresses.
* The intermediate devices must be enabled to receive Flush packets so that they can transparently transmit Flush packets.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Eth-Trunk interface in manual 1:1 master/backup mode on each of PE1 and PE2 and add physical Ethernet interfaces to each Eth-Trunk interface for link aggregation.
2. Specify the master interface for the Eth-Trunk interface on each of PE1 and PE2 to implement link backup.
3. Enable PE1 and PE2 to send Flush packets. After the master and backup interfaces are switched, the new master interface sends Flush packets to instruct the peer end to age MAC addresses.
4. Enable PE3 and PE4 to receive Flush packets so that they can transparently transmit Flush packets.

#### Data Preparation

To complete the configuration, you need the following data:

* Eth-Trunk interface ID
* Type and number of the member interface of the Eth-Trunk interface
* Control VLAN ID of Flush packets allowed to be forwarded

#### Procedure

1. Create an Eth-Trunk interface in manual 1:1 master/backup mode on each of PE1 and PE2 and add physical Ethernet interfaces to each Eth-Trunk interface.
   
   
   
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
   [~PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] portswitch
   ```
   ```
   [*PE1-Eth-Trunk1] mode manual backup
   ```
   ```
   [*PE1-Eth-Trunk1] trunkport gigabitethernet 0/1/1 0/2/1
   ```
   ```
   [*PE1-Eth-Trunk1] quit
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
   [~PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] portswitch
   ```
   ```
   [*PE2-Eth-Trunk1] mode manual backup
   ```
   ```
   [*PE2-Eth-Trunk1] trunkport gigabitethernet 0/1/1 0/2/1
   ```
   ```
   [*PE2-Eth-Trunk1] quit
   ```
   ```
   [*PE2] commit
   ```
2. Specify the master interface in the Eth-Trunk interface on each of PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port-master
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port-master
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/1
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
3. # Enable PE1 and PE2 to send Flush packets.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vlan batch 5
   ```
   ```
   [*PE1] interface eth-trunk 1
   ```
   ```
   [*PE1-Eth-Trunk1] port trunk allow-pass vlan 5
   ```
   ```
   [*PE1-Eth-Trunk1] smart-link flush send vlan 5
   ```
   ```
   [*PE1-Eth-Trunk1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] vlan batch 5
   ```
   ```
   [*PE2] interface eth-trunk 1
   ```
   ```
   [*PE2-Eth-Trunk1] port trunk allow-pass vlan 5
   ```
   ```
   [*PE2-Eth-Trunk1] smart-link flush send vlan 5
   ```
   ```
   [*PE2-Eth-Trunk1] quit
   ```
   ```
   [*PE2] commit
   ```
4. # Enable PE3 and PE4 to receive Flush packets.
   
   
   
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
   [~PE3] vlan batch 5
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] port trunk allow-pass vlan 5
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] smart-link flush enable control-vlan 5
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE3-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE3-GigabitEthernet0/2/1] portswitch
   ```
   ```
   [*PE3-GigabitEthernet0/2/1] port trunk allow-pass vlan 5
   ```
   ```
   [*PE3-GigabitEthernet0/2/1] smart-link flush enable control-vlan 5
   ```
   ```
   [*PE3-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE4
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE4] vlan batch 5
   ```
   ```
   [*PE4] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE4-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE4-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE4-GigabitEthernet0/1/1] port trunk allow-pass vlan 5
   ```
   ```
   [*PE4-GigabitEthernet0/1/1] smart-link flush enable control-vlan 5
   ```
   ```
   [*PE4-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE4] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE4-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*PE4-GigabitEthernet0/2/1] portswitch
   ```
   ```
   [*PE4-GigabitEthernet0/2/1] port trunk allow-pass vlan 5
   ```
   ```
   [*PE4-GigabitEthernet0/2/1] smart-link flush enable control-vlan 5
   ```
   ```
   [*PE4-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE4] commit
   ```
5. Verify the configuration. 
   
   
   
   # After the configuration is complete, check information about the Eth-Trunk interfaces in manual 1:1 master/backup mode. The command output shows the Eth-Trunk ID, manual 1:1 master/backup mode, and master interface information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display eth-trunk 1
   ```
   ```
   Eth-Trunk1's state information is:
   WorkingMode: BACKUP
   WorkingState: Master
   --------------------------------------------------------------------------------
   PortName                      Slave/Master
   GigabitEthernet0/1/1          M
   GigabitEthernet0/2/1          S
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  sysname PE1
  #
  vlan batch 5
  #
  interface Eth-Trunk1
   portswitch
   port trunk allow-pass vlan 5
   mode manual backup
   smart-link flush send vlan 5
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 1
   port-master
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  vlan batch 5
  #
  interface Eth-Trunk1
   portswitch
   port trunk allow-pass vlan 5
   mode manual backup
   smart-link flush send vlan 5
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 1
   port-master
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  vlan batch 5
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 5
   smart-link flush enable control-vlan 5
  #
  interface GigabitEthernet0/2/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 5
   smart-link flush enable control-vlan 5
  #
  return
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  vlan batch 5
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 5
   smart-link flush enable control-vlan 5
  #
  interface GigabitEthernet0/2/1
   portswitch
   undo shutdown
   port trunk allow-pass vlan 5
   smart-link flush enable control-vlan 5
  #
  return
  ```