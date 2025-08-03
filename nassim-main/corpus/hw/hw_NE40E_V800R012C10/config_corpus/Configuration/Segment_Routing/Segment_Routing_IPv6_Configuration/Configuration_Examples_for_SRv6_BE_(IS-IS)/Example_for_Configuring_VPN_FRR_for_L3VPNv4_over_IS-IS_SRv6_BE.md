Example for Configuring VPN FRR for L3VPNv4 over IS-IS SRv6 BE
==============================================================

This section provides an example for configuring VPN FRR for L3VPNv4 over SRv6 BE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0193356407__fig_dc_vrp_srv6_cfg_all_001101):

* PE1, PE2, and PE3 are in the same AS and run IS-IS to implement IPv6 network connectivity.
* The PEs are Level-2 devices that belong to IS-IS process 1.

It is required that a bidirectional SRv6 BE path be deployed between PE1 and PE2 as well as between PE1 and PE3 to carry L3VPNv4 services. In addition, VPN FRR needs to be configured on PE1 to improve network reliability.

**Figure 1** Networking of VPN FRR configuration for L3VPNv4 over SRv6 BE![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0193367372.png)

#### Precautions

During the configuration process, note the following:

* In a VPN FRR scenario, after the primary path recovers, traffic switches back to this path. Because the order in which nodes undergo IGP convergence differs, packet loss may occur during the switchback. To resolve this problem, run the [**route-select delay**](cmdqueryname=route-select+delay) *delay-value* command to configure a route selection delay so that traffic is switched back only after forwarding entries on the devices along the primary path are updated. The delay specified using *delay-value* depends on various factors, such as the number of routes on the devices. Set a proper delay as needed.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each PE interface.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on each PE.
3. Configure a VPN instance on each PE.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish an MP-IBGP peer relationship between PEs.
6. Configure SRv6 on each PE, and enable IS-IS SRv6.
7. Enable VPN FRR on PE1 and configure BFD to detect locator route reachability to speed up VPN FRR switching.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each PE interface
* IS-IS process ID of each PE
* IS-IS level of each PE
* VPN instance name, RD, and RT on each PE

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following example uses the configuration of PE1. The configurations of other devices are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0193356407__section_dc_vrp_srv6_cfg_all_001105) in this section.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:db8:3::1 96
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:db8:11::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
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
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface loopback1
   [*PE1-LoopBack1] isis ipv6 enable 1
   [*PE1-LoopBack1] commit
   [~PE1-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   [*PE2-isis-1] is-level level-2
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0002.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] isis 1
   [*PE3-isis-1] is-level level-2
   [*PE3-isis-1] cost-style wide
   [*PE3-isis-1] network-entity 10.0000.0000.0004.00
   [*PE3-isis-1] ipv6 enable topology ipv6
   [*PE3-isis-1] quit
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE3-GigabitEthernet0/1/0] quit
   [*PE3] interface loopback1
   [*PE3-LoopBack1] isis ipv6 enable 1
   [*PE3-LoopBack1] commit
   [~PE3-LoopBack1] quit
   ```
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0004* GE0/2/0            0000.0000.0004.02  Up   7s       L2       64 
   0000.0000.0002* GE0/1/0            0000.0000.0002.02  Up   9s       L2       64 
   
   Total Peer(s): 2
   ```
   
   # Display IS-IS routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis route
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
   
    IPV6 Dest.         ExitInterface      NextHop                    Cost     Flags    
   --------------------------------------------------------------------------------
   2001:DB8:11::/128   Loop1              Direct                     0        D/-/L/-  
   2001:DB8:12::/128   GE0/1/0            FE80::3A92:6CFF:FE31:307   10       A/-/-/-  
   2001:DB8:13::/128   GE0/2/0            FE80::3A92:6CFF:FE41:305   10       A/-/-/-  
   2001:DB8:1::/96     GE0/1/0            Direct                     10       D/-/L/-  
   2001:DB8:3::/96     GE0/2/0            Direct                     10       D/-/L/-  
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the interface that connects a PE to a CE to the VPN instance on that PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   [*PE1-vpn-instance-vpna] quit
   [*PE1] interface gigabitethernet 0/3/0 
   [*PE1-GigabitEthernet0/3/0] ip binding vpn-instance vpna
   [*PE1-GigabitEthernet0/3/0] ip address 10.1.1.1 24
   [*PE1-GigabitEthernet0/3/0] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   [*PE2-vpn-instance-vpna] quit
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance vpna
   [*PE3-vpn-instance-vpna] ipv4-family
   [*PE3-vpn-instance-vpna-af-ipv4] route-distinguisher 300:1
   [*PE3-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*PE3-vpn-instance-vpna-af-ipv4] quit
   [*PE3-vpn-instance-vpna] quit
   [*PE3] interface gigabitethernet 0/2/0
   [*PE3-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*PE3-GigabitEthernet0/2/0] ip address 10.3.1.1 24
   [*PE3-GigabitEthernet0/2/0] quit
   [*PE3] commit
   ```
   
   # Configure an IP address for each interface on the CEs, as shown in [Figure 1](#EN-US_TASK_0193356407__fig_dc_vrp_srv6_cfg_all_001101). For configuration details, see [Configuration Files](#EN-US_TASK_0193356407__section_dc_vrp_srv6_cfg_all_001105) in this section.
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on the PEs to check VPN instance configurations. The command output shows that each PE can successfully ping its connected CE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a PE has multiple interfaces bound to the same VPN instance, use the **-a** *source-ip-address* parameter to specify a source IP address when running the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation may fail.
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   [*CE1-LoopBack1] quit
   [*CE1] bgp 65410
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   [*CE1-bgp] network 11.11.11.11 32
   [*CE1-bgp] quit
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] peer 10.1.1.2 as-number 65410
   [*PE1-bgp-vpna] import-route direct
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   [*CE2-LoopBack1] quit
   [*CE2] bgp 65420
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   [*CE2-bgp] peer 10.3.1.1 as-number 100
   [*CE2-bgp] network 22.22.22.22 32
   [*CE2-bgp] quit
   [*CE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [*PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] peer 10.2.1.2 as-number 65420
   [*PE2-bgp-vpna] import-route direct
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [*PE3-bgp] router-id 3.3.3.3
   [*PE3-bgp] ipv4-family vpn-instance vpna
   [*PE3-bgp-vpna] peer 10.3.1.2 as-number 65420
   [*PE3-bgp-vpna] import-route direct
   [*PE3-bgp-vpna] commit
   [~PE3-bgp-vpna] quit
   [~PE3-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on the PEs and check whether BGP peer relationships have been established between the PEs and CEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
   ```
   ```
    BGP local router ID : 1.1.1.1
    Local AS number : 100
   
    VPN-Instance vpna, Router ID 1.1.1.1:
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.2        4       65410     1695     1704     0 24:37:20 Established        1
   ```
5. Establish an MP-IBGP peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [~PE1-bgp] peer 2001:DB8:12::2 as-number 100
   [*PE1-bgp] peer 2001:DB8:12::2 connect-interface loopback 1
   [*PE1-bgp] peer 2001:DB8:13::3 as-number 100
   [*PE1-bgp] peer 2001:DB8:13::3 connect-interface loopback 1
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:12::2 enable
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:13::3 enable
   [*PE1-bgp-af-vpnv4] commit
   [~PE1-bgp-af-vpnv4] quit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [~PE2-bgp] peer 2001:DB8:11::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:11::1 connect-interface loopback 1
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:11::1 enable
   [*PE2-bgp-af-vpnv4] commit
   [~PE2-bgp-af-vpnv4] quit
   [~PE2-bgp] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   [~PE3-bgp] peer 2001:DB8:11::1 as-number 100
   [*PE3-bgp] peer 2001:DB8:11::1 connect-interface loopback 1
   [*PE3-bgp] ipv4-family vpnv4
   [*PE3-bgp-af-vpnv4] peer 2001:DB8:11::1 enable
   [*PE3-bgp-af-vpnv4] commit
   [~PE3-bgp-af-vpnv4] quit
   [~PE3-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on the PEs and check whether BGP peer relationships have been established between the PEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
6. Establish an SRv6 BE path between PEs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An End.DT4 SID can be either dynamically allocated through BGP or manually configured. If a dynamically allocated SID and a manually configured SID both exist, the latter takes effect. If you want to run the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* command to enable dynamic End.DT4 SID allocation through BGP or the [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator) *locator-name* [**end-dt46**](cmdqueryname=end-dt46) command to enable dynamic End.DT46 SID allocation through BGP in the future, you do not need to run the **opcode** *func-opcode* **end-dt4** **vpn-instance** *vpn-instance-name* or **opcode** *func-opcode* **end-dt46** **vpn-instance** *vpn-instance-name* command to configure an opcode for static SIDs.
   
   In this example, SIDs are dynamically allocated through BGP.
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:11::1
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:12::2 prefix-sid
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:13::3 prefix-sid
   [*PE1-bgp-af-vpnv4] quit
   [*PE1-bgp] ipv4-family vpn-instance vpna
   [*PE1-bgp-vpna] segment-routing ipv6 best-effort
   [*PE1-bgp-vpna] segment-routing ipv6 locator as1
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   [~PE1] isis 1
   [~PE1-isis-1] segment-routing ipv6 locator as1
   [*PE1-isis-1] commit
   [~PE1-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:12::2
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] bgp 100
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:11::1 prefix-sid
   [*PE2-bgp-af-vpnv4] quit
   [*PE2-bgp] ipv4-family vpn-instance vpna
   [*PE2-bgp-vpna] segment-routing ipv6 best-effort
   [*PE2-bgp-vpna] segment-routing ipv6 locator as1
   [*PE2-bgp-vpna] commit
   [~PE2-bgp-vpna] quit
   [~PE2-bgp] quit
   [~PE2] isis 1
   [~PE2-isis-1] segment-routing ipv6 locator as1
   [*PE2-isis-1] commit
   [~PE2-isis-1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   [*PE3-segment-routing-ipv6] encapsulation source-address 2001:DB8:13::3
   [*PE3-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
   [*PE3-segment-routing-ipv6-locator] quit
   [*PE3-segment-routing-ipv6] quit
   [*PE3] bgp 100
   [*PE3-bgp] ipv4-family vpnv4
   [*PE3-bgp-af-vpnv4] peer 2001:DB8:11::1 prefix-sid
   [*PE3-bgp-af-vpnv4] quit
   [*PE3-bgp] ipv4-family vpn-instance vpna
   [*PE3-bgp-vpna] segment-routing ipv6 best-effort
   [*PE3-bgp-vpna] segment-routing ipv6 locator as1
   [*PE3-bgp-vpna] commit
   [~PE3-bgp-vpna] quit
   [~PE3-bgp] quit
   [~PE3] isis 1
   [~PE3-isis-1] segment-routing ipv6 locator as1
   [*PE3-isis-1] commit
   [~PE3-isis-1] quit
   ```
7. Configure VPN FRR.
   
   
   
   Configure VPN FRR and use BFD to detect locator route reachability. If the locator route is unreachable, VPN FRR is performed, triggering traffic switching.
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   [~PE1-vpn-instance-vpna] ipv4-family
   [~PE1-vpn-instance-vpna-af-ipv4] vpn frr
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   [~PE1-vpn-instance-vpna] quit
   [~PE1] bgp 100
   [~PE1-bgp] ipv4-family vpn-instance vpna
   [~PE1-bgp-vpna] route-select delay 300
   [*PE1-bgp-vpna] commit
   [~PE1-bgp-vpna] quit
   [~PE1-bgp] quit
   [~PE1] bfd
   [*PE1-bfd] quit
   [*PE1] bfd pe1tope2 bind peer-ipv6 2001:DB8:20::
   [*PE1-bfd-session-pe1tope2] discriminator local 100
   [*PE1-bfd-session-pe1tope2] discriminator remote 200
   [*PE1-bfd-session-pe1tope2] commit
   [~PE1-bfd-session-pe1tope2] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   [*PE2-bfd] quit
   [*PE2] bfd pe2tope1 bind peer-ipv6 2001:DB8:10::
   [*PE2-bfd-session-pe2tope1] discriminator local 200
   [*PE2-bfd-session-pe2tope1] discriminator remote 100
   [*PE2-bfd-session-pe2tope1] commit
   [~PE2-bfd-session-pe2tope1] quit
   ```
8. Verify the configuration.
   
   
   
   Run the [**display ip routing-table vpn-instance vpna**](cmdqueryname=display+ip+routing-table+vpn-instance+vpna) *ip-address* **verbose** command to check VPN routing information. The following example uses the command output on PE1.
   
   ```
   [~PE1]display ip routing-table vpn-instance vpna 22.22.22.22 32 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
   Summary Count : 1
   
   Destination: 22.22.22.22/32
        Protocol: IBGP               Process ID: 0
      Preference: 255                      Cost: 0
         NextHop: 2001:DB8:20::1:0:3F Neighbour: 2001:DB8:12::2
           State: Active Adv Relied         Age: 00h00m11s
             Tag: 0                    Priority: low
           Label: 3                     QoSInfo: 0x0
      IndirectID: 0x100010C            Instance:
    RelayNextHop: FE80::3A00:10FF:FE03:5 Interface: GigabitEthernet0/1/0
        TunnelID: 0x0                     Flags: RD
      RouteColor: 0
       BkNextHop: 2001:DB8:30::1:0:3F BkInterface: GigabitEthernet0/2/0
         BkLabel: 3                 SecTunnelID: 0x0
    BkPETunnelID: 0x0           BkPESecTunnelID: 0x0
    BkIndirectID: 0x100010E
   
   ```
   
   The preceding command output shows that the VPN route 22.22.22.22/32 has a backup outbound interface and a VPN FRR routing entry has been generated.
   
   Check that CEs belonging to the same VPN instance can ping each other. The following example uses the command output on CE1.
   
   ```
   [~CE1] ping -a 11.11.11.11 22.22.22.22
     PING 22.22.22.22: 56  data bytes, press CTRL_C to break
       Reply from 22.22.22.22: bytes=56 Sequence=1 ttl=253 time=7 ms
       Reply from 22.22.22.22: bytes=56 Sequence=2 ttl=253 time=5 ms
       Reply from 22.22.22.22: bytes=56 Sequence=3 ttl=253 time=4 ms
       Reply from 22.22.22.22: bytes=56 Sequence=4 ttl=253 time=5 ms
       Reply from 22.22.22.22: bytes=56 Sequence=5 ttl=253 time=5 ms
   
     --- 22.22.22.22 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 4/5/7 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    vpn frr
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  bfd
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:11::1
   locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::1/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/128
   isis ipv6 enable 1
  #               
  bfd pe1tope2 bind peer-ipv6 2001:DB8:20::
   discriminator local 100
   discriminator remote 200
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:12::2 as-number 100
   peer 2001:DB8:12::2 connect-interface LoopBack1
   peer 2001:DB8:13::3 as-number 100
   peer 2001:DB8:13::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:12::2 enable
    peer 2001:DB8:12::2 prefix-sid
    peer 2001:DB8:13::3 enable
    peer 2001:DB8:13::3 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    route-select delay 300
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.1.1.2 as-number 65410
  #               
  return
  ```
* PE2 configuration file
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  bfd
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:12::2
   locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/128
   isis ipv6 enable 1
  #               
  bfd pe2tope1 bind peer-ipv6 2001:DB8:10::
   discriminator local 200
   discriminator remote 100
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:11::1 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.2.1.2 as-number 65420
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:13::3
   locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
  #               
  isis 1          
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.3.1.1 255.255.255.0
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:13::3/128
   isis ipv6 enable 1
  #               
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv6-family unicast
    undo synchronization
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:11::1 prefix-sid
   #
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 10.3.1.2 as-number 65420
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
   ip address 10.1.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 11.11.11.11 255.255.255.255
  #               
  bgp 65410       
   peer 10.1.1.1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.1.1.1 enable
  #               
  return 
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown    
   ip address 10.3.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.1 as-number 100
   peer 10.3.1.1 as-number 100
  #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.1 enable
    peer 10.3.1.1 enable
  #
  return
  ```