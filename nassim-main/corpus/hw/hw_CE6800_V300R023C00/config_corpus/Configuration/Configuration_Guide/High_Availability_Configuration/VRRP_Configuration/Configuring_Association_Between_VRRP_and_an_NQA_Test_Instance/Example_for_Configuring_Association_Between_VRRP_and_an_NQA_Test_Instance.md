Example for Configuring Association Between VRRP and an NQA Test Instance
=========================================================================

Example for Configuring Association Between VRRP and an NQA Test Instance

#### Networking Requirements

VRRP can detect an uplink VRRP-disabled interface fault on a VRRP-enabled device. However, if a cross-device uplink fails, VRRP is unable to detect the fault. As a result, user traffic is lost.

To address this problem, you can associate a VRRP group with an NQA test instance to track the master device's cross-device uplink. If the uplink fails and hosts on the LAN cannot access the external network through the master device, NQA instructs VRRP to reduce the master's priority by a specified value. This allows the backup device with a higher priority to preempt the master role, thereby ensuring uninterrupted communication between hosts on the LAN and the external network. After the uplink recovers, NQA instructs VRRP to restore the original master's priority.

As shown in [Figure 1](#EN-US_TASK_0000001130784056__fig_dc_vrp_vrrp_cfg_014101), a VRRP group is configured on DeviceA and DeviceB, of which DeviceA is the master. The VRRP group is required to track an NQA test instance whose destination IP address is the IP address of DeviceC's uplink interface so that the VRRP group can perform a master/backup switchover when the uplink interface goes down. When the uplink interface goes up, traffic is switched back to the original master device.

**Figure 1** Network diagram of associating a VRRP group with an NQA test instance![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001130784086.png)

#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface of the devices and configure a routing protocol to ensure link connectivity.
2. Configure a VRRP group on DeviceA (master) and DeviceB (backup).
3. On DeviceA, create an NQA test instance whose destination IP address is the IP address of DeviceC's uplink interface.
4. Associate the VRRP group on DeviceA with the NQA test instance.


#### Procedure

1. Assign an IP address to each interface on DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For details, see [Configuration Scripts](#EN-US_TASK_0000001130784056__section_05).
   
   # Assign IP addresses to 100GE 1/0/1 and 100GE 1/0/2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.2.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] ip route-static 10.2.1.0 255.255.255.0 10.1.2.2
   [*DeviceA] commit
   ```
2. Configure basic VRRP group functions.
   
   # Configure VRRP group 1 on DeviceA, and set its priority to 120 so that it functions as the master.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.10
   [*DeviceA-100GE1/0/1] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/1] vrrp vrid 1 preempt timer delay 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure VRRP group 1 on DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.10
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   After completing the configurations, run the [**display vrrp verbose**](cmdqueryname=display+vrrp+verbose) command on DeviceA or DeviceB to view the VRRP status. The command outputs show that DeviceA is in the **Master** state and DeviceB is in the **Backup** state.
   ```
   [~DeviceA] display vrrp verbose
   100GE1/0/1 | Virtual Router 1
   State          : Master
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.1
   PriorityRun    : 120
   PriorityConfig : 120
   MasterPriority : 120
   Preempt        : YES   Delay Time : 20s   Remain : --
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 00-e0-fc-12-78-90
   Check TTL      : YES
   Config Type    : Normal
   Create Time       : 2020-09-24 15:08:16
   Last Change Time  : 2020-09-24 15:08:22
   ```
   ```
   [~DeviceB] display vrrp verbose
   100GE1/0/1 | Virtual Router 1
   State          : Backup
   Virtual IP     : 10.1.1.10
   Master IP      : 10.1.1.1
   PriorityRun    : 100
   PriorityConfig : 100
   MasterPriority : 120
   Preempt        : YES   Delay Time : 0s   Remain : --
   Hold Multiplier: 4
   TimerRun       : 1s
   TimerConfig    : 1s
   Auth Type      : NONE
   Virtual MAC    : 00-e0-fc-12-78-90
   Check TTL      : YES
   Config Type    : Normal
   Create Time       : 2020-09-24 15:21:13
   Last Change Time  : 2020-09-24 15:21:19
   ```
3. Create an NQA test instance whose destination IP address is 10.2.1.1/24 on DeviceA.
   ```
   [~DeviceA] nqa test-instance admin test1
   [*DeviceA-nqa-admin-test1] test-type icmp
   [*DeviceA-nqa-admin-test1] destination-address ipv4 10.2.1.1
   [*DeviceA-nqa-admin-test1] ttl 10
   [*DeviceA-nqa-admin-test1] frequency 20
   [*DeviceA-nqa-admin-test1] start now
   [*DeviceA-nqa-admin-test1] quit
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
      Last Good Probe Time: 2020-09-24 15:30:38.7
      Lost packet ratio: 0 %        
   ```
4. Associate the VRRP group with the NQA test instance.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 track nqa admin test1 reduce 40
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceA's 100GE1/0/2 to simulate a link fault. Run the [**display nqa results test-instance admin test1**](cmdqueryname=display+nqa+results+test-instance+admin+test1) command on DeviceA to check the status of the NQA test instance.

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
   Last Good Probe Time: 2020-09-24 15:40:26.7                                  
   Lost packet ratio: 100 %    
```

The command output shows that the status of the NQA test instance changes to **failed**.

After 20 seconds, run the [**display vrrp verbose**](cmdqueryname=display+vrrp+verbose) command on DeviceA and DeviceB to check the VRRP status.
```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State          : Backup
Virtual IP     : 10.1.1.10
Master IP      : 10.1.1.2
Local IP       : 10.1.1.1
PriorityRun    : 80
PriorityConfig : 120
MasterPriority : 100
Preempt        : YES   Delay Time : 20s   Remain : --
Hold Multiplier: 4
TimerRun       : 1s
TimerConfig    : 1s
Auth Type      : NONE
Virtual MAC    : 00-e0-fc-12-78-90
Check TTL      : YES
Config Type    : Normal
Track NQA         : admin  test1   
Priority Reduced : 40
NQA State         : failed
Create Time       : 2020-09-24 15:08:16
Last Change Time  : 2020-09-24 15:40:48
```
```
[~DeviceB] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State          : Master
Virtual IP     : 10.1.1.10
Master IP      : 10.1.1.2
Local IP       : 10.1.1.2
PriorityRun    : 100
PriorityConfig : 100
MasterPriority : 100
Preempt        : YES   Delay Time : 0s   Remain : --
Hold Multiplier: 4
TimerRun       : 1s
TimerConfig    : 1s
Auth Type      : NONE
Virtual MAC    : 00-e0-fc-12-78-90
Check TTL      : YES
Config Type    : Normal
Create Time       : 2020-09-24 15:21:13
Last Change Time  : 2020-09-24 15:40:48
```

The command outputs show that DeviceB is in the **Master** state and DeviceA is in the **Backup** state, indicating that a master/backup VRRP switchover has been performed.

Run the [**undo shutdown**](cmdqueryname=undo+shutdown) command on DeviceC's interface 100GE1/0/2. After the interface goes up, wait for 20 seconds, and then run the [**display vrrp verbose**](cmdqueryname=display+vrrp+verbose) command on DeviceA and DeviceB to check the VRRP status.
```
[~DeviceA] display vrrp verbose
100GE1/0/2 | Virtual Router 1
State           : Master
Virtual IP      : 10.1.1.10
Master IP       : 10.1.1.1
Local IP        : 10.1.1.1
PriorityRun     : 120
PriorityConfig  : 120
MasterPriority  : 120
Preempt         : YES   Delay Time : 20s   Remain : --
Hold Multiplier : 4
TimerRun        : 1s
TimerConfig     : 1s
Auth Type       : NONE
Virtual Mac     :  00-e0-fc-12-78-90
Check TTL       : YES
Config type     : Normal
Track NQA       : admin  test1   Priority reduced : 40
NQA state       : success
Create Time       : 2020-09-24 15:08:16
Last Change Time  : 2020-09-24 15:58:45
```
```
[~DeviceB] display vrrp verbose
100GE1/0/2 | Virtual Router 1
State          : Backup
Virtual IP     : 10.1.1.10
Master IP      : 10.1.1.1
Local IP       : 10.1.1.2
PriorityRun    : 100
PriorityConfig : 100
MasterPriority : 120
Preempt        : YES   Delay Time : 0s   Remain : --
Hold Multiplier: 4
TimerRun       : 1s
TimerConfig    : 1s
Auth Type      : NONE
Virtual Mac    :  00-e0-fc-12-78-90
Check TTL      : YES
Config type    : Normal
Backup-forward    : disabled
Create Time       : 2020-09-24 15:21:13
Last Change Time  : 2020-09-24 15:58:45
```

The command outputs show that DeviceA and DeviceB switch to the **Master** and **Backup** states, respectively.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.10
   vrrp vrid 1 priority 120
   vrrp vrid 1 preempt timer delay 20
   vrrp vrid 1 track nqa admin test1 reduce 40
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
   ip route-static 10.2.1.0 255.255.255.0 10.1.1.2
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
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.10
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
  #
   ip route-static 10.2.1.0 255.255.255.0 10.1.2.2
  #
  return 
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
  #
  return 
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
  #
  return 
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
   vlan batch 100
  #
  interface 100GE1/0/1
   port default vlan 100
  #
  interface 100GE1/0/2
   port default vlan 200
  #
  return    
  ```