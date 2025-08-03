Example for Establishing IPv6 VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)
======================================================================================

Example for Establishing IPv6 VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001147836560__fig_dc_cfg_vxlan_cfgcase_000101), an enterprise has VMs deployed in different data centers. VM1 on Server1 (Server1 VM1 for short) belongs to VLAN 10, Server3 VM1 belongs to VLAN 30, and Server2 VM1 belongs to VLAN 20. Server1 and Server2 reside on different network segments, and Server3 and Server2 reside on the same network segment. Server1 VM1, Server3 VM1, and Server2 VM1 need to communicate with each other through an IPv6 VXLAN gateway.

**Figure 1** Configuring IPv6 VXLAN in centralized gateway mode![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001193876301.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv6 routing protocol on Device1, Device2, and Device3 to ensure Layer 3 connectivity on the network.
2. Configure service access points on Device1 and Device3 to distinguish service traffic.
3. Configure IPv6 VXLAN tunnels on Device1, Device2, and Device3 to forward service traffic.
4. Configure Device2 as an IPv6 Layer 3 VXLAN gateway to allow users on different network segments to communicate at Layer 3.


#### Procedure

1. Configure an IPv6 routing protocol.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] interface loopback 1
   [*Device1-LoopBack1] ipv6 enable
   [*Device1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*Device1-LoopBack1] quit
   [*Device1] interface 100ge 1/0/1
   [*Device1-100GE1/0/1] undo portswitch
   [*Device1-100GE1/0/1] ipv6 enable
   [*Device1-100GE1/0/1] ipv6 address 2001:DB8:4::1 64
   [*Device1-100GE1/0/1] quit
   [*Device1] ospfv3 1
   [*Device1-ospfv3-1] router-id 1.1.1.1
   [*Device1-ospfv3-1] area 0
   [*Device1-ospfv3-1-area-0.0.0.0] quit
   [*Device1-ospfv3-1] quit
   [*Device1] interface loopback 1
   [*Device1-LoopBack1] ospfv3 1 area 0
   [*Device1-LoopBack1] quit
   [*Device1] interface 100ge 1/0/1
   [*Device1-100GE1/0/1] ospfv3 1 area 0
   [*Device1-100GE1/0/1] quit
   [*Device1] commit
   ```
   
   After OSPFv3 is configured, the devices can learn the IPv6 address of each other's loopback interface using OSPFv3 and successfully ping each other. The following example shows the command output on Device1 after it pings Device3.
   
   ```
   [~Device1] ping ipv6 2001:DB8:3::3
     PING 2001:DB8:3::3: 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:3::3
       bytes=56 Sequence=1 hop limit=64 time=115 ms
       Reply from 2001:DB8:3::3
       bytes=56 Sequence=2 hop limit=64 time=1 ms
       Reply from 2001:DB8:3::3
       bytes=56 Sequence=3 hop limit=64 time=1 ms
       Reply from 2001:DB8:3::3
       bytes=56 Sequence=4 hop limit=64 time=1 ms
       Reply from 2001:DB8:3::3
       bytes=56 Sequence=5 hop limit=64 time=1 ms
   ---2001:DB8:3::3 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=1/23/115 ms
   
   ```
2. Configure service access points on Device1 and Device3.
   
   
   
   # Configure Device1. The configuration of Device3 is similar to that of Device1.
   
   ```
   [~Device1] bridge-domain 10
   [*Device1-bd10] quit
   [*Device1] interface 100ge 1/0/2.1 mode l2
   [*Device1-100GE1/0/2.1] encapsulation dot1q vid 10
   [*Device1-100GE1/0/2.1] bridge-domain 10
   [*Device1-100GE1/0/2.1] quit
   [*Device1] bridge-domain 20
   [*Device1-bd20] quit
   [*Device1] interface 100ge 1/0/3.1 mode l2
   [*Device1-100GE1/0/3.1] encapsulation dot1q vid 30
   [*Device1-100GE1/0/3.1] bridge-domain 20
   [*Device1-100GE1/0/3.1] quit
   [*Device1] commit
   ```
3. Configure IPv6 VXLAN tunnels on Device1, Device2, and Device3.
   
   
   
   # Configure Device1.
   
   ```
   [~Device1] bridge-domain 10
   [~Device1-bd10] vxlan vni 5010
   [*Device1-bd10] quit
   [*Device1] interface nve 1
   [*Device1-Nve1] source 2001:DB8:1::1
   [*Device1-Nve1] vni 5010 head-end peer-list 2001:DB8:2::2
   [*Device1-Nve1] quit
   [*Device1] bridge-domain 20
   [*Device1-bd20] vxlan vni 5020
   [*Device1-bd20] quit
   [*Device1] interface nve 1
   [*Device1-Nve1] vni 5020 head-end peer-list 2001:DB8:2::2 2001:DB8:3::3
   [*Device1-Nve1] quit
   [*Device1] commit
   ```
   
   # Configure Device2.
   
   ```
   [~Device2] bridge-domain 10
   [*Device2-bd10] vxlan vni 5010
   [*Device2-bd10] quit
   [*Device2] interface nve 1
   [*Device2-Nve1] source 2001:DB8:2::2
   [*Device2-Nve1] vni 5010 head-end peer-list 2001:DB8:1::1
   [*Device2-Nve1] quit
   [*Device2] bridge-domain 20
   [*Device2-bd20] vxlan vni 5020
   [*Device2-bd20] quit
   [*Device2] interface nve 1
   [*Device2-Nve1] vni 5020 head-end peer-list 2001:DB8:1::1 2001:DB8:3::3
   [*Device2-Nve1] quit
   [*Device2] commit
   ```
   
   # Configure Device3.
   
   ```
   [~Device3] bridge-domain 20
   [~Device3-bd20] vxlan vni 5020
   [*Device3-bd20] quit
   [*Device3] interface nve 1
   [*Device3-Nve1] source 2001:DB8:3::3
   [*Device3-Nve1] vni 5020 head-end peer-list 2001:DB8:1::1 2001:DB8:2::2
   [*Device3-Nve1] quit
   [*Device3] commit
   ```
4. Configure Device2 as an IPv6 Layer 3 VXLAN gateway.
   
   
   ```
   [~Device2] interface vbdif 10
   [*Device2-Vbdif10] ip address 192.168.10.10 24
   [*Device2-Vbdif10] quit
   [*Device2] interface vbdif 20
   [*Device2-Vbdif20] ip address 192.168.20.10 24
   [*Device2-Vbdif20] quit
   [*Device2] commit
   ```

#### Verifying the Configuration

After completing the configuration, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command to check IPv6 VXLAN tunnel information and run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) command to check the VNI status. The command outputs show that the VNI status is up. The following example uses the command output on Device2.

```
[~Device1] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type     Uptime
----------------------------------------------------------------------------------- 
4026531874  2001:DB8:2::2         2001:DB8:1::1         up     static   0010h21m
4026531875  2001:DB8:2::2         2001:DB8:3::3         up     static   0012h34m
```
```
[~Device2] display vxlan vni
Number of vxlan vni : 2
VNI            BD-ID            State
---------------------------------------
5010           10               up
5020           20               up
```

VM1s on different servers can communicate.


#### Configuration Scripts

* Device1
  
  ```
  #
  sysname Device1
  #
  bridge-domain 10
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 5020
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface 100GE1/0/3.1 mode l2
   encapsulation dot1q vid 30
   bridge-domain 20
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/128
   ospfv3 1 area 0.0.0.0
  #
  interface Nve1
   source 2001:DB8:1::1
   vni 5010 head-end peer-list 2001:DB8:2::2
   vni 5020 head-end peer-list 2001:DB8:2::2 2001:DB8:3::3
  #
  return
  ```
* Device2
  
  ```
  #
  sysname Device2
  #
  bridge-domain 10
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 5020
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface Vbdif10
   ip address 192.168.10.10 255.255.255.0
  #
  interface Vbdif20
   ip address 192.168.20.10 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:5::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::2/128
   ospfv3 1 area 0.0.0.0
  #
  interface Nve1
   source 2001:DB8:2::2
   vni 5010 head-end peer-list 2001:DB8:1::1
   vni 5020 head-end peer-list 2001:DB8:1::1 2001:DB8:3::3
  #
  return
  ```
* Device3
  
  ```
  #
  sysname Device3
  #
  bridge-domain 20
   vxlan vni 5020
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:5::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:3::3/128
   ospfv3 1 area 0.0.0.0
  #
  interface Nve1
   source 2001:DB8:3::3
   vni 5020 head-end peer-list 2001:DB8:1::1 2001:DB8:2::2
  #
  return
  ```