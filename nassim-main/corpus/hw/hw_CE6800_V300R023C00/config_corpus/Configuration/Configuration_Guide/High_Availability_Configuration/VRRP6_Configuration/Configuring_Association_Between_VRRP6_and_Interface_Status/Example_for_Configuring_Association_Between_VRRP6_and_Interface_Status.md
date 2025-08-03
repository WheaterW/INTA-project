Example for Configuring Association Between VRRP6 and Interface Status
======================================================================

Example for Configuring Association Between VRRP6 and Interface Status

#### Networking Requirements

Hosts are connected to an upper-layer network through gateways. To improve network reliability, configure a VRRP6 group on the gateways to implement gateway redundancy. To further improve network reliability and implement rapid master/backup VRRP switchovers, configure VRRP6 association.

In [Figure 1](#EN-US_TASK_0000001176661769__fig_dc_vrp_vrrp6_cfg_011701), the master device (DeviceA) transmits data during normal operation. When the interface associated with the VRRP6 group fails, the backup device (DeviceB) is required to take over data transmission. After DeviceA recovers, traffic switches back to it.![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.



**Figure 1** Network diagram for configuring VRRP6 association  
![](figure/en-us_image_0000001176661789.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Configure a VRRP6 group on user-side gateways (DeviceA and DeviceB) and set a higher priority for DeviceA so that it functions as the master in the VRRP6 group.
3. Configure the VRRP6 group on DeviceA to track the uplink interface so that a master/backup VRRP switchover can be performed if the tracked interface goes down.


#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001176661769__context1421141332420) in this section.
2. Configure a VRRP6 group on DeviceA and DeviceB.# Configure an IPv6 address for DeviceA's interface 100GE1/0/1. Create VRRP6 group 1 on DeviceA's 100GE1/0/1, and set DeviceA's priority to 120 to ensure that it functions as the master.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8::1 64
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8::100
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 priority 120
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 preempt timer delay 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure an IPv6 address for DeviceB's interface 100GE1/0/1. Create VRRP6 group 1 on DeviceB's 100GE1/0/1, and use the default priority 100 to ensure that DeviceB functions as the backup.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8::2 64
   [*DeviceB-100GE1/0/1] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   [*DeviceB-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8::100
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Configure VRRP6 association. On DeviceA, associate the VRRP6 group with the uplink interface.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 track interface 100ge 1/0/2 reduce 40
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the states of DeviceA and DeviceB in the VRRP6 group.

```
[~DeviceA] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::1
Local IP        : 2001:DB8::1   
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 0000-5e00-0201
Check hop limit : YES
Config Type     : Normal
Track IF        : 100GE1/0/2             Priority Reduced : 40
IF State        : UP
Create Time     : 2020-07-27 17:33:00
Last Change Time: 2020-07-27 17:33:04
```

The command output shows that DeviceA is in the **Master** state in the group and the group is associated with the uplink interface 100GE1/0/1.

```
[~DeviceB] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::1
Local IP        : 2001:DB8::2
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 0000-5e00-0202
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 17:33:00
Last Change Time: 2020-07-27 17:33:04
```

The command output shows that DeviceB is in the **Backup** state in the VRRP6 group.

# Run the **shutdown** command on DeviceA's 100GE1/0/2 to simulate a device fault. Check the states of DeviceA and DeviceB in the VRRP6 group.

```
[~DeviceA] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::2
Local IP        : 2001:DB8::1 
PriorityRun     : 80
PriorityConfig  : 120
MasterPriority  : 100
Preempt         : YES   Delay Time : 20s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 0000-5e00-0201
Check hop limit : YES
Config Type     : Normal
Track IF        : 100GE1/0/2             Priority Reduced : 40
IF State        : DOWN
Create Time     : 2020-07-27 17:33:00
Last Change Time: 2020-07-27 17:35:14
```

The command output shows that DeviceA is in the **Backup** state in the VRRP6 group.

```
[~DeviceB] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::2
Local IP        : 2001:DB8::2
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 100
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 0000-5e00-0202
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 17:33:00
Last Change Time: 2020-07-27 17:33:04
```

The command output shows that DeviceB is in the **Master** state in the group.

# Run the **undo shutdown** command on DeviceA's 100GE1/0/2. After 100GE1/0/2 goes up, wait 20 seconds and check the state of DeviceA in the VRRP6 group.

```
[~DeviceA] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::1
Local IP        : 2001:DB8::1 
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 0000-5e00-0201
Check hop limit : YES
Config Type     : Normal
Track IF        : 100GE1/0/2               Priority Reduced : 40
IF State        : UP
Create Time     : 2020-07-27 17:33:00
Last Change Time: 2020-07-27 17:40:04
```

The command output shows that DeviceA is restored to the **Master** state.


#### Configuration Scripts

* DeviceA
  ```
  #
   sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::1/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 priority 120
   vrrp6 vrid 1 preempt timer delay 20
   vrrp6 vrid 1 track interface 100GE1/0/2 reduce 40
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceB
  ```
  #
   sysname DeviceB
  #
   ospfv3 1
   router-id 2.2.2.2
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC
  ```
  #
   sysname DeviceC
  #
  ospfv3 1
   router-id 3.3.3.3
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```