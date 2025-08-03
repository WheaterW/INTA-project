Example for Configuring Link Aggregation in Manual Load Balancing Mode
======================================================================

Example for Configuring Link Aggregation in Manual Load Balancing Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001413234641__fig_dc_cfg_eth-trunk_003401), DeviceA and DeviceB are connected through Layer 2 links and connected to devices in VLAN 10 and VLAN 20. DeviceA and DeviceB need to provide high bandwidth to implement load balancing and allow devices in the same VLAN to communicate with each other. In addition, redundancy is required to ensure data transmission and link reliability.

**Figure 1** Networking diagram of configuring link aggregation in manual load balancing mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5, respectively.


  
![](figure/en-us_image_0000001691109045.png)

#### Procedure

1. Create Eth-Trunk 1 on DeviceA and DeviceB and configure Eth-Trunk 1 to work in manual mode.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] portswitch
   [*DeviceA-Eth-Trunk1] mode manual load-balance
   [*DeviceA-Eth-Trunk1] commit 
   ```
   
   
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] portswitch
   [*DeviceB-Eth-Trunk1] mode manual load-balance
   [*DeviceB-Eth-Trunk1] commit 
   ```
2. Create VLANs on DeviceA and DeviceB and add interfaces to the VLANs.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] port link-type trunk
   [*DeviceA-100GE1/0/4] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/5
   [*DeviceA-100GE1/0/5] port link-type trunk
   [*DeviceA-100GE1/0/5] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] commit
   ```
   # Configure DeviceB.
   ```
   [~DeviceB] vlan batch 10 20
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] port link-type trunk
   [*DeviceB-100GE1/0/4] port trunk allow-pass vlan 10
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/5
   [*DeviceB-100GE1/0/5] port link-type trunk
   [*DeviceB-100GE1/0/5] port trunk allow-pass vlan 20
   [*DeviceB-100GE1/0/5] quit
   [*DeviceB] commit
   ```
3. Add member interfaces to the Eth-Trunk on DeviceA and DeviceB, and configure the Eth-Trunk interface to allow packets from VLAN 10 and VLAN 20 to pass through.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceB] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] port link-type trunk
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/3 
   [*DeviceA-Eth-Trunk1] port trunk allow pass vlan 10 20
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceB.
   
   
   
   ```
   [~DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] port link-type trunk
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/3 
   [*DeviceB-Eth-Trunk1] port trunk allow pass vlan 10 20
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
4. Configure a load balancing mode for Eth-Trunk 1 on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] load-balance src-dst-mac
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceB.
   
   
   
   ```
   [~DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] load-balance src-dst-mac
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

Run the **display eth-trunk 1** command in any view to check whether the Eth-Trunk interface is created successfully and whether member interfaces are added to the Eth-Trunk interface.

```
[~DeviceA] display eth-trunk 1
Eth-Trunk1's state information is: 
Working Mode: Normal           Hash Arithmetic: profile default
Least Active-linknumber: 1     Max Bandwidth-affected-linknumber: 16
Operating Status: up           Number of Up Ports in Trunk: 3
--------------------------------------------------------------------------------
PortName                        Status       Weight
100GE1/0/1                       Up           1
100GE1/0/2                       Up           1
100GE1/0/3                       Up           1
```

The command output shows that Eth-Trunk 1 has three member interfaces: **100GE** **1/0/1**, **100GE** **1/0/2**, and **100GE** **1/0/3** and that these member interfaces are in up state. The **Operating Status** of Eth-Trunk 1 is up.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  # 
  interface Eth-Trunk1
   portswitch
  # 
  interface 100GE1/0/1 
   eth-trunk 1
  # 
  interface 100GE1/0/2
   eth-trunk 1
  # 
  interface 100GE1/0/3
   eth-trunk 1
  #
  interface 100GE1/0/4   
   port link-type trunk   
   port trunk allow-pass vlan 10 
  # 
  interface 100GE1/0/5   
   port link-type trunk   
   port trunk allow-pass vlan 20
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  # 
  interface Eth-Trunk1
   portswitch
  # 
  interface 100GE1/0/1 
   eth-trunk 1
  # 
  interface 100GE1/0/2
   eth-trunk 1
  # 
  interface 100GE1/0/3
   eth-trunk 1
  #
  interface 100GE1/0/4   
   port link-type trunk   
   port trunk allow-pass vlan 10 
  # 
  interface 100GE1/0/5   
   port link-type trunk   
   port trunk allow-pass vlan 20
  #
  return
  ```