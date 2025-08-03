Example for Configuring VLAN-based VLAN Mapping (2 to 2)
========================================================

Example for Configuring VLAN-based VLAN Mapping (2 to 2)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176742299__fig21571951267), PC1 connected to DeviceA belongs to VLAN 10, and PC2 connected to DeviceF belongs to VLAN 30. QinQ is configured on DeviceB and DeviceE. The VLAN IDs planned for communication between DeviceC and DeviceD are different from those on the downstream network. VLAN mapping needs to be configured on DeviceC and DeviceD so that PCs in different VLANs of different branches can communicate with each other.

![](public_sys-resources/note_3.0-en-us.png) 

VLAN-based VLAN mapping can be configured only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.


**Figure 1** Network diagram of configuring VLAN-based VLAN mapping (2 to 2)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176662431.png)

#### Procedure

1. Create VLANs on DeviceA and DeviceF and add interfaces to the VLANs.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceF.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceF
   [*HUAWEI] commit
   [~DeviceF] vlan batch 30
   [*DeviceF] interface 100ge 1/0/1
   [*DeviceF-100GE1/0/1] portswitch
   [*DeviceF-100GE1/0/1] port link-type access
   [*DeviceF-100GE1/0/1] port default vlan 30
   [*DeviceF-100GE1/0/1] quit
   [*DeviceF] interface 100ge 1/0/2
   [*DeviceF-100GE1/0/2] portswitch
   [*DeviceF-100GE1/0/2] port link-type trunk
   [*DeviceF-100GE1/0/2] port trunk allow-pass vlan 30
   [*DeviceF-100GE1/0/2] quit
   [*DeviceF] commit
   ```
2. Configure QinQ on DeviceB and DeviceE.
   
   
   
   # On DeviceB, configure 100GE 1/0/1 as a QinQ interface, and configure 100GE 1/0/1 to add an outer tag with VLAN ID 20 to packets.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 20
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type dot1q-tunnel
   [*DeviceB-100GE1/0/1] port default vlan 20
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # On DeviceE, configure 100GE 1/0/1 as a QinQ interface, and configure 100GE 1/0/1 to add an outer tag with VLAN ID 40 to packets.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceE
   [*HUAWEI] commit
   [~DeviceE] vlan batch 40
   [*DeviceE] interface 100ge 1/0/1
   [*DeviceE-100GE1/0/1] portswitch
   [*DeviceE-100GE1/0/1] port link-type dot1q-tunnel
   [*DeviceE-100GE1/0/1] port default vlan 40
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] interface 100ge 1/0/2
   [*DeviceE-100GE1/0/2] portswitch
   [*DeviceE-100GE1/0/2] port link-type trunk
   [*DeviceE-100GE1/0/2] port trunk allow-pass vlan 40
   [*DeviceE-100GE1/0/2] quit
   [*DeviceE] commit
   ```
3. Configure VLAN mapping on DeviceC and DeviceD.
   
   
   
   # Configure VLAN mapping on 100GE 1/0/1 of DeviceC. If a packet carries double VLAN tags (outer VLAN tag 20 and inner VLAN tag 10), the outer VLAN tag is replaced with VLAN 50 and the inner VLAN tag is replaced with VLAN 60.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 50
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type trunk
   [*DeviceC-100GE1/0/1] port trunk allow-pass vlan 50
   [*DeviceC-100GE1/0/1] port vlan-mapping vlan 20 inner-vlan 10 map-vlan 50 map-inner-vlan 60
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type trunk
   [*DeviceC-100GE1/0/2] port trunk allow-pass vlan 50
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
   
   # Configure VLAN mapping on 100GE 1/0/1 of DeviceD. If a packet carries double VLAN tags (outer VLAN tag 40 and inner VLAN tag 30), the outer VLAN tag is replaced with VLAN 50 and the inner VLAN tag is replaced with VLAN 60.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] vlan batch 50
   [*DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] portswitch
   [*DeviceD-100GE1/0/1] port link-type trunk
   [*DeviceD-100GE1/0/1] port trunk allow-pass vlan 50
   [*DeviceD-100GE1/0/1] port vlan-mapping vlan 40 inner-vlan 30 map-vlan 50 map-inner-vlan 60
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] portswitch
   [*DeviceD-100GE1/0/2] port link-type trunk
   [*DeviceD-100GE1/0/2] port trunk allow-pass vlan 50
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

After PC1 and PC2 are configured with IP addresses on the same network segment, they can ping each other.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  vlan batch 20
  #
  interface 100GE1/0/1
   port link-type dot1q-tunnel
   port default vlan 20
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 20
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 50
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 50
   port vlan-mapping vlan 20 inner-vlan 10 map-vlan 50 map-inner-vlan 60
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 50
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 50
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 50
   port vlan-mapping vlan 40 inner-vlan 30 map-vlan 50 map-inner-vlan 60
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 50
  #
  return
  ```
* DeviceE
  ```
  #
  sysname DeviceE
  #
  vlan batch 40
  #
  interface 100GE1/0/1
   port link-type dot1q-tunnel
   port default vlan 40
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 40
  #
  return
  ```
* DeviceF
  ```
  #
  sysname DeviceF
  #
  vlan batch 30
  #
  interface 100GE1/0/1
   port default vlan 30
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 30
  #
  return
  ```