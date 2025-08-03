Example for Configuring Association Between VRRP and Interface Status
=====================================================================

Example for Configuring Association Between VRRP and Interface Status

#### Networking Requirements

VRRP cannot detect status changes of the interfaces that are not in a VRRP group. As such, if an uplink VRRP-disabled interface fails, VRRP cannot detect the failure and continues to forward user traffic through the faulty interface, resulting in service interruptions. To prevent service interruptions, configure the VRRP group to track the VRRP-disabled interface. This way, if the interface goes down, the master device in the VRRP group reduces its priority and sends a VRRP Advertisement packet carrying a priority lower than that of the backup device to enable the backup device to preempt the master role and take over traffic forwarding.

In [Figure 1](#EN-US_TASK_0000001130784068__fig_dc_vrp_vrrp_cfg_012501), HostA is connected to HostB through a default gateway, and a VRRP group is configured on DeviceA (master) and DeviceB (backup). The traffic from HostA to HostB is transmitted along the path HostA -> DeviceA -> DeviceC -> HostB. If the link between DeviceA and DeviceC fails, traffic from HostA to HostB is lost. To prevent traffic loss, configure the VRRP group to track the interface connecting DeviceA to DeviceC.

**Figure 1** Network diagram of configuring association between VRRP and interface status![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130784090.png)

#### Precautions

DeviceA's interface (100GE1/0/1) and DeviceB's interface (100GE1/0/1) must be on the same network segment.

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on the devices and configure a routing protocol to ensure IP connectivity.
2. Configure VRRP group 1 on DeviceA's 100GE1/0/1 and set a higher VRRP priority for DeviceA so that it functions as the master in the VRRP group.
3. Configure VRRP group 1 on DeviceB's 100GE1/0/1 and use the default priority so that it functions as the backup in the VRRP group.
4. Configure VRRP group 1 on DeviceA to track the uplink interface 100GE1/0/2.

#### Procedure

1. Assign an IP address to each interface on DeviceA, DeviceB, and DeviceC. Then, configure OSPF to ensure that the devices can communicate with one another.
   
   # Configure DeviceA.
   
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
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.1.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 192.168.2.1 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ip address 192.168.1.2 24
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ip address 192.168.2.2 24
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] undo portswitch
   [*DeviceC-100GE1/0/3] ip address 172.16.1.1 24
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] ospf 1
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
2. Configure a VRRP group on DeviceA and DeviceB.
   
   # Configure VRRP group 1 on DeviceA, and set the VRRP priority of DeviceA to 120 so that it functions as the master.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceA-100GE1/0/1] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure VRRP group 1 on DeviceB, and use the default priority so that it functions as the backup.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 1 virtual-ip 10.1.1.111
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
3. Associate VRRP with interface status.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 1 track interface 100ge 1/0/2 reduce 30
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check the status of the interface tracked by the VRRP group. The following example uses the command output on DeviceA.

```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State             : Master
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.1
Local IP          : 10.1.1.1
PriorityRun       : 120
PriorityConfig    : 120
MasterPriority    : 120
Preempt           : YES      Delay Time : 0s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Track IF        : 100GE1/0/2            
Priority Reduced :30
IF State        : UP
Create Time       : 2020-12-29 05:41:23
Last Change Time  : 2020-12-29 05:41:33
```

# Run the [**shutdown**](cmdqueryname=shutdown) command on DeviceA's 100GE1/0/2 to simulate a link fault.

```
[~DeviceA] interface 100ge 1/0/2
[~DeviceA-100GE1/0/2] shutdown
[*DeviceA-100GE1/0/2] quit
[*DeviceA] commit
```

# Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp verbose
100GE1/0/1 | Virtual Router 1
State           : Backup
Virtual IP        : 10.1.1.111
Master IP         : 10.1.1.2
Local IP          : 10.1.1.1
PriorityRun       : 90
PriorityConfig    : 120
MasterPriority    : 100
Preempt           : YES      Delay Time : 0s    Remain : --
Hold Multiplier   : 4
TimerRun          : 1s
TimerConfig       : 1s
Auth Type         : NONE
Virtual MAC       : 00-e0-fc-12-78-90
Check TTL         : YES
Config Type       : Normal
Track IF          : 100GE1/0/2            Priority Reduced :30
IF State        : DOWN
Create Time       : 2020-12-29 05:41:23
Last Change Time  : 2020-12-29 05:41:33
```

The command outputs show that DeviceA is in the **Backup** state and DeviceB is in the **Master** state in VRRP group 1.


#### Configuration Scripts

* DeviceA
  
  ```
  # 
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.1.1.111
   vrrp vrid 1 priority 120
   vrrp vrid 1 track interface 100ge 1/0/2 reduce 30
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
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
   vrrp vrid 1 virtual-ip 10.1.1.111
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
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
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
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