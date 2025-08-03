Example for Configuring VRRP Groups to Work in Multi-gateway Load Balancing Mode
================================================================================

In this example, two VRRP groups are configured to work in multi-gateway load balancing mode. Devices in the VRRP groups back up each other and load-balance traffic.

#### Networking Requirements

VRRP groups working in master/backup mode can be configured on Routers to implement gateway redundancy. To reduce the traffic burden on the master Router, configure VRRP groups to work in multi-gateway load balancing mode to load-balance uplink traffic.

[Figure 1](#EN-US_TASK_0172361793__fig_dc_vrp_vrrp_cfg_012201) shows two VRRP groups working in load balancing mode. DeviceD is dual-homed to DeviceA and DeviceB. Users want some hosts to use DeviceA to forward data traffic and DeviceB to provide backup, and other hosts to use DeviceB to forward data traffic and DeviceA to provide backup. DeviceA and DeviceB functioning as master devices in different VRRP groups can back up each other and load-balance data traffic.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/1, GE 0/1/2, and GE 0/2/0, respectively.


**Figure 1** VRRP groups working in multi-gateway load balancing mode  
![](images/fig_dc_vrp_vrrp_cfg_012201.png)  


#### Precautions

The IP address of GE 0/2/0 on DeviceA and IP address of GE 0/2/0 on DeviceB must be configured on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on each Router and configure a routing protocol to ensure IP reachability.
2. Create two VRRP groups on gateway Routers. Device A is configured as the master device in VRRP group 1. Device B is configured as the master device in VRRP group 2. They can load-balance traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface on each device and Layer 2 transparent transmission on DeviceD
* VRID (1) and virtual IP address (10.1.1.111) for a VRRP group configured on DeviceA and DeviceB
* VRRP priorities: 120 for DeviceA (master); default value 100 for DeviceB (backup) in VRRP group 1
* VRID (2) and virtual IP address (10.1.1.112) for the other VRRP group configured on DeviceA and DeviceB
* VRRP priorities: 120 for DeviceB (master); default value 100 for DeviceA (backup) in VRRP group 2

#### Procedure

1. Assign an IP address to each interface on DeviceA, DeviceB, and DeviceC. Configure OSPF to ensure that these Routers can communicate with each other. For details about DeviceD configurations, see [Configuration Files](#EN-US_TASK_0172361793__example671715208214023) in this section.
   
   
   
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
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ip address 192.168.1.1 24
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
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
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
   [~DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/1/2
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ip address 192.168.2.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/2] quit
   ```
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
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
   
   # Configure DeviceC.
   
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
   [~DeviceC] interface gigabitethernet 0/1/1
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] ip address 192.168.1.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] ip address 192.168.2.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ip address 172.16.1.1 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceC-ospf-1] quit
   ```
2. Create VRRP groups.
   
   
   
   # Create VRRP groups 1 and 2 on DeviceA's GE 0/2/0. Set DeviceA's priority to 120 in VRRP group 1 so that it functions as the master, and use the default priority (100) for DeviceA in VRRP group 2 so that it functions as the backup.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] vrrp vrid 1 priority 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] vrrp vrid 2 virtual-ip 10.1.1.112
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Create VRRP groups 1 and 2 on DeviceB's GE 0/2/0. Use the default priority (100) for DeviceB in VRRP group 1 so that it functions as the backup, and set the priority to 120 for DeviceB in VRRP group 2 so that it functions as the master.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] vrrp vrid 1 virtual-ip 10.1.1.111
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] vrrp vrid 2 virtual-ip 10.1.1.112
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] vrrp vrid 2 priority 120
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] quit
   ```
3. Verify the configuration.
   
   
   
   Run the **display vrrp** command on DeviceA. The command output shows that DeviceA serves as the master device in VRRP group 1 and as a backup device in VRRP group 2.
   
   ```
   <DeviceA> display vrrp
   ```
   ```
   GigabitEthernet0/2/0 | Virtual Router 1
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
   Auth Type         : None
   Virtual MAC       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   
   GigabitEthernet0/2/0 | Virtual Router 2
   State             : Backup
   Virtual IP        : 10.1.1.112
   Master IP         : 10.1.1.2
   Local IP          : 10.1.1.1
   PriorityRun       : 100
   PriorityConfig    : 100
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : None
   Virtual MAC       : 00e0-fc12-7880
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
   
   Run the **display vrrp** command on DeviceB. The command output shows that DeviceB serves as a backup device in VRRP group 1 and as the master device in VRRP group 2.
   
   ```
   <DeviceB> display vrrp
   ```
   ```
   GigabitEthernet0/2/0 | Virtual Router 1
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
   Auth Type         : None
   Virtual MAC       : 0000-5e00-0102
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   
   GigabitEthernet0/2/0 | Virtual Router 2
   State             : Master
   Virtual IP        : 10.1.1.112
   Master IP         : 10.1.1.2
   Local IP          : 10.1.1.2
   PriorityRun       : 120
   PriorityConfig    : 120
   MasterPriority    : 120
   Preempt           : YES      Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : None
   Virtual MAC       : 00e0-fc12-7880
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
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
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
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
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
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
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.1.1.110 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   port default vlan 10
  #
  return
  ```