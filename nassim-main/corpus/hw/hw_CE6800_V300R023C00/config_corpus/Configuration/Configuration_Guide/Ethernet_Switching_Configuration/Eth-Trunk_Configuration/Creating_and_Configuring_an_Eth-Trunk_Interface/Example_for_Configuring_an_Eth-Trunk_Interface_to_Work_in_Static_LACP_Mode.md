Example for Configuring an Eth-Trunk Interface to Work in Static LACP Mode
==========================================================================

Example for Configuring an Eth-Trunk Interface to Work in Static LACP Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176661237__fig_dc_cfg_eth-trunk_003501), DeviceA and DeviceB are connected through multiple links. A LAG in static LACP mode is configured on the two devices to improve bandwidth and reliability between them. The requirements are as follows:

* Traffic can be load balanced over two active links.
* One link between DeviceA and DeviceB functions as a backup link. If a fault occurs on an active link, the backup link replaces the faulty link to ensure reliable data transmission.

**Figure 1** Networking diagram of an Eth-Trunk in static LACP mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176661315.png)

#### Procedure

1. Create Eth-Trunk 1 on DeviceA and DeviceB and configure Eth-Trunk 1 to work in static LACP mode.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] mode lacp-static
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceB.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] mode lacp-static
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
2. Add member interfaces to the Eth-Trunk interface on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] eth-trunk 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] eth-trunk 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] eth-trunk 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   
   
   # Configure DeviceB.
   
   
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] eth-trunk 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] eth-trunk 1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] eth-trunk 1
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
3. Set the LACP system priority on DeviceA to 100 and retain the default LACP system priority on DeviceB so that DeviceA acts as the Actor.
   
   
   ```
   [~DeviceA] lacp priority 100
   [*DeviceA] commit
   ```
4. On DeviceA, set the upper threshold for the number of active interfaces to 2. The remaining link is used as a backup link.
   
   
   ```
   [~DeviceA] interface eth-trunk 1
   [~DeviceA-Eth-Trunk1] lacp max active-linknumber 2
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
5. Set LACP interface priorities and determine active interfaces on DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] lacp priority 100
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] lacp priority 100
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check Eth-Trunk information on DeviceA and DeviceB and check whether LACP negotiation is successful.

```
[~DeviceA] display eth-trunk 1
Eth-Trunk1's state information is:
Local:
LAG ID: 1                       Working Mode: Static
Preempt Delay: Disabled         Hash Arithmetic: profile default
System Priority: 100            System ID: xxxx-xxxx-xxxx
Least Active-linknumber: 1      Max Active-linknumber: 2
Operating Status: up            Number Of Up Ports In Trunk: 2
Timeout Period: Slow
--------------------------------------------------------------------------------
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/1              Selected 100GE     100     1      20289   10111100  1
100GE1/0/2              Selected 100GE     100     2      20289   10111100  1
100GE1/0/3              Unselect 100GE     32768   3      20289   10100000  1

Partner:
--------------------------------------------------------------------------------
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState
100GE1/0/1              32768    xxxx-xxxx-xxxx 32768   4      20289   10111100
100GE1/0/2              32768    xxxx-xxxx-xxxx 32768   5      20289   10111100
100GE1/0/3              32768    xxxx-xxxx-xxxx 32768   6      20289   10100000
```
```
[~DeviceB] display eth-trunk 1
Eth-Trunk1's state information is:
Local:
LAG ID: 1                       Working Mode: Static
Preempt Delay: Disabled         Hash Arithmetic: profile default
System Priority: 32768          System ID: xxxx-xxxx-xxxx
Least Active-linknumber: 1      Max Active-linknumber: 128
Operating Status: up            Number Of Up Ports In Trunk: 2
Timeout Period: Slow
--------------------------------------------------------------------------------
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/1              Selected 100GE     32768   4      20289   10111100  1
100GE1/0/2              Selected 100GE     32768   5      20289   10111100  1
100GE1/0/3              Unselect 100GE     32768   6      20289   10100000  1

Partner:
--------------------------------------------------------------------------------
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState
100GE1/0/1              100      xxxx-xxxx-xxxx  100     1      20289   10111100
100GE1/0/2              100      xxxx-xxxx-xxxx  100     2      20289   10111100
100GE1/0/3              100      xxxx-xxxx-xxxx  32768   3      20289   10100000
```

The command output shows that the LACP system priority of DeviceA is 100, which is higher than the LACP system priority of DeviceB. Member interfaces **100GE** **1/0/1** and **100GE** **1/0/2** are active interfaces and are in Selected state, and interface **100GE** **1/0/3** is in Unselect state. Load balancing and link backup are implemented.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  lacp priority 100
  #
  interface Eth-Trunk1 
   mode lacp-static                                                               
   lacp max active-linknumber 2                                                    
  #
  interface 100GE1/0/1
   eth-trunk 1
   lacp priority 100
  #
  interface 100GE1/0/2
   eth-trunk 1
   lacp priority 100
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
   mode lacp-static                                                                                                          
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