Example for Configuring Multicast Replication for BUM Packets
=============================================================

Example for Configuring Multicast Replication for BUM Packets

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001214973548__fig_dc_cfg_vxlan_cfgcase_001501), an enterprise has VMs deployed in multiple data centers. The servers where the VMs reside all belong to VLAN 10, and VXLAN tunnels need to be deployed to enable these VMs to communicate with each other. Device1 and Device3 function as Layer 2 VXLAN gateways, Device2 functions as a Layer 3 VXLAN gateway, and Device4 is a non-gateway node on the VXLAN network. When the VMs communicate with each other, Layer 2 gateways are used to forward traffic. When the VMs need to access an external network, the Layer 3 gateway is used to forward traffic.

To reduce traffic flooding caused by BUM packet forwarding, configure multicast replication. Device 4 can function as a static multicast RP.

**Figure 1** Configuring multicast replication for BUM packets on a VXLAN network![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 to 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001215454980.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on the involved devices to ensure Layer 3 connectivity.
2. Configure service access points on Device1 and Device3 to differentiate service traffic.
3. Configure VXLAN tunnels on Device1, Device2, and Device3.
4. Configure Device2 as a Layer 3 VXLAN gateway to allow the VMs to access the external network.
5. Configure PIM-SM on the involved devices and configure Device4 as a static RP.
6. Enable multicast replication on Device1, Device2, and Device3.


#### Procedure

1. Configure interface IP addresses on devices.
   
   
   
   Configure IP addresses for interfaces on the involved devices according to [Figure 1](#EN-US_TASK_0000001214973548__fig_dc_cfg_vxlan_cfgcase_001501).
2. Configure BGP EVPN to establish VXLAN tunnels.
   
   
   
   For details about the configuration method, see [Example for Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](../dc/dc_cfg_vxlan_cfgcase_0002.html). For detailed configurations, see Configuration Scripts.
3. Configure PIM-SM on the involved devices and configure Device4 as a static RP.
   
   # Configure Device1.
   ```
   [~Device1] multicast routing-enable
   [*Device1] pim
   [*Device1-pim] static-rp 4.4.4.4
   [*Device1-pim] quit
   [*Device1] interface 100ge 1/0/1
   [*Device1-100GE1/0/1] pim sm
   [*Device1-100GE1/0/1] quit
   [*Device1] commit
   ```
   
   # Configure Device2.
   ```
   [~Device2] multicast routing-enable
   [*Device2] pim
   [*Device2-pim] static-rp 4.4.4.4
   [*Device2-pim] quit
   [*Device2] interface 100ge 1/0/1
   [*Device2-100GE1/0/1] pim sm
   [*Device2-100GE1/0/1] quit
   [*Device2] commit
   ```
   
   # Configure Device3.
   ```
   [~Device3] multicast routing-enable
   [*Device3] pim
   [*Device3-pim] static-rp 4.4.4.4
   [*Device3-pim] quit
   [*Device3] interface 100ge 1/0/1
   [*Device3-100GE1/0/1] pim sm
   [*Device3-100GE1/0/1] quit
   [*Device3] commit
   ```
   
   # Configure Device4.
   ```
   [~Device4] multicast routing-enable
   [*Device4] pim
   [*Device4-pim] static-rp 4.4.4.4
   [*Device4-pim] quit
   [*Device4] interface 100ge 1/0/1
   [*Device4-100GE1/0/1] pim sm
   [*Device4-100GE1/0/1] quit
   [*Device4] interface 100ge 1/0/2
   [*Device4-100GE1/0/2] pim sm
   [*Device4-100GE1/0/2] quit
   [*Device4] interface 100ge 1/0/3
   [*Device4-100GE1/0/3] pim sm
   [*Device4-100GE1/0/3] quit
   [*Device4] commit
   ```
4. Enable multicast replication on Device1, Device2, and Device3.
   
   # Configure Device1.
   ```
   [~Device1] interface nve 1
   [*Device1-Nve1] vni 100 mcast-group 225.0.0.1
   [*Device1-Nve1] quit
   [*Device1] commit
   ```
   
   # Configure Device2.
   ```
   [~Device2] interface nve 1
   [*Device2-Nve1] vni 100 mcast-group 225.0.0.1
   [*Device2-Nve1] quit
   [*Device2] commit
   ```
   
   # Configure Device3.
   ```
   [~Device3] interface nve 1
   [*Device3-Nve1] vni 100 mcast-group 225.0.0.1
   [*Device3-Nve1] quit
   [*Device3] commit
   ```

#### Verifying the Configuration

After completing the configurations, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on Device1, Device2, and Device3 to check VXLAN tunnel information, including the VXLAN tunnel whose destination address is a multicast replication address. The command output shows that the status of all VXLAN tunnels is up. The following example uses the command output on Device1.

```
[~Device1] display vxlan tunnel
```
```
Number of vxlan tunnel : 3
Tunnel ID   Source                Destination           State  Type     Uptime
-----------------------------------------------------------------------------------
4026531845  1.1.1.1               2.2.2.2               up     dynamic  00:10:17
4026531846  1.1.1.1               3.3.3.3               up     dynamic  00:10:13
4026531847  1.1.1.1               225.0.0.1             up     static   00:07:56
```

After completing the configurations, run the [**display vxlan vni 100 verbose**](cmdqueryname=display+vxlan+vni+100+verbose) command on Device1, Device2, and Device3 to check the detailed configuration of the VXLAN whose VNI is 100. The command output shows that the BUM mode is multicast replication. The following example uses the command output on Device1.

```
[~Device1] display vxlan vni 100 verbose
```
```
    BD ID                  : 10
    State                  : up
    NVE                    : 64
    Source Address         : 1.1.1.1
    Source IPv6 Address    : -
    UDP Port               : 4789
    BUM Mode               : multicast replication
    Group Address          : 225.0.0.1
```

#### Configuration Scripts

* Device1
  
  ```
  #
  sysname Device1
  #
  evpn-overlay enable
  #
  multicast routing-enable
  #
  bridge-domain 10
   vxlan vni 100
   #
   evpn 
    route-distinguisher 10:1
    vpn-target 100:100 export-extcommunity
    vpn-target 100:100 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1 
   vni 100 mcast-group 225.0.0.1
   vni 100 head-end peer-list protocol bgp
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
    network 10.1.1.0 0.0.0.255
  #               
  pim             
   static-rp 4.4.4.4
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
  multicast routing-enable
  #
  bridge-domain 10
   vxlan vni 100
   #
   evpn 
    route-distinguisher 10:2
    vpn-target 100:100 export-extcommunity
    vpn-target 100:100 import-extcommunity
  #
  interface Vbdif10
   ip address 192.168.10.1 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  interface Nve1
   source 2.2.2.2
   vni 100 mcast-group 225.0.0.1 
   vni 100 head-end peer-list protocol bgp
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
    network 10.1.2.0 0.0.0.255
  #               
  pim             
   static-rp 4.4.4.4
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
  multicast routing-enable
  #
  bridge-domain 10
   vxlan vni 100
   #
   evpn 
    route-distinguisher 10:3
    vpn-target 100:100 export-extcommunity
    vpn-target 100:100 import-extcommunity
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3 
   vni 100 mcast-group 225.0.0.1
   vni 100 head-end peer-list protocol bgp
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
    network 10.1.3.0 0.0.0.255
  #               
  pim             
   static-rp 4.4.4.4
  #
  return
  ```
* Device4
  ```
  #
  sysname Device4
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.3.2 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1          
   area 0.0.0.0   
    network 4.4.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #               
  pim             
   static-rp 4.4.4.4
  #
  return
  ```