Example for Configuring Association Between VRRP and Route Status to Monitor an Uplink
======================================================================================

Example for Configuring Association Between VRRP and Route Status to Monitor an Uplink

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176663821__fig_dc_cfg_vrrp_005001), a host on a LAN accesses the external network through DeviceF, which is dual-homed to DeviceA and DeviceB. A VRRP group is deployed on DeviceA and DeviceB, of which DeviceA serves as the master. Normally, DeviceA functions as the gateway, and user traffic is forwarded along the path DeviceF -> DeviceA -> DeviceC -> DeviceE.

When the route between DeviceC and DeviceE is withdrawn or becomes inactive, the VRRP group is required to be notified of the fault and perform a master/backup switchover. DeviceB then takes over traffic forwarding to minimize the impact of the link fault on services.

**Figure 1** Network diagram of configuring a VRRP group to track an uplink route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001176663845.png)

#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on the devices and configure a routing protocol to ensure IP connectivity.
2. Configure a VRRP group on DeviceA and DeviceB. Configure a higher priority and a preemption delay of 20s for DeviceA to ensure it functions as the master and forwards traffic. Configure a lower priority for DeviceB so that it functions as the backup.
3. Configure the VRRP group on DeviceA to track an uplink route so that a master/backup VRRP switchover can be performed when the tracked route is withdrawn or becomes inactive.


#### Procedure

1. Assign an IP address to each interface on DeviceA, DeviceB, DeviceC, DeviceD, and DeviceE. Then, configure OSPF to ensure that the devices can communicate with one another. For details about DeviceF's configurations, see [Configuration Scripts](#EN-US_TASK_0000001176663821__context123891331175616).# Configure DeviceA.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 192.168.2.1 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.25
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   # Configure DeviceC.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ip address 192.168.1.2 24
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ip address 172.16.1.1 24
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] undo portswitch
   [*DeviceD-100GE1/0/1] ip address 192.168.2.2 24
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] undo portswitch
   [*DeviceD-100GE1/0/2] ip address 172.16.2.1 24
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] ospf 1
   [*DeviceD-ospf-1] area 0
   [*DeviceD-ospf-1-area-0.0.0.0] network 172.16.2.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] quit
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceE
   [*HUAWEI] commit
   [~DeviceE] interface 100ge 1/0/1
   [~DeviceE-100GE1/0/1] undo portswitch
   [*DeviceE-100GE1/0/1] ip address 172.16.1.2 24
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] interface 100ge 1/0/2
   [*DeviceE-100GE1/0/2] undo portswitch
   [*DeviceE-100GE1/0/2] ip address 172.16.2.2 24
   [*DeviceE-100GE1/0/2] quit
   [*DeviceE] ospf 1
   [*DeviceE-ospf-1] area 0
   [*DeviceE-ospf-1-area-0.0.0.0] network 172.16.2.0 0.0.0.255
   [*DeviceE-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*DeviceE-ospf-1-area-0.0.0.0] quit
   [*DeviceE-ospf-1] quit
   [*DeviceE] commit
   ```
2. Configure a VRRP group on DeviceA and DeviceB.
   
   # Configure VRRP group 1 on DeviceA. Set the VRRP priority of DeviceA to 120 to ensure it functions as the master, and set the preemption delay to 20s.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceA-100GE1/0/1] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/1] vrrp vrid 1 preempt timer delay 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure VRRP group 1 on DeviceB, and use the default priority (100) to ensure it functions as the backup.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Configure the VRRP group on DeviceA to track an uplink route. When the tracked route is withdrawn or becomes inactive, DeviceA reduces its priority by 40.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 track ip route 172.16.1.0 24 reduce 30
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State             : Master
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.1
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES      Delay Time : 20s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Track IP Route    : 172.16.1.0/24  Priority Reduced : 40                         
IP Route State    : Reachable 
Create Time       : 2020-12-29 05:41:23
Last Change Time  : 2020-12-29 05:41:33
```
```
[~DeviceB] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State             : Backup
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

The command outputs show that DeviceA is in the **Master** state and DeviceB is in the **Backup** state.

# Check the routing table on DeviceA.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 14       Routes : 14        

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

       10.1.1.0/24  Direct 0    0             D  10.1.1.1        100GE1/0/1
       10.1.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
     10.1.1.111/32  Direct 0   0             D  127.0.0.1       100GE1/0/1
     10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
   172.16.1.0/24  OSPF  10   2           D  192.168.1.2     100GE1/0/1
      127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
    192.168.1.0/24  Direct 0    0             D  192.168.1.1     100GE1/0/2
    192.168.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
    192.168.1.2/32  Direct 0    0             D  192.168.1.2     100GE1/0/2
  192.168.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
    192.168.2.0/24  OSPF   10   2             D  10.1.1.2        100GE1/0/1
255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
```

The command output shows that the routing table of DeviceA contains a route to the network segment 172.16.1.0/24.

# Verify that DeviceB becomes the master after DeviceA fails. Run the **shutdown** command on DeviceE's 100GE1/0/1 to simulate a fault on the link between DeviceC and DeviceE.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 14       Routes : 14        

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

       10.1.1.0/24  Direct 0    0             D  10.1.1.1        100GE1/0/1
       10.1.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
     10.1.1.111/32  Direct 0   0             D  127.0.0.1       100GE1/0/1
     10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
      127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
    192.168.1.0/24  Direct 0    0             D  192.168.1.1     100GE1/0/2
    192.168.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
    192.168.1.2/32  Direct 0    0             D  192.168.1.2     100GE1/0/2
  192.168.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
    192.168.2.0/24  OSPF   10   2             D  10.1.1.2        100GE1/0/1
255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
```

The preceding command output shows that the route to 172.16.1.0/24 on DeviceA is withdrawn.

# Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State             : Backup
Virtual IP        : 10.1.1.111
Master IP         : 0.0.0.0
PriorityRun       : 80
PriorityConfig    : 120
MasterPriority    : 0
Preempt           : YES      Delay Time : 20s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Track IP Route    : 172.16.1.0/24  Priority Reduced : 40                         
IP Route State    : Unreachable
Create Time       : 2020-12-29 05:51:23
Last Change Time  : 2020-12-29 05:51:33
```
```
[~DeviceB] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State             : Master
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.2
PriorityRun       : 100
PriorityConfig    : 100
MasterPriority    : 100
Preempt           : YES      Delay Time : 0s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:51:23
Last Change Time  : 2020-12-29 05:51:33
```

The command outputs show that DeviceA is in the **Backup** state and DeviceB is in the **Master** state in VRRP group 1. The tracked route is **Unreachable**.

# Verify that DeviceA can preempt the master role after the fault is rectified. Run the **undo shutdown** command on DeviceE's 100GE1/0/1. After the interface goes up, wait for 20 seconds or longer before you check the devices' states.

```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State            : Master
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.1
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES      Delay Time : 20s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Track IP Route    : 172.16.1.0/24  Priority Reduced : 40                         
IP Route State    : Reachable 
Create Time       : 2020-12-29 05:56:23
Last Change Time  : 2020-12-29 05:56:33
```
```
[~DeviceB] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State            : Backup
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
Create Time       : 2020-12-29 05:56:23
Last Change Time  : 2020-12-29 05:56:33
```

Run the **display vrrp verbose** command on DeviceA and DeviceB. The command outputs show that the VRRP statuses of DeviceA and DeviceB switch to **Master** and **Backup**, respectively. The tracked route is in the **Reachable** state on DeviceA.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt timer delay 20
   vrrp vrid 1 track ip route 172.16.1.0 24 reduce 30
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 10.1.1.0 0.0.0.255
  #
  return
  ```

* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* DeviceE
  
  ```
  #
   sysname DeviceE
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 172.16.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 172.16.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.16.2.0 0.0.0.255
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
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