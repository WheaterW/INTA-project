Example for Adding an Interface to a Multicast Group Statically
===============================================================

This section provides an example for configuring static multicast groups in typical VLAN networking.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367972__fig_dc_vrp_l2mc_cfg_003601), GE 0/1/1 on DeviceA is connected to a Router, and GE 0/1/2 on the DeviceA is connected to a switch. It is required that all the hosts in VLAN 3 should receive the multicast packets from the multicast group 225.0.0.1.

**Figure 1** Networking diagram of adding an interface to a multicast group statically![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_l2mc_cfg_003601.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN.
2. Add interfaces to the VLAN.
3. Add an interface to a multicast group statically.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address: 225.0.0.1
* ID of the VLAN to which a switch and connected host devices belong: 3
* GE 0/1/1 as the interface to a multicast group statically

#### Procedure

1. Create a VLAN.
   
   
   
   # Create VLAN 3 on DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] igmp-snooping enable
   ```
   ```
   [*DeviceA] vlan 3
   ```
   ```
   [*DeviceA-vlan3] igmp-snooping enable
   ```
   ```
   [*DeviceA-vlan3] commit
   ```
   ```
   [~DeviceA-vlan3] quit
   ```
2. Add interfaces to the VLAN.
   
   
   
   # Configure GE0/1/2 on DeviceA to allow data frames of VLAN 3 to pass through.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] port trunk allow-pass vlan 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Configure GE0/1/1 on DeviceA to allow data frames of VLAN 3 to pass through.
   
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] port trunk allow-pass vlan 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
3. Add GE0/1/2 on DeviceA to the multicast group 225.0.0.1 statically.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] l2-multicast static-group group-address 225.0.0.1 vlan 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
4. Verify the configuration.
   
   
   
   # Run the **display igmp-snooping port-info** command on DeviceA to check member ports of the multicast group 225.0.0.1.
   
   ```
   [~DeviceA] display igmp-snooping port-info
    -----------------------------------------------------------------------------------
     Flag: S:Static     D:Dynamic     M:Ssm-mapping
           A:Active     P:Protocol    F:Fast-channel                                
                       (Source, Group)  Port                                      Flag
    -----------------------------------------------------------------------------------
    VLAN 3, 1 Entry(s)
                         (*, 225.0.0.1)                                            P--
                                         GE0/1/2                                   S--
                                                           1 port(s) include
    -----------------------------------------------------------------------------------
   ```

#### Configuration Files

* DeviceA configuration file
  
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
  vlan batch 3
  ```
  ```
  #
  ```
  ```
  igmp-snooping enable
  ```
  ```
  #
  ```
  ```
  vlan 3
  ```
  ```
   igmp-snooping enable
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
   port trunk allow-pass vlan 3
  ```
  ```
  #
  ```
  ```
  interface  GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port trunk allow-pass vlan 3
  ```
  ```
   l2-multicast static-group group-address 225.0.0.1 vlan 3
  ```
  ```
  #
  ```
  ```
  return
  ```