Example for Configuring Basic IGMP Snooping over VXLAN Functions (Access Through an EVC Sub-interface)
======================================================================================================

Example for Configuring Basic IGMP Snooping over VXLAN Functions (Access Through an EVC Sub-interface)

#### Networking Requirements

On a VXLAN network, IGMP snooping over VXLAN prevents multicast traffic from being flooded in a BD and allows the ingress to forward the multicast traffic based on user requirements.

On the network shown in [Figure 1](#EN-US_TASK_0000001144940416__fig_dc_cfg_igmp_snp_014001), an enterprise has VMs deployed on different servers. VM1 on Server1 and VM1 on Server2 belong to VLAN 10; VM1 on Server3 belongs to VLAN 20. VMs on Server1 are multicast sources, and VMs on Server2 and Server3 are multicast users. It is required that VXLAN and IGMP snooping be configured to allow the VM1 users in different servers to order multicast services provided by the multicast source VM1 on Server1.

**Figure 1** Network diagram of configuring IGMP snooping over VXLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001172640848.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on DeviceA, DeviceB, DeviceC, and DeviceD to ensure Layer 3 interworking.
2. Configure VXLAN service access points in EVC sub-interface access mode on DeviceA, DeviceB, and DeviceC to differentiate service traffic.
3. Configure EVPN as the VXLAN control plane protocol on DeviceA, DeviceB, DeviceC, and DeviceD. Configure DeviceD as an RR, and establish a BGP EVPN peer relationship between it and each of the other devices. Configure an EVPN instance and ingress replication on DeviceA, DeviceB, and DeviceC so that a VXLAN tunnel is established between DeviceA and DeviceB and between DeviceA and DeviceC.
4. Enable IGMP snooping globally and in the BD on all service access points (DeviceA, DeviceB, and DeviceC), and configure DeviceA as an IGMP snooping querier to implement Layer 2 multicast on the VXLAN network.



#### Procedure

1. Configure a routing protocol.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] ip address 1.1.1.1 32
   [*DeviceA-LoopBack0] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] bgp 100
   [*DeviceA-bgp] peer 192.168.1.2 as-number 400
   [*DeviceA-bgp] network 1.1.1.1 32
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure service access points in EVC sub-interface access mode.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bridge-domain 10
   [*DeviceA-bd10] quit
   [*DeviceA] interface 100ge 1/0/2.1 mode l2
   [*DeviceA-100GE1/0/2.1] encapsulation dot1q vid 10
   [*DeviceA-100GE1/0/2.1] bridge-domain 10
   [*DeviceA-100GE1/0/2.1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
3. Configure VXLAN tunnels.
   1. Configure EVPN as the VXLAN control plane protocol.
      
      
      
      # Configure DeviceA.
      
      ```
      [~DeviceA] evpn-overlay enable
      [*DeviceA] commit
      ```
      
      The configurations of DeviceB, DeviceC, and DeviceD are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
   2. Configure DeviceD to establish BGP EVPN peer relationships with DeviceA, DeviceB, and DeviceC. Configure DeviceD as an RR, and specify DeviceA, DeviceB, and DeviceC as its clients.
      
      # Configure BGP EVPN peer relationships on DeviceD and configure the RR function.
      ```
      [~DeviceD] bgp 100 instance evpn1
      [*DeviceD-bgp-instance-evpn1] peer 1.1.1.1 as-number 100
      [*DeviceD-bgp-instance-evpn1] peer 1.1.1.1 connect-interface LoopBack0
      [*DeviceD-bgp-instance-evpn1] peer 2.2.2.2 as-number 100
      [*DeviceD-bgp-instance-evpn1] peer 2.2.2.2 connect-interface LoopBack0
      [*DeviceD-bgp-instance-evpn1] peer 3.3.3.3 as-number 100
      [*DeviceD-bgp-instance-evpn1] peer 3.3.3.3 connect-interface LoopBack0
      [*DeviceD-bgp-instance-evpn1] l2vpn-family evpn
      [*DeviceD-bgp-instance-evpn1-af-evpn] peer 1.1.1.1 enable
      [*DeviceD-bgp-instance-evpn1-af-evpn] peer 1.1.1.1 reflect-client
      [*DeviceD-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 enable
      [*DeviceD-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 reflect-client
      [*DeviceD-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 enable
      [*DeviceD-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 reflect-client
      [*DeviceD-bgp-instance-evpn1-af-evpn] undo policy vpn-target
      [*DeviceD-bgp-instance-evpn1-af-evpn] quit
      [*DeviceD-bgp-instance-evpn1] quit
      [*DeviceD] commit
      ```
   3. Configure DeviceA, DeviceB, and DeviceC to establish BGP EVPN peer relationships with DeviceD.
      
      # Configure a BGP EVPN peer relationship on DeviceA.
      ```
      [~DeviceA] bgp 100 instance evpn1
      [*DeviceA-bgp-instance-evpn1] peer 4.4.4.4 as-number 100
      [*DeviceA-bgp-instance-evpn1] peer 4.4.4.4 connect-interface LoopBack0
      [*DeviceA-bgp-instance-evpn1] l2vpn-family evpn
      [*DeviceA-bgp-instance-evpn1-af-evpn] peer 4.4.4.4 enable
      [*DeviceA-bgp-instance-evpn1-af-evpn] quit
      [*DeviceA-bgp-instance-evpn1] quit
      [*DeviceA] commit
      ```
      
      
      
      The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
   4. Configure an EVPN instance on DeviceA, DeviceB, and DeviceC.
      
      
      
      # Configure DeviceA.
      
      ```
      [~DeviceA] bridge-domain 10
      [*DeviceA-bd10] vxlan vni 10
      [*DeviceA-bd10] evpn
      [*DeviceA-bd10-evpn] route-distinguisher 10:1
      [*DeviceA-bd10-evpn] vpn-target 10:1
      [*DeviceA-bd10-evpn] quit
      [*DeviceA-bd10] quit
      [*DeviceA] commit
      ```
      
      
      
      The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
   5. Enable ingress replication on DeviceA, DeviceB, and DeviceC.
      
      
      
      # Configure DeviceA.
      
      ```
      [~DeviceA] interface nve 1
      [*DeviceA-Nve1] source 1.1.1.1
      [*DeviceA-Nve1] mac-address 00e0-fc12-3456
      [*DeviceA-Nve1] vni 10 head-end peer-list protocol bgp
      [*DeviceA-Nve1] quit
      [*DeviceA] commit
      ```
      
      
      
      The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
4. Enable IGMP snooping globally and in the BD, and configure an IGMP snooping querier on DeviceA.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] igmp snooping enable
   [*DeviceA] bridge-domain 10
   [*DeviceA-bd10] igmp snooping enable
   [*DeviceA-bd10] igmp snooping querier enable
   [*DeviceA-bd10] quit
   [*DeviceA] commit
   ```
   
   
   
   The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.

#### Verifying the Configuration

# Display VXLAN tunnel information.

```
[~DeviceA] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531841  1.1.1.1               2.2.2.2               up     dynamic  00:14:45
4026531842  1.1.1.1               3.3.3.3               up     dynamic  00:09:42
```

# Display multicast member port information.

```
[~DeviceC] display igmp snooping port-info bridge-domain 10 verbose 
The port information of Group 235.1.1.1 on Bridge-domain 10:
  Time of this group has been up : 00:01:34

  The port information of (*, 235.1.1.1):
    Time of this source has been up : 00:01:34
    Port Table on this source(*):
    Source flags: IGMP Active
    List of ports in include mode :
      No.1
        Port name : 100GE1/0/2.1(PE:20)
        Time of this port has been up as a host-port : 00:01:35
        Remain time of port expire as dynamic host-port : --
        Host-port flags : Dynamic
      No.2
        Port name : vxlan-peer(1.1.1.1)
        Time of this port has been up as a host-port : 00:01:36
        Remain time of port expire as dynamic host-port : --
        Host-port flags : Dynamic
      No.3
        Port name : vxlan-peer(2.2.2.2)
        Time of this port has been up as a host-port : 00:01:35
        Remain time of port expire as dynamic host-port : --
        Host-port flags : Dynamic
    There are 3 port(s) in include mode.
```

The command output shows that dynamic member ports 100GE1/0/2.1, vxlan-peer (1.1.1.1), and vxlan-peer (2.2.2.2) have been generated for multicast group 235.1.1.1 on DeviceC. The VMs on Server3 can order multicast traffic sent by the VMs on Server1.


#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  evpn-overlay enable
  #
  igmp snooping enable
  #
  bridge-domain 10
   vxlan vni 10
   evpn
    route-distinguisher 10:1
    vpn-target 10:1 export-extcommunity
    vpn-target 10:1 import-extcommunity
   igmp snooping enable
   igmp snooping querier enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1
   vni 10 head-end peer-list protocol bgp
   mac-address 00e0-fc12-3456
  #
  bgp 100
   peer 192.168.1.2 as-number 400
   #
   ipv4-family unicast
    network 1.1.1.1 255.255.255.255
    peer 192.168.1.2 enable
  #
  bgp 100 instance evpn1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   #
   l2vpn-family evpn
    policy vpn-target
    peer 4.4.4.4 enable
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  evpn-overlay enable
  #
  igmp snooping enable
  #
  bridge-domain 10
   vxlan vni 10
   evpn
    route-distinguisher 40:1
    vpn-target 10:1 export-extcommunity
    vpn-target 10:1 import-extcommunity
   igmp snooping enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 10 head-end peer-list protocol bgp
   mac-address 00e0-fc12-3456
  #
  bgp 200
   peer 192.168.2.2 as-number 400
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    peer 192.168.2.2 enable
  #
  bgp 100 instance evpn1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   #
   l2vpn-family evpn
    policy vpn-target
    peer 4.4.4.4 enable
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  evpn-overlay enable
  #
  igmp snooping enable
  #
  bridge-domain 10
   vxlan vni 10
   evpn
    route-distinguisher 20:1
    vpn-target 20:1 export-extcommunity
    vpn-target 20:1 import-extcommunity
   igmp snooping enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 10
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3
   vni 10 head-end peer-list protocol bgp
   mac-address 00e0-fc12-3456
  #
  bgp 300
   peer 192.168.3.2 as-number 400
   #
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    peer 192.168.3.2 enable
  #
  bgp 100 instance evpn1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   #
   l2vpn-family evpn
    policy vpn-target
    peer 4.4.4.4 enable
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  evpn-overlay enable
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
   ip address 192.168.3.2 255.255.255.0
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 400
   peer 192.168.1.1 as-number 100
   peer 192.168.2.1 as-number 200
   peer 192.168.3.1 as-number 300
   #
   ipv4-family unicast
    network 4.4.4.4 255.255.255.255
    peer 192.168.2.1 enable
    peer 192.168.3.1 enable
    peer 192.168.1.1 enable
  #
  bgp 100 instance evpn1
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
  #
  return
  ```