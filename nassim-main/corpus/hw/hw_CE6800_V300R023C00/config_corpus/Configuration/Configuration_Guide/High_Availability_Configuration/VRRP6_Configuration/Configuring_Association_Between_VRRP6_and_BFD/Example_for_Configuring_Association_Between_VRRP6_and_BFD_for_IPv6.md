Example for Configuring Association Between VRRP6 and BFD for IPv6
==================================================================

Example for Configuring Association Between VRRP6 and BFD for IPv6

#### Networking Requirements

Hosts are connected to an upper-layer network through gateways. To improve network reliability, configure a VRRP6 group on the gateways. To further improve network reliability and implement rapid master/backup VRRP switchovers, configure VRRP6 association.

In [Figure 1](#EN-US_TASK_0000001176661765__fig_dc_vrp_vrrp6_cfg_011701), the master device (DeviceA) forwards traffic in normal cases. It is required that the backup device (DeviceB) take over traffic forwarding if BFD detects a fault in the link between DeviceA and DeviceB. After DeviceA recovers, traffic switches back to it.![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.



**Figure 1** Network diagram for configuring VRRP6 association  
![](figure/en-us_image_0000001176741687.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Configure a VRRP6 group on user-side gateways (DeviceA and DeviceB). Configure a higher priority for DeviceA to ensure it functions as the master and a lower priority for DeviceB to ensure it functions as the backup.
3. Configure a BFD for IPv6 session on DeviceA and DeviceB to monitor the link DeviceA -> DeviceD -> DeviceB.
4. Configure DeviceB (backup) in the VRRP6 group to track the BFD for IPv6 session. If the BFD for IPv6 session goes down, a master/backup VRRP switchover is performed.


#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001176661765__context1421141332420).
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
   [*HUAWEI] sysname DeviceB
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
3. Configure basic BFD for IPv6 functions.# Configure a BFD for IPv6 session on DeviceA.
   ```
   [~DeviceA] bfd
   [~DeviceA-bfd] quit
   [~DeviceA] bfd atob bind peer-ipv6 2001:db8::2 interface 100ge 1/0/1
   [*DeviceA-bfd-session-atob] discriminator local 1
   [*DeviceA-bfd-session-atob] discriminator remote 2
   [*DeviceA-bfd-session-atob] min-rx-interval 50
   [*DeviceA-bfd-session-atob] min-tx-interval 50 
   [*DeviceA-bfd-session-atob] quit
   [*DeviceA] commit
   ```
   
   # Configure a BFD for IPv6 session on DeviceB.
   ```
   [~DeviceB] bfd
   [~DeviceB-bfd] quit
   [~DeviceB] bfd btoa bind peer-ipv6 2001:db8::1 interface 100ge 1/0/1
   [*DeviceB-bfd-session-btoa] discriminator local 2
   [*DeviceB-bfd-session-btoa] discriminator remote 1
   [*DeviceB-bfd-session-btoa] min-rx-interval 50
   [*DeviceB-bfd-session-btoa] min-tx-interval 50
   [*DeviceB-bfd-session-btoa] quit
   [*DeviceB] commit
   ```
   
   # After completing the configurations, run the **display bfd session all** command on DeviceA and DeviceB. The command outputs show that a BFD for IPv6 session has been established and is in the **Up** state. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all
   S: Static session
   D: Dynamic session
   IP: IP session
   IF: Single-hop session
   PEER: Multi-hop session
   AUTO: Automatically negotiated session
   VXLAN: VXLAN session
   (w): State in WTR 
   (*): State is invalid
   Total UP/DOWN Session Number : 1/0
   --------------------------------------------------------------------------------
   Local Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   1     2      2001:DB8::2     Up        S_IP_IF     100GE1/0/1
   -------------------------------------------------------------------------------- 
   ```
4. Configure VRRP6 association. On DeviceB, associate the VRRP6 group with the BFD for IPv6 session.
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp6 vrid 1 track bfd 2 increase 40
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the states of DeviceA and DeviceB in the VRRP6 group.

```
[~DeviceA] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State             : Master
Virtual IP        : FE80::1
                    2001:DB8::100
Master IP         : 2001:DB8::1
Local IP          : 2001:DB8::1   
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES   Delay Time : 20s   Remain : --
Hold Multiplier   : 4
TimerRun          : 100cs
TimerConfig       : 100cs
Virtual MAC       : 0000-5e00-0201
Check hop limit   : YES
Config Type       : Normal
Create Time       : 2020-07-27 17:33:00
Last Change Time  : 2020-07-27 17:33:04
```

The command output shows that DeviceA is in the **Master** state in the VRRP6 group.

```
[~DeviceB] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State             : Backup
Virtual IP        : FE80::1
                    2001:DB8::100
Master IP         : 2001:DB8::1
Local IP          : 2001:DB8::2
PriorityRun       : 100
PriorityConfig    : 100
MasterPriority    : 120
Preempt           : YES   Delay Time : 0s   Remain : --
Hold Multiplier   : 4
TimerRun          : 100cs
TimerConfig       : 100cs
Virtual MAC       : 0000-5e00-0202
Check hop limit   : YES
Config Type       : Normal
Track BFD         : btoa                 Priority Increased : 40
BFD-Session State : UP
Create Time       : 2020-07-27 17:33:00
Last Change Time  : 2020-07-27 17:33:04
```

The command output shows that DeviceB is in the **Backup** state in the VRRP6 group and is associated with BFD.

# Run the **shutdown** command on DeviceA's 100GE1/0/1 to simulate a device fault. Check the states of DeviceA and DeviceB in the VRRP6 group.

```
[~DeviceA] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State             : Backup
Virtual IP        : FE80::1
                    2001:DB8::100
Master IP         : 2001:DB8::2
Local IP          : 2001:DB8::1 
PriorityRun       : 80
PriorityConfig    : 120
MasterPriority    : 100
Preempt           : YES   Delay Time : 20s   Remain : --
Hold Multiplier   : 4
TimerRun          : 100cs
TimerConfig       : 100cs
Virtual MAC       : 0000-5e00-0201
Check hop limit   : YES
Config Type       : Normal
Create Time       : 2020-07-27 17:33:00
Last Change Time  : 2020-07-27 17:35:14
```

The command output shows that DeviceA is in the **Backup** state in the VRRP6 group.

```
[~DeviceB] display vrrp6 verbose
100GE1/0/1 | Virtual Router 1
State             : Master
Virtual IP        : FE80::1
                    2001:DB8::100
Master IP         : 2001:DB8::2  
Local IP          : 2001:DB8::2
PriorityRun       : 100
PriorityConfig    : 100
MasterPriority    : 100
Preempt           : YES   Delay Time : 0s   Remain : --
Hold Multiplier   : 4
TimerRun          : 100cs
TimerConfig       : 100cs
Virtual MAC       : 0000-5e00-0202
Check hop limit   : YES
Config Type       : Normal
Track BFD         : btoa                 Priority Increased : 40
BFD-Session State : DOWN
Create Time       : 2020-07-27 17:33:00
Last Change Time  : 2020-07-27 17:33:04
```

The command output shows that DeviceB is in the **Master** state in the VRRP6 group.

# Run the **undo shutdown** command on DeviceA's 100GE1/0/1. After 100GE1/0/1 goes up, wait 20 seconds and check the state of DeviceA in the VRRP6 group.

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
   bfd
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
  bfd atob bind peer-ipv6 2001:DB8::2 interface 100GE1/0/1
   discriminator local 1
   discriminator remote 2
   min-tx-interval 50
   min-rx-interval 50
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
   ospfv3 1
   router-id 2.2.2.2
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 track bfd session-name btoa increase 40
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  bfd btoa bind peer-ipv6 2001:DB8::1 interface 100GE1/0/1
   discriminator local 2
   discriminator remote 1
   min-tx-interval 50
   min-rx-interval 50
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