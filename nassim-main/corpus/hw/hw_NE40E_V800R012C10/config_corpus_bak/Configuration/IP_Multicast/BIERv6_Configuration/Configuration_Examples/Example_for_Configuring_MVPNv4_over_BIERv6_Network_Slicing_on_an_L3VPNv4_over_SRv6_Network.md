Example for Configuring MVPNv4 over BIERv6 Network Slicing on an L3VPNv4 over SRv6 Network
==========================================================================================

This section provides an example for configuring MVPNv4 over BIERv6 and BIERv6 network slicing on a unicast L3VPNv4 over SRv6 network.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001437036285__fig35284409229), L3VPNv4 over SRv6 has been deployed. It is required that MVPNv4 over BIERv6 be deployed on the existing network. Multicast service traffic in VPNA needs to be isolated from other multicast service traffic in BIERv6 tunnels. In addition, the multicast stream with the multicast source address 192.168.1.100 and multicast group address 225.0.0.1 in VPNA needs to be isolated from other multicast streams in VPNA, and independent SLA assurance is implemented. In this case, the network slicing function can be deployed in BIERv6 tunnels to carry different multicast service traffic through different slice planes.

**Figure 1** Configuring MVPNv4 over BIERv6 network slicing![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001387036516.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. (Optional) Configure L3VPNv4 over SRv6 and ensure that the unicast VPN runs properly. If the unicast network has been configured, skip this step.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on PE1, PE2, PE3, and the P.
3. Establish BGP MVPN peer relationships between PEs.
4. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel.
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
6. Enable PIM on PEs.
7. Configure network slice instances, specify basic interfaces, and create network slice interfaces on PE1, PE2, PE3, and the P.
8. Enable BIERv6 network slicing on the ingress PE1 and transit node P of the BIERv6 tunnel.
9. Specify a network slice ID for a VPN instance and another network slice ID for a multicast stream in the VPN instance on the BIERv6 tunnel ingress PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* Addresses of key interfaces on each device, as shown in [Figure 1](#EN-US_TASK_0000001437036285__fig35284409229)
* ID (1) of the public network IS-IS process, in a Level-2 area
* VPN instance name (VPNA) on PE1, PE2, and PE3
* PE2's BFR-ID (2), PE3's BFR-ID (3), sub-domain ID (0), BSL (256), and Max-SI (0)
* Network slice ID (20) for VPNA, and network slice ID (30) for the (192.168.1.100, 225.0.0.1) multicast stream in VPNA

#### Procedure

1. (Optional) Configure L3VPNv4 over SRv6.
   
   
   
   This step is a part of configuring the unicast network, and its content is for reference only. In most cases, the unicast network has been configured before multicast services are deployed. If this is the case, skip this step and contact the configuration personnel for the configuration data related to the multicast services. For details about how to configure a unicast network, see **Segment Routing IPv6 Configuration** in the Configuration Guide.
   
   # Enable IPv6 forwarding on each interface and configure an IPv6 address for each interface. The configuration of PE1 is used as an example. The configurations of PE2, PE3, and the P are similar to the configuration of PE1. For configuration details, see configuration files in this section. Similar details will be omitted in the rest of the document.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:db8:10::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   # Configure IS-IS. The configuration of PE1 is used as an example. The configurations of PE2, PE3, and the P are similar to the configuration of PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-2
   [*PE1-isis-1] cost-style wide
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
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
   
   # Configure a VPN instance on PEs, enable the IPv4 address family for the instance, and bind the interfaces that connect the PEs to a CE to the VPN instance. The configuration of PE1 is used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1.
   
   ```
   [~PE1] ip vpn-instance VPNA
   [*PE1-vpn-instance-VPNA] ipv4-family
   [*PE1-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:1
   [*PE1-vpn-instance-VPNA-af-ipv4] vpn-target 111:1 both
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   [*PE1-vpn-instance-VPNA] quit
   [*PE1] interface gigabitethernet 0/1/1
   [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
   [*PE1-GigabitEthernet0/1/1] ip address 192.168.1.1 24
   [*PE1-GigabitEthernet0/1/1] quit
   [*PE1] commit
   ```
   # Establish an EBGP peer relationship between each PE and its connected CE. The establishment of an EBGP peer relationship between PE1 and CE1 is used as an example. The establishment of an EBGP peer relationship between PE2 and CE2, and between PE3 and CE3 is similar to that between PE1 and CE1.
   * Configure CE1.
     ```
     [~CE1] bgp 65410
     [*CE1-bgp] router-id 11.11.11.11
     [*CE1-bgp] peer 192.168.1.1 as-number 100
     [*CE1-bgp] quit
     [*CE1] commit
     ```
   * Configure PE1.
     ```
     [~PE1] bgp 100
     [*PE1-bgp] router-id 1.1.1.1
     [*PE1-bgp] ipv4-family vpn-instance VPNA
     [*PE1-bgp-VPNA] peer 192.168.1.2 as-number 65410
     [*PE1-bgp-VPNA] import-route direct
     [*PE1-bgp-VPNA] commit
     [~PE1-bgp-VPNA] quit
     [~PE1-bgp] quit
     ```
   
   # Establish an MP-IBGP peer relationship between PE1 and PE2 and between PE1 and PE3. The configuration of PE1 is used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1. After the [**peer enable**](cmdqueryname=peer+enable) command is run, the system displays a confirmation message. Enter **Y** in this case. Similar details will be omitted in the rest of the document.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] peer 2001:db8:20::1 as-number 100
   [*PE1-bgp] peer 2001:db8:30::1 as-number 100
   [*PE1-bgp] peer 2001:db8:20::1 connect-interface loopback 1
   [*PE1-bgp] peer 2001:db8:30::1 connect-interface loopback 1
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:db8:20::1 enable
   [*PE1-bgp-af-vpnv4] peer 2001:db8:30::1 enable
   [*PE1-bgp-af-vpnv4] commit
   [~PE1-bgp-af-vpnv4] quit
   [~PE1-bgp] quit
   ```
   
   # Configure SRv6 SIDs, and configure PEs to add SIDs to the VPN routes to be advertised. The configurations of PE1 and P are used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:db8:10::1
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:db8:100:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] opcode ::111 end psp
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:db8:20::1 prefix-sid
   [*PE1-bgp-af-vpnv4] peer 2001:db8:30::1 prefix-sid
   [*PE1-bgp-af-vpnv4] quit
   [*PE1-bgp] ipv4-family vpn-instance VPNA
   [*PE1-bgp-VPNA] segment-routing ipv6 best-effort
   [*PE1-bgp-VPNA] segment-routing ipv6 locator PE1
   [*PE1-bgp-VPNA] commit
   [~PE1-bgp-VPNA] quit
   [~PE1-bgp] quit
   [~PE1] isis 1
   [~PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable 
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   [~P] segment-routing ipv6
   [*P-segment-routing-ipv6] encapsulation source-address 2001:db8:40::1
   [*P-segment-routing-ipv6] locator P ipv6-prefix 2001:db8:400:: 64 static 32
   [*P-segment-routing-ipv6-locator] opcode ::444 end psp
   [*P-segment-routing-ipv6-locator] quit
   [*P-segment-routing-ipv6] quit
   [*P] isis 1
   [*P-isis-1] segment-routing ipv6 locator P auto-sid-disable
   [*P-isis-1] commit
   [~P-isis-1] quit
   ```
   
   # Perform other unicast network configurations based on unicast service requirements.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In an MVPNv4 over BIERv6 scenario, if routes sent by a multicast source CE to a root PE carry Source AS Extended Community and VRF Route Import Extended Community attributes and the root PE needs to advertise only locally configured Source AS Extended Community and VRF Route Import Extended Community attributes among extended community attributes in the routes to be sent to a leaf PE, run the [**attr-set**](cmdqueryname=attr-set) command in the BGP-VPN instance IPv4 address family view on the root PE.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on PE1, PE2, PE3, and the P.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bier
   [*PE1-bier] sub-domain 0 ipv6
   [*PE1-bier-sub-domain-0-ipv6] bfr-id 1
   [*PE1-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   [*PE1-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   [*PE1-bier-sub-domain-0-ipv6] end-bier locator PE1 sid 2001:db8:100::1
   [*PE1-bier-sub-domain-0-ipv6] protocol isis
   [*PE1-bier-sub-domain-0-ipv6] quit
   [*PE1-bier] quit
   [*PE1] isis 1
   [*PE1-isis-1] bier enable
   [*PE1-isis-1] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bier
   [*PE2-bier] sub-domain 0 ipv6
   [*PE2-bier-sub-domain-0-ipv6] bfr-id 2
   [*PE2-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   [*PE2-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   [*PE2-bier-sub-domain-0-ipv6] end-bier locator PE2 sid 2001:db8:200::1
   [*PE2-bier-sub-domain-0-ipv6] protocol isis
   [*PE2-bier-sub-domain-0-ipv6] quit
   [*PE2-bier] quit
   [*PE2] isis 1
   [*PE2-isis-1] bier enable
   [*PE2-isis-1] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bier
   [*PE3-bier] sub-domain 0 ipv6
   [*PE3-bier-sub-domain-0-ipv6] bfr-id 3
   [*PE3-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   [*PE3-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   [*PE3-bier-sub-domain-0-ipv6] end-bier locator PE3 sid 2001:db8:300::1
   [*PE3-bier-sub-domain-0-ipv6] protocol isis
   [*PE3-bier-sub-domain-0-ipv6] quit
   [*PE3-bier] quit
   [*PE3] isis 1
   [*PE3-isis-1] bier enable
   [*PE3-isis-1] quit
   [*PE3] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] bier
   [*P-bier] sub-domain 0 ipv6
   [*P-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   [*P-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   [*P-bier-sub-domain-0-ipv6] end-bier locator P sid 2001:db8:400::1
   [*P-bier-sub-domain-0-ipv6] protocol isis
   [*P-bier-sub-domain-0-ipv6] quit
   [*P-bier] quit
   [*P] isis 1
   [*P-isis-1] bier enable
   [*P-isis-1] quit
   [*P] commit
   ```
3. Establish BGP MVPN peer relationships between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] ipv4-family mvpn
   [*PE1-bgp-af-mvpn] peer 2001:db8:20::1 enable
   [*PE1-bgp-af-mvpn] peer 2001:db8:30::1 enable
   [*PE1-bgp-af-mvpn] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] ipv4-family mvpn
   [*PE2-bgp-af-mvpn] peer 2001:db8:10::1 enable
   [*PE2-bgp-af-mvpn] quit
   [*PE2-bgp] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [~PE3-bgp] ipv4-family mvpn
   [*PE3-bgp-af-mvpn] peer 2001:db8:10::1 enable
   [*PE3-bgp-af-mvpn] quit
   [*PE3-bgp] quit
   [*PE3] commit
   ```
   
   # Check information about BGP MVPN peers. The command output shows that a BGP MVPN peer relationship has been established between PE1 and PE2 and between PE1 and PE3.
   
   ```
   [~PE1]display bgp mvpn all peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:20::1                   4         100   41      43    0 00:08:08        Established      0
     2001:DB8:30::1                   4         100   29      32    0 00:07:15        Established      0
   ```
4. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] multicast mvpn ipv6-underlay 2001:db8:10::1
   [*PE1] ip vpn-instance VPNA
   [*PE1-vpn-instance-VPNA] ipv4-family
   [*PE1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] ipv6 underlay enable
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] src-dt4 locator PE1 sid 2001:db8:100::2
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] bier sub-domain 0 bsl 256
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   [*PE1-vpn-instance-VPNA] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] multicast mvpn ipv6-underlay 2001:db8:20::1
   [*PE2] ip vpn-instance VPNA
   [*PE2-vpn-instance-VPNA] ipv4-family
   [*PE2-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   [*PE2-vpn-instance-VPNA-af-ipv4] mvpn
   [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
   [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] ipv6 underlay enable
   [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
   [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] quit
   [*PE2-vpn-instance-VPNA-af-ipv4] quit
   [*PE2-vpn-instance-VPNA] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] multicast mvpn ipv6-underlay 2001:db8:30::1
   [*PE3] ip vpn-instance VPNA
   [*PE3-vpn-instance-VPNA] ipv4-family
   [*PE3-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   [*PE3-vpn-instance-VPNA-af-ipv4] mvpn
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] ipv6 underlay enable
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] quit
   [*PE3-vpn-instance-VPNA-af-ipv4] quit
   [*PE3-vpn-instance-VPNA] quit
   [*PE3] commit
   ```
   
   # Check I-PMSI tunnel information of MVPN services in a specified VPN instance. The command output shows that an I-PMSI tunnel has been established, with PE1 as the root node and PE2 and PE3 as leaf nodes.
   
   ```
   [~PE1]display mvpn vpn-instance VPNA ipmsi
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: BIER IPv6
   Tunnel state: Up
   Src-dt4 SID: 2001:DB8:100::2 
   Sub-domain ID: 0
   BFR-ID: 1
   BFR prefix: 2001:DB8:10::1
   Bit string ID: 1
   Root: 2001:DB8:10::1 (local) 
   Leaf: 
     1: 2001:DB8:20::1 (BFR-ID: 2, BFR prefix: 2001:DB8:20::1)
     2: 2001:DB8:30::1 (BFR-ID: 3, BFR prefix: 2001:DB8:30::1)
   ```
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance VPNA
   [*PE1-vpn-instance-VPNA] ipv4-family
   [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] group 225.1.1.0 24 source 192.168.11.0 24 threshold 10 bier 
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] switch-delay 20
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] holddown-time 80
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] quit
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   [*PE1-vpn-instance-VPNA] quit
   [*PE1] commit
   ```
6. Enable PIM on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/1
   [~PE1-GigabitEthernet0/1/1] pim sm
   [*PE1-GigabitEthernet0/1/1] quit
   [*PE1] interface LoopBack2
   [*PE1-Loopback2] ip binding vpn-instance VPNA
   [*PE1-Loopback2] ip address 10.1.1.1 255.255.255.255
   [*PE1-Loopback2] pim sm 
   [*PE1-Loopback2] quit
   [*PE1] pim vpn-instance VPNA
   [*PE1-pim-VPNA] static-rp 10.1.1.1
   [*PE1-pim-VPNA] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/1/1
   [~PE2-GigabitEthernet0/1/1] pim sm
   [*PE2-GigabitEthernet0/1/1] quit
   [*PE2] pim vpn-instance VPNA
   [*PE2-pim-VPNA] static-rp 10.1.1.1
   [*PE2-pim-VPNA] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface gigabitethernet 0/1/1
   [~PE3-GigabitEthernet0/1/1] pim sm
   [*PE3-GigabitEthernet0/1/1] quit
   [*PE3] pim vpn-instance VPNA
   [*PE3-pim-VPNA] static-rp 10.1.1.1
   [*PE3-pim-VPNA] quit
   [*PE3] commit
   ```
   
   # Check S-PMSI tunnel information of MVPN services in a specified VPN instance. The command output on PE2 shows the S-PMSI tunnel and multicast user information.
   
   ```
   [~PE2]display mvpn vpn-instance VPNA spmsi verbose
   MVPN local S-PMSI information for VPN-Instance : VPNA 
    Total number of tunnel: 1 
    S-PMSI A-D Route Type: -- 
    Tunnel type: BIER IPv6 
    Tunnel state: -- 
    Src-dt4 SID: 2001:DB8:100::1 
    Sub-domain ID: 0 
    BFR-ID: 1 
    BFR prefix: 2001:DB8:10::1 
    Root: 2001:DB8:10::1 
    Leaf: 
      1: 2001:DB8:20::1 (BFR-ID: 2, BFR prefix: 2001:DB8:20::1)(local)
    Total number of (S, G): 1 
        1. (192.168.11.100, 225.1.1.1) 
   ```
7. Configure network slice instances, specify basic interfaces, and create network slice interfaces on PE1, PE2, PE3, and the P. The configurations of PE1 and P are used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1. 
   
   # Configure PE1.
   ```
   [~PE1] network-slice instance 10
   [*PE1-network-slice-instance-10] description Basic
   [*PE1-network-slice-instance-10] quit
   [*PE1] network-slice instance 20
   [*PE1-network-slice-instance-20] description VPNA
   [*PE1-network-slice-instance-20] quit
   [*PE1] network-slice instance 30
   [*PE1-network-slice-instance-30] description SG
   [*PE1-network-slice-instance-30] quit
   [*PE1] interface gigabitethernet 0/1/0
   [*PE1-GigabitEthernet0/1/0] network-slice 10 data-plane
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/1/0.1
   [*PE1-GigabitEthernet0/1/0.1] vlan-type dot1q 11
   [*PE1-GigabitEthernet0/1/0.1] ipv6 enable
   [*PE1-GigabitEthernet0/1/0.1] ipv6 address auto link-local
   [*PE1-GigabitEthernet0/1/0.1] mode channel enable 
   [*PE1-GigabitEthernet0/1/0.1] mode channel bandwidth 500 
   [*PE1-GigabitEthernet0/1/0.1] basic-slice 10 
   [*PE1-GigabitEthernet0/1/0.1] network-slice 20 data-plane 
   [*PE1-GigabitEthernet0/1/0.1] quit
   [*PE1] interface gigabitethernet 0/1/0.2
   [*PE1-GigabitEthernet0/1/0.2] vlan-type dot1q 22
   [*PE1-GigabitEthernet0/1/0.2] ipv6 enable
   [*PE1-GigabitEthernet0/1/0.2] ipv6 address auto link-local
   [*PE1-GigabitEthernet0/1/0.2] mode channel enable 
   [*PE1-GigabitEthernet0/1/0.2] mode channel bandwidth 500 
   [*PE1-GigabitEthernet0/1/0.2] basic-slice 10 
   [*PE1-GigabitEthernet0/1/0.2] network-slice 30 data-plane 
   [*PE1-GigabitEthernet0/1/0.2] quit
   [*PE1] commit
   ```
   
   
   # Configure the P.
   ```
   [~P] network-slice instance 10
   [*P-network-slice-instance-10] description Basic
   [*P-network-slice-instance-10] quit
   [*P] network-slice instance 20
   [*P-network-slice-instance-20] description VPNA
   [*P-network-slice-instance-20] quit
   [*P] network-slice instance 30
   [*P-network-slice-instance-30] description SG
   [*P-network-slice-instance-30] quit
   [*P] interface gigabitethernet 0/1/0
   [*P-GigabitEthernet0/1/0] network-slice 10 data-plane
   [*P-GigabitEthernet0/1/0] quit
   [*P] interface gigabitethernet 0/1/0.1
   [*P-GigabitEthernet0/1/0.1] vlan-type dot1q 11
   [*P-GigabitEthernet0/1/0.1] ipv6 enable
   [*P-GigabitEthernet0/1/0.1] ipv6 address auto link-local
   [*P-GigabitEthernet0/1/0.1] mode channel enable 
   [*P-GigabitEthernet0/1/0.1] mode channel bandwidth 500 
   [*P-GigabitEthernet0/1/0.1] basic-slice 10 
   [*P-GigabitEthernet0/1/0.1] network-slice 20 data-plane 
   [*P-GigabitEthernet0/1/0.1] quit
   [*P] interface gigabitethernet 0/1/0.2
   [*P-GigabitEthernet0/1/0.2] vlan-type dot1q 22
   [*P-GigabitEthernet0/1/0.2] ipv6 enable
   [*P-GigabitEthernet0/1/0.2] ipv6 address auto link-local
   [*P-GigabitEthernet0/1/0.2] mode channel enable 
   [*P-GigabitEthernet0/1/0.2] mode channel bandwidth 500 
   [*P-GigabitEthernet0/1/0.2] basic-slice 10 
   [*P-GigabitEthernet0/1/0.2] network-slice 30 data-plane 
   [*P-GigabitEthernet0/1/0.2] quit
   [*P] interface gigabitethernet 0/1/1
   [*P-GigabitEthernet0/1/1] network-slice 10 data-plane
   [*P-GigabitEthernet0/1/1] quit
   [*P] interface gigabitethernet 0/1/1.1
   [*P-GigabitEthernet0/1/1.1] vlan-type dot1q 11
   [*P-GigabitEthernet0/1/1.1] ipv6 enable
   [*P-GigabitEthernet0/1/1.1] ipv6 address auto link-local
   [*P-GigabitEthernet0/1/1.1] mode channel enable 
   [*P-GigabitEthernet0/1/1.1] mode channel bandwidth 500 
   [*P-GigabitEthernet0/1/1.1] basic-slice 10 
   [*P-GigabitEthernet0/1/1.1] network-slice 20 data-plane 
   [*P-GigabitEthernet0/1/1.1] quit
   [*P] interface gigabitethernet 0/1/1.2
   [*P-GigabitEthernet0/1/1.2] vlan-type dot1q 22
   [*P-GigabitEthernet0/1/1.2] ipv6 enable
   [*P-GigabitEthernet0/1/1.2] ipv6 address auto link-local
   [*P-GigabitEthernet0/1/1.2] mode channel enable 
   [*P-GigabitEthernet0/1/1.2] mode channel bandwidth 500 
   [*P-GigabitEthernet0/1/1.2] basic-slice 10 
   [*P-GigabitEthernet0/1/1.2] network-slice 30 data-plane 
   [*P-GigabitEthernet0/1/1.2] quit
   [*P] interface gigabitethernet 0/1/2
   [*P-GigabitEthernet0/1/2] network-slice 10 data-plane
   [*P-GigabitEthernet0/1/2] quit
   [*P] interface gigabitethernet 0/1/2.1
   [*P-GigabitEthernet0/1/2.1] vlan-type dot1q 11
   [*P-GigabitEthernet0/1/2.1] ipv6 enable
   [*P-GigabitEthernet0/1/2.1] ipv6 address auto link-local
   [*P-GigabitEthernet0/1/2.1] mode channel enable 
   [*P-GigabitEthernet0/1/2.1] mode channel bandwidth 500 
   [*P-GigabitEthernet0/1/2.1] basic-slice 10 
   [*P-GigabitEthernet0/1/2.1] network-slice 20 data-plane 
   [*P-GigabitEthernet0/1/2.1] quit
   [*P] interface gigabitethernet 0/1/2.2
   [*P-GigabitEthernet0/1/2.2] vlan-type dot1q 22
   [*P-GigabitEthernet0/1/2.2] ipv6 enable
   [*P-GigabitEthernet0/1/2.2] ipv6 address auto link-local
   [*P-GigabitEthernet0/1/2.2] mode channel enable 
   [*P-GigabitEthernet0/1/2.2] mode channel bandwidth 500 
   [*P-GigabitEthernet0/1/2.2] basic-slice 10 
   [*P-GigabitEthernet0/1/2.2] network-slice 30 data-plane 
   [*P-GigabitEthernet0/1/2.2] quit
   [*P1] commit
   ```
8. Enable BIERv6 network slicing on PE1 and the P. Use PE1 as an example and refer to PE1's configuration to configure the P.
   
   
   ```
   [~PE1] bier ipv6 network-slice enable
   [*PE1] commit
   ```
9. Specify a network slice ID for a VPN instance and another network slice ID for a multicast stream in the VPN instance on PE1.
   
   
   ```
   [~PE1] ip vpn-instance VPNA
   [~PE1-vpn-instance-VPNA] ipv4-family
   [~PE1-vpn-instance-VPNA-af-ipv4] mvpn
   [~PE1-vpn-instance-VPNA-af-ipv4-mvpn] bier ipv6 network-slice 20
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] bier ipv6 group 225.0.0.1 source 192.168.1.100 network-slice 30
   [*PE1] commit
   ```
10. Verify the configuration.
    
    Run the **display mvpn all-instance ingress bier ipv6** command on the ingress PE1 of the BIERv6 tunnel to check BIERv6 stream information. The command output shows that the network slice ID corresponding to the multicast stream (192.168.1.100, 225.0.0.1) is 30, and the network slice ID corresponding to other multicast streams is 20.
    ```
    <PE1> display mvpn all-instance ingress bier ipv6 
    BIER information of VPN-Instance: VPNA 
    Sub-domain ID: 0 
    BSL: 256 
    Source-Dt: 2001:DB8:100::2 
    Total Number of (S,G): 3 
    -------------------------------------------------------------- 
    Source       Group           Flow Label  SliceID 
    -------------------------------------------------------------- 
    192.168.1.103      225.0.0.3       1                   20 
    192.168.1.102      225.0.0.2       2                   20 
    192.168.1.100      225.0.0.1       3                   30 
    --------------------------------------------------------------
    ```

#### Configuration Files

* CE1 configuration file
  ```
  # 
  sysname CE1 
  #
  multicast routing-enable
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   pim sm
  # 
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 192.168.11.2 255.255.255.0
   pim sm
  #
  bgp 65410
   router-id 11.11.11.11
   peer 192.168.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.1 enable
  #
  return
  ```
* CE2 configuration file
  ```
  # 
  sysname CE2 
  #
  multicast routing-enable
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 192.168.4.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  bgp 65411
   router-id 12.12.12.12
   peer 192.168.2.1 as-number 100 
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.2.1 enable
  #
  return
  ```
* CE3 configuration file
  ```
  # 
  sysname CE3 
  #
  multicast routing-enable
  #
  interface GigabitEthernet 0/1/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
  # 
  interface GigabitEthernet 0/1/1
   undo shutdown
   ip address 192.168.5.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  bgp 65412
   router-id 13.13.13.13
   peer 192.168.3.1 as-number 100 
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.3.1 enable
  #
  return
  ```
* PE1 configuration file
  ```
  #                                                                               
  sysname PE1                                                                     
  #                                                                               
  multicast mvpn ipv6-underlay 2001:DB8:10::1                                     
  #
  network-slice instance 10
   description Basic
  #
  network-slice instance 20
   description VPNA
  #
  network-slice instance 30
   description SG
  #
  ip vpn-instance VPNA                                                            
   ipv4-family                                                                    
    route-distinguisher 100:1                                                     
    apply-label per-instance                                                      
    vpn-target 111:1 export-extcommunity                                          
    vpn-target 111:1 import-extcommunity                                          
    multicast routing-enable                                                      
    mvpn                                                                          
     ipv6 underlay enable                                                         
     sender-enable                                                                
     src-dt4 locator PE1 sid 2001:DB8:100::2
     bier ipv6 network-slice 20
     bier ipv6 group 225.0.0.1 source 192.168.1.100 network-slice 30
     rpt-spt mode                                     
     ipmsi-tunnel                                                                 
      bier                                                                        
     spmsi-tunnel                                                                 
      holddown-time 80                                                            
      switch-delay 20                                                             
      group 225.1.1.0 255.255.255.0 source 192.168.11.0 255.255.255.0 threshold 10 bier
  #                                                                               
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:10::1 
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32                            
    opcode ::111 end psp                                                       
  #                                                                               
  isis 1                                                                          
   is-level level-2                                                               
   cost-style wide                                                                
   network-entity 10.0000.0000.0001.00                                            
   bier enable                                                                    
   #                                                                              
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator PE1 auto-sid-disable                              
   #                                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:1::2/96                                                  
   isis ipv6 enable 1
   network-slice 10 data-plane                                              
  #  
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip binding vpn-instance VPNA                                                   
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface LoopBack2
   ip binding vpn-instance VPNA
   ip address 10.1.1.1 255.255.255.255
   pim sm                                                                      
  #
  pim vpn-instance VPNA
   static-rp 10.1.1.1
  #                                                                               
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:10::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.1 
   peer 2001:DB8:20::1 as-number 100                                              
   peer 2001:DB8:20::1 connect-interface LoopBack1                                
   peer 2001:DB8:30::1 as-number 100                                              
   peer 2001:DB8:30::1 connect-interface LoopBack1                                
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
   #                                                                              
   ipv4-family mvpn                                                               
    policy vpn-target                                                             
    peer 2001:DB8:20::1 enable                                                    
    peer 2001:DB8:30::1 enable                                                    
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2001:DB8:20::1 enable                                                    
    peer 2001:DB8:20::1 prefix-sid                                                
    peer 2001:DB8:30::1 enable                                                    
    peer 2001:DB8:30::1 prefix-sid  
   #                                                                              
   ipv4-family vpn-instance VPNA                                                  
    import-route direct                                                           
    segment-routing ipv6 locator PE1                                              
    segment-routing ipv6 best-effort                             
    peer 192.168.1.2 as-number 65410                                              
  #
  bier                                                                            
   sub-domain 0 ipv6
    bfr-id 1                                                              
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator PE1 sid 2001:DB8:100::1                                      
    encapsulation-type ipv6 bsl 256 max-si 0                                      
  #
  bier ipv6 network-slice enable
  #
  return
  ```
* PE2 configuration file
  ```
  #                                                                               
  sysname PE2                                                                     
  #                                                                               
  multicast mvpn ipv6-underlay 2001:DB8:20::1                                     
  #
  network-slice instance 10
   description Basic
  #
  network-slice instance 20
   description VPNA
  #
  network-slice instance 30
   description SG
  #  
  ip vpn-instance VPNA                                                            
   ipv4-family                                                                    
    route-distinguisher 100:1                                                     
    apply-label per-instance                                                      
    vpn-target 111:1 export-extcommunity  
    vpn-target 111:1 import-extcommunity                                          
    multicast routing-enable                                                      
    mvpn                                                                          
     ipv6 underlay enable
     c-multicast signaling bgp
     rpt-spt mode                                                    
  #                                                                               
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:20::1                                    
   locator PE2 ipv6-prefix 2001:DB8:200:: 64 static 32                            
    opcode ::222 end psp                                                       
  #                        
  isis 1                                                                          
   cost-style wide                                                                
   network-entity 10.0000.0000.0002.00                                            
   bier enable                                                                    
   #                                                                              
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator PE2 auto-sid-disable                              
   #                                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                          
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:2::2/96                                                  
   isis ipv6 enable 1
   network-slice 10 data-plane                                                                         
  #
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane   
  #                                                                               
  interface GigabitEthernet0/1/1                                                         
   undo shutdown                                                                  
   ip binding vpn-instance VPNA                                                   
   ip address 192.168.2.1 255.255.255.0  
   pim sm
  #
  pim vpn-instance VPNA
   static-rp 10.1.1.1
  #
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:20::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.2                                                              
   peer 2001:DB8:10::1 as-number 100                                              
   peer 2001:DB8:10::1 connect-interface LoopBack1                                
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
   #                      
   ipv4-family mvpn                                                               
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
    peer 2001:DB8:10::1 prefix-sid                                                
   #                                                                              
   ipv4-family vpn-instance VPNA                                                  
    import-route direct                                                           
    segment-routing ipv6 locator PE2                                              
    segment-routing ipv6 best-effort                             
    peer 192.168.2.2 as-number 65411                                              
  #                                      
  bier                                                                            
   sub-domain 0 ipv6                                                              
    bfr-id 2                                                                      
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator PE2 sid 2001:DB8:200::1                                      
    encapsulation-type ipv6 bsl 256 max-si 0                                      
  #
  return                                  
  ```
* PE3 configuration file
  ```
  #                                                                               
  sysname PE3                                                                     
  #                                                                               
  multicast mvpn ipv6-underlay 2001:DB8:30::1                                     
  #
  network-slice instance 10
   description Basic
  #
  network-slice instance 20
   description VPNA
  #
  network-slice instance 30
   description SG
  #
  ip vpn-instance VPNA                                                            
   ipv4-family                                                                    
    route-distinguisher 100:1                                                     
    apply-label per-instance                                                      
    vpn-target 111:1 export-extcommunity  
    vpn-target 111:1 import-extcommunity                                          
    multicast routing-enable                                                      
    mvpn                                                                          
     ipv6 underlay enable
     c-multicast signaling bgp
     rpt-spt mode                                                    
  #                                                                               
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:30::1                                    
   locator PE3 ipv6-prefix 2001:DB8:300:: 64 static 32                            
    opcode ::333 end psp                                                       
  #                        
  isis 1                                                                          
   cost-style wide                                                                
   network-entity 10.0000.0000.0003.00                                            
   bier enable                                                                    
   #                                                                              
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator PE3 auto-sid-disable                              
   #                                                                              
  #                                                                               
  interface GigabitEthernet0/1/0                                                          
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:3::2/96                                                  
   isis ipv6 enable 1
   network-slice 10 data-plane                                                                         
  #
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #                                                                               
  interface GigabitEthernet0/1/1                                                         
   undo shutdown                                                                  
   ip binding vpn-instance VPNA                                                   
   ip address 192.168.3.1 255.255.255.0  
   pim sm
  #
  pim vpn-instance VPNA
   static-rp 10.1.1.1
  #
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:30::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.3                                                              
   peer 2001:DB8:10::1 as-number 100                                              
   peer 2001:DB8:10::1 connect-interface LoopBack1                                
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
   #                      
   ipv4-family mvpn                                                               
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2001:DB8:10::1 enable                                                    
    peer 2001:DB8:10::1 prefix-sid                                                
   #                                                                              
   ipv4-family vpn-instance VPNA                                                  
    import-route direct                                                           
    segment-routing ipv6 locator PE3                                              
    segment-routing ipv6 best-effort                             
    peer 192.168.3.2 as-number 65412                                              
  #                                      
  bier                                                                            
   sub-domain 0 ipv6                                                              
    bfr-id 3                                                                      
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator PE3 sid 2001:DB8:300::1                                      
    encapsulation-type ipv6 bsl 256 max-si 0                                      
  #                                                                               
  return                                  
  ```
* P configuration file
  ```
  #                                                                               
  sysname P                                                                       
  #                                                                             
  network-slice instance 10
   description Basic
  #
  network-slice instance 20
   description VPNA
  #
  network-slice instance 30
   description SG
  # 
  segment-routing ipv6                                                            
   encapsulation source-address 2001:DB8:40::1                                    
   locator P ipv6-prefix 2001:DB8:400:: 64 static 32                              
    opcode ::444 end psp                                                       
  #                                                                               
  isis 1                                                                          
   is-level level-2                                                               
   cost-style wide                                                                
   network-entity 10.0000.0000.0004.00                                            
   bier enable                                                                    
   #                                                                              
   ipv6 enable topology ipv6                                                      
   segment-routing ipv6 locator P auto-sid-disable                                
   #                                                                              
  #                                                                               
  interface GigabitEthernet0/1/0
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:1::1/96        
   isis ipv6 enable 1
   network-slice 10 data-plane                                                             
  #
  interface GigabitEthernet0/1/0.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/0.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane                         
  #                                                                               
  interface GigabitEthernet0/1/1
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:2::1/96                                                  
   isis ipv6 enable 1
   network-slice 10 data-plane                                                            
  #
  interface GigabitEthernet0/1/1.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/1.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #                                                                               
  interface GigabitEthernet0/1/2 
   undo shutdown                                                                  
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:3::1/96                                                  
   isis ipv6 enable 1
   network-slice 10 data-plane                                                             
  #
  interface GigabitEthernet0/1/2.1 
   vlan-type dot1q 11
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 20 data-plane
  #               
  interface GigabitEthernet0/1/2.2 
   vlan-type dot1q 22
   ipv6 enable    
   ipv6 address auto link-local
   mode channel enable 
   mode channel bandwidth 500
   basic-slice 10 
   network-slice 30 data-plane
  #                                                                               
  interface LoopBack1                                                             
   ipv6 enable                                                                    
   ipv6 address 2001:DB8:40::1/128                                                
   isis ipv6 enable 1                                                             
  #                                                                               
  bier                                                                            
   sub-domain 0 ipv6                                                              
    bfr-prefix interface LoopBack1                                                
    protocol isis                                                                 
    end-bier locator P sid 2001:DB8:400::1                                        
    encapsulation-type ipv6 bsl 256 max-si 0                                    
  #
  bier ipv6 network-slice enable
  #
  return                                                                          
  ```