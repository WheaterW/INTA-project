Example for Associating a VRRP Group with a BFD Session
=======================================================

In this example, a VRRP group is associated with a BFD session. If the interface on which the VRRP status is Master or the link monitored by BFD goes Down, a backup device in the VRRP group preempts the Master state and takes over.

#### Networking Requirements

To improve link reliability, a user gateway is dual-homed to an upper-layer network and VRRP is configured to determine the active/standby status of dual-homing links and perform active/standby link switchovers if a fault occurs on the active link.

If a link fails, negotiating the VRRP status takes a certain period of time. To speed up link switchovers, enable BFD to monitor links and associate VRRP with BFD. If an interface or a link fails on the master device in the VRRP group, BFD rapidly detects the fault and notifies the VRRP group of the fault. After receiving the notification, the VRRP group performs a master/backup VRRP switchover. The backup device enters the Master state.

On the network shown in [Figure 1](#EN-US_TASK_0172361814__fig_dc_vrp_vrrp_cfg_012601), DeviceA, DeviceB, DeviceC, DeviceD, and a universal media gateway (UMG) form a simple next generation network (NGN) functioning as a bearer network.

The networking is as follows:

* The UMG is dual-homed to DeviceA and DeviceB through DeviceC and DeviceD, respectively.
* A VRRP group is configured on DeviceA and DeviceB. DeviceA is the master device, and DeviceB is the backup device.

If DeviceA fails or the GE link between DeviceA and DeviceB fails, the VRRP group is required to perform a master/backup switchover within 1 second, implementing rapid route convergence on the bearer network. To meet this requirement, associate the VRRP group with a BFD session.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.



**Figure 1** Associating a VRRP group with a BFD session  
![](images/fig_dc_vrp_vrrp_cfg_012601.png)  


#### Precautions

The IP address of GE 0/1/0 on DeviceA and IP address of GE 0/1/0 on DeviceB must be on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session on DeviceA and DeviceB to monitor DeviceA, DeviceB, the link from DeviceA to DeviceC, and the link from DeviceB to DeviceD.
2. Configure a VRRP group on GE 0/1/0 of DeviceA and GE 0/1/0 of DeviceB. DeviceA is the master device, and DeviceB is the backup device.
3. Associate the VRRP group on DeviceB (backup) with the BFD session. If the BFD session goes Down, the VRRP group immediately performs a master/backup switchover.

#### Data Preparation

To complete the configuration, you need the following data:

* Local and remote discriminators of BFD sessions
* Virtual IP address and ID of a VRRP group
* Priority of each device in a VRRP group

#### Procedure

1. Configure a BFD session.
   
   
   
   # Configure DeviceA.
   
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
   [~DeviceA] bfd
   ```
   ```
   [~DeviceA-bfd] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] bfd trackbfd bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-bfd-session-trackbfd] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-trackbfd] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-trackbfd] commit
   ```
   ```
   [~DeviceA-bfd-session-trackbfd] quit
   ```
   
   # Configure DeviceB.
   
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
   [~DeviceB] bfd
   ```
   ```
   [~DeviceB-bfd] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] bfd trackbfd bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-bfd-session-trackbfd] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-trackbfd] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-trackbfd] commit
   ```
   ```
   [~DeviceB-bfd-session-trackbfd] quit
   ```
   
   After completing the configurations, run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command on DeviceA or DeviceB. The command output shows that a BFD session has been established and its status is Up. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
   Local Remote PeerIpAddr      State     Type        InterfaceName
   ------------------------------------------------------------------------------
   1     2      10.1.1.2        Up        S_IP_IF     GigabitEthernet0/1/0
   ------------------------------------------------------------------------------
        Total UP/DOWN Session Number : 1/0
   ```
2. Configure VRRP group 1.
   
   
   
   # Configure VRRP group 1 on DeviceA, and set the VRRP priority of DeviceA to 120 so that DeviceA functions as the master device.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 priority 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure VRRP group 1 on DeviceB, and retain the default VRRP priority for DeviceB so that DeviceB functions as the backup device.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   After completing the configurations, run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceA and DeviceB. The command outputs show that the VRRP status of DeviceA is Master and that the VRRP status of DeviceB is Backup.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Master
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.1
   Local IP          : 10.1.1.1
   PriorityRun       : 120
   PriorityConfig    : 120
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
   ```
   [~DeviceB] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Backup
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.1
   Local IP          : 10.1.1.2
   PriorityRun       : 100
   PriorityConfig    : 100
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
3. Associate the VRRP group with the BFD session on DeviceB.
   
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] vrrp vrid 1 track bfd-session 2 increased 40
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   After completing the configurations, run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceB to view the associated BFD session and its status.
   
   ```
   [~DeviceB] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Backup
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.1
   Local IP          : 10.1.1.2
   PriorityRun       : 100
   PriorityConfig    : 100
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Track BFD         : 2                     Priority Increased : 40
   BFD-Session State : UP
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
4. Verify the configuration.
   
   
   
   # Run the [**shutdown**](cmdqueryname=shutdown) command on GE 0/1/0 of DeviceA to simulate a link fault.
   
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   Run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceA. The command output shows that the VRRP status of DeviceA has become Initialize.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Initialize
   Virtual IP        : 10.1.1.111
   Master IP         : 0.0.0.0
   Local IP          : 10.1.1.1
   PriorityRun       : 0
   PriorityConfig    : 120
   MasterPriority    : 0   
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
   
   Run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceB. The command output shows that the VRRP status of DeviceB has become Master.
   
   ```
   [~DeviceB] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Master
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.2
   Local IP          : 10.1.1.2
   PriorityRun       : 140
   PriorityConfig    : 100
   MasterPriority    : 140
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Track BFD         : 2              Priority Increased :40
   BFD-Session State : DOWN
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
  #
  bfd trackbfd bind peer-ip 10.1.1.2 interface gigabitethernet0/1/0
   discriminator local 1
   discriminator remote 2
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 track bfd-session 2 increased 40
  #
  bfd trackbfd bind peer-ip 10.1.1.1 interface gigabitethernet0/1/0
   discriminator local 2
   discriminator remote 1
  return
  ```