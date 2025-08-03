Example for Configuring MVPNv6 over BIERv6 on an EVPN L3VPNv6 over SRv6 Network
===============================================================================

This section describes how to configure MVPNv6 over BIERv6 on a unicast EVPN L3VPNv6 over SRv6 network.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0251394663__fig35284409229), EVPN L3VPNv6 over SRv6 has been deployed. It is required that MVPNv6 over BIERv6 be deployed on the existing network.

**Figure 1** MVPNv6 over BIERv6 networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0283462937.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. (Optional) Configure EVPN L3VPNv6 over SRv6 and ensure that the unicast VPN runs properly. If the unicast network has been configured, skip this step.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on PE1, PE2, PE3, and the P.
3. Establish BGP MVPN peer relationships between PEs.
4. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel.
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
6. Enable PIM on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of key interfaces on each device, as shown in [Figure 1](#EN-US_TASK_0251394663__fig35284409229)
* ID (1) of the public network IS-IS process, in a Level-2 area
* VPN instance name (VPNA) on PE1, PE2, and PE3
* PE2's BFR-ID (2), PE3's BFR-ID (3), sub-domain ID (0), BSL (256), and Max-SI (0)

#### Procedure

1. (Optional) Configure EVPN L3VPNv6 over SRv6.
   
   
   
   This step is a part of configuring the unicast network, and its content is for reference only. In most cases, the unicast network has been configured before multicast services are deployed. If this is the case, skip this step and contact the configuration personnel for the configuration data related to the multicast services. For details about how to configure a unicast network, see **Segment Routing IPv6 Configuration** in the Configuration Guide.
   
   # Enable IPv6 forwarding on each interface and configure an IPv6 address for each interface. The configuration of PE1 is used as an example. The configurations of PE2, PE3, and the P are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0251394663__postreq24192593172748) in this section. Similar details will be omitted in the rest of the document.
   
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
   ```
   ```
   [*PE1-isis-1] is-level level-2
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface loopback1
   ```
   ```
   [*PE1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack1] commit
   ```
   ```
   [~PE1-LoopBack1] quit
   ```
   
   # Configure an IPv6 L3VPN instance on each PE and bind the instance to an access-side interface. The configuration of PE1 is used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1. The **vpn-target evpn** and **advertise l2vpn evpn** commands allow EVPN routes to be used in an L3VPN and must be configured on an EVPN L3VPN network. To ensure that multicast runs properly, run both the [**vpn-target**](cmdqueryname=vpn-target) and [**vpn-target evpn**](cmdqueryname=vpn-target+evpn) commands.
   
   ```
   [~PE1] multicast ipv6 mvpn ipv6-underlay 2001:db8:10::1
   ```
   ```
   [*PE1] ip vpn-instance VPNA
   ```
   ```
   [*PE1-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] vpn-target 111:1 both evpn
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] ipv6 address 2001:db8:11::1 96
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface LoopBack2
   ```
   ```
   [~PE1-LoopBack2] ip binding vpn-instance VPNA
   ```
   ```
   [~PE1-LoopBack2] ipv6 enable
   ```
   ```
   [~PE1-LoopBack2] ipv6 address 2001:DB8:55::1 128
   ```
   ```
   [~PE1-LoopBack2] quit
   ```
   ```
   [*PE1] pim-ipv6 vpn-instance VPNA
   ```
   ```
   [*PE1-pim-VPNA] static-rp 2001:DB8:55::1
   ```
   ```
   [*PE1-pim-VPNA] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance VPNA
   ```
   ```
   [*PE1-bgp-6-VPNA] import-route direct
   ```
   ```
   [*PE1-bgp-6-VPNA] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-6-VPNA] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Establish an EBGP peer relationship between each PE and its connected CE. The establishment of an EBGP peer relationship between PE1 and CE1 is used as an example. The establishment of an EBGP peer relationship between PE2 and CE2, and between PE3 and CE3 is similar to that between PE1 and CE1.
   
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 11.11.11.11
   ```
   ```
   [*CE1-bgp] peer 2001:db8:11::1 as-number 100
   ```
   ```
   [*CE1-bgp] ipv6-family unicast
   ```
   ```
   [*CE1-bgp-af-ipv6] peer 2001:DB8:11::1 enable
   ```
   ```
   [*CE1-bgp-af-ipv6] import-route direct
   ```
   ```
   [*CE1-bgp-af-ipv6] quit
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance VPNA
   ```
   ```
   [*PE1-bgp-6-VPNA] peer 2001:db8:11::2 as-number 65410
   ```
   ```
   [*PE1-bgp-6-VPNA] commit
   ```
   ```
   [~PE1-bgp-6-VPNA] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Establish a BGP EVPN peer relationship between PE1 and PE2 and between PE1 and PE3. The configuration of PE1 is used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1. After you run the [**peer enable**](cmdqueryname=peer+enable) command, enter **Y** at the system prompt to confirm the action.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:db8:20::1 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:db8:30::1 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:db8:20::1 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] peer 2001:db8:30::1 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:db8:20::1 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:db8:30::1 enable
   ```
   ```
   [*PE1-bgp-af-evpn] commit
   ```
   ```
   [~PE1-bgp-af-evpn] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure SRv6 SIDs, and configure PEs to add SIDs to the VPN routes to be advertised. The configurations of PE1 and P are used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:db8:10::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:db8:100:: 64 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::10 end psp
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:db8:20::1 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:db8:30::1 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance VPNA
   ```
   ```
   [*PE1-bgp-6-VPNA] segment-routing ipv6 best-effort evpn
   ```
   ```
   [*PE1-bgp-6-VPNA] segment-routing ipv6 locator PE1 evpn
   ```
   ```
   [*PE1-bgp-6-VPNA] commit
   ```
   ```
   [~PE1-bgp-6-VPNA] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   ```
   [~PE1] isis 1
   ```
   ```
   [~PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable 
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:db8:40::1
   ```
   ```
   [*P-segment-routing-ipv6] locator P ipv6-prefix 2001:db8:400:: 64 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] opcode ::40 end psp
   ```
   ```
   [*P-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P-segment-routing-ipv6] quit
   ```
   ```
   [*P] isis 1
   ```
   ```
   [*P-isis-1] segment-routing ipv6 locator P auto-sid-disable
   ```
   ```
   [*P-isis-1] commit
   ```
   ```
   [~P-isis-1] quit
   ```
   
   # Perform other unicast network configurations based on unicast service requirements.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In an MVPNv6 over BIERv6 scenario, if routes sent by a multicast source CE to a root PE carry Source AS Extended Community and VRF Route Import Extended Community attributes and the root PE needs to advertise only locally configured Source AS Extended Community and VRF Route Import Extended Community attributes among extended community attributes in the routes to be sent to a leaf PE, run the [**attr-set**](cmdqueryname=attr-set) command in the BGP-VPN instance IPv6 address family view on the root PE.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on PE1, PE2, PE3, and the P.
   
   # Configure PE1.
   ```
   [~PE1] bier
   ```
   ```
   [*PE1-bier] sub-domain 0 ipv6
   ```
   ```
   [*PE1-bier-sub-domain-0-ipv6] bfr-id 1
   ```
   ```
   [*PE1-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*PE1-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*PE1-bier-sub-domain-0-ipv6] end-bier locator PE1 sid 2001:db8:100::1
   ```
   ```
   [*PE1-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*PE1-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*PE1-bier] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] bier enable
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   ```
   [~PE2] bier
   ```
   ```
   [*PE2-bier] sub-domain 0 ipv6
   ```
   ```
   [*PE2-bier-sub-domain-0-ipv6] bfr-id 2
   ```
   ```
   [*PE2-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*PE2-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*PE2-bier-sub-domain-0-ipv6] end-bier locator PE2 sid 2001:db8:200::1
   ```
   ```
   [*PE2-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*PE2-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*PE2-bier] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] bier enable
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   ```
   [~PE3] bier
   ```
   ```
   [*PE3-bier] sub-domain 0 ipv6
   ```
   ```
   [*PE3-bier-sub-domain-0-ipv6] bfr-id 3
   ```
   ```
   [*PE3-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*PE3-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*PE3-bier-sub-domain-0-ipv6] end-bier locator PE3 sid 2001:db8:300::1
   ```
   ```
   [*PE3-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*PE3-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*PE3-bier] quit
   ```
   ```
   [*PE3] isis 1
   ```
   ```
   [*PE3-isis-1] bier enable
   ```
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure the P.
   ```
   [~P] bier
   ```
   ```
   [*P-bier] sub-domain 0 ipv6
   ```
   ```
   [*P-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*P-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*P-bier-sub-domain-0-ipv6] end-bier locator P sid 2001:db8:400::1
   ```
   ```
   [*P-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*P-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*P-bier] quit
   ```
   ```
   [*P] isis 1
   ```
   ```
   [*P-isis-1] bier enable
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] commit
   ```
3. Establish BGP MVPN peer relationships between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv6-family mvpn
   ```
   ```
   [*PE1-bgp-af-mvpnv6] peer 2001:db8:20::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpnv6] peer 2001:db8:30::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpnv6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] ipv6-family mvpn
   ```
   ```
   [*PE2-bgp-af-mvpnv6] peer 2001:db8:10::1 enable
   ```
   ```
   [*PE2-bgp-af-mvpnv6] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [~PE3-bgp] ipv6-family mvpn
   ```
   ```
   [*PE3-bgp-af-mvpnv6] peer 2001:db8:10::1 enable
   ```
   ```
   [*PE3-bgp-af-mvpnv6] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Display information about BGP-IPv6 MVPN peers.
   
   ```
   [~PE1]display bgp mvpn vpnv6 all peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:20::1                   4         100       20       22     0 00:13:41       Established        0
     2001:DB8:30::1                   4         100       20       20     0 00:15:34       Established        0
   ```
4. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance VPNA
   ```
   ```
   [*PE1-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] ipv6 underlay enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] sender-enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] src-dt6 locator PE1 sid 2001:db8:100::2
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] ipmsi-tunnel
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] bier sub-domain 0 bsl 256
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance VPNA
   ```
   ```
   [*PE2-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] ipv6 underlay enable
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE2-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE2-vpn-instance-VPNA] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] ipv6 underlay enable
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] rpt-spt mode
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Display I-PMSI tunnel information of MVPN services in a specified VPN instance. The command output shows that an I-PMSI tunnel has been established, with PE1 as the root node and PE2 and PE3 as leaf nodes.
   
   ```
   [~PE1] display mvpn ipv6 vpn-instance VPNA ipmsi
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: BIER IPv6
   Tunnel state: Up
   Src-dt6 SID: 2001:DB8:100::2 
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
   ```
   ```
   [*PE1-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] spmsi-tunnel
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-spmsi] group FF13::100 96 source 2001:db8:111:: 64 threshold 10 bier 
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-spmsi] switch-delay 20
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-spmsi] holddown-time 80
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-spmsi] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] commit
   ```
6. Enable PIM on PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE3-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Display S-PMSI tunnel information of MVPN services in a specified VPN instance. The command output on PE2 shows the S-PMSI tunnel and multicast user information.
   
   ```
   [~PE2]display mvpn ipv6 vpn-instance VPNA spmsi verbose
   MVPN local S-PMSI information for VPN-Instance : VPNA 
    Total number of tunnel: 1 
    S-PMSI A-D Route Type: -- 
    Tunnel type: BIER IPv6 
    Tunnel state: -- 
    Src-dt6 SID: 2001:DB8:100::1 
    Sub-domain ID: 0 
    BFR-ID: 1 
    BFR prefix: 2001:DB8:10::1 
    Root: 2001:DB8:10::1 
    Leaf: 
      1: 2001:DB8:20::1 (BFR-ID: 2, BFR prefix: 2001:DB8:20::1)(local)
    Total number of (S, G): 1 
        1. (2001:DB8:111::100, FF13::100)
   ```

#### Configuration Files

CE1 configuration file

```
# 
sysname CE1 
#
multicast ipv6 routing-enable
# 
interface GigabitEthernet 0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:11::2/96
 pim ipv6 sm
#
interface GigabitEthernet 0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:111::2/96
 pim ipv6 sm
#
bgp 65410
 router-id 11.11.11.11
 peer 2001:db8:11::1 as-number 100 
 #
 ipv6-family unicast
  undo synchronization
  peer 2001:DB8:11::1 enable
  import-route direct
#
return
```

CE2 configuration file

```
# 
sysname CE2 
#
multicast ipv6 routing-enable
# 
interface GigabitEthernt 0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:12::2/96
 pim ipv6 sm
#
interface GigabitEthernt 0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:14::2/96
 pim ipv6 sm
 mld enable
 mld version 1
#
bgp 65411
 router-id 22.22.22.22
 peer 2001:DB8:12::1 as-number 100 
 #
 ipv6-family unicast
  undo synchronization
  peer 2001:DB8:12::1 enable
#
return
```

CE3 configuration file

```
# 
sysname CE3 
#
multicast ipv6 routing-enable
# 
interface GigabitEthernet 0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:13:2/96
 pim ipv6 sm 
#
interface GigabitEthernet 0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:15:2/96
 pim ipv6 sm
 mld enable
 mld version 1
#
bgp 65412
 router-id 33.33.33.33
 peer 2001:DB8:13::1 as-number 100
 #
 ipv6-family unicast
  undo synchronization
  peer 2001:DB8:13::1 enable
#
return
```

PE1 configuration file

```
#                                                                               
sysname PE1                                                                     
#                                                                               
multicast ipv6 mvpn ipv6-underlay 2001:DB8:10::1                                
# 
ip vpn-instance VPNA                                                            
 ipv6-family                                                                    
  route-distinguisher 100:1                                                     
  apply-label per-instance                                                         
  vpn-target 111:1 export-extcommunity evpn 
  vpn-target 111:1 import-extcommunity evpn
  multicast ipv6 routing-enable                                                 
  mvpn                                                                          
   vpn-target 111:1 export-extcommunity
   vpn-target 111:1 import-extcommunity
   ipv6 underlay enable
   c-multicast signaling bgp
   sender-enable                                                                
   src-dt6 locator 
   rpt-spt mode                                      
   ipmsi-tunnel                                                                 
    bier                                                                        
   spmsi-tunnel                                                                 
    holddown-time 80                                                            
    switch-delay 20                                                             
    group FF13:: 96 source 2001:DB8:111:: 64 threshold 10 bier                   
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:10::1                                    
 locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32                            
  opcode ::10 end psp                                                        
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
#                                                                               
interface GigabitEthernet0/1/1                 
 undo shutdown                                                                  
 ip binding vpn-instance VPNA                                                   
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:11::1/96                                                 
 pim ipv6 sm                                                                   
#
interface LoopBack2
 ip binding vpn-instance VPNA
 ipv6 enable
 ipv6 address 2001:DB8:55::1/128                                                             
#
pim-ipv6 vpn-instance VPNA
 static-rp 2001:DB8:55::1
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
 ipv6-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:20::1 enable                                                    
  peer 2001:DB8:30::1 enable                                                    
 #                                                                              
 ipv6-family vpn-instance VPNA                                                  
  import-route direct                                                           
  advertise l2vpn evpn                                                          
  segment-routing ipv6 locator PE1 evpn                                         
  segment-routing ipv6 best-effort evpn                        
  peer 2001:DB8:11::2 as-number 65410                                           
 # 
  l2vpn-family evpn                                                              
  policy vpn-target                                                             
  peer 2001:DB8:20::1 enable                                                    
  peer 2001:DB8:20::1 advertise encap-type srv6                                 
  peer 2001:DB8:30::1 enable                                                    
  peer 2001:DB8:30::1 advertise encap-type srv6                                 
# 
bier                                                                            
 sub-domain 0 ipv6
  bfr-id 1                                                              
  bfr-prefix interface LoopBack1                                                
  protocol isis                                                                 
  end-bier locator PE1 sid 2001:DB8:100::1                                      
  encapsulation-type ipv6 bsl 256 max-si 0                                      
#
return
```

PE2 configuration file

```
#                                                                               
sysname PE2                                                                     
# 
multicast ipv6 mvpn ipv6-underlay 2001:DB8:20::1                                
# 
ip vpn-instance VPNA                                                            
 ipv6-family                                                                    
  route-distinguisher 100:1                                                     
  apply-label per-instance
  vpn-target 111:1 export-extcommunity evpn
  vpn-target 111:1 import-extcommunity evpn                                     
  multicast ipv6 routing-enable                                                 
  mvpn
   vpn-target 111:1 export-extcommunity
   vpn-target 111:1 import-extcommunity
   ipv6 underlay enable
   c-multicast signaling bgp
   rpt-spt mode
#                                                                               
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:20::1                                    
 locator PE2 ipv6-prefix 2001:DB8:200:: 64 static 32                            
  opcode ::20 end psp                                                        
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
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
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ip binding vpn-instance VPNA                                                   
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:12::1/96                                                 
 pim ipv6 sm                                                                    
#
pim-ipv6 vpn-instance VPNA
 static-rp 2001:DB8:55::1
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
 ipv6-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:10::1 enable                                                    
 #                                                                              
 ipv6-family vpn-instance VPNA                                                  
  import-route direct                                                           
  advertise l2vpn evpn                                                          
  segment-routing ipv6 locator PE2 evpn                                         
  segment-routing ipv6 best-effort evpn                        
  peer 2001:DB8:12::2 as-number 65411                                           
 #                                                                              
 l2vpn-family evpn
  policy vpn-target                                                             
  peer 2001:DB8:10::1 enable                                                    
  peer 2001:DB8:10::1 advertise encap-type srv6                                 
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

PE3 configuration file

```
#                                                                               
sysname PE3                                                                     
# 
multicast ipv6 mvpn ipv6-underlay 2001:DB8:30::1                                
# 
ip vpn-instance VPNA                                                            
 ipv6-family                                                                    
  route-distinguisher 100:1                                                     
  apply-label per-instance
  vpn-target 111:1 export-extcommunity evpn
  vpn-target 111:1 import-extcommunity evpn                                     
  multicast ipv6 routing-enable                                                 
  mvpn                                                                          
   vpn-target 111:1 export-extcommunity
   vpn-target 111:1 import-extcommunity 
   ipv6 underlay enable
   c-multicast signaling bgp
   rpt-spt mode
#                                                                          
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:30::1                                    
 locator PE3 ipv6-prefix 2001:DB8:300:: 64 static 32                            
  opcode ::30 end psp                                                        
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
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
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ip binding vpn-instance VPNA                                                   
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:13::1/96                                                 
 pim ipv6 sm                                                                    
#
pim-ipv6 vpn-instance VPNA
 static-rp 2001:DB8:55::1
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
 ipv6-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:10::1 enable                                                    
 #                                                                              
 ipv6-family vpn-instance VPNA                                                  
  import-route direct                                                           
  advertise l2vpn evpn                                                          
  segment-routing ipv6 locator PE3 evpn                                         
  segment-routing ipv6 best-effort evpn                        
  peer 2001:DB8:13::2 as-number 65412                                           
 #                                                                              
 l2vpn-family evpn
  policy vpn-target                                                             
  peer 2001:DB8:10::1 enable                                                    
  peer 2001:DB8:10::1 advertise encap-type srv6                                 
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

P configuration file

```
#                                                                               
sysname P                                                                       
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:40::1                                    
 locator P ipv6-prefix 2001:DB8:400:: 64 static 32                              
  opcode ::40 end psp                                                       
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
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:2::1/96                                                  
 isis ipv6 enable 1                                                             
#                                                                               
interface GigabitEthernet0/1/2                                                         
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:3::1/96                                                  
 isis ipv6 enable 1                                                             
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
return
```