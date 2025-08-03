Example for Configuring VRRP6 in Master/Backup Mode
===================================================

Example for Configuring VRRP6 in Master/Backup Mode

#### Networking Requirements

Hosts are connected to an upper-layer network through gateways. To improve network reliability, configure a VRRP6 group on the gateways to implement gateway redundancy.

In [Figure 1](#EN-US_TASK_0000001130622220__fig_dc_vrp_vrrp6_cfg_011501), the master device (DeviceA) forwards traffic in normal cases. If DeviceA fails, the backup device (DeviceB) takes over traffic forwarding. After DeviceA recovers, traffic switches back to DeviceA.

**Figure 1** Network diagram of configuring a VRRP6 group in master/backup mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130622240.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Configure a VRRP6 group on user-side gateways (DeviceA and DeviceB). Configure a higher priority for DeviceA to ensure it functions as the master and a lower priority for DeviceB to ensure it functions as the backup.


#### Procedure

1. Assign an IPv6 address to each interface on DeviceA, DeviceB, and DeviceC. Configure OSPFv3 to ensure that the devices can communicate.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] area 0.0.0.0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8::1 64
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:DB8:1::1 64
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] area 0.0.0.0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8::2 64
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ipv6 enable
   [*DeviceB-100GE1/0/2] ipv6 address 2001:DB8:2::1 64
   [*DeviceB-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   [*DeviceC-ospfv3-1] area 0.0.0.0
   [*DeviceC-ospfv3-1-area-0.0.0.0] quit
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ipv6 enable
   [*DeviceC-100GE1/0/1] ipv6 address 2001:DB8:1::2 64
   [*DeviceC-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ipv6 enable
   [*DeviceC-100GE1/0/2] ipv6 address 2001:DB8:2::2 64
   [*DeviceC-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] undo portswitch
   [*DeviceC-100GE1/0/3] ipv6 enable
   [*DeviceC-100GE1/0/3] ipv6 address 2001:DB8:3::2 64
   [*DeviceC-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
2. Configure a VRRP6 group on DeviceA and DeviceB.
   
   # Create VRRP6 group 1 on DeviceA's 100GE 1/0/1, and set DeviceA's priority to 120 to ensure that it functions as the master.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8::100
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 priority 120
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 preempt timer delay 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] quit
   [*DeviceA] commit
   ```
   
   # Create VRRP6 group 1 on DeviceB's 100GE 1/0/1, and use the default priority 100 to ensure that DeviceB functions as the backup.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   [*DeviceB-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8::100
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the states of DeviceA and DeviceB in the VRRP6 group.

```
<DeviceA> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : FE80::3A40:15FF:FE11:300
Local IP        : FE80::3A40:15FF:FE11:300
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
Create Time     : 2020-07-27 07:37:45
Last Change Time: 2020-07-27 07:47:38
```

The command output shows that DeviceA is in the **Master** state.

```
<DeviceB> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : FE80::3A40:15FF:FE11:300
Local IP        : FE80::3A40:15FF:FE21:300
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
Create Time     : 2020-07-27 07:50:28
Last Change Time: 2020-07-27 07:58:13
```

The command output shows that DeviceB is in the **Backup** state.

# Run the **shutdown** command on DeviceA's 100GE 1/0/2 to simulate a device fault. Check the states of DeviceA and DeviceB in the VRRP6 group.

```
<DeviceA> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Initialize
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : ::
Local IP        : FE80::3A40:15FF:FE11:30
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 0
Preempt         : YES   Delay Time : 20s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 0000-5e00-0201
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 07:37:45
Last Change Time: 2020-07-27 07:59:38
```

The command output shows that DeviceA is in the **Initialize** state.

```
<DeviceB> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : FE80::3A40:15FF:FE21:300
Local IP        : FE80::3A40:15FF:FE21:300
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
Create Time     : 2020-07-27 07:50:28
Last Change Time: 2020-07-27 07:59:38
```

The command output shows that DeviceB is in the **Master** state.

# Run the **undo shutdown** command on DeviceA's 100GE 1/0/2. After 100GE 1/0/1 goes up, wait for 20 seconds and then check the states of DeviceA and DeviceB in the VRRP6 group.

```
<DeviceA> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : FE80::3A40:15FF:FE11:300
Local IP        : FE80::3A40:15FF:FE11:300
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
Create Time     : 2020-07-27 07:37:45
Last Change Time: 2020-07-27 08:04:47
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
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```