Example for Configuring STP
===========================

Example for Configuring STP

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001315231094__en-us_task_0000001176742791_fig_dc_cfg_stp_003701), there is a loop between DeviceA, DeviceB, DeviceC, and DeviceD. In this case, STP can be deployed on the network to break the loop and thereby avoid broadcast storms and MAC address flapping.

**Figure 1** Network diagram of STP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662945.png)

#### Procedure

1. Configure each device to work in STP mode.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] stp mode stp
   [*DeviceA] commit
   ```
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] stp mode stp
   [*DeviceB] commit
   ```
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] stp mode stp
   [*DeviceC] commit
   ```
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] stp mode stp
   [*DeviceD] commit
   ```
2. Specify the root bridge and a secondary root bridge. It is best reality to specify network devices with high performance and higher network layers as the root bridge and a secondary root bridge.
   
   
   
   # Configure DeviceA as the root bridge.
   
   ```
   [~DeviceA] stp root primary
   [*DeviceA] commit
   ```
   
   # Configure DeviceB as a secondary root bridge.
   
   ```
   [~DeviceB] stp root secondary
   [*DeviceB] commit
   ```
3. Configure all devices on the network to use the same path cost calculation method. Set a path cost value for 100GE 1/0/1 on DeviceC to block this port.
   
   
   
   # Configure DeviceA to use the Huawei legacy standard to calculate the path cost.
   
   ```
   [~DeviceA] stp pathcost-standard legacy
   [*DeviceA] commit
   ```
   
   # Configure DeviceB to use the Huawei legacy standard to calculate the path cost.
   
   ```
   [~DeviceB] stp pathcost-standard legacy
   [*DeviceB] commit
   ```
   
   # Configure DeviceC to use the Huawei legacy standard to calculate the path cost. Set the path cost value for 100GE 1/0/1 on DeviceC to 20000, which is greater than that for any other interface, to block this 100GE 1/0/1.
   
   ```
   [~DeviceC] stp pathcost-standard legacy
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] portswitch
   [*DeviceC-100GE1/0/1] stp cost 20000
   [*DeviceC-100GE1/0/1] undo shutdown
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD to use the Huawei legacy standard to calculate the path cost.
   
   ```
   [~DeviceD] stp pathcost-standard legacy
   [*DeviceD] commit
   ```
4. Disable STP on DeviceB's and DeviceC's ports that are connected to PCs.
   
   
   
   # Disable STP on DeviceB's 100GE 1/0/2.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] portswitch
   [~DeviceB-100GE1/0/2] stp disable
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Disable STP on DeviceC's 100GE 1/0/2.
   
   ```
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] portswitch
   [~DeviceC-100GE1/0/2] stp disable
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
5. Enable STP on each device.
   
   
   
   By default, STP, RSTP, or MSTP is enabled on a device. You can run the [**stp enable**](cmdqueryname=stp+enable) command in the system view to enable this function if it is disabled.

#### Verifying the Configuration

After the spanning tree calculation is stable, verify the configuration as follows:

# Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceA to check the port role and status. The command output shows that 100GE 1/0/1 and 100GE 1/0/2 have been elected as designated ports during spanning tree calculation and are in Forwarding state.

```
[~DeviceA] display stp brief
 MSTID  Port                        Role  STP State     Protection      Cost    Edged
     0  100GE1/0/1                  DESI  forwarding    none              2     disable
     0  100GE1/0/2                  DESI  forwarding    none              2     disable

```

# Run the [**display stp interface brief**](cmdqueryname=display+stp+interface+brief) command on DeviceB to check the role and status of 100GE 1/0/1. The command output shows that 100GE 1/0/1 has been elected as a designated port and is in Forwarding state.

```
[~DeviceB] display stp interface 100ge 1/0/1 brief
 MSTID  Port                        Role  STP State     Protection      Cost    Edged
     0  100GE1/0/1                  DESI  forwarding    none              2     disable

```

# Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceC to check the port role and status. The command output shows that 100GE 1/0/1 has been elected as an alternate port and is in Discarding state and that 100GE 1/0/3 has been elected as a root port and is in Forwarding state.

```
[~DeviceC] display stp brief
 MSTID  Port                        Role  STP State     Protection      Cost    Edged
     0  100GE1/0/1                  ALTE  discarding    none          20000     disable
     0  100GE1/0/3                  ROOT  forwarding    none              2     disable

```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  stp mode stp
  stp instance 0 root primary
  stp pathcost-standard legacy
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  stp mode stp
  stp instance 0 root secondary
  stp pathcost-standard legacy
  #
  interface 100GE1/0/2  
   stp disable
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  stp mode stp
  stp pathcost-standard legacy
  #
  interface 100GE1/0/1
   stp instance 0 cost 20000
  #
  interface 100GE1/0/2
   stp disable
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  stp mode stp
  stp pathcost-standard legacy
  #
  return
  ```