Example for Configuring a Unicast VRRP Group
============================================

This section provides an example for configuring a unicast VRRP group to implement the master/backup status negotiation between two devices on a Layer 3 network.

#### Networking Requirements

On the Layer 3 network shown in [Figure 1](#EN-US_TASK_0172361829__fig_dc_vrp_vrrp_cfg_014301), the master device transmits data. If the master device fails, the backup device takes over traffic forwarding. After the original master device recovers, traffic switches back to it.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.

A unicast VRRP group is usually used in BRAS scenarios to determine the master and backup role of BRASs and can run without specifying a virtual IP address for the gateway.


**Figure 1** Configuring a unicast VRRP group

![](figure/en-us_image_0000001186428972.png)



#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."

#### Configuration Roadmap

The configuration roadmap is as follows:

* Assign an IP address to each interface on each device and configure a routing protocol to ensure IP reachability.
* Create a unicast VRRP group on DeviceA and DeviceB. Configure different priorities for DeviceA and DeviceB to ensure that DeviceA functions as the master device and DeviceB functions as the backup device.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each device, as shown in [Figure 1](#EN-US_TASK_0172361829__fig_dc_vrp_vrrp_cfg_014301)
* Unicast VRRP group ID on DeviceA and DeviceB: 1
* DeviceA's priority: 120 (master); DeviceB's priority: default value 100 (backup)
* DeviceA's preemption delay: 20 seconds

#### Procedure

1. Assign an IP address to each interface on each device and configure OSPF. The configuration on DeviceA is used as an example. For configuration details about other devices, see [Configuration Files](#EN-US_TASK_0172361829__example509284841214023) in this section.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface gigabitethernet0/1/0
   [~DeviceA-GigabitEthernet0/1/0] ip address 192.168.1.1 24
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface gigabitethernet0/2/0
   [*DeviceA-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*DeviceA-GigabitEthernet0/2/0] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
2. Configure a VRRP group.
   
   
   
   # Configure VRRP group 1 on DeviceA, configure a priority of 120 to ensure that DeviceA functions as the master device, and set the preemption delay to 20s.
   
   ```
   [~DeviceA] interface loopback1
   [~DeviceA-loopback1] vrrp vrid 1 peer-ip 10.3.1.1 source-ip 10.2.1.1 
   [*DeviceA-loopback1] vrrp vrid 1 priority 120
   [*DeviceA-loopback1] vrrp vrid 1 preempt-mode timer delay 20
   [*DeviceA-loopback1] quit
   [*DeviceA] commit
   ```
   
   # Configure VRRP group 1 on DeviceB, and use the default priority (100) to ensure it functions as the backup.
   
   ```
   [~DeviceB] interface loopback1
   [~DeviceB-loopback1] vrrp vrid 1 peer-ip 10.2.1.1 source-ip 10.3.1.1 
   [*DeviceB-loopback1] quit
   [*DeviceB] commit
   ```
3. Verify the configuration.
   
   
   
   # After completing the preceding configurations, run the **display vrrp** command on DeviceA and DeviceB. The command outputs on DeviceA and DeviceB show that the VRRP statuses of DeviceA and DeviceB are **Master** and **Backup**, respectively.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
    LoopBack1 | Virtual Router 1
     State           : Master
       Peer IP         : 10.3.1.1
       Source IP       : 10.2.1.1
       Master IP       : 10.2.1.1
       Local IP        : 10.2.1.1
       PriorityRun     : 120
       PriorityConfig  : 120
       MasterPriority  : 120
       Preempt         : YES   Delay Time : 20 s
       Hold Multiplier : 4
       TimerRun        : 10 s
       TimerConfig     : 10 s
       Auth type       : NONE
       Virtual MAC     : 0000-5e00-0101
       Passive Mode      : NO  
       Check TTL       : NO
       Config type     : unicast-vrrp
       Create Time     : 2016-06-24 09:05:43                                      
       Last Change Time: 2016-06-24 09:35:21
   ```
   ```
   [~DeviceB] display vrrp
   ```
   ```
    LoopBack1 | Virtual Router 1
     State           : Backup
       Peer IP         : 10.2.1.1
       Source IP       : 10.3.1.1
       Master IP       : 10.2.1.1
       Local IP        : 10.3.1.1
       PriorityRun     : 100
       PriorityConfig  : 100
       MasterPriority  : 120
       Preempt         : YES   Delay Time : 20 s
       Hold Multiplier : 4
       TimerRun        : 10 s
       TimerConfig     : 10 s
       Auth type       : NONE
       Virtual MAC     : 0000-5e00-0102
       Passive Mode      : NO
       Check TTL       : NO
       Config type     : unicast-vrrp
       Create Time     : 2016-06-24 09:05:43                                      
       Last Change Time: 2016-06-24 09:35:21
   ```
   * Verify that DeviceA can preempt the Master state after recovering.
     
     # Run the **shutdown** command on DeviceA's interface 1 to simulate a DeviceA fault.
     
     Run the **display vrrp** command on DeviceB. The command output shows that DeviceB's status is **Master**.
     ```
     [~DeviceB] display vrrp
     ```
     ```
      LoopBack1 | Virtual Router 1
       State              : Master
         Peer IP            : 10.2.1.1
         Source IP          : 10.3.1.1
         Master IP          : 10.3.1.1
         Local IP           : 10.3.1.1
         PriorityRun        : 100
         PriorityConfig     : 100
         MasterPriority     : 120
         Preempt            : YES   Delay Time : 0 s
         Hold Multiplier    : 4
         TimerRun           : 10 s
         TimerConfig        : 10 s
         Auth type          : NONE
         Virtual MAC        : 0000-5e00-0102
         Passive Mode      : NO  
         Check TTL          : NO
         Config type        : unicast-vrrp
         Create Time        : 2016-06-24 09:05:43                                      
         Last Change Time   : 2016-06-24 09:35:21
     ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #        
  sysname DeviceA  
  #
  interface GigabitEthernet0/1/0
    undo shutdown
    ip address 192.168.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
    undo shutdown
    ip address 10.1.1.1 255.255.255.0
  #
  interface LoopBack1
    ip address 10.2.1.1 255.255.255.255
    vrrp vrid 1 peer-ip 10.3.1.1 source-ip 10.2.1.1
    vrrp vrid 1 priority 120
    vrrp vrid 1 preempt-mode timer delay 20
  #
  ospf 1
   area 0
   network 10.2.1.1 0.0.0.0
   network 10.1.1.0 0.0.0.255
   network 192.168.1.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #        
  sysname DeviceB  
  # 
  interface GigabitEthernet0/1/0
    undo shutdown
    ip address 10.1.1.2 255.255.255.0
  # 
  interface GigabitEthernet0/2/0
    undo shutdown
    ip address 192.168.2.1 255.255.255.0
  #
  interface LoopBack1
    ip address 10.3.1.1 255.255.255.255
    vrrp vrid 1 peer-ip 10.2.1.1 source-ip 10.3.1.1
  #
  ospf 1
   area 0
   network 10.3.1.1 0.0.0.0
   network 192.168.2.0 0.0.0.255
  #
  return
  ```
* DeviceC configuration file
  ```
  #        
  sysname DeviceC  
  # 
  interface GigabitEthernet0/1/0
    undo shutdown
    ip address 192.168.1.2 255.255.255.0
  # 
  interface GigabitEthernet0/2/0
    undo shutdown
    ip address 192.168.2.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
    undo shutdown
    ip address 172.16.1.1 255.255.255.0
  #
  ospf 1
   area 0
   network 192.168.1.0 0.0.0.255
   network 192.168.2.0 0.0.0.255
  #
  return
  ```