Example for Configuring mVRRP Groups
====================================

Example for Configuring mVRRP Groups

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130784048__fig_dc_vrp_vrrp_cfg_012401), DeviceC and DeviceD are each dual-homed to DeviceA and DeviceB. VRRP in master/backup mode is configured on DeviceA and DeviceB. If multiple VRRP groups are configured on DeviceA and DeviceB, a large number of VRRP Advertisement packets are exchanged between the two devices during VRRP negotiation. To reduce bandwidth and system resource consumption, configure mVRRP groups and then bind common VRRP groups to the mVRRP groups as service VRRP groups. This allows mVRRP groups to determine the master/backup state of service VRRP groups.

**Figure 1** Network diagram of configuring mVRRP groups![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, and 100GE1/0/5, respectively.


  
![](figure/en-us_image_0000001130624288.png)

#### Precautions

To improve security, you are advised to configure a VRRP security policy. For details, see [Example for Configuring VRRP in Master/Backup Mode](vrp_vrrp_cfg_0121.html).

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface on DeviceA and DeviceB, configure a routing protocol to ensure IP connectivity, and enable Layer 2 transparent transmission on DeviceC and DeviceD.
2. Configure mVRRP groups 1 and 2 on DeviceA and DeviceB.
3. Configure VRRP groups 10 and 20 on DeviceA and DeviceB and bind them to the mVRRP groups as service VRRP groups.


#### Procedure

1. Assign an IP address to each interface on DeviceA and DeviceB and configure OSPF. For details about the configurations of DeviceC and DeviceD, see [Configuration Scripts](#EN-US_TASK_0000001130784048__context158161004500).
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.10.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.20.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] undo portswitch
   [*DeviceA-100GE1/0/4] ip address 10.10.3.1 24
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/5
   [*DeviceA-100GE1/0/5] undo portswitch
   [*DeviceA-100GE1/0/5] ip address 10.20.3.1 24
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] ospf
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.3.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.20.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.20.3.0 0.0.0.255
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
   [*DeviceB-100GE1/0/1] ip address 10.10.1.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 10.20.1.2 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ip address 192.168.2.1 24
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] undo portswitch
   [*DeviceB-100GE1/0/4] ip address 10.10.3.2 24
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/5
   [*DeviceB-100GE1/0/5] undo portswitch
   [*DeviceB-100GE1/0/5] ip address 10.20.3.2 24
   [*DeviceB-100GE1/0/5] quit
   [*DeviceB] ospf
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.3.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.20.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.20.3.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
2. Configure mVRRP groups on DeviceA and DeviceB, and configure a higher priority for DeviceA so that it functions as the master.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/4
   [~DeviceA-100GE1/0/4] vrrp vrid 1 virtual-ip 10.10.3.111
   [*DeviceA-100GE1/0/4] vrrp vrid 1 admin
   [*DeviceA-100GE1/0/4] vrrp vrid 1 priority 120
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/5
   [*DeviceA-100GE1/0/5] vrrp vrid 2 virtual-ip 10.20.3.111
   [*DeviceA-100GE1/0/5] vrrp vrid 2 admin
   [*DeviceA-100GE1/0/5] vrrp vrid 2 priority 120
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/4
   [~DeviceB-100GE1/0/4] vrrp vrid 1 virtual-ip 10.10.3.111
   [*DeviceB-100GE1/0/4] vrrp vrid 1 admin
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/5
   [*DeviceB-100GE1/0/5] vrrp vrid 2 virtual-ip 10.20.3.111
   [*DeviceB-100GE1/0/5] vrrp vrid 2 admin
   [*DeviceB-100GE1/0/5] quit
   [*DeviceB] commit
   ```
3. Configure VRRP groups 10 and 20 on DeviceA and DeviceB and bind them to the mVRRP groups as service VRRP groups.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp vrid 10 virtual-ip 10.10.1.111
   [*DeviceA-100GE1/0/1] vrrp vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] vrrp vrid 20 virtual-ip 10.20.1.111
   [*DeviceA-100GE1/0/2] vrrp vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp vrid 10 virtual-ip 10.10.1.111
   [*DeviceB-100GE1/0/1] vrrp vrid 10 track admin-vrrp interface 100ge 1/0/1 vrid 1 unflowdown
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] vrrp vrid 20 virtual-ip 10.20.1.111
   [*DeviceB-100GE1/0/2] vrrp vrid 20 track admin-vrrp interface 100ge 1/0/2 vrid 2 unflowdown
   [*DeviceB-100GE1/0/2] quit 
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Master      100GE1/0/4            A       10.10.3.111
   2 Master      100GE1/0/5            A       10.20.3.111
  10 Master      100GE1/0/1            M       10.10.1.111
  20 Master      100GE1/0/2            M       10.20.1.111
```
The VRRP status on DeviceA is as follows:

* In mVRRP groups 1 and 2, **State** is **Master** and **Type** is **Admin**.
* In each service VRRP group, **State** is **Master** and **Type** is **Member**.
```
[~DeviceB] display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Backup      100GE1/0/4            A       10.10.3.111
   2 Backup      100GE1/0/5            A       10.20.3.111
  10 Backup      100GE1/0/1            M       10.10.1.111
  20 Backup      100GE1/0/2            M       10.20.1.111
```
The VRRP status on DeviceB is as follows:

* In mVRRP groups 1 and 2, **State** is **Backup** and **Type** is **Admin**.
* In each service VRRP group, **State** is **Backup** and **Type** is **Member**.

# Shut down 100GE1/0/1, 100GE1/0/2, 100GE1/0/4, and 100GE1/0/5 on DeviceA to simulate a device fault. Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Initialize  100GE1/0/4           A   10.10.3.111
   2 Initialize  100GE1/0/5           A   10.20.3.111
  10 Initialize  100GE1/0/1           M  10.10.1.111
  20 Initialize  100GE1/0/2           M  10.20.1.111
```
The VRRP status on DeviceA is as follows:

* In mVRRP groups 1 and 2, **State** is **Initialize** and **Type** is **Admin**.
* In each service VRRP group, **State** is **Initialize** and **Type** is **Member**.
```
[~DeviceB] display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Master      100GE1/0/4           A   10.10.3.111
   2 Master      100GE1/0/5           A   10.20.3.111
  10 Master      100GE1/0/1           M  10.10.1.111
  20 Master      100GE1/0/2           M  10.20.1.111
```
The VRRP status on DeviceB is as follows:

* In mVRRP groups 1 and 2, **State** is **Master** and **Type** is **Admin**.
* In each service VRRP group, **State** is **Master** and **Type** is **Member**.

The command outputs show that the mVRRP status on DeviceA and DeviceB switches between **Master** and **Backup**.

# Run the **undo shutdown** command on 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/4, and 100GE 1/0/5 of DeviceA to simulate fault recovery. Check the VRRP status on DeviceA and DeviceB.

```
[~DeviceA] display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Master      100GE1/0/4           A   10.10.3.111
   2 Master      100GE1/0/5           A   10.20.3.111
  10 Master      100GE1/0/1           M  10.10.1.111
  20 Master      100GE1/0/2           M  10.20.1.111
```
The VRRP status on DeviceA is as follows:

* In mVRRP groups 1 and 2, **State** is **Master** and **Type** is **Admin**.
* In each service VRRP group, **State** is **Master** and **Type** is **Member**.
```
[~DeviceB] display vrrp
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:0    Backup:3    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Backup      100GE1/0/4           A   10.10.3.111
   2 Backup      100GE1/0/5           A   10.20.3.111
  10 Backup      100GE1/0/1           M  10.10.1.111
  20 Backup      100GE1/0/2           M  10.20.1.111
```
The VRRP status on DeviceB is as follows:

* In mVRRP groups 1 and 2, **State** is **Backup** and **Type** is **Admin**.
* In each service VRRP group, **State** is **Backup** and **Type** is **Member**.

The command outputs show that the mVRRP status on DeviceA and DeviceB recovers.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.10.1.1 255.255.255.0
   vrrp vrid 10 virtual-ip 10.10.1.111
   vrrp vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.20.1.1 255.255.255.0
   vrrp vrid 20 virtual-ip 10.20.1.111
   vrrp vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.10.3.1 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.10.3.111
   vrrp vrid 1 admin
   vrrp vrid 1 priority 120
  #
  interface 100GE1/0/5
   undo portswitch
   ip address 10.20.3.1 255.255.255.0 
   vrrp vrid 2 virtual-ip 10.1.1.222
   vrrp vrid 2 admin
   vrrp vrid 2 priority 120
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.10.3.0 0.0.0.255
    network 10.20.1.0 0.0.0.255
    network 10.20.3.0 0.0.0.255
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
   ip address 10.10.1.2 255.255.255.0
   vrrp vrid 10 virtual-ip 10.10.1.111
   vrrp vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.20.1.2 255.255.255.0
   vrrp vrid 20 virtual-ip 10.20.1.111
   vrrp vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.10.3.2 255.255.255.0 
   vrrp vrid 1 virtual-ip 10.10.3.111
   vrrp vrid 1 admin
  #
  interface 100GE1/0/5
   undo portswitch
   ip address 10.20.3.2 255.255.255.0 
   vrrp vrid 2 virtual-ip 10.1.1.222
   vrrp vrid 2 admin
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.10.3.0 0.0.0.255
    network 10.20.1.0 0.0.0.255
    network 10.20.3.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 100 200
  #
  interface 100GE1/0/1
   port default vlan 100
  #
  interface 100GE1/0/2
   port default vlan 100
  #
  interface 100GE1/0/3
   port default vlan 200
  #
  interface 100GE1/0/4
   port default vlan 200
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
   vlan batch 100 200
  #
  interface 100GE1/0/1
   port default vlan 100
  #
  interface 100GE1/0/2
   port default vlan 100
  #
  interface 100GE1/0/3
   port default vlan 200
  #
  interface 100GE1/0/4
   port default vlan 200
  #
  return
  ```