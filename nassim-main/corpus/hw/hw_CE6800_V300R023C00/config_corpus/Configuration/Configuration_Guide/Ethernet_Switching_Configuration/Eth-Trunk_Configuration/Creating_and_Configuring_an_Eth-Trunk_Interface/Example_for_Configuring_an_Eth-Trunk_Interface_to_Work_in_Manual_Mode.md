Example for Configuring an Eth-Trunk Interface to Work in Manual Mode
=====================================================================

Example for Configuring an Eth-Trunk Interface to Work in Manual Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130781474__fig_dc_cfg_eth-trunk_003401), DeviceA and DeviceB are connected through multiple links, requiring high bandwidth for traffic load balancing. These links need to be bundled into an Eth-Trunk to ensure data transmission and link reliability.

**Figure 1** Networking diagram of an Eth-Trunk in manual mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130621750.png)

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
2. Add member interfaces to the Eth-Trunk interface on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceA-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/3 
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceB.
   
   
   
   ```
   [~DeviceB-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/3 
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

Run the **display eth-trunk 1** command in any view to check whether the Eth-Trunk interface is created and whether member interfaces are added to the Eth-Trunk interface.

```
[~DeviceA] display eth-trunk 1
Eth-Trunk1's state information is: 
Working Mode: Normal           Hash Arithmetic: profile default
Least Active-linknumber: 1     Max Bandwidth-affected-linknumber: 128
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
  return
  ```