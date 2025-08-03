Example for Associating a VRRP Group with a VRRP-disabled Interface
===================================================================

In this example, a VRRP group is associated with a VRRP-disabled interface. If the interface fails, a master/backup switchover is performed.

#### Networking Requirements

The master device cannot detect changes in the status of interfaces that are not in a VRRP group. If a VRRP-disabled interface connected to a network fails, the master device cannot detect the fault and still forwards user packets through the failed interface, which results in service interruptions. To prevent this issue, associate the VRRP group with the VRRP-disabled interface. If the interface goes Down, the VRRP group detects the fault, reduces the priority of the master device, and sends VRRP Advertisement packets to elect a new master device.

On the network shown in [Figure 1](#EN-US_TASK_0172361811__fig_dc_vrp_vrrp_cfg_012501), Host A is connected to Host B by using a default gateway. A VRRP group is configured on Device A and Device B. Device A is the master device, and Device B is the backup device. Host A sends traffic to Host B along the path Host A -> Device A -> Device C -> Host B. If the link between Device A and Device C fails, traffic from Host A to Host B is discarded. To prevent the issue, associate the VRRP group with the interfaces connecting Device A to Device C and connecting Device B to Device C.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.



**Figure 1** Associating a VRRP group with interfaces  
![](images/fig_dc_vrp_vrrp_cfg_012501.png)  


#### Precautions

The IP address of GE 0/1/0 on Device A and IP address of GE 0/1/0 on Device B must be on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VRRP group 1 on GE 0/1/0 of Device A, and set a high VRRP priority for Device A so that Device A functions as the master device.
2. Configure VRRP group 1 on GE 0/1/0 of Device B, and retain the default VRRP priority for Device B so that Device B functions as the backup device.
3. Associate VRRP group 1 on Device A with GE 0/2/0 connected to Device C.

#### Data Preparation

To complete the configuration, you need the following data:

* Virtual IP address and ID of a VRRP group
* Priority of each device in a VRRP group

#### Procedure

1. Assign an IP address to each interface on Device A, Device B, and Device C. Configure OSPF to ensure that these routers can communicate with each other.
   
   
   
   # Configure Device A.
   
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
   [*DeviceA-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip address 192.168.1.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] ospf 1
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
   
   # Configure Device B.
   
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
   [*DeviceB-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ip address 192.168.2.1 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] ospf 1
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
   
   # Configure Device C.
   
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
   [~DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ip address 192.168.1.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ip address 192.168.2.2 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] undo shutdown
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] ip address 172.16.1.1 24
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] ospf 1
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
2. Configure a VRRP group.
   
   
   
   # Configure VRRP group 1 on Device A, and set the VRRP priority of Device A to 120 so that Device A functions as the master device.
   
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
   
   # Configure VRRP group 1 on Device B, and retain the default VRRP priority for Device B so that Device B functions as the backup device.
   
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
3. Associate the VRRP group with an interface.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 30
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display vrrp**](cmdqueryname=display+vrrp) command on Device A and Device B to view information about the interface tracked by the VRRP group and its status. The following example uses the command output on Device A.
   
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
   Preempt           : YES                     Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Track IF          : GigabitEthernet0/2/0            Priority Reduced :30
   IF State          : UP
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
   
   # Run the [**shutdown**](cmdqueryname=shutdown) command on GE 0/2/0 of Device A to simulate a link fault.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   Run the [**display vrrp**](cmdqueryname=display+vrrp) command on Device A. The command output shows that the VRRP status of Device A has become Backup.
   
   ```
   [~DeviceA] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Backup
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.2
   Local IP          : 10.1.1.1
   PriorityRun       : 90
   PriorityConfig    : 120
   MasterPriority    : 100
   Preempt           : YES                Delay Time : 0s
   Hold Multiplier   : 4
   TimerRun          : 1s
   TimerConfig       : 1s
   Auth Type         : NONE
   Virtual MAC       : 0000-5e00-0101
   Passive Mode      : NO
   Check TTL         : YES
   Config Type       : normal-vrrp
   Backup-forward    : disabled
   Track IF          : GigabitEthernet0/2/0            Priority Reduced :30
   IF State          : DOWN
   Create Time          : 2011-12-29 05:41:23
   Last Change Time     : 2011-12-29 05:41:33
   ```
   
   Run the [**display vrrp**](cmdqueryname=display+vrrp) command on Device B. The command output shows that the VRRP status of Device B has become Master.
   
   ```
   [~DeviceB] display vrrp
   ```
   ```
   GigabitEthernet0/1/0 | Virtual Router 1
   State             : Master
   Virtual IP        : 10.1.1.111
   Master IP         : 10.1.1.2
   Local IP          : 10.1.1.2
   PriorityRun       : 100
   PriorityConfig    : 100
   MasterPriority    : 100
   Preempt           : YES                     Delay Time : 0s
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

#### Configuration Files

* Device A configuration file
  
  ```
  # 
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
   vrrp vrid 1 track interface gigabitethernet 0/2/0 reduced 30
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* Device B configuration file
  
  ```
  # 
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* Device C configuration file
  
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
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
    network 172.16.1.0 0.0.0.255
  #
  return
  ```