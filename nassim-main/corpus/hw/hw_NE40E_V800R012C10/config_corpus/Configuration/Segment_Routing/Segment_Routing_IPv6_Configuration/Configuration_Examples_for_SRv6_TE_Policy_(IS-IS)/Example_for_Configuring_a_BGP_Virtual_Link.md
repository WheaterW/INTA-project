Example for Configuring a BGP Virtual Link
==========================================

An SRv6 EPE virtual link can be created for a BGP multi-hop peer relationship to implement communication across a third-party network.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001241440579__en-us_task_0000001196932245_fig_dc_vrp_seamless_mpls_cfg_003102), a third-party network is deployed between DeviceC and DeviceD. The two devices run IS-IS for basic routing and establish an IBGP peer relationship. IPv6 EBGP peer relationships are established between directly connected interfaces of DeviceB and DeviceC, and between directly connected interfaces of DeviceD and DeviceE. To establish an SRv6 TE Policy across the third-party network, you can configure a BGP peer relationship-based virtual link between DeviceB and DeviceE. In addition, attribute information required for SRv6 TE Policy path computation is provided, such as the link latency, metric, affinity, and SRLG. This prevents the mismatch of the address information in the link information reported by DeviceB and DeviceE through BGP-LS, which would otherwise cause a link combination failure on the controller.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 and 2 represent GE0/1/0 and GE0/2/0, respectively.


**Figure 1** Configuring a BGP virtual link  
![](figure/en-us_image_0000001173355208.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface on DeviceA through DeviceE.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) for DeviceC and DeviceD.
3. Configure a VPN instance on DeviceC and DeviceD.
4. Establish an IBGP peer relationship between DeviceC and DeviceD.
5. Establish an EBGP peer relationship between DeviceB and DeviceC and another one between DeviceD and DeviceE.
6. Configure SRv6 SIDs and IS-IS SRv6 and configure VPN routes to carry the SID attribute on DeviceC and DeviceD.
7. Configure an SRv6 TE Policy on DeviceC and DeviceD.
8. Configure a tunnel policy on DeviceC and DeviceD to import VPN traffic.
9. Establish an EBGP peer relationship between DeviceB and DeviceE.
10. Configure a VPN instance on DeviceA and DeviceE.
11. Establish an EBGP peer relationship between DeviceA and DeviceE.
12. Configure SRv6 SIDs and enable IS-IS SRv6 on DeviceA, DeviceB, and DeviceE. Configure VPN routes to carry the SID attribute on DeviceA and DeviceE.
13. Configure the BGP EPE and virtual link functions on DeviceB and DeviceE.
14. Configure an SRv6 TE Policy on DeviceA and DeviceE.
15. Configure a tunnel policy on DeviceA and DeviceE to import VPN traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of interfaces on DeviceA through DeviceE
* IS-IS process IDs and levels on DeviceA through DeviceD
* VPN instance names, RDs, and RTs on DeviceA, DeviceE, DeviceC, and DeviceD

#### Procedure

1. Configure IPv6 addresses and enable IPv6 forwarding for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface gigabitethernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:44::1/96
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface loopBack 1
   [*DeviceA-LoopBack1] ipv6 enable
   [*DeviceA-LoopBack1] ipv6 address 2001:db8:1::1/128
   [*DeviceA-LoopBack1] commit
   [~DeviceA-LoopBack1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <DeviceB> system-view
   [~DeviceB] interface gigabitethernet 0/1/0
   [~DeviceB-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:11::1/96
   [*DeviceB-GigabitEthernet0/1/0] quit
   [~DeviceB] interface gigabitethernet 0/2/0
   [~DeviceB-GigabitEthernet0/2/0] ipv6 enable
   [*DeviceB-GigabitEthernet0/2/0] ipv6 address 2001:db8:44::2/96
   [*DeviceB-GigabitEthernet0/2/0] quit
   [*DeviceB] interface loopBack 1
   [*DeviceB-LoopBack1] ipv6 enable
   [*DeviceB-LoopBack1] ipv6 address 2001:db8:2::2/128
   [*DeviceB-LoopBack1] commit
   [~DeviceB-LoopBack1] quit
   ```
   
   # Configure DeviceC.
   
   ```
   <DeviceC> system-view
   [~DeviceC] interface gigabitethernet 0/1/0
   [~DeviceC-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceC-GigabitEthernet0/1/0] ipv6 address 2001:db8:22::1/96
   [*DeviceC-GigabitEthernet0/1/0] quit
   [*DeviceC] interface gigabitethernet 0/2/0
   [*DeviceC-GigabitEthernet0/2/0] ipv6 enable
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address 2001:db8:11::2/96
   [*DeviceC-GigabitEthernet0/2/0] quit
   [*DeviceC] interface loopBack 1
   [*DeviceC-LoopBack1] ipv6 enable
   [*DeviceC-LoopBack1] ipv6 address 2001:db8:3::3/128
   [*DeviceC-LoopBack1] commit
   [~DeviceC-LoopBack1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   <DeviceD> system-view
   [~DeviceD] interface gigabitethernet 0/1/0
   [~DeviceD-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceD-GigabitEthernet0/1/0] ipv6 address 2001:db8:33::1/96
   [*DeviceD-GigabitEthernet0/1/0] quit
   [*DeviceD] interface gigabitethernet 0/2/0
   [*DeviceD-GigabitEthernet0/2/0] ipv6 enable
   [*DeviceD-GigabitEthernet0/2/0] ipv6 address 2001:db8:22::2/96
   [*DeviceD-GigabitEthernet0/2/0] quit
   [*DeviceD] interface loopBack 1
   [*DeviceD-LoopBack1] ipv6 enable
   [*DeviceD-LoopBack1] ipv6 address 2001:db8:4::4/128
   [*DeviceD-LoopBack1] commit
   [~DeviceD-LoopBack1] quit
   ```
   
   # Configure DeviceE.
   
   ```
   <DeviceE> system-view
   [~DeviceE] interface gigabitethernet 0/2/0
   [~DeviceE-GigabitEthernet0/2/0] ipv6 enable
   [*DeviceE-GigabitEthernet0/2/0] ipv6 address 2001:db8:33::2/96
   [*DeviceE-GigabitEthernet0/2/0] quit
   [*DeviceE] interface loopBack 1
   [*DeviceE-LoopBack1] ipv6 enable
   [*DeviceE-LoopBack1] ipv6 address 2001:db8:5::5/128
   [*DeviceE-LoopBack1] commit
   [~DeviceE-LoopBack1] quit
   ```
   
   The interfaces that directly connect the devices can ping each other, but the devices cannot ping each other's loopback interface.
2. Configure IS-IS.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] is-level level-1
   [*DeviceA-isis-1] cost-style wide
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] ipv6 enable topology ipv6
   [*DeviceA-isis-1] quit
   [*DeviceA] interface gigabitethernet 0/1/0
   [*DeviceA-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] interface loopBack 1
   [*DeviceA-LoopBack1] isis ipv6 enable 1
   [*DeviceA-LoopBack1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] is-level level-1
   [*DeviceB-isis-1] cost-style wide
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   [*DeviceB-isis-1] ipv6 enable topology ipv6
   [*DeviceB-isis-1] ipv6 import-route bgp level-1
   [*DeviceB-isis-1] quit
   [*DeviceB] interface gigabitethernet 0/2/0
   [*DeviceB-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*DeviceB-GigabitEthernet0/2/0] quit
   [*DeviceB] interface loopBack 1
   [*DeviceB-LoopBack1] isis ipv6 enable 1
   [*DeviceB-LoopBack1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 100
   [*DeviceC-isis-100] is-level level-2
   [*DeviceC-isis-100] cost-style wide
   [*DeviceC-isis-100] network-entity 20.0000.0000.0001.00
   [*DeviceC-isis-100] ipv6 enable topology ipv6
   [*DeviceC-isis-100] quit
   [*DeviceC] interface gigabitethernet 0/1/0
   [*DeviceC-GigabitEthernet0/1/0] isis ipv6 enable 100
   [*DeviceC-GigabitEthernet0/1/0] quit
   [*DeviceC] interface loopBack 1
   [*DeviceC-LoopBack1] isis ipv6 enable 100
   [*DeviceC-LoopBack1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 100
   [*DeviceD-isis-1] is-level level-2
   [*DeviceD-isis-1] cost-style wide
   [*DeviceD-isis-1] network-entity 20.0000.0000.0002.00
   [*DeviceD-isis-1] ipv6 enable topology ipv6
   [*DeviceD-isis-1] quit
   [*DeviceD] interface gigabitethernet 0/2/0
   [*DeviceD-GigabitEthernet0/2/0] isis ipv6 enable 100
   [*DeviceD-GigabitEthernet0/2/0] quit
   [*DeviceD] interface loopBack 1
   [*DeviceD-LoopBack1] isis ipv6 enable 100
   [*DeviceD-LoopBack1] quit
   [*DeviceD] commit
   ```
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. DeviceC is used as an example.
   
   ```
   [~DeviceC] display isis peer
   
                             Peer information for ISIS(100)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0            0000.0000.0002.02  Up   28s      L2       64
   
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. DeviceC is used as an example.
   
   ```
   [~DeviceC] display isis route
   
                           ISIS(100) Level-2 Forwarding Table
                           --------------------------------
   
    IPV6 Dest.     ExitInterface      NextHop                    Cost     Flags
   --------------------------------------------------------------------------------
   2001:db8:3::3/1 Loop1              Direct                     0        D/-/L/-
   28
   2001:db8:4::4/1 GE0/1/0            FE80::865B:12FF:FE75:E73D  10       A/-/-/-
   28
   2001:db8:11::/9 GE0/2/0            Direct                     10       D/-/L/-
   6
   2001:db8:22::/9 GE0/1/0            Direct                     10       D/-/L/-
   6
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Create a VPN instance and configure the IPv6 address family capability for it on DeviceC and DeviceD, and implement access of DeviceB to DeviceC and access of DeviceE to DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip vpn-instance vrftest
   [*DeviceC-vpn-instance-vrftest] ipv6-family
   [*DeviceC-vpn-instance-vrftest-af-ipv6] route-distinguisher 1:1
   [*DeviceC-vpn-instance-vrftest-af-ipv6] vpn-target 100:1 export-extcommunity
   [*DeviceC-vpn-instance-vrftest-af-ipv6] vpn-target 100:1 import-extcommunity
   [*DeviceC-vpn-instance-vrftest-af-ipv6] quit
   [*DeviceC-vpn-instance-vrftest] quit
   [*DeviceC] interface gigabitethernet 0/2/0
   [*DeviceC-GigabitEthernet0/2/0] ip binding vpn-instance vrftest
   [*DeviceC-GigabitEthernet0/2/0] quit 
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ip vpn-instance vrftest
   [*DeviceD-vpn-instance-vrftest] ipv6-family
   [*DeviceD-vpn-instance-vrftest-af-ipv6] route-distinguisher 1:1
   [*DeviceD-vpn-instance-vrftest-af-ipv6] vpn-target 100:1 export-extcommunity
   [*DeviceD-vpn-instance-vrftest-af-ipv6] vpn-target 100:1 import-extcommunity
   [*DeviceD-vpn-instance-vrftest-af-ipv6] quit
   [*DeviceD-vpn-instance-vrftest] quit
   [*DeviceD] interface gigabitethernet 0/1/0
   [*DeviceD-GigabitEthernet0/1/0] ip binding vpn-instance vrftest
   [*DeviceD-GigabitEthernet0/1/0] quit
   [*DeviceD] commit
   ```
4. Establish an IBGP peer relationship between DeviceC and DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 100
   [*DeviceC-bgp] router-id 2.22.2.2
   [*DeviceC-bgp] peer 2001:db8:4::4 as-number 100
   [*DeviceC-bgp] peer 2001:db8:4::4 connect-interface LoopBack1
   [*DeviceC-bgp] ipv6-family vpnv6 
   [*DeviceC-bgp-af-vpnv6] peer 2001:db8:4::4 enable
   [*DeviceC-bgp-af-vpnv6] quit
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 100
   [*DeviceD-bgp] router-id 3.33.3.3
   [*DeviceD-bgp] peer 2001:db8:3::3 as-number 100
   [*DeviceD-bgp] peer 2001:db8:3::3 connect-interface LoopBack1
   [*DeviceD-bgp] ipv6-family vpnv6 
   [*DeviceD-bgp-af-vpnv6] peer 2001:db8:3::3 enable
   [*DeviceD-bgp-af-vpnv6] quit
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
   
   After the configuration is complete, run the **display bgp vpnv6 all peer** command on DeviceC. The command output shows that the IBGP peer relationship between DeviceC and DeviceD is in Established state.
   
   ```
   [~DeviceC] display bgp vpnv6 all peer
   
    BGP local router ID : 2.22.2.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:db8:4::4                    4         100       37       40     0 00:29:43 Established        0
   ```
5. Establish an EBGP peer relationship between DeviceB and DeviceC and another one between DeviceD and DeviceE.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   [*DeviceB-bgp] router-id 1.11.1.1
   [*DeviceB-bgp] peer 2001:db8:11::2 as-number 100
   [*DeviceB-bgp] ipv6-family unicast
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:11::2 enable
   [*DeviceB-bgp-af-ipv6] network 2001:db8:2::2 128
   [*DeviceB-bgp-af-ipv6] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 100
   [*DeviceC-bgp] ipv6-family vpn-instance vrftest
   [*DeviceC-bgp-6-vrftest] peer 2001:db8:11::1 as-number 200
   [*DeviceC-bgp-6-vrftest] quit
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 100
   [*DeviceD-bgp] ipv6-family vpn-instance vrftest
   [*DeviceD-bgp-6-vrftest] peer 2001:db8:33::2 as-number 300
   [*DeviceD-bgp-6-vrftest] quit
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] bgp 300
   [*DeviceE-bgp] router-id 4.44.4.4
   [*DeviceE-bgp] peer 2001:db8:33::1 as-number 100
   [*DeviceE-bgp] ipv6-family unicast
   [*DeviceE-bgp-af-ipv6] peer 2001:db8:33::1 enable
   [*DeviceE-bgp-af-ipv6] network 2001:db8:5::5 128
   [*DeviceE-bgp-af-ipv6] quit
   [*DeviceE-bgp] quit
   [*DeviceE] commit
   ```
   
   After the configuration is complete, run the **display bgp vpnv6 vpn-instance peer** command to check whether a BGP peer relationship has been established between DeviceB and DeviceC, and between DeviceD and DeviceE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   DeviceC is used as an example.
   
   ```
   [~DeviceC] display bgp vpnv6 vpn-instance vrftest peer
   
    BGP local router ID : 2.22.2.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     VPN-Instance vrftest, Router ID 2.22.2.2:
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:db8:11::1                   4         200        7        5     0 00:02:29 Established       1
   ```
6. Configure SRv6 SIDs and configure VPN routes to carry the SID attribute on DeviceC and DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] segment-routing ipv6
   [*DeviceC-segment-routing-ipv6] encapsulation source-address 2001:db8:3::3
   [*DeviceC-segment-routing-ipv6] locator locator1 ipv6-prefix 2001:db8:333:: 64 static 32
   [*DeviceC-segment-routing-ipv6-locator] opcode 2001:db8:333::333 end psp
   [*DeviceC-segment-routing-ipv6-locator] quit
   [*DeviceC-segment-routing-ipv6] quit
   [*DeviceC] bgp 100
   [*DeviceC-bgp] ipv6-family vpnv6
   [*DeviceC-bgp-af-vpnv6] peer 2001:db8:4::4 prefix-sid
   [*DeviceC-bgp-af-vpnv6] quit
   [*DeviceC-bgp] ipv6-family vpn-instance vrftest
   [*DeviceC-bgp-6-vrftest] segment-routing ipv6 traffic-engineer best-effort
   [*DeviceC-bgp-6-vrftest] segment-routing ipv6 locator locator1
   [*DeviceC-bgp-6-vrftest] quit
   [*DeviceC-bgp] quit
   [*DeviceC] isis 100
   [*DeviceC-isis-100] segment-routing ipv6 locator locator1 auto-sid-disable
   [*DeviceC-isis-100] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] segment-routing ipv6
   [*DeviceD-segment-routing-ipv6] encapsulation source-address 2001:db8:4::4
   [*DeviceD-segment-routing-ipv6] locator locator1 ipv6-prefix 2001:db8:444:: 64 static 32
   [*DeviceD-segment-routing-ipv6-locator] opcode 2001:db8:444::444 end psp
   [*DeviceD-segment-routing-ipv6-locator] quit
   [*DeviceD-segment-routing-ipv6] quit
   [*DeviceD] bgp 100
   [*DeviceD-bgp] ipv6-family vpnv6
   [*DeviceD-bgp-af-vpnv6] peer 2001:db8:3::3 prefix-sid
   [*DeviceD-bgp-af-vpnv6] quit
   [*DeviceD-bgp] ipv6-family vpn-instance vrftest
   [*DeviceD-bgp-6-vrftest] segment-routing ipv6 traffic-engineer best-effort
   [*DeviceD-bgp-6-vrftest] segment-routing ipv6 locator locator1
   [*DeviceD-bgp-6-vrftest] quit
   [*DeviceD-bgp] quit
   [*DeviceD] isis 100
   [*DeviceD-isis-100] segment-routing ipv6 locator locator1 auto-sid-disable
   [*DeviceD-isis-100] quit
   [*DeviceD] commit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid+end+forwarding) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~DeviceC] display segment-routing ipv6 local-sid end forwarding
   
   
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:db8:333::333/128                        FuncType    : End
   Flavor      : PSP
   LocatorName : locator1                                     LocatorID   : 2
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-02-11 17:06:25.197
   
   Total SID(s): 1
   ```
   ```
   [~DeviceD] display segment-routing ipv6 local-sid end forwarding
   
   
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:db8:444::444/128                        FuncType    : End
   Flavor      : PSP
   LocatorName : locator1                                     LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2022-02-11 17:08:23.955
   
   Total SID(s): 1
   ```
7. Configure an SRv6 TE Policy.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] segment-routing ipv6
   [*DeviceC-segment-routing-ipv6] segment-list s1
   [*DeviceC-segment-routing-ipv6-segment-list-s1] index 5 sid ipv6 2001:db8:444::444
   [*DeviceC-segment-routing-ipv6-segment-list-s1] quit
   [*DeviceC-segment-routing-ipv6] srv6-te-policy locator locator1
   [*DeviceC-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:db8:4::4 color 200
   [*DeviceC-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*DeviceC-segment-routing-ipv6-policy-policy1-path] segment-list s1 
   [*DeviceC-segment-routing-ipv6-policy-policy1-path] quit
   [*DeviceC-segment-routing-ipv6-policy-policy1] quit
   [*DeviceC-segment-routing-ipv6] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] segment-routing ipv6
   [*DeviceD-segment-routing-ipv6] segment-list s1
   [*DeviceD-segment-routing-ipv6-segment-list-s1] index 5 sid ipv6 2001:db8:333::333
   [*DeviceD-segment-routing-ipv6-segment-list-s1] quit
   [*DeviceD-segment-routing-ipv6] srv6-te-policy locator locator1
   [*DeviceD-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:db8:3::3 color 200
   [*DeviceD-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*DeviceD-segment-routing-ipv6-policy-policy1-path] segment-list s1
   [*DeviceD-segment-routing-ipv6-policy-policy1-path] quit
   [*DeviceD-segment-routing-ipv6-policy-policy1] quit
   [*DeviceD-segment-routing-ipv6] quit
   [*DeviceD] commit
   ```
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   DeviceC is used as an example.
   
   ```
   [~DeviceC] display srv6-te policy
   PolicyName : policy1
   Color                   : 200                            Endpoint             : 2001:db8:4::4
   TunnelId                : 21                             
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -
   Policy State            : Up                             State Change Time    : 2022-02-11 17:09:59
   Admin State             : Up                             Traffic Statistics   : Disable
   Backup Hot-Standby      : Disable                        BFD                  : Disable
   Interface Index         : -                              Interface Name       : -
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : -
   Candidate-path Count    : 1
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0
    Discriminator          : 100                            Binding SID          : -
    GroupId                : 21                             Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable
    DelayTimerRemain       : -                              Network Slice ID     : -
    Segment-List Count     : 1
     Segment-List          : s1
      Segment-List ID      : 21                             XcIndex              : 21
      List State           : Up                             DelayTimerRemain     : -
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600
      Weight               : 1                              BFD State            : -
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding SID  : -
      SID :
            2001:db8:444::444
   ```
8. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] route-policy RP1 permit node 1
   [*DeviceC-route-policy] apply extcommunity color 0:200
   [*DeviceC-route-policy] quit
   [*DeviceC] bgp 100
   [*DeviceC-bgp] ipv6-family vpnv6
   [*DeviceC-bgp-af-vpnv6] peer 2001:db8:4::4 route-policy RP1 import      
   [*DeviceC-bgp-af-vpnv6] quit
   [*DeviceC-bgp] quit
   [*DeviceC] tunnel-policy tnl_policy
   [*DeviceC-tunnel-policy-tnl_policy] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*DeviceC-tunnel-policy-tnl_policy] quit
   [*DeviceC] ip vpn-instance vrftest
   [*DeviceC-vpn-instance-vrftest] ipv6-family
   [*DeviceC-vpn-instance-vrftest-af-ipv6] tnl-policy tnl_policy
   [*DeviceC-vpn-instance-vrftest-af-ipv6] commit
   [~DeviceC-vpn-instance-vrftest-af-ipv6] quit
   [~DeviceC-vpn-instance-vrftest] quit
   ```
   
   
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] route-policy RP1 permit node 1
   [*DeviceD-route-policy] apply extcommunity color 0:200        
   [*DeviceD-route-policy] quit
   [*DeviceD] bgp 100
   [*DeviceD-bgp] ipv6-family vpnv6
   [*DeviceD-bgp-af-vpnv6] peer 2001:db8:3::3 route-policy RP1 import 
   [*DeviceD-bgp-af-vpnv6] quit
   [*DeviceD-bgp] quit
   [*DeviceD] tunnel-policy tnl_policy
   [*DeviceD-tunnel-policy-tnl_policy] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*DeviceD-tunnel-policy-tnl_policy] quit
   [*DeviceD] ip vpn-instance vrftest
   [*DeviceD-vpn-instance-vrftest] ipv6-family
   [*DeviceD-vpn-instance-vrftest-af-ipv6] tnl-policy tnl_policy
   [*DeviceD-vpn-instance-vrftest-af-ipv6] commit
   [~DeviceD-vpn-instance-vrftest-af-ipv6] quit
   [~DeviceD-vpn-instance-vrftest] quit
   ```
   
   Check whether the loopback interfaces on DeviceB and DeviceE can ping each other.
   
   DeviceB is used as an example.
   
   ```
   <DeviceB>ping ipv6 -a 2001:db8:2::2  2001:db8:5::5
     PING 2001:db8:5::5 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:5::5
       bytes=56 Sequence=1 hop limit=62 time=12 ms
       Reply from 2001:db8:5::5
       bytes=56 Sequence=2 hop limit=62 time=2 ms
       Reply from 2001:db8:5::5
       bytes=56 Sequence=3 hop limit=62 time=2 ms
       Reply from 2001:db8:5::5
       bytes=56 Sequence=4 hop limit=62 time=2 ms
       Reply from 2001:db8:5::5
       bytes=56 Sequence=5 hop limit=62 time=2 ms
   
     --- 2001:db8:5::5 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=2/4/12 ms
   ```
   
   After the configuration is complete, run the **display ipv6 routing-table vpn-instance vrftest** command to check the routing table of the VPN instance. The command output shows that VPN routes have successfully recursed to the SRv6 TE Policy.
   
   DeviceC is used as an example.
   
   ```
   [~DeviceC] display ipv6 routing-table vpn-instance vrftest
   Routing Table : vrftest
            Destinations : 5        Routes : 5
   
   Destination  : 2001:db8:2::2                           PrefixLength : 128
   NextHop      : 2001:db8:11::1                          Preference   : 255
   Cost         : 0                                       Protocol     : EBGP
   RelayNextHop : 2001:db8:11::1                          TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : RD
   
   Destination  : 2001:db8:5::5                           PrefixLength : 128
   NextHop      : 2001:db8:4::4                           Preference   : 255
   Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::                                      TunnelID     : 0x000000003400000015
   Interface    : policy1                                 Flags        : RD
   
   Destination  : 2001:db8:11::                           PrefixLength : 96
   NextHop      : 2001:db8:11::2                          Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:db8:11::2                          PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : DB
   ```
   ```
   [~DeviceC] display ipv6 routing-table vpn-instance vrftest 2001:db8:5::5 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vrftest
   Summary Count : 1
   
   Destination  : 2001:db8:5::5                           PrefixLength : 128
   NextHop      : 2001:db8:4::4                           Preference   : 255
   Neighbour    : 2001:db8:4::4                           ProcessID    : 0
   Label        : 3                                       Protocol     : IBGP
   State        : Active Adv Relied                       Cost         : 0
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   Priority     : low                                     Age          : 224sec
   IndirectID   : 0x2000306                               Instance     :
   RelayNextHop : ::                                      TunnelID     : 0x000000003400000015
   Interface    : policy1                                 Flags        : RD
   RouteColor   : 0                                       QoSInfo      : 0x0
   ```
9. Establish an EBGP peer relationship between DeviceB and DeviceE.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   [*DeviceB-bgp] peer 2001:db8:5::5 as-number 300
   [*DeviceB-bgp] peer 2001:db8:5::5 ebgp-max-hop 255
   [*DeviceB-bgp] peer 2001:db8:5::5 connect-interface LoopBack1
   [*DeviceB-bgp] ipv6-family unicast
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:5::5 enable
   [*DeviceB-bgp-af-ipv6] network 2001:db8:1::1 128
   [*DeviceB-bgp-af-ipv6] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceE.
   
   ```
   [~DeviceE] bgp 300
   [*DeviceE-bgp] peer 2001:db8:2::2 as-number 200
   [*DeviceE-bgp] peer 2001:db8:2::2 ebgp-max-hop 255
   [*DeviceE-bgp] peer 2001:db8:2::2 connect-interface LoopBack1
   [*DeviceE-bgp] ipv6-family unicast 
   [*DeviceE-bgp-af-ipv6] peer 2001:db8:2::2 enable
   [*DeviceE-bgp-af-ipv6] quit
   [*DeviceE-bgp] quit
   [*DeviceE] commit
   ```
   
   After the configuration is complete, run the **display bgp ipv6 peer** command on DeviceB to check whether the EBGP peer relationship between DeviceB and DeviceE has been established. If the **Established** state is displayed in the command output, the EBGP peer relationship has been established successfully.
   
   DeviceB is used as an example.
   
   ```
   [~DeviceB] display bgp ipv6 peer
   
    BGP local router ID : 1.11.1.1
    Local AS number : 200
    Total number of peers : 2                 Peers in established state : 2
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:db8:5::5                    4         300        5        6     0 00:00:24 Established       1
     2001:db8:11::2                   4         100      106      107     0 01:28:52 Established        1
   ```
10. Create a VPN instance and configure the IPv6 address family capability for it on DeviceA and DeviceE.
    
    
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] ip vpn-instance vrf
    [*DeviceA-vpn-instance-vrf] ipv6-family
    [*DeviceA-vpn-instance-vrf-af-ipv6] route-distinguisher 1:21
    [*DeviceA-vpn-instance-vrf-af-ipv6] vpn-target 1:4 export-extcommunity
    [*DeviceA-vpn-instance-vrf-af-ipv6] vpn-target 1:4 import-extcommunity
    [*DeviceA-vpn-instance-vrf-af-ipv6] quit
    [*DeviceA-vpn-instance-vrf] quit
    [*DeviceA] interface loopBack 100
    [*DeviceA-LoopBack100] ip binding vpn-instance vrf
    [*DeviceA-LoopBack100] ipv6 enable
    [*DeviceA-LoopBack100] ipv6 address 2001:db8:16::1/128
    [*DeviceA-LoopBack100] quit 
    [*DeviceA] commit
    ```
    
    # Configure DeviceE.
    
    ```
    [~DeviceE] ip vpn-instance vrf
    [*DeviceE-vpn-instance-vrf] ipv6-family
    [*DeviceE-vpn-instance-vrf-af-ipv6] route-distinguisher 1:21
    [*DeviceE-vpn-instance-vrf-af-ipv6] vpn-target 1:4 export-extcommunity
    [*DeviceE-vpn-instance-vrf-af-ipv6] vpn-target 1:4 import-extcommunity
    [*DeviceE-vpn-instance-vrf-af-ipv6] quit
    [*DeviceE-vpn-instance-vrf] quit
    [*DeviceE] interface loopBack 100
    [*DeviceE-LoopBack100] ip binding vpn-instance vrf
    [*DeviceE-LoopBack100] ipv6 enable
    [*DeviceE-LoopBack100] ipv6 address 2001:db8:15::1/128
    [*DeviceE-LoopBack100] quit
    [*DeviceE] commit
    ```
11. Establish an EBGP peer relationship between DeviceA and DeviceE.
    
    
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] bgp 200
    [*DeviceA-bgp] router-id 5.55.5.5
    [*DeviceA-bgp] peer 2001:db8:5::5 as-number 300
    [*DeviceA-bgp] peer 2001:db8:5::5 ebgp-max-hop 255
    [*DeviceA-bgp] peer 2001:db8:5::5 connect-interface LoopBack1
    [*DeviceA-bgp] ipv6-family vpnv6
    [*DeviceA-bgp-af-vpnv6] peer 2001:db8:5::5 enable
    [*DeviceA-bgp-af-vpnv6] quit
    [*DeviceA-bgp] quit
    [*DeviceA] commit
    ```
    
    # Configure DeviceE.
    
    ```
    [~DeviceE] bgp 300
    [*DeviceE-bgp] peer 2001:db8:1::1 as-number 200
    [*DeviceE-bgp] peer 2001:db8:1::1 ebgp-max-hop 255
    [*DeviceE-bgp] peer 2001:db8:1::1 connect-interface LoopBack1
    [*DeviceE-bgp] ipv6-family vpnv6
    [*DeviceE-bgp-af-vpnv6] peer 2001:db8:1::1 enable
    [*DeviceE-bgp-af-vpnv6] quit
    [*DeviceE-bgp] quit
    [*DeviceE] commit
    ```
    
    After the configuration is complete, run the **display bgp vpnv6 all peer** command on DeviceA to check whether the EBGP peer relationship between DeviceA and DeviceE has been established. If the **Established** state is displayed in the command output, the EBGP peer relationship has been established successfully.
    
    DeviceA is used as an example.
    
    ```
    [~DeviceA] display bgp vpnv6 all peer
    
     BGP local router ID : 5.55.5.5
     Local AS number : 200
     Total number of peers : 1                 Peers in established state : 1
    
      Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
      2001:db8:5::5                    4         300        4        4     0 00:00:36 Established        1
    ```
12. Configure SRv6 SIDs and configure VPN routes to carry the SID attribute on DeviceA and DeviceE.
    
    
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] segment-routing ipv6
    [*DeviceA-segment-routing-ipv6] encapsulation source-address 2001:db8:1::1
    [*DeviceA-segment-routing-ipv6] locator locator1 ipv6-prefix 2001:db8:100:: 64 static 32
    [*DeviceA-segment-routing-ipv6-locator] opcode 2001:db8:100::111 end psp
    [*DeviceA-segment-routing-ipv6-locator] opcode 2001:db8:100:600 end-op
    [*DeviceA-segment-routing-ipv6-locator] quit
    [*DeviceA-segment-routing-ipv6] quit
    [*DeviceA] bgp 200
    [*DeviceA-bgp] ipv6-family vpnv6
    [*DeviceA-bgp-af-vpnv6] peer 2001:db8:5::5 prefix-sid
    [*DeviceA-bgp-af-vpnv6] quit
    [*DeviceA-bgp] ipv6-family vpn-instance vrf
    [*DeviceA-bgp-6-vrf] import-route direct
    [*DeviceA-bgp-6-vrf] segment-routing ipv6 traffic-engineer best-effort
    [*DeviceA-bgp-6-vrf] segment-routing ipv6 locator locator1
    [*DeviceA-bgp-6-vrf] quit
    [*DeviceA-bgp] quit
    [*DeviceA] isis 1
    [*DeviceA-isis-1] segment-routing ipv6 locator locator1 auto-sid-disable
    [*DeviceA-isis-1] quit
    [*DeviceA] commit
    ```
    
    # Configure DeviceB.
    
    ```
    [~DeviceB] segment-routing ipv6
    [*DeviceB-segment-routing-ipv6] encapsulation source-address 2001:db8:2::2
    [*DeviceB-segment-routing-ipv6] locator locator1 ipv6-prefix 2001:db8:200:: 64 static 32
    [*DeviceB-segment-routing-ipv6-locator] opcode 2001:db8:200::222 end psp
    [*DeviceB-segment-routing-ipv6-locator] quit
    [*DeviceB-segment-routing-ipv6] quit
    [*DeviceB] isis 1
    [*DeviceB-isis-1] segment-routing ipv6 locator locator1 auto-sid-disable
    [*DeviceB-isis-1] quit
    [*DeviceB] bgp 200
    [*DeviceB-bgp] ipv6-family unicast
    [*DeviceB-bgp-af-ipv6] network 2001:db8:100:: 64  
    [*DeviceB-bgp-af-ipv6] network 2001:db8:200:: 64  
    [*DeviceB-bgp-af-ipv6] quit
    [*DeviceB-bgp] quit
    [*DeviceB] commit
    ```
    
    # Configure DeviceE.
    
    ```
    [~DeviceE] segment-routing ipv6
    [*DeviceE-segment-routing-ipv6] encapsulation source-address 2001:db8:5::5
    [*DeviceE-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:555:: 64 static 32
    [*DeviceE-segment-routing-ipv6-locator] opcode 2001:db8:555::555 end psp
    [*DeviceE-segment-routing-ipv6-locator] opcode 2001:db8:555::500 end-op
    [*DeviceE-segment-routing-ipv6-locator] quit
    [*DeviceE-segment-routing-ipv6] quit
    [*DeviceE] bgp 300
    [*DeviceE-bgp] ipv6-family unicast 
    [*DeviceE-bgp-af-ipv6] network 2001:db8:555:: 64
    [*DeviceE-bgp-af-ipv6] ipv6-family vpnv6
    [*DeviceE-bgp-af-vpnv6] peer 2001:db8:1::1 prefix-sid
    [*DeviceE-bgp-af-vpnv6] quit
    [*DeviceE-bgp] ipv6-family vpn-instance vrf
    [*DeviceE-bgp-6-vpna] import-route direct
    [*DeviceE-bgp-6-vpna] segment-routing ipv6 traffic-engineer best-effort
    [*DeviceE-bgp-6-vpna] segment-routing ipv6 locator as1
    [*DeviceE-bgp-6-vpna] quit
    [*DeviceE-bgp] quit
    [*DeviceE] isis 2
    [*DeviceE-isis-2] segment-routing ipv6 locator as1 auto-sid-disable
    [*DeviceE-isis-2] quit
    [*DeviceE] commit
    ```
    
    Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid+end+forwarding) **end** **forwarding** command to check information about the SRv6 local SID table.
    
    ```
    [~DeviceB] display segment-routing ipv6 local-sid end forwarding
    
                        My Local-SID End Forwarding Table
                        ---------------------------------
    
    SID         : 2001:db8:200::222/128                        FuncType    : End
    Flavor      : PSP
    LocatorName : locator1                                     LocatorID   : 2
    ProtocolType: STATIC                                       ProcessID   : --
    UpdateTime  : 2022-02-11 18:03:00.703
    
    Total SID(s): 1
    ```
13. Configure the BGP EPE and virtual link functions on DeviceB and DeviceE.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    When configuring BGP EPE, you need to enable the BGP-LS address family. Otherwise, BGP EPE cannot take effect. Route advertisement is not recommended for the virtual link between DeviceB and DeviceE.
    
    # Configure DeviceB.
    
    ```
    [~DeviceB] route-policy rp deny node 10
    [*DeviceB-route-policy] quit
    [*DeviceB] commit
    [~DeviceB] bgp 200
    [*DeviceB-bgp] peer 2001:db8:5::5 egress-engineering srv6 locator locator1
    [*DeviceB-bgp] peer 2001:db8:5::5 virtual-link
    [*DeviceB-bgp] peer 2001:db8:5::5 virtual-link te metric 16777215
    [*DeviceB-bgp] peer 2001:db8:5::5 virtual-link te link administrative group ff
    [*DeviceB-bgp] peer 2001:db8:5::5 virtual-link te srlg 4294967295
    [*DeviceB-bgp] link-state-family unicast
    [*DeviceB-bgp-af-ls] quit
    [*DeviceB-bgp] ipv6-family unicast
    [*DeviceB-bgp-af-ipv6] peer 2001:db8:5::5 route-policy rp export
    [*DeviceB-bgp-af-ipv6] quit 
    [*DeviceB-bgp] quit
    [*DeviceB] commit
    ```
    
    # Configure DeviceE.
    
    ```
    [~DeviceE] route-policy rp deny node 10
    [*DeviceE-route-policy] quit
    [*DeviceE] commit
    [~DeviceE] bgp 300
    [*DeviceE-bgp] peer 2001:db8:2::2 egress-engineering srv6 locator as1
    [*DeviceE-bgp] peer 2001:db8:2::2 virtual-link
    [*DeviceE-bgp] peer 2001:db8:2::2 virtual-link te metric 16777215
    [*DeviceE-bgp] peer 2001:db8:2::2 virtual-link te link administrative group ff
    [*DeviceE-bgp] peer 2001:db8:2::2 virtual-link te srlg 4294967295
    [*DeviceE-bgp] link-state-family unicast
    [*DeviceE-bgp-af-ls] quit
    [*DeviceE-bgp] ipv6-family unicast
    [*DeviceE-bgp-af-ipv6] peer 2001:db8:2::2 route-policy rp export
    [*DeviceE-bgp-af-ipv6] quit 
    [*DeviceE-bgp] quit
    [*DeviceE] commit
    ```
    
    After the configuration is complete, run the **display bgp egress-engineering** command to check BGP EPE information. The command output shows SRv6 SID information.
    
    ```
    [~DeviceB] display bgp egress-engineering
    
     Peer Node                     : 2001:db8:5::5
     Peer Adj Num                  : 1
     Local ASN                     : 200
     Remote ASN                    : 300
     Local Router Id               : 1.11.1.1
     Remote Router Id              : 4.44.4.4
     Local Interface Address       : 2001:db8:2::2
     Remote Interface Address      : 2001:db8:5::5
     Usable Locator                : locator1
     SRv6 SID                      : 2001:db8:200::1:0:0
     SRv6 SID (PSP)                : 2001:db8:200::1:0:1
     SRv6 SID (PSP,USP,USD)        : 2001:db8:200::1:0:2
     SRv6 SID (PSP,USP,USD,COC)    : -(ONLY SUPPORT COMPRESS TYPE)
     Nexthop                       : 2001:db8:11::2
     Out Interface                 : GigabitEthernet0/1/0
    
     Peer Adj                      : 2001:db8:11::2
     Local ASN                     : 200
     Remote ASN                    : 300
     Local Router Id               : 1.11.1.1
     Remote Router Id              : 4.44.4.4
     Interface Identifier          : 24
     Local Interface Address       : 2001:db8:11::1
     Remote Interface Address      : 2001:db8:11::2
     Usable Locator                : locator1
     SRv6 SID                      : 2001:db8:200::1:0:3
     SRv6 SID (PSP)                : 2001:db8:200::1:0:4
     SRv6 SID (PSP,USP,USD)        : 2001:db8:200::1:0:5
     SRv6 SID (PSP,USP,USD,COC)    : -(ONLY SUPPORT COMPRESS TYPE)
     Nexthop                       : 2001:db8:11::2
     Out Interface                 : GigabitEthernet0/1/0
    ```
    ```
    [~DeviceE] display bgp egress-engineering
    
     Peer Node                     : 2001:db8:2::2
     Peer Adj Num                  : 1
     Local ASN                     : 300
     Remote ASN                    : 200
     Local Router Id               : 4.44.4.4
     Remote Router Id              : 1.11.1.1
     Local Interface Address       : 2001:db8:5::5
     Remote Interface Address      : 2001:db8:2::2
     Usable Locator                : as1
     SRv6 SID                      : 2001:db8:555::1:0:1
     SRv6 SID (PSP)                : 2001:db8:555::1:0:2
     SRv6 SID (PSP,USP,USD)        : 2001:db8:555::1:0:3
     SRv6 SID (PSP,USP,USD,COC)    : -(ONLY SUPPORT COMPRESS TYPE)
     Nexthop                       : 2001:db8:33::1
     Out Interface                 : GigabitEthernet0/2/0
    
     Peer Adj                      : 2001:db8:33::1
     Local ASN                     : 300
     Remote ASN                    : 200
     Local Router Id               : 4.44.4.4
     Remote Router Id              : 1.11.1.1
     Interface Identifier          : 17
     Local Interface Address       : 2001:db8:33::2
     Remote Interface Address      : 2001:db8:33::1
     Usable Locator                : as1
     SRv6 SID                      : 2001:db8:555::1:0:4
     SRv6 SID (PSP)                : 2001:db8:555::1:0:5
     SRv6 SID (PSP,USP,USD)        : 2001:db8:555::1:0:6
     SRv6 SID (PSP,USP,USD,COC)    : -(ONLY SUPPORT COMPRESS TYPE)
     Nexthop                       : 2001:db8:33::1
     Out Interface                 : GigabitEthernet0/2/0
    ```
14. Configure an SRv6 TE Policy.
    
    
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] segment-routing ipv6
    [*DeviceA-segment-routing-ipv6] segment-list list1
    [*DeviceA-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:db8:100::111
    [*DeviceA-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:db8:200::222
    [*DeviceA-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:db8:200::1:0:0
    [*DeviceA-segment-routing-ipv6-segment-list-list1] quit
    [*DeviceA-segment-routing-ipv6] srv6-te-policy locator locator1
    [*DeviceA-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:db8:5::5 color 100
    [*DeviceA-segment-routing-ipv6-policy-policy1] candidate-path preference 100
    [*DeviceA-segment-routing-ipv6-policy-policy1-path] segment-list list1
    [*DeviceA-segment-routing-ipv6-policy-policy1-path] quit
    [*DeviceA-segment-routing-ipv6-policy-policy1] quit
    [*DeviceA-segment-routing-ipv6] quit
    [*DeviceA] commit
    ```
    
    # Configure DeviceB.
    
    ```
    [~DeviceB] segment-routing ipv6
    [*DeviceB-segment-routing-ipv6] srv6-te-policy locator locator1
    [*DeviceB-segment-routing-ipv6] quit
    [*DeviceB] commit
    ```
    
    # Configure DeviceE.
    
    ```
    [~DeviceE] segment-routing ipv6
    [*DeviceE-segment-routing-ipv6] segment-list list1
    [*DeviceE-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:db8:555::1:0:1
    [*DeviceE-segment-routing-ipv6-segment-list-list1] index 15 sid ipv6 2001:db8:200::222
    [*DeviceE-segment-routing-ipv6-segment-list-list1] index 20 sid ipv6 2001:db8:100::111
    [*DeviceE-segment-routing-ipv6-segment-list-list1] quit
    [*DeviceE-segment-routing-ipv6] srv6-te-policy locator as1
    [*DeviceE-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:db8:1::1 color 100
    [*DeviceE-segment-routing-ipv6-policy-policy1] candidate-path preference 100
    [*DeviceE-segment-routing-ipv6-policy-policy1-path] segment-list list1 
    [*DeviceE-segment-routing-ipv6-policy-policy1-path] quit
    [*DeviceE-segment-routing-ipv6-policy-policy1] quit
    [*DeviceE-segment-routing-ipv6] quit
    [*DeviceE] commit
    ```
    
    After the configuration is complete, run the **ping srv6-te policy** command to check the connectivity of the SRv6 TE Policy.
    
    ```
    <DeviceA>ping srv6-te policy policy-name policy1 end-op 2001:db8:555::500
      PING srv6-te policy : 100  data bytes, press CTRL_C to break
      srv6-te policy's segment list:
      Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 129; Xcindex: 129; end-op: 2001:db8:555::500
        Reply from 2001:db8:555::500
        bytes=100 Sequence=1 time=1 ms
        Reply from 2001:db8:555::500
        bytes=100 Sequence=2 time=1 ms
        Reply from 2001:db8:555::500
        bytes=100 Sequence=3 time=1 ms
        Reply from 2001:db8:555::500
        bytes=100 Sequence=4 time=1 ms
        Reply from 2001:db8:555::500
        bytes=100 Sequence=5 time=1 ms
    
      --- srv6-te policy ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 1/1/1 ms
    ```
    
    After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
    
    DeviceA is used as an example.
    
    ```
    [~DeviceA] display srv6-te policy
    PolicyName : policy1
    Color                   : 100                            Endpoint             : 2001:db8:5::5
    TunnelId                : 65                             
    TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -
    Policy State            : Up                             State Change Time    : 2022-02-11 18:15:17
    Admin State             : Up                             Traffic Statistics   : Disable
    Backup Hot-Standby      : Disable                        BFD                  : Disable
    Interface Index         : -                              Interface Name       : -
    Interface State         : -                              Encapsulation Mode   : Insert
    Binding SID             : -
    Candidate-path Count    : 1
    
     Candidate-path Preference : 100
     Path State             : Active                         Path Type            : Primary
     Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0
     Discriminator          : 100                            Binding SID          : -
     GroupId                : 65                             Policy Name          : policy1
     Template ID            : 0                              Path Verification    : Disable
     DelayTimerRemain       : -                              Network Slice ID     : -
     Segment-List Count     : 1
      Segment-List          : list1
       Segment-List ID      : 129                            XcIndex              : 129
       List State           : Up                             DelayTimerRemain     : -
       Verification State   : -                              SuppressTimeRemain   : -
       PMTU                 : 9600                           Active PMTU          : 9600
       Weight               : 1                              BFD State            : -
       Network Slice ID     : -
       Binding SID          : -
       Reverse Binding SID  : -
       SID :
             2001:db8:100::111
             2001:db8:200::222
             2001:db8:200::1:0:0
    ```
15. Configure a tunnel policy to import VPN traffic.
    
    
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] route-policy RP1 permit node 1
    [*DeviceA-route-policy] apply extcommunity color 0:100
    [*DeviceA-route-policy] quit
    [*DeviceA] bgp 200
    [*DeviceA-bgp] ipv6-family vpnv6
    [*DeviceA-bgp-af-vpnv6] peer 2001:db8:5::5 route-policy RP1 import
    [*DeviceA-bgp-af-vpnv6] quit
    [*DeviceA-bgp] quit
    [*DeviceA] tunnel-policy tnl_policy
    [*DeviceA-tunnel-policy-tnl_policy] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
    [*DeviceA-tunnel-policy-tnl_policy] quit
    [*DeviceA] ip vpn-instance vrf
    [*DeviceA-vpn-instance-vrf] ipv6-family
    [*DeviceA-vpn-instance-vrf-af-ipv6] tnl-policy tnl_policy
    [*DeviceA-vpn-instance-vrf-af-ipv6] commit
    [~DeviceA-vpn-instance-vrf-af-ipv6] quit
    [~DeviceA-vpn-instance-vrf] quit
    ```
    
    
    
    # Configure DeviceE.
    
    ```
    [~DeviceE] route-policy RP1 permit node 1
    [*DeviceE-route-policy] apply extcommunity color 0:100
    [*DeviceE-route-policy] quit
    [*DeviceE] bgp 300
    [*DeviceE-bgp] ipv6-family vpnv6
    [*DeviceE-bgp-af-vpnv6] peer 2001:db8:1::1 route-policy RP1 import 
    [*DeviceE-bgp-af-vpnv6] quit
    [*DeviceE-bgp] quit
    [*DeviceE] tunnel-policy tnl_policy
    [*DeviceE-tunnel-policy-tnl_policy] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
    [*DeviceE-tunnel-policy-tnl_policy] quit
    [*DeviceE] ip vpn-instance vrf
    [*DeviceE-vpn-instance-vrf] ipv6-family
    [*DeviceE-vpn-instance-vrf-af-ipv6] tnl-policy tnl_policy
    [*DeviceE-vpn-instance-vrf-af-ipv6] commit
    [~DeviceE-vpn-instance-vrf-af-ipv6] quit
    [~DeviceE-vpn-instance-vrf] quit
    ```
    
    After the configuration is complete, run the **display ipv6 routing-table vpn-instance vrf** command to check the routing table of the VPN instance. The command output shows that VPN routes have successfully recursed to the SRv6 TE Policy.
    
    DeviceA is used as an example.
    
    ```
    [~DeviceA] display ipv6 routing-table vpn-instance vrf
    Routing Table : vrf
             Destinations : 3        Routes : 3
    
    Destination  : 2001:db8:15::1                          PrefixLength : 128
    NextHop      : 2001:db8:5::5                           Preference   : 255
    Cost         : 0                                       Protocol     : EBGP
    RelayNextHop : ::                                      TunnelID     : 0x000000003400000041
    Interface    : policy1                                Flags        : RD
    
    Destination  : 2001:db8:16::1                          PrefixLength : 128
    NextHop      : 2001:db8:11::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : LoopBack100                             Flags        : D
    
    Destination  : FE80::                                  PrefixLength : 10
    NextHop      : ::                                      Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : NULL0                                   Flags        : DB
    ```
    ```
    [~DeviceA] display ipv6 routing-table vpn-instance vrf 2001:db8:15::1 verbose
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vrf
    Summary Count : 1
    
    Destination  : 2001:db8:15::1                          PrefixLength : 128
    NextHop      : 2001:db8:5::5                           Preference   : 255
    Neighbour    : 2001:db8:5::5                           ProcessID    : 0
    Label        : 3                                       Protocol     : EBGP
    State        : Active Adv Relied                       Cost         : 0
    Entry ID     : 0                                       EntryFlags   : 0x00000000
    Reference Cnt: 0                                       Tag          : 0
    Priority     : low                                     Age          : 117sec
    IndirectID   : 0x100049D                               Instance     :
    RelayNextHop : ::                                      TunnelID     : 0x000000003400000041
    Interface    : policy1                                Flags        : RD
    RouteColor   : 0                                       QoSInfo      : 0x0
    ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
  sysname DeviceA
  #
  ip vpn-instance vrf
   ipv6-family                        
    route-distinguisher 1:21           
    tnl-policy tnl_policy
    apply-label per-instance        
    vpn-target 1:4 export-extcommunity
    vpn-target 1:4 import-extcommunity
  #
  segment-routing ipv6        
   encapsulation source-address 2001:db8:1::1
   locator locator1 ipv6-prefix 2001:db8:100:: 64 static 32     
    opcode 2001:db8:100::111 end psp                  
    opcode 2001:db8:100:600 end-op                   
   srv6-te-policy locator locator1             
   segment-list list1                          
    index 5 sid ipv6 2001:db8:100::111         
    index 10 sid ipv6 2001:db8:200::222        
    index 15 sid ipv6 2001:db8:200::1:0:0     
   srv6-te policy policy1 endpoint 2001:db8:5::5 color 100
    candidate-path preference 100     
     segment-list list1                  
  #
  isis 1                      
   is-level level-1     
   cost-style wide        
   network-entity 10.0000.0000.0001.00    
   #
   ipv6 enable topology ipv6        
   segment-routing ipv6 locator locator1 auto-sid-disable     
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:44::1/96
   isis ipv6 enable 1           
   undo dcn
  #
  interface LoopBack 1
   ipv6 enable                         
   ipv6 address 2001:db8:1::1/128
   isis ipv6 enable 1                  
  #
  interface LoopBack100            
   ip binding vpn-instance vrf
   ipv6 enable                      
   ipv6 address 2001:db8:16::1/128
  #
  bgp 200                   
   router-id 5.55.5.5
   private-4-byte-as enable
   peer 2001:db8:5::5 as-number 300
   peer 2001:db8:5::5 ebgp-max-hop 255
   peer 2001:db8:5::5 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv6-family vpnv6            
    policy vpn-target
    peer 2001:db8:5::5 enable
    peer 2001:db8:5::5 route-policy RP1 import
    peer 2001:db8:5::5 prefix-sid
   #
   ipv6-family vpn-instance vrf
    import-route direct                        
    segment-routing ipv6 locator locator1      
    segment-routing ipv6 traffic-engineer best-effort      
  # 
  route-policy RP1 permit node 1
   apply extcommunity color 0:100      
  #
  tunnel-policy tnl_policy 
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1  
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  segment-routing ipv6
   encapsulation source-address 2001:db8:2::2
   locator locator1 ipv6-prefix 2001:db8:200:: 64 static 32
    opcode 2001:db8:200::222 end psp
   srv6-te-policy locator locator1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator locator1 auto-sid-disable
   ipv6 import-route bgp level-1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:11::1/96
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:44::2/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:2::2/128
  #
  bgp 200
   router-id 1.11.1.1
   private-4-byte-as enable
   peer 2001:db8:5::5 as-number 300
   peer 2001:db8:5::5 ebgp-max-hop 255
   peer 2001:db8:5::5 connect-interface LoopBack1 
   peer 2001:db8:5::5 egress-engineering srv6 locator locator1
   peer 2001:db8:5::5 virtual-link
   peer 2001:db8:5::5 virtual-link te metric 16777215
   peer 2001:db8:5::5 virtual-link te link administrative group ff
   peer 2001:db8:5::5 virtual-link te srlg 4294967295
   peer 2001:db8:11::2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
   #
   link-state-family unicast
   #
   ipv6-family unicast
    undo synchronization
    network 2001:db8:1::1 128
    network 2001:db8:2::2 128
    network 2001:db8:100:: 64
    network 2001:db8:200:: 64
    peer 2001:db8:5::5 enable
    peer 2001:db8:5::5 route-policy rp export
    peer 2001:db8:11::2 enable
  #
  route-policy rp deny node 10
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  ip vpn-instance vrftest
   ipv6-family
    route-distinguisher 1:1
    tnl-policy tnl_policy
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
  #
  segment-routing ipv6
   encapsulation source-address 2001:db8:3::3
   locator locator1 ipv6-prefix 2001:db8:333:: 64 static 32
    opcode 2001:db8:333::333 end psp
   srv6-te-policy locator locator1
   segment-list s1                         
    index 5 sid ipv6 2001:db8:444::444
   srv6-te policy policy1 endpoint 2001:db8:4::4 color 200
    candidate-path preference 100    
     segment-list s1 
  #
  isis 100
   is-level level-2
   cost-style wide
   network-entity 20.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator locator1 auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:22::1/96
   isis ipv6 enable 100
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vrftest
   ipv6 enable
   ipv6 address 2001:db8:11::2/96
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:3::3/128
   isis ipv6 enable 100
  #
  bgp 100
   router-id 2.22.2.2
   private-4-byte-as enable
   peer 2001:db8:4::4 as-number 100
   peer 2001:db8:4::4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv6-family unicast
    undo synchronization
   #
   ipv6-family vpnv6                     
    policy vpn-target
    peer 2001:db8:4::4 enable
    peer 2001:db8:4::4 route-policy RP1 import
    peer 2001:db8:4::4 prefix-sid
   # 
   ipv6-family vpn-instance vrftest               
    segment-routing ipv6 locator locator1             
    segment-routing ipv6 traffic-engineer best-effort      
    peer 2001:db8:11::1 as-number 200
  #
  route-policy RP1 permit node 1      
   apply extcommunity color 0:200
  #
  tunnel-policy tnl_policy     
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  ip vpn-instance vrftest
   ipv6-family
    route-distinguisher 1:1
    tnl-policy tnl_policy
    apply-label per-instance
    vpn-target 100:1 export-extcommunity
    vpn-target 100:1 import-extcommunity
  #
  segment-routing ipv6
   encapsulation source-address 2001:db8:4::4
   locator locator1 ipv6-prefix 2001:db8:444:: 64 static 32
    opcode 2001:db8:444::444 end psp
   srv6-te-policy locator locator1
   segment-list s1         
    index 5 sid ipv6 2001:db8:333::333
   srv6-te policy policy1 endpoint 2001:db8:3::3 color 200
    candidate-path preference 100
     segment-list s1 
  #
  isis 100
   is-level level-2
   cost-style wide
   network-entity 20.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator locator1 auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vrftest
   ipv6 enable
   ipv6 address 2001:db8:33::1/96
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:22::2/96
   isis ipv6 enable 100
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:4::4/128
   isis ipv6 enable 100
  #
  bgp 100
   router-id 3.33.3.3
   private-4-byte-as enable
   peer 2001:db8:3::3 as-number 100
   peer 2001:db8:3::3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv6-family unicast
    undo synchronization
   #
   ipv6-family vpnv6                       
    policy vpn-target
    peer 2001:db8:3::3 enable
    peer 2001:db8:3::3 route-policy RP1 import 
    peer 2001:db8:3::3 prefix-sid
   #
   ipv6-family vpn-instance vrftest
    segment-routing ipv6 locator locator1              
    segment-routing ipv6 traffic-engineer best-effort  
    peer 2001:db8:33::2 as-number 300
  #
  route-policy RP1 permit node 1
   apply extcommunity color 0:200
  #
  tunnel-policy tnl_policy
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  return
  ```
* DeviceE configuration file
  
  ```
  #
  sysname DeviceE
  #
  ip vpn-instance vrf
   ipv6-family
    route-distinguisher 1:21
    tnl-policy tnl_policy
    apply-label per-instance
    vpn-target 1:4 export-extcommunity
    vpn-target 1:4 import-extcommunity
  #
  segment-routing ipv6
   encapsulation source-address 2001:db8:5::5
   locator as1 ipv6-prefix 2001:db8:555:: 64 static 32
    opcode 2001:db8:555::555 end psp         
    opcode 2001:db8:555::500 end-op          
   srv6-te-policy locator as1
   segment-list list1
    index 10 sid ipv6 2001:db8:555::1:0:1    
    index 15 sid ipv6 2001:db8:200::222    
    index 20 sid ipv6 2001:db8:100::111    
   srv6-te policy policy1 endpoint 2001:db8:1::1 color 100
    candidate-path preference 100     
     segment-list list1   
  #
  isis 2
   #
   segment-routing ipv6 locator as1 auto-sid-disable
   #
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:33::2/96
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:5::5/128
  #
  interface LoopBack100               
   ip binding vpn-instance vrf
   ipv6 enable                        
   ipv6 address 2001:db8:15::1/128
  #
  bgp 300
   router-id 4.44.4.4
   private-4-byte-as enable
   peer 2001:db8:1::1 as-number 200
   peer 2001:db8:1::1 ebgp-max-hop 255
   peer 2001:db8:1::1 connect-interface LoopBack1
   peer 2001:db8:2::2 as-number 200
   peer 2001:db8:2::2 ebgp-max-hop 255  
   peer 2001:db8:2::2 connect-interface LoopBack1
   peer 2001:db8:2::2 egress-engineering srv6 locator as1
   peer 2001:db8:2::2 virtual-link
   peer 2001:db8:2::2 virtual-link te metric 16777215
   peer 2001:db8:2::2 virtual-link te link administrative group ff
   peer 2001:db8:2::2 virtual-link te srlg 4294967295
   peer 2001:db8:33::1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
   #
   link-state-family unicast
   #
   ipv6-family unicast
    undo synchronization
    network 2001:db8:5::5 128
    network 2001:db8:555:: 64          
    peer 2001:db8:2::2 enable
    peer 2001:db8:2::2 route-policy rp export
    peer 2001:db8:33::1 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 2001:db8:1::1 enable
    peer 2001:db8:1::1 route-policy RP1 import 
    peer 2001:db8:1::1 prefix-sid
   #
   ipv6-family vpn-instance vrf
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
  #
  route-policy RP1 permit node 1
   apply extcommunity color 0:100         
  #
  route-policy rp deny node 10      
  #
  tunnel-policy tnl_policy                   
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1 
  #
  return
  ```