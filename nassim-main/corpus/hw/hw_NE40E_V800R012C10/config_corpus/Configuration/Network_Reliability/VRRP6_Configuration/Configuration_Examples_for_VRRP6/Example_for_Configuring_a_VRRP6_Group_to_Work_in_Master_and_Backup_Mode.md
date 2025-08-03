Example for Configuring a VRRP6 Group to Work in Master/Backup Mode
===================================================================

In this example, a VRRP6 group is configured to work in master/backup mode, improving network reliability.

#### Networking Requirements

Hosts are connected to an upper-layer network through gateways. To improve network reliability, configure a VRRP6 group on the gateways to implement gateway redundancy.

As shown in [Figure 1](#EN-US_TASK_0172361873__fig_dc_vrp_vrrp6_cfg_011501), the master device (DeviceA) forwards traffic in normal circumstances. If DeviceA fails, the backup device (DeviceB) takes over traffic forwarding. After DeviceA recovers, traffic switches back to DeviceA.![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/4, respectively.



**Figure 1** VRRP6 group working in master/backup mode  
![](images/fig_dc_vrp_vrrp6_cfg_011501.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Configure a VRRP6 group on user-side gateways (DeviceA and DeviceB). Configure a higher priority for DeviceA to ensure it functions as the master and a lower priority for DeviceB to ensure it functions as the backup.


#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on each device (for configuration details, see [Configuration Files](#EN-US_TASK_0172361873__section_05) in this section)
* ID of a VRRP6 group: 1; virtual IPv6 address: 2001:db8::100
* DeviceA's priority: 120; DeviceB's priority: 100
* DeviceA's preemption delay: 20 seconds


#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate with each other. For configuration details, see [Configuration Files](#EN-US_TASK_0172361873__section_05) in this section.
2. Create a VRRP6 group.
   
   
   
   # Assign an IPv6 address to GE 0/1/0 on DeviceA. Create VRRP6 group 1 on GE 0/1/0, and set the priority of DeviceA to 120 so that DeviceA functions as the master device.
   
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
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8::1/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip 2001:db8::100
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 priority 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 preempt-mode timer delay 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 recover-delay 20
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
   
   # Assign an IPv6 address to GE 0/1/0 on DeviceB. Create VRRP6 group 1 on GE 0/1/0, and retain the default priority for DeviceB so that DeviceB functions as a backup device.
   
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
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip 2001:db8::100
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
   
   
   
   After completing the configurations, ping HostB from HostA. The ping is successful. Run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA's status is **Master**.
   
   ```
   <DeviceA> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Master
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : FE80::3A40:15FF:FE11:300
   Local IP        : FE80::3A40:15FF:FE11:300
   PriorityRun     : 120
   PriorityConfig  : 120
   MasterPriority  : 120
   Preempt         : YES   Delay Time : 20s   Remain : --
   Hold Multiplier : 3
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : normal-vrrp
   Backup-forward  : disabled
   Create Time       : 2024-11-22 12:05:06
   Last Change Time  : 2024-11-25 02:40:30
   ```
   
   Run the **display vrrp6 verbose** command on DeviceB. The command output shows that DeviceB's status is **Backup**.
   
   ```
   <DeviceB> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Backup
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : FE80::3A40:15FF:FE11:300
   Local IP        : FE80::3A40:15FF:FE21:300
   PriorityRun     : 100
   PriorityConfig  : 100
   MasterPriority  : 120
   Preempt         : YES   Delay Time : 0s   Remain : --
   Hold Multiplier : 3
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : normal-vrrp
   Backup-forward  : disabled
   Create Time       : 2024-11-22 12:05:49
   Last Change Time  : 2024-11-25 02:40:30
   ```
   
   Run the **shutdown** command on DeviceA's GE 0/2/0 to simulate a DeviceA fault.
   
   Run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA's status is **Initialize**.
   
   ```
   <DeviceA> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Initialize
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : ::
   Local IP        : FE80::3A40:15FF:FE11:300
   PriorityRun     : 120
   PriorityConfig  : 120
   MasterPriority  : 0
   Preempt         : YES   Delay Time : 20s   Remain : --
   Hold Multiplier : 3
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : normal-vrrp
   Backup-forward  : disabled
   Create Time       : 2024-11-22 12:05:06
   Last Change Time  : 2024-11-25 03:00:12
   ```
   
   Run the **display vrrp6 verbose** command on DeviceB. The command output shows that DeviceB's status is **Master**.
   
   ```
   <DeviceB> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Master
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : FE80::3A40:15FF:FE21:300
   Local IP        : FE80::3A40:15FF:FE21:300
   PriorityRun     : 100
   PriorityConfig  : 100
   MasterPriority  : 100
   Preempt         : YES   Delay Time : 0s   Remain : --
   Hold Multiplier : 3
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : normal-vrrp
   Backup-forward  : disabled
   Create Time       : 2024-11-22 12:05:49
   Last Change Time  : 2024-11-25 03:10:58
   ```
   
   Run the **undo shutdown** command on DeviceA's GE 0/2/0. After GE 0/1/0 goes up, wait 20s and run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA's status is **Master**.
   
   ```
   <DeviceA> display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Master
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : FE80::3A40:15FF:FE11:300
   Local IP        : FE80::3A40:15FF:FE11:300
   PriorityRun     : 120
   PriorityConfig  : 120
   MasterPriority  : 120
   Preempt         : YES   Delay Time : 20s   Remain : --
   Hold Multiplier : 3
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : normal-vrrp
   Backup-forward  : disabled
   Create Time       : 2024-11-22 12:05:06
   Last Change Time  : 2024-11-25 03:11:35
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
   vrrp6 vrid 1 virtual-ip fe80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
   vrrp6 vrid 1 priority 120
   vrrp6 vrid 1 preempt-mode timer delay 20
   vrrp6 recover-delay 20
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
   vrrp6 vrid 1 virtual-ip fe80::1 link-local
   vrrp6 vrid 1 virtual-ip 2001:DB8::100
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