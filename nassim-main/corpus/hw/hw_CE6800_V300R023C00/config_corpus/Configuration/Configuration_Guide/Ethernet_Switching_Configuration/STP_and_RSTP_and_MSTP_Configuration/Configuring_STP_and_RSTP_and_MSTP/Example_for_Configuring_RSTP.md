Example for Configuring RSTP
============================

Example for Configuring RSTP

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001315071130__en-us_task_0000001130623344_fig_dc_cfg_stp_003701), there is a loop between DeviceA, DeviceB, DeviceC, and DeviceD. In this case, RSTP can be deployed on this network to break the loop and thereby avoid broadcast storms and MAC address flapping.

**Figure 1** Network diagram of RSTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176662917.png)

#### Procedure

1. Configure each device to work in RSTP mode.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] stp mode rstp
   [*DeviceA] commit
   ```
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] stp mode rstp
   [*DeviceB] commit
   ```
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] stp mode rstp
   [*DeviceC] commit
   ```
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] stp mode rstp
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
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD to use the Huawei legacy standard to calculate the path cost.
   
   ```
   [~DeviceD] stp pathcost-standard legacy
   [*DeviceD] commit
   ```
4. Configure DeviceB's and DeviceC's ports that are connected to PCs as edge ports.
   
   
   
   # Configure 100GE 1/0/2 on DeviceB as an edge port and enable BPDU protection.
   
   ```
   [~DeviceB] interface 100ge 1/0/2
   [~DeviceB-100GE1/0/2] portswitch
   [~DeviceB-100GE1/0/2] stp edged-port enable
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] stp bpdu-protection
   [*DeviceB] commit
   ```
   
   # Configure 100GE 1/0/2 on DeviceC as an edge port and enable BPDU protection.
   
   ```
   [~DeviceC] interface 100ge 1/0/2
   [~DeviceC-100GE1/0/2] portswitch
   [~DeviceC-100GE1/0/2] stp edged-port enable
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] stp bpdu-protection
   [*DeviceC] commit
   ```
5. Enable RSTP on each device.
   
   
   
   By default, STP, RSTP, or MSTP is enabled on a device. You can run the [**stp enable**](cmdqueryname=stp+enable) command in the system view to enable this function if it is disabled.
6. Enable root protection for the designated ports 100GE 1/0/1 and 100GE 1/0/2 on the root bridge DeviceA.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] stp root-protection
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] stp root-protection
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

After the spanning tree calculation is stable, verify the configuration as follows:

# Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceA to check the port status and enabled protection function. The command output shows that 100GE 1/0/1 and 100GE 1/0/2 have been elected as designated ports through spanning tree calculation and that root protection has been enabled for the designated ports.

```
[~DeviceA] display stp brief
 MSTID  Port                        Role  STP State     Protection      Cost    Edged
     0  100GE1/0/1                  DESI  forwarding    root              2    disable
     0  100GE1/0/2                  DESI  forwarding    root              2    disable

```

# Run the [**display stp interface brief**](cmdqueryname=display+stp+interface+brief) command on DeviceB to check the role and status of 100GE 1/0/1. The command output shows that 100GE 1/0/1 has been elected as a designated port and is in Forwarding state.

```
[~DeviceB] display stp interface 100ge 1/0/1 brief
 MSTID  Port                        Role  STP State     Protection      Cost    Edged
     0  100GE1/0/1                  DESI  forwarding    none              2    disable

```

# Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on DeviceC to check the port role and status. The command output shows that 100GE 1/0/1 has been elected as an alternate port and is in Discarding state. Furthermore, 100GE 1/0/3 has been elected as a root port and is in Forwarding state.

```
[~DeviceC] display stp brief
 MSTID  Port                        Role  STP State     Protection      Cost    Edged
     0  100GE1/0/1                  ALTE  discarding    none          20000    disable
     0  100GE1/0/3                  ROOT  forwarding    none              2    disable

```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  stp mode rstp
  stp instance 0 root primary
  stp pathcost-standard legacy
  #
  interface 100GE1/0/1
   stp root-protection
  #
  interface 100GE1/0/2
   stp root-protection
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  stp mode rstp
  stp bpdu-protection
  stp instance 0 root secondary
  stp pathcost-standard legacy
  #
  interface 100GE1/0/2
   stp edged-port enable
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  stp mode rstp
  stp bpdu-protection
  stp pathcost-standard legacy
  #
  interface 100GE1/0/1
   stp instance 0 cost 20000
  #
  interface 100GE1/0/2
   stp edged-port enable
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  stp mode rstp
  stp pathcost-standard legacy
  #
  return
  ```