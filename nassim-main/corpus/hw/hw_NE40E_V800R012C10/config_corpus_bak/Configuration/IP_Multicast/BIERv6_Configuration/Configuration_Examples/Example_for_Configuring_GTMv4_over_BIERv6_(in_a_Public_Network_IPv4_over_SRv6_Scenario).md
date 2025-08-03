Example for Configuring GTMv4 over BIERv6 (in a Public Network IPv4 over SRv6 Scenario)
=======================================================================================

This section describes how to configure GTMv4 over BIERv6 in a public network IPv4 over SRv6 scenario.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001207908743__fig35284409229), public network IPv4 over SRv6 has been deployed. It is required that GTMv4 over BIERv6 be deployed on the existing network.

**Figure 1** GTMv4 over BIERv6 networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001207628729.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. (Optional) Configure public network IPv4 over SRv6 and ensure that unicast services are running properly. If the unicast network has been configured, skip this step.
2. Configure basic BIERv6 functions and enable IS-ISv6 for BIERv6 on PE1, PE2, PE3, and the P.
3. Establish BGP MVPN peer relationships between PEs.
4. Configure multicast traffic forwarding over a BIERv6 I-PMSI tunnel.
5. Enable the BIERv6 S-PMSI tunnel function and configure switching criteria.
6. Enable PIM on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* Addresses of key interfaces on each device, as shown in [Figure 1](#EN-US_TASK_0000001207908743__fig35284409229)
* ID (1) of the public network IS-IS process, in a Level-2 area
* PE2's BFR-ID (2), PE3's BFR-ID (3), sub-domain ID (0), BSL (256), and Max-SI (0)

#### Procedure

1. (Optional) Configure public network IPv4 over SRv6.
   
   
   
   This step is a part of configuring the unicast network, and its content is for reference only. In most cases, the unicast network has been configured before multicast services are deployed. If this is the case, skip this step and contact the configuration personnel for the configuration data related to the multicast services. For details about how to configure a unicast network, see **Segment Routing IPv6 Configuration** in the Configuration Guide.
   
   # Enable IPv6 forwarding on each interface and configure an IPv6 address for each interface. The configuration of PE1 is used as an example. The configurations of PE2, PE3, and the P are similar to the configuration of PE1. For configuration details, see Configuration Files in this section. Similar details will be omitted in the rest of the document.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 96
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface LoopBack 1
   ```
   ```
   [*PE1-LoopBack1] ipv6 enable
   ```
   ```
   [*PE1-LoopBack1] ipv6 address 2001:db8:10::1 128
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
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
   
   # Establish an EBGP peer relationship between each PE and its connected CE. The establishment of an EBGP peer relationship between PE1 and CE1 is used as an example. The establishment of an EBGP peer relationship between PE2 and CE2, and between PE3 and CE3 is similar to that between PE1 and CE1.
   
   ```
   [~CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 11.11.11.11
   ```
   ```
   [*CE1-bgp] peer 192.168.1.1 as-number 100
   ```
   ```
   [*CE1-bgp] ipv4-family unicast
   ```
   ```
   [*CE1-bgp-af-ipv4] peer 192.168.1.1 enable
   ```
   ```
   [*CE1-bgp-af-ipv4] quit
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
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] peer 192.168.1.2 as-number 65410
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 192.168.1.2 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Establish an IBGP peer relationship between PE1 and PE2 and between PE1 and PE3. The configuration of PE1 is used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1. After the [**peer enable**](cmdqueryname=peer+enable) command is run, the system displays a confirmation message. Enter **Y** in this case. Similar details will be omitted in the rest of the document.
   
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
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:db8:20::1 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:db8:30::1 enable
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:db8:30::1 advertise-ext-community
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:db8:20::1 advertise-ext-community
   ```
   ```
   [*PE1-bgp-af-ipv4] commit
   ```
   ```
   [~PE1-bgp-af-ipv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure SRv6 SIDs and enable PEs to exchange prefix SIDs with their peers. The configurations of PE1 and P are used as an example. The configurations of PE2 and PE3 are similar to the configuration of PE1.
   
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
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv4] import-route direct
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:db8:20::1 prefix-sid advertise-srv6-locator
   ```
   ```
   [*PE1-bgp-af-ipv4] peer 2001:db8:30::1 prefix-sid advertise-srv6-locator
   ```
   ```
   [*PE1-bgp-af-ipv4] segment-routing ipv6 best-effort
   ```
   ```
   [*PE1-bgp-af-ipv4] segment-routing ipv6 locator PE1
   ```
   ```
   [*PE1-bgp-af-ipv4] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable 
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
   [~PE1-bgp] ipv4-family mvpn
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 2001:db8:20::1 enable
   ```
   ```
   [*PE1-bgp-af-mvpn] peer 2001:db8:30::1 enable
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
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] ipv4-family mvpn
   ```
   ```
   [*PE2-bgp-af-mvpn] peer 2001:db8:10::1 enable
   ```
   ```
   [*PE2-bgp-af-mvpn] quit
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
   [~PE3-bgp] ipv4-family mvpn
   ```
   ```
   [*PE3-bgp-af-mvpn] peer 2001:db8:10::1 enable
   ```
   ```
   [*PE3-bgp-af-mvpn] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
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
   [~PE1] multicast routing-enable
   ```
   ```
   [*PE1] multicast mvpn ipv6-underlay 2001:db8:10::1
   ```
   ```
   [*PE1] multicast vpn-public
   ```
   ```
   [*PE1-mvpn-pub] sender-enable
   ```
   ```
   [*PE1-mvpn-pub] ipv6 underlay enable
   ```
   ```
   [*PE1-mvpn-pub] src-dt4 locator PE1 sid 2001:db8:100::2
   ```
   ```
   [*PE1-mvpn-pub] rpt-spt mode
   ```
   ```
   [*PE1-mvpn-pub] ipmsi-tunnel
   ```
   ```
   [*PE1-mvpn-pub-ipmsi] bier sub-domain 0 bsl 256
   ```
   ```
   [*PE1-mvpn-pub-ipmsi] quit
   ```
   ```
   [*PE1-mvpn-pub] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] multicast routing-enable
   ```
   ```
   [*PE2] multicast mvpn ipv6-underlay 2001:db8:20::1
   ```
   ```
   [*PE2] multicast vpn-public
   ```
   ```
   [*PE2-mvpn-pub] c-multicast signaling bgp
   ```
   ```
   [*PE2-mvpn-pub] ipv6 underlay enable
   ```
   ```
   [*PE2-mvpn-pub] rpt-spt mode
   ```
   ```
   [*PE2-mvpn-pub] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] multicast routing-enable
   ```
   ```
   [*PE3] multicast mvpn ipv6-underlay 2001:db8:30::1
   ```
   ```
   [*PE3] multicast vpn-public
   ```
   ```
   [*PE3-mvpn-pub] c-multicast signaling bgp
   ```
   ```
   [*PE3-mvpn-pub] ipv6 underlay enable
   ```
   ```
   [*PE3-mvpn-pub] rpt-spt mode
   ```
   ```
   [*PE3-mvpn-pub] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Check I-PMSI tunnel information of MVPN services in a specified VPN instance. The command output shows that an I-PMSI tunnel has been established, with PE1 as the root node and PE2 and PE3 as leaf nodes.
   
   ```
   [~PE1]display mvpn public ipmsi
   MVPN local I-PMSI information for VPN-Instance: _public_
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
   [~PE1] multicast vpn-public
   ```
   ```
   [*PE1-mvpn-pub] ipmsi-to-spmsi switch immediately
   ```
   ```
   [*PE1-mvpn-pub] spmsi-tunnel
   ```
   ```
   [*PE1-mvpn-pub-spmsi] group 225.1.1.0 24 source 192.168.11.0 24 threshold 10 bier 
   ```
   ```
   [*PE1-mvpn-pub--spmsi] switch-delay 20
   ```
   ```
   [*PE1-mvpn-pub--spmsi] holddown-time 80
   ```
   ```
   [*PE1-mvpn-pub-spmsi] quit
   ```
   ```
   [*PE1-mvpn-pub] quit
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
   [~PE1-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] interface LoopBack2
   ```
   ```
   [*PE1-Loopback2] ip address 10.1.1.1 255.255.255.255
   ```
   ```
   [*PE1-Loopback2] pim sm 
   ```
   ```
   [*PE1-Loopback2] quit
   ```
   ```
   [*PE1] pim
   ```
   ```
   [*PE1-pim] static-rp 10.1.1.1
   ```
   ```
   [*PE1-pim] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] pim
   ```
   ```
   [*PE2-pim] static-rp 10.1.1.1
   ```
   ```
   [*PE2-pim] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface gigabitethernet 0/1/1
   ```
   ```
   [~PE3-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*PE3-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE3] pim 
   ```
   ```
   [*PE3-pim] static-rp 10.1.1.1
   ```
   ```
   [*PE3-pim] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Check S-PMSI tunnel information of MVPN services in a specified VPN instance. The command output on PE2 shows S-PMSI tunnel and multicast user information.
   
   ```
   [~PE2] display mvpn public spmsi verbose
   MVPN local S-PMSI information for VPN-Instance : _public_ 
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

#### Configuration Files

CE1 configuration file

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

CE2 configuration file

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

CE3 configuration file

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

PE1 configuration file

```
#                                                                               
sysname PE1                                                                     
#
multicast routing-enable
#                                                                               
multicast mvpn ipv6-underlay 2001:DB8:10::1
#                                                                               
multicast vpn-public 
 ipv6 underlay enable                                                         
 sender-enable                                                                
 src-dt4 locator PE1 sid 2001:DB8:100::2
 rpt-spt mode                                     
 ipmsi-tunnel 
  bier sub-domain 0 bsl 256
 ipmsi-to-spmsi switch immediately
 spmsi-tunnel                                                                 
  holddown-time 80                                                            
  switch-delay 20                                                             
  group 225.1.1.0 255.255.255.0 source 192.168.11.0 255.255.255.0 threshold 10 bier
#                                                                               
segment-routing ipv6
 encapsulation source-address 2001:DB8:10::1 
 locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
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
 ip address 192.168.1.1 255.255.255.0                                           
 pim sm
#
interface LoopBack2
 ip address 10.1.1.1 255.255.255.255
 pim sm                                                                      
#
pim
 static-rp 10.1.1.1
#                                                                               
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:10::1/128                                                
 isis ipv6 enable 1                                                             
#                                                                               
bgp 100                                                                         
 router-id 1.1.1.1
 peer 192.168.1.2 as-number 65410 
 peer 2001:DB8:20::1 as-number 100                                              
 peer 2001:DB8:20::1 connect-interface LoopBack1                                
 peer 2001:DB8:30::1 as-number 100                                              
 peer 2001:DB8:30::1 connect-interface LoopBack1                                
 #                                                                              
 ipv4-family unicast                                                              
  undo synchronization
  import-route direct
  segment-routing ipv6 locator PE1                                              
  segment-routing ipv6 best-effort
  peer 192.168.1.2 enable
  peer 2001:DB8:20::1 enable
  peer 2001:DB8:20::1 advertise-ext-community
  peer 2001:DB8:20::1 prefix-sid advertise-srv6-locator
  peer 2001:DB8:30::1 enable
  peer 2001:DB8:30::1 advertise-ext-community
  peer 2001:DB8:30::1 prefix-sid advertise-srv6-locator
 #                                                                              
 ipv4-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:20::1 enable                                                    
  peer 2001:DB8:30::1 enable
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
multicast routing-enable 
#                                                                               
multicast mvpn ipv6-underlay 2001:DB8:20::1                                     
#                                                                               
multicast vpn-public  
 ipv6 underlay enable
 c-multicast signaling bgp
 rpt-spt mode                                                    
#                                                                               
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:20::1                                    
 locator PE2 ipv6-prefix 2001:DB8:200:: 64 static 32
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
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                             
 ip address 192.168.2.1 255.255.255.0  
 pim sm
# 
pim
 static-rp 10.1.1.1
#
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:20::1/128                                                
 isis ipv6 enable 1                                                             
#                                                                               
bgp 100                                                                         
 router-id 1.1.1.2
 peer 192.168.2.2 as-number 65411                                                              
 peer 2001:DB8:10::1 as-number 100                                              
 peer 2001:DB8:10::1 connect-interface LoopBack1                                
 #                                                                              
 ipv4-family unicast                                                            
  undo synchronization
  import-route direct                                                           
  segment-routing ipv6 locator PE2                                              
  segment-routing ipv6 best-effort
  peer 192.168.2.2 enable
  peer 2001:DB8:10::1 enable
  peer 2001:DB8:10::1 advertise-ext-community
  peer 2001:DB8:10::1 prefix-sid advertise-srv6-locator
 #                      
 ipv4-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:10::1 enable                                                                                                  
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
multicast routing-enable
#                                                                               
multicast mvpn ipv6-underlay 2001:DB8:30::1                                     
#                                                                               
multicast vpn-public                                                                          
 ipv6 underlay enable
 c-multicast signaling bgp
 rpt-spt mode                                                    
#                                                                               
segment-routing ipv6                                                            
 encapsulation source-address 2001:DB8:30::1                                    
 locator PE3 ipv6-prefix 2001:DB8:300:: 64 static 32                                                       
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
#                                                                               
interface GigabitEthernet0/1/1                                                         
 undo shutdown                                                   
 ip address 192.168.3.1 255.255.255.0  
 pim sm
#
pim
 static-rp 10.1.1.1
#
interface LoopBack1                                                             
 ipv6 enable                                                                    
 ipv6 address 2001:DB8:30::1/128                                                
 isis ipv6 enable 1                                                             
#                                                                               
bgp 100                                                                         
 router-id 1.1.1.3
 peer 192.168.3.2 as-number 65412                                                              
 peer 2001:DB8:10::1 as-number 100                                              
 peer 2001:DB8:10::1 connect-interface LoopBack1                                
 #                                                                              
 ipv4-family unicast                                                            
  undo synchronization
  import-route direct                                                           
  segment-routing ipv6 locator PE3                                              
  segment-routing ipv6 best-effort
  peer 192.168.3.2 enable
  peer 2001:DB8:10::1 enable
  peer 2001:DB8:10::1 advertise-ext-community
  peer 2001:DB8:10::1 prefix-sid advertise-srv6-locator
 #                      
 ipv4-family mvpn                                                               
  policy vpn-target                                                             
  peer 2001:DB8:10::1 enable                                          
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