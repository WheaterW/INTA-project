Example for Configuring VXLAN in Distributed Gateway Mode Using BGP EVPN
========================================================================

This section provides an example for configuring VXLAN in distributed gateway mode using BGP EVPN.

#### Networking Requirements

Distributed VXLAN gateways can be configured to address problems that occur in legacy centralized VXLAN gateway networking, for example, forwarding paths are not optimal, or the ARP entry specification is a bottleneck.

On the network shown in [Figure 1](#EN-US_TASK_0172363834__fig_dc_vrp_vxlan_cfg_106101), an enterprise has VMs deployed in different DCs. On Server1, VM1 belongs to VLAN 10, and VM2 belongs to VLAN 20. Similarly, on Server2, VM1 belongs to VLAN 10, and VM2 belongs to VLAN 20. The gateways for VLAN 10 and VLAN 20 belong to different subnets. To allow VMs in different DCs to communicate, configure VXLAN in distributed gateway mode.

**Figure 1** Network diagram of configuring VXLAN in distributed gateway mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GigabitEthernet0/1/0 and GigabitEthernet0/1/1, respectively.

![](images/fig_dc_vrp_vxlan_cfg_106101.png)


**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| Device1 | GigabitEthernet0/1/0 | 192.168.3.2/24 |
| GigabitEthernet0/1/1 | 192.168.2.2/24 |
| LoopBack0 | 1.1.1.1/32 |
| Device2 | GigabitEthernet0/1/0 | 192.168.2.1/24 |
| LoopBack0 | 2.2.2.2/32 |
| Device3 | GigabitEthernet0/1/0 | 192.168.3.1/24 |
| LoopBack0 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP to run between Device1 and Device2 and between Device1 and Device3.
2. Configure a service access point on Device2 and Device3 to differentiate service traffic.
3. Specify Device1 as a BGP EVPN peer for Device2 and Device3.
4. Specify Device2 and Device3 as BGP EVPN peers for Device1 and configure Device2 and Device3 as RR clients.
5. Configure VPN and EVPN instances on Device2 and Device3.
6. Configure an ingress replication list on Device2 and Device3.
7. Configure Device2 and Device3 as Layer 3 VXLAN gateways.
8. Configure Device1 to exchange IRB routes with Device2 and Device3 as BGP peers.


#### Data Preparation

To complete the configuration, you need the following data.

* VMs' VLAN IDs (10 and 20)
* IP addresses of interfaces connecting devices
* BD IDs (10 and 20)
* VNI IDs (10 and 20)
* VNI ID in VPN instance (5010)

#### Procedure

1. Configure an IGP.
   
   
   
   Assign an IP address to each involved interface on Device1, Device2, and Device3 according to [Figure 1](#EN-US_TASK_0172363834__fig_dc_vrp_vxlan_cfg_106101).
   
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
   [~Device1] isis 1
   ```
   ```
   [*Device1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*Device1-isis-1] quit
   ```
   ```
   [*Device1] commit
   ```
   ```
   [~Device1] interface loopback 0
   ```
   ```
   [*Device1-LoopBack0] ip address 1.1.1.1 32
   ```
   ```
   [*Device1-LoopBack0] isis enable 1
   ```
   ```
   [*Device1-LoopBack0] quit
   ```
   ```
   [*Device1] interface GigabitEthernet0/1/0
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] ip address 192.168.3.2 24
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*Device1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Device1] interface GigabitEthernet0/1/1
   ```
   ```
   [*Device1-GigabitEthernet0/1/1] ip address 192.168.2.2 24
   ```
   ```
   [*Device1-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*Device1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Device1] commit
   ```
   
   The configurations of Device2 and Device3 are similar to that of Device1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
2. Configure a service access point on Device2 and Device3.
   
   
   
   # Configure Device2.
   
   ```
   [~Device2] bridge-domain 10
   ```
   ```
   [*Device2-bd10] quit
   ```
   ```
   [*Device2] interface GigabitEthernet0/1/1.1 mode l2
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.1] rewrite pop single
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.1] bridge-domain 10
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*Device2] commit
   ```
   ```
   [~Device2] bridge-domain 20
   ```
   ```
   [*Device2-bd20] quit
   ```
   ```
   [*Device2] interface GigabitEthernet0/1/1.2 mode l2
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.2] encapsulation dot1q vid 20
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.2] rewrite pop single
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.2] bridge-domain 20
   ```
   ```
   [*Device2-GigabitEthernet0/1/1.2] quit
   ```
   ```
   [*Device2] commit
   ```
   
   The configuration of Device3 is similar to that of Device2. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
3. Specify Device1 as a BGP EVPN peer for Device2 and Device3.
   
   # Specify a BGP EVPN peer for Device2.
   ```
   [~Device2] bgp 100
   ```
   ```
   [*Device2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*Device2-bgp] peer 1.1.1.1 connect-interface LoopBack0
   ```
   ```
   [*Device2-bgp] l2vpn-family evpn
   ```
   ```
   [*Device2-bgp-af-evpn] policy vpn-target
   ```
   ```
   [*Device2-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*Device2-bgp-af-evpn] peer 1.1.1.1 advertise encap-type vxlan
   ```
   ```
   [*Device2-bgp-af-evpn] quit
   ```
   ```
   [*Device2-bgp] quit
   ```
   ```
   [*Device2] commit
   ```
   
   The configuration of Device3 is similar to that of Device2. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
4. On Device1, specify Device2 and Device3 as BGP EVPN peers and configure them as RR clients.
   
   # Specify BGP EVPN peers for Device1.
   ```
   [~Device1] bgp 100
   ```
   ```
   [*Device1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*Device1-bgp] peer 2.2.2.2 connect-interface LoopBack0
   ```
   ```
   [*Device1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*Device1-bgp] peer 3.3.3.3 connect-interface LoopBack0
   ```
   ```
   [*Device1-bgp] l2vpn-family evpn
   ```
   ```
   [*Device1-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*Device1-bgp-af-evpn] peer 2.2.2.2 advertise encap-type vxlan
   ```
   ```
   [*Device1-bgp-af-evpn] peer 2.2.2.2 reflect-client
   ```
   ```
   [*Device1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*Device1-bgp-af-evpn] peer 3.3.3.3 advertise encap-type vxlan
   ```
   ```
   [*Device1-bgp-af-evpn] peer 3.3.3.3 reflect-client
   ```
   ```
   [*Device1-bgp-af-evpn] undo policy vpn-target
   ```
   ```
   [*Device1-bgp-af-evpn] quit
   ```
   ```
   [*Device1-bgp] quit
   ```
   ```
   [*Device1] commit
   ```
5. Configure VPN and EVPN instances on Device2 and Device3.
   
   
   
   # Configure Device2.
   
   ```
   [~Device2] ip vpn-instance vpn1
   ```
   ```
   [*Device2-vpn-instance-vpn1] vxlan vni 5010
   ```
   ```
   [*Device2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*Device2-vpn-instance-vpn1-af-ipv4] route-distinguisher 11:11
   ```
   ```
   [*Device2-vpn-instance-vpn1-af-ipv4] vpn-target 11:1 evpn
   ```
   ```
   [*Device2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*Device2-vpn-instance-vpn1] quit
   ```
   ```
   [*Device2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*Device2-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*Device2-evpn-instance-evrf1] vpn-target 10:1
   ```
   ```
   [*Device2-evpn-instance-evrf1] vpn-target 11:1 export-extcommunity
   ```
   ```
   [*Device2-evpn-instance-evrf1] quit
   ```
   ```
   [*Device2] bridge-domain 10
   ```
   ```
   [*Device2-bd10] vxlan vni 10 split-horizon-mode
   ```
   ```
   [*Device2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*Device2-bd10] quit
   ```
   ```
   [*Device2] commit
   ```
   ```
   [*Device2] evpn vpn-instance evrf2 bd-mode
   ```
   ```
   [*Device2-evpn-instance-evrf2] route-distinguisher 20:1
   ```
   ```
   [*Device2-evpn-instance-evrf2] vpn-target 20:1
   ```
   ```
   [*Device2-evpn-instance-evrf2] vpn-target 11:1 export-extcommunity
   ```
   ```
   [*Device2-evpn-instance-evrf2] quit
   ```
   ```
   [*Device2] bridge-domain 20
   ```
   ```
   [*Device2-bd20] vxlan vni 20 split-horizon-mode
   ```
   ```
   [*Device2-bd20] evpn binding vpn-instance evrf2
   ```
   ```
   [*Device2-bd20] quit
   ```
   ```
   [*Device2] commit
   ```
   
   The configuration of Device3 is similar to that of Device2. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
6. Configure an ingress replication list on Device2 and Device3.
   
   # Configure an ingress replication list on Device2.
   ```
   [~Device2] interface nve 1
   ```
   ```
   [*Device2-Nve1] source 2.2.2.2
   ```
   ```
   [*Device2-Nve1] vni 10 head-end peer-list protocol bgp
   ```
   ```
   [*Device2-Nve1] vni 20 head-end peer-list protocol bgp
   ```
   ```
   [*Device2-Nve1] quit
   ```
   ```
   [*Device2] commit
   ```
   
   The configuration of Device3 is similar to that of Device2. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
7. Configure Device2 and Device3 as Layer 3 VXLAN gateways.
   
   
   
   # Configure Device2.
   
   ```
   [~Device2] interface Vbdif10
   ```
   ```
   [*Device2-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*Device2-Vbdif10] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*Device2-Vbdif10] vxlan anycast-gateway enable
   ```
   ```
   [*Device2-Vbdif10] arp collect host enable
   ```
   ```
   [*Device2-Vbdif10] quit
   ```
   ```
   [*Device2] commit
   ```
   ```
   [~Device2] interface Vbdif20
   ```
   ```
   [*Device2-Vbdif20] ip binding vpn-instance vpn1
   ```
   ```
   [*Device2-Vbdif20] ip address 10.2.1.1 255.255.255.0
   ```
   ```
   [*Device2-Vbdif20] vxlan anycast-gateway enable
   ```
   ```
   [*Device2-Vbdif20] arp collect host enable
   ```
   ```
   [*Device2-Vbdif20] quit
   ```
   ```
   [*Device2] commit
   ```
   
   The configuration of Device3 is similar to that of Device2. Note that the IP addresses of VBDIF interfaces on Device2 and Device3 must belong to different subnets. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
8. Configure Device1 to exchange IRB routes with Device2 and Device3 as BGP peers.
   
   
   
   # Configure Device1.
   
   ```
   [~Device1] bgp 100
   ```
   ```
   [~Device1-bgp] l2vpn-family evpn
   ```
   ```
   [~Device1-bgp-af-evpn] peer 2.2.2.2 advertise irb
   ```
   ```
   [*Device1-bgp-af-evpn] peer 3.3.3.3 advertise irb
   ```
   ```
   [*Device1-bgp-af-evpn] quit
   ```
   ```
   [*Device1-bgp] quit
   ```
   ```
   [*Device1] commit
   ```
   
   # Configure Device2.
   
   ```
   [~Device2] bgp 100
   ```
   ```
   [~Device2-bgp] l2vpn-family evpn
   ```
   ```
   [~Device2-bgp-af-evpn] peer 1.1.1.1 advertise irb
   ```
   ```
   [*Device2-bgp-af-evpn] quit
   ```
   ```
   [*Device2-bgp] quit
   ```
   ```
   [*Device2] commit
   ```
   
   The configuration of Device3 is similar to that of Device2. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172363834__section_dc_vrp_vxlan_cfg_106101).
9. Verify the configuration.
   
   
   
   After the configuration is complete, run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on Device2 and Device3 to check VXLAN tunnel information. The following example uses the command output on Device2.
   
   ```
   [*Device2] display vxlan tunnel
   ```
   ```
   Number of vxlan tunnel : 1
   Tunnel ID   Source           Destination      State  Type     Uptime
   --------------------------------------------------------------------
   4026531841  2.2.2.2          3.3.3.3          up     dynamic  0026h29m
   ```
   
   Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) command to check EVPN route information.
   
   ```
   [*Device2]display bgp evpn all routing-table
    Local AS number : 100
   
    BGP Local router ID is 192.168.2.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:
    Number of Mac Routes: 6
    Route Distinguisher: 10:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:a416-e788-f8ca:0:0.0.0.0                          0.0.0.0                                      
    *>    0:48:c4b8-b4aa-a9dd:0:0.0.0.0                          0.0.0.0                                      
    *>    0:48:c4b8-b4aa-a9dd:32:10.1.1.10                       0.0.0.0                                      
    Route Distinguisher: 20:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:c4b8-b4aa-a9de:0:0.0.0.0                          0.0.0.0                                      
    *>    0:48:c4b8-b4aa-a9de:32:10.2.1.11                       0.0.0.0
    Route Distinguisher: 30:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>i   0:48:c4b8-b4aa-aa9c:0:0.0.0.0                          3.3.3.3                                      
    *>i   0:48:c4b8-b4aa-aa9c:32:10.1.1.11                       3.3.3.3                                      
    *>i   0:48:d44f-6750-a2e1:0:0.0.0.0                          3.3.3.3
    Route Distinguisher: 40:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>i   0:48:c4b8-b4aa-a9df:0:0.0.0.0                          3.3.3.3                                      
    *>i   0:48:c4b8-b4aa-a9df:32:10.2.1.10                       3.3.3.3                                      
   
   
    EVPN-Instance evrf1:
    Number of Mac Routes: 6
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:a416-e788-f8ca:0:0.0.0.0                          0.0.0.0                                      
    *>    0:48:c4b8-b4aa-a9dd:0:0.0.0.0                          0.0.0.0                                      
    *>    0:48:c4b8-b4aa-a9dd:32:10.1.1.10                       0.0.0.0                                      
    *>i   0:48:c4b8-b4aa-aa9c:0:0.0.0.0                          3.3.3.3                                      
    *>i   0:48:c4b8-b4aa-aa9c:32:10.1.1.11                       3.3.3.3                                      
    *>i   0:48:d44f-6750-a2e1:0:0.0.0.0                          3.3.3.3                                      
   
    EVPN-Instance evrf2:
    Number of Mac Routes: 4
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:a416-e788-f8ca:0:0.0.0.0                          0.0.0.0                                      
    *>    0:48:c4b8-b4aa-a9dd:32:10.1.1.11                       0.0.0.0                                      
    *>i   0:48:c4b8-b4aa-aa9c:0:0.0.0.0                          3.3.3.3                                      
    *>i   0:48:c4b8-b4aa-aa9c:32:10.1.1.10                       3.3.3.3                                      
   
    EVPN address family:
    Number of Inclusive Multicast Routes: 2
    Route Distinguisher: 10:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:2.2.2.2                                           0.0.0.0
    Route Distinguisher: 20:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:3.3.3.3                                           3.3.3.3                                      
   
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:2.2.2.2                                           0.0.0.0
    *>i   0:32:3.3.3.3                                           3.3.3.3  
   ```
   
   Run the [**display bgp vpnv4 all routing-table**](cmdqueryname=display+bgp+vpnv4+all+routing-table) command to check VPN route information.
   
   ```
   [*Device2]display bgp vpnv4 all routing-table
   
    BGP Local router ID is 192.168.2.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
    
    
    VPN-Instance vrf1, Router ID 192.168.2.1:
    
    Total Number of Routes: 2
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
    *>     10.1.1.11/32        3.3.3.3                        0                     0       ?
    *>     10.2.1.10/32        3.3.3.3                        0                     0       ?
   ```
   
   After the configuration is complete, VMs belonging to different servers on different subnets can communicate. On the distributed gateway Device2, use the vbdif1 gateway address to ping VM2 on Server2.
   
   ```
   [~Device2] ping -vpn-instance vpn1 âa 10.1.1.1 10.2.1.10 
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

#### Configuration Files

* Device1 configuration file
  
  ```
  #
  sysname Device1
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   isis enable 1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise encap-type vxlan
    peer 2.2.2.2 advertise irb
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise encap-type vxlan
    peer 3.3.3.3 advertise irb
    peer 3.3.3.3 reflect-client
  #
  return
  ```
* Device2 configuration file
  
  ```
  #
  sysname Device2
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 10:1 export-extcommunity
   vpn-target 11:1 export-extcommunity
   vpn-target 10:1 import-extcommunity
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 20:1
   vpn-target 20:1 export-extcommunity
   vpn-target 11:1 export-extcommunity
   vpn-target 20:1 import-extcommunity
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf2
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp collect host enable
   vxlan anycast-gateway enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp collect host enable
   vxlan anycast-gateway enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/1.2 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  interface Nve1
   source 2.2.2.2
   vni 10 head-end peer-list protocol bgp
   vni 20 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise encap-type vxlan
    peer 1.1.1.1 advertise irb
  #
  return
  ```
* Device3 configuration file
  
  ```
  #
  sysname Device3
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 22:22
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 30:1
   vpn-target 10:1 export-extcommunity
   vpn-target 11:1 export-extcommunity
   vpn-target 10:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 40:1
   vpn-target 20:1 export-extcommunity
   vpn-target 11:1 export-extcommunity
   vpn-target 20:1 import-extcommunity
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf2
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.2 255.255.255.0
   arp collect host enable
   vxlan anycast-gateway enable
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.2 255.255.255.0
   arp collect host enable
   vxlan anycast-gateway enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/1.2 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  interface Nve1
   source 3.3.3.3
   vni 20 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   l2vpn-family evpn
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise encap-type vxlan
    peer 1.1.1.1 advertise irb
  #
  return
  ```