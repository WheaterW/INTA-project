Example for Associating a VRRP Group with a Route
=================================================

In this example, a VRRP backup group is associated with the uplink route that is connected to a network. If the route is withdrawn or becomes inactive, the RM module notifies the VRRP backup group of the change. After receiving the notification, the VRRP backup group performs a master/backup VRRP switchover.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E-M2K is used as an example.

To improve device reliability, two user gateways work in master/backup mode and are connected to a Layer 3 network. VRRP is enabled on these gateways to determine their master/backup status.

If an uplink route to a network becomes unreachable, user hosts cannot detect the change and still uses the route to transmit traffic. As a result, service traffic loss occurs. Associating the VRRP backup group with the route can prevent service traffic loss. The VRRP backup group can be configured to track the uplink route to the network. If the route is withdrawn or becomes inactive, the route management (RM) module notifies the VRRP backup group of the change. After receiving the notification, the VRRP backup group changes its master device's VRRP priority and performs a master/backup switchover.

On the network shown in [Figure 1](#EN-US_TASK_0000001163341710__en-us_task_0172361823_fig_dc_vrp_vrrp_cfg_012801), PE1 and PE2 are two user gateways and form a VRRP backup group working in master/backup mode. On PE1 (master), associate VRRP with the route destined for PE3's interface. If PE3's interface goes Down, the RM module instructs the VRRP module to perform a master/backup VRRP switchover. After the interface goes Up, traffic switches back to Master.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.



**Figure 1** Associating a VRRP backup group with a route  
![](images/fig_dc_vrp_vrrp_cfg_012801.png)  


#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface to ensure link connectivity.
2. Configure a VRRP backup group on PE1 and PE2, and ensure that PE1 is the master and PE2 is the backup.
   
   If the link between PE1 and PE3 goes Down, the VRRP backup group performs a master/backup VRRP switchover and PE2 preempts the Master state.
3. Associate the VRRP backup group on PE1 with the route to PE3. The VRRP module monitors the route.
   
   If the associated route is withdrawn or becomes inactive, PE1 reduces its VRRP priority by 40 and triggers a master/backup VRRP switchover.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the interfaces on CE, PE1, PE2, and PE3 (For configuration details, see [Figure 1](#EN-US_TASK_0000001163341710__en-us_task_0172361823_fig_dc_vrp_vrrp_cfg_012801) or [Configuration Files](#EN-US_TASK_0000001163341710__en-us_task_0172361823_example1416641522214023) in this section.)
* Virtual IP address of the VRRP backup group: 10.1.1.10; preemption delay after the master device recovers: 20s
* Route to be associated with the VRRP backup group: 192.168.1.0/24

#### Procedure

1. Configure interface attributes of the CE, and assign IP addresses to the interfaces of PE1, PE2, and PE3.
   
   
   
   # Configure the CE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE] vlan 10
   ```
   ```
   [*CE-vlan10] port gigabitethernet 0/1/1
   ```
   ```
   [*CE-vlan10] port gigabitethernet 0/1/2
   ```
   ```
   [*CE-vlan10] quit
   ```
   ```
   [*CE] interface vlanif 10
   ```
   ```
   [*CE-Vlanif10] ip address 10.1.1.3 24
   ```
   ```
   [*CE] commit
   ```
   
   
   
   # Assign IP addresses to PE1's GE 0/1/1 and GE 0/1/2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] ip address 192.168.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Assign IP addresses to PE2's GE 0/1/1 and GE 0/1/2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] ip address 10.1.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] ip address 192.168.2.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   # Assign an IP address to PE3's GE 0/1/1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE3
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE3] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE3-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] ip address 192.168.1.2 24
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE3] commit
   ```
2. Configure basic functions of a VRRP backup group.
   
   
   
   # Configure a VRRP group with the VRID of 1 on PE1, and set the VRRP priority of PE1 to 120 so that PE1 functions as the master device.
   
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.10
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] vrrp vrid 1 priority 120
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] vrrp vrid 1 preempt-mode timer delay 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] vrrp recover-delay 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure a VRRP backup group with the VRID of 1 on PE2, and retain the default VRRP priority for PE2 so that PE2 functions as the backup device.
   
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] vrrp vrid 1 virtual-ip 10.1.1.10
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Run the [**display vrrp**](cmdqueryname=display+vrrp) command on PE1 and PE2. The command outputs show that the VRRP status of PE1 is **Master** and that the VRRP status of PE2 is **Backup**.
   
   ```
   [~PE1] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.1
   Local IP       : 10.1.1.1
   PriorityRun    : 120
   PriorityConfig : 120
   MasterPriority : 120
   Preempt        : YES   Delay Time : 20s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Create Time       : 2012-04-26 10:04:12
   Last Change Time  : 2012-04-26 10:05:32
   ```
   ```
   [~PE2] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 1
   State          : Backup
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.1
   Local IP       : 10.1.1.2
   PriorityRun    : 100
   PriorityConfig : 100
   MasterPriority : 120
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Create Time       : 2012-04-26 10:04:36
   Last Change Time  : 2012-04-26 10:09:46
   ```
3. Configure IS-IS.
   
   # Set the IS-IS entity name to 10.0000.0000.0001.00 and the IS-IS level to 1 on PE1.
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1] is-level level-1
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Set the IS-IS entity name to 10.0000.0000.0002.00 on PE3.
   ```
   [~PE3] isis 1
   ```
   ```
   [*PE3-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE3] commit
   ```
4. Associate the VRRP backup group with the route 192.168.1.0/24.
   
   
   
   # Associate the VRRP backup group on PE1 with the route 192.168.1.0/24, and set the value by which the VRRP priority of PE1 decreases to 40 when the route is withdrawn.
   
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] vrrp vrid 1 track ip route 192.168.1.0 255.255.255.0 reduced 40 
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
5. Verify the configuration.
   
   
   
   # Run the [**shutdown**](cmdqueryname=shutdown) command on GE 0/1/1 of PE3 to simulate a link fault.
   
   # Run the [**display vrrp**](cmdqueryname=display+vrrp) command on PE1 and PE2. The command outputs show that the VRRP status of PE2 is **Master** and the VRRP status of PE1 is **Backup**, indicating that the VRRP backup group has performed a master/backup VRRP switchover.
   
   ```
   [~PE1] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 1  
   State          : Backup
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.2
   Local IP       : 10.1.1.1
   PriorityRun    : 80
   PriorityConfig : 120
   MasterPriority : 100
   Preempt        : YES   Delay Time : 20s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Track IP Route    : 192.168.1.0/24   Priority Reduced : 40
   IP Route State    : Unreachable
   Create Time       : 2012-04-26 10:04:12
   Last Change Time  : 2012-04-26 10:23:37
   ```
   ```
   [~PE2] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.2
   Local IP       : 10.1.1.2
   PriorityRun    : 100
   PriorityConfig : 100
   MasterPriority : 100
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Create Time       : 2012-04-26 10:04:36
   Last Change Time  : 2012-04-26 10:23:37
   ```
   
   # Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on GE 0/1/1 of PE3. The command output shows that GE 0/1/1 goes Up. Wait 20s and run the [**display vrrp**](cmdqueryname=display+vrrp) command on PE1 and PE2. The command outputs show that the VRRP status of PE1 is **Master** and that the VRRP status of PE2 is **Backup**.
   
   ```
   [~PE1] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.1
   Local IP       : 10.1.1.1
   PriorityRun    : 120
   PriorityConfig : 120
   MasterPriority : 120
   Preempt        : YES   Delay Time : 20s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Track IP Route    : 192.168.1.0/24   Priority Reduced : 40
   IP Route State    : Reachable 
   Create Time       : 2012-04-26 10:04:12    
   Last Change Time  : 2012-04-26 10:25:22
   ```
   ```
   [~PE2] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 1
   State          : Backup
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.1
   Local IP       : 10.1.1.2
   PriorityRun    : 100
   PriorityConfig : 100
   MasterPriority : 120
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Create Time       : 2012-04-26 10:04:36
   Last Change Time  : 2012-04-26 10:25:22
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown 
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.10
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 20
   vrrp recover-delay 20
   vrrp vrid 1 track ip route 192.168.1.0 255.255.255.0 reduced 40
   isis enable 1
  #
  interface GigabitEthernet0/1/2
   undo shutdown 
   ip address 192.168.1.1 255.255.255.0
   isis enable 1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  isis 1
   is-level level-1
   network-entity 20.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown 
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.10
  #
  interface GigabitEthernet0/1/2
   undo shutdown 
   ip address 192.168.2.1 255.255.255.0
  #
  return 
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown 
   ip address 192.168.1.2 255.255.255.0
   isis enable 1
  #
  return 
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  vlan batch 10
  #
  vlan 10
   port gigabitethernet 0/1/1
   port gigabitethernet 0/1/2
  #
  interface Vlanif10
   ip address 10.1.1.3 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
  #
  return
  ```