Example for Configuring a VRRP Group on VLANIF Interfaces
=========================================================

In this example, user packets are sent to Device C that is dual-homed to Device A and Device B. The three devices form a ring network. A VRRP group is configured on VLANIF interfaces of these Devices to implement device backup. Broadcasting VRRP packets on the ring network causes broadcast storms. A ring network protocol needs to be configured to prevent this problem. In this example, the Multiple Spanning Tree Protocol (MSTP) is used.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E-M2K is used as an example.

On the network shown in [Figure 1](#EN-US_TASK_0000001163341708__en-us_task_0172361802_fig_dc_vrp_vrrp_cfg_013301), Device C is dual-homed to two directly connected devices Device A and Device B, forming a ring network.

Device A is the master device and periodically broadcasts VRRP packets through VLAN 10's member interfaces to inform Device B that Device A is working properly. VLAN 10's member interfaces include interface1 and Eth-Trunk1 members interface3 and interface2. The deployment causes broadcast storms on the ring network.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE 0/1/1, GE 0/1/2, GE 0/2/1, GE 0/2/2, and GE 0/1/5, respectively. To ensure link reliability, you are advised to deploy interface 2 and interface 3 on different boards.


A ring network protocol can be configured to break loops and prevent broadcast storms.

**Figure 1** Network diagram for a VRRP group on VLANIF interfaces  
![](images/fig_dc_vrp_vrrp_cfg_013301.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, MSTP is used. For information about other ring network protocols, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - LAN Access and MAN Access*.



#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface to ensure IP connectivity.
2. Configure MSTP on each device to break loops and prevent broadcast storms.
3. Configure a VRRP group and set VRRP priority values on Device A and Device B to implement device backup.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of VLANIF 10 (10.1.1.2) on Device A and that (10.1.1.3) on Device B
* Multiple Spanning Tree (MST) region name (RG1) and multiple spanning tree instance (MSTI) name (MSTI1) on each device
* VRID (1), virtual IP address (10.1.1.1), VRRP priority value (130) on Device A, and VRRP priority value (default value 100) on Device B

#### Procedure

1. Configure interface attributes on each device.
   
   
   * Create a VLAN and add interfaces to the VLAN on each device.
     
     # On Device C, create VLAN 10 and add GE 0/1/2 and GE 0/1/5 to VLAN 10.
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] sysname DeviceC
     ```
     ```
     [*HUAWEI] commit
     ```
     ```
     [~DeviceC] interface gigabitethernet 0/1/2
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/2] undo shutdown
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/2] portswitch
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/2] commit
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/2] quit
     ```
     ```
     [~DeviceC] interface gigabitethernet 0/1/5
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/5] undo shutdown
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/5] portswitch
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/5] commit
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/5] quit
     ```
     ```
     [~DeviceC] vlan 10
     ```
     ```
     [*DeviceC-vlan10] port gigabitethernet 0/1/2
     ```
     ```
     [*DeviceC-vlan10] port gigabitethernet 0/1/5
     ```
     ```
     [*DeviceC-vlan10] commit
     ```
     ```
     [~DeviceC-vlan10] quit
     ```
     
     # On Device A, create VLAN 10, add GE 0/1/1 to VLAN 10, configure VLANIF interface, and assign an IP address to the VLANIF interface.
     
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
     [~DeviceA-GigabitEthernet0/1/1] undo shutdown
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] portswitch
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] commit
     ```
     ```
     [~DeviceA-GigabitEthernet0/1/1] quit
     ```
     ```
     [~DeviceA] vlan 10
     ```
     ```
     [*DeviceA-vlan10] port gigabitethernet 0/1/1
     ```
     ```
     [*DeviceA-vlan10] commit
     ```
     ```
     [~DeviceA-vlan10] quit
     ```
     ```
     [~DeviceA] interface vlanif10
     ```
     ```
     [*DeviceA-vlanif10] ip address 10.1.1.2 255.255.255.0
     ```
     ```
     [*DeviceA-vlanif10] commit
     ```
     ```
     [~DeviceA-vlanif10] quit
     ```
     
     # On Device B, create VLAN 10, add GE 0/1/1 to VLAN 10, configure VLANIF interface, and assign an IP address to the VLANIF interface.
     
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
     [~DeviceB-GigabitEthernet0/1/1] undo shutdown
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/1] portswitch
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/1] commit
     ```
     ```
     [~DeviceB-GigabitEthernet0/1/1] quit
     ```
     ```
     [~DeviceB] vlan 10
     ```
     ```
     [*DeviceB-vlan10] port gigabitethernet 0/1/1
     ```
     ```
     [*DeviceB-vlan10] commit
     ```
     ```
     [~DeviceB-vlan10] quit
     ```
     ```
     [~DeviceB] interface vlanif10
     ```
     ```
     [*DeviceB-vlanif10] ip address 10.1.1.3 255.255.255.0
     ```
     ```
     [*DeviceB-vlanif10] commit
     ```
     ```
     [~DeviceB-vlanif10] quit
     ```
   * Configure an Eth-Trunk between Device A and Device B.
     
     # Configure Device A.
     
     ```
     [~DeviceA] interface eth-trunk 1
     ```
     ```
     [*DeviceA-Eth-Trunk1] commit
     ```
     ```
     [~DeviceA-Eth-Trunk1] quit
     ```
     ```
     [~DeviceA] interface gigabitethernet 0/2/1
     ```
     ```
     [~DeviceA-GigabitEthernet0/2/1] undo shutdown
     ```
     ```
     [*DeviceA-GigabitEthernet0/2/1] eth-trunk 1
     ```
     ```
     [*DeviceA-GigabitEthernet0/2/1] commit
     ```
     ```
     [~DeviceA-GigabitEthernet0/2/1] quit
     ```
     ```
     [~DeviceA] interface gigabitethernet 0/1/2
     ```
     ```
     [~DeviceA-GigabitEthernet0/1/2] undo shutdown
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2] eth-trunk 1
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2] commit
     ```
     ```
     [~DeviceA-GigabitEthernet0/1/2] quit
     ```
     ```
     [~DeviceA] interface eth-trunk 1
     ```
     ```
     [*DeviceA-Eth-Trunk1] portswitch
     ```
     ```
     [*DeviceA-Eth-Trunk1] port link-type trunk
     ```
     ```
     [*DeviceA-Eth-Trunk1] port trunk allow-pass vlan 10
     ```
     ```
     [*DeviceA-Eth-Trunk1] commit
     ```
     ```
     [~DeviceA-Eth-Trunk1] quit
     ```
     
     # Configure Device B.
     
     ```
     [~DeviceB] interface eth-trunk 1
     ```
     ```
     [*DeviceB-Eth-Trunk1] commit
     ```
     ```
     [~DeviceB-Eth-Trunk1] quit
     ```
     ```
     [~DeviceB] interface gigabitethernet 0/2/1
     ```
     ```
     [~DeviceB-GigabitEthernet0/2/1] undo shutdown
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/1] eth-trunk 1
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/1] commit
     ```
     ```
     [~DeviceB-GigabitEthernet0/2/1] quit
     ```
     ```
     [~DeviceB] interface gigabitethernet 0/1/2
     ```
     ```
     [~DeviceB-GigabitEthernet0/1/2] undo shutdown
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2] eth-trunk 1
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2] commit
     ```
     ```
     [~DeviceB-GigabitEthernet0/1/2] quit
     ```
     ```
     [~DeviceB] interface eth-trunk 1
     ```
     ```
     [*DeviceB-Eth-Trunk1] portswitch
     ```
     ```
     [*DeviceB-Eth-Trunk1] port link-type trunk
     ```
     ```
     [*DeviceB-Eth-Trunk1] port trunk allow-pass vlan 10
     ```
     ```
     [*DeviceB-Eth-Trunk1] commit
     ```
     ```
     [~DeviceB-Eth-Trunk1] quit
     ```
2. Configure MSTP on each device.
   
   
   * Configure an MSTI named MSTI1 in an MST region named RG1 on each device.
     
     # Configure Device C.
     
     ```
     [~DeviceC] stp region-configuration
     ```
     ```
     [~DeviceC-mst-region] region-name RG1
     ```
     ```
     [*DeviceC-mst-region] instance 1 vlan 10
     ```
     ```
     [*DeviceC-mst-region] commit
     ```
     ```
     [~DeviceC-mst-region] quit
     ```
     
     # Configure Device A.
     
     ```
     [~DeviceA] stp region-configuration
     ```
     ```
     [~DeviceA-mst-region] region-name RG1
     ```
     ```
     [*DeviceA-mst-region] instance 1 vlan 10
     ```
     ```
     [*DeviceA-mst-region] commit
     ```
     ```
     [~DeviceA-mst-region] quit
     ```
     
     # Configure Device B.
     
     ```
     [~DeviceB] stp region-configuration
     ```
     ```
     [~DeviceB-mst-region] region-name RG1
     ```
     ```
     [*DeviceB-mst-region] instance 1 vlan 10
     ```
     ```
     [*DeviceB-mst-region] commit
     ```
     ```
     [~DeviceB-mst-region] quit
     ```
   * Set a Spanning Tree Protocol (STP) priority value for Device A to allow Device A to function as MSTI1's root bridge in RG1.
     
     ```
     [~DeviceA] stp instance 1 priority 0
     ```
     ```
     [*DeviceA] commit
     ```
   * Enable MSTP on each device and interface.
     
     # Configure Device C.
     
     ```
     [~DeviceC] stp enable
     ```
     ```
     [*DeviceC] interface gigabitethernet 0/1/2
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/2] stp enable
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/2] commit
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/2] quit
     ```
     ```
     [~DeviceC] interface gigabitethernet 0/1/5
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/5] stp enable
     ```
     ```
     [*DeviceC-GigabitEthernet0/1/5] commit
     ```
     ```
     [~DeviceC-GigabitEthernet0/1/5] quit
     ```
     
     # Configure Device A.
     
     ```
     [~DeviceA] stp enable
     ```
     ```
     [*DeviceA] interface eth-trunk 1
     ```
     ```
     [*DeviceA-Eth-Trunk1] stp enable
     ```
     ```
     [*DeviceA-Eth-Trunk1] commit
     ```
     ```
     [~DeviceA-Eth-Trunk1] quit
     ```
     ```
     [~DeviceA] interface gigabitethernet 0/1/1
     ```
     ```
     [~DeviceA-GigabitEthernet0/1/1] stp enable
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] commit
     ```
     ```
     [~DeviceA-GigabitEthernet0/1/1] quit
     ```
     
     # Configure Device B.
     
     ```
     [~DeviceB] stp enable
     ```
     ```
     [*DeviceB] interface eth-trunk 1
     ```
     ```
     [*DeviceB-Eth-Trunk1] stp enable
     ```
     ```
     [*DeviceB-Eth-Trunk1] commit
     ```
     ```
     [~DeviceB-Eth-Trunk1] quit
     ```
     ```
     [*DeviceB] interface gigabitethernet 0/1/1
     ```
     ```
     [~DeviceB-GigabitEthernet0/1/1] stp enable
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/1] commit
     ```
     ```
     [~DeviceB-GigabitEthernet0/1/1] quit
     ```
   * Verify the MSTP configuration.
     
     # Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on Device C to view the role that GE 0/1/2 plays. GE 0/1/2 directly connecting Device C to Device A is a root interface in MSTI1 after Device A has been configured as the root bridge.
     
     ```
     [~DeviceC] display stp brief
     ```
     ```
      MSTID  Port                        Role  STP State     Protection
        0    GigabitEthernet0/1/2        ALTE  DISCARDING      NONE
        0    GigabitEthernet0/1/5        ROOT  FORWARDING      NONE
        1    GigabitEthernet0/1/2        ROOT  FORWARDING      NONE
        1    GigabitEthernet0/1/5        ALTE  DISCARDING      NONE    
     ```
     
     # Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on Device A to view the role that GE 0/1/1 and Eth-Trunk 1 play. GE 0/1/1 and Eth-Trunk 1 on Device A are designated interfaces in MSTI1 after Device A has been configured as the root bridge.
     
     ```
     [~DeviceA] display stp brief
     ```
     ```
      MSTID  Port                        Role  STP State     Protection
        0    Eth-Trunk1                  ROOT  FORWARDING      NONE
        0    GigabitEthernet0/1/1        DESI  FORWARDING      NONE
        1    Eth-Trunk1                  DESI  FORWARDING      NONE
        1    GigabitEthernet0/1/1        DESI  FORWARDING      NONE
     ```
     
     # Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on Device B to view the role that Eth-Trunk 1 plays. Eth-Trunk 1 on Device B is a root interface in MSTI1 after Device A has been configured as the root bridge.
     
     ```
     [~DeviceB] display stp brief
     ```
     ```
      MSTID  Port                        Role  STP State     Protection
        0    Eth-Trunk1                  DESI  FORWARDING      NONE
        0    GigabitEthernet0/1/1        DESI  FORWARDING      NONE
        1    Eth-Trunk1                  ROOT  FORWARDING      NONE
        1    GigabitEthernet0/1/1        DESI  FORWARDING      NONE
     ```
3. Configure VRRP on Device A and Device B.
   
   
   
   # On Device A, create VRRP group 1 and set a higher priority for Device A so that it becomes the master device.
   
   ```
   [~DeviceA] interface vlanif10
   ```
   ```
   [*DeviceA-vlanif10] vrrp vrid 1 virtual-ip 10.1.1.1
   ```
   ```
   [*DeviceA-vlanif10] vrrp vrid 1 priority 130
   ```
   ```
   [*DeviceA-vlanif10] commit
   ```
   ```
   [~DeviceA-vlanif10] quit
   ```
   
   # Configure Device B. The VRRP group uses the default priority 100.
   
   ```
   [~DeviceB] interface vlanif10
   ```
   ```
   [*DeviceB-vlanif10] vrrp vrid 1 virtual-ip 10.1.1.1
   ```
   ```
   [*DeviceB-vlanif10] commit
   ```
   ```
   [~DeviceB-vlanif10] quit
   ```
4. Verify the VRRP configuration.
   
   
   
   # After completing the configuration, run the [**display vrrp**](cmdqueryname=display+vrrp) command on each device to view information about the VRRP group. Device A is in the **Master** state and Device B is in the **Backup** state in VRRP group 1.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   Vlanif10 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.1
   Master IP      : 10.1.1.2
   Local IP       : 10.1.1.2
   PriorityRun    : 130
   PriorityConfig : 130
   MasterPriority : 130
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
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
   [~DeviceB] display vrrp
   ```
   ```
   Vlanif10 | Virtual Router 1
   State          : Backup
   Virtual IP     : 10.1.1.1
   Master IP      : 10.1.1.2
   Local IP       : 10.1.1.3
   PriorityRun    : 100
   PriorityConfig : 100
   MasterPriority : 130
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
   Create Time       : 2013-03-11 12:58:02
   Last Change Time  : 2013-03-11 12:58:07
   
   ```
   
   # Run the **shutdown** command on VLANIF 10 of Device A to simulate a link failure.
   
   ```
   [~DeviceA] interface vlanif10
   ```
   ```
   [*DeviceA-Vlanif10] shutdown
   ```
   ```
   [*DeviceA-Vlanif10] commit
   ```
   ```
   [~DeviceA-Vlanif10] quit
   ```
   
   # Run the **display vrrp** command on Device A. Device A's status has successfully changed to **Initialize** in VRRP group 1.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   Vlanif10 | Virtual Router 1
   State          : Initialize
   Virtual IP     : 10.1.1.1
   Master IP      : 0.0.0.0
   Local IP       : 10.1.1.2
   PriorityRun    : 130
   PriorityConfig : 130
   MasterPriority : 0
   Preempt        : YES   Delay Time : 0s
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config Type    : normal-vrrp
   Backup-forward    : disabled
   Create Time       : 2013-03-11 12:57:42
   Last Change Time  : 2013-03-11 13:05:31
   
   ```
   
   # Run the **display vrrp** command on Device B. Device B's status has successfully changed to **Master** in VRRP group 1.
   
   ```
   [~DeviceB] display vrrp
   ```
   ```
   Vlanif10 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.1
   Master IP      : 10.1.1.3
   Local IP       : 10.1.1.3
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
   Create Time       : 2013-03-11 12:58:02
   Last Change Time  : 2013-03-11 13:05:31
   
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.1
   vrrp vrid 1 priority 130
  #
  interface Eth-Trunk1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   portswitch
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
  #
  stp region-configuration
  region-name RG1
  instance 1 vlan 10
  #
  stp instance 1 priority 0
  stp enable
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.1.1.3 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.1
  #
  interface Eth-Trunk1
   portswitch
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   portswitch
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   eth-trunk 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   eth-trunk 1
  #
  stp enable
  #
  stp region-configuration
  region-name RG1
  instance 1 vlan 10
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   portswitch
   port default vlan 10
  #
  interface GigabitEthernet0/1/5
   undo shutdown
   portswitch
   port default vlan 10
  #
  stp region-configuration
  region-name RG1
  instance 1 vlan 10
  #
  stp enable
  # 
  return
  ```