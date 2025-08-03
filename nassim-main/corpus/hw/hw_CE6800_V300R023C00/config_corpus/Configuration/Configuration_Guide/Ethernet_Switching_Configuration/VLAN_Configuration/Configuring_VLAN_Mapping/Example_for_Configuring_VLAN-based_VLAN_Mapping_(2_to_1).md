Example for Configuring VLAN-based VLAN Mapping (2 to 1)
========================================================

Example for Configuring VLAN-based VLAN Mapping (2 to 1)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662391__fig265374023812), PC1 and PC3 connected to DeviceA belong to VLAN 2 and VLAN 3 respectively, and PC2 and PC4 connected to DeviceB belong to VLAN 2 and VLAN 3 respectively. QinQ is configured on DeviceC and DeviceD. VLAN mapping needs to be configured on DeviceE so that PCs in the same VLAN of different branches can communicate with each other.

![](public_sys-resources/note_3.0-en-us.png) 

VLAN-based VLAN mapping can be configured only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.


**Figure 1** Network diagram of configuring VLAN-based VLAN mapping (2 to 1)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000002150819682.png)

#### Procedure

1. Create VLAN 2 and VLAN 3 on DeviceA and add interfaces to the VLANs. The configuration of DeviceB is similar to that of DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 3
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 3
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 2 3
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. On DeviceC, configure 100GE 1/0/1 as a QinQ interface, and configure 100GE 1/0/1 to add an outer tag with VLAN ID 201 to packets. The configuration of DeviceD is similar to that of DeviceC.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 201
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type dot1q-tunnel
   [*DeviceC-100GE1/0/1] port default vlan 201
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type trunk
   [*DeviceC-100GE1/0/2] port trunk allow-pass vlan 201
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
3. Configure VLAN mapping on DeviceE. If a packet carries double VLAN tags (outer VLAN tag 201 and inner VLAN tag 2), DeviceE replaces both VLAN tags with VLAN tag 501. If a packet carries double VLAN tags (outer VLAN tag 201 and inner VLAN tag 3), DeviceE replaces both VLAN tags with VLAN tag 502.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceE
   [*HUAWEI] commit
   [~DeviceE] vlan batch 501 502
   [*DeviceE] interface 100ge 1/0/1
   [*DeviceE-100GE1/0/1] portswitch
   [*DeviceE-100GE1/0/1] port link-type trunk
   [*DeviceE-100GE1/0/1] port trunk allow-pass vlan 501 502
   [*DeviceE-100GE1/0/1] port vlan-mapping vlan 201 inner-vlan 2 map-single-vlan 501
   [*DeviceE-100GE1/0/1] port vlan-mapping vlan 201 inner-vlan 3 map-single-vlan 502
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] interface 100ge 1/0/2
   [*DeviceE-100GE1/0/2] portswitch
   [*DeviceE-100GE1/0/2] port link-type trunk
   [*DeviceE-100GE1/0/2] port trunk allow-pass vlan 501 502
   [*DeviceE-100GE1/0/2] port vlan-mapping vlan 201 inner-vlan 2 map-single-vlan 501
   [*DeviceE-100GE1/0/2] port vlan-mapping vlan 201 inner-vlan 3 map-single-vlan 502
   [*DeviceE-100GE1/0/2] quit
   [*DeviceE] interface 100ge 1/0/3
   [*DeviceE-100GE1/0/3] portswitch
   [*DeviceE-100GE1/0/3] port link-type trunk
   [*DeviceE-100GE1/0/3] port trunk allow-pass vlan 501 502
   [*DeviceE-100GE1/0/3] quit
   [*DeviceE] commit
   ```

#### Verifying the Configuration

PC1 and PC2 in the same VLAN can communicate with each other, and PC3 and PC4 in the same VLAN can communicate with each other. PCs in different VLANs cannot communicate with each other.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 2 to 3
  #
  interface 100GE1/0/1
   
   port default vlan 2
  #
  interface 100GE1/0/2
   
   port default vlan 3
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 2 to 3
  #
  interface 100GE1/0/1
   port default vlan 2
  #
  interface 100GE1/0/2
   port default vlan 3
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 201
  #
  interface 100GE1/0/1
   
   port link-type dot1q-tunnel
   port default vlan 201
  #
  interface 100GE1/0/2
   
   port link-type trunk
   port trunk allow-pass vlan 201
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 201
  #
  interface 100GE1/0/1
   port link-type dot1q-tunnel
   port default vlan 201
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 201
  #
  return
  ```
* DeviceE
  ```
  #
  sysname DeviceE
  #
  vlan batch 501 to 502
  #
  interface 100GE1/0/1
   port link-type trunk 
   port trunk allow-pass vlan 501 to 502
   port vlan-mapping vlan 201 inner-vlan 2 map-single-vlan 501
   port vlan-mapping vlan 201 inner-vlan 3 map-single-vlan 502
  #
  interface 100GE1/0/2
   port link-type trunk 
   port trunk allow-pass vlan 501 to 502
   port vlan-mapping vlan 201 inner-vlan 2 map-single-vlan 501
   port vlan-mapping vlan 201 inner-vlan 3 map-single-vlan 502
  #
  interface 100GE1/0/3
   port link-type trunk 
   port trunk allow-pass vlan 501 to 502
  #
  return
  ```