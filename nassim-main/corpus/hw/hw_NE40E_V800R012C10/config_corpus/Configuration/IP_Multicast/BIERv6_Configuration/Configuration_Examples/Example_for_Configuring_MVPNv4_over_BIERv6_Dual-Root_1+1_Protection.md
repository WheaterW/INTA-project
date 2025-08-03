Example for Configuring MVPNv4 over BIERv6 Dual-Root 1+1 Protection
===================================================================

This section describes how to configure MVPNv4 over BIERv6 dual-root 1+1 protection. In this example, the unicast network type is L3VPNv4 over SRv6. Configuring multicast services on other types of unicast networks is similar to this procedure.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0251394662__fig35284409229), L3VPNv4 over SRv6 has been deployed. CE1 is dual-homed to the public network in active-active mode. It is required that MVPNv4 over BIERv6 services and dual-root 1+1 protection be deployed on the existing network.

**Figure 1** MVPNv4 over BIERv6 dual-root 1+1 protection networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0283833930.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. (Optional) Configure L3VPNv4 over SRv6 and ensure that the unicast VPN runs properly. If the unicast network has been configured, skip this step.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on Root1, Root2, P1, P2, and PE1.
3. Establish a BGP MVPN peer relationship between Root1 and PE1 and between Root2 and PE1.
4. Configure multicast traffic forwarding over two BIERv6 I-PMSI tunnels.
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
6. Enable PIM on Root1, Root2, and PE1.
7. Configure dual-root 1+1 protection.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of main interfaces on each device, as shown in [Figure 1](#EN-US_TASK_0251394662__fig35284409229)
* ID (1) of the public network IS-IS process, in a Level-2 area
* VPN instance name (VPNA) on Root1, Root2, and PE1
* PE1's BFR-ID (1), sub-domain ID (0), BSL (256), and Max-SI (0)

#### Procedure

1. (Optional) Configure L3VPNv4 over SRv6.
   
   
   
   This step is a part of configuring the unicast network, and its content is for reference only. In most cases, the unicast network has been configured before multicast services are deployed. If this is the case, skip this step and contact the configuration personnel for the configuration data related to the multicast services. For details about how to configure a unicast network, see **Segment Routing IPv6 Configuration** in the Configuration Guide.
   
   # Enable IPv6 forwarding on each interface and configure an IPv6 address for each interface. The configuration of Root1 is used as an example. The configurations of Root2, P1, P2, and PE1 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0251394662__postreq24192593172748) in this section. Similar details will be omitted in the rest of the document.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Root1
   [*HUAWEI] commit
   [~Root1] interface gigabitethernet 0/1/0
   [~Root1-GigabitEthernet0/1/0] ipv6 enable
   [*Root1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 96
   [*Root1-GigabitEthernet0/1/0] quit
   [*Root1] interface LoopBack 1
   [*Root1-LoopBack1] ipv6 enable
   [*Root1-LoopBack1] ipv6 address 2001:db8:111::1 128
   [*Root1-LoopBack1] quit
   [*Root1] commit
   ```
   
   # Configure IS-IS. The configuration of Root1 is used as an example. The configurations of Root2, P1, P2, and PE1 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0251394662__postreq24192593172748) in this section.
   
   ```
   [~Root1] isis 1
   ```
   ```
   [*Root1-isis-1] is-level level-2
   ```
   ```
   [*Root1-isis-1] cost-style wide
   ```
   ```
   [*Root1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*Root1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*Root1-isis-1] quit
   ```
   ```
   [*Root1] interface gigabitethernet 0/1/0
   ```
   ```
   [*Root1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*Root1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Root1] interface loopback1
   ```
   ```
   [*Root1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*Root1-LoopBack1] commit
   ```
   ```
   [~Root1-LoopBack1] quit
   ```
   
   # Configure a VPN instance on PEs, enable the IPv4 address family for the instance, and bind the interfaces that connect the PEs to a CE to the VPN instance. The configuration of Root1 is used as an example. The configurations of Root2 and PE1 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0251394662__postreq24192593172748) in this section.
   
   ```
   [~Root1] ip vpn-instance VPNA
   ```
   ```
   [*Root1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA] quit
   ```
   ```
   [*Root1] interface gigabitethernet 0/1/1
   ```
   ```
   [*Root1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
   ```
   ```
   [*Root1-GigabitEthernet0/1/1] ip address 192.168.1.2 24
   ```
   ```
   [*Root1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Establish EBGP peer relationships between the roots and CEs and between PEs and the CEs. The peer relationship establishment between Root1 and CE1 is used as an example. The peer relationship establishment between Root2 and CE1, and between PE1 and CE2 is similar to that between Root1 and CE1.
   
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 11.11.11.11
   ```
   ```
   [*CE1-bgp] peer 192.168.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   ```
   [~Root1] bgp 100
   ```
   ```
   [*Root1-bgp] router-id 1.1.1.1
   ```
   ```
   [*Root1-bgp] ipv4-family vpn-instance VPNA
   ```
   ```
   [*Root1-bgp-VPNA] peer 192.168.1.1 as-number 65410
   ```
   ```
   [*Root1-bgp-VPNA] import-route direct
   ```
   ```
   [*Root1-bgp-VPNA] commit
   ```
   ```
   [~Root1-bgp-VPNA] quit
   ```
   ```
   [~Root1-bgp] quit
   ```
   
   # Establish an MP-IBGP peer relationship between Root1 and PE1 and between Root2 and PE1. The configuration of Root1 is used as an example. The configurations of Root2 and PE1 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0251394662__postreq24192593172748) in this section. After you run the [**peer enable**](cmdqueryname=peer+enable) command, enter **Y** at the system prompt to confirm the action.
   
   ```
   [~Root1] bgp 100
   ```
   ```
   [~Root1-bgp] peer 2001:db8:115::1 as-number 100
   ```
   ```
   [*Root1-bgp] peer 2001:db8:115::1 connect-interface loopback 1
   ```
   ```
   [*Root1-bgp] ipv4-family vpnv4
   ```
   ```
   [*Root1-bgp-af-vpnv4] peer 2001:db8:115::1 enable
   ```
   ```
   [*Root1-bgp-af-vpnv4] commit
   ```
   ```
   [~Root1-bgp-af-vpnv4] quit
   ```
   ```
   [~Root1-bgp] quit
   ```
   
   # Configure SRv6 SIDs, and configure PEs to add SIDs to the VPN routes to be advertised. The configurations of Root1 and P1 are used as an example. The configurations of Root2, P2, and PE1 are similar to the configuration of Root1. For configuration details, see [Configuration Files](#EN-US_TASK_0251394662__postreq24192593172748) in this section. The [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) command does not need to be run on PE1.
   
   ```
   [~Root1] segment-routing ipv6
   ```
   ```
   [*Root1-segment-routing-ipv6] encapsulation source-address 2001:db8:111::1
   ```
   ```
   [*Root1-segment-routing-ipv6] locator Root1 ipv6-prefix 2001:db8:11:: 64 static 32
   ```
   ```
   [*Root1-segment-routing-ipv6-locator] opcode ::111 end psp
   ```
   ```
   [*Root1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*Root1-segment-routing-ipv6] quit
   ```
   ```
   [*Root1] bgp 100
   ```
   ```
   [*Root1-bgp] ipv4-family vpnv4
   ```
   ```
   [*Root1-bgp-af-vpnv4] peer 2001:db8:115::1 prefix-sid
   ```
   ```
   [*Root1-bgp-af-vpnv4] quit
   ```
   ```
   [*Root1-bgp] ipv4-family vpn-instance VPNA
   ```
   ```
   [*Root1-bgp-VPNA] segment-routing ipv6 best-effort
   ```
   ```
   [*Root1-bgp-VPNA] segment-routing ipv6 locator Root1
   ```
   ```
   [*Root1-bgp-VPNA] commit
   ```
   ```
   [~Root1-bgp-VPNA] quit
   ```
   ```
   [~Root1-bgp] quit
   ```
   ```
   [~Root1] isis 1
   ```
   ```
   [~Root1-isis-1] segment-routing ipv6 locator Root1 auto-sid-disable 
   ```
   ```
   [*Root1-isis-1] commit
   ```
   ```
   [~Root1-isis-1] quit
   ```
   ```
   [~P1] segment-routing ipv6
   ```
   ```
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:db8:113::1
   ```
   ```
   [*P1-segment-routing-ipv6] locator P1 ipv6-prefix 2001:db8:13:: 64 static 32
   ```
   ```
   [*P1-segment-routing-ipv6-locator] opcode ::333 end psp
   ```
   ```
   [*P1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P1-segment-routing-ipv6] quit
   ```
   ```
   [*P1] isis 1
   ```
   ```
   [*P1-isis-1] segment-routing ipv6 locator P1 auto-sid-disable
   ```
   ```
   [*P1-isis-1] commit
   ```
   ```
   [~P1-isis-1] quit
   ```
   
   # Perform other unicast network configurations based on unicast service requirements.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In an MVPNv4 over BIERv6 scenario, if routes sent by a multicast source CE to a root node carry Source AS Extended Community and VRF Route Import Extended Community attributes and the root node needs to advertise only locally configured Source AS Extended Community and VRF Route Import Extended Community attributes among extended community attributes in the routes to be sent to a leaf node, run the [**attr-set**](cmdqueryname=attr-set) command in the BGP-VPN instance IPv4 address family view on the root node.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on Root1, Root2, P1, P2, and PE1.
   
   # Configure Root1.
   ```
   [~Root1] bier
   ```
   ```
   [*Root1-bier] sub-domain 0 ipv6
   ```
   ```
   [*Root1-bier-sub-domain-0-ipv6] bfr-id 2
   ```
   ```
   [*Root1-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*Root1-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*Root1-bier-sub-domain-0-ipv6] end-bier locator Root1 sid 2001:db8:11::1
   ```
   ```
   [*Root1-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*Root1-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*Root1-bier] quit
   ```
   ```
   [*Root1] isis 1
   ```
   ```
   [*Root1-isis-1] bier enable
   ```
   ```
   [*Root1-isis-1] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   ```
   [~Root2] bier
   ```
   ```
   [*Root2-bier] sub-domain 0 ipv6
   ```
   ```
   [*Root2-bier-sub-domain-0-ipv6] bfr-id 3
   ```
   ```
   [*Root2-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*Root2-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*Root2-bier-sub-domain-0-ipv6] end-bier locator Root2 sid 2001:db8:12::1
   ```
   ```
   [*Root2-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*Root2-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*Root2-bier] quit
   ```
   ```
   [*Root2] isis 1
   ```
   ```
   [*Root2-isis-1] bier enable
   ```
   ```
   [*Root2-isis-1] quit
   ```
   ```
   [*Root2] commit
   ```
   
   # Configure P1.
   ```
   [~P1] bier
   ```
   ```
   [*P1-bier] sub-domain 0 ipv6
   ```
   ```
   [*P1-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*P1-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*P1-bier-sub-domain-0-ipv6] end-bier locator P1 sid 2001:db8:13::1
   ```
   ```
   [*P1-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*P1-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*P1-bier] quit
   ```
   ```
   [*P1] isis 1
   ```
   ```
   [*P1-isis-1] bier enable
   ```
   ```
   [*P1-isis-1] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure P2.
   ```
   [~P2] bier
   ```
   ```
   [*P2-bier] sub-domain 0 ipv6
   ```
   ```
   [*P2-bier-sub-domain-0-ipv6] encapsulation-type ipv6 bsl 256 max-si 0
   ```
   ```
   [*P2-bier-sub-domain-0-ipv6] bfr-prefix interface loopback1
   ```
   ```
   [*P2-bier-sub-domain-0-ipv6] end-bier locator P2 sid 2001:db8:14::1
   ```
   ```
   [*P2-bier-sub-domain-0-ipv6] protocol isis
   ```
   ```
   [*P2-bier-sub-domain-0-ipv6] quit
   ```
   ```
   [*P2-bier] quit
   ```
   ```
   [*P2] isis 1
   ```
   ```
   [*P2-isis-1] bier enable
   ```
   ```
   [*P2-isis-1] quit
   ```
   ```
   [*P2] commit
   ```
   
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
   [*PE1-bier-sub-domain-0-ipv6] end-bier locator PE1 sid 2001:db8:15::1
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
3. Establish a BGP MVPN peer relationship between Root1 and PE1 and between Root2 and PE1.
   
   
   
   # Configure Root1.
   
   ```
   [~Root1] bgp 100
   ```
   ```
   [~Root1-bgp] ipv4-family mvpn
   ```
   ```
   [*Root1-bgp-af-mvpn] peer 2001:db8:115::1 enable
   ```
   ```
   [*Root1-bgp-af-mvpn] quit
   ```
   ```
   [*Root1-bgp] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   
   ```
   [~Root2] bgp 100
   ```
   ```
   [~Root2-bgp] ipv4-family mvpn
   ```
   ```
   [*Root2-bgp-af-mvpn] peer 2001:db8:115::1 enable
   ```
   ```
   [*Root2-bgp-af-mvpn] quit
   ```
   ```
   [*Root2-bgp] quit
   ```
   ```
   [*Root2] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family mvpn
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 2001:db8:111::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 2001:db8:112::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Display information about BGP MVPN peers. The command output shows that a BGP MVPN peer relationship has been established between PE1 and Root1 and between PE1 and Root2.
   
   ```
   [~PE1]display bgp mvpn all peer
   
    BGP local router ID : 1.1.1.5
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:111::1                  4         100   41      43    0 00:08:08        Established      0
     2001:DB8:112::1                  4         100   29      32    0 00:07:15        Established      0
   ```
4. Configure multicast traffic forwarding over two BIERv6 I-PMSI tunnels.
   
   
   
   # Configure Root1.
   
   ```
   [~Root1] multicast mvpn ipv6-underlay 2001:db8:111::1
   ```
   ```
   [*Root1] ip vpn-instance VPNA
   ```
   ```
   [*Root1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] ipv6 underlay enable
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] src-dt4 locator Root1 sid 2001:db8:11::2
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] bier sub-domain 0 bsl 256
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   
   ```
   [~Root2] multicast mvpn ipv6-underlay 2001:db8:112::1
   ```
   ```
   [*Root2] ip vpn-instance VPNA
   ```
   ```
   [*Root2-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] ipv6 underlay enable
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] src-dt4 locator Root2 sid 2001:db8:12::2
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] bier sub-domain 0 bsl 256
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*Root2-vpn-instance-VPNA] quit
   ```
   ```
   [*Root2] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] multicast mvpn ipv6-underlay 2001:db8:115::1
   ```
   ```
   [*PE1] ip vpn-instance VPNA
   ```
   ```
   [*PE1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] ipv6 underlay enable
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Display I-PMSI tunnel information of MVPN services in a specified VPN instance. The command output shows that two I-PMSI tunnels have been established, with Root1 and Root2 as the root nodes and PE1 as a leaf node.
   
   ```
   [~PE1]display mvpn vpn-instance VPNA ipmsi
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: BIER IPv6
   Tunnel state: --
   Src-dt4 SID: 2001:DB8:11::2
   Sub-domain ID: 0
   BFR-ID: --
   BFR prefix: 2001:DB8:111::1
   Root: 2001:DB8:111::1
   Leaf: 
     1: 2001:DB8:115::1 (BFR-ID: 1, BFR prefix: 2001:DB8:115::1) (local)
   
   Tunnel type: BIER IPv6
   Tunnel state: --
   Src-dt4 SID: 2001:DB8:12::2
   Sub-domain ID: 0
   BFR-ID: --
   BFR prefix: 2001:DB8:112::1
   Root: 2001:DB8:112::1
   Leaf: 
     1: 2001:DB8:115::1 (BFR-ID: 1, BFR prefix: 2001:DB8:115::1) (local)
   ```
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
   
   
   
   # Configure Root1.
   
   ```
   [~Root1] ip vpn-instance VPNA
   ```
   ```
   [*Root1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] group 232.1.1.0 24 source 192.168.10.0 24 threshold 10 bier
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] switch-delay 20
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] holddown-time 80
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*Root1-vpn-instance-VPNA] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   
   ```
   [~Root2] ip vpn-instance VPNA
   ```
   ```
   [*Root2-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] group 232.1.1.0 24 source 192.168.10.0 24 threshold 10 bier 
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] switch-delay 20
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] holddown-time 80
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] quit
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*Root2-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*Root2-vpn-instance-VPNA] quit
   ```
   ```
   [*Root2] commit
   ```
6. Enable PIM on Root1, Root2, and PE1.
   
   
   
   # Configure Root1.
   
   ```
   [~Root1] interface gigabitethernet 0/1/1
   ```
   ```
   [~Root1-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*Root1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   
   ```
   [~Root2] interface gigabitethernet 0/1/1
   ```
   ```
   [~Root2-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*Root2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Root2] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
7. Configure dual-root 1+1 protection.
   
   
   
   # Configure VPN FRR on PE1.
   
   ```
   [~PE1] ip vpn-instance VPNA
   ```
   ```
   [~PE1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [~PE1-vpn-instance-VPNA-af-ipv4] vpn frr
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure C-multicast FRR in flow-based detection mode on PE1.
   
   ```
   [~PE1] acl 2111
   ```
   ```
   [*PE1-acl4-basic-2111] rule permit source any
   ```
   ```
   [*PE1-acl4-basic-2111] quit
   ```
   ```
   [*PE1] ip vpn-instance VPNA
   ```
   ```
   [*PE1-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] MVPN
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast frr
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast frr flow-detection-based 2111
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] multicast wtr 100
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-VPNA] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Display S-PMSI tunnel information of MVPN services in a specified VPN instance. The command output on PE1 shows the S-PMSI tunnel and (S, G) information.
   
   ```
   [~PE1]display mvpn vpn-instance VPNA spmsi verbose
   MVPN local S-PMSI information for VPN-Instance : VPNA 
    Total number of tunnel: 2 
    S-PMSI A-D Route Type: -- 
    Tunnel type: BIER IPv6 
    Tunnel state: -- 
    Src-dt4 SID: 2001:DB8:11::2 
    Sub-domain ID: 0 
    BFR-ID: -- 
    BFR prefix: 2001:DB8:111::1 
    Root: 2001:DB8:111::1 
    Leaf: 
      1: 2001:DB8:115::1 (BFR-ID: 2, BFR prefix: 2001:DB8:115::1)(local)
    Total number of (S, G): 2 
        1. (192.168.10.100, 232.1.1.1) 
        2. (192.168.10.100, 232.1.1.2)
   
    Total number of tunnel: 2 
    S-PMSI A-D Route Type: -- 
    Tunnel type: BIER IPv6 
    Tunnel state: -- 
    Src-dt4 SID: 2001:DB8:12::2 
    Sub-domain ID: 0 
    BFR-ID: -- 
    BFR prefix: 2001:DB8:112::1 
    Root: 2001:DB8:112::1 
    Leaf: 
      1: 2001:DB8:115::1 (BFR-ID: 2, BFR prefix: 2001:DB8:115::1)(local)
    Total number of (S, G): 2 
        1. (192.168.10.100, 232.1.1.1) 
        2. (192.168.10.100, 232.1.1.2)
   ```
8. Verify the configuration.
   
   
   
   # Run the **display pim vpn-instance routing-table** command to check the PIM routing table. The command output shows that a backup upstream interface exists.
   
   ```
   <PE1> display pim all-instance routing-table mode sm outgoing-interface-number  
   VPN-Instance: VPNA  
   Total 0 (*, G) entries; 2 (S, G) entry   
   (192.168.10.100, 232.1.1.1)          
      Protocol: pim-sm, Flag: SG_RCVR      
      UpTime: 00:00:04      
      Upstream interface: through-BGP, Refresh time: 00:00:04          
          Upstream neighbor: 2001:DB8:111::1           
          RPF prime neighbor: 2001:DB8:111::1
      Backup upstream interface: through-BGP          
          Upstream neighbor: 2001:DB8:112::1           
          RPF prime neighbor: 2001:DB8:112::1
      Downstream interface(s) information:      
      Total number of downstreams: 1
   
   (192.168.10.100, 232.1.1.2)           
      Protocol: pim-sm, Flag: SG_RCVR      
      UpTime: 00:00:05      
      Upstream interface: Register, Refresh time: 00:00:05          
          Upstream neighbor: NULL          
          RPF prime neighbor: NULL      
      Backup upstream interface: through-BGP          
          Upstream neighbor: 2001:DB8:112::1           
          RPF prime neighbor: 2001:DB8:112::1
      Downstream interface(s) information:      
      Total number of downstreams: 1
   ```

#### Configuration Files

CE1 configuration file

```
#   
sysname CE1 
# 
multicast routing-enable
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 192.168.1.1 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 192.168.2.1 255.255.255.0
 pim sm
#
bgp 65410
 router-id 11.11.11.11
 peer 192.168.1.2 as-number 100
 peer 192.168.2.2 as-number 100
 #
 ipv4-family unicast
  undo synchronization
  peer 192.168.1.2 enable
  peer 192.168.2.2 enable
#
return
```

CE2 configuration file

```
# 
sysname CE2
#
multicast routing-enable
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 10.11.3.1 255.255.255.0
 pim sm
 igmp enable
 igmp version 3
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 192.168.3.1 255.255.255.0
 pim sm
#
bgp 65411
 router-id 12.12.12.12
 peer 192.168.3.2 as-number 100
 #
 ipv4-family unicast
  undo synchronization
  peer 192.168.3.2 enable
#
return
```

Root1 configuration file

```
#                                                                               
sysname Root1                                                                   
# 
multicast mvpn ipv6-underlay 2001:DB8:111::1                                    
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
   src-dt4 locator Root1 sid 2001:DB8:11::2                                     
   ipmsi-tunnel                                                                 
    bier                                                                        
   spmsi-tunnel                                                                 
    holddown-time 80                                                            
    switch-delay 20                                                             
    group 232.1.1.0 255.255.255.0 source 192.168.10.0 255.255.255.0 threshold 10 bier 
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:111::1                                   
 locator Root1 ipv6-prefix 2001:DB8:11:: 64 static 32                           
  opcode ::111 end psp                                                       
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
 cost-style wide                                                                
 network-entity 10.0000.0000.0001.00                                            
 bier enable                                                                    
 #                                                                              
 ipv6 enable topology ipv6                                                      
 segment-routing ipv6 locator Root1 auto-sid-disable                            
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
 ip address 192.168.1.2 255.255.255.0                                           
 pim sm
# 
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:111::1/128                                               
 isis ipv6 enable 1                                                             
# 
bgp 100                                                                         
 router-id 1.1.1.1                                                              
 peer 2001:DB8:115::1 as-number 100                                             
 peer 2001:DB8:115::1 connect-interface LoopBack1                               
 #                                                                              
 ipv4-family unicast                                                            
  undo synchronization                                                          
 #                                                                              
 ipv4-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:115::1 enable                                                   
 #                                                                              
 ipv4-family vpnv4                                                              
  policy vpn-target                                                             
  peer 2001:DB8:115::1 enable                                                   
  peer 2001:DB8:115::1 prefix-sid                                               
 #                                                                              
 ipv4-family vpn-instance VPNA                                                  
  import-route direct                                                           
  segment-routing ipv6 locator Root1                                            
  segment-routing ipv6 best-effort 
  peer 192.168.1.1 as-number 65410                                              
# 
bier                                                                            
 sub-domain 0 ipv6
  bfr-id 2                                                              
  bfr-prefix interface LoopBack1                                                
  protocol isis                                                                 
  end-bier locator Root1 sid 2001:DB8:11::1                                     
  encapsulation-type ipv6 bsl 256 max-si 0                                      
# 
return
```

Root2 configuration file

```
#                                                                               
sysname Root2                                                                   
# 
multicast mvpn ipv6-underlay 2001:DB8:112::1                                    
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
   src-dt4 locator Root2 sid 2001:DB8:12::2                                     
   ipmsi-tunnel                                                                 
    bier                                                                        
   spmsi-tunnel                                                                 
    holddown-time 80                                                            
    switch-delay 20                                                             
    group 232.1.1.0 255.255.255.0 source 192.168.10.0 255.255.255.0 threshold 10 bier 
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:112::1                                   
 locator Root2 ipv6-prefix 2001:DB8:12:: 64 static 32                           
  opcode ::222 end psp                                                       
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
 cost-style wide                                                                
 network-entity 10.0000.0000.0002.00                                            
 bier enable                                                                    
 #                                                                              
 ipv6 enable topology ipv6                                                      
 segment-routing ipv6 locator Root2 auto-sid-disable                            
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
 ip address 192.168.2.2 255.255.255.0                                           
 pim sm
# 
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:112::1/128                                               
 isis ipv6 enable 1                                                             
# 
bgp 100                                                                         
 router-id 1.1.1.2                                                              
 peer 2001:DB8:115::1 as-number 100                                             
 peer 2001:DB8:115::1 connect-interface LoopBack1                               
 #                                                                              
 ipv4-family unicast                                                            
  undo synchronization                                                          
 #                                                                              
 ipv4-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:115::1 enable                                                   
 #                                                                              
 ipv4-family vpnv4                                                              
  policy vpn-target                                                             
  peer 2001:DB8:115::1 enable                                                   
  peer 2001:DB8:115::1 prefix-sid                                               
 #                                                                              
 ipv4-family vpn-instance VPNA                                                  
  import-route direct                                                           
  segment-routing ipv6 locator Root2                                            
  segment-routing ipv6 best-effort 
  peer 192.168.2.1 as-number 65410                                              
# 
bier                                                                            
 sub-domain 0 ipv6
  bfr-id 3                                                              
  bfr-prefix interface LoopBack1                                                
  protocol isis                                                                 
  end-bier locator Root2 sid 2001:DB8:12::1                                     
  encapsulation-type ipv6 bsl 256 max-si 0                                      
# 
return
```

P1 configuration file

```
#                                                                               
sysname P1                                                                      
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:113::1                                   
 locator P1 ipv6-prefix 2001:DB8:13:: 64 static 32                              
  opcode ::333 end psp                                                       
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
 cost-style wide                                                                
 network-entity 10.0000.0000.0003.00                                            
 bier enable                                                                    
 #                                                                              
 ipv6 enable topology ipv6                                                      
 segment-routing ipv6 locator P1 auto-sid-disable                               
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
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:113::1/128                                               
 isis ipv6 enable 1                                                             
# 
bier                                                                            
 sub-domain 0 ipv6                                                              
  bfr-prefix interface LoopBack1                                                
  protocol isis                                                                 
  end-bier locator P1 sid 2001:DB8:13::1                                        
  encapsulation-type ipv6 bsl 256 max-si 0                                      
#
return
```

P2 configuration file

```
#                                                                               
sysname P2                                                                      
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:114::1                                   
 locator P2 ipv6-prefix 2001:DB8:14:: 64 static 32                              
  opcode ::444 end psp                                                       
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
 cost-style wide                                                                
 network-entity 10.0000.0000.0004.00                                            
 bier enable                                                                    
 #                                                                              
 ipv6 enable topology ipv6                                                      
 segment-routing ipv6 locator P2 auto-sid-disable                               
 #                                                                              
#                                                                               
interface GigabitEthernet0/1/0                                                         
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:3::1/96
 isis ipv6 enable 1                                                             
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:4::1/96                                                  
 isis ipv6 enable 1                                                             
# 
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:114::1/128                                               
 isis ipv6 enable 1                                                             
# 
bier                                                                            
 sub-domain 0 ipv6                                                              
  bfr-prefix interface LoopBack1                                                
  protocol isis                                                                 
  end-bier locator P2 sid 2001:DB8:14::1                                        
  encapsulation-type ipv6 bsl 256 max-si 0                                      
#
return
```

PE1 configuration file

```
#                                                                               
sysname PE1                                                                 
# 
multicast mvpn ipv6-underlay 2001:DB8:115::1                                    
# 
ip vpn-instance VPNA                                                            
 ipv4-family                                                                    
  route-distinguisher 100:1                                                     
  vpn frr                                                                       
  apply-label per-instance                                                      
  vpn-target 111:1 export-extcommunity                                          
  vpn-target 111:1 import-extcommunity                                          
  multicast routing-enable                                                      
  mvpn                                                                          
   ipv6 underlay enable
   c-multicast signaling bgp                                                    
   c-multicast frr                                                              
   c-multicast frr flow-detection-based 2111
   multicast wtr 100                                       
# 
acl number 2111                                                                 
 rule 5 permit                                                                  
# 
segment-routing ipv6                                                                                               
 locator PE1 ipv6-prefix 2001:DB8:15:: 64 static 32                           
  opcode ::555 end psp                                                       
#                                                                               
isis 1                                                                          
 is-level level-2                                                               
 cost-style wide                                                                
 network-entity 10.0000.0000.0005.00                                            
 bier enable                                                                    
 #                                                                              
 ipv6 enable topology ipv6                                                      
 segment-routing ipv6 locator PE1 auto-sid-disable                            
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
 ip address 192.168.3.2 255.255.255.0                                           
 pim sm 
#
interface GigabitEthernet0/1/2                                                          
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:4::2/96                                                  
 isis ipv6 enable 1
#
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:115::1/128                                               
 isis ipv6 enable 1                                                             
# 
bgp 100                                                                         
 router-id 1.1.1.5                                                              
 peer 2001:DB8:111::1 as-number 100                                             
 peer 2001:DB8:111::1 connect-interface LoopBack1                               
 peer 2001:DB8:112::1 as-number 100                                             
 peer 2001:DB8:112::1 connect-interface LoopBack1                               
 #                                                                              
 ipv4-family unicast                                                            
  undo synchronization                                                          
 # 
 ipv4-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:111::1 enable                                                   
  peer 2001:DB8:112::1 enable                                                   
 #                                                                              
 ipv4-family vpnv4                                                              
  policy vpn-target                                                             
  peer 2001:DB8:111::1 enable                                                   
  peer 2001:DB8:111::1 prefix-sid                                               
  peer 2001:DB8:112::1 enable                                                   
  peer 2001:DB8:112::1 prefix-sid                                               
 #                                                                              
 ipv4-family vpn-instance VPNA                                                  
  import-route direct                                                           
  segment-routing ipv6 locator PE1                                            
  segment-routing ipv6 best-effort                             
  peer 192.168.3.1 as-number 65411                                              
# 
bier                                                                            
 sub-domain 0 ipv6                                                              
  bfr-id 1                                                                      
  bfr-prefix interface LoopBack1                                                
  protocol isis                                                                 
  end-bier locator PE1 sid 2001:DB8:15::1                                     
  encapsulation-type ipv6 bsl 256 max-si 0                                      
# 
return 
```