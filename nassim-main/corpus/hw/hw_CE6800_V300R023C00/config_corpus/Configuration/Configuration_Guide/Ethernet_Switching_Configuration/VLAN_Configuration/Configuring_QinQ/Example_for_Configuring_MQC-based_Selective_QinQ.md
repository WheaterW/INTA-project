Example for Configuring MQC-based Selective QinQ
================================================

Example for Configuring MQC-based Selective QinQ

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662417__fig10534133734710), PC1 and PC2 connected to DeviceA belong to VLAN 200 and VLAN 300, respectively, whereas PC3 and PC4 connected to DeviceD belong to VLAN 200 and VLAN 300, respectively, whereas PC1 and PC3 are on the same network segment, and PC2 and PC4 are on the same network segment. On the network between DeviceB and DeviceC, VLAN 2 is used for communication between PC1 and PC3, whereas VLAN 3 is used for communication between PC2 and PC4. MQC-based selective QinQ needs to be configured on DeviceB so that PC1 can unidirectionally access PC3 and PC2 can unidirectionally access PC4.

**Figure 1** Network diagram of configuring MQC-based selective QinQ![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176742379.png)

#### Procedure

1. Create VLANs and add interfaces to the VLANs.
   
   
   
   # Create VLAN 200 and VLAN 300 on DeviceA, add 100GE 1/0/2 to VLAN 200 and 100GE 1/0/3 to VLAN 300, and configure 100GE 1/0/1 to allow packets from VLAN 200 and VLAN 300 to pass through. The configuration of DeviceD is similar to that of DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 200 300
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 200 300
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 200
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 300
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Create VLAN 2 and VLAN 3 on DeviceB so that DeviceB can add an outer VLAN 2 or VLAN 3 tag to packets. Configure 100GE 1/0/1 and 100GE 1/0/2 to allow packets from the two VLANs to pass through.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2 3
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 2 3
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 2 3
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Create VLAN 2 and VLAN 3 on DeviceC, and configure 100GE 1/0/1 and 100GE 1/0/2 to allow packets from VLAN 2 and VLAN 3 to pass through.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 2 3
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] port link-type hybrid
   [*DeviceC-100GE1/0/1] port hybrid untagged vlan 2 3
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type hybrid
   [*DeviceC-100GE1/0/2] port hybrid untagged vlan 2 3
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
2. Configure traffic classifiers, traffic behaviors, and traffic policies.
   
   
   
   # Configure traffic classifiers, traffic behaviors, and a traffic policy on DeviceB to add an outer VLAN 2 tag to the packets sent from VLAN 200 and an outer VLAN 3 tag to the packets sent from VLAN 300.
   
   ```
   [~DeviceB] traffic classifier name1
   [*DeviceB-classifier-name1] if-match vlan 200
   [*DeviceB-classifier-name1] quit
   [*DeviceB] traffic behavior name1
   [*DeviceB-behavior-name1] vlan-stacking vlan 2
   [*DeviceB-behavior-name1] quit
   [*DeviceB] traffic classifier name2
   [*DeviceB-classifier-name2] if-match vlan 300
   [*DeviceB-classifier-name2] quit
   [*DeviceB] traffic behavior name2
   [*DeviceB-behavior-name2] vlan-stacking vlan 3
   [*DeviceB-behavior-name2] quit
   [*DeviceB] traffic policy name1
   [*DeviceB-trafficpolicy-name1] classifier name1 behavior name1
   [*DeviceB-trafficpolicy-name1] classifier name2 behavior name2
   [*DeviceB-trafficpolicy-name1] quit
   [*DeviceB] commit
   ```
3. Apply the traffic policy to a specified interface.
   
   
   
   # Apply the traffic policy to 100GE 1/0/1 of DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] traffic-policy name1 inbound
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

After the configuration is complete, PC1 can access PC3, and PC2 can access PC4.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 200 300
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 200 300
  #
  interface 100GE1/0/2
   port default vlan 200
  #
  interface 100GE1/0/3
   port default vlan 300
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
  traffic classifier name1 type or
   if-match vlan 200
  #
  traffic classifier name2 type or
   if-match vlan 300
  #
  traffic behavior name1
   vlan-stacking vlan 2
  #
  traffic behavior name2
   vlan-stacking vlan 3
  #
  traffic policy name1
   classifier name1 behavior name1 precedence 5
   classifier name2 behavior name2 precedence 10
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 3
   traffic-policy name1 inbound
  #
  interface 100GE1/0/2
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
  vlan batch 2 to 3
  #
  interface 100GE1/0/1
   port link-type hybrid
   port hybrid untagged vlan 2 to 3
  #
  interface 100GE1/0/2
   port link-type hybrid
   port hybrid untagged vlan 2 to 3
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 200 300
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 200 300
  #
  interface 100GE1/0/2
   port default vlan 200
  #
  interface 100GE1/0/3
   port default vlan 300
  #
  return
  ```