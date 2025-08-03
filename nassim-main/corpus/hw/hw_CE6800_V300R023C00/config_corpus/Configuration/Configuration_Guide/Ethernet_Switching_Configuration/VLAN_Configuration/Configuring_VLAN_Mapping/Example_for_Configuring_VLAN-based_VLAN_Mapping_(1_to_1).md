Example for Configuring VLAN-based VLAN Mapping (1 to 1)
========================================================

Example for Configuring VLAN-based VLAN Mapping (1 to 1)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782640__fig8627748238), PC1 and PC2 connected to DeviceA belong to VLAN 5, and PC3 and PC4 connected to DeviceC belong to VLAN 6. PC1, PC2, PC3, and PC4 are on the same network segment. It is required that PCs in different VLANs communicate with each other through 1 to 1 VLAN mapping on DeviceB.

![](public_sys-resources/note_3.0-en-us.png) 

VLAN-based VLAN mapping can be configured only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.


**Figure 1** Network diagram of configuring VLAN-based VLAN mapping (1 to 1)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662441.png)

#### Procedure

1. Add 100GE 1/0/1 and 100GE 1/0/2 of DeviceA to VLAN 5 and configure 100GE 1/0/3 to allow packets from VLAN 5 to pass through.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 5
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 5
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 5
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 5
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. Add 100GE 1/0/1 and 100GE 1/0/2 of DeviceC to VLAN 6 and configure 100GE 1/0/3 to allow packets from VLAN 6 to pass through.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 6
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type access
   [*DeviceC-100GE1/0/1] port default vlan 6
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type access
   [*DeviceC-100GE1/0/2] port default vlan 6
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] portswitch
   [*DeviceC-100GE1/0/3] port link-type trunk
   [*DeviceC-100GE1/0/3] port trunk allow-pass vlan 6
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
3. Configure VLAN mapping on 100GE 1/0/1 of DeviceB and configure 100GE 1/0/1 and 100GE 1/0/2 to allow packets from VLAN 6 to pass through.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 6
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 6
   [*DeviceB-100GE1/0/1] port vlan-mapping vlan 5 map-vlan 6
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 6
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

PC1 or PC2 in VLAN 5 and PC3 or PC4 in VLAN 6 can ping each other.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 5
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 5
  #
  interface 100GE1/0/2
   port link-type access
   port default vlan 5
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 5
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 6
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 6
   port vlan-mapping vlan 5 map-vlan 6
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 6
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 6
  #
  interface 100GE1/0/1
   port link-type access
   port default vlan 6
  #
  interface 100GE1/0/2
   port link-type access
   port default vlan 6
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 6
  #
  return
  ```