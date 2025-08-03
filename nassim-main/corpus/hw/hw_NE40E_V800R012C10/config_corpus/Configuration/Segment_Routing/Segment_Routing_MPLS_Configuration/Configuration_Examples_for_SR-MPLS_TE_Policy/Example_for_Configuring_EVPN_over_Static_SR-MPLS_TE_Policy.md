Example for Configuring EVPN over Static SR-MPLS TE Policy
==========================================================

This section provides an example for configuring EVPN over static SR-MPLS TE Policy in order to transmit traffic on an EVPN network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368915__fig_dc_vrp_sr_all_cfg_010001), PE1, P1, P2, and PE2 are in the same AS. IS-IS is required to implement network connectivity. An SR-MPLS TE Policy needs to be configured on PE1 and PE2 to carry EVPN services.

**Figure 1** Networking of EVPN route recursion based on an SR-MPLS TE Policy![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_sr_all_cfg_010001.png)

#### Precautions

During the configuration, note the following:

After a VPN instance is bound to a PE interface connected to a CE, Layer 3 configurations on this interface, such as IP address and routing protocol configurations, are automatically deleted. Add these configurations again if necessary.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses on each device.
2. Configure an IGP on each device so that PEs and Ps on the backbone network can communicate with each other. IS-IS is used as an example.
3. Enable MPLS on each device.
4. Configure Segment Routing and static adjacency labels on each device.
5. Configure an SR-MPLS TE Policy on each PE.
6. Configure SBFD and HSB on each PE to enhance SR-MPLS TE Policy reliability.
7. Configure a route-policy on each PE.
8. Establish a BGP EVPN peer relationship between the PEs, apply an import route-policy, and set the color extended community for routes.
9. Configure an EVPN instance on each PE and connect the corresponding site to the PE.
10. Configure a tunnel selection policy on each PE to preferentially select an SR-MPLS TE Policy.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and Ps
* VPN targets and RDs of the EVPN instance named **evrf1** and the L3VPN instance named **vpn1**

#### Procedure

1. Configure interface IP addresses on each device.
   
   
   
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
   [*PE1-GigabitEthernet0/1/0] ip address 10.11.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.13.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
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
   [*PE2-GigabitEthernet0/1/0] ip address 10.12.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.14.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
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
2. Configure an IGP on each device so that PEs and Ps on the backbone network can communicate with each other. IS-IS is used as an example.
   
   
   
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
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
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
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
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
3. Configure basic MPLS functions on each device.
   
   
   
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
4. Configure Segment Routing on each device.
   
   
   
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
   [~PE1-segment-routing] segment-list path1
   ```
   ```
   [*PE1-segment-routing-segment-list-path1] index 10 sid label 330000
   ```
   ```
   [*PE1-segment-routing-segment-list-path1] index 20 sid label 330002
   ```
   ```
   [*PE1-segment-routing-segment-list-path1] quit
   ```
   ```
   [*PE1-segment-routing] segment-list path2
   ```
   ```
   [*PE1-segment-routing-segment-list-path2] index 10 sid label 330001
   ```
   ```
   [*PE1-segment-routing-segment-list-path2] index 20 sid label 330003
   ```
   ```
   [*PE1-segment-routing-segment-list-path2] quit
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
   [*PE1-segment-routing-te-policy-policy100] candidate-path preference 200
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] segment-list path1
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100] candidate-path preference 100
   ```
   ```
   [*PE1-segment-routing-te-policy-policy100-path] segment-list path2
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
   [~PE2-segment-routing] segment-list path1
   ```
   ```
   [*PE2-segment-routing-segment-list-path1] index 10 sid label 330000
   ```
   ```
   [*PE2-segment-routing-segment-list-path1] index 20 sid label 330003
   ```
   ```
   [*PE2-segment-routing-segment-list-path1] quit
   ```
   ```
   [*PE2-segment-routing] segment-list path2
   ```
   ```
   [*PE2-segment-routing-segment-list-path2] index 10 sid label 330001
   ```
   ```
   [*PE2-segment-routing-segment-list-path2] index 20 sid label 330002
   ```
   ```
   [*PE2-segment-routing-segment-list-path2] quit
   ```
   ```
   [*PE2-segment-routing] sr-te policy policy100 endpoint 1.1.1.9 color 100
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] binding-sid 115
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] mtu 1000
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] candidate-path preference 200
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100-path] segment-list path1
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] candidate-path preference 100
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100-path] segment-list path2
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100-path] quit
   ```
   ```
   [*PE2-segment-routing-te-policy-policy100] quit
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] commit
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
7. Configure a route-policy on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] route-policy rp1 permit node 10
   ```
   ```
   [*PE1-route-policy] if-match route-type evpn mac
   ```
   ```
   [*PE1-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] route-policy rp1 permit node 20
   ```
   ```
   [*PE1-route-policy] if-match route-type evpn prefix
   ```
   ```
   [*PE1-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] route-policy rp1 permit node 30
   ```
   ```
   [*PE1-route-policy] if-match route-type evpn inclusive
   ```
   ```
   [*PE1-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] route-policy rp1 permit node 40
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] route-policy rp1 permit node 10
   ```
   ```
   [*PE2-route-policy] if-match route-type evpn mac
   ```
   ```
   [*PE2-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] route-policy rp1 permit node 20
   ```
   ```
   [*PE2-route-policy] if-match route-type evpn prefix
   ```
   ```
   [*PE2-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] route-policy rp1 permit node 30
   ```
   ```
   [*PE2-route-policy] if-match route-type evpn inclusive
   ```
   ```
   [*PE2-route-policy] apply extcommunity color 0:100
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [~PE2] route-policy rp1 permit node 40
   ```
   ```
   [*PE2-route-policy] quit
   ```
   ```
   [*PE2] commit
   ```
8. Establish a BGP EVPN peer relationship between the PEs, apply an import route-policy, and set the color extended community for routes.
   
   
   
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
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.9 enable
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.9 route-policy rp1 import
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.9 advertise irb
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
   [*PE2-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 1.1.1.9 enable
   ```
   ```
   [*PE2-bgp-af-evpn] peer 1.1.1.9 route-policy rp1 import
   ```
   ```
   [*PE2-bgp-af-evpn] peer 1.1.1.9 advertise irb
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
   
   After the configuration is complete, run the **display bgp evpn peer** command on the PEs to check whether the BGP EVPN peer relationship has been established. If the **Established** state is displayed in the command output, the BGP EVPN peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   ```
   ```
    BGP local router ID : 1.1.1.9
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.9         4         100        4        4     0 00:00:28 Established        0
   ```
9. Configure an EVPN instance on each PE and connect the corresponding site to the PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 2:2
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] evpn source-address 1.1.1.9
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] esi 0011.1001.1001.1001.1001
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/3/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-GigabitEthernet0/3/0.1] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet0/3/0.1] bridge-domain 10
   ```
   ```
   [*PE1-GigabitEthernet0/3/0.1] quit
   ```
   ```
   [*PE1] interface Vbdif10
   ```
   ```
   [*PE1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-Vbdif10] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*PE1-Vbdif10] arp collect host enable
   ```
   ```
   [*PE1-Vbdif10] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] import-route direct
   ```
   ```
   [*PE1-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 evpn
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 200:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 2:2
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] evpn source-address 3.3.3.9
   ```
   ```
   [*PE2] bridge-domain 10
   ```
   ```
   [*PE2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-bd10] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] esi 0011.1001.1001.1001.1002
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/3/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet0/3/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE2-GigabitEthernet0/3/0.1] rewrite pop single
   ```
   ```
   [*PE2-GigabitEthernet0/3/0.1] bridge-domain 10
   ```
   ```
   [*PE2-GigabitEthernet0/3/0.1] quit
   ```
   ```
   [*PE2] interface Vbdif10
   ```
   ```
   [*PE2-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-Vbdif10] ip address 10.2.1.1 255.255.255.0
   ```
   ```
   [*PE2-Vbdif10] arp collect host enable
   ```
   ```
   [*PE2-Vbdif10] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp-vpn1] import-route direct
   ```
   ```
   [*PE2-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE2-bgp-vpn1] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
10. Configure a tunnel selection policy on each PE to preferentially select an SR-MPLS TE Policy.
    
    
    
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
    [*PE1] ip vpn-instance vpn1
    ```
    ```
    [*PE1-vpn-instance-vpn1] ipv4-family
    ```
    ```
    [*PE1-vpn-instance-vpn1-af-ipv4] tnl-policy p1 evpn
    ```
    ```
    [*PE1-vpn-instance-vpn1-af-ipv4] quit
    ```
    ```
    [*PE1-vpn-instance-vpn1] quit
    ```
    ```
    [*PE1] evpn vpn-instance evrf1 bd-mode
    ```
    ```
    [*PE1-evpn-instance-evrf1] tnl-policy p1
    ```
    ```
    [*PE1-evpn-instance-evrf1] quit
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
    [*PE2] ip vpn-instance vpn1
    ```
    ```
    [*PE2-vpn-instance-vpn1] ipv4-family
    ```
    ```
    [*PE2-vpn-instance-vpn1-af-ipv4] tnl-policy p1 evpn
    ```
    ```
    [*PE2-vpn-instance-vpn1-af-ipv4] quit
    ```
    ```
    [*PE2-vpn-instance-vpn1] quit
    ```
    ```
    [*PE2] evpn vpn-instance evrf1 bd-mode
    ```
    ```
    [*PE2-evpn-instance-evrf1] tnl-policy p1
    ```
    ```
    [*PE2-evpn-instance-evrf1] quit
    ```
    ```
    [*PE2] commit
    ```
11. Verify the configuration.
    
    
    
    After completing the configurations, run the **display bgp evpn all routing-table prefix-route** command on PE1 to view information about the IP prefix routes sent from PE2.
    
    ```
    [~PE1] display bgp evpn all routing-table prefix-route
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 1.1.1.9
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of Ip Prefix Routes: 2
     Route Distinguisher: 100:1
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
     *>    0:10.1.1.0:24                                          0.0.0.0
     *>i   0:10.2.1.0:24                                          3.3.3.9
    ```
    
    Run the **display bgp evpn all routing-table prefix-route 0:10.2.1.0:24** command on PE1 to view information about the IP prefix routes sent from PE2.
    
    ```
    [~PE1] display bgp evpn all routing-table prefix-route 0:10.2.1.0:24
    ```
    ```
     BGP local router ID : 1.1.1.9
     Local AS number : 100
     Total routes of Route Distinguisher(100:1): 1
     BGP routing table entry information of 0:10.2.1.0:24:
     Label information (Received/Applied): 330000/NULL
     From: 3.3.3.9 (3.3.3.9) 
     Route Duration: 0d00h09m04s
     Relay IP Nexthop: 10.11.1.2
     Relay IP Out-Interface:GigabitEthernet0/1/0
     Relay Tunnel Out-Interface: 
     Original nexthop: 3.3.3.9
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, Color <0 : 100>
     AS-path Nil, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20
     Route Type: 5 (Ip Prefix Route)
     Ethernet Tag ID: 0, IP Prefix/Len: 10.2.1.0/24, ESI: 0000.0000.0000.0000.0000, GW IP Address: 0.0.0.0
     Not advertised to any peer yet   
    ```
    
    Run the **display ip routing-table vpn-instance vpn1** command on PE1 to view information about the VPN routes sent from PE2.
    
    ```
    [~PE1] display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 7        Routes : 7         
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
           10.1.1.0/24  Direct  0    0             D   10.1.1.1        Vbdif10
           10.1.1.1/32  Direct  0    0             D   127.0.0.1       Vbdif10
         10.1.1.255/32  Direct  0    0             D   127.0.0.1       Vbdif10
           10.2.1.0/24  IBGP    255  0             RD  3.3.3.9         policy100 
           10.2.1.1/32  IBGP    255  0             RD  3.3.3.9         policy100 
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    
    Run the **display bgp evpn all routing-table mac-route** command on PE1 to check MAC route information sent from PE2.
    
    ```
    [~PE1] display bgp evpn all routing-table mac-route
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 1.1.1.9
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of Mac Routes: 4
     Route Distinguisher: 200:1
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:00e0-fc49-fa04:0:0.0.0.0                          3.3.3.9
     *>i   0:48:00e0-fc49-fa04:32:10.2.1.1                        3.3.3.9
     *>    0:48:00e0-fc0d-3801:0:0.0.0.0                          0.0.0.0
     *>    0:48:00e0-fc0d-3801:32:10.1.1.1                        0.0.0.0
        
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 4
           Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
     *>i   0:48:00e0-fc49-fa04:0:0.0.0.0                          3.3.3.9
     *>i   0:48:00e0-fc49-fa04:32:10.2.1.1                        3.3.3.9
     *>    0:48:00e0-fc0d-3801:0:0.0.0.0                          0.0.0.0
     *>    0:48:00e0-fc0d-3801:32:10.1.1.1                        0.0.0.0
    ```
    
    Run the **display bgp evpn all routing-table mac-route 0:48:00e0-fc49-fa04:0:0.0.0.0** command on PE1 to check details about the MAC route sent from PE2.
    
    ```
    [~PE1] display bgp evpn all routing-table mac-route 0:48:00e0-fc49-fa04:0:0.0.0.0
    ```
    ```
     BGP local router ID : 1.1.1.9
     Local AS number : 100
     Total routes of Route Distinguisher(200:1): 1
     BGP routing table entry information of 0:48:00e0-fc49-fa04:0:0.0.0.0:
     Label information (Received/Applied): 330000/NULL
     From: 3.3.3.9 (3.3.3.9) 
     Route Duration: 0d00h01m49s
     Relay IP Nexthop: 10.11.1.2
     Relay IP Out-Interface:GigabitEthernet0/1/0
     Relay Tunnel Out-Interface:
     Original nexthop: 3.3.3.9
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, RT <2 : 2>, SoO <3.3.3.9 : 0> , Color <0 : 100>, Mac Mobility <flag:1 seq:0 res:0>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 20
     Route Type: 2 (MAC Advertisement Route)
     Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc49-fa04/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000
     Not advertised to any peer yet
     
        
    
     EVPN-Instance evrf1:
     Number of Mac Routes: 1
     BGP routing table entry information of 0:48:00e0-fc49-fa04:0:0.0.0.0:
     Route Distinguisher: 200:1
     Remote-Cross route
     Label information (Received/Applied): 330000/NULL
     From: 3.3.3.9 (3.3.3.9) 
     Route Duration: 2d02h23m40s
     Relay Tunnel Out-Interface: policy100(srtepolicy)
     Original nexthop: 3.3.3.9
     Qos information : 0x0
     Ext-Community: RT <1 : 1>, RT <2 : 2>, SoO <3.3.3.9 : 0> , Color <0 : 100>, Mac Mobility <flag:1 seq:0 res:0>
     AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255
     Route Type: 2 (MAC Advertisement Route)
     Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc49-fa04/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000
     Not advertised to any peer yet
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   tnl-policy p1
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
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
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.11.1.1 remote-ip-addr 10.11.1.2 sid 330000
   ipv4 adjacency local-ip-addr 10.13.1.1 remote-ip-addr 10.13.1.2 sid 330001
   sr-te-policy backup hot-standby enable
   sr-te-policy seamless-bfd enable
   segment-list path1
    index 10 sid label 330000
    index 20 sid label 330002
   segment-list path2
    index 10 sid label 330001
    index 20 sid label 330003
   sr-te policy policy100 endpoint 3.3.3.9 color 100
    binding-sid 115
    mtu 1000
    candidate-path preference 200
     segment-list path1
    candidate-path preference 100
     segment-list path2
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-1
   segment-routing mpls
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.11.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.13.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   esi 0011.1001.1001.1001.1001
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    peer 3.3.3.9 enable
    peer 3.3.3.9 route-policy rp1 import
    peer 3.3.3.9 advertise irb
  #
  route-policy rp1 permit node 10
   if-match route-type evpn mac
   apply extcommunity color 0:100
  #
  route-policy rp1 permit node 20
   if-match route-type evpn prefix
   apply extcommunity color 0:100
  #
  route-policy rp1 permit node 30
   if-match route-type evpn inclusive
   apply extcommunity color 0:100
  #
  route-policy rp1 permit node 40
  #
  tunnel-policy p1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix
  #
  evpn source-address 1.1.1.9
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
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 200:1
   tnl-policy p1
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
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
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  segment-routing
   ipv4 adjacency local-ip-addr 10.12.1.2 remote-ip-addr 10.12.1.1 sid 330000
   ipv4 adjacency local-ip-addr 10.14.1.2 remote-ip-addr 10.14.1.1 sid 330001
   sr-te-policy backup hot-standby enable
   sr-te-policy seamless-bfd enable
   segment-list path1
    index 10 sid label 330000
    index 20 sid label 330003
   segment-list path2
    index 10 sid label 330001
    index 20 sid label 330002
   sr-te policy policy100 endpoint 1.1.1.9 color 100
    binding-sid 115
    mtu 1000
    candidate-path preference 200
     segment-list path1
    candidate-path preference 100
     segment-list path2
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-1
   segment-routing mpls
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.12.1.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.14.1.2 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   esi 0011.1001.1001.1001.1002
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    peer 1.1.1.9 enable
    peer 1.1.1.9 route-policy rp1 import
    peer 1.1.1.9 advertise irb
  #
  route-policy rp1 permit node 10
   if-match route-type evpn mac
   apply extcommunity color 0:100
  #
  route-policy rp1 permit node 20
   if-match route-type evpn prefix
   apply extcommunity color 0:100
  #
  route-policy rp1 permit node 30
   if-match route-type evpn inclusive
   apply extcommunity color 0:100
  #
  route-policy rp1 permit node 40
  #
  tunnel-policy p1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix
  #
  evpn source-address 3.3.3.9
  #
  return
  ```