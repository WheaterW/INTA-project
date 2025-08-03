Example for Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed Gateway: M-LAG+ Static Bypass VXLAN)
=========================================================================================================

Example for Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed Gateway: M-LAG+ Static Bypass VXLAN)

#### Networking Requirements

Distributed VXLAN gateways can address issues with centralized gateway networking. Such issues include sub-optimal forwarding paths and bottlenecks on Layer 3 gateways in terms of ARP entry specifications.

On the network shown in [Figure 1](#EN-US_TASK_0000001176743957__fig_dc_cfg_vxlan_cfgcase_000401), an enterprise has VMs deployed in different data centers. VM1 on Server1 (Server1 VM1 for short) belongs to VLAN 10, and Server2 VM1 belongs to VLAN 20. The two VMs belong to different network segments. Server1 connects to the VXLAN through Device2 and Device4. Server1 VM1 and Server2 VM1 need to communicate with each other through a distributed VXLAN gateway. Device1 is deployed in AS 100, Device2 and Device4 in AS 200, and Device3 in AS 300. All the devices use AS number 100 as the BGP EVPN process ID.

**Figure 1** Network for configuring VXLAN in distributed gateway mode![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001130784370.png)

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| Device1 | 100GE1/0/1 | 192.168.3.2/24 |
| 100GE1/0/2 | 192.168.2.2/24 |
| 100GE1/0/3 | 192.168.4.2/24 |
| LoopBack0 | 1.1.1.1/32 |
| Device2 | Management interface | 10.10.1.1/24 |
| 100GE1/0/1 | 192.168.2.1/24 |
| LoopBack0 | 2.2.2.2/32 |
| LoopBack1 | 2.2.2.3/32 |
| Vlanif 100 | 10.10.10.1/24 |
| Device3 | 100GE1/0/1 | 192.168.3.1/24 |
| LoopBack0 | 3.3.3.3/32 |
| Device4 | Management interface | 10.10.1.2/24 |
| 100GE1/0/1 | 192.168.4.1/24 |
| LoopBack0 | 4.4.4.4/32 |
| LoopBack1 | 2.2.2.3/32 |
| Vlanif 100 | 10.10.10.2/24 |



#### Configuration Precautions

In a scenario where a device is dual-homed to a VXLAN network through an M-LAG and the physical peer-link is used, running the [**port vlan exclude**](cmdqueryname=port+vlan+exclude) command on a peer-link interface is mutually exclusive with binding a BD to a VNI (by running the [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* command in the BD view). In this case, you are advised to configure a static bypass VXLAN tunnel and then bind the BD to a VNI.

[Table 2](#EN-US_TASK_0000001176743957__table1011135203114) lists the RDs and RTs of EVPN and VPN instances.

**Table 2** RDs and RTs of devices
| Device | RD | RT |
| --- | --- | --- |
| Device2 | EVPN instance: 10:2  VPN instance: 20:2 | EVPN instance:  * ERT/IRT: 100:10 * ERT: 100:5010  VPN instance:  * ERT/IRT (EVPN): 100:5010 |
| Device3 | EVPN instance: 10:3  VPN instance: 20:3 | EVPN instance:  * ERT/IRT: 100:20 * ERT: 100:5010  VPN instance:  * ERT/IRT (EVPN): 100:5010 |
| Device4 | EVPN instance: 10:4  VPN instance: 20:4 | EVPN instance:  * ERT/IRT: 100:10 * ERT: 100:5010  VPN instance:  * ERT/IRT (EVPN): 100:5010 |


**Figure 2** Configuring RTs  
![](figure/en-us_image_0000001130624582.png)
The RT configuration guidelines for VPN and EVPN instances are as follows:

* For VPN instances, specify the **evpn** keyword during the configuration of an ERT (such as ERT Y) and an IRT (such as IRT Y) to enable route leaking into peer EVPN instances for host route generation. If route leaking into common L3VPN instances is required, configure common RTs on demand.
* For EVPN instances, in addition to ERTs (such as ERT A and ERT B) and IRTs (such as IRT A and IRT B) for different BDs, configure ERT Y. This ERT is used for route leaking into a peer VPN instance. Note that IRT Y does not typically need to be configured, because doing so would cause MAC addresses to be advertised in EVPN instances of different BDs.
* The ERT/IRT Y value of a VPN instance cannot be the same as the ERT/IRT A or ERT/IRT B value of an EVPN instance. It is recommended that the VPN and EVPN instances use different RT ranges for differentiation.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure EBGP to run between Device1 and Device2, Device3, and Device4.
2. Configure V-STP-based M-LAG on Device2 and Device4.
3. Configure a static bypass VXLAN tunnel between Device2 and Device4 in an M-LAG.
4. Configure service access points on Device2, Device3, and Device4 to distinguish service traffic.
5. Enable EVPN to function as the VXLAN control plane protocol.
6. Configure Device1 to establish BGP EVPN peer relationships with Device2, Device3, and Device4, and configure Device1 as the RR.
7. Configure Device2, Device3, and Device4 to establish IBGP EVPN peer relationships with Device1.
8. Configure a VPN instance and an EVPN instance on Device2, Device3, and Device4.
9. Enable ingress replication on Device2, Device3, and Device4.
10. Configure Device2, Device3, and Device4 as a Layer 3 VXLAN gateway.
11. Configure BGP to advertise IRB routes between Device1 and Device2, Device3, and Device4.
12. Configure BGP to advertise IP prefix routes to peers between Device2 and Device3 and between Device2 and Device4.


#### Procedure

1. Configure EBGP.
   
   
   
   # Configure Device1. The configurations of Device2, Device3, and Device4 are similar to the configuration of Device1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device1
   [*HUAWEI] commit
   [~Device1] interface loopback 0
   [*Device1-LoopBack0] ip address 1.1.1.1 32
   [*Device1-LoopBack0] quit
   [*Device1] interface 100ge 1/0/1
   [*Device1-100GE1/0/1] undo portswitch
   [*Device1-100GE1/0/1] ip address 192.168.3.2 24
   [*Device1-100GE1/0/1] quit
   [*Device1] interface 100ge 1/0/2
   [*Device1-100GE1/0/2] undo portswitch
   [*Device1-100GE1/0/2] ip address 192.168.2.2 24
   [*Device1-100GE1/0/2] quit
   [*Device1] interface 100ge 1/0/3
   [*Device1-100GE1/0/3] undo portswitch
   [*Device1-100GE1/0/3] ip address 192.168.4.2 24
   [*Device1-100GE1/0/3] quit
   [*Device1] bgp 100
   [*Device1-bgp] peer 192.168.2.1 as-number 200
   [*Device1-bgp] peer 192.168.3.1 as-number 300
   [*Device1-bgp] peer 192.168.4.1 as-number 200
   [*Device1-bgp] network 1.1.1.1 32
   [*Device1-bgp] quit
   [*Device1] commit
   ```
   
   Device2 and Device4 both belong to AS 200. To enable them to advertise BGP routes to each other, run the [**peer 192.168.2.2 allow-as-loop**](cmdqueryname=peer+192.168.2.2+allow-as-loop) command on Device2 and run the [**peer 192.168.4.2 allow-as-loop**](cmdqueryname=peer+192.168.4.2+allow-as-loop) command on Device4.
   
   On Device2 and Device3, run the **advertise lowest-priority all-address-family peer-up** command in the BGP view to adjust the priority of BGP routes to the lowest level when the peer relationship goes up from down, and delay route advertisement to reduce packet loss during traffic switchback.
2. Configure V-STP-based M-LAG on Device2 and Device4.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the uplink connecting Device2 to the VXLAN fails, no upstream interface is available, and so Device2 will discard all received user traffic. In this case, configure a monitor-link group to associate the upstream and downstream interfaces of Device2. If the upstream interface of Device2 is down, the downstream interface will also go down. As a result, user-side traffic is not forwarded through Device2, preventing traffic from being discarded.
   
   
   
   1. Configure V-STP on Device2 and Device4.
      
      
      
      # Configure Device2. The configuration of Device4 is similar to the configuration of Device2.
      
      ```
      [~Device2] stp mode rstp
      [*Device2] stp v-stp enable
      [*Device2] commit
      ```
   2. On each of Device2 and Device4, configure a DFS group and bind the DFS group to the IP address of the management interface.
      
      
      
      Ensure that Device2 and Device4 can communicate at Layer 3 through their management interfaces.
      
      # Configure Device2. The configuration of Device4 is similar to the configuration of Device2.
      
      ```
      [~Device2] interface meth 0/0/0
      [~Device2-MEth0/0/0] ip address 10.10.1.1 24
      [*Device2-MEth0/0/0] quit
      [*Device2] dfs-group 1
      [*Device2-dfs-group-1] dual-active detection source ip 10.10.1.1 peer 10.10.1.2
      [*Device2-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*Device2-dfs-group-1] quit
      [*Device2] commit
      ```
   3. Configure the links between Device2 and Device4 as peer-links.
      
      
      
      # Configure Device2. The configuration of Device4 is similar to the configuration of Device2.
      
      ```
      [~Device2] interface eth-trunk 1
      [*Device2-Eth-Trunk1] mode lacp-static
      [*Device2-Eth-Trunk1] trunkport 100ge 1/0/3 to 1/0/4
      [*Device2-Eth-Trunk1] peer-link 1
      [*Device2-Eth-Trunk1] port vlan exclude 1
      [*Device2-Eth-Trunk1] quit
      [*Device2] commit
      ```
   4. Bind the user-side Eth-Trunk interface to the DFS group on Device2 and Device4.
      
      
      
      # Configure Device2. The configuration of Device4 is similar to the configuration of Device2.
      
      ```
      [~Device2] interface eth-trunk 10
      [*Device2-Eth-Trunk10] mode lacp-static
      [*Device2-Eth-Trunk10] trunkport 100ge 1/0/2
      [*Device2-Eth-Trunk10] dfs-group 1 m-lag 1
      [*Device2-Eth-Trunk10] stp edged-port enable
      [*Device2-Eth-Trunk10] quit
      [*Device2] commit
      ```
3. Configure a static bypass VXLAN tunnel on Device2 and Device4.
   
   
   
   # Configure Device2.
   
   ```
   [~Device2] vlan 100
   [*Device2-vlan100] quit
   [*Device2] interface vlanif 100
   [*Device2-Vlanif100] ip address 10.10.10.1 24
   [*Device2-Vlanif100] quit
   [*Device2] interface nve 1
   [*Device2-Nve1] pip-source 10.10.10.1 peer 10.10.10.2 bypass
   [*Device2-Nve1] quit
   [*Device2] commit
   ```
   
   
   
   # Configure Device4.
   
   ```
   [~Device4] vlan 100
   [*Device4-vlan100] quit
   [*Device4] interface vlanif 100
   [*Device4-Vlanif100] ip address 10.10.10.2 24
   [*Device4-Vlanif100] quit
   [*Device4] interface nve 1
   [*Device4-Nve1] pip-source 10.10.10.2 peer 10.10.10.1 bypass
   [*Device4-Nve1] quit
   [*Device4] commit
   ```
4. Configure service access points on Device2, Device3, and Device4.
   
   
   
   # Configure Device2. The configurations of Device3 and Device4 are similar to the configuration of Device2.
   
   ```
   [~Device2] bridge-domain 10
   [*Device2-bd10] quit
   [*Device2] interface eth-trunk 10.1 mode l2
   [*Device2-Eth-Trunk10.1] encapsulation dot1q vid 10
   [*Device2-Eth-Trunk10.1] bridge-domain 10
   [*Device2-Eth-Trunk10.1] quit
   [*Device2] commit
   ```
5. Enable EVPN to function as the VXLAN control plane protocol.
   
   
   
   # Configure Device1. The configurations of Device2, Device3, and Device4 are similar to the configuration of Device1.
   
   ```
   [~Device1] evpn-overlay enable
   [*Device1] commit
   ```
6. Configure Device1 to establish BGP EVPN peer relationships with Device2, Device3, and Device4. Configure Device1 as the RR, and Device2, Device3, and Device4 as its clients.
   
   # Configure BGP EVPN peer relationships on Device1.
   ```
   [~Device1] bgp 100 instance evpn1
   [*Device1-bgp-instance-evpn1] peer 2.2.2.2 as-number 100
   [*Device1-bgp-instance-evpn1] peer 2.2.2.2 connect-interface LoopBack0
   [*Device1-bgp-instance-evpn1] peer 3.3.3.3 as-number 100
   [*Device1-bgp-instance-evpn1] peer 3.3.3.3 connect-interface LoopBack0
   [*Device1-bgp-instance-evpn1] peer 4.4.4.4 as-number 100
   [*Device1-bgp-instance-evpn1] peer 4.4.4.4 connect-interface LoopBack0
   [*Device1-bgp-instance-evpn1] l2vpn-family evpn
   [*Device1-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: y
   [*Device1-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 reflect-client
   [*Device1-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: y
   [*Device1-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 reflect-client
   [*Device1-bgp-instance-evpn1-af-evpn] peer 4.4.4.4 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: y
   [*Device1-bgp-instance-evpn1-af-evpn] peer 4.4.4.4 reflect-client
   [*Device1-bgp-instance-evpn1-af-evpn] undo policy vpn-target
   [*Device1-bgp-instance-evpn1-af-evpn] quit
   [*Device1-bgp-instance-evpn1] quit
   [*Device1] commit
   ```
7. Configure Device2, Device3, and Device4 to establish IBGP EVPN peer relationships with Device1.
   
   # Configure a BGP EVPN peer relationship on Device2. The configurations of Device3 and Device4 are similar to the configuration of Device2.
   ```
   [~Device2] bgp 100 instance evpn1
   [*Device2-bgp-instance-evpn1] peer 1.1.1.1 as-number 100
   [*Device2-bgp-instance-evpn1] peer 1.1.1.1 connect-interface LoopBack0
   [*Device2-bgp-instance-evpn1] l2vpn-family evpn
   [*Device2-bgp-instance-evpn1-af-evpn] peer 1.1.1.1 enable
   Warning: This operation will reset the peer session. Continue? [Y/N]: y
   [*Device2-bgp-instance-evpn1-af-evpn] quit
   [*Device2-bgp-instance-evpn1] quit
   [*Device2] commit
   ```
8. Configure a VPN instance and an EVPN instance on Device2, Device3, and Device4.
   
   
   
   # Configure Device2. The configurations of Device3 and Device4 are similar to the configuration of Device2.
   
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
   [*Device2-bd10-evpn] quit
   [*Device2-bd10] quit
   [*Device2] commit
   ```
9. Enable ingress replication on Device2, Device3, and Device4.
   
   
   
   # Configure Device2. The configurations of Device3 and Device4 are similar to the configuration of Device2. However, on Device3, you do not need to configure a MAC address for the NVE interface.
   
   ```
   [~Device2] interface nve 1
   [*Device2-Nve1] source 2.2.2.3
   [*Device2-Nve1] mac-address 00e0-fc12-3456
   [*Device2-Nve1] vni 10 head-end peer-list protocol bgp
   [*Device2-Nve1] quit
   [*Device2] commit
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Because Device2 and Device4 work as active-active gateways, ensure that their NVE interfaces have the same IP and MAC addresses.
10. Configure Device2, Device3, and Device4 as a Layer 3 VXLAN gateway.
    
    # Configure Device2 as a Layer 3 VXLAN gateway. The configurations of Device3 and Device4 are similar to the configuration of Device2. Keep in mind that: The IP addresses of the VBDIF interfaces on Device2 and Device3 must be on different network segments. The IP and MAC addresses of the VBDIF interfaces on Device2 and Device4 must be the same. You do not need to configure a MAC address for the VBDIF interface on Device3.
    ```
    [~Device2] interface vbdif10
    [*Device2-Vbdif10] ip binding vpn-instance vpn1
    [*Device2-Vbdif10] ip address 10.1.1.1 255.255.255.0
    [*Device2-Vbdif10] mac-address 00e0-fc12-3457
    [*Device2-Vbdif10] vxlan anycast-gateway enable
    [*Device2-Vbdif10] arp collect host enable
    [*Device2-Vbdif10] arp broadcast-detect enable
    [*Device2-Vbdif10] quit
    [*Device2] commit
    ```
    ![](../public_sys-resources/note_3.0-en-us.png) 
    
    Because Device2 and Device4 work as dual-active gateways, ensure that their VBDIF interfaces have the same IP and MAC addresses.
11. Configure BGP to advertise IRB routes between Device1 and Device2, Device3, and Device4.
    
    
    
    # Configure Device1. The configurations of Device2, Device3, and Device4 are similar to the configuration of Device1.
    
    ```
    [~Device1] bgp 100 instance evpn1
    [~Device1-bgp-instance-evpn1] l2vpn-family evpn
    [~Device1-bgp-instance-evpn1-af-evpn] peer 2.2.2.2 advertise irb
    [*Device1-bgp-instance-evpn1-af-evpn] peer 3.3.3.3 advertise irb
    [*Device1-bgp-instance-evpn1-af-evpn] peer 4.4.4.4 advertise irb
    [*Device1-bgp-instance-evpn1-af-evpn] quit
    [*Device1-bgp-instance-evpn1] quit
    [*Device1] commit
    ```
12. Configure BGP to advertise IP prefix routes to peers between Device2 and Device3 and between Device2 and Device4.
    
    
    
    # Configure Device2. The configurations of Device3 and Device4 are similar to the configuration of Device2.
    
    ```
    [~Device2] bgp 100 instance evpn1
    [~Device2-bgp-instance-evpn1] ipv4-family vpn-instance vpn1
    [*Device2-bgp-instance-evpn1-vpn1] import-route direct
    [*Device2-bgp-instance-evpn1-vpn1] advertise l2vpn evpn
    [*Device2-bgp-instance-evpn1-vpn1] quit
    [*Device2-bgp-instance-evpn1] quit
    [*Device2] commit
    ```

#### Verifying the Configuration

After completing the configurations, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on Device2, Device3, and Device4 to check VXLAN tunnel information. The following example uses the command output on Device2.

```
[~Device2] display vxlan tunnel
Number of vxlan tunnel : 2
Tunnel ID   Source                Destination           State  Type          Uptime
-----------------------------------------------------------------------------------
4026531841  2.2.2.3             3.3.3.3               up     dynamic       03:12:45
4026531844  10.10.10.1            10.10.10.2            up     static        03:12:33
```

VM1s on different servers can communicate.

![](../public_sys-resources/note_3.0-en-us.png) 

The tunnel goes up only after a Layer 2 sub-interface on Device2, Device3, or Device4 is connected to a server. When there is no access server, the VXLAN tunnel state is not displayed because no IRB route is advertised.



#### Configuration Scripts

* Device1
  
  ```
  #
  sysname Device1
  #
  evpn-overlay enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   private-4-byte-as enable
   peer 192.168.2.1 as-number 200
   peer 192.168.3.1 as-number 300
   peer 192.168.4.1 as-number 200
   #
   ipv4-family unicast
    network 1.1.1.1 255.255.255.255
    peer 192.168.2.1 enable
    peer 192.168.3.1 enable
    peer 192.168.4.1 enable
  #
  bgp 100 instance evpn1
   private-4-byte-as enable
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0 
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
    peer 3.3.3.3 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise irb
    peer 4.4.4.4 reflect-client
  #
  return
  ```
* Device2
  
  ```
  #
  sysname Device2
  #
  dfs-group 1
   dual-active detection source ip 10.10.1.1 peer 10.10.1.2
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgwh\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%# 
  #
  stp mode rstp
  stp v-stp enable
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
  vlan 100
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
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   mac-address 00e0-fc12-3457
   vxlan anycast-gateway enable
   arp broadcast-detect enable
   arp collect host enable
  #
  interface vlanif100
   ip address 10.10.10.1 255.255.255.0
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk10
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface MEth0/0/0
   ip address 10.10.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 1
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  interface LoopBack1
   ip address 2.2.2.3 255.255.255.255
  #
  interface Nve1
   source 2.2.2.3
   vni 10 head-end peer-list protocol bgp
   mac-address 00e0-fc12-3456
   pip-source 10.10.10.1 peer 10.10.10.2 bypass
  #
  bgp 200
   advertise lowest-priority all-address-family peer-up  //Adjust the priority of BGP routes to the lowest level when the peer relationship goes up from down, and delay route advertisement to reduce packet loss during traffic switchback.
   private-4-byte-as enable
   peer 192.168.2.2 as-number 100
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    network 2.2.2.3 255.255.255.255
    peer 192.168.2.2 enable
    peer 192.168.2.2 allow-as-loop
  #
  bgp 100 instance evpn1
   private-4-byte-as enable
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #                                                                              
   ipv4-family vpn-instance vpn1                                                  
    import-route direct                                                           
    advertise l2vpn evpn 
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
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
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.20.1.1 255.255.255.0
   vxlan anycast-gateway enable
   arp collect host enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface 100GE1/0/2.1 mode l2
   encapsulation dot1q vid 20
   bridge-domain 20
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3
   vni 20 head-end peer-list protocol bgp
  #
  bgp 300
   advertise lowest-priority all-address-family peer-up  //Adjust the priority of BGP routes to the lowest level when the peer relationship goes up from down, and delay route advertisement to reduce packet loss during traffic switchback.
   private-4-byte-as enable
   peer 192.168.3.2 as-number 100
   #
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    peer 192.168.3.2 enable
  #
  bgp 100 instance evpn1
   private-4-byte-as enable
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #                                                                              
   ipv4-family vpn-instance vpn1                                                  
    import-route direct                                                           
    advertise l2vpn evpn 
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
  #
  return
  ```
* Device4
  
  ```
  #
  sysname Device4
  #
  dfs-group 1
   dual-active detection source ip 10.10.1.2 peer 10.10.1.1
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!=I9f8>C{!P_bhB31@7r-=jrS8c|_"(Bn~#=!!!!!!!!!!!!!!!9!!!!kx-6@.tGA(wAt/IQXl6>[g{6YlOi9$!!!!!!!!!!%+%#
  #
  stp mode rstp
  stp v-stp enable
  #
  evpn-overlay enable
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:4
    vpn-target 100:5010 export-extcommunity evpn
    vpn-target 100:5010 import-extcommunity evpn
   vxlan vni 5010
  #
  vlan 100
  #
  bridge-domain 10
   vxlan vni 10
   #
   evpn
    route-distinguisher 10:4
    vpn-target 100:10 export-extcommunity
    vpn-target 100:5010 export-extcommunity
    vpn-target 100:10 import-extcommunity
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   mac-address 00e0-fc12-3457
   vxlan anycast-gateway enable
   arp broadcast-detect enable
   arp collect host enable
  #
  interface vlanif100
   ip address 10.10.10.2 255.255.255.0
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk10
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface MEth0/0/0 
   ip address 10.10.1.2 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 1
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
  #
  interface LoopBack1
   ip address 2.2.2.3 255.255.255.255
  #
  interface Nve1
   source 2.2.2.3
   vni 10 head-end peer-list protocol bgp
   mac-address 00e0-fc12-3456
   pip-source 10.10.10.2 peer 10.10.10.1 bypass
  #
  bgp 200
   private-4-byte-as enable
   peer 192.168.4.2 as-number 100
   #
   ipv4-family unicast
    network 2.2.2.3 255.255.255.255
    network 4.4.4.4 255.255.255.255
    peer 192.168.4.2 enable
    peer 192.168.4.2 allow-as-loop
  #
  bgp 100 instance evpn1
   private-4-byte-as enable
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #                                                                              
   ipv4-family vpn-instance vpn1                                                  
    import-route direct                                                           
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
  #
  return
  ```