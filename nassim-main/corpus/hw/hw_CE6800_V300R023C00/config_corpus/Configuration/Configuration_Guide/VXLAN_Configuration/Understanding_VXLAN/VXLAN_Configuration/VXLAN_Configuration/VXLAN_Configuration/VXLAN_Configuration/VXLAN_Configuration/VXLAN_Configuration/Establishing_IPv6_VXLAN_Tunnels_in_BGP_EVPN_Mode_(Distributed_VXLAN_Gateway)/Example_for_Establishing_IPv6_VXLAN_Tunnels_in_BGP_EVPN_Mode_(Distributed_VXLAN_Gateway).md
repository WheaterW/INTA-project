Example for Establishing IPv6 VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)
========================================================================================

Example for Establishing IPv6 VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)

#### Networking Requirements

IPv6 VXLAN distributed gateways can address issues with centralized gateway networking, such as sub-optimal forwarding paths and bottlenecks on Layer 3 gateways in terms of ARP or ND entry specifications.

On the network shown in [Figure 1](#EN-US_TASK_0000001193911169__fig_dc_cfg_vxlan_cfgcase_000401), an enterprise deploys IPv4 VMs in different areas of an IPv6 DC. IPv4 VM1 on Server1 belongs to VLAN 10, and IPv4 VM1 on Server2 belongs to VLAN 20. The two VMs belong to different network segments. IPv6 VXLAN in distributed gateway mode is required for communication between IPv4 VM1s on different servers.

**Figure 1** Configuring IPv6 VXLAN in distributed gateway mode![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001193991055.png)

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| Device1 | 100GE1/0/1 | 2001:DB8:3::2/64 |
| 100GE1/0/2 | 2001:DB8:2::2/64 |
| LoopBack0 | 2001:DB8:11::1/128 |
| Device2 | 100GE1/0/1 | 2001:DB8:2::1/64 |
| LoopBack0 | 2001:DB8:22::2/128 |
| Device3 | 100GE1/0/1 | 2001:DB8:3::1/64 |
| LoopBack0 | 2001:DB8:33::3/128 |



#### Precautions

[Table 2](#EN-US_TASK_0000001193911169__table1011135203114) lists the RDs and RTs of EVPN and VPN instances.

**Table 2** RDs and RTs of devices
| Device | RD | RT |
| --- | --- | --- |
| Device2 | EVPN instance: 10:2  VPN instance: 20:2 | EVPN instance:  * ERT/IRT: 100:10 * ERT: 100:5010  VPN instance:  * ERT/IRT (EVPN): 100:5010 |
| Device3 | EVPN instance: 10:3  VPN instance: 20:3 | EVPN instance:  * ERT/IRT: 100:20 * ERT: 100:5010  VPN instance:  * ERT/IRT (EVPN): 100:5010 |


**Figure 2** Configuring RTs  
![](figure/en-us_image_0000001147871458.png)
The RT configuration guidelines for VPN and EVPN instances are as follows:

* For VPN instances, specify the **evpn** keyword during the configuration of an ERT (such as ERT Y) and an IRT (such as IRT Y) to enable route leaking into peer EVPN instances for host route generation. If route leaking into common L3VPN instances is required, configure common RTs on demand.
* In EVPN instances, in addition to ERTs (such as ERT A and ERT B) and IRTs (such as IRT A and IRT B) for different BDs, configure ERT Y that is used for route leaking into a peer VPN instance. Generally, IRT Y does not need to be configured, because doing so would cause MAC addresses to be advertised in EVPN instances of different BDs.
* The ERT/IRT Y value of a VPN instance cannot be the same as the ERT/IRT A or ERT/IRT B value of an EVPN instance. It is recommended that the VPN and EVPN instances use different RT ranges for differentiation.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPFv3 to run between Device1 and Device2 and between Device1 and Device3.
2. Configure service access points on Device2 and Device3 to differentiate service traffic.
3. Configure Device2 and Device3 to establish BGP EVPN peer relationships with Device1.
4. Configure Device1 to establish BGP EVPN peer relationships with Device2 and Device3. Then, configure Device1 as the RR.
5. Configure VPN and EVPN instances on Device2 and Device3.
6. Enable ingress replication on Device2 and Device3.
7. Configure an IPv6 Layer 3 VXLAN gateway on Device2 and Device3, and configure an IPv4 address for the gateway interface.
8. Configure BGP to advertise IRB routes and IP prefix routes between Device1 and Device2 and between Device1 and Device3.


#### Procedure

1. Assign an IPv6 address for each interface.
   
   
   
   Assign an IPv6 address to each interface on Device1, Device2, and Device3 according to [Figure 1](#EN-US_TASK_0000001193911169__fig_dc_cfg_vxlan_cfgcase_000401). For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001193911169__postreq19133121341511).
2. Configure OSPFv3.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] ospfv3 1
   [*Device1-ospfv3-1] router-id 1.1.1.1
   [*Device1-ospfv3-1] area 0.0.0.0
   [*Device1-ospfv3-1-area-0.0.0.0] quit
   [*Device1-ospfv3-1] quit
   [*Device1] commit
   [~Device1] interface loopback 0
   [*Device1-LoopBack0] ospfv3 1 area 0.0.0.0
   [*Device1-LoopBack0] quit
   [*Device1] interface 100GE1/0/1
   [*Device1-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*Device1-100GE1/0/1] quit
   [*Device1] interface 100GE1/0/2
   [*Device1-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*Device1-100GE1/0/2] quit
   [*Device1] commit
   ```
3. Configure service access points on Device2 and Device3.
   
   
   
   # Configure Device2. The configuration of Device3 is similar to that of Device2.
   
   ```
   [~Device2] bridge-domain 10
   [*Device2-bd10] quit
   [*Device2] interface 100ge 1/0/2.1 mode l2
   [*Device2-100GE1/0/2.1] encapsulation dot1q vid 10
   [*Device2-100GE1/0/2.1] bridge-domain 10
   [*Device2-100GE1/0/2.1] quit
   [*Device2] commit
   ```
4. Enable EVPN to function as the VXLAN control plane protocol.
   
   
   
   # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
   
   ```
   [~Device1] evpn-overlay enable
   [*Device1] commit
   ```
5. Configure Device2 and Device3 to establish BGP EVPN peer relationships with Device1.
   
   # Configure a BGP EVPN peer relationship on Device2. The configuration of Device3 is similar to that of Device2.
   ```
   [~Device2] bgp 100
   [*Device2-bgp] peer 2001:DB8:11::1 as-number 100
   [*Device2-bgp] peer 2001:DB8:11::1 connect-interface LoopBack0
   [*Device2-bgp] l2vpn-family evpn
   [*Device2-bgp-af-evpn] policy vpn-target
   [*Device2-bgp-af-evpn] peer 2001:DB8:11::1 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: Y
   [*Device2-bgp-af-evpn] quit
   [*Device2-bgp] quit
   [*Device2] commit
   ```
6. Configure Device1 to establish BGP EVPN peer relationships with Device2 and Device3. Then configure Device1 as the RR and Device2 and Device3 as the RR clients.
   
   # Configure Device1.
   ```
   [~Device1] bgp 100
   [*Device1-bgp] peer 2001:DB8:22::2 as-number 100
   [*Device1-bgp] peer 2001:DB8:22::2 connect-interface LoopBack0
   [*Device1-bgp] peer 2001:DB8:33::3 as-number 100
   [*Device1-bgp] peer 2001:DB8:33::3 connect-interface LoopBack0
   [*Device1-bgp] l2vpn-family evpn
   [*Device1-bgp-af-evpn] peer 2001:DB8:22::2 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: Y
   [*Device1-bgp-af-evpn] peer 2001:DB8:22::2 reflect-client
   [*Device1-bgp-af-evpn] peer 2001:DB8:33::3 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: Y
   [*Device1-bgp-af-evpn] peer 2001:DB8:33::3 reflect-client
   [*Device1-bgp-af-evpn] undo policy vpn-target
   [*Device1-bgp-af-evpn] quit
   [*Device1-bgp] quit
   [*Device1] commit
   ```
7. Configure VPN and EVPN instances on Device2 and Device3.
   
   
   
   # Configure Device2. The configuration of Device3 is similar to that of Device2.
   
   ```
   [~Device2] ip vpn-instance vpn1
   [*Device2-vpn-instance-vpn1] vxlan vni 5010
   [*Device2-vpn-instance-vpn1] ipv4-family
   [*Device2-vpn-instance-vpn1-af-ipv4] route-distinguisher 20:2
   [*Device2-vpn-instance-vpn1-af-ipv4] vpn-target 100:5010 evpn
   [*Device2-vpn-instance-vpn1-af-ipv4] quit
   [*Device2-vpn-instance-vpn1] quit
   [*Device2] bridge-domain 10
   [*Device2-bd10] vxlan vni 10
   [*Device2-bd10] evpn
   [*Device2-bd10-evpn] route-distinguisher 10:2
   [*Device2-bd10-evpn] vpn-target 100:10
   [*Device2-bd10-evpn] vpn-target 100:5010 export-extcommunity
   [*Device2-bd10-evpn] vpn-target 100:5010 import-extcommunity
   [*Device2-bd10-evpn] quit
   [*Device2-bd10] quit
   [*Device2] commit
   ```
8. Enable ingress replication on Device2 and Device3.
   
   
   
   # Configure Device2. The configuration of Device3 is similar to that of Device2.
   
   ```
   [~Device2] interface nve 1
   [*Device2-Nve1] source 2001:DB8:22::2
   [*Device2-Nve1] vni 10 head-end peer-list protocol bgp
   [*Device2-Nve1] quit
   [*Device2] commit
   ```
9. Configure Layer 3 VXLAN gateways on Device2 and Device3.
   
   # Configure a Layer 3 VXLAN gateway on Device2. The configuration of Device3 is similar to the configuration of Device2. Note that the IP addresses of VBDIF interfaces on Device2 and Device3 must belong to different network segments.
   ```
   [~Device2] interface Vbdif10
   [*Device2-Vbdif10] ip binding vpn-instance vpn1
   [*Device2-Vbdif10] ip address 10.1.1.1 255.255.255.0
   [*Device2-Vbdif10] vxlan anycast-gateway enable
   [*Device2-Vbdif10] arp collect host enable
   [*Device2-Vbdif10] arp direct-route enable
   [*Device2-Vbdif10] quit
   [*Device2] commit
   ```
10. Configure BGP to advertise IRB routes between Device1 and Device2 and between Device1 and Device3.
    
    
    
    # Configure Device1. The configurations of Device2 and Device3 are similar to the configuration of Device1.
    
    ```
    [~Device1] bgp 100
    [~Device1-bgp] l2vpn-family evpn
    [~Device1-bgp-af-evpn] peer 2001:DB8:22::2 advertise irb
    [*Device1-bgp-af-evpn] peer 2001:DB8:33::3 advertise irb
    [*Device1-bgp-af-evpn] quit
    [*Device1-bgp] quit
    [*Device1] commit
    ```
11. Configure Device2 and Device3 to advertise IP prefix routes.
    
    
    
    # Configure Device2. The configuration of Device3 is similar to that of Device2.
    
    ```
    [~Device2] bgp 100
    [~Device2-bgp] ipv4-family vpn-instance vpn1
    [*Device2-bgp-vpn1] import-route direct
    [*Device2-bgp-vpn1] advertise l2vpn evpn
    [*Device2-bgp-vpn1] quit
    [*Device2-bgp] quit
    [*Device2] commit
    ```

#### Verifying the Configuration

After completing the configurations, run the **display vxlan tunnel** command on Device2 and Device3 to check IPv6 VXLAN tunnel information. The following example uses the command output on Device2.

```
[~Device2] display vxlan tunnel
```
```
Number of vxlan tunnel : 1
Tunnel ID   Source           Destination      State  Type     Uptime
--------------------------------------------------------------------
4026531919  2001:DB8:22::2   2001:DB8:33::3   up     dynamic  00:44:18
```

VM1s on different servers can communicate. VM1 on Server2 can be pinged from the distributed gateway Device2.

```
[~Device2] ping -vpn-instance vpn1 10.2.1.10 
  PING 10.2.1.10: 300  data bytes, press CTRL_C to break
    Reply from 10.2.1.10: bytes=300 Sequence=1 ttl=254 time=30 ms
    Reply from 10.2.1.10: bytes=300 Sequence=2 ttl=254 time=30 ms
    Reply from 10.2.1.10: bytes=300 Sequence=3 ttl=254 time=30 ms
    Reply from 10.2.1.10: bytes=300 Sequence=4 ttl=254 time=30 ms
    Reply from 10.2.1.10: bytes=300 Sequence=5 ttl=254 time=30 ms

  --- 10.2.1.10 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 30/30/30 ms
```
![](../public_sys-resources/note_3.0-en-us.png) 

The tunnel goes up only after a Layer 2 sub-interface on Device2 or Device3 connects to a server. When there is no access server, the VXLAN tunnel state is not displayed because no IRB route is advertised.



#### Configuration Scripts

* Device1
  
  ```
  #
  sysname Device1
  #
  evpn-overlay enable                                                             
  # 
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:11::1/128
   ospfv3 1 area 0.0.0.0
  #
  bgp 100
   private-4-byte-as enable
   peer 2001:DB8:22::2 as-number 100
   peer 2001:DB8:22::2 connect-interface LoopBack0
   peer 2001:DB8:33::3 as-number 100
   peer 2001:DB8:33::3 connect-interface LoopBack0
   #
   ipv4-family unicast
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2001:DB8:22::2 enable
    peer 2001:DB8:22::2 advertise irb
    peer 2001:DB8:22::2 reflect-client
    peer 2001:DB8:33::3 enable
    peer 2001:DB8:33::3 advertise irb
    peer 2001:DB8:33::3 reflect-client
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:2
    vpn-target 100:5010 export-extcommunity evpn
    vpn-target 100:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:2
    vpn-target 100:10 export-extcommunity
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:10 import-extcommunity
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
   arp direct-route enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:22::2/128
   ospfv3 1 area 0.0.0.0
  #
  interface Nve1
   source 2001:DB8:22::2
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   private-4-byte-as enable
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack0
   #
   ipv4-family unicast
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:11::1 advertise irb
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
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:3
    vpn-target 100:5010 export-extcommunity evpn
    vpn-target 100:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20
   #
   evpn
    route-distinguisher 10:3
    vpn-target 100:20 export-extcommunity
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:20 import-extcommunity
    vpn-target 100:5010 import-extcommunity
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
   arp direct-route enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:33::3/128
   ospfv3 1 area 0.0.0.0
  #
  interface Nve1
   source 2001:DB8:33::3
   vni 20 head-end peer-list protocol bgp
  #
  bgp 100
   private-4-byte-as enable
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack0
   #
   ipv4-family unicast
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:11::1 advertise irb
  #
  return
  ```