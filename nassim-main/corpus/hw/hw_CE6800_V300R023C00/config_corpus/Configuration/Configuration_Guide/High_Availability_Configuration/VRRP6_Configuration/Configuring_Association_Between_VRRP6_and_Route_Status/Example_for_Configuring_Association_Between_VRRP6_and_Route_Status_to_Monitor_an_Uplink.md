Example for Configuring Association Between VRRP6 and Route Status to Monitor an Uplink
=======================================================================================

Example for Configuring Association Between VRRP6 and Route Status to Monitor an Uplink

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001212741448__fig12998916133218), a host on a LAN accesses the external network through DeviceE, which is dual-homed to DeviceA and DeviceB. A VRRP6 group is deployed on DeviceA and DeviceB, of which DeviceA serves as the master. Normally, DeviceA functions as the gateway, and user traffic is forwarded along the path DeviceF -> DeviceA -> DeviceC.

When the route between DeviceA and DeviceC is withdrawn or becomes inactive, the VRRP6 group is required to be notified and trigger a master/backup switchover. DeviceB then takes over traffic forwarding to minimize the impact of the link fault on services.**Figure 1** Network diagram of configuring association between VRRP6 and route status to monitor an uplink![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001212526642.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on each device and configure a routing protocol to ensure network reachability.
2. Configure a VRRP6 group on DeviceA and DeviceB. Configure a higher priority and a preemption delay of 20s for DeviceA to ensure it functions as the master and forwards traffic. Configure a lower priority for DeviceB so that it functions as the backup.
3. Configure the VRRP6 group on DeviceA to track an uplink route so that a master/backup VRRP6 group switchover can be performed when the tracked route is withdrawn or becomes inactive.

#### Procedure

1. Configure IS-IS on DeviceA, DeviceB, DeviceC, and DeviceD for interworking between them. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001212741448__en-us_task_0000001176663821_context123891331175616) in this section.
2. Configure a VRRP6 group on DeviceA and DeviceB.# Configure an IPv6 address for DeviceA's interface 100GE1/0/1. # Create VRRP6 group 1 on DeviceA's 100GE1/0/1, and set DeviceA's priority to 120 to ensure that it functions as the master.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:DB8:1::1 64
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::1 link-local
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:DB8::100
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 priority 120
   [*DeviceA-100GE1/0/1] vrrp6 vrid 1 preempt timer delay 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure an IPv6 address for DeviceB's interface 100GE1/0/1. # Create VRRP6 group 1 on DeviceB's 100GE1/0/1, and use the default priority 100 to ensure that DeviceB functions as the backup.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:1::2 64
   [*DeviceB-100GE1/0/1] vrrp6 vrid 1 virtual-ip FE80::1 link-local
   [*DeviceB-100GE1/0/1] vrrp6 vrid 1 virtual-ip 2001:DB8::100
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Configure the VRRP6 group on DeviceA to track an uplink route. When the tracked route is withdrawn or becomes inactive, DeviceA reduces its priority by 40.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp6 vrid 1 track ipv6 route 2001:DB8:2::2 64 reduce 40
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the states of DeviceA and DeviceB in the VRRP6 group.

```
[~DeviceA] display vrrp6 interface 100GE1/0/1  verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : xxxx::xxxx
Local IP        : xxxx::xxxx
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s
Hold Multiplier : 3
TimerRun        : 200ms
TimerConfig     : 200ms
Virtual MAC     : xxxx-xxxx-xxxx
Check hop limit : YES
Config Type     : normal-vrrp
Backup-forward  : disabled
Track IPv6 Route    : 2001:DB8:2::2  Priority Reduced : 40
IPv6 Route State    : Reachable
Create Time       : 2022-02-24 10:23:21
Last Change Time  : 2022-02-24 11:19:36
```
```
[~DeviceB] display vrrp6 interface 100GE1/0/1  verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : xxxx::xxxx
Local IP        : xxxx::xxxx
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s
Hold Multiplier : 3
TimerRun        : 200ms
TimerConfig     : 200ms
Virtual MAC     : xxxx-xxxx-xxxx
Check hop limit : YES
Config Type     : normal-vrrp
Backup-forward  : disabled
Create Time       : 2022-02-24 10:23:21
Last Change Time  : 2022-02-24 11:19:36
```

The command outputs show that DeviceA is in the **Master** state and DeviceB is in the **Backup** state.

# Check the routing table on DeviceA.

```
[~DeviceA] display ipv6 routing-table brief
Routing Table : _public_
         Destinations : 1        Routes : 1        

Format :
Destination/Mask                             Protocol
Nexthop                                      Interface
------------------------------------------------------------------------------
 2001:DB8:2::2/64                             Static                             
  ::                                          100GE1/0/2
```

The command output shows that the routing table of DeviceA contains a route to 2001:DB8:2::2/64.

# Verify that DeviceB becomes the master after the link fails. Run the **shutdown** command on DeviceE's 100GE1/0/1 to simulate a fault on the link between DeviceA and DeviceC.

```
[~DeviceA] display ipv6 routing-table brief
Routing Table : _public_
         Destinations : 1        Routes : 1        

Format :
Destination/Mask                             Protocol
Nexthop                                      Interface
------------------------------------------------------------------------------
                           
  2001:DB8:4::1/64                           Static                             
  ::                                         100GE1/0/2
```

The command output shows that the route to 2001:DB8:2::2/64 has been withdrawn on DeviceA.

# Check the states of DeviceA and DeviceB in the VRRP6 group.

```
[~DeviceA] display vrrp6 interface 100GE1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : xxxx::xxxx
Local IP        : xxxx::xxxx
PriorityRun     : 80
PriorityConfig  : 120
MasterPriority  : 100
Preempt         : YES   Delay Time : 20s
Hold Multiplier : 3
TimerRun        : 200ms
TimerConfig     : 200ms
Virtual MAC     : xxxx-xxxx-xxxx
Check hop limit : YES
Config Type     : normal-vrrp
Backup-forward  : disabled
Track IPv6 Route    : 2001:DB8:2::2/64  Priority Reduced : 40
IPv6 Route State    : Unreachable
Create Time       : 2022-02-24 10:23:21
Last Change Time  : 2022-02-24 11:19:36
```
```
[~DeviceB] display vrrp6 interface 100GE1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : xxxx::xxxx
Local IP        : xxxx::xxxx
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 100
Preempt         : YES   Delay Time : 20s
Hold Multiplier : 3
TimerRun        : 200ms
TimerConfig     : 200ms
Virtual MAC     : xxxx-xxxx-xxxx
Check hop limit : YES
Config Type     : normal-vrrp
Backup-forward  : disabled
Create Time       : 2022-02-24 10:23:21
Last Change Time  : 2022-02-24 11:19:36
```

The command outputs show that DeviceA is in the **Backup** state and DeviceB is in the **Master** state in the VRRP6 group. The tracked route is **Unreachable**.

# Verify that DeviceA can preempt the master role after the fault is rectified. Run the **undo shutdown** command on DeviceE's 100GE1/0/1. After the interface goes up, wait 20 seconds.

```
[~DeviceA] display vrrp6 interface 100GE1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State           : Master
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : xxxx::xxxx
Local IP        : xxxx::xxxx
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s
Hold Multiplier : 3
TimerRun        : 200ms
TimerConfig     : 200ms
Virtual MAC     : xxxx-xxxx-xxxx
Check hop limit : YES
Config Type     : normal-vrrp
Backup-forward  : disabled
Track IPv6 Route    : 2001:DB8:2::2/64  Priority Reduced : 40
IPv6 Route State    : Reachable
Create Time       : 2022-02-24 10:23:21
Last Change Time  : 2022-02-24 11:19:36

```
```
[~DeviceB] display vrrp6 interface 100GE1/0/1 verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP      : FE80::1
                  2001:DB8::100
Master IP       : xxxx::xxxx
Local IP        : xxxx::xxxx
PriorityRun     : 100
PriorityConfig  : 100
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s
Hold Multiplier : 3
TimerRun        : 200ms
TimerConfig     : 200ms
Virtual MAC     : xxxx-xxxx-xxxx
Check hop limit : YES
Config Type     : normal-vrrp
Backup-forward  : disabled
Create Time       : 2022-02-24 10:23:21
Last Change Time  : 2022-02-24 11:19:36
```

Run the **display vrrp6 interface verbose** command on DeviceA and DeviceB. The command outputs show that the states of DeviceA and DeviceB in the VRRP6 group switch to **Master** and **Backup**, respectively. The tracked route is in the **Reachable** state on DeviceA.


#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
  #
   ipv6 enable 
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 priority 120
   vrrp6 vrid 1 preempt timer delay 20
   vrrp6 vrid 1 track ip route 2001:DB8:2::2 64 reduce 40
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
  #
   ipv6 enable 
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 priority 120
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
   sysname DeviceC
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
  #
  #
   ipv6 enable 
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
   sysname DeviceD
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
  #
   ipv6 enable 
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceE
  
  ```
  #
   sysname DeviceE
  #
   vlan 10
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 10
  #
  return
  ```