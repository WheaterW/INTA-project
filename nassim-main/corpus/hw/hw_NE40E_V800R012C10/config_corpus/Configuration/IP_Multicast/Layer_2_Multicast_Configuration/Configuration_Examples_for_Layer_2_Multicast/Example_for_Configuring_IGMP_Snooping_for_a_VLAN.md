Example for Configuring IGMP Snooping for a VLAN
================================================

This section provides an example for configuring IGMP snooping for a VLAN in typical Layer 2 networking.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367966__fig_dc_vrp_l2mc_cfg_003401), GE 0/1/0 on DeviceA is connected to an upstream multicast Router, DeviceB. DeviceA is connected to SwitchA and SwitchB, which belong to VLAN 3.

If DeviceA does not support IGMP snooping, multicast data traffic will be broadcast to SwitchA and SwitchB, wasting network resources.

After IGMP snooping is enabled on DeviceA, multicast data traffic will be sent only to access devices connected to multicast receivers.

In the network with a stable topology, if hosts connected to DeviceA need to receive multicast data for a long period of time, the interface connecting DeviceA to DeviceB can be configured as a router interface.

**Figure 1** Example for configuring IGMP Snooping for a VLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_l2mc_cfg_003401.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VLANs.
2. Configure basic IGMP snooping functions.
3. Configure GE 0/1/0 on DeviceA as a static router port.

#### Data Preparation

To complete the configuration, you need the following data:

* GE 0/1/0 as a static router port
* VLAN 3 to which SwitchA, SwitchB, and the switches connected to them belong

#### Procedure

1. Configure VLANs.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] vlan 3
   ```
   ```
   [*DeviceA-vlan3] port gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-vlan3] port gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-vlan3] commit
   ```
   ```
   [~DeviceA-vlan3] quit
   ```
2. Enable IGMP snooping on the Router.
   
   
   
   # Enable global IGMP snooping on DeviceA.
   
   ```
   [~DeviceA] igmp-snooping enable
   ```
   
   # On DeviceA, enable global IGMP snooping for VLAN 3.
   
   ```
   [~DeviceA] vlan 3
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
3. Configure GE 0/1/0 on DeviceA as a static router port.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] port link-type access
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] port default vlan 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] igmp-snooping static-router-port vlan 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   # Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) command on DeviceA.
   
   ```
   [~DeviceA] display igmp-snooping vlan configuration
   ```
   ```
    IGMP Snooping Configuration for VLAN 3
   ```
   ```
        igmp-snooping enable
   ```
   
   # Run the [**display igmp-snooping router-port vlan 3**](cmdqueryname=display+igmp-snooping+router-port+vlan+3) command on Device A.
   
   ```
   [~DeviceA] display igmp-snooping router-port vlan 3
   ```
   ```
    Port Name                         UpTime        Expires       Flags
   ```
   ```
    ---------------------------------------------------------------------
   ```
   ```
    VLAN 3, 1 router-port(s)
   ```
   ```
    GigabitEthernet0/1/0            00:01:02      --            STATIC
   ```
   
   The preceding command output shows that GE 0/1/0 is configured as a static router port.

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
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type access
  ```
  ```
   port default vlan 3
  ```
  ```
   igmp-snooping static-router-port vlan 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port default vlan 3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port default vlan 3
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
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
   multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.252
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
  area 0.0.0.0
  ```
  ```
  network 10.1.1.1 0.0.0.3
  ```
  ```
  #
  ```
  ```
  return
  ```