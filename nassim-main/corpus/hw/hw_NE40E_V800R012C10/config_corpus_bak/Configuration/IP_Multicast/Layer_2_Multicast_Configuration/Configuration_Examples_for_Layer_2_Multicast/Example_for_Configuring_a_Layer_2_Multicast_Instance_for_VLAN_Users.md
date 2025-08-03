Example for Configuring a Layer 2 Multicast Instance for VLAN Users
===================================================================

This section provides an example for configuring a Layer 2 multicast instance for VLAN users who request for the same multicast group's data from the same source.

#### Networking Requirements

In conventional multicast on-demand mode, if users in different VLANs orders data of the same multicast source from one device, the device has to send a copy of multicast data to each user. Such implementation wastes bandwidth resources and burdens the upstream device. For example, on the network shown in [Figure 1](#EN-US_TASK_0172368003__fig_dc_vrp_l2mc_cfg_006901), the PE connects to a device on the multicast source side, and the CE connects to users. Users in different VLANs request the same multicast data.

To enable the CE to request for only one single of each flow from the PE for all the users in the VLANs, configure a Layer 2 multicast instance. To facilitate data forwarding management, specify a multicast channel for the Layer 2 multicast instance.

**Figure 1** Configuring a Layer 2 multicast instance for VLAN users  
![](images/fig_dc_vrp_l2mc_cfg_006901.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VLANs and enable basic IGMP snooping functions.
2. Configure static Layer 2 multicast groups for VLANs.
3. Create a Layer 2 multicast instance.
4. Specify a channel for the Layer 2 multicast instance.
5. Configure the multicast instance and user instances for the Layer 2 multicast instance.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast channel addresses and static multicast group addresses
* ID of the VLAN to be configured as the multicast instance, and IDs of the VLANs to be configured as user instances

#### Procedure

1. Create VLANs.
   
   
   
   # Create VLANs on the CE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] vlan 3
   ```
   ```
   [*CE-vlan3] quit
   ```
   ```
   [*CE] vlan 11
   ```
   ```
   [*CE-vlan11] quit
   ```
   ```
   [*CE] vlan 22
   ```
   ```
   [*CE-vlan22] quit
   ```
   ```
   [*CE] commit
   ```
2. Enable IGMP snooping on the CE.
   
   
   ```
   [~CE] igmp-snooping enable
   ```
3. On the CE, configure GE 0/2/0 to permit the data frames of VLAN 11, and add this interface to the multicast group 225.0.0.1.
   
   
   ```
   [~CE] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/2/0] port trunk allow-pass vlan 11
   ```
   ```
   [*CE-GigabitEthernet0/2/0] l2-multicast static-group group-address 225.0.0.1 vlan 11
   ```
   ```
   [*CE-GigabitEthernet0/2/0] commit
   ```
   ```
   [~CE-GigabitEthernet0/2/0] quit
   ```
4. On the CE, configure GE 0/3/0 to permit the data frames of VLAN 22, and add this interface to the multicast group 225.0.0.1.
   
   
   ```
   [~CE] interface gigabitethernet 0/3/0
   ```
   ```
   [*CE-GigabitEthernet0/3/0] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/3/0] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/3/0] port trunk allow-pass vlan 22
   ```
   ```
   [*CE-GigabitEthernet0/3/0] l2-multicast static-group group-address 225.0.0.1 vlan 22
   ```
   ```
   [*CE-GigabitEthernet0/3/0] commit
   ```
   ```
   [~CE-GigabitEthernet0/3/0] quit
   ```
5. On the CE, configure GE 0/1/0 to permit only the data frames of VLAN 3.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The following configurations apply only to the Layer 2 multicast instance deployment scenario. In other cases, you need to configure GE 0/2/0 to permit the data frames of both VLANs 11 and 22.
   
   ```
   [~CE] interface gigabitethernet 0/1/0
   ```
   ```
   [*CE-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/0] port trunk allow-pass vlan 3
   ```
   ```
   [*CE-GigabitEthernet0/1/0] commit
   ```
   ```
   [~CE-GigabitEthernet0/1/0] quit
   ```
6. On the CE, enable IGMP snooping for VLAN 3.
   
   
   ```
   [~CE] vlan 3
   ```
   ```
   [~CE-vlan3] igmp-snooping enable
   ```
   ```
   [*CE-vlan3] commit
   ```
   ```
   [~CE-vlan3] quit
   ```
7. Create a Layer 2 multicast instance and enter the instance view.
   
   
   ```
   [~CE] l2-multicast instance 1
   ```
8. Specify a multicast channel for the Layer 2 multicast instance.
   
   
   ```
   [*CE-l2-minst1] import-channel 225.0.0.0 24
   ```
9. Configure a VLAN as the multicast instance for the Layer 2 multicast instance.
   
   
   ```
   [*CE-l2-minst1] multicast-instance vlan 3
   ```
10. Configure VLANs as user instances for the Layer 2 multicast instance.
    
    
    ```
    [*CE-l2-minst1] user-instance vlan 11 22
    ```
    ```
    [*CE-l2-minst1] commit
    ```
    ```
    [~CE-l2-minst1] quit
    ```
11. Verify the configuration.
    
    
    
    # Run the [**display l2-multicast instance**](cmdqueryname=display+l2-multicast+instance) command on the CE to check information about the multicast instance, user instances, and channel of the Layer 2 multicast instance.
    
    ```
    [CE] display l2-multicast instance
    ```
    ```
    L2-multicast instance ID: 1
    Multicast-instance: VLAN 3
    Multicast channels:
     225.0.0.0/24
    User-instance count: 2
    User-instance List:
    VLAN List:
     VLAN 11 22
    ```

#### Configuration Files

* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan batch 3 11 22
  #
  igmp-snooping enable
  #
  vlan 3
   igmp-snooping enable
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port trunk allow-pass vlan 3
  #
  interface GigabitEthernet0/2/0
   portswitch
   undo shutdown
   port trunk allow-pass vlan 11
   l2-multicast static-group group-address 225.0.0.1 vlan 11
  #
  interface GigabitEthernet0/3/0
   portswitch
   undo shutdown
   port trunk allow-pass vlan 22
   l2-multicast static-group group-address 225.0.0.1 vlan 22
  #
  l2-multicast instance 1
   multicast-instance vlan 3
   import-channel 225.0.0.0 255.255.255.0
   user-instance vlan 11 22
  #
  return
  ```