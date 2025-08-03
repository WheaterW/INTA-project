Example for Configuring EVPN L3VPNv4 over SRv6 TE Policy (Manual Configuration + UCMP Scenario)
===============================================================================================

This section provides an example for configuring an SRv6 TE Policy to carry EVPN L3VPNv4 services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000002030829457__fig3691666259), PEs and Ps are in the same AS and need to run IS-IS to implement IPv6 network connectivity.

Configure EVPN L3VPN services to recurse to SRv6 TE Policies to ensure secure communication between users in the same VPN. Because multiple links exist between the PEs, unequal-cost multiple path (UCMP) load balancing needs to be performed on these links.

**Figure 1** EVPN L3VPNv4 over SRv6 TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/8, respectively.


  
![](figure/en-us_image_0000002030987825.png)

**Table 1** 
| Device Name | Interface Number | Interface IP Address |
| --- | --- | --- |
| PE1 | GE0/1/0 | 10.1.1.2/24 |
| PE1 | GE0/2/0 | 2001:DB8:12::1/96 |
| PE1 | GE0/3/0 | 2001:DB8:13::1/96 |
| PE1 | GE0/1/8 | 2001:DB8:14::1/96 |
| PE2 | GE0/1/0 | 10.2.1.2/24 |
| PE2 | GE0/2/0 | 2001:DB8:22::1/96 |
| PE2 | GE0/3/0 | 2001:DB8:23::1/96 |
| PE2 | GE0/1/8 | 2001:DB8:24::1/96 |
| P1 | GE0/1/0 | 2001:DB8:12::2/96 |
| P1 | GE0/2/0 | 2001:DB8:22::2/96 |
| P2 | GE0/1/0 | 2001:DB8:13::2/96 |
| P2 | GE0/2/0 | 2001:DB8:23::2/96 |
| P3 | GE0/1/0 | 2001:DB8:14::2/96 |
| P3 | GE0/2/0 | 2001:DB8:24::2/96 |



#### Precautions

1. SRv6 TE Policy configuration requires End or End.X SIDs. The SIDs can either be configured manually or be generated dynamically using an IGP. In scenarios where SRv6 TE Policies are configured manually, dynamic SIDs used for the SRv6 TE Policies may change after an IGP restart. In this case, you need to manually adjust the SRv6 TE Policies so that they remain up. For this reason, dynamic SIDs are not suitable for large-scale use. You are therefore advised to configure SIDs manually and not to use dynamic SIDs.
2. To implement color-based traffic steering into SRv6 TE Policies, you need to configure the color attribute using an import or export route-policy. You also need to configure a tunnel policy to allow routes to recurse to SRv6 TE Policies.
   
   After the preceding configurations are complete, if the color and next hop of a route are the same as the color and endpoint of an SRv6 TE Policy, respectively, the route can successfully recurse to the SRv6 TE Policy. This enables the traffic forwarded through the route to be steered into the SRv6 TE Policy.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 forwarding and configure IPv6 addresses for interfaces on PE1, the Ps, and PE2.
2. Enable IS-IS, configure an IS-IS level, and specify a network entity title on PE1, the Ps, and PE2.
3. Configure an EVPN L3VPN instance on each PE and bind the instance to an access-side interface.
4. Establish an EBGP peer relationship between each PE and its connected CE.
5. Establish a BGP EVPN peer relationship between the PEs.
6. Configure SRv6 SIDs and IS-IS SRv6 on PE1, the Ps, and PE2. In addition, enable PE1 and PE2 to add the SID attribute to the VPN routes to be advertised.
7. Deploy an SRv6 TE Policy between PE1 and PE2. In addition, configure three segment lists for the candidate path of the policy, and configure weights 50, 30, and 20, respectively, for these segment lists so that they work in UCMP mode.
8. Configure a tunnel policy on PE1 and PE2 to import VPN traffic.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses of interfaces on PE1, the Ps, and PE2
* IS-IS process IDs of PE1, the Ps, and PE2
* IS-IS levels of PE1, the Ps, and PE2
* VPN instance names, RDs, and RTs on PE1 and PE2

#### Procedure

1. Enable IPv6 forwarding and configure IPv6 addresses for interfaces.
   
   
   
   # Configure PE1. The configurations of other devices are similar to the configuration of PE1. For detailed configurations, see Configuration Files.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname PE1
   [*HUAWEI] commit
   [~PE1] interface gigabitethernet 0/2/0
   [~PE1-GigabitEthernet0/2/0] ipv6 enable
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:DB8:12::1 96
   [*PE1-GigabitEthernet0/2/0] quit
   [~PE1] interface gigabitethernet 0/3/0
   [~PE1-GigabitEthernet0/3/0] ipv6 enable
   [*PE1-GigabitEthernet0/3/0] ipv6 address 2001:DB8:13::1 96
   [*PE1-GigabitEthernet0/3/0] quit
   [~PE1] interface gigabitethernet 0/1/8
   [~PE1-GigabitEthernet0/1/8] ipv6 enable
   [*PE1-GigabitEthernet0/1/8] ipv6 address 2001:DB8:14::1 96
   [*PE1-GigabitEthernet0/1/8] quit
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
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/8
   ```
   ```
   [*PE1-GigabitEthernet0/1/8] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/8] quit
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
   
   # Configure P1.
   
   ```
   [~P1] isis 1 
   ```
   ```
   [*P1-isis-1] is-level level-1
   ```
   ```
   [*P1-isis-1] cost-style wide
   ```
   ```
   [*P1-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P1-isis-1] quit
   ```
   ```
   [*P1] interface gigabitethernet 0/1/0
   ```
   ```
   [*P1-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P1] interface gigabitethernet 0/2/0
   ```
   ```
   [*P1-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P1] interface loopback1
   ```
   ```
   [*P1-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P1-LoopBack1] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure P2.
   
   ```
   [~P2] isis 1 
   ```
   ```
   [*P2-isis-1] is-level level-1
   ```
   ```
   [*P2-isis-1] cost-style wide
   ```
   ```
   [*P2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*P2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P2-isis-1] quit
   ```
   ```
   [*P2] interface gigabitethernet 0/1/0
   ```
   ```
   [*P2-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P2] interface gigabitethernet 0/2/0
   ```
   ```
   [*P2-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P2] interface loopback1
   ```
   ```
   [*P2-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P2-LoopBack1] quit
   ```
   ```
   [*P2] commit
   ```
   
   # Configure P3.
   
   ```
   [~P3] isis 1 
   ```
   ```
   [*P3-isis-1] is-level level-1
   ```
   ```
   [*P3-isis-1] cost-style wide
   ```
   ```
   [*P3-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*P3-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P3-isis-1] quit
   ```
   ```
   [*P3] interface gigabitethernet 0/1/0
   ```
   ```
   [*P3-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*P3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P3] interface gigabitethernet 0/2/0
   ```
   ```
   [*P3-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*P3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P3] interface loopback1
   ```
   ```
   [*P3-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*P3-LoopBack1] quit
   ```
   ```
   [*P3] commit
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
   [*PE2-isis-1] network-entity 10.0000.0000.0005.00
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
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
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
   [*PE2] interface gigabitethernet 0/1/8
   ```
   ```
   [*PE2-GigabitEthernet0/1/8] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/8] quit
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
   
   
   
   After completing the configurations, perform the following operations to check whether IS-IS is successfully configured.
   
   # Display IS-IS neighbor information. The following uses PE1 as an example.
   
   ```
   [~PE1] display isis peer
   ```
   ```
                             Peer information for ISIS(1)
                            
     System Id     Interface         Circuit Id        State HoldTime Type     PRI
   --------------------------------------------------------------------------------
   0000.0000.0002* GE0/2/0           0000.0000.0001.01  Up  29s       L1       64 
   0000.0000.0002* GE0/3/0           0000.0000.0001.02  Up  25s       L1       64 
   0000.0000.0002* GE0/1/8           0000.0000.0004.01  Up   8s       L1       64 
   
   Total Peer(s): 1
   ```
3. Configure an EVPN L3VPN instance on each PE and bind the instance to an access-side interface.
   
   
   
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
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
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
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.2 24
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
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
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
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.2 24
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
   [~CE1] interface gigabitethernet0/1/0
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*CE1] interface loopbacK 1
   ```
   ```
   [*CE1-LoopBack1] ip address 10.11.1.1 32
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
   [*CE1-bgp] peer 10.1.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] import-route direct
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
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 10.1.1.1 as-number 65410
   ```
   ```
   [*PE1-bgp-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-vpna] advertise l2vpn evpn
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
   [~CE2] interface gigabitethernet0/1/0
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] ip address 10.2.1.1 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [~CE2] interface loopback 1
   ```
   ```
   [*CE2-LoopBack1] ip address 10.22.2.2 32
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
   [*CE2-bgp] peer 10.2.1.2 as-number 100
   ```
   ```
   [*CE2-bgp] import-route direct
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
   [~PE2-bgp] router-id 5.5.5.5
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] peer 10.2.1.1 as-number 65420
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] advertise l2vpn evpn
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
   
   After completing the configurations, run the **display bgp vpnv4 vpn-instance peer** command on the PEs to check whether BGP peer relationships have been established between the PEs and CEs. The command output shows that the BGP peer relationships have been established between the PEs and CEs and are in the **Established** state.
   
   The following uses the peer relationship between PE1 and CE1 as an example.
   
   ```
   [~PE1] display bgp vpnv4 vpn-instance vpna peer
    BGP local router ID : 1.1.1.1                                                  
    Local AS number : 100      
   
    VPN-Instance vpna, Router ID 1.1.1.1:                                          
    Total number of peers : 1                 Peers in established state : 1       
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv          
     10.1.1.1        4       65410        9       10     0 00:39:40 Established        2 
   ```
5. Establish a BGP EVPN peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:DB8:5::5 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:DB8:5::5 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2001:DB8:5::5 enable
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
   
   After completing the configurations, run the **display bgp evpn peer** command on the PEs to check whether a BGP EVPN peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:5::5                    4         100       49       49     0 00:30:41 Established        2
   ```
6. Configure SRv6 SIDs and enable the PEs to add the SID attribute to the VPN routes to be advertised.
   
   
   
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
   [*PE1-bgp-af-evpn] peer 2001:DB8:5::5 advertise encap-type srv6
   ```
   ```
   [*PE1-bgp-af-evpn] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 locator PE1 evpn
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
   [~PE1-isis-1] segment-routing ipv6 locator PE1 auto-sid-disable
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] segment-routing ipv6
   ```
   ```
   [*P1-segment-routing-ipv6] encapsulation source-address 2001:DB8:2::2
   ```
   ```
   [*P1-segment-routing-ipv6] locator P1 ipv6-prefix 2001:DB8:120:: 64 static 32
   ```
   ```
   [*P1-segment-routing-ipv6-locator] opcode ::20 end psp
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
   
   # Configure P2.
   
   ```
   [~P2] segment-routing ipv6
   ```
   ```
   [*P2-segment-routing-ipv6] encapsulation source-address 2001:DB8:3::3
   ```
   ```
   [*P2-segment-routing-ipv6] locator P2 ipv6-prefix 2001:DB8:130:: 64 static 32
   ```
   ```
   [*P2-segment-routing-ipv6-locator] opcode ::30 end psp
   ```
   ```
   [*P2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P2-segment-routing-ipv6] quit
   ```
   ```
   [*P2] isis 1
   ```
   ```
   [*P2-isis-1] segment-routing ipv6 locator P2 auto-sid-disable
   ```
   ```
   [*P2-isis-1] commit
   ```
   ```
   [~P2-isis-1] quit
   ```
   
   # Configure P3.
   
   ```
   [~P3] segment-routing ipv6
   ```
   ```
   [*P3-segment-routing-ipv6] encapsulation source-address 2001:DB8:4::4
   ```
   ```
   [*P3-segment-routing-ipv6] locator P3 ipv6-prefix 2001:DB8:140:: 64 static 32
   ```
   ```
   [*P3-segment-routing-ipv6-locator] opcode ::40 end psp
   ```
   ```
   [*P3-segment-routing-ipv6-locator] quit
   ```
   ```
   [*P3-segment-routing-ipv6] quit
   ```
   ```
   [*P3] isis 1
   ```
   ```
   [*P3-isis-1] segment-routing ipv6 locator P3 auto-sid-disable
   ```
   ```
   [*P3-isis-1] commit
   ```
   ```
   [~P3-isis-1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:DB8:5::5
   ```
   ```
   [*PE2-segment-routing-ipv6] locator PE2 ipv6-prefix 2001:DB8:150:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::50 end psp
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
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 traffic-engineer best-effort evpn
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 locator PE2 evpn
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
   [~PE2-isis-1] segment-routing ipv6 locator PE2 auto-sid-disable
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   
   Run the [**display segment-routing ipv6 local-sid**](cmdqueryname=display+segment-routing+ipv6+local-sid) **end** **forwarding** command to check information about the SRv6 local SID table.
   
   The following uses PE1 as an example.
   
   ```
   [~PE1] display segment-routing ipv6 local-sid end forwarding
                       My Local-SID End Forwarding Table
                       ---------------------------------
   
   SID         : 2001:DB8:100::10/128                         FuncType    : End
   Flavor      : PSP                                          SidCompress : NO
   LocatorName : PE1                                          LocatorID   : 1
   ProtocolType: STATIC                                       ProcessID   : --
   UpdateTime  : 2021-08-30 01:46:05.713
   
   Total SID(s): 1
   ```
7. Configure an SRv6 TE Policy.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6 
   [~PE1-segment-routing-ipv6] segment-list list1
   [*PE1-segment-routing-ipv6-segment-list-list1] index 5 sid ipv6 2001:DB8:120::20
   [*PE1-segment-routing-ipv6-segment-list-list1] index 10 sid ipv6 2001:DB8:150::50
   [*PE1-segment-routing-ipv6-segment-list-list1] quit
   [*PE1-segment-routing-ipv6] segment-list list2
   [*PE1-segment-routing-ipv6-segment-list-list2] index 5 sid ipv6 2001:DB8:130::30
   [*PE1-segment-routing-ipv6-segment-list-list2] index 10 sid ipv6 2001:DB8:150::50
   [*PE1-segment-routing-ipv6-segment-list-list2] quit
   [*PE1-segment-routing-ipv6] segment-list list3
   [*PE1-segment-routing-ipv6-segment-list-list3] index 5 sid ipv6 2001:DB8:140::40
   [*PE1-segment-routing-ipv6-segment-list-list3] index 10 sid ipv6 2001:DB8:150::50
   [*PE1-segment-routing-ipv6-segment-list-list3] commit
   [~PE1-segment-routing-ipv6-segment-list-list3] quit
   [*PE1-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:5::5 color 101
   [*PE1-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list1 weight 50
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list2 weight 30
   [*PE1-segment-routing-ipv6-policy-policy1-path] segment-list list3 weight 20
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
   [*PE2-segment-routing-ipv6-segment-list-list1] quit
   [*PE2-segment-routing-ipv6] segment-list list2 
   [*PE2-segment-routing-ipv6-segment-list-list2] index 5 sid ipv6 2001:DB8:130::30
   [*PE2-segment-routing-ipv6-segment-list-list2] index 10 sid ipv6 2001:DB8:100::10
   [*PE2-segment-routing-ipv6-segment-list-list2] quit
   [*PE2-segment-routing-ipv6] segment-list list3 
   [*PE2-segment-routing-ipv6-segment-list-list3] index 5 sid ipv6 2001:DB8:140::40
   [*PE2-segment-routing-ipv6-segment-list-list3] index 10 sid ipv6 2001:DB8:100::10
   [*PE2-segment-routing-ipv6-segment-list-list3] commit
   [~PE2-segment-routing-ipv6-segment-list-list3] quit
   [*PE2-segment-routing-ipv6] srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
   [*PE2-segment-routing-ipv6-policy-policy1] candidate-path preference 100
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list1 weight 50 
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list2 weight 30
   [*PE2-segment-routing-ipv6-policy-policy1-path] segment-list list3 weight 20
   [*PE2-segment-routing-ipv6-policy-policy1-path] commit
   [~PE2-segment-routing-ipv6-policy-policy1-path] quit
   [~PE2-segment-routing-ipv6-policy-policy1] quit
   [~PE2-segment-routing-ipv6] quit
   ```
   
   After completing the configurations, run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) command to check SRv6 TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display srv6-te policy 
   PolicyName : policy1
   Color                   : 101                            Endpoint             : 2001:DB8:5::5
   TunnelId                : 1                              
   TunnelType              : SRv6-TE Policy                 DelayTimerRemain     : -
   Policy State            : Up                             State Change Time    : 2020-12-30 07:02:14
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
    GroupId                : 1                              Policy Name          : policy1
    Template ID            : 0                              Path Verification    : Disable
    DelayTimerRemain       : -                              Network Slice ID     : -
    Segment-List Count     : 3
     Segment-List          : list1
      Segment-List ID      : 1                              XcIndex              : 1  
      List State           : Up                             DelayTimerRemain     : -  
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600
      Weight               : 50                             BFD State            : - 
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding ID   : -
      SID :  
            2001:DB8:120::20
            2001:DB8:150::50
     Segment-List          : list2
      Segment-List ID      : 2                              XcIndex              : 2  
      List State           : Up                             DelayTimerRemain     : -  
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600
      Weight               : 3                              BFD State            : - 
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding ID   : -
      SID :  
            2001:DB8:130::30
            2001:DB8:150::50
     Segment-List          : list3
      Segment-List ID      : 3                              XcIndex              : 3  
      List State           : Up                             DelayTimerRemain     : -  
      Verification State   : -                              SuppressTimeRemain   : -
      PMTU                 : 9600                           Active PMTU          : 9600
      Weight               : 20                             BFD State            : - 
      Loop Detection State : Up                             BFD Delay Remain     : - 
      Network Slice ID     : -
      Binding SID          : -
      Reverse Binding ID   : -
      SID :  
            2001:DB8:140::40
            2001:DB8:150::50
   ```
8. Configure a tunnel policy to import VPN traffic.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy p1 permit node 10
   [*PE1-route-policy] apply extcommunity color 0:101
   [*PE1-route-policy] quit
   [*PE1] bgp 100
   [*PE1-bgp] l2vpn-family evpn
   [*PE1-bgp-af-evpn] peer 2001:DB8:5::5 route-policy p1 import 
   [*PE1-bgp-af-evpn] quit
   [*PE1-bgp] quit
   [*PE1] tunnel-policy p1
   [*PE1-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE1-tunnel-policy-p1] quit
   [*PE1] ip vpn-instance vpna
   [*PE1-vpn-instance-vpna] ipv4-family
   [*PE1-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
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
   [*PE2-bgp] l2vpn-family evpn
   [*PE2-bgp-af-evpn] peer 2001:DB8:1::1 route-policy p1 import 
   [*PE2-bgp-af-evpn] quit
   [*PE2-bgp] quit
   [*PE2] tunnel-policy p1
   [*PE2-tunnel-policy-p1] tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
   [*PE2-tunnel-policy-p1] quit
   [*PE2] ip vpn-instance vpna
   [*PE2-vpn-instance-vpna] ipv4-family
   [*PE2-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   [~PE2-vpn-instance-vpna] quit
   ```
   
   After completing the configurations, run the **display ip routing-table vpn-instance vpna** command to check the IPv4 routing table of the specified VPN instance. The command output shows that the VPN route has successfully recursed to the SRv6 TE Policy.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpna
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route                 
   ------------------------------------------------------------------------------  
   Routing Table : vpna        
            Destinations : 8        Routes : 8                                     
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface    
   
          10.1.1.0/24  Direct  0    0             D   10.1.1.2        GigabitEthernet0/1/0
          10.1.1.2/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
          10.2.1.0/24  IBGP    255  0             RD  2001:DB8:5::5   policy1 
         10.11.1.1/32  EBGP    255  0             RD  10.1.1.1        GigabitEthernet0/1/0
         10.22.2.2/32  IBGP    255  0             RD  2001:DB8:5::5   policy1  
         127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0  
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0  
   ```
   ```
   [~PE1] display ip routing-table vpn-instance vpna 10.22.2.2 verbose 
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route 
   ------------------------------------------------------------------------------  
   Routing Table : vpna        
   Summary Count : 1           
   
   Destination: 10.22.2.2/32    
        Protocol: IBGP               Process ID: 0                                 
      Preference: 255                      Cost: 0                                 
         NextHop: 2001:DB8:5::5       Neighbour: 2001:DB8:5::5                     
           State: Active Adv Relied         Age: 00h49m52s                         
             Tag: 0                    Priority: low                               
           Label: NULL                  QoSInfo: 0x0                               
      IndirectID: 0x10000DF            Instance:                                   
    RelayNextHop: ::                  Interface: policy1                    
        TunnelID: 0x000000003400000001    Flags: RD 
      RouteColor: 0 
   ```
9. Verify the configuration.
   
   
   
   Check that CEs belonging to the same VPN instance can ping each other. For example:
   
   ```
   [~CE1] ping -a 10.11.1.1 10.22.2.2                                                 
     PING 22.2.2.2: 56  data bytes, press CTRL_C to break                          
       Reply from 10.22.2.2: bytes=56 Sequence=1 ttl=253 time=32 ms                 
       Reply from 10.22.2.2: bytes=56 Sequence=2 ttl=253 time=24 ms                 
       Reply from 10.22.2.2: bytes=56 Sequence=3 ttl=253 time=27 ms                 
       Reply from 10.22.2.2: bytes=56 Sequence=4 ttl=253 time=35 ms                 
       Reply from 10.22.2.2: bytes=56 Sequence=5 ttl=253 time=28 ms                 
   
     --- 10.22.2.2 ping statistics ---                                              
       5 packet(s) transmitted 
       5 packet(s) received    
       0.00% packet loss       
       round-trip min/avg/max = 24/29/35 ms 
   ```
   
   
   
   Ping the SRv6 TE Policy from a PE. The command output shows that each segment list can be pinged.
   
   ```
   [~PE1]ping srv6-te policy  policy-name policy1
     PING srv6-te policy : 100  data bytes, press CTRL_C to break
     srv6-te policy's segment list:
     Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 1; Xcindex: 1
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=1 time=3 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=2 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=3 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=4 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=5 time=2 ms
   
     --- srv6-te policy ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/2/3 ms
   
     srv6-te policy's segment list:
     Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 2; Xcindex: 2
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=1 time=3 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=2 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=3 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=4 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=5 time=2 ms
   
     --- srv6-te policy ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/2/3 ms
   
     srv6-te policy's segment list:
     Preference: 100; Path Type: primary; Protocol-Origin: local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID: 3; Xcindex: 3
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=1 time=3 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=2 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=3 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=4 time=2 ms
       Reply from 2001:DB8:150::50
       bytes=100 Sequence=5 time=2 ms
   
     --- srv6-te policy ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/2/3 ms
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
    apply-label per-instance
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn      
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:1::1
   locator PE1 ipv6-prefix 2001:DB8:100:: 64 static 32
    opcode ::10 end psp
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:150::50
   segment-list list2
    index 5 sid ipv6 2001:DB8:130::30
    index 10 sid ipv6 2001:DB8:150::50
   segment-list list3
    index 5 sid ipv6 2001:DB8:140::40
    index 10 sid ipv6 2001:DB8:150::50
   srv6-te policy policy1 endpoint 2001:DB8:5::5 color 101
    candidate-path preference 100
     segment-list list1 weight 50
     segment-list list2 weight 30
     segment-list list3 weight 20
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
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::1/96
   isis ipv6 enable 1 
  #
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::1/96
   isis ipv6 enable 1 
  #    
  interface GigabitEthernet0/1/8
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::1/96
   isis ipv6 enable 1 
  #    
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:DB8:5::5 as-number 100
   peer 2001:DB8:5::5 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE1 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.1.1.1 as-number 65410
   #              
   l2vpn-family evpn
    policy vpn-target
    peer 2001:DB8:5::5 enable
    peer 2001:DB8:5::5 route-policy p1 import
    peer 2001:DB8:5::5 advertise encap-type srv6
  #               
  route-policy p1 permit node 10
   apply extcommunity color 0:101
  #               
  tunnel-policy p1
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return 
  ```
* P1 configuration file
  
  ```
  #
  sysname P1
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:2::2
   locator P1 ipv6-prefix 2001:DB8:120:: 64 static 32
    opcode ::20 end psp
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P1 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:12::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:22::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/128
   isis ipv6 enable 1
  #               
  return 
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:3::3
   locator P2 ipv6-prefix 2001:DB8:130:: 64 static 32
    opcode ::30 end psp
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P2 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:13::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:23::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:3::3/128
   isis ipv6 enable 1
  #               
  return 
  ```
* P3 configuration file
  
  ```
  #
  sysname P3
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:4::4
   locator P3 ipv6-prefix 2001:DB8:140:: 64 static 32
    opcode ::40 end psp
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator P3 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:14::2/96
   isis ipv6 enable 1
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:24::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:4::4/128
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
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn        
  #               
  segment-routing ipv6
   encapsulation source-address 2001:DB8:5::5
   locator PE2 ipv6-prefix 2001:DB8:150:: 64 static 32
    opcode ::50 end psp
   segment-list list1
    index 5 sid ipv6 2001:DB8:120::20
    index 10 sid ipv6 2001:DB8:100::10
   segment-list list2
    index 5 sid ipv6 2001:DB8:130::30
    index 10 sid ipv6 2001:DB8:100::10
   segment-list list3
    index 5 sid ipv6 2001:DB8:140::40
    index 10 sid ipv6 2001:DB8:100::10
   srv6-te policy policy1 endpoint 2001:DB8:1::1 color 101
    candidate-path preference 100
     segment-list list1 weight 50
     segment-list list2 weight 30
     segment-list list3 weight 20
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0005.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator PE2 auto-sid-disable
   #              
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0 
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:22::1/96
   isis ipv6 enable 1  
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:23::1/96
   isis ipv6 enable 1  
  #  
  interface GigabitEthernet0/1/8
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:24::1/96
   isis ipv6 enable 1  
  #      
  interface LoopBack1
   ipv6 enable    
   ipv6 address 2001:DB8:5::5/128
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 5.5.5.5
   peer 2001:DB8:1::1 as-number 100
   peer 2001:DB8:1::1 connect-interface LoopBack1
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    advertise l2vpn evpn
    segment-routing ipv6 locator PE2 evpn
    segment-routing ipv6 traffic-engineer best-effort evpn
    peer 10.2.1.1 as-number 65420
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
   tunnel select-seq ipv6 srv6-te-policy load-balance-number 1
  #               
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #               
  interface  GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 10.11.1.1 32
  #               
  bgp 65410       
   router-id 10.11.1.1
   peer 10.1.1.2 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.1.1.2 enable
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
   ip address 10.2.1.1 255.255.255.0
  #               
  interface LoopBack1
   ip address 10.22.2.2 32
  #               
  bgp 65420       
   router-id 10.22.2.2
   peer 10.2.1.2 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 10.2.1.2 enable
  #
  return
  ```