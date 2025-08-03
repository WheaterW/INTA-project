Example for Configuring Users on Different Subnets to Communicate Through a Layer 3 VXLAN Gateway
=================================================================================================

This section provides an example for configuring users on different subnets to communicate through a Layer 3 gateway. To enable such communication, the default gateway address of the users must be the IP address of the Layer 3 gateway's BDIF interface.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363831__fig_dc_vrp_vxlan_cfg_102601), an enterprise has VMs deployed in different DCs. VM1 on Server1 and VM1 on Server2 belong to VLAN 10 and VLAN 20, respectively, and reside on different subnets. To allow VM1s in different DCs to communicate with each other, configure a VXLAN tunnel between Device1 and Device2 and one between Device2 and Device3.

**Figure 1** Network diagram of configuring users on different subnets to communicate through a Layer 3 VXLAN gateway![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/1 and GE0/1/2, respectively.

![](figure/en-us_image_0000002126491049.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on Device1, Device2, and Device3 to allow them to communicate at Layer 3.
2. Configure a service access point on Device1 and Device3 to differentiate service traffic.
3. Configure a VXLAN tunnel on Device1, Device2, and Device3 to forward service traffic.
4. Configure Device2 as a Layer 3 VXLAN gateway to allow users on different subnets to communicate.


#### Data Preparation

To complete the configuration, you need the following data:

* VMs' VLAN IDs (10 and 20)
* IP addresses of interfaces connecting devices
* Interior Gateway Protocol (IGP) running between devices (OSPF in this example)
* BD IDs (10 and 20)
* VNI IDs (5010 and 5020)

#### Procedure

1. Configure a routing protocol.
   
   
   
   Assign an IP address to each interface on Device1, Device2, and Device3 according to [Figure 1](#EN-US_TASK_0172363831__fig_dc_vrp_vxlan_cfg_102601).
   
   # Configure Device1.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device1] interface loopback 1
   ```
   ```
   [*Device1-LoopBack1] ip address 2.2.2.2 32
   ```
   ```
   [*Device1-LoopBack1] quit
   ```
   ```
   [*Device1] interface gigabitethernet 0/1/1
   ```
   ```
   [*Device1-GigabitEthernet0/1/1] ip address 192.168.1.1 24
   ```
   ```
   [*Device1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Device1] ospf
   ```
   ```
   [*Device1-ospf-1] area 0
   ```
   ```
   [*Device1-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*Device1-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   ```
   ```
   [*Device1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*Device1-ospf-1] quit
   ```
   ```
   [*Device1] commit
   ```
   
   The configurations of Device2 and Device3 are similar to the configuration of Device1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363831__section_dc_vrp_vxlan_cfg_102601).
   
   After OSPF is configured, the devices can use OSPF to learn the IP addresses of each other's loopback interfaces and successfully ping each other. The following example shows the command output on Device1 after it pings Device3:
   ```
   [~Device1] ping 4.4.4.4
   ```
   ```
     PING 4.4.4.4: 56  data bytes, press CTRL_C to break
       Reply from 4.4.4.4: bytes=56 Sequence=1 ttl=254 time=5 ms
       Reply from 4.4.4.4: bytes=56 Sequence=2 ttl=254 time=2 ms
       Reply from 4.4.4.4: bytes=56 Sequence=3 ttl=254 time=2 ms
       Reply from 4.4.4.4: bytes=56 Sequence=4 ttl=254 time=3 ms
       Reply from 4.4.4.4: bytes=56 Sequence=5 ttl=254 time=3 ms
   
     --- 4.4.4.4 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/3/5 ms
   ```
2. Configure a service access point on Device1 and Device3.
   
   # Configure Device1.
   ```
   [~Device1] bridge-domain 10
   ```
   ```
   [*Device1-bd10] quit
   ```
   ```
   [*Device1] interface gigabitethernet0/1/2.1 mode l2
   ```
   ```
   [*Device1-GigabitEthernet0/1/2.1] encapsulation dot1q vid 10
   ```
   ```
   [*Device1-GigabitEthernet0/1/2.1] rewrite pop single
   ```
   ```
   [*Device1-GigabitEthernet0/1/2.1] bridge-domain 10
   ```
   ```
   [*Device1-GigabitEthernet0/1/2.1] quit
   ```
   ```
   [*Device1] commit
   ```
   
   The configuration of Device3 is similar to the configuration of Device1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363831__section_dc_vrp_vxlan_cfg_102601).
3. Configure VXLAN tunnels on Device1, Device2, and Device3.
   
   
   ```
   [~Device1] bridge-domain 10
   ```
   ```
   [*Device1-bd10] vxlan vni 5010
   ```
   ```
   [*Device1-bd10] quit
   ```
   ```
   [*Device1] interface nve 1
   ```
   ```
   [*Device1-Nve1] source 2.2.2.2
   ```
   ```
   [*Device1-Nve1] vni 5010 head-end peer-list 3.3.3.3
   ```
   ```
   [*Device1-Nve1] quit
   ```
   ```
   [*Device1] commit
   ```
   # Configure Device2.
   ```
   [~Device2] bridge-domain 10
   ```
   ```
   [*Device2-bd10] vxlan vni 5010
   ```
   ```
   [*Device2-bd10] quit
   ```
   ```
   [*Device2] interface nve 1
   ```
   ```
   [*Device2-Nve1] source 3.3.3.3
   ```
   ```
   [*Device2-Nve1] vni 5010 head-end peer-list 2.2.2.2
   ```
   ```
   [*Device2-Nve1] quit
   ```
   ```
   [~Device2] bridge-domain 20
   ```
   ```
   [*Device2-bd20] vxlan vni 5020
   ```
   ```
   [*Device2-bd20] quit
   ```
   ```
   [*Device2] interface nve 1
   ```
   ```
   [*Device2-Nve1] vni 5020 head-end peer-list 4.4.4.4
   ```
   ```
   [*Device2-Nve1] quit
   ```
   ```
   [*Device2] commit
   ```
   
   # Configure Device3.
   ```
   [~Device3] bridge-domain 20
   ```
   ```
   [*Device3-bd20] vxlan vni 5020
   ```
   ```
   [*Device3-bd20] quit
   ```
   ```
   [*Device3] interface nve 1
   ```
   ```
   [*Device3-Nve1] source 4.4.4.4
   ```
   ```
   [*Device3-Nve1] vni 5020 head-end peer-list 3.3.3.3
   ```
   ```
   [*Device3-Nve1] quit
   ```
   ```
   [*Device3] commit
   ```
4. Configure Device2 as a Layer 3 VXLAN gateway.
   
   
   ```
   [~Device2] interface vbdif 10
   ```
   ```
   [*Device2-Vbdif10] ip address 192.168.10.10 24
   ```
   ```
   [*Device2-Vbdif10] quit
   ```
   ```
   [*Device2] interface vbdif 20
   ```
   ```
   [*Device2-Vbdif20] ip address 192.168.20.10 24
   ```
   ```
   [*Device2-Vbdif20] quit
   ```
   ```
   [*Device2-Vbdif20] commit
   ```
5. Verify the configuration.
   
   
   
   After the configuration is complete, run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) and [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) commands on Device1, Device2, and Device3 to check the VNI status and VXLAN tunnel information, respectively. The VNIs are Up on Device1, Device2, and Device3. The following example shows the command output on Device2.
   
   ```
   [~Device2] display vxlan vni
   ```
   ```
   Number of vxlan vni: 2
   VNI            BD-ID            State
   ---------------------------------------
   5010           10               up
   5020           20               up
   ```
   ```
   [~Device2] display vxlan tunnel
   ```
   ```
   Number of Vxlan tunnel : 2
   Tunnel ID   Source           Destination        State  Type    Uptime
   ---------------------------------------------------------------------
   4026531841  3.3.3.3          2.2.2.2            up     static 0029h30m
   4026531842  3.3.3.3          4.4.4.4            up     static 0029h44m
   ```
   
   Configure 192.168.10.10/24 as the default gateway IP address of VM1 in VLAN 10 on Server1.
   
   Configure 192.168.20.10/24 as the default gateway IP address of VM1 in VLAN 20 on Server2.
   
   After the configuration is complete, VM1s on different subnets can communicate with each other. In addition, to enable Device1 and Device3 to communicate on the overlay network, configure static routes or an IGP to advertise routes to 192.168.10.0/24 and 192.168.20.0/24 to each other. The next hop is the VBDIF interface address on Device2.

#### Configuration Files

* Device1 configuration file
  
  ```
  #
  sysname Device1
  #
  bridge-domain 10
   vxlan vni 5010
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 5010 head-end peer-list 3.3.3.3
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* Device2 configuration file
  
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
  interface Vbdif10
   ip address 192.168.10.10 255.255.255.0
  #
  interface Vbdif20
   ip address 192.168.20.10 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3
   vni 5010 head-end peer-list 2.2.2.2
   vni 5020 head-end peer-list 4.4.4.4
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* Device3 configuration file
  
  ```
  #
  sysname Device3
  #
  bridge-domain 20
   vxlan vni 5020
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  interface Nve1
   source 4.4.4.4
   vni 5020 head-end peer-list 3.3.3.3
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  return
  ```