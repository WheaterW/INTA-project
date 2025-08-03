Example for Configuring mVRRP6
==============================

Example for Configuring mVRRP6

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176741659__fig_dc_vrp_vrrp_cfg_012401), DeviceC and DeviceD are each dual-homed to DeviceA and DeviceB. VRRP6 in master/backup mode is configured on DeviceA and DeviceB. If multiple VRRP6 groups are configured on DeviceA and DeviceB, a large number of VRRP6 Advertisement packets are exchanged between the two devices during VRRP negotiation. To reduce bandwidth and system resource consumption, configure mVRRP6 groups and then bind common VRRP6 groups to the mVRRP6 groups as service VRRP6 groups. This allows mVRRP6 groups to determine the master/backup state of service VRRP6 groups.

**Figure 1** Network diagram of configuring mVRRP6 groups![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, and 100GE1/0/5, respectively.


  
![](figure/en-us_image_0000001130782016.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on DeviceA and DeviceB, configure a routing protocol to ensure IPv6 connectivity, and enable Layer 2 transparent transmission on DeviceC and DeviceD.
2. Configure mVRRP6 groups 1 and 2 on DeviceA and DeviceB.
3. Configure VRRP6 groups 10 and 20 on the interfaces connecting DeviceA to DeviceC and DeviceD and on the interfaces connecting DeviceB to DeviceC and DeviceD. Then bind the VRRP6 groups to the mVRRP groups as service VRRP6 groups.

#### Procedure

1. Assign an IPv6 address to each interface on DeviceA and DeviceB and configure OSPFv3. For details about the configurations of DeviceC and DeviceD, see the Configuration Scripts.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   [*DeviceA-ospfv3-1] area 0.0.0.0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1:1::1 64
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:1:2::1 64
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ipv6 enable
   [*DeviceA-100GE1/0/3] ipv6 address 2001:db8:1:5::1 64
   [*DeviceA-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] undo portswitch
   [*DeviceA-100GE1/0/4] ipv6 enable
   [*DeviceA-100GE1/0/4] ipv6 address 2001:db8:1:3::1 64
   [*DeviceA-100GE1/0/4] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/5
   [*DeviceA-100GE1/0/5] undo portswitch
   [*DeviceA-100GE1/0/5] ipv6 enable
   [*DeviceA-100GE1/0/5] ipv6 address 2001:db8:1:4::1 64
   [*DeviceA-100GE1/0/5] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] area 0.0.0.0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:1:1::2 64
   [*DeviceB-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ipv6 enable
   [*DeviceB-100GE1/0/2] ipv6 address 2001:db8:1:2::2 64
   [*DeviceB-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100ge 1/0/3
   [*DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ipv6 enable
   [*DeviceB-100GE1/0/3] ipv6 address 2001:db8:1:6::1 64
   [*DeviceB-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] undo portswitch
   [*DeviceB-100GE1/0/4] ipv6 enable
   [*DeviceB-100GE1/0/4] ipv6 address 2001:db8:1:3::2 64
   [*DeviceB-100GE1/0/4] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/5
   [*DeviceB-100GE1/0/5] undo portswitch
   [*DeviceB-100GE1/0/5] ipv6 enable
   [*DeviceB-100GE1/0/5] ipv6 address 2001:db8:1:4::2 64
   [*DeviceB-100GE1/0/5] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/5] quit
   [*DeviceB] commit
   ```
2. Configure mVRRP6 groups on DeviceA and DeviceB, and configure a higher priority for DeviceA so that it functions as the master.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/4
   [~DeviceA-100GE1/0/4] vrrp6 vrid 1 virtual-ip fe80::4 link-local
   [*DeviceA-100GE1/0/4] vrrp6 vrid 1 virtual-ip 2001:db8:1:3::11
   [*DeviceA-100GE1/0/4] vrrp6 vrid 1 admin
   [*DeviceA-100GE1/0/4] vrrp6 vrid 1 priority 120
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/5
   [*DeviceA-100GE1/0/5] vrrp6 vrid 2 virtual-ip fe80::5 link-local
   [*DeviceA-100GE1/0/5] vrrp6 vrid 2 virtual-ip 2001:db8:1:4::11
   [*DeviceA-100GE1/0/5] vrrp6 vrid 2 admin
   [*DeviceA-100GE1/0/5] vrrp6 vrid 2 priority 120
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/4
   [~DeviceB-100GE1/0/4] vrrp6 vrid 1 virtual-ip fe80::4 link-local
   [*DeviceB-100GE1/0/4] vrrp6 vrid 1 virtual-ip 2001:db8:1:3::11
   [*DeviceB-100GE1/0/4] vrrp vrid 1 admin
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/5
   [*DeviceB-100GE1/0/5] vrrp6 vrid 2 virtual-ip fe80::5 link-local
   [*DeviceB-100GE1/0/5] vrrp6 vrid 2 virtual-ip 2001:db8:1:4::11
   [*DeviceB-100GE1/0/5] vrrp vrid 2 admin
   [*DeviceB-100GE1/0/5] quit
   [*DeviceB] commit
   ```
3. Configure VRRP6 groups 10 and 20 on the interfaces connecting DeviceA to DeviceC and DeviceD, and on the interfaces connecting DeviceB to DeviceC and DeviceD. Then bind the VRRP6 groups to the mVRRP6 groups as service VRRP6 groups so that the mVRRP6 groups determine the master/backup state of the service VRRP6 groups.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] vrrp6 vrid 10 virtual-ip fe80::1 link-local
   [*DeviceA-100GE1/0/1] vrrp6 vrid 10 virtual-ip 2001:db8:1:1::11
   [*DeviceA-100GE1/0/1] vrrp6 vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] vrrp6 vrid 20 virtual-ip fe80::2 link-local
   [*DeviceA-100GE1/0/2] vrrp6 vrid 20 virtual-ip 2001:db8:1:2::11
   [*DeviceA-100GE1/0/2] vrrp6 vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] vrrp6 vrid 10 virtual-ip fe80::1 link-local
   [*DeviceB-100GE1/0/1] vrrp6 vrid 10 virtual-ip 2001:db8:1:1::11
   [*DeviceB-100GE1/0/1] vrrp6 vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] vrrp6 vrid 20 virtual-ip fe80::2 link-local
   [*DeviceB-100GE1/0/2] vrrp6 vrid 20 virtual-ip 2001:db8:1:2::11
   [*DeviceB-100GE1/0/2] vrrp6 vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
   [*DeviceB-100GE1/0/2] quit 
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the states of DeviceA and DeviceB in the VRRP6 groups.

```
[~DeviceA] display vrrp6
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Master      100GE1/0/4            A       2001:db8:1:3::11
   2 Master      100GE1/0/5            A       2001:db8:1:4::11
  10 Master      100GE1/0/1            M       2001:db8:1:1::11
  20 Master      100GE1/0/2            M       2001:db8:1:2::11
```
The states of DeviceA in the VRRP6 groups are as follows:

* In mVRRP6 groups 1 and 2, **State** is **Master**, and **Type** is **Admin**.
* In each service VRRP6 group, **State** is **Master**, and **Type** is **Member**.
```
[~DeviceB] display vrrp6
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Backup      100GE1/0/4            A       2001:db8:1:3::11
   2 Backup      100GE1/0/5            A       2001:db8:1:4::11
  10 Backup      100GE1/0/1            M       2001:db8:1:1::11
  20 Backup      100GE1/0/2            M       2001:db8:1:2::11
```
The states of DeviceB in the VRRP6 groups are as follows:

* In mVRRP6 groups 1 and 2, **State** is **Backup**, and **Type** is **Admin**.
* In each service VRRP6 group, **State** is **Backup**, and **Type** is **Member**.

# Shut down 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/4, and 100GE 1/0/5 on DeviceA to simulate a device fault. Check the VRRP6 states on DeviceA and DeviceB.

```
[~DeviceA] display vrrp6
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Initialize  100GE1/0/4           A   2001:db8:1:3::11
   2 Initialize  100GE1/0/5           A   2001:db8:1:4::11
  10 Initialize  100GE1/0/1           M   2001:db8:1:1::11
  20 Initialize  100GE1/0/2           M   2001:db8:1:2::11
```
The states of DeviceA in the VRRP6 groups are as follows:

* In mVRRP6 groups 1 and 2, **State** is **Initialize**, and **Type** is **Admin**.
* In each service VRRP6 group, **State** is **Initialize**, and **Type** is **Member**.
```
[~DeviceB] display vrrp6
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Master      100GE1/0/4           A   2001:db8:1:3::11
   2 Master      100GE1/0/5           A   2001:db8:1:4::11
  10 Master      100GE1/0/1           M   2001:db8:1:1::11
  20 Master      100GE1/0/2           M   2001:db8:1:2::11
```
The states of DeviceB in the VRRP6 groups are as follows:

* In mVRRP6 groups 1 and 2, **State** is **Master**, and **Type** is **Admin**.
* In each service VRRP6 group, **State** is **Master**, and **Type** is **Member**.

The command outputs show that the mVRRP6 states on DeviceA and DeviceB switch between **Master** and **Backup**.

# Run the **undo shutdown** command on 100GE1/0/1, 100GE1/0/2, 100GE1/0/4, and 100GE1/0/5 of DeviceA to simulate fault recovery. Check the VRRP6 states on DeviceA and DeviceB.

```
[~DeviceA] display vrrp6
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:3    Backup:0    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Master      100GE1/0/4           A   2001:db8:1:3::11
   2 Master      100GE1/0/5           A   2001:db8:1:4::11
  10 Master      100GE1/0/1           M   2001:db8:1:1::11
  20 Master      100GE1/0/2           M   2001:db8:1:2::11
```
The states of DeviceA in the VRRP6 groups are as follows:

* In mVRRP6 groups 1 and 2, **State** is **Master**, and **Type** is **Admin**.
* In each service VRRP6 group, **State** is **Master**, and **Type** is **Member**.
```
[~DeviceB] display vrrp6
Type: 
        N: Normal 
        A: Administrator 
        M: Member
        L: Load-Balance 
        LM: Load-Balance-Member
Total:3     Master:0    Backup:3    Non-active:0    
VRID State       Interface        Type    Virtual IP
--------------------------------------------------------
   1 Backup      100GE1/0/4           A   2001:db8:1:3::11
   2 Backup      100GE1/0/5           A   2001:db8:1:4::11
  10 Backup      100GE1/0/1           M   2001:db8:1:1::11
  20 Backup      100GE1/0/2           M   2001:db8:1:2::11
```
The states of DeviceB in the VRRP6 groups are as follows:

* In mVRRP6 groups 1 and 2, **State** is **Backup**, and **Type** is **Admin**.
* In each service VRRP6 group, **State** is **Backup** and **Type** is **Member**.

The command outputs show that the mVRRP status on DeviceA and DeviceB recovers.


#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch 
   ipv6 enable
   ipv6 address 2001:db8:1:1::1 64
   vrrp6 vrid 10 virtual-ip fe80::1 link-local
   vrrp6 vrid 10 virtual-ip 2001:db8:1:1::11
   vrrp6 vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable 
   ipv6 address 2001:db8:1:2::1 64
   vrrp6 vrid 20 virtual-ip fe80::1 link-local
   vrrp6 vrid 20 virtual-ip 2001:db8:1:2::11
   vrrp6 vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:5::1 64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:3::1 64
   vrrp6 vrid 1 virtual-ip fe80::1 link-local 
   vrrp6 vrid 1 virtual-ip 2001:db8:1:3::11
   vrrp6 vrid 1 admin
   vrrp6 vrid 1 priority 120
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/5
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:4::1 64
   vrrp6 vrid 2 virtual-ip fe80::1 link-local
   vrrp6 vrid 2 virtual-ip 2001:db8:1:4::11
   vrrp6 vrid 2 admin
   vrrp6 vrid 2 priority 120
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 1.1.1.1
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:1::2 64
   vrrp6 vrid 10 virtual-ip fe80::1 link-local
   vrrp6 vrid 10 virtual-ip 2001:db8:1:1::11
   vrrp6 vrid 10 track admin-vrrp interface 100ge 1/0/4 vrid 1 unflowdown
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable 
   ipv6 address 2001:db8:1:2::2 64
   vrrp6 vrid 20 virtual-ip fe80::1 link-local
   vrrp6 vrid 20 virtual-ip 2001:db8:1:2::11
   vrrp6 vrid 20 track admin-vrrp interface 100ge 1/0/5 vrid 2 unflowdown
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:6::1 64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:3::2 64
   vrrp6 vrid 1 virtual-ip fe80::1 link-local 
   vrrp6 vrid 1 virtual-ip 2001:db8:1:3::11
   vrrp6 vrid 1 admin
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/5
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:4::2 64
   vrrp6 vrid 2 virtual-ip fe80::1 link-local
   vrrp6 vrid 2 virtual-ip 2001:db8:1:4::11
   vrrp6 vrid 2 admin
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 2.2.2.2
  #
  return
  ```
* DeviceC
  
  ```
  #
   sysname DeviceC
  #
   vlan batch 10 20 30 40
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 20
  #
  interface 100GE1/0/3
   port default vlan 30
  #
  interface 100GE1/0/4
   port default vlan 40
  #
  return
  ```
* DeviceD
  
  ```
  #
   sysname DeviceD
  #
   vlan batch 10 20 30 40
  #
  interface 100GE1/0/1
   
   port default vlan 10
  #
  interface 100GE1/0/2
   port default vlan 20
  #
  interface 100GE1/0/3
   
   port default vlan 30
  #
  interface 100GE1/0/4
   port default vlan 40
  #
  return
  ```