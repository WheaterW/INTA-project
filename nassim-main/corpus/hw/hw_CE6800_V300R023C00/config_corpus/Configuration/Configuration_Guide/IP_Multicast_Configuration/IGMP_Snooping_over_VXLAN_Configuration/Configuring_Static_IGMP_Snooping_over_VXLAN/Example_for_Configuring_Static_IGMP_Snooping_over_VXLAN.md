Example for Configuring Static IGMP Snooping over VXLAN
=======================================================

Example for Configuring Static IGMP Snooping over VXLAN

#### Networking Requirements

On a VXLAN network, static IGMP snooping over VXLAN allows forwarding paths to be manually specified for multicast traffic, ensuring that downstream users can continuously and stably receive multicast traffic while also preventing multicast traffic flooding in the BD.

On the network shown in [Figure 1](#EN-US_TASK_0000001200723013__fig_dc_cfg_igmp_snp_014001), an enterprise has VMs deployed on different servers. VM1s on Server1, Server2, and Server3 belong to VLAN 10. The VMs on Server1 are multicast sources. The VMs on Server2 want to continuously receive traffic from multicast group 255.0.0.0, and the VMs on Server3 want to continuously receive traffic from multicast group 255.0.0.1. Static IGMP snooping over VXLAN needs to be configured to implement continuous traffic forwarding.

**Figure 1** Networking diagram for configuring static IGMP snooping over VXLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001172481782.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on DeviceA, DeviceB, and DeviceC to ensure Layer 3 interworking.
2. Configure a VXLAN service access point on DeviceA, DeviceB, and DeviceC to distinguish service traffic.
3. Configure static VXLAN tunnels on DeviceA, DeviceB, and DeviceC.
4. Enable IGMP snooping globally and in the BD on all service access points on DeviceA, DeviceB, and DeviceC to implement Layer 2 multicast on the VXLAN network.
5. Enable IGMP snooping proxy globally and in the BD on all service access points on DeviceA, DeviceB, and DeviceC. Configure the transmit end DeviceA to periodically send Query messages to collect join information, and configure the receive ends DeviceB and DeviceC to reply with join information based on static entries.
6. On DeviceB and DeviceC, configure static forwarding entries in which the outbound interfaces are downstream VMs.
7. Disable DeviceA from dynamically learning multicast group member ports. This prevents DeviceA from generating unnecessary dynamic router ports after receiving IGMP Query messages from downstream devices, which would otherwise cause redundant traffic forwarding.



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
   [*DeviceA-100GE1/0/1] ip address 192.168.2.2 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255 
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.3.0 0.0.0.255 
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure service access points.
   
   
   
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
3. Configure static VXLAN tunnels.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface nve 1
   [*DeviceA-Nve1] source 1.1.1.1
   [*DeviceA-Nve1] vni 10 head-end peer-list 2.2.2.2 3.3.3.3
   [*DeviceA-Nve1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
4. Enable IGMP snooping globally and in the BD.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] igmp snooping enable
   [*DeviceA] bridge-domain 10
   [*DeviceA-bd10] igmp snooping enable
   [*DeviceA-bd10] quit
   [*DeviceA] commit
   ```
   
   
   
   The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
5. Configure IGMP snooping proxy.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bridge-domain 10
   [*DeviceA-bd10] igmp snooping proxy
   [*DeviceA-bd10] quit
   [*DeviceA] commit 
   ```
   
   The configurations of DeviceB and DeviceC are similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
6. Configure static Layer 2 multicast entries.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/2.1 mode l2  
   [*DeviceB-100GE1/0/2.1] igmp snooping static-group group-address 225.0.0.0 dot1q vid 10  
   [*DeviceB-100GE1/0/2.1] quit 
   [*DeviceB] commit
   ```
   
   The configuration of DeviceC is similar to that of DeviceB. For detailed configurations, see Configuration Scripts.
7. Disable the transmit end from automatically learning router ports.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bridge-domain 10 
   [*DeviceA-bd10] igmp snooping router-learning disable  
   [*DeviceA-bd10] quit 
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display VXLAN tunnel information.

```
[~DeviceA] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531841  1.1.1.1               2.2.2.2               up     dynamic  02:14:45
4026531842  1.1.1.1               3.3.3.3               up     dynamic  02:09:42
```

# Display router port information on a receive end.

```
[~DeviceB] display igmp snooping router-port
 Port Name                            UpTime        Expires       Flags
 --------------------------------------------------------------------------
 Bridge-domain 1, 1 router-port(s)
 vxlan-peer(1.1.1.1)                  02h15m42s     00h02m32s     DYNAMIC
```

The command output shows that a dynamic router port pointing to DeviceA has been generated on DeviceB.

# Display information about multicast group member ports on the transmit end.

```
[~DeviceA] display igmp snooping port-info bridge-domain 10 verbose 
The port information of Group 225.0.0.0 on Bridge-domain 10:
  Time of this group has been up : 02:13:13

  The port information of (*, 225.0.0.0):
    Time of this source has been up : 02:13:13
    Port Table on this source(*):
    Source flags: IGMP
    List of ports in include mode : 
      No.1 
        Port name : vxlan-peer(2.2.2.2) 
        Time of this port has been up as a host-port : 02:13:14 
        Remain time of port expire as dynamic host-port : -- 
        Host-port flags : Dynamic 
    There are 1 port(s) in include mode. 
The port information of Group 225.0.0.1 on Bridge-domain 10: 
  Time of this group has been up : 02:13:12 
 
  The port information of (*, 225.0.0.1): 
    Time of this source has been up : 02:13:12 
    Port Table on this source(*): 
    Source flags: IGMP 
    List of ports in include mode : 
      No.1 
        Port name : vxlan-peer(3.3.3.3) 
        Time of this port has been up as a host-port : 02:13:12 
        Remain time of port expire as dynamic host-port : -- 
        Host-port flags : Dynamic 
    There are 1 port(s) in include mode.
```

The command output on DeviceA shows that the dynamic member port **vxlan-peer(2.2.2.2)** has been generated for the traffic of the multicast group 225.0.0.0 to be sent to DeviceB, and the dynamic member port **vxlan-peer(3.3.3.3)** has been generated for the traffic of the multicast group 225.0.0.1 to be sent to DeviceC.

# Display information about multicast group member ports on a receiver end.

```
[~DeviceB] display igmp snooping port-info bridge-domain 10 verbose  
The port information of Group 225.0.0.0 on Bridge-domain 10: 
  Time of this group has been up : 02:21:15 
 
  The port information of (*, 225.0.0.0): 
    Time of this source has been up : 02:21:15 
    Port Table on this source(*): 
    Source flags: IGMP 
    List of ports in include mode : 
      No.1 
        Port name : 100GE1/0/2.1(PE:10) 
        Time of this port has been up as a host-port : 02:21:15 
        Remain time of port expire as dynamic host-port : -- 
        Host-port flags : Static 
    There are 1 port(s) in include mode.
```

The command output shows that the Layer 2 sub-interface 100GE1/0/2.1 on DeviceB has been statically added to multicast group 225.0.0.0 and works as a static member port.


#### Configuration Scripts

* DeviceA
  ```
  # 
  sysname DeviceA  
  # 
  igmp snooping enable 
  # 
  bridge-domain 10
   vxlan vni 10
   igmp snooping enable
   igmp snooping router-learning disable
   igmp snooping proxy
  # 
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  # 
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
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
   vni 10 head-end peer-list 2.2.2.2
   vni 10 head-end peer-list 3.3.3.3
  # 
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.2.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
  # 
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  igmp snooping enable
  # 
  bridge-domain 10
   vxlan vni 10
   igmp snooping enable
   igmp snooping proxy
  # 
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  # 
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   igmp snooping static-group group-address 225.0.0.0 dot1q vid 10
  # 
  interface LoopBack0 
    ip address 2.2.2.2 255.255.255.255 
  # 
  interface Nve1
   source 2.2.2.2
   vni 10 head-end peer-list 1.1.1.1
  # 
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.2.0 0.0.0.255
  # 
  return
  ```
* DeviceC
  
  ```
  # 
  sysname DeviceC  
  # 
  igmp snooping enable 
  # 
  bridge-domain 10
   vxlan vni 10
   igmp snooping enable
   igmp snooping proxy
  # 
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  # 
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   igmp snooping static-group group-address 225.0.0.1 dot1q vid 10
  # 
  interface LoopBack0 
    ip address 3.3.3.3 255.255.255.255 
  # 
   interface Nve1
   source 3.3.3.3
   vni 10 head-end peer-list 1.1.1.1 
  # 
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.3.0 0.0.0.255
  # 
  return
  ```