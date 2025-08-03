Example for Configuring VRRP6 Association
=========================================

In this example, a VRRP6 group is associated with a VRRP6-disabled interface or a BFD session. If the interface or the link monitored by BFD goes down, a master/backup VRRP6 switchover is performed.

#### Networking Requirements

Hosts are connected to a network through gateway Routers. To improve network reliability, configure a VRRP6 group on the gateway Routers to implement gateway redundancy. To further improve network reliability and implement a rapid master/backup VRRP6 switchover, configure VRRP6 association.

On the network shown in [Figure 1](#EN-US_TASK_0172361882__fig_dc_vrp_vrrp6_cfg_011701), the master Router forwards traffic in normal circumstances. If the BFD-monitored active link on the master Router or a VRRP6-disabled interface fails, associate the VRRP6 group with the BFD session or VRRP6-disabled interface to implement a rapid master/backup VRRP6 switchover. After the master Router recovers, traffic is switched back to it.![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/4, respectively.



**Figure 1** VRRP6 association  
![](images/fig_dc_vrp_vrrp6_cfg_011701.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on the devices and configure OSPFv3 to ensure IPv6 connectivity.
2. Create a VRRP6 group on gateway Routers and configure different priorities for the Routers to determine the master or backup role.
3. Configure a BFD session on DeviceA and DeviceB to monitor the link DeviceA -> DeviceD -> DeviceB.
4. Associate the VRRP6 group with the BFD session on DeviceB (backup). If the BFD session goes down, the VRRP6 group immediately performs a master/backup VRRP6 switchover.
5. Associate the VRRP6 group with a VRRP6-disabled interface on DeviceA. If the VRRP6-disabled interface goes down, the VRRP6 group immediately performs a master/backup VRRP6 switchover.


#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on each device (for configuration details, see [Configuration Files](#EN-US_TASK_0172361882__section_05) in this section)
* ID of a VRRP6 group: 1; virtual IPv6 address: 2001:db8::100
* DeviceA's priority: 120; DeviceB's priority: 100
* Local and remote discriminators of BFD sessions
* Priority by which DeviceB increases if the BFD session goes down: 40
* Priority by which DeviceA decreases if the VRRP6-disabled interface goes down: 40
* DeviceA's preemption delay: 20 seconds


#### Procedure

1. Configure OSPFv3 on DeviceA, DeviceB, and DeviceC to ensure that they can communicate with each other. For configuration details, see [Configuration Files](#EN-US_TASK_0172361882__section_05) in this section.
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
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:DB8::1/64
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
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
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
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:DB8::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip fe80::1 link-local
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 virtual-ip 2001:db8::100
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure basic BFD functions.
   
   
   
   # Configure a BFD session on DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [~DeviceA-bfd] quit
   ```
   ```
   [~DeviceA] bfd atob bind peer-ipv6 2001:db8::2 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-atob] min-rx-interval 50
   ```
   ```
   [*DeviceA-bfd-session-atob] min-tx-interval 50 
   ```
   ```
   [*DeviceA-bfd-session-atob] commit
   ```
   ```
   [~DeviceA-bfd-session-atob] quit
   ```
   
   # Configure a BFD session on DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [~DeviceB-bfd] quit
   ```
   ```
   [~DeviceB] bfd btoa bind peer-ipv6 2001:db8::1 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-btoa] min-rx-interval 50
   ```
   ```
   [*DeviceB-bfd-session-btoa] min-tx-interval 50
   ```
   ```
   [*DeviceB-bfd-session-btoa] commit
   ```
   ```
   [~DeviceB-bfd-session-btoa] quit
   ```
   
   After completing the configurations, run the **display bfd session all** command on DeviceA or DeviceB. The command output shows that the BFD session is **Up**. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all
   ```
   ```
   S: Static session
   D: Dynamic session
   IP: IP session
   IF: Single-hop session
   PEER: Multi-hop session
   AUTO: Automatically negotiated session
   (w): State in WTR 
   (*): State is invalid
   Total UP/DOWN Session Number : 1/0
   --------------------------------------------------------------------------------
   Local Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   1     2      2001:DB8::2     Up        S_IP_IF     GigabitEthernet0/1/0
   --------------------------------------------------------------------------------   
   ```
4. Configure VRRP6 association.
   
   
   
   # Associate the VRRP6 group with the VRRP6-disabled interface on DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp6 vrid 1 track interface gigabitethernet 0/2/0 reduced 40
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Associate the VRRP6 group with the BFD session on DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp6 vrid 1 track bfd-session 2 increased 40
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
5. Verify the configuration.
   
   
   
   After completing the configurations, ping HostB from HostA. The ping is successful. Run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA's status is **Master** and GE 0/2/0 has been associated.
   
   ```
   [*DeviceA] display vrrp6 interface gigabitethernet0/1/0 verbose
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
   Preempt         : YES   Delay Time : 20s   Remain : --
   Hold Multiplier : 4
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : Normal
   Track IF          : GigabitEthernet0/2/0             Priority Reduced : 40
   IF State          : UP
   Create Time       : 2013-07-27 17:33:00
   Last Change Time  : 2013-07-27 17:33:04
   ```
   
   Run the **display vrrp6 verbose** command on DeviceB. The command output shows that DeviceB's status is **Backup** and the BFD session has been associated.
   
   ```
   [*DeviceB] display vrrp6 interface gigabitethernet0/1/0 verbose
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
   Track BFD         : btoa                 Priority Increased : 40
   BFD-Session State : UP
   Create Time       : 2013-07-27 17:33:00
   Last Change Time  : 2013-07-27 17:33:04
   ```
   
   Run the **shutdown** command on DeviceA's GE 0/2/0 to simulate a DeviceA fault.
   
   Run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA's status is **Backup**.
   
   ```
   [*DeviceA] display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Backup
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : 2001:DB8::2
   Local IP        : 2001:DB8::1 
   PriorityRun     : 80
   PriorityConfig  : 120
   MasterPriority  : 100
   Preempt         : YES   Delay Time : 20s   Remain : --
   Hold Multiplier : 4
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : Normal
   Track IF          : GigabitEthernet0/2/0             Priority Reduced : 40
   IF State          : DOWN
   Create Time       : 2013-07-27 17:33:00
   Last Change Time  : 2013-07-27 17:35:14
   ```
   
   Run the **display vrrp6 verbose** command on DeviceB. The command output shows that DeviceB's status is **Master**.
   
   ```
   [*DeviceB] display vrrp6 interface gigabitethernet0/1/0 verbose
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State           : Master
   Virtual IP      : FE80::1
                     2001:DB8::100
   Master IP       : 2001:DB8::2
   Local IP        : 2001:DB8::2
   PriorityRun     : 100
   PriorityConfig  : 100
   MasterPriority  : 100
   Preempt         : YES   Delay Time : 0s   Remain : --
   Hold Multiplier : 4
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0202
   Check hop limit : YES
   Config Type     : Normal
   Track BFD         : btoa                 Priority Increased : 40
   BFD-Session State : UP
   Create Time       : 2013-07-27 17:33:00
   Last Change Time  : 2013-07-27 17:33:04
   ```
   
   Run the **undo shutdown** command on DeviceA's GE 0/2/0. After GE 0/2/0 goes up, wait 20s and run the **display vrrp6 verbose** command on DeviceA. The command output shows that DeviceA's status is **Master**.
   
   ```
   [*DeviceA] display vrrp6 interface gigabitethernet0/1/0 verbose
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
   Preempt         : YES   Delay Time : 20s   Remain : --
   Hold Multiplier : 4
   TimerRun        : 100cs
   TimerConfig     : 100cs
   Virtual MAC     : 0000-5e00-0201
   Check hop limit : YES
   Config Type     : Normal
   Track IF          : GigabitEthernet0/2/0             Priority Reduced : 40
   IF State          : UP
   Create Time       : 2013-07-27 17:33:00
   Last Change Time  : 2013-07-27 17:40:04
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
   bfd
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
   vrrp6 vrid 1 preempt-mode timer delay 20
   vrrp6 recover-delay 20
   vrrp6 vrid 1 track interface gigabitethernet 0/2/0 reduced 40
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  bfd atob bind peer-ipv6 2001:DB8::2 interface gigabitethernet 0/1/0
   discriminator local 1
   discriminator remote 2
   min-tx-interval 50
   min-rx-interval 50
   commit
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  bfd
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
   vrrp6 vrid 1 track bfd-session 2 increased 40
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  bfd btoa bind peer-ipv6 2001:DB8::1 interface gigabitethernet 0/1/0
   discriminator local 2
   discriminator remote 1
   min-tx-interval 50
   min-rx-interval 50
   commit
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
   commit
  #
  return
  ```