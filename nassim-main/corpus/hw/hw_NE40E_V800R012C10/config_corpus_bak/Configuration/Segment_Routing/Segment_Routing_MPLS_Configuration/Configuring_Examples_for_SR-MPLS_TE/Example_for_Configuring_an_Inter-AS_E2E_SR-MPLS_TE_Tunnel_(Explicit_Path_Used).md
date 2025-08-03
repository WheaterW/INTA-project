Example for Configuring an Inter-AS E2E SR-MPLS TE Tunnel (Explicit Path Used)
==============================================================================

An inter-AS E2E SR-MPLS TE tunnel can be configured to provide a secure data channel for services, for example, inter-AS VPN services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368895__fig-dc_vrp_sr_all_cfg_004001), PE1 and ASBR1 reside in AS 100, PE2 and ASBR2 reside in AS 200, and ASBR1 and ASBR2 are directly connected through two physical links. A bidirectional E2E tunnel needs to be established between PE1 and PE2, with SR being used for path generation and data forwarding. In the PE1-to-PE2 direction, PE1 and PE2 are the ingress and egress of the path, respectively. In the PE2-to-PE1 direction, PE2 and PE1 are the ingress and egress of the path, respectively.

**Figure 1** E2E SR-MPLS TE tunnel networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig-dc_vrp_sr_all_cfg_004001.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure intra-AS SR-MPLS TE tunnels in AS 100 and AS 200. Set binding SIDs for the SR-MPLS TE tunnels.
2. Establish an EBGP peer relationship between ASBR1 and ASBR2, enable BGP EPE and BGP-LS, and configure the devices to generate BGP Peer SIDs. Note that you only need to enable the address family for BGP-LS, without having to enable the BGP peer relationship in the address family.
3. Create an E2E SR-MPLS TE tunnel interface on PE1 and PE2. Specify the IP address, tunneling protocol, and destination address of each tunnel. Explicit paths are used for path computation.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces as shown in [Figure 1](#EN-US_TASK_0172368895__fig-dc_vrp_sr_all_cfg_004001)
* IS-IS process ID (1), IS-IS level (Level-2), and IS-IS system IDs (10.0000.0000.0001.00, 10.0000.0000.0002.00, 10.0000.0000.0003.00, and 10.0000.0000.0004.00)
* AS number (100) of PE1 and ASBR1 and that (200) of PE2 and ASBR2
* SR-MPLS TE tunnel interface names in AS 100 (Tunnel1) and AS 200 (Tunnel2); tunnel interface name of the PE1-to-PE2 E2E SR-MPLS TE tunnel (Tunnel3) and that of the PE2-to-PE1 E2E SR-MPLS TE tunnel (Tunnel3)

#### Procedure

1. Assign an IP address and a mask to each interface.
   
   
   
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
   [*ASBR1-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/3/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] ip address 10.0.1.2 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] quit
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
   [*ASBR2-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/3/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/3/0] ip address 10.9.1.1 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/3/0] quit
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
2. Configure an intra-AS SR-MPLS TE tunnel in AS 100.
   
   
   
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
   [*PE1] segment-routing
   ```
   ```
   [*PE1-segment-routing] quit
   ```
   ```
   [*PE1] isis 1
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
   [*PE1-isis-1] segment-routing mpls
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
   [*PE1-LoopBack1] isis prefix-sid absolute 16100
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
   [*PE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] explicit-path path2asbr1
   ```
   ```
   [*PE1-explicit-path-path2asbr1] next sid label 330102 type adjacency
   ```
   ```
   [*PE1-explicit-path-path2asbr1] quit
   ```
   ```
   [*PE1] interface tunnel1
   ```
   ```
   [*PE1-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*PE1-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*PE1-Tunnel1] destination 2.2.2.2
   ```
   ```
   [*PE1-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*PE1-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE1-Tunnel1] mpls te path explicit-path path2asbr1
   ```
   ```
   [*PE1-Tunnel1] commit
   ```
   ```
   [~PE1-Tunnel1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding steps, the [**next sid label**](cmdqueryname=next+sid+label) command uses the adjacency label from PE1 to ASBR1, which is dynamically generated by IS-IS. Before the configuration, you can run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command to query the label value. For example:
   
   ```
   [~PE1] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------
   330102    GE0/1/0           10.0.1.2         ISIS-V4     ---       1500      _public_      
   
   Total information(s): 1
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
   [*ASBR1] segment-routing
   ```
   ```
   [*ASBR1-segment-routing] quit
   ```
   ```
   [*ASBR1] isis 1
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
   [*ASBR1-isis-1] segment-routing mpls
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
   [*ASBR1-LoopBack1] isis prefix-sid absolute 16200
   ```
   ```
   [*ASBR1-LoopBack1] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet0/3/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] mpls te
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*ASBR1] explicit-path path2pe1
   ```
   ```
   [*ASBR1-explicit-path-path2pe1] next sid label 330201 type adjacency
   ```
   ```
   [*ASBR1-explicit-path-path2pe1] quit
   ```
   ```
   [*ASBR1] interface tunnel1
   ```
   ```
   [*ASBR1-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*ASBR1-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*ASBR1-Tunnel1] destination 1.1.1.1
   ```
   ```
   [*ASBR1-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*ASBR1-Tunnel1] mpls te signal-protocol segment-routing
   ```
   ```
   [*ASBR1-Tunnel1] mpls te path explicit-path path2pe1
   ```
   ```
   [*ASBR1-Tunnel1] commit
   ```
   ```
   [~ASBR1-Tunnel1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding step, an ASBR1-to-PE1 adjacency label is used in the [**next sid label**](cmdqueryname=next+sid+label) command and is dynamically generated using IS-IS. To obtain the label value, run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command. For example:
   
   ```
   [~ASBR1] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------------
   330201    GE0/3/0           10.0.1.1         ISIS-V4     ---       1500      _public_      
   
   Total information(s): 1
   ```
3. Configure an intra-AS SR-MPLS TE tunnel in AS 200.
   
   
   
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
   [*ASBR2] segment-routing
   ```
   ```
   [*ASBR2-segment-routing] quit
   ```
   ```
   [*ASBR2] isis 1
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
   [*ASBR2-isis-1] segment-routing mpls
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
   [*ASBR2-LoopBack1] isis prefix-sid absolute 16300
   ```
   ```
   [*ASBR2-LoopBack1] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/3/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*ASBR2-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/3/0] mpls te
   ```
   ```
   [*ASBR2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*ASBR2] explicit-path path2pe2
   ```
   ```
   [*ASBR2-explicit-path-path2pe2] next sid label 330304 type adjacency
   ```
   ```
   [*ASBR2-explicit-path-path2pe2] quit
   ```
   ```
   [*ASBR2] interface tunnel2
   ```
   ```
   [*ASBR2-Tunnel2] ip address unnumbered interface loopback 1
   ```
   ```
   [*ASBR2-Tunnel2] tunnel-protocol mpls te
   ```
   ```
   [*ASBR2-Tunnel2] destination 4.4.4.4
   ```
   ```
   [*ASBR2-Tunnel2] mpls te tunnel-id 1
   ```
   ```
   [*ASBR2-Tunnel2] mpls te signal-protocol segment-routing
   ```
   ```
   [*ASBR2-Tunnel2] mpls te path explicit-path path2pe2
   ```
   ```
   [*ASBR2-Tunnel2] commit
   ```
   ```
   [~ASBR2-Tunnel2] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding step, an ASBR2-to-PE2 adjacency label is used in the [**next sid label**](cmdqueryname=next+sid+label) command and is dynamically generated using IS-IS. To obtain the label value, run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command. For example:
   
   ```
   [~ASBR2] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------------
   330304    GE0/3/0           10.9.1.2         ISIS-V4     ---       1500      _public_      
   
   Total information(s): 1
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
   [*PE2] segment-routing
   ```
   ```
   [*PE2-segment-routing] quit
   ```
   ```
   [*PE2] isis 1
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
   [*PE2-isis-1] segment-routing mpls
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
   [*PE2-LoopBack1] isis prefix-sid absolute 16400
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
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] explicit-path path2asbr2
   ```
   ```
   [*PE2-explicit-path-path2asbr2] next sid label 330403 type adjacency
   ```
   ```
   [*PE2-explicit-path-path2asbr2] quit
   ```
   ```
   [*PE2] interface tunnel2
   ```
   ```
   [*PE2-Tunnel2] ip address unnumbered interface loopback 1
   ```
   ```
   [*PE2-Tunnel2] tunnel-protocol mpls te
   ```
   ```
   [*PE2-Tunnel2] destination 3.3.3.3
   ```
   ```
   [*PE2-Tunnel2] mpls te tunnel-id 1
   ```
   ```
   [*PE2-Tunnel2] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE2-Tunnel2] mpls te path explicit-path path2asbr2
   ```
   ```
   [*PE2-Tunnel2] commit
   ```
   ```
   [~PE2-Tunnel2] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding step, a PE2-to-ASBR2 adjacency label is used in the [**next sid label**](cmdqueryname=next+sid+label) command and is dynamically generated using IS-IS. To obtain the label value, run the [**display segment-routing adjacency mpls forwarding**](cmdqueryname=display+segment-routing+adjacency+mpls+forwarding) command. For example:
   
   ```
   [~PE2] display segment-routing adjacency mpls forwarding
               Segment Routing Adjacency MPLS Forwarding Information
   
   Label     Interface         NextHop          Type        MPLSMtu   Mtu       VPN-Name       
   -------------------------------------------------------------------------------------------
   330403    GE0/1/0           10.9.1.1         ISIS-V4     ---       1500      _public_      
   
   Total information(s): 1
   ```
4. Configure the MPLS TE capability on ASBRs.
   
   
   
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
5. Establish an EBGP peer relationship between ASBRs and enable BGP EPE and BGP-LS.
   
   
   
   In this example, a loopback interface is used to establish a multi-hop EBGP peer relationship. Before the configuration, ensure that the loopback interfaces of ASBR1 and ASBR2 are routable to each other.
   
   Currently, BGP EPE supports only EBGP peers. For multi-hop EBGP peers, they must be directly connected through physical links. If intermediate nodes exist, the nodes do not have BGP Peer SID information, causing a forwarding failure.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] ip route-static 3.3.3.3 32 gigabitethernet0/1/0 10.1.1.2 description asbr1toasbr2
   ```
   ```
   [*ASBR1] ip route-static 3.3.3.3 32 gigabitethernet0/2/0 10.2.1.2 description asbr1toasbr2
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
   [*ASBR1-bgp-af-ipv4] network 10.2.1.0 24
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
   [*ASBR2] ip route-static 2.2.2.2 32 gigabitethernet0/2/0 10.2.1.1 description asbr2toasbr1
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
   [*ASBR2-bgp-af-ipv4] network 10.2.1.0 24
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
   
   After the configuration, run the [**display bgp egress-engineering**](cmdqueryname=display+bgp+egress-engineering) command to check BGP EPE information. For example:
   
   ```
   [~ASBR1] display bgp egress-engineering
    Peer Node                : 3.3.3.3
    Peer Adj Num             : 2
    Local ASN                : 100
    Remote ASN               : 200
    Local Router Id          : 2.2.2.2
    Remote Router Id         : 3.3.3.3
    Local Interface Address  : 2.2.2.2
    Remote Interface Address : 3.3.3.3
    SID Label                : 32768
    Peer Set SID Label       : --
    Nexthop                  : 10.1.1.2
    Out Interface            : GigabitEthernet0/1/0
    Nexthop                  : 10.2.1.2
    Out Interface            : GigabitEthernet0/2/0
   
    Peer Adj                 : 10.1.1.2
    Local ASN                : 100
    Remote ASN               : 200
    Local Router Id          : 2.2.2.2
    Remote Router Id         : 3.3.3.3
    Interface Identifier     : 6
    Local Interface Address  : 10.1.1.1
    Remote Interface Address : 10.1.1.2
    SID Label                : 32770
    Nexthop                  : 10.1.1.2
    Out Interface            : GigabitEthernet0/1/0
    
    Peer Adj                 : 10.2.1.2
    Local ASN                : 100
    Remote ASN               : 200
    Local Router Id          : 2.2.2.2
    Remote Router Id         : 3.3.3.3
    Interface Identifier     : 7
    Local Interface Address  : 10.2.1.1
    Remote Interface Address : 10.2.1.2
    SID Label                : 32769
    Nexthop                  : 10.2.1.2
    Out Interface            : GigabitEthernet0/2/0
   ```
   ```
   [~ASBR2] display bgp egress-engineering
    Peer Node                : 2.2.2.2
    Peer Adj Num             : 2
    Local ASN                : 200
    Remote ASN               : 100
    Local Router Id          : 3.3.3.3
    Remote Router Id         : 2.2.2.2
    Local Interface Address  : 3.3.3.3
    Remote Interface Address : 2.2.2.2
    SID Label                : 31768
    Peer Set SID Label       : --
    Nexthop                  : 10.1.1.1
    Out Interface            : GigabitEthernet0/1/0
    Nexthop                  : 10.2.1.1
    Out Interface            : GigabitEthernet0/2/0
   
    Peer Adj                 : 10.1.1.1
    Local ASN                : 200
    Remote ASN               : 100
    Local Router Id          : 3.3.3.3
    Remote Router Id         : 2.2.2.2
    Interface Identifier     : 6
    Local Interface Address  : 10.1.1.2
    Remote Interface Address : 10.1.1.1
    SID Label                : 31770
    Nexthop                  : 10.1.1.1
    Out Interface            : GigabitEthernet0/1/0
   
    Peer Adj                 : 10.2.1.1
    Local ASN                : 200
    Remote ASN               : 100
    Local Router Id          : 3.3.3.3
    Remote Router Id         : 2.2.2.2
    Interface Identifier     : 7
    Local Interface Address  : 10.2.1.2
    Remote Interface Address : 10.2.1.1
    SID Label                : 31769
    Nexthop                  : 10.2.1.1
    Out Interface            : GigabitEthernet0/2/0
   ```
6. Set binding SIDs for the SR-MPLS TE tunnels within AS domains.
   
   
   
   **In the direction from PE1 to PE2:**
   
   # Configure PE1.
   
   ```
   [~PE1] interface tunnel1
   ```
   ```
   [*PE1-Tunnel1] mpls te binding-sid label 1000
   ```
   ```
   [*PE1-Tunnel1] commit
   ```
   ```
   [~PE1-Tunnel1] quit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] interface tunnel2
   ```
   ```
   [*ASBR2-Tunnel2] mpls te binding-sid label 2000
   ```
   ```
   [*ASBR2-Tunnel2] commit
   ```
   ```
   [~ASBR2-Tunnel2] quit
   ```
   
   **In the direction from PE2 to PE1:**
   
   # Configure PE2.
   
   ```
   [~PE2] interface tunnel2
   ```
   ```
   [*PE2-Tunnel2] mpls te binding-sid label 3000
   ```
   ```
   [*PE2-Tunnel2] commit
   ```
   ```
   [~PE2-Tunnel2] quit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] interface tunnel1
   ```
   ```
   [*ASBR1-Tunnel1] mpls te binding-sid label 4000
   ```
   ```
   [*ASBR1-Tunnel1] commit
   ```
   ```
   [~ASBR1-Tunnel1] quit
   ```
7. Configure a bidirectional E2E SR-MPLS TE tunnel between PE1 and PE2.
   
   
   
   **In the direction from PE1 to PE2:**
   
   # Configure PE1. There are multiple links between the ASBRs. You can select any of them. In this example, the link ASBR1 (GigabitEthernet 0/1/0) -> ASBR2 (GigabitEthernet 0/1/0) is selected.
   
   ```
   [~PE1] explicit-path path2pe2
   ```
   ```
   [*PE1-explicit-path-path2pe2] next sid label 1000 type binding-sid
   ```
   ```
   [*PE1-explicit-path-path2pe2] next sid label 32770 type adjacency
   ```
   ```
   [*PE1-explicit-path-path2pe2] next sid label 2000 type binding-sid
   ```
   ```
   [*PE1-explicit-path-path2pe2] quit
   ```
   ```
   [*PE1] interface tunnel3
   ```
   ```
   [*PE1-Tunnel3] ip address unnumbered interface loopback 1
   ```
   ```
   [*PE1-Tunnel3] tunnel-protocol mpls te
   ```
   ```
   [*PE1-Tunnel3] destination 4.4.4.4
   ```
   ```
   [*PE1-Tunnel3] mpls te tunnel-id 100
   ```
   ```
   [*PE1-Tunnel3] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE1-Tunnel3] mpls te path explicit-path path2pe2
   ```
   ```
   [*PE1-Tunnel3] commit
   ```
   ```
   [~PE1-Tunnel3] quit
   ```
   
   **In the direction from PE2 to PE1:**
   
   # Configure PE2. There are multiple links between the ASBRs. You can select any of them. In this example, the link ASBR2 (GigabitEthernet 0/1/0) -> ASBR1 (GigabitEthernet 0/1/0) is selected.
   
   ```
   [~PE2] explicit-path path2pe1
   ```
   ```
   [*PE2-explicit-path-path2pe1] next sid label 3000 type binding-sid
   ```
   ```
   [*PE2-explicit-path-path2pe1] next sid label 31770 type adjacency
   ```
   ```
   [*PE2-explicit-path-path2pe1] next sid label 4000 type binding-sid
   ```
   ```
   [*PE2-explicit-path-path2pe1] quit
   ```
   ```
   [*PE2] interface tunnel3
   ```
   ```
   [*PE2-Tunnel3] ip address unnumbered interface loopback 1
   ```
   ```
   [*PE2-Tunnel3] tunnel-protocol mpls te
   ```
   ```
   [*PE2-Tunnel3] destination 1.1.1.1
   ```
   ```
   [*PE2-Tunnel3] mpls te tunnel-id 400
   ```
   ```
   [*PE2-Tunnel3] mpls te signal-protocol segment-routing
   ```
   ```
   [*PE2-Tunnel3] mpls te path explicit-path path2pe1
   ```
   ```
   [*PE2-Tunnel3] commit
   ```
   ```
   [~PE2-Tunnel3] quit
   ```
8. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) *tunnel-name* command. The command output shows that the E2E SR-MPLS TE tunnel named **Tunnel3** is **Up**. For example:
   
   # Check the status on PE1.
   ```
   [~PE1] display mpls te tunnel-interface tunnel3
       Tunnel Name       : Tunnel3
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP
       Traffic Switch      : - 
       Session ID          : 100
       Ingress LSR ID      : 1.1.1.1               Egress LSR ID: 4.4.4.4
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : Segment-Routing
       FTid                : 2
       Tie-Breaking Policy : None                  Metric Type  : TE
       Bfd Cap             : None               
       Reopt               : Disabled              Reopt Freq   : - 
       Inter-area Reopt    : Disabled              
       Auto BW             : Disabled              Threshold    : - 
       Current Collected BW: -                     Auto BW Freq : -
       Min BW              : -                     Max BW       : -
       Offload             : Disabled              Offload Freq : - 
       Low Value           : -                     High Value   : - 
       Readjust Value      : - 
       Offload Explicit Path Name: -
       Tunnel Group        : Primary
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0
       Primary Tunnel      : -                     Pri Tunn Sum : -
       Backup Tunnel       : -
       Group Status        : Up                    Oam Status   : None
       IPTN InLabel        : -                     Tunnel BFD Status : -
       BackUp LSP Type     : None                  BestEffort   : -
       Secondary HopLimit  : -
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: -
       Secondary Affinity Prop/Mask: 0x0/0x0
       BestEffort Affinity Prop/Mask: -  
       IsConfigLspConstraint: -
       Hot-Standby Revertive Mode:  Revertive
       Hot-Standby Overlap-path:  Disabled
       Hot-Standby Switch State:  CLEAR
       Bit Error Detection:  Disabled
       Bit Error Detection Switch Threshold:  -
       Bit Error Detection Resume Threshold:  -
       Ip-Prefix Name    : -
       P2p-Template Name : -
       PCE Delegate      : No                     LSP Control Status : Local control
       Path Verification : No
       Entropy Label     : -
       Associated Tunnel Group ID: -              Associated Tunnel Group Type: -
       Auto BW Remain Time   : -                  Reopt Remain Time     : - 
       Segment-Routing Remote Label   : -
       Metric Inherit IGP : None
       Binding Sid       : 2001                  Reverse Binding Sid : 2002 
       FRR Attr Source   : -                     Is FRR degrade down : -
       Color             : - 
                                                      
       Primary LSP ID      : 1.1.1.1:3
       LSP State           : UP                    LSP Type     : Primary
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       SidProtectType      : - 
       Configured Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Actual Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Explicit Path Name  : path2pe2                         Hop Limit: -
       Record Route        : -                            Record Label : -
       Route Pinning       : -
       FRR Flag            : -
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : -
       Reroute Flag        : -
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
   ```
   # Check the status on PE2.
   ```
   [~PE2] display mpls te tunnel-interface tunnel3
       Tunnel Name       : Tunnel3
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP
       Traffic Switch      : - 
       Session ID          : 400
       Ingress LSR ID      : 4.4.4.4               Egress LSR ID: 1.1.1.1
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : Segment-Routing
       FTid                : 65
       Tie-Breaking Policy : None                  Metric Type  : TE
       Bfd Cap             : None                  
       Reopt               : Disabled              Reopt Freq   : -   
       Inter-area Reopt    : Disabled           
       Auto BW             : Disabled              Threshold    : - 
       Current Collected BW: -                     Auto BW Freq : -
       Min BW              : -                     Max BW       : -
       Offload             : Disabled              Offload Freq : - 
       Low Value           : -                     High Value   : - 
       Readjust Value      : - 
       Offload Explicit Path Name: -
       Tunnel Group        : Primary
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0
       Primary Tunnel      : -                     Pri Tunn Sum : -
       Backup Tunnel       : -
       Group Status        : Up                    Oam Status   : None
       IPTN InLabel        : -                     Tunnel BFD Status : -
       BackUp LSP Type     : None                  BestEffort   : -
       Secondary HopLimit  : -
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: -
       Secondary Affinity Prop/Mask: 0x0/0x0
       BestEffort Affinity Prop/Mask: -  
       IsConfigLspConstraint: -
       Hot-Standby Revertive Mode:  Revertive
       Hot-Standby Overlap-path:  Disabled
       Hot-Standby Switch State:  CLEAR
       Bit Error Detection:  Disabled
       Bit Error Detection Switch Threshold:  -
       Bit Error Detection Resume Threshold:  -
       Ip-Prefix Name    : -
       P2p-Template Name : -
       PCE Delegate      : No                     LSP Control Status : Local control
       Path Verification : No
       Entropy Label     : -
       Associated Tunnel Group ID: -              Associated Tunnel Group Type: -
       Auto BW Remain Time   : -                  Reopt Remain Time     : - 
       Segment-Routing Remote Label   : -
       Metric Inherit IGP : None
       Binding Sid       : 2002                  Reverse Binding Sid : 2001 
       FRR Attr Source   : -                     Is FRR degrade down : -
                                
       Primary LSP ID      : 4.4.4.4:4
       LSP State           : UP                    LSP Type     : Primary
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       Configured Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Actual Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Explicit Path Name  : path2pe1                         Hop Limit: -
       Record Route        : -                            Record Label : -
       Route Pinning       : -
       FRR Flag            : -
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : -
       Reroute Flag        : -
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
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
  explicit-path path2asbr1
   next sid label 330102 type adjacency index 1
  #
  explicit-path path2pe2
   next sid label 1000 type binding-sid index 1
   next sid label 32770 type adjacency index 2
   next sid label 2000 type binding-sid index 3
  #               
  segment-routing 
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
   isis prefix-sid absolute 16100
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path path2asbr1
   mpls te binding-sid label 1000
  #
  interface Tunnel3
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 100
   mpls te path explicit-path path2pe2
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
  explicit-path path2pe1
   next sid label 330201 type adjacency index 1
  #               
  segment-routing 
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
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.0.1.2 255.255.255.0
   isis enable 1  
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16200
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path path2pe1
   mpls te binding-sid label 4000
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
    network 10.2.1.0 255.255.255.0
    import-route isis 1
    peer 3.3.3.3 enable
   #
   link-state-family unicast
  #
  ip route-static 3.3.3.3 255.255.255.255 gigabitethernet0/1/0 10.1.1.2 description asbr1toasbr2
  ip route-static 3.3.3.3 255.255.255.255 gigabitethernet0/2/0 10.2.1.2 description asbr1toasbr2
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
  explicit-path path2pe2
   next sid label 330304 type adjacency index 1
  #               
  segment-routing 
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
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.9.1.1 255.255.255.0
   isis enable 1  
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
   isis prefix-sid absolute 16300
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path path2pe2
   mpls te binding-sid label 2000
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
    network 10.2.1.0 255.255.255.0
    import-route isis 1
    peer 2.2.2.2 enable
   #
   link-state-family unicast
  #
  ip route-static 2.2.2.2 255.255.255.255 gigabitethernet0/1/0 10.1.1.1 description asbr2toasbr1
  ip route-static 2.2.2.2 255.255.255.255 gigabitethernet0/2/0 10.2.1.1 description asbr2toasbr1
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
  explicit-path path2asbr2
   next sid label 330403 type adjacency index 1
  #
  explicit-path path2pe1
   next sid label 3000 type binding-sid index 1
   next sid label 31770 type adjacency index 2
   next sid label 4000 type binding-sid index 3
  #               
  segment-routing 
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
   isis prefix-sid absolute 16400
  #
  interface Tunnel2
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 1
   mpls te path explicit-path path2asbr2
   mpls te binding-sid label 3000
  #
  interface Tunnel3
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol segment-routing
   mpls te tunnel-id 400
   mpls te path explicit-path path2pe1
  #
  return
  ```