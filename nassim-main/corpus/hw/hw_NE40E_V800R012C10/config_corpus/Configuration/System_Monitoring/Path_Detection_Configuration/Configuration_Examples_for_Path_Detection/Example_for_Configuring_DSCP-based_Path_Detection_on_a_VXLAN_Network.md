Example for Configuring DSCP-based Path Detection on a VXLAN Network
====================================================================

This section uses an IPv4 NFVI distributed gateway as an example to describe how to implement DSCP-based path detection on a VXLAN network.

#### Networking Requirements

The NFVI telco cloud solution is based on Data Center Interconnect (DCI) + data center network (DCN) networking, as shown in [Figure 1](#EN-US_TASK_0253270076__fig_01).

* DCGWs are the DCN's border gateways and can exchange Internet routes with the external network.
* L2GW/L3GW1 and L2GW/L3GW2 access the virtualized network functions (VNFs).
* VNF1 and VNF2 can be deployed as virtualized NEs to implement the vUGW and vMSE functions and connect to L2GW/L3GW1 and L2GW/L3GW2 through the interface processing unit (IPU).

Assume that the detected path is DCGW2 -> L2GW/L3GW2 -> VNF2. DSCP-based IPv4 path detection is enabled on all devices along the path, and a detection packet is constructed and forwarded on DCGW2 (ingress).

Generally, the NE40E is used as the DCGW for path detection.

**Figure 1** Configuring DSCP-based path detection in IPv4 NFVI distributed gateway networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE0/1/1, GE0/1/2, GE0/1/3, GE0/1/4, and GE0/1/5, respectively.


  
![](figure/en-us_image_0253408691.png)

**Table 1** IP addresses of interfaces
| Device Name | Interface | IP Address |
| --- | --- | --- |
| DCGW1 | GigabitEthernet 0/1/1 | 10.6.1.1/24 |
| GigabitEthernet 0/1/2 | 10.6.2.1/24 |
| GigabitEthernet0/1/3 | - |
| LoopBack0 | 9.9.9.9/32 |
| LoopBack1 | 3.3.3.3/32 |
| LoopBack2 | 33.33.33.33/32 |
| DCGW2 | GigabitEthernet 0/1/1 | 10.6.1.2/24 |
| GigabitEthernet 0/1/2 | 10.6.3.1/24 |
| GigabitEthernet0/1/3 | - |
| LoopBack0 | 9.9.9.9/32 |
| LoopBack1 | 4.4.4.4/32 |
| LoopBack2 | 44.44.44.44/32 |
| L2GW/L3GW1 | GigabitEthernet 0/1/1 | 10.6.4.1/24 |
| GigabitEthernet 0/1/2 | 10.6.2.2/24 |
| GigabitEthernet 0/1/3 | - |
| GigabitEthernet 0/1/4 | - |
| GigabitEthernet 0/1/5 | - |
| LoopBack1 | 1.1.1.1/32 |
| L2GW/L3GW2 | GigabitEthernet 0/1/1 | 10.6.4.2/24 |
| GigabitEthernet 0/1/2 | 10.6.3.2/24 |
| GigabitEthernet 0/1/3 | - |
| GigabitEthernet 0/1/4 | - |
| LoopBack1 | 2.2.2.2/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each device interface, including the loopback interfaces.
2. Configure a routing protocol on each DCGW and each L2GW/L3GW to ensure Layer 3 communication. OSPF is used in this example.
3. Configure IPv4 NFVI distributed gateway networking on DCGWs and L2GWs/L3GWs.
4. Configure DSCP-based IPv4 path detection on DCGW2 and L2GW/L3GW2.
5. Configure DCGW2 to construct and forward IPv4 detection packets.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before the configuration, ensure that a NETCONF connection has been established between the controller and device.



#### Procedure

1. Assign an IP address to each device interface, including the loopback interfaces.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0253270076__dc_vrp_evpn_cfg_010701).
2. Configure a routing protocol on each DCGW and each L2GW/L3GW to ensure Layer 3 communication. OSPF is used in this example.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0253270076__dc_vrp_evpn_cfg_010701).
3. Configure IPv4 NFVI distributed gateway networking on DCGWs and L2GWs/L3GWs.
   
   
   
   For the configuration roadmap, see [VXLAN Configuration](../vrp/dc_vrp_vxlan_cfg_1082.html). For configuration details, see [Configuration Files](#EN-US_TASK_0253270076__dc_vrp_evpn_cfg_010701).
4. Configure DSCP-based IPv4 path detection on DCGW2 and L2GW/L3GW2.
   
   
   
   # Configure DCGW2.
   
   ```
   [~DCGW2] ip path detection enable dscp 3
   ```
   
   # Configure L2GW/L3GW2.
   
   ```
   [~L2GW/L3GW2] ip path detection enable dscp 3
   ```
5. Configure DCGW2 to construct and forward IPv4 detection packets.
   
   
   ```
   [*DCGW2] ip path detection send-packet src-mac 00e0-fc12-3456 dst-mac 00e0-fc12-7890 pe-vlan 10 src-ip 10.1.1.1 dst-ip 10.2.2.2 protocol udp src-port 1000 dst-port 2000 dscp 3 vpn-instance vpn1 interface GigabitEthernet0/1/3 testid 2
   ```

#### Configuration Files

* DCGW1 configuration file
  
  ```
  #
  sysname DCGW1
  #
  evpn
   bypass-vxlan enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    export route-policy dp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 200  
  #
  bridge-domain 10
   vxlan vni 100 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   vxlan vni 110 split-horizon-mode
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   vxlan vni 120 split-horizon-mode
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   vxlan vni 130 split-horizon-mode
   evpn binding vpn-instance evrf4
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0002
   vxlan anycast-gateway enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   vxlan anycast-gateway enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   vxlan anycast-gateway enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   vxlan anycast-gateway enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.1.1 255.255.255.0 
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.2.1 255.255.255.0
  #
  interface GigabitEthernet0/1/3
   undo shutdown
  #
  interface GigabitEthernet0/1/3.1 mode l2
    encapsulation dot1q vid 20
    rewrite pop single
    bridge-domain 20
  # 
  interface GigabitEthernet0/1/3.2 mode l2
    encapsulation dot1q vid 40
    rewrite pop single
    bridge-domain 40
  #
  interface LoopBack0
   ip address 9.9.9.9 255.255.255.255
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ip address 33.33.33.33 255.255.255.255
  #
  interface Nve1
   source 9.9.9.9
   bypass source 3.3.3.3
   mac-address 00e0-fc00-0009
   vni 100 head-end peer-list protocol bgp
   vni 110 head-end peer-list protocol bgp
   vni 120 head-end peer-list protocol bgp
   vni 130 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0 0
    import-route direct
    maximum load-balancing 16  
    advertise l2vpn evpn
    peer 5.5.5.5 as-number 100
    peer 5.5.5.5 connect-interface LoopBack2
    peer 5.5.5.5 route-policy p1 export
    peer 6.6.6.6 as-number 100
    peer 6.6.6.6 connect-interface LoopBack2
    peer 6.6.6.6 route-policy p1 export
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 capability-advertise add-path both
    peer 1.1.1.1 advertise add-path path-number 16
    peer 1.1.1.1 advertise encap-type vxlan
    peer 2.2.2.2 enable
    peer 2.2.2.2 capability-advertise add-path both
    peer 2.2.2.2 advertise add-path path-number 16
    peer 2.2.2.2 advertise encap-type vxlan
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise encap-type vxlan
    peer 4.4.4.4 route-policy stopuIP export
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 9.9.9.9 0.0.0.0
    network 10.6.1.0 0.0.0.255
    network 10.6.2.0 0.0.0.255
  #
  ip ip-prefix lp index 10 permit 33.33.33.33 32
  ip ip-prefix uIP index 10 permit 10.10.10.10 32
  #
  route-policy dp permit node 10
   if-match tag 2000
  #
  route-policy dp permit node 15
   if-match ip-prefix lp
  #
  route-policy dp deny node 20
  #
  route-policy p1 deny node 10
  #
  route-policy stopuIP deny node 10
   if-match ip-prefix uIP
  #
  route-policy stopuIP permit node 20
  #
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
  #
  return
  ```
* DCGW2 configuration file
  
  ```
  #
  sysname DCGW2
  #
  evpn
   bypass-vxlan enable
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    export route-policy dp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 200  
  #
  bridge-domain 10
   vxlan vni 100 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   vxlan vni 110 split-horizon-mode
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   vxlan vni 120 split-horizon-mode
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   vxlan vni 130 split-horizon-mode
   evpn binding vpn-instance evrf4
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0002
   vxlan anycast-gateway enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   vxlan anycast-gateway enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   vxlan anycast-gateway enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   vxlan anycast-gateway enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.3.1 255.255.255.0
  #
  interface GigabitEthernet0/1/3
   undo shutdown
  #
  interface GigabitEthernet0/1/3.1 mode l2
    encapsulation dot1q vid 10
    rewrite pop single
    bridge-domain 10 
  # 
  interface GigabitEthernet0/1/3.2 mode l2
    encapsulation dot1q vid 30
    rewrite pop single
    bridge-domain 30
  #
  interface LoopBack0
   ip address 9.9.9.9 255.255.255.255
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ip address 44.44.44.44 255.255.255.255
  #
  interface Nve1
   source 9.9.9.9
   bypass source 4.4.4.4
   mac-address 00e0-fc00-0009
   vni 100 head-end peer-list protocol bgp
   vni 110 head-end peer-list protocol bgp
   vni 120 head-end peer-list protocol bgp
   vni 130 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0 0
    import-route direct
    maximum load-balancing 16  
    advertise l2vpn evpn
    peer 5.5.5.5 as-number 100
    peer 5.5.5.5 connect-interface LoopBack2
    peer 5.5.5.5 route-policy p1 export
    peer 6.6.6.6 as-number 100
    peer 6.6.6.6 connect-interface LoopBack2
    peer 6.6.6.6 route-policy p1 export
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 capability-advertise add-path both
    peer 1.1.1.1 advertise add-path path-number 16
    peer 1.1.1.1 advertise encap-type vxlan
    peer 2.2.2.2 enable
    peer 2.2.2.2 capability-advertise add-path both
    peer 2.2.2.2 advertise add-path path-number 16
    peer 2.2.2.2 advertise encap-type vxlan
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise encap-type vxlan
    peer 3.3.3.3 route-policy stopuIP export
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 9.9.9.9 0.0.0.0
    network 10.6.1.0 0.0.0.255
    network 10.6.3.0 0.0.0.255
  #
  ip ip-prefix lp index 10 permit 44.44.44.44 32
  ip ip-prefix uIP index 10 permit 10.10.10.10 32
  #
  route-policy dp permit node 10
   if-match tag 2000
  #
  route-policy dp permit node 15
   if-match ip-prefix lp
  #
  route-policy dp deny node 20
  #
  route-policy p1 deny node 10
  #
  route-policy stopuIP deny node 10
   if-match ip-prefix uIP
  #
  route-policy stopuIP permit node 20
  #
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 NULL0 tag 2000
  #
  ip path detection enable dscp 3
  #
  return
  ```
* L2GW/L3GW1 configuration file
  
  ```
  #
  sysname L2GW/L3GW1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    export route-policy sp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 200
  #
  bridge-domain 10
   vxlan vni 100 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   vxlan vni 110 split-horizon-mode
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   vxlan vni 120 split-horizon-mode
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   vxlan vni 130 split-horizon-mode
   evpn binding vpn-instance evrf4
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0002
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.4.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.2.2 255.255.255.0
  #
  interface GigabitEthernet0/1/3.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/4.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface GigabitEthernet0/1/5.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface Nve1
   source 1.1.1.1
   vni 100 head-end peer-list protocol bgp
   vni 110 head-end peer-list protocol bgp
   vni 120 head-end peer-list protocol bgp
   vni 130 head-end peer-list protocol bgp
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route static
    maximum load-balancing 16  
    advertise l2vpn evpn import-route-multipath
   #
   l2vpn-family evpn
    undo policy vpn-target
    bestroute add-path path-number 16
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise arp
    peer 2.2.2.2 advertise encap-type vxlan
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise arp
    peer 3.3.3.3 capability-advertise add-path both
    peer 3.3.3.3 advertise add-path path-number 16
    peer 3.3.3.3 advertise encap-type vxlan
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise arp
    peer 4.4.4.4 capability-advertise add-path both
    peer 4.4.4.4 advertise add-path path-number 16
    peer 4.4.4.4 advertise encap-type vxlan
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.6.2.0 0.0.0.255
    network 10.6.4.0 0.0.0.255
  #
  route-policy sp permit node 10
   if-match tag 1000
   apply gateway-ip origin-nexthop
  #
  route-policy sp deny node 20
  #
  ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.1.1.2 tag 1000
  ip route-static vpn-instance vpn1 5.5.5.5 255.255.255.255 10.2.1.2 tag 1000
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.1.1.3 tag 1000
  #
  return
  ```
* L2GW/L3GW2 configuration file
  
  ```
  #
  sysname L2GW/L3GW2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 1:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 2:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 3:3
   vpn-target 3:3 export-extcommunity
   vpn-target 3:3 import-extcommunity
  #
  evpn vpn-instance evrf4 bd-mode
   route-distinguisher 4:4
   vpn-target 4:4 export-extcommunity
   vpn-target 4:4 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    export route-policy sp evpn
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 200
  #
  bridge-domain 10
   vxlan vni 100 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   vxlan vni 110 split-horizon-mode
   evpn binding vpn-instance evrf2
  #
  bridge-domain 30
   vxlan vni 120 split-horizon-mode
   evpn binding vpn-instance evrf3
  #
  bridge-domain 40
   vxlan vni 130 split-horizon-mode
   evpn binding vpn-instance evrf4
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0002
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0003
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif30
   ip binding vpn-instance vpn1
   ip address 10.3.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0001
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface Vbdif40
   ip binding vpn-instance vpn1
   ip address 10.4.1.1 255.255.255.0
   arp generate-rd-table enable
   mac-address 00e0-fc00-0004
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.6.4.2 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.6.3.2 255.255.255.0
  #
  interface GigabitEthernet0/1/3.1 mode l2
   encapsulation dot1q vid 30
   rewrite pop single
   bridge-domain 30
  #
  interface GigabitEthernet0/1/4.1 mode l2
   encapsulation dot1q vid 40
   rewrite pop single
   bridge-domain 40
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #               
  interface Nve1
   source 2.2.2.2
   vni 100 head-end peer-list protocol bgp
   vni 110 head-end peer-list protocol bgp
   vni 120 head-end peer-list protocol bgp
   vni 130 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route static
    maximum load-balancing 16  
    advertise l2vpn evpn import-route-multipath
   #
   l2vpn-family evpn
    undo policy vpn-target
    bestroute add-path path-number 16
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise arp
    peer 1.1.1.1 advertise encap-type vxlan
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise arp
    peer 3.3.3.3 capability-advertise add-path both
    peer 3.3.3.3 advertise add-path path-number 16
    peer 3.3.3.3 advertise encap-type vxlan
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise arp
    peer 4.4.4.4 capability-advertise add-path both
    peer 4.4.4.4 advertise add-path path-number 16
    peer 4.4.4.4 advertise encap-type vxlan
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.6.3.0 0.0.0.255
    network 10.6.4.0 0.0.0.255
  #
  route-policy sp permit node 10
   if-match tag 1000
   apply gateway-ip origin-nexthop
  #
  route-policy sp deny node 20
  #
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.3.1.2 tag 1000
  ip route-static vpn-instance vpn1 6.6.6.6 255.255.255.255 10.4.1.2 tag 1000
  #
  ip path detection enable dscp 3
  #
  return
  ```
* VNF1 configuration file
  
  For details, see the configuration file of the specific device model.
* VNF2 configuration file
  
  For details, see the configuration file of the specific device model.