Example for Configuring APN ID Isolation in an EVPN L3VPNv6 over SRv6 TE Policy Scenario
========================================================================================

This section provides an example of configuring APN ID isolation in an EVPN L3VPNv6 over SRv6 TE Policy scenario.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001247813226__fig3691666259), PE1, the P, and PE2 belong to the same AS and need to run IS-IS to implement IPv6 network connectivity. Establish a bidirectional SRv6 TE Policy between PE1 and PE2 to transport EVPN L3VPNv6 services. After receiving service flows from a CE, each PE is required to match them against the APN isolation policy, isolating the ones that conform to the policy.

**Figure 1** EVPN L3VPNv6 over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001247653504.png)

#### Configuration Precautions

1. SRv6 TE Policy configuration requires End or End.X SIDs. The SIDs can be either configured manually or generated dynamically using an IGP. In scenarios where SRv6 TE Policies are configured manually, dynamic SIDs used for the SRv6 TE Policies may change after an IGP restart. In this case, you need to manually adjust the SRv6 TE Policies so that they remain up. For this reason, dynamic SIDs are not suitable for large-scale use. You are therefore advised to configure SIDs manually and not to use dynamic SIDs.
2. In APN ID-based traffic steering, the headend recurses traffic based on the next hop of the corresponding route in compliance with the configured tunnel policy. If traffic recursion to an SRv6 TE flow group is configured, the headend matches the traffic with an SRv6 mapping policy based on the color attribute. If an SRv6 mapping policy is matched, the headend dynamically generates an SRv6 TE flow group that contains multiple SRv6 TE Policies with the same endpoint but different color values. Otherwise, the headend does not dynamically create an SRv6 TE flow group.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure an IPv6 address for each interface on PE1, the P, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, the P, and PE2.
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish a BGP EVPN peer relationship between the PEs.
6. Configure SRv6 SIDs and enable IS-IS SRv6 on PE1, the P, and PE2. In addition, configure PE1 and PE2 to advertise VPN routes carrying SIDs.
7. Deploy an SRv6 TE Policy on PE1 and PE2.
8. Configure a service flow filtering policy on PE1 and PE2 to ensure that APN IDs are generated for permitted service flows based on the specified generation mode.
9. Configure and apply an APN ID isolation policy on PE1 and PE2.
10. Configure APN IDs for service flows on PE1 and PE2.
11. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.

#### Data Preparation

To complete the configuration, you need the following data.

* IPv6 address of each interface on PE1, the P, and PE2
* IS-IS process ID of PE1, the P, and PE2
* IS-IS level for PE1, the P, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure PE1. The configurations of the P and PE2 are similar to the configuration of PE1. For detailed configurations, see the configuration files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/1/0
   [~PE1-GigabitEthernet0/1/0] ipv6 enable
   [*PE1-GigabitEthernet0/1/0] ipv6 address 2001:DB8:10::1 64
   [*PE1-GigabitEthernet0/1/0] quit
   [*PE1] interface LoopBack 1
   [*PE1-LoopBack1] ipv6 enable
   [*PE1-LoopBack1] ipv6 address 2001:DB8:1::1 128
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
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
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
   [*P-LoopBack1] quit
   ```
   ```
   [*P] commit
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
   [*PE2] interface loopback1
   ```
   ```
   [*PE2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   After completing the configuration, check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface         Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/1/0           0000.0000.0002.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
3. Configure an EVPN L3VPN instance on each PE and bind the EVPN L3VPN instance to an access-side interface.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] vpn-target 1:1 evpn
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:11::1 64
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
   [*PE2-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv6] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv6] vpn-target 1:1 evpn
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv6] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ipv6 address 2001:DB8:22::1 64
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-LoopBack1] ipv6 enable
   ```
   ```
   [*CE1-LoopBack1] ipv6 address 2001:DB8:111::111 128
   ```
   ```
   [*CE1-LoopBack1] quit
   ```
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] router-id 10.11.1.1
   ```
   ```
   [*CE1-bgp] peer 2001:DB8:11::1 as-number 100
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
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] router-id 1.1.1.1
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-6-vpna] peer 2001:DB8:11::2 as-number 65410
   ```
   ```
   [*PE1-bgp-6-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-6-vpna] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-6-vpna] commit
   ```
   ```
   [~PE1-bgp-6-vpna] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface loopback 1
   ```
   ```
   [*CE2-LoopBack1] ipv6 enable
   ```
   ```
   [*CE2-LoopBack1] ipv6 address 2001:DB8:222::222 128
   ```
   ```
   [*CE2-LoopBack1] quit
   ```
   ```
   [*CE2] bgp 65420
   ```
   ```
   [*CE2-bgp] router-id 10.22.2.2
   ```
   ```
   [*CE2-bgp] peer 2001:DB8:22::1 as-number 100
   ```
   ```
   [*CE2-bgp] ipv6-family unicast
   ```
   ```
   [*CE2-bgp-af-ipv6] peer 2001:DB8:22::1 enable
   ```
   ```
   [*CE2-bgp-af-ipv6] import-route direct
   ```
   ```
   [*CE2-bgp-af-ipv6] quit
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
   [~PE2-bgp] router-id 3.3.3.3
   ```
   ```
   [*PE2-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-6-vpna] peer 2001:DB8:22::2 as-number 65420
   ```
   ```
   [*PE2-bgp-6-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-6-vpna] advertise l2vpn evpn
   ```
   ```
   [*PE2-bgp-6-vpna] commit
   ```
   ```
   [~PE2-bgp-6-vpna] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After completing the configuration, run the **display bgp vpnv6 vpn-instance peer** command on each PE to check whether a BGP peer relationship has been established between the PE and its connected CE. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully.
   
   The following example uses the command output on PE1 to show that a relationship has been established between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv6 vpn-instance vpna peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     VPN-Instance vpna, Router ID 1.1.1.1:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:11::2  4       65410      131      132     0 01:51:37 Established        2
   ```
5. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:3::3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
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
   [~PE2-bgp] peer 2001:DB8:1::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:DB8:1::1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 enable
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configuration, run the **display bgp evpn peer** command on the PEs to check whether a BGP EVPN peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:3::3                    4         100       40       40     0 00:30:41 Established        2
   ```
6. Configure SRv6 SIDs and configure the PEs to advertise VPN routes carrying SIDs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:DB8:1::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
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
   [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-6-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE1-bgp-6-vpna] segment-routing ipv6 locator PE1 evpn
   ```
   ```
   [*PE1-bgp-6-vpna] commit
   ```
   ```
   [~PE1-bgp-6-vpna] quit
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
   
   # Configure the P.
   
   ```
   [~P] segment-routing ipv6
   ```
   ```
   [*P-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P-segment-routing-ipv6] locator P ipv6-prefix 2001:DB8:120:: 64 static 32
   ```
   ```
   [*P-segment-routing-ipv6-locator] opcode ::20 end psp
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
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::30 end psp
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
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 advertise encap-type srv6
   ```
   ```
   [*PE2-bgp-af-evpn] quit
   ```
   ```
   [*PE2-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-6-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE2-bgp-6-vpna] segment-routing ipv6 locator PE2 evpn
   ```
   ```
   [*PE2-bgp-6-vpna] commit
   ```
   ```
   [~PE2-bgp-6-vpna] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   ```
   [~PE2] isis 1
   ```
   ```
   [~PE2-isis-1] segment-routing ipv6 locator PE2 auto-sid-disable
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   
   Run the **display segment-routing ipv6 local-sid** **end forwarding** command to check information about the SRv6 local SID table.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:100::10/128                         FuncType : End
   Flavor      : PSP
   LocatorName : PE1                                          LocatorID: 1
   ProtocolType: STATIC                                       ProcessID: --
   UpdateTime  : 2021-08-30 01:46:05.713
   
   Total SID(s): 1
   ```
   ```
   [~PE2] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:130::30/128                         FuncType : End
   Flavor      : PSP
   LocatorName : PE2                                          LocatorID: 1
   ProtocolType: STATIC                                       ProcessID: --
   UpdateTime  : 2021-08-30 01:47:26.426
   
   Total SID(s): 1
   ```
   ```
   [~P] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:120::20/128                         FuncType : End
   Flavor      : PSP
   LocatorName : P                                            LocatorID: 1
   ProtocolType: STATIC                                       ProcessID: --
   UpdateTime  : 2021-08-30 01:49:44.292
   
   Total SID(s): 1
   ```
7. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1 
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:130::30
   [*PE1-segment-routing-ipv6-segment-list-list1] commit
   [~PE1-segment-routing-ipv6-segment-list-list1] quit
   [~PE1-segment-routing-ipv6] srv6-te-policy locator PE1 
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:100::450
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
   [*PE2-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE2-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:100::10
   [*PE2-segment-routing-ipv6-segment-list-list1] commit
   [~PE2-segment-routing-ipv6-segment-list-list1] quit
   [~PE2-segment-routing-ipv6] srv6-te-policy locator PE2 
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] binding-sid 2001:DB8:130::350
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 
   [*PE2-segment-routing-ipv6-policy-policy1-path] commit
   [~PE2-segment-routing-ipv6-policy-policy1-path] quit
   [~PE2-segment-routing-ipv6-policy-policy1] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After completing the configuration, run the **display srv6-te policy** command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy 
   PolicyName : policy1
   Color                   : 101                            Endpoint             : 2001:DB8:3::3
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -
   Policy State            : Up                             State Change Time    : 2019-03-24 19:45:30
   Admin State             : Up                             Traffic Statistics   : Disable
   Backup Hot-Standby      : Disable                        BFD                  : Disable
   Interface Index         : -                              Interface Name       : - 
   Interface State         : -                              Encapsulation Mode   : Insert
   Binding SID             : 2001:DB8:100::450(Insert, Preferred)
   Candidate-path Count    : 1
   
    Candidate-path Preference : 100
    Path State             : Active                         Path Type            : Primary
    Protocol-Origin        : Configuration(30)              Originator           : 0, 0.0.0.0
    Discriminator          : 100                            Binding SID          : 2001:DB8:100::450
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
            2001:DB8:120::20
            2001:DB8:130::30
   ```
8. Configure an APN6 instance.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] apn 
   [*PE1-apn] ipv6 
   [*PE1-apn-ipv6] apn-id template tmplt1 length 64 app-group 32 user-group 32 
   [*PE1-apn-ipv6-template-tmplt1] app-group index 1 app-group1 length 10
   [*PE1-apn-ipv6-template-tmplt1] user-group index 1 user-group1 length 8
   [*PE1-apn-ipv6-template-tmplt1] quit 
   [*PE1-apn-ipv6] apn-id instance inst1 
   [*PE1-apn-ipv6-instance-inst1] template tmplt1 
   [*PE1-apn-ipv6-instance-inst1] apn-field app-group1 301 
   [*PE1-apn-ipv6-instance-inst1] apn-field user-group1 201
   [*PE1-apn-ipv6-instance-inst1] quit 
   [*PE1-apn-ipv6] quit 
   [*PE1-apn] quit
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] apn 
   [*PE2-apn] ipv6 
   [*PE2-apn-ipv6] apn-id template tmplt1 length 64 app-group 32 user-group 32 
   [*PE2-apn-ipv6-template-tmplt1] app-group index 1 app-group1 length 10
   [*PE2-apn-ipv6-template-tmplt1] user-group index 1 user-group1 length 8
   [*PE2-apn-ipv6-template-tmplt1] quit 
   [*PE2-apn-ipv6] apn-id instance inst1 
   [*PE2-apn-ipv6-instance-inst1] template tmplt1 
   [*PE2-apn-ipv6-instance-inst1] apn-field app-group1 301 
   [*PE2-apn-ipv6-instance-inst1] apn-field user-group1 201
   [*PE2-apn-ipv6-instance-inst1] quit 
   [*PE2-apn-ipv6] quit 
   [*PE2-apn] quit
   [*PE2] commit
   ```
   
   
   
   Run the **display apn-id-ipv6 instance** command to check APN6 instance information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display apn-id-ipv6 instance name inst1
   Instance Name        : inst1
   Instance ID          : 1                    APN ID Length : 64
   APN ID               : 0x4b400000 0xc9000000
   APN Mask             : 0xffc00000 0xff000000
   ```
9. Configure and apply an APN ID isolation policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] apn 
   [*PE1-apn] ipv6 
   [*PE1-apn-ipv6] isolate-group name group10
   [*PE1-apn-ipv6] apn-id isolate policy policy1
   [*PE1-apn-ipv6-isolate-policy-policy1] index 1 instance inst1 isolate-group group10 behavior deny
   [*PE1-apn-ipv6-isolate-policy-policy1] quit 
   [*PE1-apn-ipv6] isolate-group mapping-vpn
   [*PE1-apn-ipv6-isolate-group-mapping-vpn] vpn-instance vpna peer-locator 2001:DB8:130:: 64 match isolate-group group10
   [*PE1-apn-ipv6-isolate-group-mapping-vpn] quit 
   [*PE1-apn-ipv6] quit 
   [*PE1-apn] quit
   [*PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] apn-id-ipv6 isolate-policy policy1 inbound 
   [*PE1-vpn-instance-vpna] quit 
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] apn 
   [*PE2-apn] ipv6 
   [*PE2-apn-ipv6] isolate-group name group10
   [*PE2-apn-ipv6] apn-id isolate policy policy1
   [*PE2-apn-ipv6-isolate-policy-policy1] index 1 instance inst1 isolate-group group10 behavior deny
   [*PE2-apn-ipv6-isolate-policy-policy1] quit 
   [*PE2-apn-ipv6] isolate-group mapping-vpn
   [*PE2-apn-ipv6-isolate-group-mapping-vpn] vpn-instance vpna peer-locator 2001:DB8:100:: 64 match isolate-group group10
   [*PE2-apn-ipv6-isolate-group-mapping-vpn] quit 
   [*PE2-apn-ipv6] quit 
   [*PE2-apn] quit
   [*PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] apn-id-ipv6 isolate-policy policy1 inbound 
   [*PE2-vpn-instance-vpna] quit 
   [*PE2] commit
   ```
10. Configure a service flow filtering policy to ensure that APN IDs are generated for permitted service flows based on the specified generation mode. If APN IDs are encapsulated in packets by terminals, skip this step.
    
    # Configure PE1.
    ```
    [~PE1] acl ipv6 number 3333
    [*PE1-acl6-advance-3333] rule 5 permit ipv6 source 2008:db8:111::111 1 destination 2008:db8:222::222 1
    [*PE1-acl6-advance-3333] commit
    [~PE1-acl6-advance-3333] quit
    [~PE1] traffic classifier c1
    [*PE1-classifier-c1] if-match ipv6 acl 3333
    [*PE1-classifier-c1] commit
    [~PE1-classifier-c1] quit
    [~PE1] traffic behavior b1
    [*PE1-behavior-b1] remark apn-id-ipv6 instance inst1 
    [*PE1-behavior-b1] commit
    [~PE1-behavior-b1] quit
    [~PE1] traffic policy p1
    [*PE1-trafficpolicy-p1] classifier c1 behavior b1
    [*PE1-trafficpolicy-p1] share-mode
    [*PE1-trafficpolicy-p1] statistics enable
    [*PE1-trafficpolicy-p1] quit
    [*PE1] interface GigabitEthernet 0/2/0
    [*PE1-GigabitEthernet0/2/0] traffic-policy p1 inbound
    [*PE1-GigabitEthernet0/2/0] commit
    [~PE1-GigabitEthernet0/2/0] quit
    ```
    
    
    # Configure PE2.
    ```
    [~PE2] acl ipv6 number 3333
    [*PE2-acl6-advance-3333] rule 5 permit ipv6 source 2008:db8:222::222 0 destination 2008:db8:111::111 0
    [*PE2-acl6-advance-3333] commit
    [~PE2-acl6-advance-3333] quit
    [~PE2] traffic classifier c1
    [*PE2-classifier-c1] if-match ipv6 acl 3333
    [*PE2-classifier-c1] commit
    [~PE2-classifier-c1] quit
    [~PE2] traffic behavior b1
    [*PE2-behavior-b1] remark apn-id-ipv6 instance inst1
    [*PE2-behavior-b1] commit
    [~PE2-behavior-b1] quit
    [~PE2] traffic policy p1
    [*PE2-trafficpolicy-p1] classifier c1 behavior b1
    [*PE2-trafficpolicy-p1] share-mode
    [*PE2-trafficpolicy-p1] statistics enable
    [*PE2-trafficpolicy-p1] quit
    [*PE2] interface GigabitEthernet 0/2/0
    [*PE2-GigabitEthernet0/2/0] traffic-policy p1 inbound
    [*PE2-GigabitEthernet0/2/0] commit
    [~PE2-GigabitEthernet0/2/0] quit
    ```
11. Configure a tunnel policy to import VPN traffic.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] route-policy p1 permit node 10
    [*PE1-route-policy] apply extcommunity color 0:101
    [*PE1-route-policy] quit
    [*PE1] bgp 100
    [*PE1-bgp] l2vpn-family evpn
    [*PE1-bgp-af-evpn] peer 2001:DB8:3::3 route-policy p1 import 
    [*PE1-bgp-af-evpn] quit
    [*PE1-bgp] quit
    [*PE1] tunnel-policy p1
    [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
    [*PE1-tunnel-policy-p1] quit
    [*PE1] ip vpn-instance vpna
    [*PE1-vpn-instance-vpna] ipv6-family
    [*PE1-vpn-instance-vpna-af-ipv6] tnl-policy p1 evpn
    [*PE1-vpn-instance-vpna-af-ipv6] commit
    [~PE1-vpn-instance-vpna-af-ipv6] quit
    [~PE1-vpn-instance-vpna] quit
    ```
    
    
    
    # Configure PE2.
    
    ```
    [~PE2] route-policy p1 permit node 10
    [*PE2-route-policy] apply extcommunity color 0:101
    [*PE2-route-policy] quit
    [*PE2] bgp 100
    [*PE2-bgp] l2vpn-family evpn
    [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 route-policy p1 import 
    [*PE2-bgp-af-evpn] quit
    [*PE2-bgp] quit
    [*PE2] tunnel-policy p1
    [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
    [*PE2-tunnel-policy-p1] quit
    [*PE2] ip vpn-instance vpna
    [*PE2-vpn-instance-vpna] ipv6-family
    [*PE2-vpn-instance-vpna-af-ipv6] tnl-policy p1 evpn
    [*PE2-vpn-instance-vpna-af-ipv6] commit
    [~PE2-vpn-instance-vpna-af-ipv6] quit
    [~PE2-vpn-instance-vpna] quit
    ```
    
    After completing the configuration, run the **display ipv6 routing-table vpn-instance vpna** command to check that the VPN route has successfully recursed to the SRv6 TE Policy.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display ipv6 routing-table vpn-instance vpna
    Routing Table : vpna
             Destinations : 6        Routes : 6         
    
    Destination  : 2001:DB8:111::111                       PrefixLength : 128
    NextHop      : 2001:DB8:11::2                          Preference   : 255
    Cost         : 0                                       Protocol     : EBGP
    RelayNextHop : 2001:DB8:11::2                          TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : RD
    
    Destination  : 2001:DB8:222::222                       PrefixLength : 128
    NextHop      : 2001:DB8:3::3                           Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : ::                                      TunnelID     : 0x000000003400000001
    Interface    : policy1                                Flags        : RD
    
    Destination  : 2001:DB8:11::                           PrefixLength : 64
    NextHop      : 2001:DB8:11::1                          Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
    
    Destination  : 2001:DB8:11::1                          PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
    
    Destination  : 2001:DB8:22::                           PrefixLength : 64
    NextHop      : 2001:DB8:3::3                           Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : ::                                      TunnelID     : 0x000000003400000001
    Interface    : policy1                                Flags        : RD
    
    Destination  : FE80::                                  PrefixLength : 10
    NextHop      : ::                                      Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : NULL0                                   Flags        : DB
    ```
    ```
    [~PE1] display ipv6 routing-table vpn-instance vpna 2001:DB8:222::222 verbose 
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpna
    Summary Count : 1
    
    Destination  : 2001:DB8:222::222                       PrefixLength : 128
    NextHop      : 2001:DB8:3::3                           Preference   : 255
    Neighbour    : 2001:DB8:3::3                           ProcessID    : 0
    Label        : NULL                                    Protocol     : IBGP
    State        : Active Adv Relied                       Cost         : 0
    Entry ID     : 0                                       EntryFlags   : 0x00000000
    Reference Cnt: 0                                       Tag          : 0
    Priority     : low                                     Age          : 1867sec
    IndirectID   : 0x10000DC                               Instance     : 
    RelayNextHop : ::                                      TunnelID     : 0x000000003400000001
    Interface    : policy1                                Flags        : RD
    ```
12. Verify the configuration.
    
    
    
    Check that the CEs belonging to the same VPN instance can ping each other. For example:
    
    ```
    [~CE1] ping ipv6 -a 2001:DB8:111::111 2001:DB8:222::222
      PING 2001:DB8:222::222 : 56  data bytes, press CTRL_C to break
        Reply from 2001:DB8:222::222 
        bytes=56 Sequence=1 hop limit=62 time=148 ms
        Reply from 2001:DB8:222::222 
        bytes=56 Sequence=2 hop limit=62 time=31 ms
        Reply from 2001:DB8:222::222 
        bytes=56 Sequence=3 hop limit=62 time=46 ms
        Reply from 2001:DB8:222::222 
        bytes=56 Sequence=4 hop limit=62 time=28 ms
        Reply from 2001:DB8:222::222 
        bytes=56 Sequence=5 hop limit=62 time=26 ms
    
      --- 2001:DB8:222::222 ping statistics---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
    ```
    
    Check the traffic statistics of policy1 used by vpna.
    
    ```
    <PE1> display apn-id-ipv6 isolate-policy statistics policy policy1 vpn-instance vpna 
    Vpn-Instance           : vpna
    Isolate-Policy inbound : policy1
    Item                   Packets                    Bytes
    -------------------------------------------------------------------
    Matched                1                          1
    Last 300 seconds rate
    Item                   pps                        bps
    -------------------------------------------------------------------
    Matched                1                          1
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  sysname PE1
  #
  apn
   ipv6
    apn-id template tmplt1 length 64 app-group 32 user-group 32
     app-group index 1 app-group1 length 10
     user-group index 1 user-group1 length 8
    apn-id instance inst1
     template tmplt1
     apn-field app-group1 301
     apn-field user-group1 201
    isolate-group name group10
    apn-id isolate policy policy1
     statistics enable
     index 1 instance inst1 isolate-group group10 behavior deny
    isolate-group mapping-vpn   
     vpn-instance vpna peer-locator 2001:DB8:130:: 64 match isolate-group group10
  #
   acl ipv6 number 3333
   rule 5 permit ipv6 source 2008:db8:111::111 1 destination 2008:db8:222::222 1
  #
  traffic classifier c1
   if-match ipv6 acl 3333
  #
  traffic behavior b1
   remark apn-id-ipv6 instance inst1
  #
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn
   apn-id-ipv6 isolate-policy policy1 inbound
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::10 end psp
   srv6-te-policy locator PE1
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:130::30
   srv6-te policy policy1 endpoint 2001:DB8:3::3 color 101
    binding-sid 2001:DB8:100::450
    candidate-path preference 100
     segment-list list1
   mapping-policy p1 color 101
    match-type apn-id-ipv6
     index 1 instance inst1 match srv6-te-policy color 101
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE1 auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   isis ipv6 enable 1
   undo dcn
   undo dcn mode vlan
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ipv6 enable
   ipv6 address 2001:DB8:11::1/64
   traffic-policy p1 inbound
   undo dcn
   undo dcn mode vlan
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 1.1.1.1
   private-4-byte-as enable
   peer 2001:DB8:3::3 as-number 100
   peer 2001:DB8:3::3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv6-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 2001:DB8:11::2 as-number 65410
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:3::3 enable
    peer 2001:DB8:3::3 route-policy p1 import
    peer 2001:DB8:3::3 advertise encap-type srv6
  #
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #
  return
  ```
* P configuration file
  
  ```
  sysname P
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator P ipv6-prefix 2001:DB8:120:: 64 static 32
    opcode ::20 end psp
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P auto-sid-disable
   #              
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
   ipv6 address 2001:DB8:20::1/64
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* PE2 configuration file
  
  ```
  sysname PE2
  #
  apn
   ipv6
    apn-id template tmplt1 length 64 app-group 32 user-group 32
     app-group index 1 app-group1 length 10
     user-group index 1 user-group1 length 8
    apn-id instance inst1
     template tmplt1
     apn-field app-group1 301
     apn-field user-group1 201
    isolate-group name group10
    apn-id isolate policy policy1
     statistics enable
     index 1 instance inst1 isolate-group group10 behavior deny
    isolate-group mapping-vpn   
     vpn-instance vpna peer-locator 2001:DB8:100:: 64 match isolate-group group10
  #
  acl ipv6 number 3333
   rule 5 permit ipv6 source 2008:db8:222::222 0 destination 2008:db8:111::111 0
  #
  traffic classifier c1
   if-match ipv6 acl 3333
  #
  traffic behavior b1
   remark apn-id-ipv6 instance inst1
  #
  traffic policy p1
   share-mode
   statistics enable
   classifier c1 behavior b1
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn
   apn-id-ipv6 isolate-policy policy1 inbound
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator PE2 ipv6-prefix 2001:DB8:130:: 64 static 32
    opcode ::30 end psp
   srv6-te-policy locator PE2
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:100::10
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    binding-sid 2001:DB8:130::350
    candidate-path preference 100
     segment-list list1
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:20::2/64
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ipv6 enable
   ipv6 address 2001:DB8:22::1/64
   traffic-policy p1 inbound
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 3.3.3.3
   private-4-byte-as enable
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
   #
   ipv6-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE2 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 2001:DB8:22::2 as-number 65420
   #
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:1::1 enable
    peer 2001:DB8:1::1 route-policy p1 import
    peer 2001:DB8:1::1 advertise encap-type srv6
  #
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-flow-group load-balance-number 1
  #
  return
  ```
* CE1 configuration file
  
  ```
  sysname CE1
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:11::2/64             
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:111::111/128
  #               
  bgp 65410       
   router-id 10.11.1.1
   peer 2001:DB8:11::1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:DB8:11::1 enable
  #  
  return 
  ```
* CE2 configuration file
  
  ```
  sysname CE2
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:22::2/64
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:222::222/128
  #               
  bgp 65420       
   router-id 10.22.2.2
   peer 2001:DB8:22::1 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:DB8:22::1 enable
  #
  return
  ```