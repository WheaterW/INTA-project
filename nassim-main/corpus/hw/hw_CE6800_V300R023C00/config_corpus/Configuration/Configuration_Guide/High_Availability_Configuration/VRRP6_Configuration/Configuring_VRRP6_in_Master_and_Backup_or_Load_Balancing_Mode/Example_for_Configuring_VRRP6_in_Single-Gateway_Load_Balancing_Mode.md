Example for Configuring VRRP6 in Single-Gateway Load Balancing Mode
===================================================================

Example for Configuring VRRP6 in Single-Gateway Load Balancing Mode

#### Networking Requirements

Hosts are connected to an upper-layer network through gateways. To improve network reliability, configure VRRP6 groups working in master/backup mode on gateways. If multiple VRRP6 groups run on a device, configure the groups to work in single-gateway load balancing mode to balance traffic.

In [Figure 1](#EN-US_TASK_0000001176741669__fig8509122411516), two VRRP6 groups are configured on both DeviceA and DeviceB. VRRP6 group 1 is an LBRG and VRRP6 group 2 is an LBRG member group.

* DeviceA functions as the master in VRRP6 group 1 and as the backup in VRRP6 group 2.
* DeviceB functions as the master in VRRP6 group 2 and as the backup in VRRP6 group 1.
* Both HostA and HostB use VRRP6 group 1 as their gateway. After receiving an NS message from a user, VRRP6 group 1 encapsulates its own or VRRP6 group 2's virtual MAC address into an NA message to implement load balancing.

**Figure 1** Network diagram of configuring VRRP6 groups in single-gateway load balancing mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176661785.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Create two VRRP6 groups on both DeviceA and DeviceB. One functions as an LBRG, and the other functions as an LBRG member group.
   * Create VRRP6 groups 1 and 2 on DeviceA's interface 100GE1/0/1. Configure DeviceA as the master in VRRP6 group 1 and as the backup in VRRP6 group 2.
   * Create VRRP6 groups 1 and 2 on DeviceB's interface 100GE1/0/1. Configure DeviceB as the backup in VRRP6 group 1 and as the master in VRRP6 group 2.


#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001176741669__section_05) in this section.
2. Configure VRRP6 groups.
   
   # Configure an IPv6 address for DeviceA's interface 100GE1/0/1. Create VRRP6 groups 1 and 2 on DeviceA's 100GE1/0/1. Set the priority to 120 for DeviceA to ensure that it functions as the master in VRRP6 group 1, and use the default priority 100 for DeviceA to ensure that it functions as the backup in VRRP6 group 2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/11] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8::1 64
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:db8::100
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 priority 120
   [*DeviceA-100GE1/0/1] vrrp6 vrid 2
   ```
   
   # On DeviceA's 100GE1/0/1, configure VRRP6 group 1 as an LBRG and add VRRP6 group 2 to the LBRG.
   
   ```
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 load-balance
   [*DeviceA-100GE1/0/1] vrrp6 vrid 2 join load-balance-vrrp vrid 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] quit
   [*DeviceA] commit
   ```
   
   # Configure an IPv6 address for DeviceB's interface 100GE1/0/1. Create VRRP6 groups 1 and 2 on DeviceB's 100GE1/0/1. Use the default priority 100 for DeviceB to ensure that it functions as the backup in VRRP6 group 1, and set the priority to 120 for DeviceB to ensure that it functions as the master in VRRP6 group 2.
   
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
   [*DeviceB-100GE1/0/1] vrrp6 vrid 2
   [*DeviceB-100GE1/0/1] vrrp6 vrid 2 priority 120
   ```
   
   # On DeviceB's 100GE1/0/1, configure VRRP6 group 1 as an LBRG and add VRRP6 group 2 to the LBRG.
   
   ```
   [*DeviceB-100GE1/0/1] vrrp6 vrid 1 load-balance
   [*DeviceB-100GE1/0/1] vrrp6 vrid 2 join load-balance-vrrp vrid 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the states of DeviceA and DeviceB in the VRRP6 groups.

```
<DeviceA> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::1
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-34-56
Check hop limit : YES
Config Type     : Load-Balance
Create Time     : 2020-07-27 20:15:46
Last Change Time: 2020-07-27 20:15:46

100GE1/0/1 | Virtual Router 2
State           : Backup
Virtual IP      : ::
Master IP       : 2001:DB8::2
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-34-57
Check hop limit : YES
Config Type     : Load-Balance-Member
Create Time     : 2020-07-27 20:17:46
Last Change Time: 2020-07-27 20:17:46
```

The command output shows that DeviceA functions as the master in the LBRG (VRRP6 group 1) and as the backup in the LBRG member group (VRRP6 group 2).

```
<DeviceB> display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : 2001:DB8::1
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-34-56
Check hop limit : YES
Config Type     : Load-Balance
Create Time     : 2020-07-27 20:19:46
Last Change Time: 2020-07-27 20:19:46

100GE1/0/1 | Virtual Router 2
State           : Master
Virtual IP      : ::
Master IP       : 2001:DB8::2
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-34-57
Check hop limit : YES
Config Type     : Load-Balance-Member
Create Time     : 2020-07-27 20:21:46
Last Change Time: 2020-07-27 20:21:46
```

The command output shows that DeviceB functions as the backup in the LBRG (VRRP6 group 1) and as the master in the LBRG member group (VRRP6 group 2).

# Check information about the VRRP6 LBRG and its member group on DeviceA and DeviceB.

```
<DeviceA> display vrrp6 load-balance member-vrrp
Interface: 1/0/1, load-balance-vrrp vrid: 1, state: Master
  Member-vrrp number: 1
    Member-vrrp vrid: 2, state: Backup
```
```
<DeviceB> display vrrp6 load-balance member-vrrp
Interface: 1/0/1, load-balance-vrrp vrid: 1, state: Backup
  Member-vrrp number: 1
    Member-vrrp vrid: 2, state: Master
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  ospfv3 1
   router-id 10.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::1/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 load-balance
   vrrp6 vrid 1 priority 120
   vrrp6 vrid 2
   vrrp6 vrid 2 join load-balance-vrrp vrid 1
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
   router-id 10.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 load-balance
   vrrp6 vrid 2
   vrrp6 vrid 2 priority 120
   vrrp6 vrid 2 join load-balance-vrrp vrid 1
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
   router-id 10.1.1.3
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