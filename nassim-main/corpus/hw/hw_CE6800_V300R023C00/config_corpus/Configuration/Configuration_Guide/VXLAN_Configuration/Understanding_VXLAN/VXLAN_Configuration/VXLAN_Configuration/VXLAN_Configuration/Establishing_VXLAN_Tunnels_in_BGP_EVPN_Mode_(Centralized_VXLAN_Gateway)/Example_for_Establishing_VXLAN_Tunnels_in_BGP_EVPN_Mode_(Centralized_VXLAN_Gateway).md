Example for Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)
===================================================================================

Example for Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001130784308__fig_dc_cfg_vxlan_cfgcase_000201), an enterprise has VMs deployed in different data centers. VM1 on Server1 (Server1 VM1 for short) belongs to VLAN 10, Server2 VM1 belongs to VLAN 20, and Server3 VM1 belongs to VLAN 30. Server1 and Server2 reside on different network segments, and Server3 and Server2 reside on the same network segment. Server1 VM1, Server3 VM1, and Server2 VM1 need to communicate with each other through a Layer 3 VXLAN gateway.

**Figure 1** Networking for configuring VXLAN in centralized gateway mode for dynamic tunnel establishment![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 to 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001176743999.png)

#### Precautions

If M-LAG is used for Layer 3 gateway access, you need to configure a bypass VXLAN tunnel and enable ARP route advertisement.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on Device1, Device2, and Device3 to ensure Layer 3 connectivity on the network.
2. Configure service access points on Device1 and Device3 to distinguish service traffic.
3. Enable EVPN to function as the VXLAN control plane.
4. Configure BGP EVPN peer relationships.
5. Configure EVPN instances.
6. Configure ingress replication.
7. Configure Device2 as a Layer 3 VXLAN gateway.



#### Procedure

1. Configure a routing protocol.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1. If OSPF is used, ensure that 32-bit loopback interface addresses are advertised.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] interface loopback 1
   [*Device1-LoopBack1] ip address 1.1.1.1 32
   [*Device1-LoopBack1] quit
   [*Device1] interface 100ge 1/0/1
   [*Device1-100GE1/0/1] undo portswitch
   [*Device1-100GE1/0/1] ip address 192.168.1.1 24
   [*Device1-100GE1/0/1] quit
   [*Device1] ospf
   [*Device1-ospf-1] area 0
   [*Device1-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   [*Device1-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*Device1-ospf-1-area-0.0.0.0] quit
   [*Device1-ospf-1] quit
   [*Device1] commit
   ```
   
   # After OSPF is configured, the devices can learn each other's loopback interface IP address and successfully ping one another. The following example shows the command output on Device1 after it pings Device3.
   
   ```
   [~Device1] ping 3.3.3.3
     PING 3.3.3.3: 56  data bytes, press CTRL_C to break
       Reply from 3.3.3.3: bytes=56 Sequence=1 ttl=253 time=5 ms
       Reply from 3.3.3.3: bytes=56 Sequence=2 ttl=253 time=2 ms
       Reply from 3.3.3.3: bytes=56 Sequence=3 ttl=253 time=2 ms
       Reply from 3.3.3.3: bytes=56 Sequence=4 ttl=253 time=3 ms
       Reply from 3.3.3.3: bytes=56 Sequence=5 ttl=253 time=3 ms
   
     --- 3.3.3.3 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/3/5 ms
   ```
2. Configure service access points on Device1 and Device3.
   
   
   
   # Configure Device1.
   
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
   
   # Configure Device3.
   
   ```
   [~Device3] bridge-domain 20
   [*Device3-bd20] quit
   [*Device3] interface 100ge 1/0/2.1 mode l2
   [*Device3-100GE1/0/2.1] encapsulation dot1q vid 20
   [*Device3-100GE1/0/2.1] bridge-domain 20
   [*Device3-100GE1/0/2.1] quit
   [*Device3] commit
   ```
3. Enable EVPN to function as the VXLAN control plane protocol on Device1, Device2, and Device3.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   [~Device1] evpn-overlay enable
   [*Device1] commit
   ```
4. Configure BGP EVPN peer relationships.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   [~Device1] bgp 100
   [*Device1-bgp] peer 2.2.2.2 as-number 100
   [*Device1-bgp] peer 2.2.2.2 connect-interface LoopBack1
   [*Device1-bgp] peer 3.3.3.3 as-number 100
   [*Device1-bgp] peer 3.3.3.3 connect-interface LoopBack1
   [*Device1-bgp] l2vpn-family evpn
   [*Device1-bgp-af-evpn] peer 2.2.2.2 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   [*Device1-bgp-af-evpn] peer 3.3.3.3 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]:y
   [*Device1-bgp-af-evpn] quit
   [*Device1-bgp] quit
   [*Device1] commit
   ```
5. Configure EVPN instances on Device1, Device2, and Device3.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   [~Device1] bridge-domain 10
   [~Device1-bd10] vxlan vni 5010
   [*Device1-bd10] evpn
   [*Device1-bd10-evpn] route-distinguisher 10:11
   [*Device1-bd10-evpn] vpn-target 100:5010
   [*Device1-bd10-evpn] quit
   [*Device1-bd10] quit
   [*Device1] bridge-domain 20
   [*Device1-bd20] vxlan vni 5020
   [*Device1-bd20] evpn
   [*Device1-bd20-evpn] route-distinguisher 10:12
   [*Device1-bd20-evpn] vpn-target 100:5020
   [*Device1-bd20-evpn] quit
   [*Device1-bd20] quit
   [*Device1] commit
   ```
6. Configure ingress replication.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   [~Device1] interface nve 1
   [*Device1-Nve1] source 1.1.1.1
   [*Device1-Nve1] vni 5010 head-end peer-list protocol bgp
   [*Device1-Nve1] vni 5020 head-end peer-list protocol bgp
   [*Device1-Nve1] quit
   [*Device1] commit
   ```
7. Configure Device2 as a Layer 3 VXLAN gateway.
   
   
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

After completing the configuration, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command to check VXLAN tunnel information, and run the [**display vxlan vni**](cmdqueryname=display+vxlan+vni) command on Device1, Device2, and Device3 to check whether the VNI state is up. The following example uses the command output on Device1.

```
[~Device1] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531843  1.1.1.1               2.2.2.2               up     dynamic  0035h21m
4026531844  1.1.1.1               3.3.3.3               up     dynamic  0036h21m
```
```
[~Device1] display vxlan vni
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
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 5010
   #
   evpn
    route-distinguisher 10:11
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:5010 import-extcommunity
  #
  bridge-domain 20
   vxlan vni 5020
   #
   evpn
    route-distinguisher 10:12
    vpn-target 100:5020 export-extcommunity
    vpn-target 100:5020 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
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
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1
   vni 5010 head-end peer-list protocol bgp
   vni 5020 head-end peer-list protocol bgp
  #
  bgp 100
   private-4-byte-as enable
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* Device2
  
  ```
  #
  sysname Device2
  #
  evpn-overlay enable
  #
  bridge-domain 10
   vxlan vni 5010
   #
   evpn
    route-distinguisher 10:21
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:5010 import-extcommunity
  #
  bridge-domain 20
   vxlan vni 5020
   #
   evpn
    route-distinguisher 10:22
    vpn-target 100:5020 export-extcommunity
    vpn-target 100:5020 import-extcommunity
  #
  interface Vbdif10
   ip address 192.168.10.10 255.255.255.0
  #
  interface Vbdif20
   ip address 192.168.20.10 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 5010 head-end peer-list protocol bgp
   vni 5020 head-end peer-list protocol bgp
  #
  bgp 100
   private-4-byte-as enable
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* Device3
  
  ```
  #
  sysname Device3
  #
  evpn-overlay enable
  #
  bridge-domain 20
   vxlan vni 5020
   #
   evpn
    route-distinguisher 10:31
    vpn-target 100:5020 export-extcommunity
    vpn-target 100:5020 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3
   vni 5020 head-end peer-list protocol bgp
  #
  bgp 100
   private-4-byte-as enable
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  return
  ```