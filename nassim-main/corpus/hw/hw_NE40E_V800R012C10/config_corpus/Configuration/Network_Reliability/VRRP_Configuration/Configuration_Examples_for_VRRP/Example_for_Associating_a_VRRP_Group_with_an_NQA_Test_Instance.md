Example for Associating a VRRP Group with an NQA Test Instance
==============================================================

In this example, a VRRP group is associated with an NQA test instance. When NQA detects that a cross-device uplink goes Down, it instructs the VRRP group to perform a master/backup switchover.

#### Networking Requirements

VRRP can detect an uplink VRRP-disabled interface fault on a VRRP-enabled Router. However, if Device C's Interface2 shown in [Figure 1](dc_vrp_vrrp_cfg_0140.html#EN-US_TASK_0172361779__fig_dc_vrp_vrrp_cfg_014001) goes Down and its IP address is unreachable, VRRP cannot detect the fault. As a result, user traffic is lost.

The NE40E supports NQA. NQA uses a test instance to send probe packets to check destination IP address reachability.

You can associate VRRP with an NQA test instance to track the master device's uplink (cross-device). If the uplink fails and hosts on the LAN cannot access the external network through the master Router, NQA instructs VRRP to reduce the master Router's priority by a specified value. In this way, another Router in the group has a higher priority, becomes the master, and takes over services, ensuring communication continuity between hosts on a LAN and an external network. After the uplink recovers, NQA instructs VRRP to restore the Router's priority.

As shown in [Figure 1](#EN-US_TASK_0172361826__fig_dc_vrp_vrrp_cfg_014101), a VRRP group is configured on DeviceA and DeviceB, and the IP address of DeviceC's uplink interface is 10.2.1.1. Associate the VRRP group with an NQA test instance with a destination IP address of 10.2.1.1 on DeviceA so that the VRRP group can perform a master/backup VRRP switchover based on the status change in DeviceC's uplink interface. When the uplink interface goes Up, traffic is switched back to the Master device. ![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.



**Figure 1** Associating a VRRP group with an NQA test instance  
![](images/fig_dc_vrp_vrrp_cfg_014101.png)  


#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see "Example for Configuring a VRRP Group."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface and configure a routing protocol to ensure link connectivity.
2. Create a VRRP group on DeviceA and DeviceB, and ensure that DeviceA is the master and DeviceB is the backup.
3. Create an NQA test instance with a destination IP address of 10.2.1.1 (IP address of DeviceC's uplink interface) on DeviceA.
4. Associate the VRRP group with the NQA test instance on DeviceA.


#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses of the DeviceE, DeviceA, DeviceB, and DeviceC (For details, see [Figure 1](#EN-US_TASK_0172361826__fig_dc_vrp_vrrp_cfg_014101).)
* ID of the VRRP group created on DeviceA and DeviceB: 1; virtual IP address: 10.1.1.10
* DeviceA's priority: 120; DeviceB's priority: 100; DeviceB's preemption delay: 20 seconds
* Name of the NQA test instance created on DeviceA: test1; destination IP address of the NQA test instance: 10.2.1.1/24; type of the NQA test instance: ICMP; TTL value carried in an NQA test packet: 10; interval at which NQA tests are performed: 20 seconds
* Value by which DeviceA's priority reduces if the master link goes Down: 40

#### Procedure

1. Assign IP addresses to DeviceA's interfaces. The configurations of the DeviceE, DeviceB, and DeviceC are similar to the configuration of DeviceA. For configuration details, see [Configuration Files](#EN-US_TASK_0172361826__section_05) in this section.
   
   
   
   # Assign IP addresses to GE 0/1/0 and GE 0/2/0.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
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
   [*DeviceA-GigabitEthernet0/2/0] ip address 10.1.2.1 24
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] ip route-static 10.2.1.0 255.255.255.0 10.1.2.2
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure basic VRRP group functions.
   
   
   
   # Create VRRP group 1 on DeviceA, and set DeviceA's priority to 120 so that DeviceA functions as the master device.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 priority 120
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 preempt-mode timer delay 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] vrrp recover-delay 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Create VRRP group 1 on DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] vrrp vrid 1 virtual-ip 10.1.1.10
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   After completing the configurations, run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceA and DeviceB. The command outputs show that DeviceA's and DeviceB's VRRP statuses are **Master** and **Backup**, respectively.
   ```
   [~DeviceA] display vrrp interface gigabitethernet 0/1/0 verbose
   GigabitEthernet0/1/0 | Virtual Router 1
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
   Backup-forward : disabled
   Create Time       : 2013-09-24 15:08:16
   Last Change Time  : 2013-09-24 15:08:22
   ```
   ```
   [~DeviceB] display vrrp interface gigabitethernet 0/1/0 verbose
   GigabitEthernet0/1/0 | Virtual Router 1
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
   Backup-forward : disabled
   Create Time       : 2013-09-24 15:21:13
   Last Change Time  : 2013-09-24 15:21:19
   ```
3. Create an NQA test instance with a destination IP address of 10.2.1.1/24 on DeviceA.
   
   
   ```
   [~DeviceA] nqa test-instance admin test1
   ```
   ```
   [*DeviceA-nqa-admin-test1] test-type icmp
   ```
   ```
   [*DeviceA-nqa-admin-test1] destination-address ipv4 10.2.1.1
   ```
   ```
   [*DeviceA-nqa-admin-test1] ttl 10
   ```
   ```
   [*DeviceA-nqa-admin-test1] frequency 20
   ```
   ```
   [*DeviceA-nqa-admin-test1] start now
   ```
   ```
   [*DeviceA] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   After completing the configurations, run the [**display nqa results test-instance admin test1**](cmdqueryname=display+nqa+results+test-instance+admin+test1) command. The command output shows that the status of the NQA test instance is **success**.
   
   ```
   [~DeviceA] display nqa results test-instance admin test1
   NQA entry(admin, test1) :testflag is active ,testtype is icmp
     1 .Test 1 result   The test is finished
      Send operation times: 3              Receive response times: 3
      Completion:success                  RTD OverThresholds number: 0
      Attempts number:1                    Drop operation number:0
      Disconnect operation number:0        Operation timeout number:0
      System busy operation number:0       Connection fail number:0
      Operation sequence errors number:0   RTT Stats errors number:0
      Destination ip address:10.2.1.1
      Min/Max/Average Completion Time: 60/90/80
      Sum/Square-Sum  Completion Time: 240/19800
      Last Good Probe Time: 2013-09-24 15:30:38.7
      Lost packet ratio: 0 %        
   ```
4. Associate the VRRP group with the NQA test instance.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] vrrp vrid 1 track nqa admin test1 reduced 40
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
5. Verify the configuration.
   
   
   
   Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceC's GE 0/2/0 to simulate a link fault.
   
   Run the [**display nqa results test-instance admin test1**](cmdqueryname=display+nqa+results+test-instance+admin+test1) command on DeviceA. The command output shows that the status of the NQA test instance is **failed**.
   
   ```
   [~DeviceA] display nqa results test-instance admin test1
   NQA entry(admin, test1) :testflag is active ,testtype is icmp
     1 .Test 1 result   The test is finished
      Send operation times: 3              Receive response times: 0               
      Completion:failed                   RTD OverThresholds number: 0            
      Attempts number:1                    Drop operation number:3                 
      Disconnect operation number:0        Operation timeout number:0              
      System busy operation number:0       Connection fail number:0                
      Operation sequence errors number:0   RTT Stats errors number:0               
      Destination ip address:10.2.1.1                                              
      Min/Max/Average Completion Time: 0/0/0                                       
      Sum/Square-Sum  Completion Time: 0/0                                         
      Last Good Probe Time: 2013-09-24 15:40:26.7                                  
      Lost packet ratio: 100 %    
   ```
   After 20 seconds, run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceA and DeviceB. The command outputs show that DeviceA's and DeviceB's VRRP statuses become **Backup** and **Master**, respectively.
   ```
   [~DeviceA] display vrrp
   GigabitEthernet0/1/0 | Virtual Router 1
   State          : Backup
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.2
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
   Backup-forward : disabled
   Track NQA         : admin  test1   Priority Reduced : 40
   NQA State         : failed
   Create Time       : 2013-09-24 15:08:16
   Last Change Time  : 2013-09-24 15:40:48
   ```
   ```
   [~DeviceB] display vrrp
   GigabitEthernet0/1/0 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.2
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
   Backup-forward : disabled
   Create Time       : 2013-09-24 15:21:13
   Last Change Time  : 2013-09-24 15:40:48
   ```
   
   Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on DeviceC's GE 0/2/0. After GE 0/2/0 goes Up, wait 20 seconds and then run the [**display vrrp**](cmdqueryname=display+vrrp) command on DeviceA and DeviceB. The command outputs show that DeviceA's and DeviceB's VRRP statuses become **Master** and **Backup**, respectively.
   ```
   [~DeviceA] display vrrp interface gigabitethernet 0/1/0 verbose
   GigabitEthernet0/1/0 | Virtual Router 1
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
   Virtual Mac    :  0000-5e00-0101
   Passive Mode      : NO
   Check TTL      : YES
   Config type    : normal-vrrp
   Backup-forward : disabled
   Track NQA      : admin  test1   Priority reduced : 40
   NQA state      : success
   Create Time       : 2013-09-24 15:08:16
   Last Change Time  : 2013-09-24 15:58:45
   ```
   ```
   [~DeviceB] display vrrp interface gigabitethernet 0/1/0 verbose
   GigabitEthernet0/1/0 | Virtual Router 1
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
   Virtual Mac    :  0000-5e00-0102
   Passive Mode      : NO
   Check TTL      : YES
   Config type    : normal-vrrp
   Backup-forward : disabled
   Create Time       : 2013-09-24 15:21:13
   Last Change Time  : 2013-09-24 15:58:45
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.10
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt-mode timer delay 20
   vrrp recover-delay 20
   vrrp vrid 1 track nqa admin test1 reduced 40
  #
  interface GigabitEthernet0/2/0
   ip address 10.1.2.1 255.255.255.0
  #
   ip route-static 10.2.1.0 255.255.255.0 10.1.2.2
  #
  nqa test-instance admin test1
   test-type icmp
   destination-address ipv4 10.2.1.1
   frequency 20
   ttl 10
   start now
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.10
  #
  interface GigabitEthernet0/2/0
   ip address 10.1.2.1 255.255.255.0
  #
   ip route-static 10.2.1.0 255.255.255.0 10.1.2.2
  #
  return 
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.2.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   ip address 10.2.1.1 255.255.255.0
  #
  return 
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  vlan batch 10
  #
  interface Vlanif10
   ip address 10.1.1.3 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port default vlan 10
  #
  interface GigabitEthernet0/2/0
   portswitch
   undo shutdown
   port default vlan 10
  #
  return    
  ```