Example for Configuring Dual-Homing EVPN VPLS over IS-IS SRv6 BE (Active/Standby Status Determined by E-Trunk)
==============================================================================================================

This section provides an example for configuring SRv6 BE to carry EVPN E-LAN services. In the example, a redundancy mode needs to be configured on a per Ethernet segment identifier (ESI) basis.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001154848716__en-us_task_0227408534_fig_dc_vrp_srv6_cfg_all_002201), CE2 and CE3 are both dual-homed to PE2 and PE3. It is required that CE1-to-CE2 traffic be transmitted in load-balancing mode, whereas CE1-to-CE3 traffic be transmitted in non-load-balancing mode.

To meet this requirement, configure the all-active redundancy mode on a per ESI basis for CE2 access to PE2 and PE3 and the single-active redundancy mode on a per ESI basis for CE3 access to PE2 and PE3.

**Figure 1** EVPN VPLS over SRv6 BE (CE dual-homing) networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/1, respectively.


  
![](figure/en-us_image_0000002079418413.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each PE interface.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity on each PE.
3. Configure a BD EVPN instance on each PE.
4. Establish BGP EVPN peer relationships among the PEs.
5. Configure SRv6 BE on the PEs.
6. Bind the BD on each PE to an access-side sub-interface.
7. Configure a redundancy mode on a per ESI basis on PE2 and PE3.
8. Configure CE access to the PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance names: evrf1 and evrf2
* RDs and RTs of the EVPN instances
* BD IDs
* Locator names for PE1, PE2, and PE3: PE1\_BUM, PE2\_BUM, and PE3\_BUM, respectively; dynamically generated operation code (opcode)
* Length of the Args field for locators PE1\_BUM, PE2\_BUM, and PE3\_BUM: 10 bits

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:20::1 64
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
   [*PE1-LoopBack1] quit
   [*PE1] commit
   ```
   
   Configure an IPv4 address for the loopback interface because the EVPN source address needs to be an IPv4 address. The preceding example uses the configuration of PE1. The configurations of other devices are similar to that of PE1. For detailed configurations, see Configuration Files.
2. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   [*PE1-isis-1] is-level level-1
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
   [*PE2-isis-1] is-level level-1
   [*PE2-isis-1] cost-style wide
   [*PE2-isis-1] network-entity 10.0000.0000.0002.00
   [*PE2-isis-1] ipv6 enable topology ipv6
   [*PE2-isis-1] quit
   [*PE2] interface gigabitethernet 0/1/0
   [*PE2-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/1/0] quit
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE2-GigabitEthernet0/2/0] quit
   [*PE2] interface loopback1
   [*PE2-LoopBack1] isis ipv6 enable 1
   [*PE2-LoopBack1] commit
   [~PE2-LoopBack1] quit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] isis 1
   [*PE3-isis-1] is-level level-1
   [*PE3-isis-1] cost-style wide
   [*PE3-isis-1] network-entity 10.0000.0000.0003.00
   [*PE3-isis-1] ipv6 enable topology ipv6
   [*PE3-isis-1] quit
   [*PE3] interface gigabitethernet 0/1/0
   [*PE3-GigabitEthernet0/1/0] isis ipv6 enable 1
   [*PE3-GigabitEthernet0/1/0] quit
   [*PE3] interface gigabitethernet 0/2/0
   [*PE3-GigabitEthernet0/2/0] isis ipv6 enable 1
   [*PE3-GigabitEthernet0/2/0] quit
   [*PE3] interface loopback1
   [*PE3-LoopBack1] isis ipv6 enable 1
   [*PE3-LoopBack1] commit
   [~PE3-LoopBack1] quit
   ```
   
   After the configuration is complete, run the **display isis peer** and **display isis route** commands to check whether IS-IS has been configured successfully. PE1 is used as an example.
   
   ```
   [~PE1] display isis peer
                             Peer information for ISIS(1)  
   
     System Id     Interface          Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0003* GE0/2/0            0000.0000.0003.02  Up   8s       L1       64 
   0000.0000.0002* GE0/1/0            0000.0000.0002.02  Up   6s       L1       64 
   
   Total Peer(s): 2 
   ```
3. Configure a BD EVPN instance on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] bridge-domain 10
   [*PE1-bd10] evpn binding vpn-instance evrf1
   [*PE1-bd10] quit
   [*PE1] evpn vpn-instance evrf2 bd-mode
   [*PE1-evpn-instance-evrf2] route-distinguisher 200:1
   [*PE1-evpn-instance-evrf2] vpn-target 2:2
   [*PE1-evpn-instance-evrf2] quit
   [*PE1] bridge-domain 20
   [*PE1-bd20] evpn binding vpn-instance evrf2
   [*PE1-bd20] quit
   [*PE1] commit
   ```
   
   The preceding example uses the configuration of PE1. The configurations of other devices are similar to that of PE1. For detailed configurations, see Configuration Files.
4. Establish BGP EVPN peer relationships among the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] router-id 1.1.1.1
   [*PE1-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE1-bgp] peer 2001:DB8:2::2 as-number 100
   [*PE1-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   [*PE1-bgp-af-evpn] peer 2001:DB8:2::2 enable
   [*PE1-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   [*PE2-bgp] router-id 2.2.2.2
   [*PE2-bgp] peer 2001:DB8:1::1 as-number 100
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*PE2-bgp] peer 2001:DB8:3::3 as-number 100
   [*PE2-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
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
   [*PE3-bgp] peer 2001:DB8:1::1 as-number 100
   [*PE3-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   [*PE3-bgp] peer 2001:DB8:2::2 as-number 100
   [*PE3-bgp] peer 2001:DB8:2::2 connect-interface loopback 1
   [*PE3-bgp] l2vpn-family evpn
   [*PE3-bgp-af-evpn] peer 2001:DB8:1::1 enable
   [*PE3-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 enable
   [*PE3-bgp-af-evpn] peer 2001:DB8:2::2 advertise encap-type srv6
   [*PE3-bgp-af-evpn] quit
   [*PE3-bgp] quit
   [*PE3] commit
   ```
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether the BGP EVPN peer relationships have been established. If the **Established** state is displayed in the command output, the BGP EVPN peer relationships have been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer                              
   
    BGP local router ID : 1.1.1.1                          
    Local AS number : 100                                  
    Total number of peers : 2                 Peers in established state : 2       
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv                              
     2001:DB8:2::2                    4         100      120      125     0 01:05:04 Established        6                              
     2001:DB8:3::3                    4         100       27       27     0 00:12:15 Established        5 
   ```
5. Configure SRv6 BE on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   [*PE1-segment-routing-ipv6] locator PE1_BUM ipv6-prefix 2001:DB8:12:: 64 args 10
   [*PE1-segment-routing-ipv6-locator] quit
   [*PE1-segment-routing-ipv6] quit
   [*PE1] isis 1
   [*PE1-isis-1] segment-routing ipv6 locator PE1_BUM auto-sid-disable
   [*PE1-isis-1] quit
   [*PE1] evpn vpn-instance evrf1 bd-mode
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 locator PE1_BUM
   [*PE1-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf1] quit
   [*PE1] evpn vpn-instance evrf2 bd-mode
   [*PE1-evpn-instance-evrf2] segment-routing ipv6 locator PE1_BUM
   [*PE1-evpn-instance-evrf2] segment-routing ipv6 best-effort
   [*PE1-evpn-instance-evrf2] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   [*PE2-segment-routing-ipv6] locator PE2_BUM ipv6-prefix 2001:DB8:22:: 64 args 10
   [*PE2-segment-routing-ipv6-locator] quit
   [*PE2-segment-routing-ipv6] quit
   [*PE2] isis 1
   [*PE2-isis-1] segment-routing ipv6 locator PE2_BUM auto-sid-disable
   [*PE2-isis-1] quit
   [*PE2] evpn vpn-instance evrf1 bd-mode
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 locator PE2_BUM
   [*PE2-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf1] quit
   [*PE2] evpn vpn-instance evrf2 bd-mode
   [*PE2-evpn-instance-evrf2] segment-routing ipv6 locator PE2_BUM
   [*PE2-evpn-instance-evrf2] segment-routing ipv6 best-effort
   [*PE2-evpn-instance-evrf2] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] segment-routing ipv6
   [*PE3-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   [*PE3-segment-routing-ipv6] locator PE3_BUM ipv6-prefix 2001:DB8:32:: 64 args 10
   [*PE3-segment-routing-ipv6-locator] quit
   [*PE3-segment-routing-ipv6] quit
   [*PE3] isis 1
   [*PE3-isis-1] segment-routing ipv6 locator PE3_BUM auto-sid-disable
   [*PE3-isis-1] quit
   [*PE3] evpn vpn-instance evrf1 bd-mode
   [*PE3-evpn-instance-evrf1] segment-routing ipv6 locator PE3_BUM
   [*PE3-evpn-instance-evrf1] segment-routing ipv6 best-effort
   [*PE3-evpn-instance-evrf1] quit
   [*PE3] evpn vpn-instance evrf2 bd-mode
   [*PE3-evpn-instance-evrf2] segment-routing ipv6 locator PE3_BUM
   [*PE3-evpn-instance-evrf2] segment-routing ipv6 best-effort
   [*PE3-evpn-instance-evrf2] quit
   [*PE3] commit
   ```
   
   Run the **display segment-routing ipv6 local-sid** { **end-dt2u** | **end-dt2ul** | **end-dt2m** } **forwarding** command on each PE to check information about the SRv6 BE local SID table. PE1 is used as an example.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end-dt2m forwarding
                       My Local-SID End.DT2M Forwarding Table  
                       --------------------------------------                      
   
   SID             : 2001:DB8:12::400:0:7800/118                  FuncType : End.DT2M
   Bridge-domain ID: 10                                    
   LocatorName     : PE1_BUM                                      LocatorID: 2
   Flavor          : NO-FLAVOR                                    SidCompress : NO
   UpdateTime      : 2023-05-10 01:46:05.713
   
   SID             : 2001:DB8:12::400:0:7C00/118                  FuncType : End.DT2M 
   Bridge-domain ID: 20                                    
   LocatorName     : PE1_BUM                                      LocatorID: 2
   Flavor          : NO-FLAVOR                                    SidCompress : NO
   UpdateTime      : 2023-05-10 01:46:05.713
   
   Total SID(s): 2 
   ```
6. Bind the BD on each PE to an access-side sub-interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/3/0.1 mode l2
   [*PE1-GigabitEthernet0/3/0.1] encapsulation dot1q vid 10
   [*PE1-GigabitEthernet0/3/0.1] rewrite pop single
   [*PE1-GigabitEthernet0/3/0.1] bridge-domain 10
   [*PE1-GigabitEthernet0/3/0.1] quit
   [*PE1] interface gigabitethernet 0/3/0.2 mode l2
   [*PE1-GigabitEthernet0/3/0.2] encapsulation dot1q vid 20
   [*PE1-GigabitEthernet0/3/0.2] rewrite pop single
   [*PE1-GigabitEthernet0/3/0.2] bridge-domain 20
   [*PE1-GigabitEthernet0/3/0.2] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] lacp e-trunk system-id 00e0-fc12-3456
   [*PE2] e-trunk 1
   [*PE2-e-trunk-1] priority 10
   [*PE2-e-trunk-1] peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   [*PE2-e-trunk-1] security-key cipher YsHsjx_202206
   [*PE2-e-trunk-1] quit
   [*PE2] e-trunk 2
   [*PE2-e-trunk-2] priority 10
   [*PE2-e-trunk-2] peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   [*PE2-e-trunk-2] security-key cipher 00E0FC000011
   [*PE2-e-trunk-2] quit
   [*PE2] interface eth-trunk 10
   [*PE2-Eth-Trunk10] mode lacp-static
   [*PE2-Eth-Trunk10] e-trunk 1
   [*PE2-Eth-Trunk10] quit
   [*PE2] interface eth-trunk 10.1 mode l2
   [*PE2-Eth-Trunk10.1] encapsulation dot1q vid 10
   [*PE2-Eth-Trunk10.1] rewrite pop single
   [*PE2-Eth-Trunk10.1] bridge-domain 10
   [*PE2-Eth-Trunk10.1] quit
   [*PE2] interface eth-trunk 20
   [*PE2-Eth-Trunk20] mode lacp-static
   [*PE2-Eth-Trunk20] e-trunk 2
   [*PE2-Eth-Trunk20] quit
   [*PE2] interface eth-trunk 20.1 mode l2
   [*PE2-Eth-Trunk20.1] encapsulation dot1q vid 20
   [*PE2-Eth-Trunk20.1] rewrite pop single
   [*PE2-Eth-Trunk20.1] bridge-domain 20
   [*PE2-Eth-Trunk20.1] quit
   [*PE2] interface gigabitethernet 0/3/0
   [*PE2-GigabitEthernet0/3/0] eth-trunk 10
   [*PE2-GigabitEthernet0/3/0] quit
   [*PE2] interface gigabitethernet 0/1/1
   [*PE2-GigabitEthernet0/1/1] eth-trunk 20
   [*PE2-GigabitEthernet0/1/1] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] lacp e-trunk system-id 00e0-fc12-3456
   [*PE3] e-trunk 1
   [*PE3-e-trunk-1] priority 10
   [*PE3-e-trunk-1] peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   [*PE3-e-trunk-1] security-key cipher YsHsjx_202206
   [*PE3-e-trunk-1] quit
   [*PE3] e-trunk 2
   [*PE3-e-trunk-2] priority 10
   [*PE3-e-trunk-2] peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   [*PE3-e-trunk-2] security-key cipher 00E0FC000011
   [*PE3-e-trunk-2] quit
   [*PE3] interface eth-trunk 10
   [*PE3-Eth-Trunk10] mode lacp-static
   [*PE3-Eth-Trunk10] e-trunk 1
   [*PE3-Eth-Trunk10] quit
   [*PE3] interface eth-trunk 10.1 mode l2
   [*PE3-Eth-Trunk10.1] encapsulation dot1q vid 10
   [*PE3-Eth-Trunk10.1] rewrite pop single
   [*PE3-Eth-Trunk10.1] bridge-domain 10
   [*PE3-Eth-Trunk10.1] quit
   [*PE3] interface eth-trunk 20
   [*PE3-Eth-Trunk20] mode lacp-static
   [*PE3-Eth-Trunk20] e-trunk 2
   [*PE3-Eth-Trunk20] quit
   [*PE3] interface eth-trunk 20.1 mode l2
   [*PE3-Eth-Trunk20.1] encapsulation dot1q vid 20
   [*PE3-Eth-Trunk20.1] rewrite pop single
   [*PE3-Eth-Trunk20.1] bridge-domain 20
   [*PE3-Eth-Trunk20.1] quit
   [*PE3] interface gigabitethernet 0/3/0
   [*PE3-GigabitEthernet0/3/0] eth-trunk 20
   [*PE3-GigabitEthernet0/3/0] quit
   [*PE3] interface gigabitethernet 0/1/1
   [*PE3-GigabitEthernet0/1/1] eth-trunk 10
   [*PE3-GigabitEthernet0/1/1] quit
   [*PE3] commit
   ```
7. Configure a redundancy mode on a per ESI basis on PE2 and PE3.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] evpn
   [*PE2-evpn] esi 0001.0002.0003.0004.0005
   [*PE2-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode all-active
   [*PE2-evpn-esi-0001.0002.0003.0004.0005] quit
   [*PE2-evpn] esi 0005.0004.0003.0002.0001
   [*PE2-evpn-esi-0005.0004.0003.0002.0001] evpn redundancy-mode single-active
   [*PE2-evpn-esi-0005.0004.0003.0002.0001] quit
   [*PE2-evpn] quit
   [*PE2] interface Eth-Trunk 10
   [*PE2-Eth-Trunk10] esi 0001.0002.0003.0004.0005
   [*PE2-Eth-Trunk10] e-trunk mode force-master
   [*PE2-Eth-Trunk10] quit
   [*PE2] interface Eth-Trunk 20
   [*PE2-Eth-Trunk20] esi 0005.0004.0003.0002.0001
   [*PE2-Eth-Trunk20] e-trunk mode auto
   [*PE2-Eth-Trunk20] quit
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn
   [*PE3-evpn] esi 0001.0002.0003.0004.0005
   [*PE3-evpn-esi-0001.0002.0003.0004.0005] evpn redundancy-mode all-active
   [*PE3-evpn-esi-0001.0002.0003.0004.0005] quit
   [*PE3-evpn] esi 0005.0004.0003.0002.0001
   [*PE3-evpn-esi-0005.0004.0003.0002.0001] evpn redundancy-mode single-active
   [*PE3-evpn-esi-0005.0004.0003.0002.0001] quit
   [*PE3-evpn] quit
   [*PE3] interface Eth-Trunk 10
   [*PE3-Eth-Trunk10] esi 0001.0002.0003.0004.0005
   [*PE3-Eth-Trunk10] e-trunk mode force-master
   [*PE3-Eth-Trunk10] quit
   [*PE3] interface Eth-Trunk 20
   [*PE3-Eth-Trunk20] esi 0005.0004.0003.0002.0001
   [*PE3-Eth-Trunk20] e-trunk mode auto
   [*PE3-Eth-Trunk20] quit
   [*PE3] commit
   ```
8. Configure CE access to the PEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0
   [~CE1-GigabitEthernet0/1/0] undo shutdown
   [*CE1-GigabitEthernet0/1/0] quit
   [*CE1] interface gigabitethernet 0/1/0.1
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   [*CE1-GigabitEthernet0/1/0.1] ip address 10.1.1.1 255.255.255.0
   [*CE1-GigabitEthernet0/1/0.1] quit
   [*CE1] interface gigabitethernet 0/1/0.2
   [*CE1-GigabitEthernet0/1/0.2] vlan-type dot1q 20
   [*CE1-GigabitEthernet0/1/0.2] ip address 10.2.1.1 255.255.255.0
   [*CE1-GigabitEthernet0/1/0.2] quit
   [*CE1] commit
   ```
   
   
   
   # Configure CE2 and enable intra-VLAN Eth-Trunk load balancing.
   
   ```
   [~CE2] interface Eth-Trunk10
   [*CE2-Eth-Trunk10] mode lacp-static
   [*CE2-Eth-Trunk10] quit
   [*CE2] interface Eth-Trunk10.1
   [*CE2-Eth-Trunk10.1] vlan-type dot1q 10
   [*CE2-Eth-Trunk10.1] ip address 10.1.1.2 255.255.255.0
   [*CE2-Eth-Trunk10.1] quit
   [*CE2] interface gigabitethernet 0/1/0
   [*CE2-GigabitEthernet0/1/0] undo shutdown
   [*CE2-GigabitEthernet0/1/0] eth-trunk 10
   [*CE2-GigabitEthernet0/1/0] quit
   [*CE2] interface gigabitethernet 0/2/0
   [*CE2-GigabitEthernet0/2/0] undo shutdown
   [*CE2-GigabitEthernet0/2/0] eth-trunk 10
   [*CE2-GigabitEthernet0/2/0] quit
   [*CE2] vlan 10
   [*CE2-vlan10] trunk multicast load-balance enable
   [*CE2-vlan10] quit
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] interface Eth-Trunk20
   [*CE3-Eth-Trunk20] mode lacp-static
   [*CE3-Eth-Trunk20] quit
   [*CE3] interface Eth-Trunk20.1
   [*CE3-Eth-Trunk20.1] vlan-type dot1q 20
   [*CE3-Eth-Trunk20.1] ip address 10.2.1.2 255.255.255.0
   [*CE3-Eth-Trunk20.1] quit
   [*CE3] interface gigabitethernet 0/1/0
   [*CE3-GigabitEthernet0/1/0] undo shutdown
   [*CE3-GigabitEthernet0/1/0] eth-trunk 20
   [*CE3-GigabitEthernet0/1/0] quit
   [*CE3] interface gigabitethernet 0/2/0
   [*CE3-GigabitEthernet0/2/0] undo shutdown
   [*CE3-GigabitEthernet0/2/0] eth-trunk 20
   [*CE3-GigabitEthernet0/2/0] quit
   [*CE3] commit
   ```
   
   After the configuration is complete, the corresponding Eth-Trunk should be up. Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) command on PE2 and PE3 to check the Eth-Trunk status.
   
   Command output on PE2:
   
   ```
   [~PE2] display eth-trunk 10                              
   Eth-Trunk10's state information is:                     
   WorkingMode: NORMAL          Hash arithmetic: According to flow                 
   Least Active-linknumber: 1   Max Bandwidth-affected-linknumber: 32              
   Operate status: up           Number Of Up Ports In Trunk: 1                     
   --------------------------------------------------------------------------------
   PortName                      Status      Weight        
   GigabitEthernet0/3/0          Up          1             
   
   [~PE2] display eth-trunk 20 
   Eth-Trunk20's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 20                      WorkingMode: STATIC
   Preempt Delay: Disabled         Hash arithmetic: According to flow
   System Priority: 32768          System ID: xxxx-xxxx-xxxx
   Least Active-linknumber: 1      Max Active-linknumber: 64
   Operate status: up              Number Of Up Ports In Trunk: 1
   Timeout Period: Slow          
   PortKeyMode: Auto
   ------------------------------------------------------------------------------------
   ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
   GigabitEthernet0/1/1(r)    Selected 10GE     32768   1      5185    10111100  1     
   
   Partner:
   ------------------------------------------------------------------------------------
   ActorPortName              SysPri   SystemID        PortPri PortNo PortKey PortState
   GigabitEthernet0/1/1       32768    xxxx-xxxx-xxxx  32768   2      5185    10111100 
   ```
   
   Command output on PE3:
   
   ```
   [~PE3] display eth-trunk 10                              
   Eth-Trunk10's state information is:                     
   WorkingMode: NORMAL          Hash arithmetic: According to flow                 
   Least Active-linknumber: 1   Max Bandwidth-affected-linknumber: 32              
   Operate status: up           Number Of Up Ports In Trunk: 1                     
   --------------------------------------------------------------------------------
   PortName                      Status      Weight        
   GigabitEthernet0/1/1       Up          1             
   
   [~PE3] display eth-trunk 20    
   Eth-Trunk20's state information is:
   (h): high priority
   (r): reference port
   Local:
   LAG ID: 20                      WorkingMode: STATIC
   Preempt Delay: Disabled         Hash arithmetic: According to flow
   System Priority: 32768          System ID: xxxx-xxxx-xxxx(Remote)
   Least Active-linknumber: 1      Max Active-linknumber: 64
   Operate status: down            Number Of Up Ports In Trunk: 0
   Timeout Period: Slow          
   PortKeyMode: Auto
   ------------------------------------------------------------------------------------
   ActorPortName              Status   PortType PortPri PortNo PortKey PortState Weight
   GigabitEthernet0/3/0(r)    Unselect 10GE     32768   32770  5185    10100000  1     
   
   Partner:
   ------------------------------------------------------------------------------------
   ActorPortName              SysPri   SystemID        PortPri PortNo PortKey PortState
   GigabitEthernet0/3/0       32768    xxxx-xxxx-xxxx  32768   1      5185    10110000
   ```
   
   According to the Eth-Trunk status shown in the preceding command output, for Eth-Trunk 10, PE2 and PE3 are both active; for Eth-Trunk 20, PE2 and PE3 are in master and backup states, respectively. That is, for Eth-Trunk 20, only PE2 is active.
9. Verify the configuration.
   
   
   
   Run the **display bgp evpn all routing-table** command on each PE. The command output shows the EVPN routes sent from the peer end. PE1 is used as an example.
   
   ```
   [~PE1] display bgp evpn all routing-table
   
    Local AS number : 100                                  
   
    BGP Local router ID is 1.1.1.1                         
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale 
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:                                   
    Number of A-D Routes: 7                                
    Route Distinguisher: 100:1                             
          Network(ESI/EthTagId)                                  NextHop           
    *>i   0001.0002.0003.0004.0005:0                             2001:DB8:2::2     
    * i                                                          2001:DB8:3::3                                                         
    Route Distinguisher: 200:1                             
          Network(ESI/EthTagId)                                  NextHop           
    *>i   0005.0004.0003.0002.0001:0                             2001:DB8:2::2     
    * i                                                          2001:DB8:3::3     
    Route Distinguisher: 2.2.2.2:0                         
          Network(ESI/EthTagId)                                  NextHop           
    *>i   0001.0002.0003.0004.0005:4294967295                    2001:DB8:2::2  
    Route Distinguisher: 3.3.3.3:0                         
          Network(ESI/EthTagId)                                  NextHop           
    *>i   0001.0002.0003.0004.0005:4294967295                    2001:DB8:3::3     
    *>i   0005.0004.0003.0002.0001:4294967295                    2001:DB8:3::3     
   
   
    EVPN-Instance evrf1:                                   
    Number of A-D Routes: 4                                
          Network(ESI/EthTagId)                                  NextHop           
    *>i   0001.0002.0003.0004.0005:0                             2001:DB8:2::2     
    * i                                                          2001:DB8:3::3     
    *>i   0001.0002.0003.0004.0005:4294967295                    2001:DB8:2::2     
    * i                                                          2001:DB8:3::3     
   
   
    EVPN-Instance evrf2:                                   
    Number of A-D Routes: 3                                
          Network(ESI/EthTagId)                                  NextHop           
    *>i   0005.0004.0003.0002.0001:0                             2001:DB8:3::3     
      i                                                          2001:DB8:2::2     
    *>i   0005.0004.0003.0002.0001:4294967295                    2001:DB8:3::3  
   
    EVPN address family:                                   
    Number of Mac Routes: 3                                
    Route Distinguisher: 100:1                             
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop           
    *>i   0:48:38c2-6721-0300:0:0.0.0.0                          2001:DB8:2::2     
    * i                                                          2001:DB8:3::3     
    Route Distinguisher: 200:1                             
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop           
    *>    0:48:38c2-6721-0300:0:0.0.0.0                          0.0.0.0           
   
   
    EVPN-Instance evrf1:       
    Number of Mac Routes: 3                                
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop           
    *>    0:48:38c2-6721-0300:0:0.0.0.0                          0.0.0.0           
    * i                                                          2001:DB8:2::2     
    * i                                                          2001:DB8:3::3     
   
   
    EVPN-Instance evrf2:                                   
    Number of Mac Routes: 1                                
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop           
    *>    0:48:38c2-6721-0300:0:0.0.0.0                          0.0.0.0           
   
    EVPN address family:                                   
    Number of Inclusive Multicast Routes: 6                
    Route Distinguisher: 100:1                             
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop           
    *>    0:32:1.1.1.1                                           127.0.0.1         
    *>i   0:32:2.2.2.2                                           2001:DB8:2::2     
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3     
    Route Distinguisher: 200:1                             
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop           
    *>    0:32:1.1.1.1                                           127.0.0.1         
    *>i   0:32:2.2.2.2                                           2001:DB8:2::2     
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3     
   
   
    EVPN-Instance evrf1:                                   
    Number of Inclusive Multicast Routes: 3                
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop           
    *>    0:32:1.1.1.1                                           127.0.0.1     
    *>i   0:32:2.2.2.2                                           2001:DB8:2::2     
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3     
   
   
    EVPN-Instance evrf2:                                   
    Number of Inclusive Multicast Routes: 3                
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop           
    *>    0:32:1.1.1.1                                           127.0.0.1         
    *>i   0:32:2.2.2.2                                           2001:DB8:2::2     
    *>i   0:32:3.3.3.3                                           2001:DB8:3::3     
   ```
   
   Run the **display bgp evpn all routing-table ad-route** command on PE1. The command output shows the A-D EVPN routes sent from the peer end.
   
   Check the route of the ESI 0001.0002.0003.0004.0005. According to the **ESI Label** field, dual-homing active-active networking has been configured for the ESI.
   
   ```
   [~PE1] display bgp evpn all routing-table ad-route 0001.0002.0003.0004.0005:4294967295 
   
    BGP local router ID : 1.1.1.1                          
    Local AS number : 100                                  
    Total routes of Route Distinguisher(2.2.2.2:0): 1      
    BGP routing table entry information of 0001.0002.0003.0004.0005:4294967295:    
    From: 2001:DB8:2::2 (2.2.2.2)                          
    Route Duration: 0d00h31m39s                            
    Relay IP Nexthop: FE80::3AC2:67FF:FE31:307             
    Relay IP Out-Interface:GigabitEthernet0/1/0
    Relay Tunnel Out-Interface:                            
    Original nexthop: 2001:DB8:2::2                        
    Qos information : 0x0                                  
    Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, ESI Label<0 : 0 : 48066>    
    Prefix-sid: 2001:DB8:21::1:0:20, Endpoint Behavior: DT2U(23)
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 4294967295                     
    Not advertised to any peer yet                         
   
    Total routes of Route Distinguisher(3.3.3.3:0): 1      
    BGP routing table entry information of 0001.0002.0003.0004.0005:4294967295:    
    From: 2001:DB8:3::3 (3.3.3.3)     
    Route Duration: 0d00h30m23s                            
    Relay IP Nexthop: FE80::3AC2:67FF:FE41:305             
    Relay IP Out-Interface:GigabitEthernet0/2/0                   
    Relay Tunnel Out-Interface:                            
    Original nexthop: 2001:DB8:3::3                        
    Qos information : 0x0                                  
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, ESI Label<0 : 0 : 48066>    
    Prefix-sid: 2001:DB8:31::1:0:20, Endpoint Behavior: DT2U(23)                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 4294967295                     
    Not advertised to any peer yet                         
   
   
   
    EVPN-Instance evrf1:                                   
    Number of A-D Routes: 2                                
    BGP routing table entry information of 0001.0002.0003.0004.0005:4294967295:    
    Route Distinguisher: 2.2.2.2:0                         
    Remote-Cross route                                     
    From: 2001:DB8:2::2 (2.2.2.2)                          
    Route Duration: 0d00h31m53s     
    Relay IP Nexthop: FE80::3AC2:67FF:FE31:307             
    Relay IP Out-Interface:GigabitEthernet0/1/0                   
    Relay Tunnel Out-Interface:                            
    Original nexthop: 2001:DB8:2::2                        
    Qos information : 0x0                                  
    Ext-Community: RT <1 : 1>, SoO <2.2.2.2 : 0>, ESI Label<0 : 0 : 48066>    
    Prefix-sid: 2001:DB8:21::1:0:20, Endpoint Behavior: DT2U(23)                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 4294967295                     
    Not advertised to any peer yet                         
   
    BGP routing table entry information of 0001.0002.0003.0004.0005:4294967295:    
    Route Distinguisher: 3.3.3.3:0                         
    Remote-Cross route                                     
    From: 2001:DB8:3::3 (3.3.3.3)                          
    Route Duration: 0d00h30m38s                            
    Relay IP Nexthop: FE80::3AC2:67FF:FE41:305             
    Relay IP Out-Interface:GigabitEthernet0/2/0                   
    Relay Tunnel Out-Interface:                            
    Original nexthop: 2001:DB8:3::3  
    Qos information : 0x0                                  
    Ext-Community: RT <1 : 1>, SoO <3.3.3.3 : 0>, ESI Label<0 : 0 : 48066>    
    Prefix-sid: 2001:DB8:31::1:0:20, Endpoint Behavior: DT2U(23)                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, pre 255, IGP cost 10, not preferred for router ID      
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0001.0002.0003.0004.0005, Ethernet Tag ID: 4294967295                     
    Not advertised to any peer yet 
   ```
   
   Check the route of the ESI 0005.0004.0003.0002.0001. According to the **ESI Label** field, dual-homing single-active networking has been configured for the ESI.
   
   ```
   [~PE1] display bgp evpn all routing-table ad-route 0005.0004.0003.0002.0001:4294967295
   
    BGP local router ID : 1.1.1.1                          
    Local AS number : 100                                  
    Total routes of Route Distinguisher(3.3.3.3:0): 1      
    BGP routing table entry information of 0005.0004.0003.0002.0001:4294967295:    
    From: 2001:DB8:3::3 (3.3.3.3)                          
    Route Duration: 0d00h33m11s                            
    Relay IP Nexthop: FE80::3AC2:67FF:FE41:305             
    Relay IP Out-Interface:GigabitEthernet0/2/0                   
    Relay Tunnel Out-Interface:                            
    Original nexthop: 2001:DB8:3::3                        
    Qos information : 0x0                                  
    Ext-Community: RT <2 : 2>, SoO <3.3.3.3 : 0>, ESI Label<1 : 0 : 48067>    
    Prefix-sid: 2001:DB8:21::1:0:20, Endpoint Behavior: 23                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0005.0004.0003.0002.0001, Ethernet Tag ID: 4294967295                     
    Not advertised to any peer yet                         
   
   
    EVPN-Instance evrf2:                                   
    Number of A-D Routes: 1                                
    BGP routing table entry information of 0005.0004.0003.0002.0001:4294967295:    
    Route Distinguisher: 3.3.3.3:0                         
    Remote-Cross route                                     
    From: 2001:DB8:3::3 (3.3.3.3)                          
    Route Duration: 0d00h33m11s                            
    Relay IP Nexthop: FE80::3AC2:67FF:FE41:305             
    Relay IP Out-Interface:GigabitEthernet0/2/0                   
    Relay Tunnel Out-Interface:                            
    Original nexthop: 2001:DB8:3::3                        
    Qos information : 0x0                                  
    Ext-Community: RT <2 : 2>, SoO <3.3.3.3 : 0>, ESI Label<1 : 0 : 48067>    
    Prefix-sid: 2001:DB8:21::1:0:20, Endpoint Behavior: 23                                        
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 10                     
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)    
    ESI: 0005.0004.0003.0002.0001, Ethernet Tag ID: 4294967295                     
    Not advertised to any peer yet      
   ```
   
   Check that CE1 can ping CE2 and CE3. For example:
   
   ```
   [~CE1] ping 10.1.1.2                                     
     PING 10.1.1.2: 56  data bytes, press CTRL_C to break  
       Reply from 10.1.1.2: bytes=56 Sequence=1 ttl=255 time=224 ms                
       Reply from 10.1.1.2: bytes=56 Sequence=2 ttl=255 time=10 ms                 
       Reply from 10.1.1.2: bytes=56 Sequence=3 ttl=255 time=10 ms                 
       Reply from 10.1.1.2: bytes=56 Sequence=4 ttl=255 time=9 ms                  
       Reply from 10.1.1.2: bytes=56 Sequence=5 ttl=255 time=10 ms                 
   
     --- 10.1.1.2 ping statistics ---                      
       5 packet(s) transmitted                             
       5 packet(s) received                                
       0.00% packet loss                                   
       round-trip min/avg/max = 9/52/224 ms   
   ```
   ```
   [~CE1] ping 10.2.1.2                                     
     PING 10.2.1.2: 56  data bytes, press CTRL_C to break  
       Reply from 10.2.1.2: bytes=56 Sequence=1 ttl=255 time=12 ms                 
       Reply from 10.2.1.2: bytes=56 Sequence=2 ttl=255 time=10 ms                 
       Reply from 10.2.1.2: bytes=56 Sequence=3 ttl=255 time=7 ms                  
       Reply from 10.2.1.2: bytes=56 Sequence=4 ttl=255 time=11 ms                 
       Reply from 10.2.1.2: bytes=56 Sequence=5 ttl=255 time=7 ms                  
   
     --- 10.2.1.2 ping statistics ---                      
       5 packet(s) transmitted                             
       5 packet(s) received                                
       0.00% packet loss                                   
       round-trip min/avg/max = 7/9/12 ms  
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
   segment-routing ipv6 locator PE1_BUM
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 200:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE1_BUM 
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:1::1
   locator PE1_BUM ipv6-prefix 2001:DB8:12:: 64 args 10
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1_BUM auto-sid-disable 
   #              
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
  # 
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/3/0.2 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack1
   ipv6 enable    
   ip address 1.1.1.1 255.255.255.255
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
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
  lacp e-trunk system-id 00e0-fc12-3456
  #
  evpn
   #  
   mac-duplication 
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode all-active
   #
   esi 0005.0004.0003.0002.0001
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 300:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE2_BUM
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 400:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE2_BUM 
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  e-trunk 1
   priority 10
   peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   security-key cipher %^%#VQE;E!Dl&Rr]if$F>}w9uk5C>y-4|MS$unQ!#Mb#%^%#
  #
  e-trunk 2
   priority 10
   peer-ipv6 2001:DB8:3::3 source-ipv6 2001:DB8:2::2
   security-key cipher %^%#F&zi0c6x_2+SrLT_nm4,vfS$SCd]G:r~A_T!C>A$%^%#
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:2::2
   locator PE2_BUM ipv6-prefix 2001:DB8:22:: 64 args 10
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2_BUM auto-sid-disable 
   #              
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   mode lacp-static
   e-trunk 2
   esi 0005.0004.0003.0002.0001
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
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
   ipv6 address 2001:DB8:30::1/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   eth-trunk 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 20
  #
  interface LoopBack1
   ipv6 enable    
   ip address 2.2.2.2 255.255.255.255
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 advertise encap-type srv6
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
  lacp e-trunk system-id 00e0-fc12-3456
  #
  evpn
   #  
   mac-duplication 
   #
   esi 0001.0002.0003.0004.0005
    evpn redundancy-mode all-active
   #
   esi 0005.0004.0003.0002.0001
    evpn redundancy-mode single-active
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 500:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE3_BUM
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 600:1
   segment-routing ipv6 best-effort
   segment-routing ipv6 locator PE3_BUM 
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  e-trunk 1
   priority 10
   peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   security-key cipher %^%#!8C!"bAoc~O}UW2)%$HP4%.G9179.;&Yr[GmV.PN%^%# 
  #
  e-trunk 2
   priority 10
   peer-ipv6 2001:DB8:2::2 source-ipv6 2001:DB8:3::3
   security-key cipher %^%#GAG\Y-F%GY[GnwCkov7A<e(m/cl}m86`jd6z[79~%^%#
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:3::3
   locator PE3_BUM ipv6-prefix 2001:DB8:32:: 64 args 10
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE3_BUM auto-sid-disable 
   #              
  #
  interface Eth-Trunk10
   mode lacp-static
   e-trunk 1
   e-trunk mode force-master
   esi 0001.0002.0003.0004.0005
  #
  interface Eth-Trunk10.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface Eth-Trunk20
   mode lacp-static
   e-trunk 2
   esi 0005.0004.0003.0002.0001
  #
  interface Eth-Trunk20.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  # 
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable    
   ipv6 address 2001:DB8:30::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   eth-trunk 20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   eth-trunk 10
  #
  interface LoopBack1
   ipv6 enable    
   ip address 3.3.3.3 255.255.255.255
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 3.3.3.3
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   peer 2001:DB8:2::2 as-number 100
   peer 2001:DB8:2::2 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 advertise encap-type srv6
    peer 2001:DB8:2::2 enable
    peer 2001:DB8:2::2 advertise encap-type srv6
  #
  evpn source-address 3.3.3.3
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
   vlan-type dot1q 10   
   ip address 10.1.1.1 255.255.255.0 
  # 
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 20    
   ip address 10.2.1.1 255.255.255.0 
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  vlan 10
   trunk multicast load-balance enable
  #
  interface Eth-Trunk10
   mode lacp-static
  #
  interface Eth-Trunk10.1
   vlan-type dot1q 10             
   ip address 10.1.1.2 255.255.255.0
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
* CE3 configuration file
  ```
  #
  sysname CE3
  #
  interface Eth-Trunk20
   mode lacp-static
  #
  interface Eth-Trunk20.1
   vlan-type dot1q 20             
   ip address 10.2.1.2 255.255.255.0
  #   
  interface GigabitEthernet0/1/0 
   undo shutdown
   eth-trunk 20
  #                                  
  interface GigabitEthernet0/2/0 
   undo shutdown
   eth-trunk 20
  #
  return
  ```