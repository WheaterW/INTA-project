Example for Configuring L3VPNv4 HoVPN over MPLS Plus IS-IS SRv6 TE Policy
=========================================================================

This section provides an example for configuring L3VPNv4 HoVPN over MPLS plus SRv6 TE Policy.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0227026921__fig_dc_vrp_srv6_cfg_all_001101):

* The UPE, SPE, and NPE all belong to AS 100. They need to run IS-IS to implement IPv6 network connectivity.
* The UPE, SPE, and NPE all belong to IS-IS process 1.

It is required that a bidirectional MPLS LDP tunnel be established between the UPE and SPE and a bidirectional SRv6 TE Policy be established between the SPE and NPE to carry L3VPNv4 services.

**Figure 1** L3VPNv4 HoVPN over MPLS plus SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0235808557.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6/IPv4 address for each interface on the UPE, NPE, and SPE.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title (NET) on each device.
3. Configure basic MPLS functions and MPLS LDP on the UPE and SPE, and establish MPLS LDP LSPs between the two devices.
4. Configure VPN instances on the UPE, NPE, and SPE, and enable the IPv4 address family for the instances.
5. Establish an EBGP peer relationship between the UPE and CE1 and another one between the NPE and CE2.
6. Establish an MP-IBGP peer relationship between the UPE and SPE and another one between the SPE and NPE.
7. Configure SRv6 SIDs on the NPE and SPE, and enable the devices to advertise VPN routes carrying SIDs.
8. Deploy an SRv6 TE Policy between the SPE and NPE.
9. Configure a tunnel policy on the SPE and NPE to import traffic.
10. Specify the UPE as the peer of the SPE and configure the SPE to advertise the default route to the UPE.
11. Configure the SPE to advertise regenerated routes to the NPE.


#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface on the UPE, SPE, and NPE
* IS-IS process ID of the UPE, SPE, and NPE
* IS-IS level of the UPE, SPE, and NPE
* VPN instance name, RD, and RT on the SPE and NPE

#### Procedure

1. Configure an IP address and enable IPv6 forwarding for each interface.
   
   
   
   # Configure the NPE. The configurations of the SPE and UPE are similar to the configuration of the NPE. For configuration details, see [Configuration Files](#EN-US_TASK_0227026921__example764102717246) in this section.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname NPE
   [~HUAWEI] commit
   [~NPE] interface gigabitethernet 0/1/0
   [~NPE-GigabitEthernet0/1/0] ipv6 enable
   [*NPE-GigabitEthernet0/1/0] ipv6 address 2001:DB8:2001::2 96
   [*NPE-GigabitEthernet0/1/0] quit
   [*NPE] interface LoopBack 1
   [*NPE-LoopBack1] ip address 3.3.3.3 32
   [*NPE-LoopBack1] ipv6 enable
   [*NPE-LoopBack1] ipv6 address 2001:DB8:2::2 128
   [*NPE-LoopBack1] quit
   [*NPE] commit
   ```
2. Configure IS-IS.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] isis 1
   [*UPE-isis-1] is-level level-1
   [*UPE-isis-1] cost-style wide
   [*UPE-isis-1] network-entity 10.0000.0000.0001.00
   [*UPE-isis-1] quit
   [*UPE] interface gigabitethernet 0/1/0
   [*UPE-GigabitEthernet0/1/0] isis enable 1
   [*UPE-GigabitEthernet0/1/0] quit
   [*UPE] interface loopback1
   [*UPE-LoopBack1] isis enable 1
   [*UPE-LoopBack1] commit
   [~UPE-LoopBack1] quit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] isis 1 
   [*SPE-isis-1] is-level level-1
   [*SPE-isis-1] cost-style wide
   [*SPE-isis-1] network-entity 10.0000.0000.0002.00
   [*SPE-isis-1] ipv6 enable topology ipv6
   [*SPE-isis-1] quit
   [*SPE] interface gigabitethernet 0/1/0
   [*SPE-GigabitEthernet0/1/0] isis enable 1
   [*SPE-GigabitEthernet0/1/0] quit
   [*SPE] interface gigabitethernet 0/2/0
   [*SPE-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*SPE-GigabitEthernet0/2/0] quit
   [*SPE] interface loopback1
   [*SPE-LoopBack1] isis ipv6 enable 1
   [*SPE-LoopBack1] isis enable 1
   [*SPE-LoopBack1] commit
   [~SPE-LoopBack1] quit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] isis 1
   [*NPE-isis-1] is-level level-1
   [*NPE-isis-1] cost-style wide
   [*NPE-isis-1] network-entity 10.0000.0000.0003.00
   [*NPE-isis-1] ipv6 enable topology ipv6
   [*NPE-isis-1] quit
   [*NPE] interface gigabitethernet 0/1/0
   [*NPE-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*NPE-GigabitEthernet0/1/0] quit
   [*NPE] interface loopback1
   [*NPE-LoopBack1] isis ipv6 enable 1
   [*NPE-LoopBack1] commit
   [~NPE-LoopBack1] quit
   ```
   
   After the configuration is complete, perform the following operations to check whether IS-IS is successfully configured:
   
   # Display IS-IS neighbor information. The following example uses the command output on the UPE.
   ```
   [~UPE] display isis peer 
    
                             Peer information for ISIS(1) 
                             
     System Id     Interface          Circuit Id        State HoldTime Type     PRI 
   -------------------------------------------------------------------------------- 
   0000.0000.0002* GE0/1/0            0000.0000.0002.01  Up   8s       L1       64  
    
   Total Peer(s): 1
   ```
   
   # Display IS-IS routing table information. The following example uses the command output on the NPE.
   ```
   [~NPE] display isis route 
                            Route information for ISIS(1) 
                            ----------------------------- 
    
                           ISIS(1) Level-1 Forwarding Table 
                           -------------------------------- 
    
    IPV6 Dest.          ExitInterface   NextHop                    Cost     Flags     
   -------------------------------------------------------------------------------- 
   2001:DB8:1::1/128    GE0/1/0         FE80::3A92:6CFF:FE21:10    10       A/-/-/-   
   2001:DB8:2::2/128    Loop1           Direct                     0        D/-/L/-   
   2001:DB8:2001::/96   GE0/1/0         Direct                     10       D/-/L/-   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,  
               U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
3. Configure basic MPLS functions and MPLS LDP on the UPE and SPE, and establish MPLS LDP LSPs between the two devices.
   
   # Configure the UPE.
   ```
   [~UPE] mpls lsr-id 1.1.1.1
   [*UPE] mpls
   [*UPE-mpls] commit
   [~UPE-mpls] quit
   [~UPE] mpls ldp
   [*UPE-mpls-ldp] quit
   [*UPE] interface gigabitethernet 0/1/0
   [*UPE-GigabitEthernet0/1/0] mpls
   [*UPE-GigabitEthernet0/1/0] mpls ldp
   [*UPE-GigabitEthernet0/1/0] commit
   [~UPE-GigabitEthernet0/1/0] quit
   ```
   
   # Configure the SPE.
   ```
   [~SPE] mpls lsr-id 2.2.2.2
   [*SPE] mpls
   [*SPE-mpls] commit
   [~SPE-mpls] quit
   [~SPE] mpls ldp
   [*SPE-mpls-ldp] quit
   [*SPE] interface gigabitethernet 0/1/0
   [*SPE-GigabitEthernet0/1/0] mpls
   [*SPE-GigabitEthernet0/1/0] mpls ldp
   [*SPE-GigabitEthernet0/1/0] commit
   [~SPE-GigabitEthernet0/1/0] quit
   ```
   
   After the configuration is complete, run the **display mpls ldp session** command. If **Status** is displayed as **Operational** in the command output, LDP sessions have been successfully established between the UPE and SPE. Then, run the **display mpls ldp lsp** command to check whether LDP LSPs have been successfully established.
   
   The following example uses the command output on the UPE.
   ```
   [~UPE] display mpls ldp session
                  LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    -------------------------------------------------------------------------
    Peer-ID            Status       LAM  SsnRole  SsnAge       KA-Sent/Rcv
    -------------------------------------------------------------------------
    2.2.2.2:0          Operational DU   Passive  0006:20:55   39551/39552
    -------------------------------------------------------------------------
    TOTAL: 1 session(s) Found.
   ```
   ```
   [~UPE] display mpls ldp lsp
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop         OutInterface
    -------------------------------------------------------------------------------
    1.1.1.1/32         3/NULL         2.2.2.2         127.0.0.1       Loop1
   *1.1.1.1/32         Liberal/1024                   DS/2.2.2.2
    2.2.2.2/32         NULL/3         -               10.1.2.2        GE0/1/0
    2.2.2.2/32         1024/3         2.2.2.2         10.1.2.2        GE0/1/0
   -------------------------------------------------------------------------------
    TOTAL: 3 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 FRR LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   ```
4. On the UPE, NPE, and SPE, configure a VPN instance and enable the IPv4 address family for the instance.
   
   # Configure the UPE.
   ```
   [~UPE] ip vpn-instance vpna
   [*UPE-vpn-instance-vpna] ipv4-family
   [*UPE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*UPE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*UPE-vpn-instance-vpna-af-ipv4] quit
   [*UPE-vpn-instance-vpna] quit
   [*UPE] interface gigabitethernet 0/2/0
   [*UPE-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*UPE-GigabitEthernet0/2/0] ip address 10.1.1.1 24
   [*UPE-GigabitEthernet0/2/0] quit
   [*UPE] commit
   ```
   
   # Configure the SPE.
   ```
   [~SPE] ip vpn-instance vpna
   [*SPE-vpn-instance-vpna] ipv4-family
   [*SPE-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   [*SPE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*SPE-vpn-instance-vpna-af-ipv4] quit
   [*SPE-vpn-instance-vpna] quit
   [*SPE] commit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] ip vpn-instance vpna
   [*NPE-vpn-instance-vpna] ipv4-family
   [*NPE-vpn-instance-vpna-af-ipv4] route-distinguisher 300:1
   [*NPE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   [*NPE-vpn-instance-vpna-af-ipv4] quit
   [*NPE-vpn-instance-vpna] quit
   [*NPE] interface gigabitethernet 0/2/0
   [*NPE-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   [*NPE-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   [*NPE-GigabitEthernet0/2/0] quit
   [*NPE] commit
   ```
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on the UPE and NPE to check VPN instance configurations.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the UPE and NPE have multiple interfaces bound to the same VPN instance, use the **-a** *source-ip-address* parameter to specify a source IP address when running the **ping -vpn-instance** *vpn-instance-name* ***-a** source-ip-address dest-ip-address* command to ping the peer CE. If the source IP address is not specified, the ping operation may fail.
5. Establish an EBGP peer relationship between the UPE and CE1 and another one between the NPE and CE2.
   
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
   
   # Configure the UPE.
   ```
   [~UPE] bgp 100
   [*UPE-bgp] router-id 1.1.1.1
   [*UPE-bgp] ipv4-family vpn-instance vpna
   [*UPE-bgp-vpna] peer 10.1.1.2 as-number 65410
   [*UPE-bgp-vpna] import-route direct
   [*UPE-bgp-vpna] commit
   [~UPE-bgp-vpna] quit
   [~UPE-bgp] quit
   ```
   
   # Configure CE2.
   ```
   [~CE2] interface loopback 1
   [*CE2-LoopBack1] ip address 22.22.22.22 32
   [*CE2-LoopBack1] quit
   [*CE2] bgp 65420
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   [*CE2-bgp] network 22.22.22.22 32
   [*CE2-bgp] quit
   [*CE2] commit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] bgp 100
   [*NPE-bgp] router-id 3.3.3.3
   [*NPE-bgp] ipv4-family vpn-instance vpna
   [*NPE-bgp-vpna] peer 10.2.1.2 as-number 65420
   [*NPE-bgp-vpna] import-route direct
   [*NPE-bgp-vpna] commit
   [~NPE-bgp-vpna] quit
   [~NPE-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on the UPE and NPE to check whether BGP peer relationships have been established. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the command output on the UPE to show that a BGP peer relationship has been established between the UPE and CE1.
   ```
   [~UPE] display bgp vpnv4 vpn-instance vpna peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
   
    VPN-Instance vpna, Router ID 1.1.1.1:
    Total number of peers : 1            Peers in established state : 1
   
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.2        4   65410  11     9          0     00:06:37   Established  1
   ```
6. Establish an MP-IBGP peer relationship between the UPE and SPE and another one between the SPE and NPE.
   
   # Configure the UPE.
   ```
   [~UPE] bgp 100
   [~UPE-bgp] peer 2.2.2.2 as-number 100
   [*UPE-bgp] peer 2.2.2.2 connect-interface loopback 1
   [*UPE-bgp] ipv4-family vpnv4
   [*UPE-bgp-af-vpnv4] peer 2.2.2.2 enable
   [*UPE-bgp-af-vpnv4] commit
   [~UPE-bgp-af-vpnv4] quit
   [~UPE-bgp] quit
   ```
   
   # Configure the SPE.
   ```
   [~SPE] bgp 100
   [~SPE-bgp] peer 1.1.1.1 as-number 100
   [*SPE-bgp] peer 1.1.1.1 connect-interface loopback 1
   [*SPE-bgp] peer 2001:DB8:2::2 as-number 100
   [*SPE-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*SPE-bgp] ipv4-family vpnv4
   [*SPE-bgp-af-vpnv4] peer 1.1.1.1 enable
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:2::2 enable
   [*SPE-bgp-af-vpnv4] commit
   [~SPE-bgp-af-vpnv4] quit
   [~SPE-bgp] quit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] bgp 100
   [~NPE-bgp] peer 2001:DB8:1::1 as-number 100
   [*NPE-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*NPE-bgp] ipv4-family vpnv4
   [*NPE-bgp-af-vpnv4] peer 2001:DB8:1::1 enable
   [*NPE-bgp-af-vpnv4] commit
   [~NPE-bgp-af-vpnv4] quit
   [~NPE-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on the UPE and NPE to check whether BGP peer relationships have been established. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
   
   The following example uses the command output on the UPE.
   ```
   [~UPE] display bgp vpnv4 all peer 
    
    BGP local router ID : 1.1.1.1 
    Local AS number : 100 
    Total number of peers : 2                 Peers in established state : 2 
    
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv 
     2.2.2.2            4         100      216      220     0 03:03:35 Established        2 
    
     Peer of IPv4-family for vpn instance : 
    
     VPN-Instance vpna, Router ID 1.1.1.1: 
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv 
     10.1.1.2        4       65410      216      217     0 03:06:22 Established        1
   ```
7. Configure SRv6 SIDs on the NPE and SPE and enable the devices to carry SIDs in VPN routes.
   
   # Configure the SPE.
   ```
   [~SPE] segment-routing ipv6
   [*SPE-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*SPE-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
   [*SPE-segment-routing-ipv6-locator] opcode ::200 end no-flavor
   [*SPE-segment-routing-ipv6-locator] quit
   [*SPE-segment-routing-ipv6] quit
   [*SPE] bgp 100
   [*SPE-bgp] ipv4-family vpnv4
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:2::2 prefix-sid
   [*SPE-bgp-af-vpnv4] quit
   [*SPE-bgp] ipv4-family vpn-instance vpna
   [*SPE-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   [*SPE-bgp-vpna] segment-routing ipv6 locator as1
   [*SPE-bgp-vpna] commit
   [~SPE-bgp-vpna] quit
   [~SPE-bgp] quit
   [~SPE] isis 1
   [~SPE-isis-1] segment-routing ipv6 locator as1
   [*SPE-isis-1] commit
   [~SPE-isis-1] quit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] segment-routing ipv6
   [*NPE-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*NPE-segment-routing-ipv6] locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
   [*NPE-segment-routing-ipv6-locator] opcode ::300 end no-flavor
   [*NPE-segment-routing-ipv6-locator] quit
   [*NPE-segment-routing-ipv6] quit
   [*NPE] bgp 100
   [*NPE-bgp] ipv4-family vpnv4
   [*NPE-bgp-af-vpnv4] peer 2001:DB8:1::1 prefix-sid
   [*NPE-bgp-af-vpnv4] quit
   [*NPE-bgp] ipv4-family vpn-instance vpna
   [*NPE-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort
   [*NPE-bgp-vpna] segment-routing ipv6 locator as1
   [*NPE-bgp-vpna] commit
   [~NPE-bgp-vpna] quit
   [~NPE-bgp] quit
   [~NPE] isis 1
   [~NPE-isis-1] segment-routing ipv6 locator as1
   [*NPE-isis-1] commit
   [~NPE-isis-1] quit
   ```
   
   Run the **display segment-routing ipv6 local-sid** **end** **forwarding** command to check information about the SRv6 local SID table.
   ```
   [~SPE] display segment-routing ipv6 local-sid end forwarding 
                       My Local-SID End Forwarding Table 
                       --------------------------------- 
    
   SID         : 2001:DB8:10::200/128                       FuncType : End 
   Flavor      : NO-FLAVOR                                  SidCompress : NO   
   LocatorName : as1                                        LocatorID: 1 
   ProtocolType: STATIC                                     ProcessID: 1
   UpdateTime  : 2021-08-30 02:50:43.171
    
   SID         : 2001:DB8:10::1:0:1/128                     FuncType : End 
   Flavor      : PSP                                        SidCompress : NO
   LocatorName : as1                                        LocatorID: 1 
   ProtocolType: ISIS                                       ProcessID: 1
   UpdateTime  : 2021-08-30 01:49:56.292
    
   SID         : 2001:DB8:10::1:0:2/128                     FuncType : End 
   Flavor      : PSP USP USD                                SidCompress : NO
   LocatorName : as1                                        LocatorID: 1 
   ProtocolType: ISIS                                       ProcessID: 1
   UpdateTime  : 2021-08-30 01:49:56.292
    
   Total SID(s): 3
   ```
   ```
   [~NPE] display segment-routing ipv6 local-sid end forwarding 
                       My Local-SID End Forwarding Table 
                       --------------------------------- 
    
   SID         : 2001:DB8:20::300/128                       FuncType : End 
   Flavor      : NO-FLAVOR                                  SidCompress : NO
   LocatorName : as1                                        LocatorID: 1 
   ProtocolType: STATIC                                     ProcessID: 1
   UpdateTime  : 2021-08-29 03:29:43.171
    
   SID         : 2001:DB8:20::1:0:1/128                     FuncType : End 
   Flavor      : PSP                                        SidCompress : NO
   LocatorName : as1                                        LocatorID: 1
   ProtocolType: ISIS                                       ProcessID: 1
   UpdateTime  : 2021-08-30 01:17:59.324
    
   SID         : 2001:DB8:20::1:0:2/128                     FuncType : End 
   Flavor      : PSP USP USD                                SidCompress : NO
   LocatorName : as1                                        LocatorID: 1
   ProtocolType: ISIS                                       ProcessID: 1
   UpdateTime  : 2021-08-30 01:17:59.324
    
   Total SID(s): 3
   ```
8. Configure an SRv6 TE Policy.
   
   # Configure the SPE.
   ```
   [~SPE] segment-routing ipv6  
   [~SPE-segment-routing-ipv6] segment-list list1  
   [*SPE-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:20::300 
   [*SPE-segment-routing-ipv6-segment-list-list1] commit 
   [~SPE-segment-routing-ipv6-segment-list-list1] quit 
   [~SPE-segment-routing-ipv6] srv6-te-policy locator as1  
   [*SPE-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:2::2 color 101 
   [*SPE-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:10::100 
   [*SPE-segment-routing-ipv6-policy-policy1] candidate-path preference 100 
   [*SPE-segment-routing-ipv6-policy-policy1-path] segment-list list1  
   [*SPE-segment-routing-ipv6-policy-policy1-path] commit 
   [~SPE-segment-routing-ipv6-policy-policy1-path] quit 
   [~SPE-segment-routing-ipv6-policy-policy1] quit
   [~SPE-segment-routing-ipv6] quit
   ```
   
   
   # Configure the NPE.
   ```
   [~NPE] segment-routing ipv6  
   [~NPE-segment-routing-ipv6] segment-list list1  
   [*NPE-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:10::200 
   [*NPE-segment-routing-ipv6-segment-list-list1] commit 
   [~NPE-segment-routing-ipv6-segment-list-list1] quit 
   [~NPE-segment-routing-ipv6] srv6-te-policy locator as1  
   [*NPE-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101 
   [*NPE-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:20::200 
   [*NPE-segment-routing-ipv6-policy-policy1] candidate-path preference 100 
   [*NPE-segment-routing-ipv6-policy-policy1-path] segment-list list1  
   [*NPE-segment-routing-ipv6-policy-policy1-path] commit 
   [~NPE-segment-routing-ipv6-policy-policy1-path] quit 
   [~NPE-segment-routing-ipv6-policy-policy1] quit
   [~NPE-segment-routing-ipv6] quit
   ```
   
   After the configuration is complete, run the **display srv6-te policy** command to check SRv6 TE Policy information.
   
   The following example uses the command output on the SPE.
   ```
   [~SPE] display srv6-te policy  
   PolicyName : policy1 
   Color                   : 101                            Endpoint             : 2001:DB8:2::2 
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : - 
   Policy State            : Up                             State Change Time    : 2020-04-02 01:18:25
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
            2001:DB8:20::300
   ```
9. Configure a tunnel policy to import traffic.
   
   # Configure the SPE.
   ```
   [~SPE] route-policy p1 permit node 10 
   [*SPE-route-policy] apply extcommunity color 0:101 
   [*SPE-route-policy] quit 
   [*SPE] bgp 100 
   [*SPE-bgp] ipv4-family vpnv4 
   [*SPE-bgp-af-vpnv4] peer 2001:DB8:2::2 route-policy p1 import  
   [*SPE-bgp-af-vpnv4] quit 
   [*SPE-bgp] quit 
   [*SPE] tunnel-policy p1 
   [*SPE-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1 
   [*SPE-tunnel-policy-p1] quit 
   [*SPE] ip vpn-instance vpna 
   [*SPE-vpn-instance-vpna] ipv4-family
   [*SPE-vpn-instance-vpna-af-ipv4] tnl-policy p1 
   [*SPE-vpn-instance-vpna-af-ipv4] commit
   [~SPE-vpn-instance-vpna-af-ipv4] quit
   [~SPE-vpn-instance-vpna] quit
   ```
   
   # Configure the NPE.
   ```
   [~NPE] route-policy p1 permit node 10 
   [*NPE-route-policy] apply extcommunity color 0:101 
   [*NPE-route-policy] quit 
   [*NPE] bgp 100 
   [*NPE-bgp] ipv4-family vpnv4 
   [*NPE-bgp-af-vpnv4] peer 2001:DB8:1::1 route-policy p1 import  
   [*NPE-bgp-af-vpnv4] quit 
   [*NPE-bgp] quit 
   [*NPE] tunnel-policy p1 
   [*NPE-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1 
   [*NPE-tunnel-policy-p1] quit 
   [*NPE] ip vpn-instance vpna 
   [*NPE-vpn-instance-vpna] ipv4-family
   [*NPE-vpn-instance-vpna-af-ipv4] tnl-policy p1 
   [*NPE-vpn-instance-vpna-af-ipv4] commit
   [~NPE-vpn-instance-vpna-af-ipv4] quit
   [~NPE-vpn-instance-vpna] quit
   ```
   
   After the configuration is complete, run the **display ip routing-table vpn-instance vpna** command to check the routing table of the VPN instance. The command output shows that the corresponding route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on the SPE.
   ```
   [~SPE] display ip routing-table vpn-instance vpna  
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
   ------------------------------------------------------------------------------ 
   Routing Table : vpna 
            Destinations : 6        Routes : 6          
    
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface 
    
          10.1.1.0/24  Direct  0    0             D   1.1.1.1         GigabitEthernet0/1/0 
          10.2.1.0/24  IBGP    255  0             RD  2001:DB8:2::2   policy1 
       11.11.11.11/32  EBGP    255  0             RD  1.1.1.1         GigabitEthernet0/1/0 
       22.22.22.22/32  IBGP    255  0             RD  2001:DB8:2::2   policy1 
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0 
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   ```
   ```
   [~SPE] display ip routing-table vpn-instance vpna 22.22.22.22 verbose  
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
   ------------------------------------------------------------------------------ 
   Routing Table : vpna 
   Summary Count : 1 
    
   Destination: 22.22.22.22/32       
        Protocol: IBGP               Process ID: 0               
      Preference: 255                      Cost: 0               
         NextHop: 2001:DB8:2::2       Neighbour: 2001:DB8:2::2 
           State: Active Adv Relied         Age: 00h03m15s            
             Tag: 0                    Priority: low             
           Label: 3                     QoSInfo: 0x0            
      IndirectID: 0x10000E0            Instance:                                  
    RelayNextHop: 2001:DB8:2::2        Interface: policy1 
        TunnelID: 0x000000003400000001    Flags: RD 
      RouteColor: 0  
   ```
10. Specify the UPE as the peer of the SPE and configure the SPE to advertise the default route to the UPE.
    
    
    ```
    [~SPE] bgp 100
    [~SPE-bgp] ipv4-family vpnv4
    [*SPE-bgp-af-vpnv4] peer 1.1.1.1 upe
    [*SPE-bgp-af-vpnv4] peer 1.1.1.1 default-originate vpn-instance vpna
    [*SPE-bgp-af-vpnv4] commit
    [~SPE-bgp-af-vpnv4] quit
    [~SPE-bgp] quit
    ```
11. Configure the SPE to advertise regenerated routes to the NPE.
    
    
    ```
    [~SPE] bgp 100
    [~SPE-bgp] ipv4-family vpn-instance vpna
    [*SPE-bgp-vpna] advertise best-route route-reoriginate
    [*SPE-bgp-vpna] commit
    [~SPE-bgp-vpna] quit
    [~SPE-bgp] ipv4-family vpnv4
    [*SPE-bgp-af-vpnv4] peer 2001:DB8:2::2 advertise route-reoriginated vpnv4
    [*SPE-bgp-af-vpnv4] commit
    [~SPE-bgp-af-vpnv4] quit
    [~SPE-bgp] quit
    ```
12. Verify the configuration.
    
    # Check the routing tables of the SPE and NPE.
    ```
    [~SPE] display bgp vpnv4 all routing-table 10.1.1.2 
     BGP local router ID : 2.2.2.2
     Local AS number : 100
     
     Total routes of Route Distinguisher(100:1): 1
     BGP routing table entry information of 10.1.1.0/24:
     Label information (Received/Applied): 48060/NULL
     From: 1.1.1.1 (10.1.1.2)  
     Route Duration: 0d01h06m07s
     Relay IP Nexthop: 11.11.11.1
     Relay IP Out-Interface: GigabitEthernet0/1/0
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 1.1.1.1
     Qos information : 0x0
     Ext-Community: RT <111 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10
     Not advertised to any peer yet
     
     Total routes of Route Distinguisher(200:1): 1
     BGP routing table entry information of 10.1.1.0/24:
     From: 1.1.1.1 (10.1.1.2)  
     Route Duration: 0d00h10m13s
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 0.0.0.0
     Qos information : 0x0
     Ext-Community: RT <111 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, reoriginated, IGP cost 10
     Advertised to such 1 peers:
        2001:DB8:2::2
        
     VPN-Instance 1, Router ID 2.2.2.2:
     
     Total Number of Routes: 1
     BGP routing table entry information of 10.1.1.0/24:
     Route Distinguisher: 100:1
     Remote-Cross route
     Label information (Received/Applied): 48060/NULL
     From: 1.1.1.1 (10.1.1.2)  
     Route Duration: 0d00h10m40s
     Relay Tunnel Out-Interface: GigabitEthernet0/1/0
     Original nexthop: 1.1.1.1
     Qos information : 0x0
     Ext-Community: RT <111 : 1>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10
     Not advertised to any peer yet
    ```
    ```
    [~UPE] display ip routing-table vpn-instance vpna  
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
    ------------------------------------------------------------------------------ 
    Routing Table : vpna 
             Destinations : 7        Routes : 7          
     
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface 
     
           0.0.0.0/24   IBGP    255  0             RD  2.2.2.2         GigabitEthernet0/2/0 
          10.1.1.0/24   Direct  0    0             D   10.1.1.1        GigabitEthernet0/1/0 
          10.1.1.1/32   Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0 
        10.1.1.255/24   Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0  
       11.11.11.11/32   EBGP    255  0             RD  10.1.1.2        GigabitEthernet0/1/0 
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0 
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    
    # Check that CE1 can ping CE2 successfully.
    
    ```
    [~CE1] ping -a 11.11.11.11 22.22.22.22
      PING 22.22.22.22: 56  data bytes, press CTRL_C to break
        Reply from 22.22.22.22: bytes=56 Sequence=1 ttl=252 time=131 ms
        Reply from 22.22.22.22: bytes=56 Sequence=2 ttl=252 time=12 ms
        Reply from 22.22.22.22: bytes=56 Sequence=3 ttl=252 time=14 ms
        Reply from 22.22.22.22: bytes=56 Sequence=4 ttl=252 time=14 ms
        Reply from 22.22.22.22: bytes=56 Sequence=5 ttl=252 time=12 ms
    
      --- 22.22.22.22 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 12/36/131 ms
    ```

#### Configuration Files

* UPE configuration file
  ```
  # 
  sysname UPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-1
   cost-style wide
   mpls ldp auto-config
   network-entity 10.0000.0000.0001.00
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   router-id 1.1.1.1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.1.1.2 as-number 65410
  #
  return
  ```
* SPE configuration file
  ```
  # 
  sysname SPE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator as1 ipv6-prefix 2001:DB8:10:: 64 static 32
    opcode ::200 end no-flavor
   srv6-te-policy locator as1
   segment-list list1
    index 10 sid ipv6 2001:DB8:20::300
   srv6-te policy policy1 endpoint 2001:DB8:2::2 color 101
    binding-sid 2001:DB8:10::100
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   mpls ldp auto-config
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2001::1/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ip address 2.2.2.2 255.255.255.255
   ipv6 address 2001:DB8:1::1/128
   isis enable 1
   isis ipv6 enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 upe
    peer 1.1.1.1 default-originate vpn-instance vpna
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 route-policy p1 import
    peer 2001:DB8:2::2 prefix-sid
    peer 2001:DB8:2::2 advertise route-reoriginated vpnv4
   #
   ipv4-family vpn-instance vpna
    advertise best-route route-reoriginate
    segment-routing ipv6 locator as1
    segment-routing ipv6 traffic-engineer best-effort
  #
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #
  return
  ```
* NPE configuration file
  ```
  # 
  sysname NPE
  # 
  ip vpn-instance vpna 
   ipv4-family 
    route-distinguisher 300:1
    apply-label per-instance 
    tnl-policy p1 
    vpn-target 111:1 export-extcommunity 
    vpn-target 111:1 import-extcommunity 
  #                
  segment-routing ipv6 
   encapsulation source-address 2001:DB8:2::2 
   locator as1 ipv6-prefix 2001:DB8:20:: 64 static 32
    opcode ::300 end no-flavor
   srv6-te-policy locator as1 
   segment-list list1 
    index 10 sid ipv6 2001:DB8:10::200
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101 
    binding-sid 2001:DB8:20::200 
    candidate-path preference 100 
     segment-list list1  
  #                
  isis 1           
   is-level level-1 
   cost-style wide 
   network-entity 10.0000.0000.0003.00 
   #               
   ipv6 enable topology ipv6 
   segment-routing ipv6 locator as1 
   #               
  #                
  interface GigabitEthernet0/1/0 
   undo shutdown   
   ipv6 enable     
   ipv6 address 2001:DB8:2001::2/96 
   isis ipv6 enable 1 
  #                
  interface GigabitEthernet0/2/0
   undo shutdown   
   ip binding vpn-instance vpna 
   ip address 10.2.1.1 255.255.255.0 
  #                
  interface LoopBack1 
   ipv6 enable     
   ip address 3.3.3.3 255.255.255.255 
   ipv6 address 2001:DB8:2::2/128 
   isis ipv6 enable 1 
  #                
  bgp 100          
   router-id 3.3.3.3 
   peer 2001:DB8:1::1 as-number 100 
   peer 2001:DB8:1::1 connect-interface LoopBack1 
   #               
   ipv4-family unicast 
    undo synchronization 
   #               
   ipv4-family vpnv4 
    policy vpn-target 
    peer 2001:DB8:1::1 enable 
    peer 2001:DB8:1::1 route-policy p1 import 
    peer 2001:DB8:1::1 prefix-sid 
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
  interface LoopBack1 
   ip address 22.22.22.22 255.255.255.255 
  # 
  bgp 65420 
   peer 10.2.1.1 as-number 100 
   #
   ipv4-family unicast 
    undo synchronization 
    network 22.22.22.22 255.255.255.255 
    peer 10.2.1.1 enable 
  # 
  return
  ```