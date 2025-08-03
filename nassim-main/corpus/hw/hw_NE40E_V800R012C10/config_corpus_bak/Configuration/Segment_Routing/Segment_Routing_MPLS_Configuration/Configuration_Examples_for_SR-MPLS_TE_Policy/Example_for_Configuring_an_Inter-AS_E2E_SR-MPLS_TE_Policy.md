Example for Configuring an Inter-AS E2E SR-MPLS TE Policy
=========================================================

This section provides an example for configuring an inter-AS E2E SR-MPLS TE Policy to provide secure data channels for services such as inter-AS VPN.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001844948629__fig-dc_vrp_sr_all_cfg_004001), PE1 and ASBR1 reside in AS 100, PE2 and ASBR2 reside in AS 200, and ASBR1 and ASBR2 are directly connected through a physical link. A bidirectional E2E SR-MPLS TE Policy needs to be established between PE1 and PE2, with SR being used for path generation and data forwarding. In the PE1-to-PE2 direction, PE1 and PE2 are the ingress and egress of the path, respectively. In the PE2-to-PE1 direction, PE2 and PE1 are the ingress and egress of the path, respectively.

**Figure 1** E2E SR-MPLS TE Policy networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001844868557.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure intra-AS Adjacency SIDs in AS 100 and AS 200.
2. Establish an EBGP peer relationship between ASBR1 and ASBR2, enable BGP EPE and BGP-LS, and configure the devices to generate BGP Peer Adjacency SIDs. Note that you only need to enable the address family for BGP-LS, without having to enable the BGP peer relationship in the address family.
3. Deploy an E2E SR-MPLS TE Policy between PE1 and PE2, specifying elements such as the endpoint and color and adopting explicit paths for path computation.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IP addresses shown in [Figure 1](#EN-US_TASK_0000001844948629__fig-dc_vrp_sr_all_cfg_004001)
* IS-IS process ID: 1; IS-IS level: Level-2; IS-IS system IDs of nodes: 10.0000.0000.0001.00, 10.0000.0000.0002.00, 10.0000.0000.0003.00, and 10.0000.0000.0004.00
* AS number for PE1 and ASBR1: 100; AS number for PE2 and ASBR2: 200
* Name of the E2E SR-MPLS TE Policy from PE1 to PE2: Policy1 (with the segment list pe1); name of the E2E SR-MPLS TE Policy from PE2 to PE1: Policy1 (with the segment list pe2)

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure PE1.
   
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
   [~PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] ip address 1.1.1.1 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.0.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname ASBR1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~ASBR1] interface loopback 1
   ```
   ```
   [*ASBR1-LoopBack1] ip address 2.2.2.2 32
   ```
   ```
   [*ASBR1-LoopBack1] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] ip address 10.0.1.2 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname ASBR2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~ASBR2] interface loopback 1
   ```
   ```
   [*ASBR2-LoopBack1] ip address 3.3.3.3 32
   ```
   ```
   [*ASBR2-LoopBack1] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/1/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] ip address 10.9.1.1 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] ip address 4.4.4.4 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.9.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
2. Configure IGP route interworking in AS 100 and AS 200. This example uses IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-2
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] traffic-eng level-2
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] isis enable 1
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] isis 1
   ```
   ```
   [*ASBR1-isis-1] is-level level-2
   ```
   ```
   [*ASBR1-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*ASBR1-isis-1] cost-style wide
   ```
   ```
   [*ASBR1-isis-1] traffic-eng level-2
   ```
   ```
   [*ASBR1-isis-1] quit
   ```
   ```
   [*ASBR1] interface loopback 1
   ```
   ```
   [*ASBR1-LoopBack1] isis enable 1
   ```
   ```
   [*ASBR1-LoopBack1] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] isis 1
   ```
   ```
   [*ASBR2-isis-1] is-level level-2
   ```
   ```
   [*ASBR2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*ASBR2-isis-1] cost-style wide
   ```
   ```
   [*ASBR2-isis-1] traffic-eng level-2
   ```
   ```
   [*ASBR2-isis-1] quit
   ```
   ```
   [*ASBR2] interface loopback 1
   ```
   ```
   [*ASBR2-LoopBack1] isis enable 1
   ```
   ```
   [*ASBR2-LoopBack1] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-2
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] traffic-eng level-2
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] isis enable 1
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
3. Enable basic MPLS functions in AS 100 and AS 200.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls te
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 2.2.2.2
   ```
   ```
   [*ASBR1] mpls
   ```
   ```
   [*ASBR1-mpls] mpls te
   ```
   ```
   [*ASBR1-mpls] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls lsr-id 3.3.3.3
   ```
   ```
   [*ASBR2] mpls
   ```
   ```
   [*ASBR2-mpls] mpls te
   ```
   ```
   [*ASBR2-mpls] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/2/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 4.4.4.4
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls te
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Enable Segment Routing and configure Adjacency SIDs in AS 100 and AS 200.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] ipv4 adjacency local-ip-addr 10.0.1.1 remote-ip-addr 10.0.1.2 sid 330122
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] segment-routing mpls
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure ASBR1.
   
   ```
   [*ASBR1] segment-routing
   ```
   ```
   [*ASBR1-segment-routing] ipv4 adjacency local-ip-addr 10.0.1.2 remote-ip-addr 10.0.1.1 sid 330222
   ```
   ```
   [*ASBR1-segment-routing] quit
   ```
   ```
   [*ASBR1] isis 1
   ```
   ```
   [*ASBR1-isis-1] segment-routing mpls
   ```
   ```
   [*ASBR1-isis-1] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR2.
   
   ```
   [*ASBR2] segment-routing
   ```
   ```
   [*ASBR2-segment-routing] ipv4 adjacency local-ip-addr 10.9.1.1 remote-ip-addr 10.9.1.2 sid 330120
   ```
   ```
   [*ASBR2-segment-routing] quit
   ```
   ```
   [*ASBR2] isis 1
   ```
   ```
   [*ASBR2-isis-1] segment-routing mpls
   ```
   ```
   [*ASBR2-isis-1] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] ipv4 adjacency local-ip-addr 10.9.1.2 remote-ip-addr 10.9.1.1 sid 330220
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] segment-routing mpls
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] commit
   ```
5. Configure MPLS TE on the ASBRs.
   
   
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] interface gigabitethernet0/1/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] interface gigabitethernet0/1/0
   ```
   ```
   [~ASBR2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
6. Establish an EBGP peer relationship between the ASBRs and enable BGP EPE and BGP-LS.
   
   
   
   In this example, a loopback interface is used to establish a multi-hop EBGP peer relationship. Before the configuration, ensure that the loopback interfaces of ASBR1 and ASBR2 are routable to each other.
   
   Currently, BGP EPE supports only EBGP peers. For multi-hop EBGP peers, they must be directly connected through physical links. If intermediate nodes exist, the nodes do not have BGP Peer SID information, causing a forwarding failure.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] ip route-static 3.3.3.3 32 gigabitethernet0/1/0 10.1.1.2 description asbr1toasbr2
   ```
   ```
   [*ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 3.3.3.3 as-number 200
   ```
   ```
   [*ASBR1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] peer 3.3.3.3 ebgp-max-hop 2
   ```
   ```
   [*ASBR1-bgp] peer 3.3.3.3 egress-engineering
   ```
   ```
   [*ASBR1-bgp] link-state-family unicast
   ```
   ```
   [*ASBR1-bgp-af-ls] quit
   ```
   ```
   [*ASBR1-bgp] ipv4-family unicast
   ```
   ```
   [*ASBR1-bgp-af-ipv4] network 2.2.2.2 32
   ```
   ```
   [*ASBR1-bgp-af-ipv4] network 10.1.1.0 24
   ```
   ```
   [*ASBR1-bgp-af-ipv4] import-route isis 1
   ```
   ```
   [*ASBR1-bgp-af-ipv4] commit
   ```
   ```
   [~ASBR1-bgp-af-ipv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] ip route-static 2.2.2.2 32 gigabitethernet0/1/0 10.1.1.1 description asbr2toasbr1
   ```
   ```
   [*ASBR2] bgp 200
   ```
   ```
   [*ASBR2-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*ASBR2-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*ASBR2-bgp] peer 2.2.2.2 ebgp-max-hop 2
   ```
   ```
   [*ASBR2-bgp] peer 2.2.2.2 egress-engineering
   ```
   ```
   [*ASBR2-bgp] link-state-family unicast
   ```
   ```
   [*ASBR2-bgp-af-ls] quit
   ```
   ```
   [*ASBR2-bgp] ipv4-family unicast
   ```
   ```
   [*ASBR2-bgp-af-ipv4] network 3.3.3.3 32
   ```
   ```
   [*ASBR2-bgp-af-ipv4] network 10.1.1.0 24
   ```
   ```
   [*ASBR2-bgp-af-ipv4] import-route isis 1
   ```
   ```
   [*ASBR2-bgp-af-ipv4] commit
   ```
   ```
   [~ASBR2-bgp-af-ipv4] quit
   ```
   ```
   [~ASBR2-bgp] quit
   ```
   
   After completing the configuration, run the [**display bgp egress-engineering**](cmdqueryname=display+bgp+egress-engineering) command to check BGP EPE information. For example:
   
   ```
   [~ASBR1] display bgp egress-engineering
    Peer Node                : 3.3.3.3
    Peer Adj Num             : 1
    Local ASN                : 100
    Remote ASN               : 200
    Local Router Id          : 2.2.2.2
    Remote Router Id         : 3.3.3.3
    Local Interface Address  : 2.2.2.2
    Remote Interface Address : 3.3.3.3
    SID Label                : 31768
    Peer Set SID Label       : --
    Nexthop                  : 10.1.1.2
    Out Interface            : GigabitEthernet0/1/0
   
    Peer Adj                 : 10.1.1.2
    Local ASN                : 100
    Remote ASN               : 200
    Local Router Id          : 2.2.2.2
    Remote Router Id         : 3.3.3.3
    Interface Identifier     : 6
    Local Interface Address  : 10.1.1.1
    Remote Interface Address : 10.1.1.2
    SID Label                : 31770
    Nexthop                  : 10.1.1.2
    Out Interface            : GigabitEthernet0/1/0
   ```
   ```
   [~ASBR2] display bgp egress-engineering
    Peer Node                : 2.2.2.2
    Peer Adj Num             : 1
    Local ASN                : 200
    Remote ASN               : 100
    Local Router Id          : 3.3.3.3
    Remote Router Id         : 2.2.2.2
    Local Interface Address  : 3.3.3.3
    Remote Interface Address : 2.2.2.2
    SID Label                : 32768
    Peer Set SID Label       : --
    Nexthop                  : 10.1.1.1
    Out Interface            : GigabitEthernet0/1/0
   
    Peer Adj                 : 10.1.1.1
    Local ASN                : 200
    Remote ASN               : 100
    Local Router Id          : 3.3.3.3
    Remote Router Id         : 2.2.2.2
    Interface Identifier     : 6
    Local Interface Address  : 10.1.1.2
    Remote Interface Address : 10.1.1.1
    SID Label                : 32770
    Nexthop                  : 10.1.1.1
    Out Interface            : GigabitEthernet0/1/0
   ```
7. Deploy an SR-MPLS TE Policy between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] segment-list pe1
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 10 sid label 330122
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 20 sid label 31770
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 30 sid label 330120
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] quit
   ```
   ```
   [*PE1-segment-routing] sr-te policy policy1 endpoint 4.4.4.4 color 100
   ```
   ```
   [*PE1-segment-routing-te-policy-policy1] candidate-path preference 100
   ```
   ```
   [*PE1-segment-routing-te-policy-policy1-path] segment-list pe1
   ```
   ```
   [*PE1-segment-routing-te-policy-policy1-path] quit
   ```
   ```
   [*PE1-segment-routing-te-policy-policy1] quit
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] segment-list pe2
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 10 sid label 330220
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 20 sid label 32770
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 30 sid label 330222
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] quit
   ```
   ```
   [*PE2-segment-routing] sr-te policy policy1 endpoint 1.1.1.1 color 100
   ```
   ```
   [*PE2-segment-routing-te-policy-policy1] candidate-path preference 100
   ```
   ```
   [*PE2-segment-routing-te-policy-policy1-path] segment-list pe2
   ```
   ```
   [*PE2-segment-routing-te-policy-policy1-path] quit
   ```
   ```
   [*PE2-segment-routing-te-policy-policy1] quit
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configuration, run the **display sr-te policy** command to check SR-MPLS TE Policy information.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display sr-te policy
   PolicyName : policy1
   Endpoint             : 4.4.4.4                        Color                : 100
   TunnelId             : 1                              TunnelType           : SR-TE Policy
   Binding SID          : -                              MTU                  : -
   Policy State         : Up                             State Change Time    : 2024-01-24 09:29:47
   Admin State          : Up                             Traffic Statistics   : Disable
   BFD                  : Disable                        Backup Hot-Standby   : Disable
   DiffServ-Mode        : -
   Active IGP Metric    : -
   Candidate-path Count : 1
    
   Candidate-path Preference: 100
   Policy Name          : policy1
   Candidate-path Name  :
   Path State           : Active                         Path Type            : Primary
   Protocol-Origin      : Configuration(30)              Originator           : 0, 0.0.0.0
   Discriminator        : 100                            Binding SID          : -
   GroupId              : 1                              Compute Source       : -
   Template ID          : -                              CT0 Bandwidth        : -
   Active IGP Metric    : -                              ODN Color            : -
   Metric               :
    IGP Metric          : -                              TE Metric            : -
    Delay Metric        : -                              Hop Counts           : -
   Segment-List Count   : 1
    Segment-List        : pe1
     Segment-List ID    : 2                              XcIndex              : 2000002
     List State         : Up                             BFD State            : -
     EXP                : 0                              TTL                  : 255
     DeleteTimerRemain  : -                              Weight               : 1
     Metric             :
      IGP Metric        : -                              TE Metric            : -
      Delay Metric      : -                              Hop Counts           : -
     Label : 330122, 31770, 330120
   ```
8. Verify the configuration.
   
   
   
   After completing the configuration, perform a ping operation on the SR-MPLS TE Policy to check its connectivity.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] ping lsp sr-te policy policy-name policy1  
    LSP PING FEC:  Nil FEC  : 100 data bytes, press CTRL_C to break  
    sr-te policy's segment list:  
    Preference : 100; Path Type: main; Protocol-Origin : local; Originator: 0, 0.0.0.0; Discriminator: 100; Segment-List ID : 1;  Xcindex : 1  
      Reply from 4.4.4.4: bytes=100 Sequence=1 time=13 ms  
      Reply from 4.4.4.4: bytes=100 Sequence=2 time=9 ms   
      Reply from 4.4.4.4: bytes=100 Sequence=3 time=2 ms     
      Reply from 4.4.4.4: bytes=100 Sequence=4 time=3 ms    
      Reply from 4.4.4.4: bytes=100 Sequence=5 time=6 ms 
   
    --- FEC: Nil FEC ping statistics ---   
      5 packet(s) transmitted         
      5 packet(s) received        
      0.00% packet loss        
      round-trip min/avg/max = 2/6/13 ms
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.0.1.1 remote-ip-addr 10.0.1.2 sid 330122
   segment-list pe1
    index 10 sid label 330122
    index 20 sid label 31770
    index 30 sid label 330120
   sr-te policy policy1 endpoint 4.4.4.4 color 100
    candidate-path preference 100
     segment-list pe1
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-2
   segment-routing mpls
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.0.1.1 255.255.255.0
   isis enable 1  
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.0.1.2 remote-ip-addr 10.0.1.1 sid 330222
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
   segment-routing mpls
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.0.1.2 255.255.255.0
   isis enable 1  
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  bgp 100
   private-4-byte-as enable 
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 ebgp-max-hop 2
   peer 3.3.3.3 connect-interface LoopBack1
   peer 3.3.3.3 egress-engineering
   #
   ipv4-family unicast
    network 2.2.2.2 255.255.255.255
    network 10.1.1.0 255.255.255.0
    import-route isis 1
    peer 3.3.3.3 enable
   #
   link-state-family unicast
  #
  ip route-static 3.3.3.3 255.255.255.255 gigabitethernet0/1/0 10.1.1.2 description asbr1toasbr2
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.9.1.1 remote-ip-addr 10.9.1.2 sid 330120
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-2
   segment-routing mpls
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.9.1.1 255.255.255.0
   isis enable 1  
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  bgp 200
   private-4-byte-as enable 
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 ebgp-max-hop 2
   peer 2.2.2.2 connect-interface LoopBack 1
   peer 2.2.2.2 egress-engineering
   #
   ipv4-family unicast
    network 3.3.3.3 255.255.255.255
    network 10.1.1.0 255.255.255.0
    import-route isis 1
    peer 2.2.2.2 enable
   #
   link-state-family unicast
  #
  ip route-static 2.2.2.2 255.255.255.255 gigabitethernet0/1/0 10.1.1.1 description asbr2toasbr1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.9.1.2 remote-ip-addr 10.9.1.1 sid 330220
   segment-list pe2
    index 10 sid label 330220
    index 20 sid label 32770
    index 30 sid label 330222
   sr-te policy policy1 endpoint 1.1.1.1 color 100
    candidate-path preference 100
     segment-list pe2
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0004.00
   traffic-eng level-2
   segment-routing mpls
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.9.1.2 255.255.255.0
   isis enable 1  
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  return
  ```