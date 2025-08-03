Example for Configuring VRRP in Single-Gateway Load Balancing Mode
==================================================================

Example for Configuring VRRP in Single-Gateway Load Balancing Mode

#### Networking Requirements

A VRRP group working in master/backup mode can be configured on gateways to implement gateway redundancy. To reduce the traffic load on the master device, configure VRRP groups working in single-gateway load balancing mode to balance uplink traffic.

As shown in [Figure 1](#EN-US_TASK_0000001130624254__fig_dc_vrp_vrrp_cfg_013001), DeviceD is dual-homed to DeviceA and DeviceB. Traffic of some hosts needs to be forwarded using DeviceA, with DeviceB serving as the backup; whereas traffic of other hosts needs to be forwarded using DeviceB, with DeviceA serving as the backup. When DeviceA and DeviceB function as master devices in different backup groups, they can back up each other and balance data traffic.

**Figure 1** Network diagram of configuring VRRP in single-gateway load balancing mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130624278.png)

#### Precautions

DeviceA's interface (100GE1/0/3) and DeviceB's interface (100GE1/0/3) must be on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface of the devices and configure a routing protocol to ensure IP connectivity.
2. Configure two VRRP groups on user-side gateways. To balance traffic, configure VRRP group 1 as an LBRG with DeviceA being the master and VRRP group 2 as an LBRG member group with DeviceB being the master.

#### Procedure

1. Assign an IP address to each interface on DeviceA, DeviceB, and DeviceC. Configure OSPF to ensure that the devices can communicate. For details about DeviceD's configurations, see [Configuration Scripts](#EN-US_TASK_0000001130624254__example1700881952214023).
   
   # Configure DeviceA.
   
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
   
   # Create VRRP groups 1 and 2 on DeviceA's interface. Set the priority to 120 for DeviceA to ensure that it functions as the master in VRRP group 1, and use the default priority 100 for DeviceA to ensure that it functions as the backup in VRRP group 2.
   
   ```
   [~DeviceA] interface 100ge1/0/3
   [~DeviceA-100GE1/0/3] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceA-100GE1/0/3] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/3] vrrp vrid 2
   ```
   
   # On DeviceA's GE0/1/3, configure VRRP group 1 as an LBRG and add VRRP group 2 to the LBRG.
   
   ```
   [~DeviceA-100GE1/0/3] vrrp vrid 1 load-balance
   [*DeviceA-100GE1/0/3] vrrp vrid 2 join load-balance-vrrp vrid 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Create VRRP groups 1 and 2 on DeviceB's interface. Use the default priority 100 for DeviceB to ensure that it functions as the backup in VRRP group 1, and set the priority to 120 for DeviceB to ensure that it functions as the master in VRRP group 2.
   
   ```
   [~DeviceB] interface 100ge1/0/3
   [~DeviceB-100GE1/0/3] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceB-100GE1/0/3] vrrp vrid 2
   [*DeviceB-100GE1/0/3] vrrp vrid 2 priority 120
   ```
   
   # On DeviceB's GE0/1/3, configure VRRP group 1 as an LBRG and add VRRP group 2 to the LBRG.
   
   ```
   [~DeviceB-100GE1/0/3] vrrp vrid 1 load-balance
   [*DeviceB-100GE1/0/3] vrrp vrid 2 join load-balance-vrrp vrid 1
   [*DeviceB-100GE1/0/3] quit
   
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the VRRP status on DeviceA and DeviceB.

```
<DeviceA> display vrrp verbose
100GE1/0/3 | Virtual Router 1
State           : Master
Virtual IP      : 10.1.1.111
Master IP         : 10.1.1.1
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES   Delay Time : 0s   Remain : --
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00e0-fc12-3456
Check TTL         : YES
Config Type     : Load-Balance
Create Time       : 2020-10-19 03:29:46
Last Change Time  : 2020-10-19 03:29:51

100GE1/0/3 | Virtual Router 2
State          : Backup
Virtual IP     : 0.0.0.0
Master IP        : 10.1.1.2
PriorityRun      : 100
PriorityConfig   : 100
MasterPriority   : 120
Preempt          : YES   Delay Time : 0s   Remain : --
TimerRun         : 1s
TimerConfig      : 1s
Auth Type        : NONE
Virtual MAC      : 00e0-fc12-3457
Check TTL        : YES
Config Type    : Load-Balance-Member
Create Time      : 2020-10-19 03:30:17
Last Change Time : 2020-10-19 03:33:05
                                           
```
```
<DeviceB> display vrrp verbose
100GE1/0/3 | Virtual Router 1
State           : Backup
Virtual IP      : 10.1.1.111
Master IP         : 10.1.1.1
PriorityRun       : 100
PriorityConfig    : 100
MasterPriority    : 120
Preempt           : YES   Delay Time : 0s   Remain : --
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00e0-fc12-3456
Check TTL         : YES
Config Type     : Load-Balance
Create Time       : 2012-10-19 03:32:29
Last Change Time  : 2012-10-19 03:32:31

100GE1/0/3 | Virtual Router 2
State           : Master
Virtual IP      : 0.0.0.0
Master IP         : 10.1.1.2
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES   Delay Time : 0s   Remain : --
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00e0-fc12-3457
Check TTL         : YES
Config Type     : Load-Balance-Member
Create Time       : 2020-10-19 03:32:51
Last Change Time  : 2020-10-19 03:33:04                            
```

The command outputs show that DeviceA functions as the master in the LBRG and as the backup in the LBRG member group and DeviceB functions as the backup in the LBRG and as the master in the LBRG member group.

# Check information about the LBRG and its member group.

```
<DeviceA> display vrrp load-balance member-vrrp
Interface: 100GE1/0/3, load-balance-vrrp vrid: 1, state: Master
  Member-vrrp number: 1
    Member-vrrp vrid: 2, state: Backup
```
```
<DeviceB> display vrrp load-balance member-vrrp
Interface: 100GE1/0/3, load-balance-vrrp vrid: 1, state: Backup
  Member-vrrp number: 1
    Member-vrrp vrid: 2, state: Master
```

The command outputs show information about the LBRG and its member group on DeviceA and DeviceB, respectively.


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
   vrrp vrid 1 load-balance
   vrrp vrid 1 priority 120
   vrrp vrid 2
   vrrp vrid 2 join load-balance-vrrp vrid 1
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
   vrrp vrid 1 load-balance
   vrrp vrid 2
   vrrp vrid 2 priority 120
   vrrp vrid 2 join load-balance-vrrp vrid 1
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
  vlan batch 10
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 10
  #
  return
  ```