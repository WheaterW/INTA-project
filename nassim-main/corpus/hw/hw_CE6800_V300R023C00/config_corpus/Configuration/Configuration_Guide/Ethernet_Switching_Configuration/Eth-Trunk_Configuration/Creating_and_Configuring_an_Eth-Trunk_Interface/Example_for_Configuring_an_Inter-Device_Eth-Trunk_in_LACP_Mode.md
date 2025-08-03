Example for Configuring an Inter-Device Eth-Trunk in LACP Mode
==============================================================

Example for Configuring an Inter-Device Eth-Trunk in LACP Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176741159__fig_01), DeviceA connects to DeviceB and DeviceC using an inter-device Eth-Trunk. An Eth-Trunk interface in LACP mode is configured on DeviceA and its member interfaces are connected to 100GE 1/0/1 and 100GE 1/0/2 on DeviceB and DeviceC. The interfaces 100GE 1/0/1 and 100GE 1/0/2 work at the same rate and in the same duplex mode. Traffic needs to be load balanced between DeviceB and DeviceC.

**Figure 1** Networking diagram for configuring an inter-device Eth-Trunk in LACP mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001130621760.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create Eth-Trunk 1 on DeviceA, DeviceB, and DeviceC, configure Eth-Trunk 1 to work in static LACP mode, and add member interfaces to Eth-Trunk 1.
2. Configure the same LACP system ID on DeviceB and DeviceC.
3. Configure the same LACP system priority on DeviceB and DeviceC.
4. On DeviceC, increase the numbers of Eth-Trunk member interfaces by 32768, so that the numbers of Eth-Trunk member interfaces in LACP mode on DeviceB and DeviceC are different.

#### Procedure

1. Create Eth-Trunk 1 on DeviceA, DeviceB, and DeviceC, configure Eth-Trunk 1 to work in static LACP mode, and add member interfaces to Eth-Trunk 1.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] mode lacp-static
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/4
   [*DeviceA-Eth-Trunk1] commit
   [~DeviceA-Eth-Trunk1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] mode lacp-static
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/2
   [*DeviceB-Eth-Trunk1] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] interface eth-trunk 1
   [*DeviceC-Eth-Trunk1] mode lacp-static
   [*DeviceC-Eth-Trunk1] trunkport 100ge 1/0/1 to 1/0/2
   [*DeviceC-Eth-Trunk1] commit
   ```
2. Set the LACP system ID to 00e0-fc00-0000 on both DeviceB and DeviceC.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB-Eth-Trunk1] lacp system-id 00e0-fc00-0000
   [*DeviceB-Eth-Trunk1] commit
   [~DeviceB-Eth-Trunk1] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC-Eth-Trunk1] lacp system-id 00e0-fc00-0000
   [*DeviceC-Eth-Trunk1] commit
   [~DeviceC-Eth-Trunk1] quit
   ```
3. Set the LACP system priority to 100 on both DeviceB and DeviceC.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] lacp priority 100
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] lacp priority 100
   [*DeviceC] commit
   ```
4. On DeviceC, increase the numbers of Eth-Trunk member interfaces by 32768.
   
   
   ```
   [~DeviceC] interface eth-trunk 1
   [~DeviceC-Eth-Trunk1] lacp port-id-extension enable
   [*DeviceC-Eth-Trunk1] commit
   [~DeviceC-Eth-Trunk1] quit
   ```

#### Verifying the Configuration

# Check Eth-Trunk information on DeviceA, DeviceB, and DeviceC, and check whether LACP negotiation is successful.

```
[~DeviceA] display eth-trunk 1
Eth-Trunk1's state information is:
Local:
LAG ID: 1                       Working Mode: Static
Preempt Delay: Disabled         Hash Arithmetic: profile default
System Priority: 100            System ID: 00e0-fc12-1111
Least Active-linknumber: 1      Max Active-linknumber: 128
Operating Status: up            Number Of Up Ports In Trunk: 4
Timeout Period: Slow
--------------------------------------------------------------------------------
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/1              Selected 100GE     32768   3      321     10111100  1
100GE1/0/2              Selected 100GE     32768   1      321     10100010  1
100GE1/0/3              Selected 100GE     32768   4      321     10111100  1
100GE1/0/4              Selected 100GE     32768   2      321     10100010  1

Partner:
--------------------------------------------------------------------------------
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState
100GE1/0/1              100      00e0-fc00-0000  32768   32769  321     10111100
100GE1/0/2              100      00e0-fc00-0000  32768   32770  321     10111100
100GE1/0/1              100      00e0-fc00-0000  32768   4      321     10111100
100GE1/0/2              100      00e0-fc00-0000  32768   5      321     10111100
```
```
[~DeviceB] display eth-trunk 1
Eth-Trunk1's state information is:
Local:
LAG ID: 1                       Working Mode: Static
Preempt Delay: Disabled         Hash Arithmetic: profile default
System Priority: 100            System ID: 00e0-fc00-0000
Least Active-linknumber: 1      Max Active-linknumber: 128
Operating Status: up            Number Of Up Ports In Trunk: 2
Timeout Period: Slow
--------------------------------------------------------------------------------
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/1              Selected 100GE     32768   4      321     10111100  1
100GE1/0/2              Selected 100GE     32768   5      321     10111100  1

Partner:
--------------------------------------------------------------------------------
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState
100GE1/0/3              100      00e0-fc12-1111  32768   4      321     10111100
100GE1/0/4              100      00e0-fc12-1111  32768   2      321     10100010
```
```
[~DeviceC] display eth-trunk 1
Eth-Trunk1's state information is:
Local:
LAG ID: 1                       Working Mode: Static
Preempt Delay: Disabled         Hash Arithmetic: profile default
System Priority: 100            System ID: 00e0-fc00-0000
Least Active-linknumber: 1      Max Active-linknumber: 128
Operating Status: up            Number Of Up Ports In Trunk: 2
Timeout Period: Slow
--------------------------------------------------------------------------------
ActorPortName          Status   PortType PortPri PortNo PortKey PortState Weight
100GE1/0/1              Selected 100GE     32768   32769  321     10111100  1
100GE1/0/2              Selected 100GE     32768   32770  321     10111100  1

Partner:
--------------------------------------------------------------------------------
ActorPortName          SysPri   SystemID        PortPri PortNo PortKey PortState
100GE1/0/1              100      00e0-fc12-1111  32768   3      321     10111100
100GE1/0/2              100      00e0-fc12-1111  32768   1      321     10100010
```

The command output shows that **Operating Status** of each device is **Up**, indicating that Eth-Trunk 1 is successfully established. The Eth-Trunk member interfaces on DeviceB and DeviceC become active interfaces and are in the **Selected** state, indicating that traffic can be load balanced on all member interfaces on DeviceB and DeviceC. **PortNo** in the command output of DeviceC shows that the numbers of Eth-Trunk member interfaces have increased by 32768.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
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
  interface 100GE1/0/4
   eth-trunk 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  lacp priority 100
  #
  interface Eth-Trunk1
   mode lacp-static
   lacp system-id 00e0-fc00-0000
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  lacp priority 100
  #
  interface Eth-Trunk1
   mode lacp-static
   lacp system-id 00e0-fc00-0000
   lacp port-id-extension enable
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  return
  ```