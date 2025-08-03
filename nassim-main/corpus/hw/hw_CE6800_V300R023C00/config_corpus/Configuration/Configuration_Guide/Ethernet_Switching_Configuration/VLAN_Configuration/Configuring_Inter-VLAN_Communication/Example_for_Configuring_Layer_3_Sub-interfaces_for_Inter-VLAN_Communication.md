Example for Configuring Layer 3 Sub-interfaces for Inter-VLAN Communication
===========================================================================

Example for Configuring Layer 3 Sub-interfaces for Inter-VLAN Communication

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176662397__fig10388155315573), hosts in VLAN 2 and VLAN 3 are on different network segments. Layer 3 sub-interface need to be configured on DeviceA so that hosts in VLAN 2 and VLAN 3 can communicate with each other.

**Figure 1** Networking diagram for configuring Layer 3 sub-interfaces to implement inter-VLAN communication![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001176662445.png)

#### Procedure

1. Create VLANs on DeviceB.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2 3
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] portswitch
   [*DeviceB-100GE1/0/1] port link-type access
   [*DeviceB-100GE1/0/1] port default vlan 2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type access
   [*DeviceB-100GE1/0/2] port default vlan 3
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
2. On DeviceB, configure 100GE 1/0/3 to allow packets from the VLANs to which users belong to pass through.
   
   
   ```
   [~DeviceB] interface 100ge 1/0/3
   [~DeviceB-100GE1/0/3] portswitch
   [~DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 2 3
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
3. Create sub-interfaces on DeviceA and associate them with VLANs.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/4
   [~DeviceA-100GE1/0/4] undo portswitch
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/4.1
   [*DeviceA-100GE1/0/4.1] dot1q termination vid 2 
   [*DeviceA-100GE1/0/4.1] quit
   [*DeviceA] interface 100ge 1/0/4.2
   [*DeviceA-100GE1/0/4.2] dot1q termination vid 3
   [*DeviceA-100GE1/0/4.2] quit
   [*DeviceA] commit
   ```
4. Configure IP addresses for the sub-interfaces on DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/4.1
   [~DeviceA-100GE1/0/4.1] ip address 10.10.10.2 24
   [*DeviceA-100GE1/0/4.1] quit
   [*DeviceA] interface 100ge 1/0/4.2
   [*DeviceA-100GE1/0/4.2] ip address 10.10.20.2 24
   [*DeviceA-100GE1/0/4.2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

On the hosts in VLAN 2 and VLAN 3, set the default gateway address to 10.10.10.2/24 (IP address of 100GE 1/0/4.1) and 10.10.20.2/24 (IP address of 100GE 1/0/4.2), respectively. After the configuration, the hosts in VLAN 2 and VLAN 3 can ping each other.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/4
   undo portswitch
  #
  interface 100GE1/0/4.1
   ip address 10.10.10.2 255.255.255.0
   encapsulation dot1q-termination
   dot1q termination vid 2
  #
  interface 100GE1/0/4.2
   ip address 10.10.20.2 255.255.255.0
   encapsulation dot1q-termination
   dot1q termination vid 3
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