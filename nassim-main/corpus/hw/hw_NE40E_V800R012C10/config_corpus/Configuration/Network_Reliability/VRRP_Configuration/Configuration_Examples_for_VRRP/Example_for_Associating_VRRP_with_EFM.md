Example for Associating VRRP with EFM
=====================================

In this example, Virtual Router Redundancy Protocol (VRRP) is associated with Ethernet in the First Mile (EFM).

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E-M2K is used as an example.

On the network shown in [Figure 1](#EN-US_TASK_0000001208740175__en-us_task_0172361820_fig_dc_vrp_vrrp_cfg_013801), DeviceC is dual-homed to DeviceA and DeviceB. A VRRP group is deployed on both DeviceA and DeviceB to improve link reliability.

If a link fails, negotiating the VRRP status takes a certain period of time. To speed up link switchovers, enable Bidirectional Forwarding Detection (BFD) to monitor links and configure a VRRP group to monitor a BFD session. If an interface or link on the master device fails, BFD rapidly detects the fault and notifies the VRRP group. A backup device then preempts the Master state and takes over. However, this method does not apply to some networks or devices that do not support BFD. If a device does not support BFD but supports EFM, you can use EFM to implement rapid switchovers.

On the network shown in [Figure 1](#EN-US_TASK_0000001208740175__en-us_task_0172361820_fig_dc_vrp_vrrp_cfg_013801), DeviceC does not support BFD. Therefore, EFM is used to monitor the link between RouterA and DeviceC, and peer BFD is used to monitor the link between DeviceA and DeviceB. Associate VRRP with EFM and peer BFD to implement a rapid master/backup VRRP switchover based on the status of EFM and peer BFD sessions.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.



**Figure 1** VRRP association with EFM  
![](images/fig_dc_vrp_vrrp_cfg_013801.png)  


#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface and configure a routing protocol.
2. Create a VRRP group on the GE interfaces of DeviceA and DeviceB, and configure DeviceA as the master device and DeviceB as the backup device.
3. Enable peer BFD on DeviceA and DeviceB to monitor the link between them.
4. Enable EFM on DeviceA and DeviceB globally and on their GE interfaces.
5. Associate VRRP with peer BFD on DeviceB.
6. Associate VRRP with EFM on DeviceA.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* This example provides only the configurations for DeviceA and DeviceB.
* To associate VRRP with EFM and peer BFD, perform the following operations:
  + Associate VRRP with EFM on the master device. When an EFM session enters the Discovery state, the master device's VRRP status becomes Initialize.
  + Associate VRRP with peer BFD on a backup device. When a peer BFD session goes Down, the backup device increases its own VRRP priority and preempts the Master state.



#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on DeviceA and DeviceB (For details, see [Configuration Files](#EN-US_TASK_0000001208740175__en-us_task_0172361820_section_05) in this section.)
* VRRP group ID: 10; virtual IP address: 10.1.1.111; DeviceA's VRRP priority: 160; DeviceB's VRRP priority: 140; DeviceB's VRRP priority increased by: 40
* Interval at which errored frames are checked on GE 0/1/1: 5 seconds; interval at which errored frame seconds are checked on GE 0/1/1: 120 seconds
* Local and remote discriminators of a peer BFD session

#### Procedure

1. Assign IP addresses to DeviceA's and DeviceB's interfaces and configure Open Shortest Path First (OSPF) on DeviceA and DeviceB. For detailed DeviceC configuration, see Configuration Files in this section.
   
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
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceA-ospf-1] quit
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
   [~DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceA-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
2. Create a VRRP group and configure basic VRRP functions.
   
   
   
   # Create VRRP group 10 on DeviceA and set its VRRP priority to 160.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] vrrp vrid 10 virtual-ip 10.1.1.111
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] vrrp vrid 10 priority 160
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Create VRRP group 10 on DeviceB and set its VRRP priority to 140.
   
   ```
   [~DeviceB] interface gigabitethernet0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] vrrp vrid 10 virtual-ip 10.1.1.111
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] vrrp vrid 10 priority 140
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
3. Configure basic BFD functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] commit
   ```
   ```
   [~DeviceA-bfd] quit
   ```
   ```
   [~DeviceA] bfd atob bind peer-ip 10.1.1.2 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-atob] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-atob] commit
   ```
   ```
   [~DeviceA-bfd-session-atob] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] commit
   ```
   ```
   [~DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd btoa bind peer-ip 10.1.1.1 interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-btoa] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-btoa] commit
   ```
   ```
   [~DeviceB-bfd-session-btoa] quit
   ```
   
   After the configuration is complete, run the **display bfd session** command on DeviceA or DeviceB. The command output shows that a peer BFD session has been created. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   1     2      10.1.1.2        Up        S_IP_IF     GigabitEthernet0/1/1
   --------------------------------------------------------------------------------
        Total UP/DOWN Session Number : 1/0   
   ```
4. Configure EFM.
   
   
   
   # Enable EFM on DeviceA globally and on its GE 0/1/1, and set the intervals at which errored frames and errored frame seconds are checked on the interface to 5 seconds and 120 seconds, respectively.
   
   ```
   [~DeviceA] efm enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] efm enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] efm error-frame period 5
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] efm error-frame threshold 5
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] efm error-frame notification enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] efm error-frame-second period 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Enable EFM on DeviceB globally and on its GE 0/1/1, and set the intervals at which errored frames and errored frame seconds are checked on the interface to 5 seconds and 120 seconds, respectively.
   
   ```
   [~DeviceB] efm enable
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] efm enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] efm error-frame period 5
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] efm error-frame threshold 5
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] efm error-frame notification enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] efm error-frame-second period 120
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   
   After the configuration is complete, run the [**display efm session all**](cmdqueryname=display+efm+session+all) command on DeviceA or DeviceB. The command output shows that an EFM session has been created. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display efm session all
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/1/1      detect                      --                      
   ```
5. Associate VRRP with peer BFD.
   
   
   
   # Associate VRRP with peer BFD on DeviceB, and configure DeviceB to increase its own VRRP priority by 40 if the peer BFD session goes Down.
   
   ```
   [~DeviceB-GigabitEthernet0/1/1] vrrp vrid 10 track bfd-session 2 increased 40
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
   
   After the configuration is complete, run the **display vrrp** command on DeviceA and DeviceB. The command output on DeviceA shows that DeviceA is the master device. The command output on DeviceB shows that DeviceB is the backup device and that VRRP is associated with peer BFD.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 10
   State          : Master
   Virtual IP     : 10.1.1.111
   Master IP      : 10.1.1.1
   Local IP       : 10.1.1.1
   PriorityRun    : 160
   PriorityConfig : 160
   MasterPriority : 160
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1
   TimerConfig    : 1
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Create Time       : 2013-03-11 12:57:42
   Last Change Time  : 2013-03-11 12:57:47
   ```
   ```
   [~DeviceB]display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 10
   State          : Backup
   Virtual IP     : 10.1.1.111
   Master IP      : 10.1.1.1
   Local IP       : 10.1.1.2
   PriorityRun    : 140
   PriorityConfig : 140
   MasterPriority : 160
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1
   TimerConfig    : 1
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Track BFD      : 2  Priority increased : 40
   BFD-Session State : UP
   Create Time       : 2013-03-11 12:58:02
   Last Change Time  : 2013-03-11 12:58:07
   ```
6. Associate VRRP with EFM.
   
   
   
   # Associate VRRP with EFM on DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] vrrp vrid 10 track efm interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
7. Verify the configuration.
   
   
   
   # Run the **shutdown** command on DeviceA's GE 0/1/1 to simulate a link fault.
   
   ```
   [*DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Run the **display vrrp** command on DeviceA. The command output shows that DeviceA's VRRP status is **Initialize**.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 10
   State          : Initialize
   Virtual IP     : 10.1.1.111
   Master IP      : 0.0.0.0
   Local IP       : 10.1.1.1
   PriorityRun    : 160
   PriorityConfig : 160
   MasterPriority : 0
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1
   TimerConfig    : 1
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Track EFM      : GigabitEthernet0/1/1
   EFM state      : DOWN
   Create Time       : 2013-03-11 12:57:42
   Last Change Time  : 2013-03-11 12:57:47
   ```
   
   # Run the **display vrrp** command on DeviceB. The command output shows that DeviceB's VRRP status is **Master**.
   
   ```
   [~DeviceB] display vrrp
   ```
   ```
   GigabitEthernet0/1/1 | Virtual Router 10
   State          : Master
   Virtual IP     : 10.1.1.111
   Master IP      : 10.1.1.2
   Local IP       : 10.1.1.2
   PriorityRun    : 180
   PriorityConfig : 140
   MasterPriority : 180
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1
   TimerConfig    : 1
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Track BFD      : 2  Priority increased : 40
   BFD-Session State : Down
   Create Time       : 2013-03-11 12:58:02
   Last Change Time  : 2013-03-11 12:58:07
   ```
   
   # Run the **display efm session all** command on DeviceA. The command output shows that the status of the EFM session is **discovery**.
   
   ```
   [~DeviceA] display efm session all
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/1/0      discovery                   --
   
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  efm enable
  #
  bfd
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 10 virtual-ip 10.1.1.111
   vrrp vrid 10 priority 160
   vrrp vrid 10 track efm interface GigabitEthernet0/1/1
   efm enable
   efm error-frame period 5
   efm error-frame threshold 5
   efm error-frame notification enable
   efm error-frame-second period 120 
  #
  bfd atob bind peer-ip 10.1.1.2 interface gigabitethernet0/1/1
   discriminator local 1
   discriminator remote 2
   #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  efm enable
  #
  bfd
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 10 virtual-ip 10.1.1.111
   vrrp vrid 10 priority 140
   vrrp vrid 10 track bfd-session 2 increased 40
   efm enable
   efm error-frame period 5
   efm error-frame threshold 5
   efm error-frame notification enable
   efm error-frame-second period 120  
  #
  bfd btoa bind peer-ip 10.1.1.1 interface gigabitethernet0/1/1
   discriminator local 2
   discriminator remote 1
   #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
   sysname DeviceC
  #
   vlan batch 10
  #
  efm enable
  #
  interface Vlanif10
   ip address 10.1.1.3 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port default vlan 10
   efm enable
   efm error-frame period 5
   efm error-frame threshold 5
   efm error-frame notification enable
   efm error-frame-second period 120  
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port default vlan 10
   efm enable
   efm error-frame period 5
   efm error-frame threshold 5
   efm error-frame notification enable
   efm error-frame-second period 120
  #
  return
  ```