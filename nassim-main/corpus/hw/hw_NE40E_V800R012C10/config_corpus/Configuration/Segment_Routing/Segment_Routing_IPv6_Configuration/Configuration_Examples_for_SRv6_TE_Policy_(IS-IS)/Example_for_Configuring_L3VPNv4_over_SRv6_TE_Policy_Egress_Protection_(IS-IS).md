Example for Configuring L3VPNv4 over SRv6 TE Policy Egress Protection (IS-IS)
=============================================================================

This section provides an example for configuring egress protection when an SRv6 TE Policy is used to carry L3VPNv4 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0186214484__fig184238288365):

* PE1, the P, and PE2 are in the same AS and run IS-IS to implement IPv6 network connectivity.
* PE1, the P, and PE2 are Level-1 devices that belong to IS-IS process 1.

It is required that a bidirectional SRv6 TE Policy be deployed between PE1 and PE2 to carry L3VPNv4 services. In this example, PE2 is the egress of the SRv6 TE Policy, and PE3 provides protection for PE2 to enhance reliability.

**Figure 1** Networking for L3VPNv4 over SRv6 TE Policy egress protection![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0186215988.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, PE2, and PE3.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on PE1, PE2, PE3, and the P.
3. Configure VPN instances on PE1 and PE2.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish an MP-IBGP peer relationship between the PEs.
6. Enable IS-IS SRv6 on PE1, the P, PE2, and PE3, and configure static End SIDs for SRv6 TE Policy configuration.
7. Configure an SRv6 TE Policy on PE1 and PE2.
8. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.
9. Configure egress protection on PE3.
10. Configure SRv6 TI-LFA FRR and microloop avoidance on the PEs and P.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on PE1, the P, PE2, and PE3
* IS-IS process ID of PE1, the P, PE2, and PE3
* IS-IS level of PE1, the P, PE2, and PE3
* VPN instance name, RD, and RT on PE1, PE2, and PE3

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of the P, PE2, and PE3 are similar to the configuration of PE1. For configuration details, see [Configuration Files](#EN-US_TASK_0186214484__example201171946201118) in this section.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::1 96
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:11::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
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
   
   # Configure the P.
   
   ```
   [~P] isis 1 
   ```
   ```
   [*P-isis-1] is-level level-1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface gigabitethernet 0/1/0
   ```
   ```
   [*P-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P] interface gigabitethernet 0/2/0
   ```
   ```
   [*P-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P] interface loopback1
   ```
   ```
   [*P-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P-LoopBack1] commit
   ```
   ```
   [~P-LoopBack1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] commit
   ```
   ```
   [~PE2-LoopBack1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] isis 1
   ```
   ```
   [*PE3-isis-1] is-level level-1
   ```
   ```
   [*PE3-isis-1] cost-style wide
   ```
   ```
   [*PE3-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*PE3-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE3-isis-1] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] isis ipv6 enable 1
   ```
   ```
   [*PE3-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE3] interface loopback1
   ```
   ```
   [*PE3-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE3-LoopBack1] commit
   ```
   ```
   [~PE3-LoopBack1] quit
   ```
   
   
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   
                             Peer information for ISIS(1)
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0            0000.0000.0004.01  Up   7s       L1       64 
   
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis route
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
    IPV6 Dest.           ExitInterface      NextHop                    Cost     Flags    
   --------------------------------------------------------------------------------
   2001:DB8:11::1/128    Loop1              Direct                     0        D/-/L/-  
   2001:DB8:12::2/128    GE0/1/0            FE80::3AC2:67FF:FE31:300   10       A/-/-/-  
   2001:DB8:13::3/128    GE0/1/0            FE80::3AC2:67FF:FE41:307   10       A/-/-/-  
   2001:DB8:14::4/128    GE0/1/0            FE80::3AC2:67FF:FE61:302   10       A/-/-/-   
   2001:DB8:1::/96       GE0/1/0            Direct                     10       D/-/L/-  
   2001:DB8:2::/96       GE0/1/0            FE80::3AC2:67FF:FE31:300   20       A/-/-/-  
   2001:DB8:3::/96       GE0/1/0            FE80::3AC2:67FF:FE31:300   20       A/-/-/-   
   2001:DB8:4::/96       GE0/1/0            FE80::3AC2:67FF:FE41:307   20       A/-/-/-  
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut, 
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the interface that connects each PE to a CE to the VPN instance on that PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance vpna
   ```
   ```
   [*PE3-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE3-vpn-instance-vpna-af-ipv4] route-distinguisher 300:1
   ```
   ```
   [*PE3-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE3-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE3-vpn-instance-vpna] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip address 10.3.1.1 24
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure an IP address for each interface on the CEs, as shown in [Figure 1](#EN-US_TASK_0186214484__fig184238288365). For configuration details, see [Configuration Files](#EN-US_TASK_0186214484__screen1390157886214049) in this section.
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on the PEs to check VPN instance configurations. The command output shows that each PE can successfully ping its connected CE.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a PE has multiple interfaces bound to the same VPN instance, use the **-a** *source-ip-address* parameter to specify a source IP address when running the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation may fail.
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ip address 11.11.11.11 32
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   ```
   ```
   [*CE1-bgp] network 11.11.11.11 32
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 10.1.1.2 as-number 65410
   ```
   ```
   [*PE1-bgp-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   ```
   ```
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   ```
   ```
   [*CE2-LoopBack1] quit
   ```
   ```
   [*CE2] bgp 65420
   ```
   ```
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   ```
   ```
   [*CE2-bgp] peer 10.3.1.1 as-number 100
   ```
   ```
   [*CE2-bgp] network 22.22.22.22 32
   ```
   ```
   [*CE2-bgp] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] router-id 2.2.2.2
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] peer 10.2.1.2 as-number 65420
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] commit
   ```
   ```
   [~PE2-bgp-vpna] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE3-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE3-bgp-vpna] peer 10.3.1.2 as-number 65420
   ```
   ```
   [*PE3-bgp-vpna] import-route direct
   ```
   ```
   [*PE3-bgp-vpna] commit
   ```
   ```
   [~PE3-bgp-vpna] quit
   ```
   ```
   [~PE3-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on the PEs and check whether BGP peer relationships have been established between the PEs and CEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
   
    VPN-Instance vpna, Router ID 1.1.1.1:
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.2        4       65410      463      481     0 06:43:32 Established        2
   ```
5. Establish an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:13::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:13::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:14::4 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:14::4 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:13::3 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:14::4 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] peer 2001:DB8:11::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:11::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:14::4 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:14::4 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:11::1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:14::4 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] commit
   ```
   ```
   [~PE2-bgp-af-vpnv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [~PE3-bgp] peer 2001:DB8:11::1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:11::1 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:13::3 as-number 100
   ```
   ```
   [*PE3-bgp] peer 2001:DB8:13::3 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 2001:DB8:11::1 enable
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 2001:DB8:13::3 enable
   ```
   ```
   [*PE3-bgp-af-vpnv4] commit
   ```
   ```
   [~PE3-bgp-af-vpnv4] quit
   ```
   ```
   [~PE3-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on the PEs to check whether BGP peer relationships have been established between the PEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp vpnv4 all peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:13::3  4         100      466      459     0 06:36:07 Established        3
     2001:DB8:14::4  4         100      421      419     0 05:59:33 Established        3
   
     Peer of IPv4-family for vpn instance :
   
     VPN-Instance vpna, Router ID 1.1.1.1:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.2        4       65410      469      487     0 06:48:40 Established        2
   ```
6. Configure SRv6 SIDs, and configure the PEs to carry SIDs in VPN routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:11::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::1 end psp
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
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:13::3 prefix-sid
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:14::4 prefix-sid
   ```
   ```
   [*PE1-bgp-af-vpnv4] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 locator as1
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   ```
   [~PE1] isis 1
   ```
   ```
   [~PE1-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:DB8:12::2
   ```
   ```
   [*P-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] opcode ::1 end psp
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
   [*P-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   ```
   ```
   [*P-isis-1] commit
   ```
   ```
   [~P-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:13::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::1 end psp
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:11::1 prefix-sid
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:14::4 prefix-sid
   ```
   ```
   [*PE2-bgp-af-vpnv4] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 locator as1
   ```
   ```
   [*PE2-bgp-vpna] commit
   ```
   ```
   [~PE2-bgp-vpna] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   ```
   [~PE2] isis 1
   ```
   ```
   [~PE2-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   ```
   ```
   [*PE3-segment-routing-ipv6] encapsulation source-address 2001:DB8:14::4
   ```
   ```
   [*PE3-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32
   ```
   ```
   [*PE3-segment-routing-ipv6-locator] opcode ::1 end psp
   ```
   ```
   [*PE3-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE3-segment-routing-ipv6] quit
   ```
   ```
   [*PE3] bgp 100
   ```
   ```
   [*PE3-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 2001:DB8:11::1 prefix-sid
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 2001:DB8:13::3 prefix-sid
   ```
   ```
   [*PE3-bgp-af-vpnv4] quit
   ```
   ```
   [*PE3-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE3-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   ```
   ```
   [*PE3-bgp-vpna] segment-routing ipv6 locator as1
   ```
   ```
   [*PE3-bgp-vpna] commit
   ```
   ```
   [~PE3-bgp-vpna] quit
   ```
   ```
   [~PE3-bgp] quit
   ```
   ```
   [~PE3] isis 1
   ```
   ```
   [~PE3-isis-1] segment-routing ipv6 locator as1 auto-sid-disable
   ```
   ```
   [*PE3-isis-1] commit
   ```
   ```
   [~PE3-isis-1] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:10::1/128                           FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : as1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:46:05.713
   
   Total SID(s): 1
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:30::1/128                           FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : as1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:47:26.426
   
   Total SID(s): 1
   ```
   ```
   [~P] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:20::1/128                           FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : as1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:49:44.292
   
   Total SID(s): 1
   ```
7. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:20::1
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:30::1
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:13::3 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:10::100
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE1-segment-routing-ipv6-policy-policy1-path] commit
   [~PE1-segment-routing-ipv6-policy-policy1-path] quit
   [~PE1-segment-routing-ipv6-policy-policy1] quit
   [~PE1-segment-routing-ipv6] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6 
   [~PE2-segment-routing-ipv6] segment-list list1 
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:20::1
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:10::1
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator as1 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:11::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:30::300
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] commit
   [~PE2-segment-routing-ipv6-policy-policy1-path] quit
   [~PE2-segment-routing-ipv6-policy-policy1] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After the configuration is complete, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy 
   PolicyName : policy1
   Color                   : 101                            Endpoint             : 2001:DB8:13::3
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -
   Policy State            : Up                             State Change Time    : 2019-04-08 09:13:35
   Admin State             : Up                             Traffic Statistics   : Disable
   Backup Hot-Standby      : Disable                        BFD                  : Disable
   Interface Index         : -                              Interface Name       : - 
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:10::100(Insert, Preferred)
   Candidate-path Count    : 1                    
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0
    Discriminator          : 100                            Binding SID          : 2001:DB8:10::100
    GroupId                : 1                              Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable
    DelayTimerRemain       : -                              Network Slice ID     : -
    Segment-List Count     : 1
     Segment-List          : list1
      Segment-List ID      : 1                              XcIndex              : 1  
      List State           : Up                             DelayTimerRemain     : - 
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600 
      Weight               : 1                              BFD State            : -
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding ID   : -
      SID :  
            2001:DB8:20::1
            2001:DB8:30::1
   ```
8. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy p1 permit node 10
   [*PE1-route-policy] apply extcommunity color 0:101
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] ipv4-family vpnv4
   [*PE1-bgp-af-vpnv4] peer 2001:DB8:13::3 route-policy p1 import 
   [*PE1-bgp-af-vpnv4] quit
   [*PE1-bgp] quit
   [*PE1] tunnel-policy p1
   [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE1-tunnel-policy-p1] quit
   [*PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] tnl-policy p1
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   [~PE1-vpn-instance-vpna] quit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] route-policy p1 permit node 10
   [*PE2-route-policy] apply extcommunity color 0:101
   [*PE2-route-policy] quit
   [*PE2] bgp 100
   [*PE2-bgp] ipv4-family vpnv4
   [*PE2-bgp-af-vpnv4] peer 2001:DB8:11::1 route-policy p1 import 
   [*PE2-bgp-af-vpnv4] quit
   [*PE2-bgp] quit
   [*PE2] tunnel-policy p1
   [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE2-tunnel-policy-p1] quit
   [*PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] tnl-policy p1
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   [~PE2-vpn-instance-vpna] quit
   ```
   
   After the configuration is complete, run the **display ip routing-table vpn-instance vpna** command to check the routing table of the VPN instance. The command output shows that the VPN route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpna 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
            Destinations : 9        Routes : 9         
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop             Interface
   
          10.1.1.0/24  Direct  0    0             D   10.1.1.1            GigabitEthernet0/2/0
          10.1.1.1/32  Direct  0    0             D   127.0.0.1           GigabitEthernet0/2/0
        10.1.1.255/32  Direct  0    0             D   127.0.0.1           GigabitEthernet0/2/0
          10.2.1.0/24  IBGP    255  0             RD  2001:DB8:13::3      policy1
          10.3.1.0/24  IBGP    255  0             RD  2001:DB8:40::1:0:0  GigabitEthernet0/1/0
       11.11.11.11/32  EBGP    255  0             RD  10.1.1.2            GigabitEthernet0/2/0
       22.22.22.22/32  IBGP    255  0             RD  2001:DB8:13::3      policy1
         127.0.0.0/8   Direct  0    0             D   127.0.0.1           InLoopBack0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1           InLoopBack0
   ```
   ```
   [~PE1] display ip routing-table vpn-instance vpna 22.22.22.22 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
   Summary Count : 1
   
   Destination: 22.22.22.22/32      
        Protocol: IBGP               Process ID: 0              
      Preference: 255                      Cost: 0              
         NextHop: 2001:DB8:13::3      Neighbour: 2001:DB8:13::3
           State: Active Adv Relied         Age: 00h03m15s           
             Tag: 0                    Priority: low            
           Label: 3                     QoSInfo: 0x0           
      IndirectID: 0x10000E0            Instance:                                 
    RelayNextHop: ::                  Interface: policy1
        TunnelID: 0x000000003400000001    Flags: RD  
      RouteColor: 0 
   ```
9. Configure egress protection on PE3.
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   ```
   ```
   [~PE3-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32
   ```
   ```
   [*PE3-segment-routing-ipv6-locator] opcode ::999 end-m mirror-locator 2001:DB8:30:: 64
   ```
   ```
   [*PE3-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE3-segment-routing-ipv6] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure the P.
   
   ```
   [~P] isis 1
   [~P-isis-1] ipv6 frr                         
   [*P-isis-1-ipv6-frr] loop-free-alternate level-1
   [*P-isis-1-ipv6-frr] quit 
   [*P-isis-1] quit 
   [*P] commit                             
   ```
   
   After the configuration is complete, run the **display segment-routing ipv6 local-sid** **end-m** **forwarding** command to check SRv6 local SID table information.
   
   ```
   [~PE3] display segment-routing ipv6 local-sid end-m forwarding 
   
                       My Local-SID End.M Forwarding Table
                       ---------------------------------
   
   SID        : 2001:DB8:40::999/128                         FuncType : End.M
   Flavor     : --                                           SidCompress: NO  
   LocatorName: as1                                          LocatorID: 3
   MirrorLocatorNumber: 1
   MirrorLocator: 2001:DB8:30::/64 
   UpdateTime : 2023-05-10 01:46:05.713
   
   Total SID(s): 1
   ```
   
   # Display mirror FRR entries on the P.
   
   ```
   [~P] display isis route ipv6 2001:DB8:30:: 64 verbose                 
                            Route information for ISIS(1)  
                            -----------------------------  
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
    IPV6 Dest  : 2001:DB8:130::/64              Cost : 10           Flags: A/-/-/- 
    Admin Tag  : -                         Src Count : 2         Priority: Low     
    NextHop    :                           Interface :         ExitIndex :        
       FE80::3A92:6CFF:FE41:300                GE0/2/0            0x00000007       
    SRv6 MIRROR FRR:                                       
       Interface : GE0/3/0                                
       NextHop   : FE80::3A92:6CFF:FE61:302          IID  : 0x0100009c             
       Backup Sid Stack(Top->Bottom): {2001:DB8:40::999}            
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,     
               U-Up/Down Bit Set, LP-Local Prefix-Sid 
        Protect Type: L-Link Protect, N-Node Protect
   ```
10. Configure SRv6 TI-LFA FRR and microloop avoidance on the PEs and P.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] isis 1
    [~PE1-isis-1] avoid-microloop frr-protected
    [*PE1-isis-1] ipv6 avoid-microloop segment-routing
    [*PE1-isis-1] ipv6 frr                        
    [*PE1-isis-1-ipv6-frr] loop-free-alternate level-1
    [*PE1-isis-1-ipv6-frr] ti-lfa level-1
    [*PE1-isis-1-ipv6-frr] quit
    [*PE1-isis-1] quit 
    [*PE1] commit
    ```
    
    
    
    # Configure PE2.
    
    ```
    [~PE2] isis 1
    [~PE2-isis-1] avoid-microloop frr-protected
    [*PE2-isis-1] ipv6 avoid-microloop segment-routing
    [*PE2-isis-1] ipv6 frr                        
    [*PE2-isis-1-ipv6-frr] loop-free-alternate level-1
    [*PE2-isis-1-ipv6-frr] ti-lfa level-1
    [*PE2-isis-1-ipv6-frr] quit
    [*PE2-isis-1] quit 
    [*PE2] commit
    ```
    
    
    
    # Configure PE3.
    
    ```
    [~PE3] isis 1
    [~PE3-isis-1] avoid-microloop frr-protected
    [*PE3-isis-1] ipv6 avoid-microloop segment-routing
    [*PE3-isis-1] ipv6 frr                        
    [*PE3-isis-1-ipv6-frr] loop-free-alternate level-1
    [*PE3-isis-1-ipv6-frr] ti-lfa level-1
    [*PE3-isis-1-ipv6-frr] quit
    [*PE3-isis-1] quit 
    [*PE3] commit
    ```
    
    
    
    # Configure the P.
    
    ```
    [~P] isis 1
    [~P-isis-1] avoid-microloop frr-protected
    [*P-isis-1] ipv6 avoid-microloop segment-routing
    [*P-isis-1] ipv6 frr 
    [*P-isis-1-ipv6-frr] ti-lfa level-1
    [*P-isis-1-ipv6-frr] quit
    [*P-isis-1] quit 
    [*P] commit 
    ```
11. Verify the configuration.
    
    
    
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
    
    Disable an interface on PE2 to simulate a link fault.
    
    ```
    [~PE2] interface gigabitethernet 0/1/0
    ```
    ```
    [~PE2-GigabitEthernet0/1/0] shutdown
    ```
    ```
    [*PE2-GigabitEthernet0/1/0] commit
    ```
    ```
    [~PE2-GigabitEthernet0/1/0] quit
    ```
    
    Run the [**ping**](cmdqueryname=ping) command again. The command output shows that CEs belonging to the same VPN can still ping each other. For example:
    
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
    
    The preceding verification results indicate that PE3 can provide egress protection for the SRv6 TE Policy between PE1 and PE2.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:11::1
   locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
    opcode ::1 end psp 
   srv6-te-policy locator as1
   segment-list list1
    index 5 sid ipv6 2001:DB8:20::1
    index 10 sid ipv6 2001:DB8:30::1
   srv6-te policy policy1 endpoint 2001:DB8:13::3 color 101
    binding-sid 2001:DB8:10::100
    candidate-path preference 100
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   avoid-microloop frr-protected
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   ipv6 avoid-microloop segment-routing                   
   ipv6 frr                                               
    loop-free-alternate level-1                           
    ti-lfa level-1 
   #              
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:11::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:13::3 as-number 100
   peer 2001:DB8:13::3 connect-interface LoopBack1
   peer 2001:DB8:14::4 as-number 100
   peer 2001:DB8:14::4 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:DB8:13::3 enable
    peer 2001:DB8:13::3 route-policy p1 import
    peer 2001:DB8:13::3 prefix-sid
    peer 2001:DB8:14::4 enable
    peer 2001:DB8:14::4 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.1.1.2 as-number 65410
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return 
  ```
* P configuration file
  
  ```
  #
  sysname P        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:12::2
   locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
    opcode ::1 end psp 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   avoid-microloop frr-protected
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   ipv6 avoid-microloop segment-routing                   
   ipv6 frr                                               
    loop-free-alternate level-1                           
    ti-lfa level-1  
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
   ipv6 enable    
   ipv6 address 2001:DB8:2::1/96
   isis ipv6 enable 1  
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::1/96
   isis ipv6 enable 1 
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/128
   isis ipv6 enable 1
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
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:13::3
   locator as1 ipv6-prefix 2001:DB8:30:: 64 static 32
    opcode ::1 end psp 
   srv6-te-policy locator as1
   segment-list list1
    index 5 sid ipv6 2001:DB8:20::1
    index 10 sid ipv6 2001:DB8:10::1
   srv6-te policy policy1 endpoint 2001:DB8:11::1 color 101
    binding-sid 2001:DB8:30::300
    candidate-path preference 100
     segment-list list1 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   avoid-microloop frr-protected
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   ipv6 avoid-microloop segment-routing                   
   ipv6 frr                                               
    loop-free-alternate level-1                           
    ti-lfa level-1 
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:4::1/96
   isis ipv6 enable 1 
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:13::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack1
   peer 2001:DB8:14::4 as-number 100
   peer 2001:DB8:14::4 connect-interface LoopBack1
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
    peer 2001:DB8:11::1 route-policy p1 import
    peer 2001:DB8:11::1 prefix-sid
    peer 2001:DB8:14::4 enable
    peer 2001:DB8:14::4 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
    peer 10.2.1.2 as-number 65420
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
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
   encapsulation source-address 2001:DB8:14::4
   locator as1 ipv6-prefix 2001:DB8:40:: 64 static 32
    opcode ::1 end psp
    opcode ::999 end-m mirror-locator 2001:DB8:30:: 64
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   avoid-microloop frr-protected
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1 auto-sid-disable
   ipv6 avoid-microloop segment-routing                   
   ipv6 frr                                               
    loop-free-alternate level-1                           
    ti-lfa level-1 
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
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:4::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:14::4/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 2001:DB8:11::1 as-number 100
   peer 2001:DB8:11::1 connect-interface LoopBack1
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
    peer 2001:DB8:11::1 enable
    peer 2001:DB8:11::1 prefix-sid
    peer 2001:DB8:13::3 enable
    peer 2001:DB8:13::3 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
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