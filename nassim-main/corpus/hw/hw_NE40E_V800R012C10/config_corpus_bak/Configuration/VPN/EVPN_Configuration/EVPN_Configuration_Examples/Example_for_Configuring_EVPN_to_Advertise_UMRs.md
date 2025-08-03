Example for Configuring EVPN to Advertise UMRs
==============================================

This section provides an example for configuring EVPN to advertise UMR routes in an EVPN VPLS service scenario. This configuration reduces the MAC address learning pressure of the RR and aggregation devices.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001082316108__fig14669457122110), active-active EVPN VPLS over SRv6 BE is deployed on PE1, PE2, and PE3. To reduce the MAC address learning pressure of the RR and PE1, enable UMR generation on PE2 and PE3, configure PE2 and PE3 not to advertise specific MAC routes to the RR, and enable UMR forwarding on PE1. In addition, configure PE2 and PE3 to advertise only specific MAC routes to each other and configure the RR to reflect only specific MAC routes to PE2 and PE3.

**Figure 1** EVPN VPLS over SRv6 BE service![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](figure/en-us_image_0000001187371568.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding on each interface of PE1, PE2, PE3, and the RR, configure an IPv6 address for each interface, and configure an IPv4 address for each loopback interface as the EVPN source address.
2. Configure IS-IS on PE1, PE2, PE3, and the RR for IPv6 interworking.
3. Configure an EVPN instance in BD mode on each PE and bind an access-side sub-interface to the corresponding BD.
4. Enable UMR generation on PE2 and PE3, and enable UMR forwarding on PE1.
5. Configure the ESI and E-Trunk for dual-homing active-active networking. The E-Trunk uses the default encryption mode **enhanced-hmac-sha256** for authentication.
6. Establish a BGP EVPN peer relationship between each PE and the RR.
7. Configure PE2 and PE3 to advertise only specific MAC routes to each other and configure the RR to reflect only specific MAC routes to PE2 and PE3.
8. Configure SRv6 BE on each PE.
9. Configure CE2 to access PE2 and PE3 through an Eth-Trunk interface, and configure CE1 to access PE1 through a physical interface.
10. Configure IP addresses of the same network segment for CE1 and CE2. Then perform a ping operation on the network segment to trigger the local and remote PEs to learn CE-side MAC addresses.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name (evrf1)
* EVPN instance evrf1's RDs (100:1, 200:1, and 300:1) and RTs (1:1) on each PE
* BD ID (100)
* Names of SID node route locators on PE2 (PE2\_BUM and PE2\_UNICAST), names of SID node route locators on PE3 (PE3\_BUM, PE3\_UNICAST), and dynamically generated opcodes
* Length of the Args field for locators PE2\_BUM and PE3\_BUM (10 bits)

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1.
   
   ```
   <~HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:30::2 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 64
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   An IPv4 address needs to be configured for the loopback interface, because the EVPN source address needs to be an IPv4 address. The following example uses the configuration of PE1. The configurations of other PEs and the RR are similar to that of PE1. For detailed configurations, see Configuration Files.
2. Configure IS-IS on PE1, PE2, PE3, and the RR for IPv6 interworking.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-1
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.1111.1111.1111.00
   [*PE1-isis-1] ipv6 enable topology ipv6
   [*PE1-isis-1] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   The following example uses the configuration of PE1. The configurations of other PEs and the RR are similar to that of PE1. For detailed configurations, see Configuration Files.
3. Configure an EVPN instance in BD mode on each PE and bind an access-side sub-interface to the corresponding BD.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] bridge-domain 100
   [*PE1-bd100] evpn binding vpn-instance evrf1
   [*PE1-bd100] quit
   [*PE1] interface gigabitethernet 0/2/0.1 mode l2
   [*PE1-GigabitEthernet 0/2/0.1] encapsulation dot1q vid 1
   [*PE1-GigabitEthernet 0/2/0.1] rewrite pop single
   [*PE1-GigabitEthernet 0/2/0.1] bridge-domain 100
   [*PE1-GigabitEthernet 0/2/0.1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   [*PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] route-distinguisher 200:1
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] bridge-domain 100
   [*PE2-bd100] evpn binding vpn-instance evrf1
   [*PE2-bd100] quit
   [*PE2] interface Eth-Trunk10
   [*PE2-Eth-Trunk10] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet 0/1/0] eth-trunk 10
   [*PE2-GigabitEthernet 0/1/0] quit
   [*PE2] interface Eth-Trunk10.1 mode l2
   [*PE2-Eth-Trunk10.1] encapsulation dot1q vid 1
   [*PE2-Eth-Trunk10.1] rewrite pop single
   [*PE2-Eth-Trunk10.1] bridge-domain 100
   [*PE2-Eth-Trunk10.1] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 3.3.3.3
   [*PE3] evpn vpn-instance evrf1 bd-mode
   [*PE3-evpn-instance-evrf1] route-distinguisher 300:1
   [*PE3-evpn-instance-evrf1] vpn-target 1:1
   [*PE3-evpn-instance-evrf1] quit
   [*PE3] bridge-domain 100
   [*PE3-bd100] evpn binding vpn-instance evrf1
   [*PE3-bd100] quit
   [*PE3] interface Eth-Trunk10
   [*PE3-Eth-Trunk10] quit
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet 0/1/0] eth-trunk 10
   [*PE3-GigabitEthernet 0/1/0] quit
   [*PE3] interface Eth-Trunk10.1 mode l2
   [*PE3-Eth-Trunk10.1] encapsulation dot1q vid 1
   [*PE3-Eth-Trunk10.1] rewrite pop single
   [*PE3-Eth-Trunk10.1] bridge-domain 100
   [*PE3-Eth-Trunk10.1] quit
   [*PE3] commit
   ```
4. Enable UMR generation on PE2 and PE3, and enable UMR forwarding on PE1.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] bridge-domain 100
   [~PE2-bd100] umr originate detail-suppressed
   [*PE2-bd100] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bridge-domain 100
   [~PE3-bd100] umr originate detail-suppressed
   [*PE3-bd100] quit
   [*PE3] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bridge-domain 100
   [~PE1-bd100] umr forward enable
   [*PE1-bd100] quit
   [*PE1] commit
   ```
5. Configure the ESI and E-Trunk for dual-homing active-active networking.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are not advised to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] e-trunk 1
   [*PE2-e-trunk-1] peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   [*PE2-e-trunk-1] security-key cipher YsHsjx_202206
   [*PE2-e-trunk-1] quit
   [*PE2] interface eth-trunk 10
   [*PE2-Eth-Trunk10] e-trunk 1
   [*PE2-Eth-Trunk10] e-trunk mode force-master
   [*PE2-Eth-Trunk10] esi 0000.1111.2222.1111.1111
   [*PE2-Eth-Trunk10] quit
   [*PE2] commit
   [~PE2] bridge-domain 100
   [~PE2-bd100] esi 0000.1111.2222.1111.2222
   [*PE2-bd100] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] e-trunk 1
   [*PE3-e-trunk-1] peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   [*PE3-e-trunk-1] security-key cipher YsHsjx_202206
   [*PE3-e-trunk-1] quit
   [*PE3] interface eth-trunk 10
   [*PE3-Eth-Trunk10] e-trunk 1
   [*PE3-Eth-Trunk10] e-trunk mode force-master
   [*PE3-Eth-Trunk10] esi 0000.1111.2222.1111.1111
   [*PE3-Eth-Trunk10] quit
   [*PE3] commit
   [~PE3] bridge-domain 100
   [~PE3-bd100] esi 0000.1111.2222.1111.2222
   [*PE3-bd100] quit
   [*PE3] commit
   ```
6. Establish a BGP EVPN peer relationship between each PE and the RR.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] peer 2001:DB8:4::4 as-number 100
   [*PE1-bgp] peer 2001:DB8:4::4 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:4::4 enable
   [*PE1-bgp-af-evpn] peer 2001:DB8:4::4 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [*PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] peer 2001:DB8:4::4 as-number 100
   [*PE2-bgp] peer 2001:DB8:4::4 connect-interface loopback 1
   [*PE2-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE2-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:4::4 enable
   [*PE2-bgp-af-evpn] peer 2001:DB8:4::4 advertise encap-type srv6
   [*PE2-bgp-af-evpn] peer 2001:DB8:3::3 enable
   [*PE2-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [*PE3-bgp] router-id 3.3.3.3
   [*PE3-bgp] peer 2001:DB8:4::4 as-number 100
   [*PE3-bgp] peer 2001:DB8:4::4 connect-interface loopback 1
   [*PE3-bgp] peer 2001:DB8:2::2 as-number 100
   [*PE3-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*PE3-bgp] l2vpn-family evpn
   [*PE3-bgp-af-evpn] peer 2001:DB8:4::4 enable
   [*PE3-bgp-af-evpn] peer 2001:DB8:4::4 advertise encap-type srv6
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 enable
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   [*PE3-bgp-af-evpn] quit
   [*PE3-bgp] quit
   [*PE3] commit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] bgp 100
   [*RR-bgp] router-id 4.4.4.4
   [*RR-bgp] peer 2001:DB8:1::1 as-number 100
   [*RR-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*RR-bgp] peer 2001:DB8:2::2 as-number 100
   [*RR-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*RR-bgp] peer 2001:DB8:3::3 as-number 100
   [*RR-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*RR-bgp] l2vpn-family evpn
   [*RR-bgp-af-evpn] undo policy vpn-target
   [*RR-bgp-af-evpn] peer 2001:DB8:1::1 enable
   [*RR-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   [*RR-bgp-af-evpn] peer 2001:DB8:1::1 reflect-client
   [*RR-bgp-af-evpn] peer 2001:DB8:2::2 enable
   [*RR-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   [*RR-bgp-af-evpn] peer 2001:DB8:2::2 reflect-client
   [*RR-bgp-af-evpn] peer 2001:DB8:3::3 enable
   [*RR-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   [*RR-bgp-af-evpn] peer 2001:DB8:3::3 reflect-client
   [*RR-bgp-af-evpn] quit
   [*RR-bgp] quit
   [*RR] commit
   ```
7. Configure PE2 and PE3 to advertise only specific MAC routes to each other and configure the RR to reflect only specific MAC routes to PE2 and PE3.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] l2vpn-family evpn
   [~PE2-bgp-af-evpn] peer 2001:DB8:3::3 advertise evpn mac-route detail-only
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [~PE3-bgp] l2vpn-family evpn
   [~PE3-bgp-af-evpn] peer 2001:DB8:2::2 advertise evpn mac-route detail-only
   [*PE3-bgp-af-evpn] quit
   [*PE3-bgp] quit
   [*PE3] commit
   ```
   
   
   
   # Configure the RR.
   
   ```
   [~RR] bgp 100
   [~RR-bgp] l2vpn-family evpn
   [~RR-bgp-af-evpn] peer 2001:DB8:2::2 advertise evpn mac-route detail-only
   [~RR-bgp-af-evpn] peer 2001:DB8:3::3 advertise evpn mac-route detail-only
   [*RR-bgp-af-evpn] quit
   [*RR-bgp] quit
   [*RR] commit
   ```
8. Configure SRv6 BE on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator PE1_UNICAST ipv6-prefix 2001:DB8:11:: 64
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] locator PE1_BUM ipv6-prefix 2001:DB8:12:: 64 args 10
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator PE1_UNICAST
   [*PE1-isis-1] segment-routing ipv6 locator PE1_BUM auto-sid-disable
   [*PE1-isis-1] quit
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 locator PE1_BUM unicast-locator PE1_UNICAST
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*PE2-segment-routing-ipv6] locator PE2_UNICAST ipv6-prefix 2001:DB8:21:: 64
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] locator PE2_BUM ipv6-prefix 2001:DB8:22:: 64 args 10
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator PE2_UNICAST
   [*PE2-isis-1] segment-routing ipv6 locator PE2_BUM auto-sid-disable
   [*PE2-isis-1] quit
   [*PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 locator PE2_BUM unicast-locator PE2_UNICAST
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] commit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   [*PE3-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE3-segment-routing-ipv6] locator PE3_UNICAST ipv6-prefix 2001:DB8:31:: 64
   [*PE3-segment-routing-ipv6-locator] quit
   [*PE3-segment-routing-ipv6] locator PE3_BUM ipv6-prefix 2001:DB8:32:: 64 args 10
   [*PE3-segment-routing-ipv6-locator] quit
   [*PE3-segment-routing-ipv6] quit
   [*PE3] isis 1
   [*PE3-isis-1] segment-routing ipv6 locator PE3_UNICAST
   [*PE3-isis-1] segment-routing ipv6 locator PE3_BUM auto-sid-disable
   [*PE3-isis-1] quit
   [*PE3] evpn vpn-instance evrf1 bd-mode
   [*PE3-evpn-instance-evrf1] segment-routing ipv6 locator PE3_BUM unicast-locator PE3_UNICAST
   [*PE3-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE3-evpn-instance-evrf1] quit
   [*PE3] commit
   ```
9. Configure CE2 to access PE2 and PE3 through an Eth-Trunk interface, and configure CE1 to access PE1 through a physical interface.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet0/1/0.1
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 1
   [*CE1-GigabitEthernet0/1/0.1] ip address 192.168.1.1 24
   [*CE1-GigabitEthernet0/1/0.1] quit
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface Eth-Trunk10
   [*CE2-Eth-Trunk10] quit
   [*CE2] interface gigabitethernet 0/1/0
   [*CE2-GigabitEthernet0/1/0] eth-trunk 10
   [*CE2-GigabitEthernet0/1/0] quit
   [*CE2] interface gigabitethernet 0/2/0
   [*CE2-GigabitEthernet0/2/0] eth-trunk 10
   [*CE2-GigabitEthernet0/2/0] quit
   [*CE2] interface Eth-Trunk10.1
   [*CE2-Eth-Trunk10.1] vlan-type dot1q 1
   [*CE2-Eth-Trunk10.1] ip address 192.168.1.2 24
   [*CE2-Eth-Trunk10.1] quit
   [*CE2] commit
   ```
10. Configure IP addresses of the same network segment for CE1 and CE2. Then perform a ping operation on the network segment to trigger the local and remote PEs to learn CE-side MAC addresses.
    
    
    
    # Ping CE2 from CE1 (with the source and destination IP addresses being on the same network segment). The following example uses the command output on CE1.
    
    ```
    [~CE1] ping 192.168.1.2 
    ```
    ```
     PING 192.168.1.2: 56  data bytes, press CTRL_C to break                      
        Reply from 192.168.1.2: bytes=56 Sequence=1 ttl=255 time=13 ms             
        Reply from 192.168.1.2: bytes=56 Sequence=2 ttl=255 time=4 ms              
        Reply from 192.168.1.2: bytes=56 Sequence=3 ttl=255 time=3 ms              
        Reply from 192.168.1.2: bytes=56 Sequence=4 ttl=255 time=4 ms              
        Reply from 192.168.1.2: bytes=56 Sequence=5 ttl=255 time=4 ms              
    
      --- 192.168.1.12 ping statistics ---                                          
        5 packet(s) transmitted                                                     
        5 packet(s) received                                                        
        0.00% packet loss                                                           
        round-trip min/avg/max = 3/5/13 ms 
    ```
11. Verifying the Configuration
    
    
    
    Run the **display bgp evpn all routing-table mac-route** command on PE1. The command output shows that PE1 has received UMRs only from PE2 and PE3 and does not have specific MAC routes.
    
    ```
    [~PE1] display bgp evpn all routing-table mac-route
    
     Local AS number : 100
    
     BGP Local router ID is 1.1.1.1
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
    
     EVPN address family:
     Number of Mac Routes: 3
     Route Distinguisher: 100:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>    0:48:3806-eb11-0300:0:0.0.0.0                          0.0.0.0                                      
     Route Distinguisher: 200:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:0000-0000-0000:0:0.0.0.0                          2001:DB8:2::2                                
     Route Distinguisher: 300:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:0000-0000-0000:0:0.0.0.0                          2001:DB8:3::3                                
    
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 3
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:0000-0000-0000:0:0.0.0.0                          2001:DB8:2::2                                
     * i                                                          2001:DB8:3::3                                
     *>    0:48:3806-eb11-0300:0:0.0.0.0                          0.0.0.0  
    ```

#### Configuration Files

* PE1 configuration file
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE1_BUM unicast-locator PE1_UNICAST
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
   umr forward enable
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1_BUM ipv6-prefix 2001:DB8:12:: 64 args 10
   locator PE1_UNICAST ipv6-prefix 2001:DB8:11:: 64
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.1111.1111.1111.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1_BUM auto-sid-disable
   segment-routing ipv6 locator PE1_UNICAST
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 100
  #
  interface LoopBack1
   ipv6 enable
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:DB8:4::4 as-number 100
   peer 2001:DB8:4::4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:4::4 enable
    peer 2001:DB8:4::4 advertise encap-type srv6
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE2_BUM unicast-locator PE2_UNICAST
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
   umr originate detail-suppressed
   esi 0000.1111.2222.1111.2222
  #
  e-trunk 1
   priority 10
   peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   security-key cipher %^%#6Gh9KL,t[4NnY);fgQw7G<Ge"}pg|K+%]R,MM<Z*%^%#
   authentication-mode enhanced-hmac-sha256
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator PE2_BUM ipv6-prefix 2001:DB8:22:: 64 args 10
   locator PE2_UNICAST ipv6-prefix 2001:DB8:21:: 64
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.2222.2222.2222.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2_BUM auto-sid-disable
   segment-routing ipv6 locator PE2_UNICAST
   #
  #
  interface Eth-Trunk10
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.2222.1111.1111
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 100
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ip address 2.2.2.2 255.255.255.255
   ipv6 address 2001:DB8:2::2/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 2.2.2.2
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   peer 2001:DB8:4::4 as-number 100
   peer 2001:DB8:4::4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
    peer 2001:DB8:3::3 advertise evpn mac-route detail-only
    peer 2001:DB8:4::4 enable
    peer 2001:DB8:4::4 advertise encap-type srv6
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* PE3 configuration file
  ```
  #
  sysname PE3
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 300:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE3_BUM unicast-locator PE3_UNICAST
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  bridge-domain 100
   evpn binding vpn-instance evrf1
   umr originate detail-suppressed
   esi 0000.1111.2222.1111.2222
  #
  e-trunk 1
   priority 10
   peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   security-key cipher %^%#SFL6N2HY;<T]1&0E%462E(-L<)C/3I@gam-CSZVN%^%#
   authentication-mode enhanced-hmac-sha256
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE3_BUM ipv6-prefix 2001:DB8:32:: 64 args 10
   locator PE3_UNICAST ipv6-prefix 2001:DB8:31:: 64
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.3333.3333.3333.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE3_BUM auto-sid-disable
   segment-routing ipv6 locator PE3_UNICAST
   #
  #
  interface Eth-Trunk10
   e-trunk 1
   e-trunk mode force-master
   esi 0000.1111.2222.1111.1111
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 1
   rewrite pop single
   bridge-domain 100
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ip address 3.3.3.3 255.255.255.255
   ipv6 address 2001:DB8:3::3/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   peer 2001:DB8:4::4 as-number 100
   peer 2001:DB8:4::4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
    peer 2001:DB8:2::2 advertise evpn mac-route detail-only
    peer 2001:DB8:4::4 enable
    peer 2001:DB8:4::4 advertise encap-type srv6
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* RR configuration file
  ```
  #
  sysname RR
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.4444.4444.4444.00
   #
   ipv6 enable topology ipv6
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:30::1/64
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ip address 4.4.4.4 255.255.255.255
   ipv6 address 2001:DB8:4::4/64
   isis ipv6 enable 1
  #
  bgp 100
   router-id 4.4.4.4
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 reflect-client
    peer 2001:DB8:1::1 advertise encap-type srv6
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 reflect-client
    peer 2001:DB8:2::2 advertise encap-type srv6
    peer 2001:DB8:2::2 advertise evpn mac-route detail-only
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 reflect-client
    peer 2001:DB8:3::3 advertise encap-type srv6
    peer 2001:DB8:3::3 advertise evpn mac-route detail-only
  #
  return
  ```
* CE1 configuration file
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   ip address 192.168.1.1 255.255.255.0
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  interface Eth-Trunk10
  #
  interface Eth-Trunk10.1
   vlan-type dot1q 1
   ip address 192.168.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   eth-trunk 10
  #
  return
  ```