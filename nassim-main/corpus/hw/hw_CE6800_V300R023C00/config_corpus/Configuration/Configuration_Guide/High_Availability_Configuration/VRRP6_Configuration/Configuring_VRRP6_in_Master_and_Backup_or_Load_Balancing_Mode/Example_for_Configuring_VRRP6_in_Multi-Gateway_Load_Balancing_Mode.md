Example for Configuring VRRP6 in Multi-Gateway Load Balancing Mode
==================================================================

Example for Configuring VRRP6 in Multi-Gateway Load Balancing Mode

#### Networking Requirements

Hosts are connected to an upper-layer network through gateways. To improve network reliability, configure VRRP6 groups working in master/backup mode on gateways. If multiple VRRP6 groups run on a device, configure the groups to work in multi-gateway load balancing mode to balance traffic.

In [Figure 1](#EN-US_TASK_0000001130622212__fig_dc_vrp_vrrp6_cfg_011601),

* DeviceA functions as the master in VRRP6 group 1 and as the backup in VRRP6 group 2.
* DeviceB functions as the master in VRRP6 group 2 and as the backup in VRRP6 group 1.
* HostA uses the virtual IPv6 address of VRRP6 group 1 as a default gateway address, and HostB uses the virtual IPv6 address of VRRP6 group 2 as a default gateway address. The two VRRP6 groups back up each other and balance data traffic.

**Figure 1** Network diagram of configuring VRRP6 groups working in multi-gateway load balancing mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130622232.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Create VRRP6 groups 1 and 2 on DeviceA's interface 100GE1/0/1. Configure DeviceA as the master in VRRP6 group 1 and as the backup in VRRP6 group 2.
3. Create VRRP6 groups 1 and 2 on DeviceB's interface 100GE1/0/1. Configure DeviceB as the backup in VRRP6 group 1 and as the master in VRRP6 group 2.

#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001130622212__section_05) in this section.
2. Configure VRRP6 groups.
   
   # Configure an IPv6 address for DeviceA's interface 100GE1/0/1. Create VRRP6 groups 1 and 2 on DeviceA's 100GE1/0/1. Set the priority to 120 for DeviceA to ensure that it functions as the master in VRRP6 group 1, and use the default priority 100 for DeviceA to ensure that it functions as the backup in VRRP6 group 2.
   
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
   [*DeviceA-100GE1/0/1] vrrp6 vrid 2 virtual-ip fe80::2 link-local
   [*DeviceA-100GE1/0/1] vrrp6 vrid 2 virtual-ip 2001:db8::60
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
   [*DeviceB-100GE1/0/1] vrrp6 vrid 2 virtual-ip fe80::2 link-local
   [*DeviceB-100GE1/0/1] vrrp6 vrid 2 virtual-ip 2001:db8::60
   [*DeviceB-100GE1/0/1] vrrp6 vrid 2 priority 120
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
Virtual MAC     : 0000-5e00-0201
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 20:15:46
Last Change Time: 2020-07-27 20:15:46

100GE1/0/1 | Virtual Router 2
State           : Backup
Virtual IP      : FE80::2
                  2001:DB8::60
Master IP       : 2001:DB8::2
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-78-80
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 20:17:46
Last Change Time: 2020-07-27 20:17:46
```

The command output shows that two VRRP6 groups have been created on DeviceA. DeviceA is in the **Master** and **Backup** states in VRRP6 groups 1 and 2, respectively.

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
Virtual MAC     : 0000-5e00-0202
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 20:19:46
Last Change Time: 2020-07-27 20:19:46

100GE1/0/1 | Virtual Router 2
State           : Master
Virtual IP      : FE80::2
                  2001:DB8::60
Master IP       : 2001:DB8::2
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 0s   Remain : --
Hold Multiplier : 4
TimerRun        : 100cs
TimerConfig     : 100cs
Virtual MAC     : 00-e0-fc-12-78-80
Check hop limit : YES
Config Type     : Normal
Create Time     : 2020-07-27 20:21:46
Last Change Time: 2020-07-27 20:21:46
```

The command output shows that two VRRP6 groups have been created on DeviceB. DeviceB is in the **Backup** and **Master** states in VRRP6 groups 1 and 2, respectively.


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
   vrrp6 vrid 2 virtual-ip FE80::2 link-local
   vrrp6 vrid 2 virtual-ip 2001:DB8::60
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
   router-id 1.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 2 virtual-ip FE80::2 link-local
   vrrp6 vrid 2 virtual-ip 2001:DB8::60
   vrrp6 vrid 2 priority 120
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