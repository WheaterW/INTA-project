Example for Configuring BGP4+ 6PE over Static SR-MPLS TE Policy
===============================================================

This section provides an example for configuring BGP4+ 6PE over static SR-MPLS TE Policy, thereby connecting discontinuous IPv6 networks through an SR network.

#### Networking Requirements

If an SR network is deployed between two discontinuous IPv6 networks, you can recurse BGP4+ 6PE routes to SR-MPLS TE Policies for the IPv6 networks to communicate with each other.

On the network shown in [Figure 1](#EN-US_TASK_0172368912__fig_dc_vrp_sr_all_cfg_008101), there is no direct link between CE1 and CE2 on the IPv6 network. CE1 and CE2 need to communicate through the SR network. To meet this requirement, a 6PE peer relationship can be established between PE1 and PE2. The 6PE peers exchange IPv6 routes learned from their attached CEs using MP-BGP, and forward IPv6 data over SR-MPLS TE Policies.

**Figure 1** BGP4+ 6PE route recursion to manually configured SR-MPLS TE Policies![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_sr_all_cfg_008101.png)

#### Precautions

In the BGP4+ 6PE scenario, no VPN instance needs to be configured.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IS-IS on the backbone network to ensure that PEs can interwork with each other.
2. Enable MPLS and SR for each device on the backbone network, and configure static adjacency SIDs.
3. Configure an SR-MPLS TE Policy with primary and backup paths on each PE.
4. Configure SBFD and HSB on each PE to enhance SR-MPLS TE Policy reliability.
5. Apply an import or export route-policy to a specified peer on each PE, and set the Color Extended Community. In this example, an import route-policy with the Color Extended Community is applied.
6. Establish an MP-IBGP peer relationship between PEs and enable them to advertise labeled routes.
7. Configure a tunnel selection policy on each PE.
8. Establish an EBGP peer relationship between each CE-PE pair for the CE and PE to exchange routing information.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and Ps

#### Procedure

1. Configure interface IP addresses for each device on the backbone network.
   
   
   
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
   [*PE1-LoopBack1] ip address 1.1.1.9 32
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.13.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] ip address 10.11.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure P1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P1] interface loopback 1
   ```
   ```
   [*P1-LoopBack1] ip address 2.2.2.9 32
   ```
   ```
   [*P1-LoopBack1] quit
   ```
   ```
   [*P1] interface gigabitethernet0/1/0
   ```
   ```
   [*P1-GigabitEthernet0/1/0] ip address 10.11.1.2 24
   ```
   ```
   [*P1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P1] interface gigabitethernet0/2/0
   ```
   ```
   [*P1-GigabitEthernet0/2/0] ip address 10.12.1.1 24
   ```
   ```
   [*P1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P1] commit
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
   [*PE2-LoopBack1] ip address 3.3.3.9 32
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] ip address 10.14.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] ip address 10.12.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure P2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P2] interface loopback 1
   ```
   ```
   [*P2-LoopBack1] ip address 4.4.4.9 32
   ```
   ```
   [*P2-LoopBack1] quit
   ```
   ```
   [*P2] interface gigabitethernet0/1/0
   ```
   ```
   [*P2-GigabitEthernet0/1/0] ip address 10.13.1.2 24
   ```
   ```
   [*P2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P2] interface gigabitethernet0/2/0
   ```
   ```
   [*P2-GigabitEthernet0/2/0] ip address 10.14.1.1 24
   ```
   ```
   [*P2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P2] commit
   ```
2. Configure an IGP for each device on the backbone network to implement interworking between PEs and Ps. IS-IS is used as an example.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
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
   [*PE1] interface gigabitethernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
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
   [*P1-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P1-isis-1] quit
   ```
   ```
   [*P1] interface loopback 1
   ```
   ```
   [*P1-LoopBack1] isis enable 1
   ```
   ```
   [*P1-LoopBack1] quit
   ```
   ```
   [*P1] interface gigabitethernet0/1/0
   ```
   ```
   [*P1-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*P1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P1] interface gigabitethernet0/2/0
   ```
   ```
   [*P1-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*P1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
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
   [*PE2] interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
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
   
   # Configure P2.
   
   ```
   [~P2] isis 1
   ```
   ```
   [*P2-isis-1] is-level level-1
   ```
   ```
   [*P2-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*P2-isis-1] quit
   ```
   ```
   [*P2] interface loopback 1
   ```
   ```
   [*P2-LoopBack1] isis enable 1
   ```
   ```
   [*P2-LoopBack1] quit
   ```
   ```
   [*P2] interface gigabitethernet0/1/0
   ```
   ```
   [*P2-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*P2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P2] interface gigabitethernet0/2/0
   ```
   ```
   [*P2-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*P2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P2] commit
   ```
3. Configure basic MPLS functions for each device on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] commit
   ```
   ```
   [~PE1-mpls] quit
   ```
   
   # Configure P1.
   
   ```
   [~P1] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P1] mpls
   ```
   ```
   [*P1-mpls] commit
   ```
   ```
   [~P1-mpls] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] commit
   ```
   ```
   [~PE2-mpls] quit
   ```
   
   # Configure P2.
   
   ```
   [~P2] mpls lsr-id 4.4.4.9
   ```
   ```
   [*P2] mpls
   ```
   ```
   [*P2-mpls] commit
   ```
   ```
   [~P2-mpls] quit
   ```
4. Configure Segment Routing on the backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] ipv4 adjacency local-ip-addr 10.11.1.1 remote-ip-addr 10.11.1.2 sid 330000
   ```
   ```
   [*PE1-segment-routing] ipv4 adjacency local-ip-addr 10.13.1.1 remote-ip-addr 10.13.1.2 sid 330001
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] traffic-eng level-1
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
   
   # Configure P1.
   
   ```
   [~P1] segment-routing
   ```
   ```
   [*P1-segment-routing] ipv4 adjacency local-ip-addr 10.11.1.2 remote-ip-addr 10.11.1.1 sid 330003
   ```
   ```
   [*P1-segment-routing] ipv4 adjacency local-ip-addr 10.12.1.1 remote-ip-addr 10.12.1.2 sid 330002
   ```
   ```
   [*P1-segment-routing] quit
   ```
   ```
   [*P1] isis 1
   ```
   ```
   [*P1-isis-1] cost-style wide
   ```
   ```
   [*P1-isis-1] traffic-eng level-1
   ```
   ```
   [*P1-isis-1] segment-routing mpls
   ```
   ```
   [*P1-isis-1] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] ipv4 adjacency local-ip-addr 10.12.1.2 remote-ip-addr 10.12.1.1 sid 330000
   ```
   ```
   [*PE2-segment-routing] ipv4 adjacency local-ip-addr 10.14.1.2 remote-ip-addr 10.14.1.1 sid 330001
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] traffic-eng level-1
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
   
   # Configure P2.
   
   ```
   [~P2] segment-routing
   ```
   ```
   [*P2-segment-routing] ipv4 adjacency local-ip-addr 10.13.1.2 remote-ip-addr 10.13.1.1 sid 330002
   ```
   ```
   [*P2-segment-routing] ipv4 adjacency local-ip-addr 10.14.1.1 remote-ip-addr 10.14.1.2 sid 330003
   ```
   ```
   [*P2-segment-routing] quit
   ```
   ```
   [*P2] isis 1
   ```
   ```
   [*P2-isis-1] cost-style wide
   ```
   ```
   [*P2-isis-1] traffic-eng level-1
   ```
   ```
   [*P2-isis-1] segment-routing mpls
   ```
   ```
   [*P2-isis-1] quit
   ```
   ```
   [*P2] commit
   ```
5. Configure an SR-MPLS TE Policy on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing
   ```
   ```
   [~PE1-segment-routing] segment-list pe1
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 10 sid label 330000
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] index 20 sid label 330002
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1] quit
   ```
   ```
   [*PE1-segment-routing] segment-list pe1backup
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1backup] index 10 sid label 330001
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1backup] index 20 sid label 330003
   ```
   ```
   [*PE1-segment-routing-segment-list-pe1backup] quit
   ```
   ```
   [*PE1-segment-routing] sr-te policy policy100 endpoint 3.3.3.9 color 100
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] binding-sid 115
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] mtu 1000
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] candidate-path preference 100
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] segment-list pe1backup
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] candidate-path preference 200
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] segment-list pe1
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] quit
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
   [~PE2-segment-routing] segment-list pe2
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 10 sid label 330000
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] index 20 sid label 330003
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2] quit
   ```
   ```
   [*PE2-segment-routing] segment-list pe2backup
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2backup] index 10 sid label 330001
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2backup] index 20 sid label 330002
   ```
   ```
   [*PE2-segment-routing-segment-list-pe2backup] quit
   ```
   ```
   [*PE2-segment-routing] sr-te policy policy200 endpoint 1.1.1.9 color 200
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200] binding-sid 115
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200] mtu 1000
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200] candidate-path preference 100
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200-path] segment-list pe2backup
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200-path] quit
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200] candidate-path preference 200
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200-path] segment-list pe2
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200-path] quit
   ```
   ```
   [*PE2-segment-routing-te-policy-policy200] quit
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the [**display sr-te policy**](cmdqueryname=display+sr-te+policy) command to check SR-MPLS TE Policy information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display sr-te policy
   PolicyName : policy100
   Endpoint             : 3.3.3.9              Color                : 100
   TunnelId             : 1                    TunnelType           : SR-TE Policy
   Binding SID          : 115                  MTU                  : 1000
   Policy State         : Up                   State Change Time    : 2019-11-22 16:45:09
   Admin State          : Up                   Traffic Statistics   : Disable
   BFD                  : Disable              Backup Hot-Standby   : Disable
   DiffServ-Mode        : -
   Active IGP Metric    : -
   Candidate-path Count : 2                    
   
   Candidate-path Preference: 200
   Path State           : Active               Path Type            : Primary
   Protocol-Origin      : Configuration(30)    Originator           : 0, 0.0.0.0
   Discriminator        : 200                  Binding SID          : -
   GroupId              : 2                    Policy Name          : policy100
   Template ID          : -
   Active IGP Metric    : -                              ODN Color            : -
   Metric               :
    IGP Metric          : -                              TE Metric            : -
    Delay Metric        : -                              Hop Counts           : -
   Segment-List Count   : 1
    Segment-List        : pe1
     Segment-List ID    : 129                  XcIndex              : 68
     List State         : Up                   BFD State            : -
     EXP                : -                    TTL                  : -
     DeleteTimerRemain  : -                    Weight               : 1
     Label : 330000, 330002
   
   Candidate-path Preference: 100
   Path State           : Inactive (Valid)     Path Type            : -
   Protocol-Origin      : Configuration(30)    Originator           : 0, 0.0.0.0
   Discriminator        : 100                  Binding SID          : -
   GroupId              : 1                    Policy Name          : policy100
   Template ID          : -
   Active IGP Metric    : -                              ODN Color            : -
   Metric               :
    IGP Metric          : -                              TE Metric            : -
    Delay Metric        : -                              Hop Counts           : -
   Segment-List Count   : 1
    Segment-List        : pe1backup
     Segment-List ID    : 194                  XcIndex              : -
     List State         : Up                   BFD State            : -
     EXP                : -                    TTL                  : -
     DeleteTimerRemain  : -                    Weight               : 1
     Label : 330001, 330003
   ```
6. Configure SBFD and HSB.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] sbfd
   ```
   ```
   [*PE1-sbfd] reflector discriminator 1.1.1.9
   ```
   ```
   [*PE1-sbfd] quit
   ```
   ```
   [*PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] sr-te-policy seamless-bfd enable
   ```
   ```
   [*PE1-segment-routing] sr-te-policy backup hot-standby enable
   ```
   ```
   [*PE1-segment-routing] commit
   ```
   ```
   [~PE1-segment-routing] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] sbfd
   ```
   ```
   [*PE2-sbfd] reflector discriminator 3.3.3.9
   ```
   ```
   [*PE2-sbfd] quit
   ```
   ```
   [*PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] sr-te-policy seamless-bfd enable
   ```
   ```
   [*PE2-segment-routing] sr-te-policy backup hot-standby enable
   ```
   ```
   [*PE2-segment-routing] commit
   ```
   ```
   [~PE2-segment-routing] quit
   ```
7. Configure route-policies.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy color100 permit node 1
   ```
   ```
   [*PE1-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] route-policy color200 permit node 1
   ```
   ```
   [*PE2-route-policy] apply extcommunity color 0:200
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] commit
   ```
8. Establish an MP-IBGP peer relationship between PEs and enable them to advertise labeled routes. Apply import route-policies to BGP4+ peers and set the color extended community for routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.9 enable
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.9 label-route-capability
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.9 route-policy color100 import
   ```
   ```
   [*PE1-bgp-af-ipv6] commit
   ```
   ```
   [~PE1-bgp-af-ipv6] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.9 enable
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.9 label-route-capability
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.9 route-policy color200 import
   ```
   ```
   [*PE2-bgp-af-ipv6] commit
   ```
   ```
   [~PE2-bgp-af-ipv6] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp ipv6 peer** command on the PEs to check whether the BGP peer relationship has been established. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp ipv6 peer
   ```
   ```
    BGP local router ID : 1.1.1.9
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.9         4         100        6        7     0 00:01:16 Established        0
   ```
9. Configure a tunnel selection policy on each PE for the specified SR-MPLS TE Policy to be preferentially selected.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] tunnel-policy p1
   ```
   ```
   [*PE1-tunnel-policy-p1] tunnel select-seq sr-te-policy load-balance-number 1 unmix
   ```
   ```
   [*PE1-tunnel-policy-p1] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv6-family unicast
   ```
   ```
   [*PE1-bgp-af-ipv6] peer 3.3.3.9 tnl-policy p1
   ```
   ```
   [*PE1-bgp-af-ipv6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] tunnel-policy p1
   ```
   ```
   [*PE2-tunnel-policy-p1] tunnel select-seq sr-te-policy load-balance-number 1 unmix
   ```
   ```
   [*PE2-tunnel-policy-p1] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv6-family unicast
   ```
   ```
   [*PE2-bgp-af-ipv6] peer 1.1.1.9 tnl-policy p1
   ```
   ```
   [*PE2-bgp-af-ipv6] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
10. Establish an EBGP peer relationship between each CE-PE pair.
    
    
    
    # Configure CE1.
    
    ```
    <HUAWEI> system-view
    ```
    ```
    [~HUAWEI] sysname CE1
    ```
    ```
    [*HUAWEI] commit
    ```
    ```
    [~CE1] interface loopback 1
    ```
    ```
    [*CE1-LoopBack1] ipv6 enable
    ```
    ```
    [*CE1-LoopBack1] ipv6 address 2001:db8:1::11:1 128
    ```
    ```
    [*CE1-LoopBack1] quit
    ```
    ```
    [*CE1] interface gigabitethernet0/1/0
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] ipv6 enable
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] ipv6 address 2001:db8::1:1 96
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] quit
    ```
    ```
    [*CE1] bgp 65410
    ```
    ```
    [*CE1-bgp] router-id 10.10.10.10
    ```
    ```
    [*CE1-bgp] peer 2001:db8::1:2 as-number 100
    ```
    ```
    [*CE1-bgp] ipv6-family unicast
    ```
    ```
    [*CE1-bgp-af-ipv6] peer 2001:db8::1:2 enable
    ```
    ```
    [*CE1-bgp-af-ipv6] network 2001:db8:1::11:1 128
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
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of CE2 is similar to the configuration of CE1. For detailed configurations, see Configuration Files.
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 100
    ```
    ```
    [~PE1-bgp] peer 2001:db8::1:1 as-number 65410
    ```
    ```
    [*PE1-bgp] ipv6-family unicast
    ```
    ```
    [*PE1-bgp-af-ipv6] peer 2001:db8::1:1 enable
    ```
    ```
    [*PE1-bgp-af-ipv6] commit
    ```
    ```
    [~PE1-bgp-af-ipv6] quit
    ```
    ```
    [~PE1-bgp] quit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of PE2 is similar to the configuration of PE1. For detailed configurations, see Configuration Files.
    
    After completing the configuration, run the **display bgp ipv6 peer** command on each PE. The following example uses the peer relationship between PE1 and CE1. The command output shows that a BGP4+ peer relationship has been established between the PE and CE and is in the Established state.
    
    ```
    [~PE1] display bgp ipv6 peer
    ```
    ```
     BGP local router ID : 1.1.1.9
     Local AS number : 100
     Total number of peers : 2                 Peers in established state : 2
    
      Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
      3.3.3.9         4         100        6        7     0 00:01:16 Established        0
      2001:DB8::1:1   4       65410        5        4     0 00:01:16 Established        1
    ```
11. Verify the configuration.
    
    
    
    After completing the configuration, run the **display ipv6 routing-table** command on each PE to check information about the loopback interface route toward a CE.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display ipv6 routing-table
    ```
    ```
    Routing Table : _public_
             Destinations : 8        Routes : 8         
    
    Destination  : ::1                                     PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : InLoopBack0                             Flags        : D
    
    Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104
    NextHop      : ::FFFF:127.0.0.1                        Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : InLoopBack0                             Flags        : D
    
    Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : InLoopBack0                             Flags        : D
    
    Destination  : 2001:DB8::                              PrefixLength : 96
    NextHop      : 2001:DB8::1:2                           Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
                    
    Destination  : 2001:DB8::1:2                           PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
                    
    Destination  : 2001:DB8:1::11:1                        PrefixLength : 128
    NextHop      : 2001:DB8::1:1                           Preference   : 255
    Cost         : 0                                       Protocol     : EBGP
    RelayNextHop : 2001:DB8::1:1                           TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : RD
                    
    Destination  : 2001:DB8:2::22:2                        PrefixLength : 128
    NextHop      : ::FFFF:3.3.3.9                          Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : 2001:DB8::1:1                           TunnelID     : 0x000000003200000001
    Interface    : policy100                               Flags        : RD
                    
    Destination  : FE80::                                  PrefixLength : 10
    NextHop      : ::                                      Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : NULL0                                   Flags        : DB
    ```
    
    Run the **display ipv6 routing-table verbose** command on each PE to check details about the loopback interface route toward a CE.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display ipv6 routing-table 2001:db8:2::22:2 verbose
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : _public_
    Summary Count : 1
    
    Destination  : 2001:DB8:2::22:2                        PrefixLength : 128
    NextHop      : ::FFFF:3.3.3.9                          Preference   : 255
    Neighbour    : ::3.3.3.9                               ProcessID    : 0
    Label        : 48183                                   Protocol     : IBGP
    State        : Active Adv Relied                       Cost         : 0
    Entry ID     : 0                                       EntryFlags   : 0x00000000
    Reference Cnt: 0                                       Tag          : 0
    Priority     : low                                     Age          : 288sec
    IndirectID   : 0x10000C8                               Instance     : 
    RelayNextHop : 0.0.0.0                                 TunnelID     : 0x000000003200000001
    Interface    : policy100                              Flags        : RD
    ```
    
    The command output shows that the BGP4+ route has been successfully recursed to the specified SR-MPLS TE Policy.
    
    Check that the CEs can ping each other. For example, CE1 can ping CE2 at 2001:db8:2::22:2.
    
    ```
    [~CE1] ping ipv6 -a 2001:db8:1::11:1 2001:db8:2::22:2
      PING 2001:DB8:2::22:2 : 56  data bytes, press CTRL_C to break
        Reply from 2001:DB8:2::22:2
        bytes=56 Sequence=1 hop limit=62  time = 170 ms
        Reply from 2001:DB8:2::22:2
        bytes=56 Sequence=2 hop limit=62  time = 140 ms
        Reply from 2001:DB8:2::22:2
        bytes=56 Sequence=3 hop limit=62  time = 150 ms
        Reply from 2001:DB8:2::22:2
        bytes=56 Sequence=4 hop limit=62  time = 140 ms
        Reply from 2001:DB8:2::22:2
        bytes=56 Sequence=5 hop limit=62  time = 170 ms
    
      --- 2001:DB8:2::22:2 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 140/154/170 ms
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  bfd
  #
  sbfd
   reflector discriminator 1.1.1.9
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls            
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.11.1.1 remote-ip-addr 10.11.1.2 sid 330000
   ipv4 adjacency local-ip-addr 10.13.1.1 remote-ip-addr 10.13.1.2 sid 330001
   sr-te-policy backup hot-standby enable
   sr-te-policy seamless-bfd enable
   segment-list pe1
    index 10 sid label 330000
    index 20 sid label 330002
   segment-list pe1backup
    index 10 sid label 330001
    index 20 sid label 330003
   sr-te policy policy100 endpoint 3.3.3.9 color 100
    binding-sid 115
    mtu 1000    
    candidate-path preference 200
     segment-list pe1
    candidate-path preference 100
     segment-list pe1backup
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-1
   segment-routing mpls
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.13.1.1 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable
   ipv6 address 2001:DB8::1:2/96
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.11.1.1 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1  
  #               
  bgp 100         
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   peer 2001:DB8::1:1 as-number 65410
   #              
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
   #              
   ipv6-family unicast
    undo synchronization
    peer 3.3.3.9 route-policy color100 import
    peer 3.3.3.9 label-route-capability
    peer 3.3.3.9 tnl-policy p1
    peer 2001:DB8::1:1 enable
  #
  route-policy color100 permit node 1
   apply extcommunity color 0:100
  #               
  tunnel-policy p1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix
  #
  return
  ```
* P1 configuration file
  
  ```
  #
  sysname P1
  #
  mpls lsr-id 2.2.2.9
  #               
  mpls            
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.12.1.1 remote-ip-addr 10.12.1.2 sid 330002
   ipv4 adjacency local-ip-addr 10.11.1.2 remote-ip-addr 10.11.1.1 sid 330003
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-1
   segment-routing mpls
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.11.1.2 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.12.1.1 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1  
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  bfd
  #
  sbfd
   reflector discriminator 3.3.3.9
  #
  mpls lsr-id 3.3.3.9
  #               
  mpls            
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.12.1.2 remote-ip-addr 10.12.1.1 sid 330000
   ipv4 adjacency local-ip-addr 10.14.1.2 remote-ip-addr 10.14.1.1 sid 330001
   sr-te-policy backup hot-standby enable
   sr-te-policy seamless-bfd enable
   segment-list pe2
    index 10 sid label 330000
    index 20 sid label 330003
   segment-list pe2backup
    index 10 sid label 330001
    index 20 sid label 330002
   sr-te policy policy200 endpoint 1.1.1.9 color 200
    binding-sid 115
    mtu 1000 
    candidate-path preference 200
     segment-list pe2
    candidate-path preference 100
     segment-list pe2backup
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-1
   segment-routing mpls
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.14.1.2 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable
   ipv6 address 2001:DB8::2:2/96
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.12.1.2 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1  
  #               
  bgp 100         
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   peer 2001:DB8::2:1 as-number 65420
   #              
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #              
   ipv6-family unicast
    undo synchronization
    peer 1.1.1.9 route-policy color200 import
    peer 1.1.1.9 label-route-capability
    peer 1.1.1.9 tnl-policy p1
    peer 2001:DB8::2:1 enable
  #
  route-policy color200 permit node 1
   apply extcommunity color 0:200
  #               
  tunnel-policy p1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix
  #
  return
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #
  mpls lsr-id 4.4.4.9
  #               
  mpls            
  #               
  segment-routing 
   ipv4 adjacency local-ip-addr 10.13.1.2 remote-ip-addr 10.13.1.1 sid 330002
   ipv4 adjacency local-ip-addr 10.14.1.1 remote-ip-addr 10.14.1.2 sid 330003
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   traffic-eng level-1
   segment-routing mpls
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.13.1.2 255.255.255.0
   isis enable 1  
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.14.1.1 255.255.255.0
   isis enable 1  
  #               
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1  
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
   ipv6 enable
   ipv6 address 2001:DB8::1:1/96
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:1::11:1/128
  #
  bgp 65410
   router-id 10.10.10.10
   peer 2001:DB8::1:2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:DB8:1::11:1 128
    peer 2001:DB8::1:2 enable
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
   ipv6 enable
   ipv6 address 2001:DB8::2:1/96
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::22:2/128
  #
  bgp 65420
   router-id 10.20.20.20
   peer 2001:DB8::2:2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    network 2001:DB8:2::22:2 128
    peer 2001:DB8::2:2 enable
  #
  return
  ```