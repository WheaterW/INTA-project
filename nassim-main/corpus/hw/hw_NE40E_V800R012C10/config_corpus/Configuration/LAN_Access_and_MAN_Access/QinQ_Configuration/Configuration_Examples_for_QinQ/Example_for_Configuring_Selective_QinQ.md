Example for Configuring Selective QinQ
======================================

This section provides an example for configuring Layer 2 selective QinQ. Layer 2 selective QinQ is an extension to Layer 2 QinQ tunneling and is more flexible. When receiving packets, a Layer 2 selective QinQ-enabled interface can add different outer tags depending on the inner tags of the packets, making user VLAN classification more fine-grained.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363294__en-us_task_0172363203_fig_dc_vrp_qinq_cfg_005101), company 1 and company 2 each have multiple offices.

* VLANs 2 to 500 are used on the network of company 1.
* VLANs 501 to 4094 are used on the network of company 2.
* GE 0/1/1 on Device A receives packets from different VLANs of company 1 and company 2.

Layer 2 selective QinQ is required on GE 0/1/1 of Device A on the carrier network so that the office networks of each company can communicate with each other, but the office networks of different companies cannot.

**Figure 1** Networking of selective QinQ![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/1, GE0/2/1, and GE0/3/1, respectively.


  
![](figure/en-us_image_0000001505350536.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure default outer VLAN IDs.
2. Configure Layer 2 selective QinQ on Layer 2 interfaces so that the interfaces can add different outer VLAN tags to packets.
3. Configure other Layer 2 selective QinQ-incapable interfaces to forward packets carrying a specific outer VLAN ID.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of the access interfaces of company 1 and company 2
* Outer VLAN IDs that Layer 2 interfaces on Device A and Device B add to packets from different companies

#### Procedure

1. Create default outer VLAN IDs on Layer 2 interfaces.
   
   
   
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
   [~DeviceA] vlan batch 10 20
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] vlan batch 20
   ```
   ```
   [*DeviceB] commit
   ```
2. Configure Layer 2 selective QinQ on Layer 2 interfaces.
   
   
   
   # Configure Device A.
   
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port vlan-stacking vlan 2 to 500 stack-vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port vlan-stacking vlan 1000 to 2000 stack-vlan 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/1] port vlan-stacking vlan 100 to 500 stack-vlan 10
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/1] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] port vlan-stacking vlan 1000 to 4094 stack-vlan 20
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/1] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/1] port vlan-stacking vlan 501 to 2500 stack-vlan 20
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/1] quit
   ```
3. Configure other interfaces.
   
   
   
   # Configure GE 0/3/1 on Device A to forward packets carrying outer VLAN ID 20.
   
   ```
   [*DeviceA] interface gigabitethernet 0/3/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/1] port trunk allow-pass vlan 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/3/1] quit
   ```
   
   # Configure GE 0/3/1 on Device B to forward packets carrying outer VLAN ID 20.
   
   ```
   [*DeviceB] interface gigabitethernet 0/3/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/1] portswitch
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/1] port trunk allow-pass vlan 20
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/1] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/1] quit
   ```
4. Verify the configuration.
   
   
   
   Hosts in different offices but the same VLAN can ping each other in company 1.
   
   Hosts in different offices but the same VLAN can ping each other in company 2.
   
   Hosts in company 1 and hosts in company 2 cannot ping each other.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
   vlan batch 10 20
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port vlan-stacking vlan 2 to 500 stack-vlan 10
  ```
  ```
   port vlan-stacking vlan 1000 to 2000 stack-vlan 20
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port vlan-stacking vlan 100 to 500 stack-vlan 10
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 20
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
   vlan batch 20
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port vlan-stacking vlan 1000 to 4094 stack-vlan 20
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port vlan-stacking vlan 501 to 2500 stack-vlan 20
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 20
  ```
  ```
  #
  ```
  ```
  return
  ```