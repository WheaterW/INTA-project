Example for Adding Double VLAN Tags to Untagged Packets
=======================================================

Example for Adding Double VLAN Tags to Untagged Packets

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001310525589__fig10534133734710), PC1 and PC2 need to send untagged packets to each other and receive only untagged packets from each other. During transmission on the backbone network, double VLAN tags need to be added to untagged packets to conserve VLAN IDs on the public network and isolate services of different users.

**Figure 1** Network diagram of adding double VLAN tags to untagged packets![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001262485712.png)

#### Procedure

1. Create VLANs.
   
   
   
   # Create VLAN 2 (the outer VLAN IDs to be added) on 100GE 1/0/1 of DeviceA. The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 2
   [*DeviceA] commit
   ```
2. Create VLANs and add interfaces to the VLANs.
   
   
   
   # Configure 100GE 1/0/1 on DeviceA to add double tags to untagged packets. The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type hybrid
   [*DeviceA-100GE1/0/1] port hybrid untagged vlan 2
   [*DeviceA-100GE1/0/1] port vlan-stacking untagged stack-vlan 2 stack-inner-vlan 200
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
3. Add the outbound interfaces to the outer VLANs.
   
   
   
   # Configure 100GE 1/0/2 on DeviceA to allow packets from VLAN 2 to pass through. The configuration of DeviceB is similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] portswitch
   [~DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

After completing the configuration, verify that DeviceA can add double VLAN tags to the packets sent by PC1 and that PC2 can receive untagged packets.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan 2
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid untagged vlan 2
   port vlan-stacking untagged stack-vlan 2 stack-inner-vlan 200
   #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan 2
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid untagged vlan 2
   port vlan-stacking untagged stack-vlan 2 stack-inner-vlan 200
   #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2
  #
  return
  ```