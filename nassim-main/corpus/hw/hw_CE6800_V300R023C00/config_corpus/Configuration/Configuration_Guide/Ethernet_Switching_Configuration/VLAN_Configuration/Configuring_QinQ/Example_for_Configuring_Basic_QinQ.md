Example for Configuring Basic QinQ
==================================

Example for Configuring Basic QinQ

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782620__fig7135457586), DeviceA and DeviceB located in different areas are connected to user networks A and B, and connected to each other through the public network. On the public network, VLAN 100 and VLAN 200 are assigned for user networks A and B to transmit traffic, respectively. Basic QinQ needs to be configured on DeviceA and DeviceB so that VLANs can be divided in user networks A and B separately without affecting each other, users in user network A connected to DeviceA can communicate with users in the same network connected to DeviceB, and users in different user networks are isolated from each other.

**Figure 1** Networking diagram for configuring basic QinQ![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130622880.png)![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.




#### Procedure

1. Create VLANs.
   
   
   
   # Create VLAN 100 and VLAN 200 on DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 100 200
   [*DeviceA] commit
   ```
   
   # Create VLAN 100 and VLAN 200 on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 100 200
   [*DeviceB] commit
   ```
2. On DeviceA, configure 100GE 1/0/1 and 100GE 1/0/2 as QinQ interfaces, configure 100GE 1/0/1 to add an outer tag with VLAN ID 100 to packets, and configure 100GE 1/0/2 to add an outer tag with VLAN ID 200 to packets. The configuration of DeviceB is similar to that of DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type dot1q-tunnel
   [*DeviceA-100GE1/0/1] port default vlan 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type dot1q-tunnel
   [*DeviceA-100GE1/0/2] port default vlan 200
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
3. Add 100GE 1/0/3 on DeviceA to VLAN 100 and VLAN 200. The configuration of DeviceB is similar to that of DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/3
   [~DeviceA-100GE1/0/3] portswitch
   [~DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 100 200
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

* Any host on user network A connected to DeviceA can successfully ping a host in the same VLAN on user network A connected to DeviceB.
* Any host on user network B connected to DeviceA can successfully ping a host in the same VLAN on user network B connected to DeviceB.
* Any host on user network A connected to DeviceA cannot ping a host in the same VLAN on user network B connected to DeviceB.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 100 200
  #
  interface 100GE1/0/1
   port link-type dot1q-tunnel
   port default vlan 100
  #
  interface 100GE1/0/2
   port link-type dot1q-tunnel
   port default vlan 200
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 100 200
  #
  interface 100GE1/0/1
   port link-type dot1q-tunnel
   port default vlan 100
  #
  interface 100GE1/0/2
   port link-type dot1q-tunnel
   port default vlan 200
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 100 200
  #
  return
  ```