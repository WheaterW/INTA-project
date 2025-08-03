Example for Configuring GTMv6 over BIERv6 Dual-Root 1+1 Protection
==================================================================

This section describes how to configure GTMv6 over BIERv6 dual-root 1+1 protection. In this example, the unicast network is of the public network IPv6 over SRv6 type. Configuring multicast services on other types of unicast networks is similar to this procedure.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001216220077__fig35284409229), public network IPv6 over SRv6 has been deployed. CE1 is dual-homed to the public network in active-active mode. It is required that GTMv6 over BIERv6 services and dual-root 1+1 protection be deployed on the existing network.

**Figure 1** GTMv6 over BIERv6 dual-root 1+1 protection networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001171138806.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. (Optional) Configure public network IPv6 over SRv6 and ensure that unicast services are running properly. If the unicast network has been configured, skip this step.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on Root1, Root2, P1, P2, and PE1.
3. Establish a BGP MVPN peer relationship between Root1 and PE1 and between Root2 and PE1.
4. Configure multicast traffic forwarding over two BIERv6 I-PMSI tunnels.
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
6. Enable PIM on Root1, Root2, and PE1.
7. Configure dual-root 1+1 protection.

#### Data Preparation

To complete the configuration, you need the following data:

* Addresses of key interfaces on each device, as shown in [Figure 1](#EN-US_TASK_0000001216220077__fig35284409229)
* ID (1) of the public network IS-IS process, in a Level-2 area
* PE1's BFR-ID (1), sub-domain ID (0), BSL (256), and Max-SI (0)

#### Procedure

1. (Optional) Configure public network IPv6 over SRv6.
   
   
   
   This step is a part of configuring the unicast network, and its content is for reference only. In most cases, the unicast network has been configured before multicast services are deployed. If this is the case, skip this step and contact the configuration personnel for the configuration data related to the multicast services. For details about how to configure a unicast network, see **Segment Routing IPv6 Configuration** in the Configuration Guide.
   
   # Enable IPv6 forwarding on each interface and configure an IPv6 address for each interface. The configuration of Root1 is used as an example. The configurations of Root2, P1, P2, and PE1 are similar to the configuration of Root1. For configuration details, see Configuration Files in this section. Similar details will be omitted in the rest of the document.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Root1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Root1] interface gigabitethernet 0/1/0
   ```
   ```
   [~Root1-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*Root1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:3::1 112
   ```
   ```
   [*Root1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Root1] interface LoopBack 1
   ```
   ```
   [*Root1-LoopBack1] ipv6 enable
   ```
   ```
   [*Root1-LoopBack1] ipv6 address 2001:db8:111::1 128
   ```
   ```
   [*Root1-LoopBack1] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure IS-IS. The configuration of Root1 is used as an example. The configurations of Root2, P1, P2, and PE1 are similar to the configuration of Root1.
   
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
   
   # Establish an EBGP peer relationship between each root node and its connected CE, and between each PE and its connected CE. The peer relationship establishment between Root1 and CE1 is used as an example. The peer relationship establishment between Root2 and CE1, and between PE1 and CE2 is similar to that between Root1 and CE1.
   
   Establish an EBGP peer relationship on CE1.
   
   ```
   [*CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] ipv6 address 2001:DB8:2::1 112
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 11.11.11.11
   ```
   ```
   [*CE1-bgp] peer 2001:DB8:1::2 as-number 100
   ```
   ```
   [*CE1-bgp] ipv6-family unicast
   ```
   ```
   [*CE1-bgp-af-ipv6] peer 2001:DB8:1::2 enable
   ```
   ```
   [*CE1-bgp-af-ipv6] import-route direct
   ```
   ```
   [*CE1-bgp-af-ipv6] quit
   ```
   ```
   [*CE1-bgp-af] quit 
   ```
   ```
   [*CE1] commit
   ```
   
   Establish an EBGP peer relationship on Root1.
   
   ```
   [~Root1] bgp 100
   ```
   ```
   [*Root1-bgp] router-id 1.1.1.1
   ```
   ```
   [*Root1-bgp] peer 2001:DB8:1::1 as-number 65410
   ```
   ```
   [*Root1-bgp] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Establish an MP-IBGP peer relationship between Root1 and PE1 and between Root2 and PE1. The configuration of Root1 is used as an example. The configurations of Root2 and PE1 are similar to the configuration of Root1. After the [**peer enable**](cmdqueryname=peer+enable) command is run, the system displays a confirmation message. Enter **Y** in this case. Similar details will be omitted in the rest of the document.
   
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
   [*Root1-bgp] ipv6-family unicast
   ```
   ```
   [*Root1-bgp-af-ipv6] peer 2001:db8:115::1 enable
   ```
   ```
   [*Root1-bgp-af-ip6] peer 2001:db8:115::1 advertise-ext-community
   ```
   ```
   [*Root1-bgp-af-ipv6] quit
   ```
   ```
   [~Root1-bgp-af-evpn] commit
   ```
   ```
   [~Root1-bgp] quit
   ```
   
   # Configure SRv6 SIDs, and configure PEs to add SIDs to the VPN routes to be advertised. The configurations of Root1 and P1 are used as an example. The configurations of Root2 and PE1 are similar to the configuration of Root1, and the configurations of P2 are similar to the configurations of P1. The [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) command does not need to be run on PE1.
   
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
   [*Root1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*Root1-segment-routing-ipv6] quit
   ```
   ```
   [*Root1] bgp 100
   ```
   ```
   [*Root1-bgp] ipv6-family unicast
   ```
   ```
   [*Root1-bgp-af-ipv6] import-route direct
   ```
   ```
   [*Root1-bgp-af-ipv6] peer 2001:db8:115::1 prefix-sid advertise-srv6-locator
   ```
   ```
   [*Root1-bgp-af-ipv6] segment-routing ipv6 best-effort
   ```
   ```
   [*Root1-bgp-af-ipv6] segment-routing ipv6 locator Root1
   ```
   ```
   [*Root1-bgp-af-ipv6] quit
   ```
   ```
   [*Root1-bgp] quit
   ```
   ```
   [*Root1] isis 1
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
   [~Root1-bgp] ipv6-family mvpn
   ```
   ```
   [*Root1-bgp-af-mvpn6] peer 2001:db8:115::1 enable
   ```
   ```
   [*Root1-bgp-af-mvpn6] quit
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
   [~Root2-bgp] ipv6-family mvpn
   ```
   ```
   [*Root2-bgp-af-mvpnv6] peer 2001:db8:115::1 enable
   ```
   ```
   [*Root2-bgp-af-mvpnv6] quit
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
   [~PE1-bgp] ipv6-family mvpn
   ```
   ```
   [*PE1-bgp-af-mvpnv6] peer 2001:db8:111::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpnv6] peer 2001:db8:112::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpn6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Check information about BGP MVPN peers. The command output shows that a BGP MVPN peer relationship has been established between PE1 and Root1 and between PE1 and Root2.
   
   ```
   [~PE1] display bgp mvpn vpnv6 all peer
   
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
   [~Root1] multicast ipv6 routing-enable
   ```
   ```
   [*Root1] multicast ipv6 mvpn ipv6-underlay 2001:DB8:111::1 
   ```
   ```
   [*Root1] multicast ipv6 vpn-public
   ```
   ```
   [*Root1-mvpn-pub-ipv6] sender-enable
   ```
   ```
   [*Root1-mvpn-pub-ipv6] ipv6 underlay enable
   ```
   ```
   [*Root1-mvpn-pub-ipv6] src-dt6 locator Root1 sid 2001:db8:11::2
   ```
   ```
   [*Root1-mvpn-pub-ipv6] ipmsi-tunnel
   ```
   ```
   [*Root1-mvpn-pub-ipv6-ipmsi] bier sub-domain 0 bsl 256
   ```
   ```
   [*Root1-mvpn-pub-ipv6-ipmsi] quit
   ```
   ```
   [*Root1-mvpn-pub-ipv6] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   
   ```
   [~Root2] multicast ipv6 routing-enable
   ```
   ```
   [*Root2] multicast ipv6 mvpn ipv6-underlay 2001:DB8:112::1
   ```
   ```
   [*Root2] multicast ipv6 vpn-public
   ```
   ```
   [*Root2-mvpn-pub-ipv6] sender-enable
   ```
   ```
   [*Root2-mvpn-pub-ipv6] ipv6 underlay enable
   ```
   ```
   [*Root2-mvpn-pub-ipv6] src-dt6 locator Root2 sid 2001:db8:12::2
   ```
   ```
   [*Root2-mvpn-pub-ipv6] ipmsi-tunnel
   ```
   ```
   [*Root2-mvpn-pub-ipv6-ipmsi] bier sub-domain 0 bsl 256
   ```
   ```
   [*Root2-mvpn-pub-ipv6-ipmsi] quit
   ```
   ```
   [*Root2-mvpn-pub-ipv6] quit
   ```
   ```
   [*Root2] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] multicast ipv6 routing-enable
   ```
   ```
   [*PE1] multicast ipv6 mvpn ipv6-underlay 2001:DB8:115::1
   ```
   ```
   [*PE1] multicast ipv6 vpn-public
   ```
   ```
   [*PE1-mvpn-pub-ipv6] c-multicast signaling bgp
   ```
   ```
   [*PE1-mvpn-pub-ipv6] ipv6 underlay enable
   ```
   ```
   [*PE1-mvpn-pub-ipv6] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Check I-PMSI tunnel information of MVPN services in a specified VPN instance. The command output shows that two I-PMSI tunnels have been established, with Root1 and Root2 as the root nodes and PE1 as a leaf node.
   
   ```
   [~PE1]display mvpn ipv6 public ipmsi
   MVPN local I-PMSI information for VPN-Instance: _public_
   Tunnel type: BIER IPv6
   Tunnel state: --
   Src-dt6 SID: 2001:DB8:11::2
   Sub-domain ID: 0
   BFR-ID: --
   BFR prefix: 2001:DB8:111::1
   Root: 2001:DB8:111::1
   Leaf: 
     1: 2001:DB8:115::1 (BFR-ID: 1, BFR prefix: 2001:DB8:115::1) (local)
   
   Tunnel type: BIER IPv6
   Tunnel state: --
   Src-dt6 SID: 2001:DB8:12::2
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
   [~Root1] multicast ipv6 vpn-public
   ```
   ```
   [*Root1-mvpn-pub-ipv6] spmsi-tunnel
   ```
   ```
   [*Root1-mvpn-pub-ipv6-spmsi] group FF3E::0 112 source 2001:db8:555::0 112 threshold 10 bier
   ```
   ```
   [*Root1-mvpn-pub-ipv6-spmsi] switch-delay 20
   ```
   ```
   [*Root1-mvpn-pub-ipv6-spmsi] holddown-time 80
   ```
   ```
   [*Root1-mvpn-pub-ipv6-spmsi] quit
   ```
   ```
   [*Root1-mvpn-pub-ipv6] quit
   ```
   ```
   [*Root1] commit
   ```
   
   # Configure Root2.
   
   ```
   [~Root2] multicast ipv6 vpn-public
   ```
   ```
   [*Root2-mvpn-pub-ipv6] spmsi-tunnel
   ```
   ```
   [*Root2-mvpn-pub-ipv6-spmsi] group FF3E::0 112 source 2001:db8:555::0 112 threshold 10 bier 
   ```
   ```
   [*Root2-mvpn-pub-ipv6-spmsi] switch-delay 20
   ```
   ```
   [*Root2-mvpn-pub-ipv6-spmsi] holddown-time 80
   ```
   ```
   [*Root2-mvpn-pub-ipv6-spmsi] quit
   ```
   ```
   [*Root2-mvpn-pub-ipv6] quit
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
   [~Root1-GigabitEthernet0/1/1] pim ipv6 sm
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
   [~Root2-GigabitEthernet0/1/1] pim ipv6 sm
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
   [~PE1-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
7. Configure dual-root 1+1 protection.
   
   # Configure Auto FRR on PE1.
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] auto-frr
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure multicast FRR in flow-based detection mode on PE1.
   
   ```
   [~PE1] acl ipv6 2111
   ```
   ```
   [*PE1-acl6-basic-2111] rule permit source any
   ```
   ```
   [*PE1-acl6-basic-2111] quit
   ```
   ```
   [*PE1] multicast ipv6 vpn-public
   ```
   ```
   [*PE1-mvpn-pub-ipv6] c-multicast frr
   ```
   ```
   [*PE1-mvpn-pub-ipv6] c-multicast frr flow-detection-based 2111
   ```
   ```
   [*PE1-mvpn-pub-ipv6] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Check S-PMSI tunnel information of MVPN services in a specified VPN instance. The command output on PE1 shows S-PMSI tunnel and multicast user information.
   
   ```
   [~PE1]display mvpn ipv6 public spmsi verbose
   MVPN local S-PMSI information for VPN-Instance : _public_ 
    Total number of tunnel: 2 
    S-PMSI A-D Route Type: -- 
    Tunnel type: BIER IPv6 
    Tunnel state: -- 
    Src-dt6 SID: 2001:DB8:11::1 
    Sub-domain ID: 0 
    BFR-ID: -- 
    BFR prefix: 2001:DB8:111::1 
    Root: 2001:DB8:111::1 
    Leaf: 
      1: 2001:DB8:115::1 (BFR-ID: 2, BFR prefix: 2001:DB8:115::1)(local)
    Total number of (S, G): 2 
        1. (2001:db8:555::0, FF3E::1) 
        2. (2001:db8:555::0, FF3E::2)
   
    Total number of tunnel: 2 
    S-PMSI A-D Route Type: -- 
    Tunnel type: BIER IPv6 
    Tunnel state: -- 
    Src-dt6 SID: 2001:DB8:12::1 
    Sub-domain ID: 0 
    BFR-ID: -- 
    BFR prefix: 2001:DB8:112::1 
    Root: 2001:DB8:112::1 
    Leaf: 
      1: 2001:DB8:115::1 (BFR-ID: 2, BFR prefix: 2001:DB8:115::1)(local)
    Total number of (S, G): 2 
        1. (2001:db8:555::0, FF3E::1) 
        2. (2001:db8:555::0, FF3E::2)
   ```
8. Verify the configuration.
   
   
   
   # Run the **display pim ipv6 routing-table** command to check the IPv6 PIM routing table. The command output shows that a backup upstream interface exists.
   
   ```
   [~PE1] display pim ipv6 all-instance routing-table mode sm outgoing-interface-number  
   VPN-Instance: public net  
   Total 0 (*, G) entries; 2 (S, G) entry   
   (2001:db8:555::0, FF3E::1)           
      Protocol: pim-sm, Flag: SG_RCVRR      
      UpTime: 00:00:04      
      Upstream interface: through-BGP, Refresh time: 00:00:04          
          Upstream neighbor: 2001:DB8:111::1           
          RPF prime neighbor: 2001:DB8:111::1
      Backup upstream interface: through-BGP          
          Upstream neighbor: 2001:DB8:112::1           
          RPF prime neighbor: 2001:DB8:112::1
      Downstream interface(s) information:      
      Total number of downstreams: 1  
   
   (2001:db8:555::0, FF3E::2)           
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
multicast ipv6 routing-enable
#
interface GigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:1::1/112
 pim ipv6 sm
#
interface GigabitEthernet0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:2::1/112
 pim ipv6 sm
#
interface GigabitEthernet0/1/3
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:555::0/112
 pim ipv6 sm
#
bgp 65410
 router-id 11.11.11.11
 peer 2001:DB8:1::2 as-number 100
 peer 2001:DB8:2::2 as-number 100
 #
 ipv6-family unicast
  undo synchronization
  import-route direct
  peer 2001:DB8:1::2 enable
  peer 2001:DB8:2::2 enable
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
interface GigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:9::2/112
 pim ipv6 sm
 mld enable
#
interface GigabitEthernet0/1/1
 undo shutdown
 ipv6 enable
 ipv6 address 2001:DB8:7::2/112
 pim ipv6 sm
#
bgp 65411
 router-id 12.12.12.12
 peer 2001:DB8:7::1 as-number 100
 #
 ipv6-family unicast
  undo synchronization
  import-route direct
  peer 2001:DB8:7::1 enable
#
return
```

Root1 configuration file

```
#                                                                               
sysname Root1                                                                   
#
multicast ipv6 routing-enable
# 
multicast ipv6 mvpn ipv6-underlay 2001:DB8:111::1                                    
#                                                     
multicast ipv6 vpn-public                                                                          
 ipv6 underlay enable                                                         
 sender-enable                                                                
 src-dt6 locator Root1 sid 2001:DB8:11::2                                     
 ipmsi-tunnel                                                                 
  bier                                                                        
 spmsi-tunnel                                                                 
  holddown-time 80                                                            
  switch-delay 20                                                             
  group FF3E::0 112 source 2001:DB8:555::0 112 threshold 10 bier 
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:111::1                                   
 locator Root1 ipv6-prefix 2001:DB8:11:: 64 static 32                                                                                 
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
 ipv6 address 2001:DB8:3::1/112                                                  
 isis ipv6 enable 1
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ipv6 enable                                                   
 ipv6 address 2001:DB8:1::2/112                                           
 pim ipv6 sm
# 
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:111::1/128                                               
 isis ipv6 enable 1                                                             
# 
bgp 100                                                                         
 router-id 1.1.1.1
 peer 2001:DB8:1::1 as-number 65410                                                             
 peer 2001:DB8:115::1 as-number 100                                             
 peer 2001:DB8:115::1 connect-interface LoopBack1                               
 #
 ipv4-family unicast                                                            
  undo synchronization
 #                                                                              
 ipv6-family unicast                                                            
  undo synchronization
  import-route direct
  segment-routing ipv6 locator Root1
  segment-routing ipv6 best-effort
  peer 2001:DB8:1::1 enable
  peer 2001:DB8:115::1 enable
  peer 2001:DB8:115::1 advertise-ext-community
  peer 2001:DB8:115::1 prefix-sid advertise-srv6-locator                                                          
 #                                                                              
 ipv6-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:115::1 enable
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
multicast ipv6 routing-enable
# 
multicast ipv6 mvpn ipv6-underlay 2001:DB8:112::1                                    
#                                                      
multicast ipv6 vpn-public
 ipv6 underlay enable                                                         
 sender-enable                                                                
 src-dt6 locator Root2 sid 2001:DB8:12::2                                     
 ipmsi-tunnel                                                                 
  bier                                                                        
 spmsi-tunnel                                                                 
  holddown-time 80                                                            
  switch-delay 20                                                             
  group FF3E::0 112 source 2001:DB8:555::0 112 threshold 10 bier 
# 
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:112::1                                   
 locator Root2 ipv6-prefix 2001:DB8:12:: 64 static 32 
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
 ipv6 address 2001:DB8:4::1/112                                                  
 isis ipv6 enable 1
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown
 ipv6 enable                                                    
 ipv6 address 2001:DB8:2::2/112                                           
 pim ipv6 sm
# 
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:112::1/128                                               
 isis ipv6 enable 1                                                             
# 
bgp 100                                                                         
 router-id 1.1.1.2
 peer 2001:DB8:2::1 as-number 65410                                                              
 peer 2001:DB8:115::1 as-number 100                                             
 peer 2001:DB8:115::1 connect-interface LoopBack1                               
 #
 ipv4-family unicast                                                            
  undo synchronization
 #
 ipv6-family unicast                                                            
  undo synchronization
  import-route direct
  segment-routing ipv6 locator Root2
  segment-routing ipv6 best-effort
  peer 2001:DB8:2::1 enable
  peer 2001:DB8:115::1 enable
  peer 2001:DB8:115::1 advertise-ext-community
  peer 2001:DB8:115::1 prefix-sid advertise-srv6-locator                                                          
 #                                                                              
 ipv6-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:115::1 enable                                                   
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
 ipv6 address 2001:DB8:3::2/112
 isis ipv6 enable 1                                                             
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:5::1/112                                                  
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
 ipv6 address 2001:DB8:4::2/112
 isis ipv6 enable 1                                                             
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                                  
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:6::1/112                                                  
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
multicast ipv6 routing-enable
# 
multicast ipv6 mvpn ipv6-underlay 2001:DB8:115::1                                    
#                                                                                                                   
multicast ipv6 vpn-public                                                                          
 ipv6 underlay enable
 c-multicast signaling bgp                                                    
 c-multicast frr                                                              
 c-multicast frr flow-detection-based 2111
# 
acl ipv6 number 2111                                                                 
 rule 5 permit                                                                  
# 
segment-routing ipv6                                                                                               
 locator PE1 ipv6-prefix 2001:DB8:15:: 64 static 32                           
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
 ipv6 address 2001:DB8:5::2/112                                                  
 isis ipv6 enable 1 
#                                                                               
interface GigabitEthernet0/1/1                                                       
 undo shutdown 
 ipv6 enable                                         
 ipv6 address 2001:DB8:7::1/112                                           
 pim ipv6 sm 
# 
interface GigabitEthernet0/1/2                                                       
 undo shutdown
 ipv6 enable  
 ipv6 address 2001:DB8:6::2/112                                           
 pim ipv6 sm
 isis ipv6 enable 1 
#
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:115::1/128                                               
 isis ipv6 enable 1                                                             
# 
bgp 100                                                                         
 router-id 1.1.1.5
 peer 2001:DB8:7::2 as-number 65411                                                              
 peer 2001:DB8:111::1 as-number 100                                             
 peer 2001:DB8:111::1 connect-interface LoopBack1                               
 peer 2001:DB8:112::1 as-number 100                                             
 peer 2001:DB8:112::1 connect-interface LoopBack1                               
 # 
 ipv4-family unicast                                                            
  undo synchronization
 #
 ipv6-family unicast                                                            
  undo synchronization
  import-route direct
  auto-frr
  segment-routing ipv6 locator PE1
  segment-routing ipv6 best-effort
  peer 2001:DB8:7::2 enable
  peer 2001:DB8:111::1 enable
  peer 2001:DB8:111::1 advertise-ext-community
  peer 2001:DB8:111::1 prefix-sid advertise-srv6-locator
  peer 2001:DB8:112::1 enable
  peer 2001:DB8:111::1 advertise-ext-community
  peer 2001:DB8:112::1 prefix-sid advertise-srv6-locator
 # 
 ipv6-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:111::1 enable                                                  
  peer 2001:DB8:112::1 enable
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