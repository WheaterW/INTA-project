Example for Configuring VRRP in Master/Backup Mode
==================================================

Example for Configuring VRRP in Master/Backup Mode

#### Networking Requirements

Hosts are connected to a network through gateways. To ensure non-stop service transmission, configure VRRP in master/backup mode on the gateways.

As shown in [Figure 1](#EN-US_TASK_0000001130784044__fig_dc_vrp_vrrp_cfg_012101), DeviceD is dual-homed to DeviceA and DeviceB. DeviceA functions as the master device to forward service traffic, and DeviceB is the backup device. If DeviceA fails, DeviceB takes over to forward service traffic. Then, once DeviceA recovers, traffic switches back to DeviceA.

**Figure 1** Network diagram of configuring VRRP in master/backup mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176743733.png)

#### Precautions

DeviceA's interface (100GE1/0/3) and DeviceB's interface (100GE1/0/3) must be on the same network segment.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on the devices and configure a routing protocol to ensure IP connectivity.
2. Configure a VRRP group on DeviceA and DeviceB. Configure a higher priority for DeviceA to ensure it functions as the master and configure a lower priority for DeviceB to ensure it functions as the backup.

#### Procedure

1. Assign an IP address to each interface on DeviceA, DeviceB, and DeviceC. Then, configure OSPF to ensure that the devices can communicate with one another. For details about DeviceD's configurations, see [Configuration Scripts](#EN-US_TASK_0000001130784044__section_dc_vrp_vrrp_cfg_012105).# Configure DeviceA.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/3
   [~DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/1] quit
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
   [~DeviceB] interface 100ge 1/0/3
   [~DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 192.168.2.1 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
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
   [*DeviceC-100GE1/0/2] ip address 192.168.2.2 24
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] undo portswitch
   [*DeviceC-100GE1/0/3] ip address 172.16.1.1 24
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
2. Configure a VRRP group on DeviceA and DeviceB.
   
   # Create VRRP group 1 on DeviceA and configure a VRRP security policy. Configure a priority of 120 to ensure that DeviceA functions as the master device, and set the preemption delay to 20s.
   
   ```
   [~DeviceA] interface 100ge 1/0/3
   [~DeviceA-100GE1/0/3] vrrp vrid 1 virtual-ip 10.1.1.111
   [~DeviceA-100GE1/0/3] vrrp vrid 1 authentication-mode md5 YsH_2022
   [*DeviceA-100GE1/0/3] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/3] vrrp vrid 1 preempt timer delay 20
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Create VRRP group 1 on DeviceB, configure a VRRP security policy, and use the default priority (100) to ensure it functions as the backup.
   
   ```
   [~DeviceB] interface 100ge 1/0/3
   [~DeviceB-100GE1/0/3] vrrp vrid 1 virtual-ip 10.1.1.111
   [~DeviceB-100GE1/0/3] vrrp vrid 1 authentication-mode md5 YsH_2022
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp verbose
100GE1/0/3 | Virtual Router 1
State         : Master
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.1
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES      Delay Time : 20s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : MD5      Auth Key : ******
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:41:23
Last Change Time  : 2020-12-29 05:41:33
```
```
[~DeviceB] display vrrp verbose
100GE1/0/3 | Virtual Router 1
State         : Backup
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.1
PriorityRun       : 100
PriorityConfig    : 100
MasterPriority    : 120
Preempt           : YES      Delay Time : 0s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : MD5      Auth Key : ******
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:41:23
Last Change Time  : 2020-12-29 05:41:33
```

The command outputs show that DeviceA is in the Master state and DeviceB is in the Backup state.

# Check routing information on DeviceA and DeviceB.

```
[~DeviceA] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 14       Routes : 14        

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

       10.1.1.0/24  Direct 0    0             D  10.1.1.1        100GE1/0/3
       10.1.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
   10.1.1.111/32  Direct 0   0           D  127.0.0.1     100GE1/0/3
     10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
     172.16.1.0/24  OSPF   10   2             D  192.168.1.2     100GE1/0/3
      127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
    192.168.1.0/24  Direct 0    0             D  192.168.1.1     100GE1/0/1
    192.168.1.1/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
    192.168.1.2/32  Direct 0    0             D  192.168.1.2     100GE1/0/1
  192.168.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/1
    192.168.2.0/24  OSPF   10   2             D  10.1.1.2        100GE1/0/3
255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
```
```
[~DeviceB] display ip routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 13       Routes : 13        

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

       10.1.1.0/24  Direct 0    0             D  10.1.1.2        100GE1/0/3
       10.1.1.2/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
   10.1.1.111/32  OSPF  10  2            D  10.1.1.1      100GE1/0/3
     10.1.1.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/3
     172.16.1.0/24  OSPF   10   2             D  192.168.2.2     100GE1/0/2
      127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
      127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
    192.168.1.0/24  OSPF   10   2             D  10.1.1.1        100GE1/0/3
    192.168.2.0/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
    192.168.2.1/32  Direct 0    0             D  192.168.2.1     100GE1/0/2
    192.168.2.2/24  Direct 0    0             D  127.0.0.1       100GE1/0/2
  192.168.2.255/32  Direct 0    0             D  127.0.0.1       100GE1/0/2
255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
```

The command outputs show that a direct route to the virtual IP address of the VRRP group is available in DeviceA's routing table and an OSPF route to the virtual IP address of the VRRP group is available in DeviceB's routing table.

# Verify that DeviceB becomes the master after DeviceA fails. Run the **shutdown** command on DeviceA's 100GE1/0/3 to simulate a fault on DeviceA.

```
[~DeviceA] display vrrp verbose
100GE1/0/3 | Virtual Router 1
State             : Initialize
Virtual IP        : 10.1.1.111
Master IP         : 0.0.0.0
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 0
Preempt           : YES      Delay Time : 20s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : MD5      Auth Key : ******
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:51:23
Last Change Time  : 2020-12-29 05:51:33
```
```
[~DeviceB] display vrrp verbose
100GE1/0/3 | Virtual Router 1
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
Auth Type         : MD5      Auth Key : ******
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:51:23
Last Change Time  : 2020-12-29 05:51:33
```

The command outputs show that DeviceA is in the Initialize state and DeviceB is in the Master state.

# Verify that DeviceA can preempt the master role after the fault is rectified. Run the **undo shutdown** command on DeviceA's 100GE1/0/3. After the interface goes up, wait for 20 seconds or longer before you check the devices' status.

```
[~DeviceA] display vrrp verbose
100GE1/0/3 | Virtual Router 1
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
Auth Type         : MD5      Auth Key : ******
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:56:23
Last Change Time  : 2020-12-29 05:56:33
```
```
[~DeviceB] display vrrp verbose
100GE1/0/3 | Virtual Router 1
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
Auth Type         : MD5      Auth Key : ******
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Create Time       : 2020-12-29 05:56:23
Last Change Time  : 2020-12-29 05:56:33
```

The command outputs show that DeviceA is in the Master state and DeviceB is in the Backup state.


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
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 authentication-mode md5 YsH_2022
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt timer delay 20
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
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 authentication-mode md5 YsH_2022
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
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 172.16.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* DeviceD
  
  ```
  #
   sysname DeviceD
  #
   vlan 10
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port link-type access
   port default vlan 10
  #
  return
  ```