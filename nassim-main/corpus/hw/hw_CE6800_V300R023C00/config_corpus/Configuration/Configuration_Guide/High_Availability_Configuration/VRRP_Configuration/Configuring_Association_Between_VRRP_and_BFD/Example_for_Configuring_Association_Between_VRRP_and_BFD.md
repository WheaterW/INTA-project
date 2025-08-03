Example for Configuring Association Between VRRP and BFD
========================================================

Example for Configuring Association Between VRRP and BFD

#### Networking Requirements

To improve link reliability, a user gateway is usually dual-homed to an upper-layer network, and VRRP is configured to determine the primary/secondary status of dual-homing links and perform a primary/secondary link switchover if the primary link fails.

If a link fails, an extended period may be required to negotiate the VRRP status. To speed up link switchovers, you can deploy BFD to monitor links and configure a VRRP group to track a BFD session. If an interface or link on the master device fails, BFD rapidly detects the fault and notifies the VRRP group. The backup device then preempts the master role and takes over traffic forwarding.

On the network shown in [Figure 1](#EN-US_TASK_0000001130784062__fig_dc_vrp_vrrp_cfg_012601):

* DeviceE is dual-homed to DeviceA and DeviceB through DeviceC and DeviceD.
* A VRRP group is configured on DeviceA (master) and DeviceB (backup).

If DeviceA or the link between DeviceA and DeviceB fails, the VRRP group is required to perform a master/backup switchover within 1 second, implementing rapid route convergence on the bearer network. To meet this requirement, associate the VRRP group with a BFD session.

**Figure 1** Network diagram of associating a VRRP group with a BFD session![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001176743751.png)

#### Precautions

DeviceA's interface (100GE1/0/1) and DeviceB's interface (100GE1/0/1) must be on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session on DeviceA and DeviceB to monitor DeviceA and DeviceB as well as the link DeviceA -> DeviceC -> DeviceD -> DeviceB.
2. Configure a VRRP group on 100GE1/0/1 of DeviceA and DeviceB. DeviceA is the master, and DeviceB is the backup.
3. Configure a VRRP group on 100GE1/0/1 of DeviceA and DeviceB. DeviceA is the master, and DeviceB is the backup.
4. Configure DeviceB (backup) in the VRRP group to track the BFD session. If the BFD session goes down, a master/backup VRRP switchover is performed.

#### Procedure

1. Configure a BFD session on DeviceA and DeviceB.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] bfd
   [~DeviceA-bfd] quit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] bfd trackbfd bind peer-ip 10.1.1.2 interface 100ge 1/0/1
   [*DeviceA-bfd-session-trackbfd] discriminator local 1
   [*DeviceA-bfd-session-trackbfd] discriminator remote 2
   [*DeviceA-bfd-session-trackbfd] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] bfd
   [~DeviceB-bfd] quit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] bfd trackbfd bind peer-ip 10.1.1.1 interface 100ge 1/0/1
   [*DeviceB-bfd-session-trackbfd] discriminator local 2
   [*DeviceB-bfd-session-trackbfd] discriminator remote 1
   [*DeviceB-bfd-session-trackbfd] quit
   [*DeviceB] commit
   ```
   
   After completing the configurations, run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command on DeviceA and DeviceB. The command outputs show that a BFD session has been established and is in the **Up** state. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all
   S: Static session
   D: Dynamic session
   IP: IP session
   IF: Single-hop session
   PEER: Multi-hop session
   AUTO: Automatically negotiated session
   VXLAN: VXLAN session
   (w): State in WTR  (*): State is invalid
   Total UP/DOWN Session Number : 1/0
   ------------------------------------------------------------------------------
   Local Remote PeerIpAddr      State     Type        InterfaceName
   ------------------------------------------------------------------------------
   1     2      10.1.1.2        Up        S_IP_IF     100GE1/0/1
   ------------------------------------------------------------------------------
   ```
2. Configure VRRP group 1 on DeviceA and DeviceB.
   
   # Configure VRRP group 1 on DeviceA, and set the VRRP priority of DeviceA to 120 so that it functions as the master.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceA-100GE1/0/1] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure VRRP group 1 on DeviceB, and use the default priority so that it functions as the backup.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   After completing the configurations, run the [**display vrrp verbose**](cmdqueryname=display+vrrp+verbose) command on DeviceA and DeviceB. The command outputs show that the VRRP status of DeviceA is **Master** and that of DeviceB is **Backup**.
   
   ```
   [~DeviceA] display vrrp verbose
   100GE1/0/1 | Virtual Router 1
   State             : Master
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.1
   PriorityRun       : 120
   PriorityConfig    : 120
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s    Remain : --
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 00-e0-fc-12-78-90
   Check TTL         : YES
   Config Type       : Normal
   Create Time       : 2020-12-29 05:41:23
   Last Change Time  : 2020-12-29 05:41:33
   ```
   ```
   [~DeviceB] display vrrp verbose
   100GE1/0/1 | Virtual Router 1
   State           : Backup
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.1
   PriorityRun       : 100
   PriorityConfig    : 100
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s    Remain : --
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 00-e0-fc-12-78-90
   Check TTL         : YES
   Config Type       : Normal
   Create Time       : 2020-12-29 05:41:23
   Last Change Time  : 2020-12-29 05:41:33
   ```
3. Configure DeviceB in the VRRP group to track the BFD session.
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 1 track bfd 2 increase 40
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   After completing the configurations, run the [**display vrrp verbose**](cmdqueryname=display+vrrp+verbose) command on DeviceB to view the tracked BFD session and its status.
   
   ```
   [~DeviceB] display vrrp verbose
   100GE1/0/1 | Virtual Router 1
   State             : Backup
   Virtual IP          : 10.1.1.111
   Master IP           : 10.1.1.1
   PriorityRun         : 100
   PriorityConfig      : 100
   MasterPriority      : 120
   Preempt             : YES      Delay Time : 0s    Remain : --
   Hold Multiplier     : 4
   TimerRun            : 1s
   TimerConfig         : 1s
   Auth Type           : NONE
   Virtual MAC         : 00-e0-fc-12-78-90
   Check TTL           : YES
   Config Type         : Normal
   Track BFD         : 2                     
   Priority Increased : 40
   BFD-Session State : UP
   Create Time         : 2020-12-29 05:41:23
   Last Change Time    : 2020-12-29 05:41:33
   ```

#### Verifying the Configuration

# Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceA's **100ge 1/0/1** to simulate a link fault.

```
[~DeviceA] interface 100ge 1/0/1
[~DeviceA-100GE1/0/1] shutdown
[*DeviceA-100GE1/0/1] quit
[*DeviceA] commit
```

Check the VRRP status on DeviceA. The command output shows that DeviceA is in the **Initialize** state.

```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State              : Initialize
Virtual IP           : 10.1.1.111
Master IP            : 0.0.0.0
PriorityRun          : 0
PriorityConfig       : 120
MasterPriority       : 0   
Preempt              : YES      Delay Time : 0s    Remain : --
Hold Multiplier      : 4
TimerRun             : 1s
TimerConfig          : 1s
Auth Type            : NONE
Virtual MAC          : 00-e0-fc-12-78-90
Check TTL            : YES
Config Type          : Normal
Create Time          : 2020-12-29 05:41:23
Last Change Time     : 2020-12-29 05:41:33
```

Check the VRRP status on DeviceB. The command output shows that the VRRP priority of DeviceB has been increased by 40 and the VRRP status of DeviceB has changed to **Master**.

```
[~DeviceB] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State              : Master
Virtual IP           : 10.1.1.111
Master IP            : 10.1.1.2
PriorityRun          : 140
PriorityConfig       : 100
MasterPriority       : 140
Preempt              : YES      Delay Time : 0s    Remain : --
Hold Multiplier      : 4
TimerRun             : 1s
TimerConfig          : 1s
Auth Type            : NONE
Virtual MAC          : 00-e0-fc-12-78-90
Check TTL            : YES
Config Type          : Normal
Track BFD          : 2              
Priority Increased :40
BFD-Session State  : DOWN
Create Time          : 2020-12-29 05:41:23
Last Change Time     : 2020-12-29 05:41:33
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
  #
  bfd trackbfd bind peer-ip 10.1.1.2 interface 100GE1/0/1
   discriminator local 1
   discriminator remote 2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 track bfd 2 increase 40
  #
  bfd trackbfd bind peer-ip 10.1.1.1 interface 100GE1/0/1
   discriminator local 2
   discriminator remote 1
  #
  return
  ```