Example for Configuring VRRP6 Groups to Work in Multi-gateway Load Balancing Mode
=================================================================================

In this example, two VRRP6 groups are configured to work in multi-gateway load balancing mode. Devices in the VRRP6 groups back up each other and load-balance traffic.

#### Networking Requirements

Hosts are connected to a network through gateway Routers. To improve network reliability, configure a VRRP6 group to work in master/backup mode on gateway Routers. If multiple VRRP6 groups run on a device, configure the groups to work in multi-gateway load balancing mode to load-balance traffic.

As shown in [Figure 1](#EN-US_TASK_0172361876__fig_dc_vrp_vrrp6_cfg_011601):

* DeviceA functions as the master device in VRRP6 group 1 and the backup device in VRRP6 group 2.
* DeviceB functions as the master device in VRRP6 group 2 and the backup device in VRRP6 group 1.
* HostA uses the virtual IPv6 address of VRRP6 group 1 as a default gateway address, and HostB uses the virtual IPv6 address of VRRP6 group 2 as a default gateway address. The two VRRP6 groups back up each other and load-balance data traffic.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/4, respectively.



**Figure 1** VRRP6 groups working in multi-gateway load balancing mode  
![](images/fig_dc_vrp_vrrp6_cfg_011601.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Create VRRP6 groups 1 and 2 on DeviceA's GE 0/1/0, where DeviceA functions as the master device in VRRP6 group 1 and as a backup device in VRRP6 group 2.
3. Create VRRP6 groups 1 and 2 on DeviceB's GE 0/1/0, where DeviceB functions as a backup device in VRRP6 group 1 and as the master device in VRRP6 group 2.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on each device (for configuration details, see [Configuration Files](#EN-US_TASK_0172361876__section_05) in this section)
* VRRP6 group 1's virtual IPv6 address: 2001:db8::100; VRRP6 group 2's virtual IPv6 address: 2001:db8::60
* DeviceA's priority in VRRP6 group 1: 120; DeviceB's priority in VRRP6 group 1: 100
* DeviceB's priority in VRRP6 group 2: 120; DeviceA's priority in VRRP6 group 2: 100

#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate with each other. For configuration details, see [Configuration Files](#EN-US_TASK_0172361876__section_05) in this section.
2. Create VRRP6 groups.
   
   
   
   # Assign an IPv6 address to GE 0/1/0 on DeviceA. Create VRRP6 groups 1 and 2 on GE 0/1/0. Set DeviceA's priority to 120 in VRRP6 group 1, and retain the default priority (100) for DeviceA in VRRP6 group 2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:DB8::1/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip 2001:DB8::100
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 priority 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 2 virtual-ip fe80::2 link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 2 virtual-ip 2001:DB8::60
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] quit
   ```
   
   # Assign an IPv6 address to GE 0/1/0 on DeviceB. Create VRRP6 groups 1 and 2 on GE 0/1/0. Set DeviceB's priority to 120 in VRRP6 group 2, and retain the default priority (100) for DeviceB in VRRP6 group 1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:DB8::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip 2001:DB8::100
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 2 virtual-ip fe80::2 link-local
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 2 virtual-ip 2001:DB8::60
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 2 priority 120
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, ping HostC from HostA and HostB. The pings are successful. Run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA functions as the master device in VRRP6 group 1 and as a backup device in VRRP6 group 2.
   
   ```
   <DeviceA> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Master
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : 2001:DB8::1
   Local IP        : 2001:DB8::1 
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
   Create Time       : 2013-07-27 20:15:46
   Last Change Time  : 2013-07-27 20:15:46
   
   GigabitEthernet0/1/0 | Virtual Router 2
   State           : Backup
   Virtual IP      : FE80::2
                     2001:DB8::60
   Master IP       : 2001:DB8::2
   Local IP        : 2001:DB8::1 
   PriorityRun     : 100
   PriorityConfig  : 100
   MasterPriority  : 120
   Preempt         : YES   Delay Time : 0s   Remain : --
   Hold Multiplier : 4
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 00e0-fc12-7880
   Check hop limit : YES
   Config Type     : Normal
   Create Time       : 2013-07-27 20:17:46
   Last Change Time  : 2013-07-27 20:17:46
   ```
   
   Run the **display vrrp6 verbose** command on DeviceB. The command output shows that DeviceB functions as the master device in VRRP6 group 2 and as a backup device in VRRP6 group 1.
   
   ```
   <DeviceB> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
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
   Create Time       : 2013-07-27 20:19:46
   Last Change Time  : 2013-07-27 20:19:46
   
   GigabitEthernet0/1/0 | Virtual Router 2
   State           : Master
   Virtual IP      : FE80::2
                     2001:DB8::60
   Master IP       : 2001:DB8::2
   Local IP        : 2001:DB8::2
   PriorityRun     : 120
   PriorityConfig  : 120
   MasterPriority  : 120
   Preempt         : YES   Delay Time : 0s   Remain : --
   Hold Multiplier : 4
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 00e0-fc12-7880
   Check hop limit : YES
   Config Type     : Normal
   Create Time       : 2013-07-27 20:21:46
   Last Change Time  : 2013-07-27 20:21:46
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8::1/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 priority 120
   vrrp6 vrid 2 virtual-ip FE80::2 link-local
   vrrp6 vrid 2 virtual-ip 2001:DB8::60
   ospfv3 1 area 0.0.0.0
   #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8::2/64
   vrrp6 vrid 1 virtual-ip FE80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 2 virtual-ip FE80::2 link-local
   vrrp6 vrid 2 virtual-ip 2001:DB8::60
   vrrp6 vrid 2 priority 120
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
   sysname DeviceC
  #
  ospfv3 1
   router-id 3.3.3.3
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```