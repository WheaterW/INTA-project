Example for Configuring VRRP in Multi-Gateway Load Balancing Mode
=================================================================

Example for Configuring VRRP in Multi-Gateway Load Balancing Mode

#### Networking Requirements

A VRRP group working in master/backup mode can be configured on gateways to implement gateway redundancy. To reduce the traffic load on the master device, configure VRRP groups working in multi-gateway load balancing mode to balance uplink traffic.

As shown in [Figure 1](#EN-US_TASK_0000001130624260__fig_dc_vrp_vrrp_cfg_012201), DeviceD is dual-homed to DeviceA and DeviceB. Traffic of some hosts needs to be forwarded using DeviceA, with DeviceB serving as the backup; whereas traffic of other hosts needs to be forwarded using DeviceB, with DeviceA serving as the backup. When DeviceA and DeviceB function as master devices in different backup groups, they can back up each other and balance data traffic.

**Figure 1** Network diagram of configuring VRRP in multi-gateway load balancing mode![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130784080.png)

#### Precautions

DeviceA's interface (100GE1/0/3) and DeviceB's interface (100GE1/0/3) must be on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface of the devices and configure a routing protocol to ensure IP connectivity.
2. Configure two VRRP groups on user-side gateways. To balance traffic, configure DeviceA as the master in VRRP group 1 and DeviceB as the master device in VRRP group 2.

#### Procedure

1. Assign an IP address to each interface on DeviceA, DeviceB, and DeviceC. Configure OSPF to ensure that the devices can communicate. For details about DeviceD's configurations, see [Configuration Scripts](#EN-US_TASK_0000001130624260__context67671718387)
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge1/0/3
   [~DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge1/0/1
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
   [~DeviceB] interface 100ge1/0/3
   [~DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge1/0/2
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
   [~DeviceC] interface 100ge1/0/1
   [~DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ip address 192.168.1.2 24
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ip address 192.168.2.2 24
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge1/0/3
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
2. Configure VRRP groups on DeviceA and DeviceB.
   
   # Create VRRP groups 1 and 2 on DeviceA's interface. Set the priority to 120 for DeviceA to ensure that it functions as the master in VRRP group 1, and use the default priority 100 for DeviceA to ensure that it functions as the backup in VRRP group 2.
   
   ```
   [~DeviceA] interface 100ge1/0/3
   [~DeviceA-100GE1/0/3] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceA-100GE1/0/3] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/3] vrrp vrid 2 virtual-ip 10.1.1.112
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   # Create VRRP groups 1 and 2 on DeviceB's interface. Use the default priority 100 for DeviceB to ensure that it functions as the backup in VRRP group 1, and set the priority to 120 for DeviceB to ensure that it functions as the master in VRRP group 2.
   
   ```
   [~DeviceB] interface 100ge1/0/3
   [~DeviceB-100GE1/0/3] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceB-100GE1/0/3] vrrp vrid 2 virtual-ip 10.1.1.112
   [*DeviceB-100GE1/0/3] vrrp vrid 2 priority 120
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the VRRP status on DeviceA and DeviceB.

```
<DeviceA> display vrrp verbose
100GE1/0/3 | Virtual Router 1
State             : Master
Virtual IP          : 10.1.1.1
Master IP           : 10.1.1.1
PriorityRun         : 120
PriorityConfig      : 120
MasterPriority      : 120
Preempt             : YES      Delay Time : 0s    Remain : --
Hold Multiplier     : 4
TimerRun            : 1s
TimerConfig         : 1s
Auth Type           : NONE
Virtual MAC         : 0000-5e00-0101
Check TTL           : YES
Config Type         : Normal
Create Time         : 2020-12-29 05:41:23
Last Change Time    : 2020-12-29 05:41:33

100GE1/0/3| Virtual Router 2
State             : Backup
Virtual IP          : 10.1.1.112
Master IP           : 10.1.1.2
PriorityRun         : 100
PriorityConfig      : 100
MasterPriority      : 120
Preempt             : YES      Delay Time : 0s    Remain : --
Hold Multiplier     : 4
TimerRun            : 1s
TimerConfig         : 1s
Auth Type           : NONE
Virtual MAC         : 0000-5e00-0101
Check TTL           : YES
Config Type         : Normal
Create Time         : 2020-12-29 05:41:23
Last Change Time    : 2020-12-29 05:41:33
```
```
<DeviceB> display vrrp verbose
100GE1/0/3 | Virtual Router 1
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
Virtual MAC         : 0000-5e00-0102
Check TTL           : YES
Config Type         : Normal
Create Time         : 2020-12-29 05:41:23
Last Change Time    : 2020-12-29 05:41:33

100GE1/0/3 | Virtual Router 2
State             : Master
Virtual IP          : 10.1.1.112
Master IP           : 10.1.1.2
PriorityRun         : 120
PriorityConfig      : 120
MasterPriority      : 120
Preempt             : YES      Delay Time : 0s    Remain : --
Hold Multiplier     : 4
TimerRun            : 1s
TimerConfig         : 1s
Auth Type           : NONE
Virtual MAC         : 0000-5e00-0102
Check TTL           : YES
Config Type         : Normal
Create Time         : 2020-12-29 05:41:23
Last Change Time    : 2020-12-29 05:41:33
```

The command outputs show that DeviceA functions as the master device in VRRP group 1 and the backup device in VRRP group 2, and DeviceB functions as the backup device in VRRP group 1 and the master device in VRRP group 2.


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
   vrrp vrid 1 priority 120
   vrrp vrid 2 virtual-ip 10.1.1.112
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
   vrrp vrid 2 virtual-ip 10.1.1.112
   vrrp vrid 2 priority 120
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