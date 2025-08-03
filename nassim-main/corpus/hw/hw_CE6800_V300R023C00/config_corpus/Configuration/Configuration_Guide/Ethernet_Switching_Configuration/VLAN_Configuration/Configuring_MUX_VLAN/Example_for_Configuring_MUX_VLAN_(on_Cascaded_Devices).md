Example for Configuring MUX VLAN (on Cascaded Devices)
======================================================

Example for Configuring MUX VLAN (on Cascaded Devices)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176662393__fig788783512161), it is required that all hosts can access the Internet, hosts in VLAN 3 can communicate with each other, and hosts in VLAN 4 cannot communicate with each other.

**Figure 1** Network diagram of configuring MUX VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130782684.png)

#### Procedure

1. Configure MUX VLAN.
   
   
   
   # Create VLAN 2 to VLAN 4 on DeviceB. Configure VLAN 2 as a principal VLAN, VLAN 3 as a group VLAN, and VLAN 4 as a separate VLAN.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] vlan batch 2 3 4
   [*DeviceB] vlan 2
   [*DeviceB-vlan2] mux-vlan
   [*DeviceB-vlan2] subordinate group 3
   [*DeviceB-vlan2] subordinate separate 4
   [*DeviceB-vlan2] quit
   [*DeviceB] commit
   ```
   
   # Create VLAN 2 to VLAN 4 on DeviceC. Configure VLAN 2 as a principal VLAN, VLAN 3 as a group VLAN, and VLAN 4 as a separate VLAN.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 2 3 4
   [*DeviceC] vlan 2
   [*DeviceC-vlan2] mux-vlan
   [*DeviceC-vlan2] subordinate group 3
   [*DeviceC-vlan2] subordinate separate 4
   [*DeviceC-vlan2] quit
   [*DeviceC] commit
   ```
   
   # Create VLAN 2 to VLAN 4 on DeviceD. Configure VLAN 2 as a principal VLAN, VLAN 3 as a group VLAN, and VLAN 4 as a separate VLAN.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] vlan batch 2 3 4
   [*DeviceD] vlan 2
   [*DeviceD-vlan2] mux-vlan
   [*DeviceD-vlan2] subordinate group 3
   [*DeviceD-vlan2] subordinate separate 4
   [*DeviceD-vlan2] quit
   [*DeviceD] commit
   ```
2. Add uplink interface 1 of DeviceB to VLAN 2, enable the MUX VLAN function on interface 1, and configure downlink interface 2 and interface 3 to allow packets from VLAN 2 to VLAN 4 to pass through.
   
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] portswitch
   [~DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 2
   [*DeviceB-100GE1/0/1] port mux-vlan enable vlan 2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] portswitch
   [*DeviceB-100GE1/0/2] port link-type trunk
   [*DeviceB-100GE1/0/2] port trunk allow-pass vlan 2 to 4
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] portswitch
   [*DeviceB-100GE1/0/3] port link-type trunk
   [*DeviceB-100GE1/0/3] port trunk allow-pass vlan 2 to 4
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
3. Configure uplink interface 1 of DeviceC to allow packets from VLAN 2 to VLAN 4 to pass through, add downlink interface 2 and interface 3 to VLAN 3, and enable the MUX VLAN function on interface 2 and interface 3.
   
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] portswitch
   [~DeviceC-100GE1/0/1] port link-type trunk
   [*DeviceC-100GE1/0/1] port trunk allow-pass vlan 2 to 4
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] portswitch
   [*DeviceC-100GE1/0/2] port link-type access
   [*DeviceC-100GE1/0/2] port default vlan 3
   [*DeviceC-100GE1/0/2] port mux-vlan enable vlan 3
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] portswitch
   [*DeviceC-100GE1/0/3] port link-type access
   [*DeviceC-100GE1/0/3] port default vlan 3
   [*DeviceC-100GE1/0/3] port mux-vlan enable vlan 3
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
4. Configure uplink interface 1 of DeviceD to allow packets from VLAN 2 to VLAN 4 to pass through, add downlink interface 2 and interface 3 to VLAN 4, and enable the MUX VLAN function on interface 2 and interface 3.
   
   
   ```
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] portswitch
   [~DeviceD-100GE1/0/1] port link-type trunk
   [*DeviceD-100GE1/0/1] port trunk allow-pass vlan 2 to 4
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] portswitch
   [*DeviceD-100GE1/0/2] port link-type access
   [*DeviceD-100GE1/0/2] port default vlan 4
   [*DeviceD-100GE1/0/2] port mux-vlan enable vlan 4
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/3
   [*DeviceD-100GE1/0/3] portswitch
   [*DeviceD-100GE1/0/3] port link-type access
   [*DeviceD-100GE1/0/3] port default vlan 4
   [*DeviceD-100GE1/0/3] port mux-vlan enable vlan 4
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] commit
   ```
5. Create VLANIF 2 on DeviceA, configure the IP address 10.1.1.1 24 for VLANIF 2, and add interface 1 to VLAN 2.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 2
   [*DeviceA-Vlanif2] ip address 10.1.1.1 24
   [*DeviceA-Vlanif2] quit
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the MUX VLAN contains multiple group VLANs and they need to communicate with each other, run the **arp proxy intra-vlan enable** command on the VLANIF interface of DeviceA to configure intra-VLAN proxy ARP.
6. Configure IP addresses for hosts on the network and ensure that the IP addresses are on the same network segment as the IP address of VLANIF 2 on DeviceA.

#### Verifying the Configuration

* Host1, Host2, Host3, and Host4 can access the Internet.
* Host1 and Host2 can ping each other.
* Host3 and Host4 cannot ping each other.
* Host1 and Host2 in VLAN 3 and Host3 and Host4 in VLAN 4 cannot ping each other.

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 2
  #
  interface Vlanif2
   ip address 10.10.10.1 255.255.255.0
  #
  interface 100GE1/0/1
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
  vlan batch 2 to 4
  #
  vlan 2
   mux-vlan
   subordinate separate 4
   subordinate group 3
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2
   port mux-vlan enable vlan 2
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 2 to 4
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 2 to 4
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 2 to 4
  #
  vlan 2
   mux-vlan
   subordinate separate 4
   subordinate group 3
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 4
  #
  interface 100GE1/0/2
   port default vlan 3
   port mux-vlan enable vlan 3
  #
  interface 100GE1/0/3
   port default vlan 3
   port mux-vlan enable vlan 3
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  vlan batch 2 to 4
  #
  vlan 2
   mux-vlan
   subordinate separate 4
   subordinate group 3
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 2 to 4
  #
  interface 100GE1/0/2
   port default vlan 4
   port mux-vlan enable vlan 4
  #
  interface 100GE1/0/3
   port default vlan 4
   port mux-vlan enable vlan 4
  #
  return
  ```