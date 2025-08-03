Example for Creating an SR-MPLS TE Policy in ODN Mode
=====================================================

This section provides an example for creating an SR-MPLS TE Policy in ODN mode to better meet service requirements.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001530204385__fig_dc_vrp_sr_all_cfg_008301):

* CE1 and CE2 belong to a VPN instance named **vpna**.
* The VPN target used by **vpna** is 111:1.

Configure EVPN L3VPN services to recurse to SR-MPLS TE Policies to ensure secure communication between users in the same VPN. Because multiple links exist between PEs on the public network, other links must be able to provide protection for the primary link.

In traditional scenarios where traffic is steered into SR-MPLS TE Policies based on colors, the SR-MPLS TE Policies must be configured in advance. This may fail to meet diversified service requirements. The on-demand next hop (ODN) function does not require a large number of SR-MPLS TE Policies to be configured in advance. Instead, it enables SR-MPLS TE Policy creation to be dynamically triggered on demand based on service routes, simplifying network operations. During SR-MPLS TE Policy creation, you can select a pre-configured attribute template and constraint template to ensure that the to-be-created SR-MPLS TE Policy meets service requirements.

**Figure 1** Creating an SR-MPLS TE Policy in ODN mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/8, respectively.


  
![](figure/en-us_image_0000001479804478.png)

#### Precautions

During the configuration, note the following:

After a PE interface connected to a CE is bound to a VPN instance, Layer 3 configurations on this interface are automatically deleted. Such configurations include IP address and routing protocol configurations, and must be added again if needed.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on the backbone network.
2. Configure IS-IS on the backbone network to ensure that PEs can interwork with each other.
3. Enable MPLS on the backbone network.
4. Configure SR on the backbone network. In addition, configure IS-IS SR and use IS-IS to dynamically generate adjacency SIDs and advertise the SIDs to neighbors.
5. Configure TE attributes. The TE metric is used in this example. You can also configure other attributes, such as affinity attributes, path constraints, bandwidth constraints, bandwidth usage, IGP metric, delay, and hop limit, as required.
6. Establish a BGP-LS address family peer relationship between PE1 and the controller and another one between PE2 and the controller. In this way, the PEs can report network topology and label information to the controller through BGP-LS.
7. Configure route-policies with the color extended community attribute specified for routes on PE1 and PE2. Export route-policies are used in this example.
8. Configure an ODN template.
9. Establish PCEP connections between the PEs and controller. With these connections, the PEs functioning as PCCs send path computation requests to the controller functioning as the PCE. After completing path computation, the controller delivers the computation result to PE1 through PCEP.
10. Configure a source address on each PE.
11. Establish a BGP EVPN peer relationship between the PEs for them to exchange routing information.
12. Configure an EVPN L3VPN instance on each PE and bind an access-side interface to the instance.
13. Configure a tunnel selection policy on each PE.
14. Establish EBGP peer relationships between the CEs and PEs for them to exchange routing information.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs on the PEs and Ps
* VPN target and RD of **vpna**
* SRGB ranges on the PEs and Ps

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
   [*PE1] interface gigabitethernet0/1/8
   ```
   ```
   [*PE1-GigabitEthernet0/1/8] ip address 10.3.1.1 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/8] quit
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
   [*P1] interface gigabitethernet0/3/0
   ```
   ```
   [*P1-GigabitEthernet0/3/0] ip address 10.23.1.1 24
   ```
   ```
   [*P1-GigabitEthernet0/3/0] quit
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
   [*PE2] interface gigabitethernet0/1/8
   ```
   ```
   [*PE2-GigabitEthernet0/1/8] ip address 10.4.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/1/8] quit
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
   [*P2] interface gigabitethernet0/3/0
   ```
   ```
   [*P2-GigabitEthernet0/3/0] ip address 10.23.1.2 24
   ```
   ```
   [*P2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*P2] commit
   ```
   
   # Configure the Controller.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Controller
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Controller] interface loopback 1
   ```
   ```
   [*Controller-LoopBack1] ip address 10.10.10.10 32
   ```
   ```
   [*Controller-LoopBack1] quit
   ```
   ```
   [~Controller] interface gigabitethernet0/1/0
   ```
   ```
   [~Controller-GigabitEthernet0/1/0] ip address 10.3.1.2 24
   ```
   ```
   [*Controller-GigabitEthernet0/1/0] quit
   ```
   ```
   [*Controller] interface gigabitethernet0/2/0
   ```
   ```
   [*Controller-GigabitEthernet0/2/0] ip address 10.4.1.2 24
   ```
   ```
   [*Controller-GigabitEthernet0/2/0] quit
   ```
   ```
   [*Controller] commit
   ```
2. Configure an IGP on the backbone network for the PEs and Ps to communicate. IS-IS is used as an example.
   
   
   
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
   [*P1] interface gigabitethernet0/3/0
   ```
   ```
   [*P1-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*P1-GigabitEthernet0/3/0] quit
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
   [*P2] interface gigabitethernet0/3/0
   ```
   ```
   [*P2-GigabitEthernet0/3/0] isis enable 1
   ```
   ```
   [*P2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*P2] commit
   ```
3. Configure basic MPLS functions on the backbone network.
   
   
   
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
   [*PE1-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface loopback 1
   ```
   ```
   [*PE1-LoopBack1] isis prefix-sid index 10
   ```
   ```
   [*PE1-LoopBack1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure P1.
   
   ```
   [~P1] segment-routing
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
   [*P1-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*P1-isis-1] quit
   ```
   ```
   [*P1] interface loopback 1
   ```
   ```
   [*P1-LoopBack1] isis prefix-sid index 20
   ```
   ```
   [*P1-LoopBack1] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing
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
   [*PE2-isis-1] segment-routing mpls
   ```
   ```
   [PE2-isis-1] traffic-eng level-1
   ```
   ```
   [*PE2-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface loopback 1
   ```
   ```
   [*PE2-LoopBack1] isis prefix-sid index 30
   ```
   ```
   [*PE2-LoopBack1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure P2.
   
   ```
   [~P2] segment-routing
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
   [*P2-isis-1] segment-routing global-block 16000 23999
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The SRGB range varies according to the device. The range specified in this example is for reference only.
   
   ```
   [*P2-isis-1] quit
   ```
   ```
   [*P2] interface loopback 1
   ```
   ```
   [*P2-LoopBack1] isis prefix-sid index 40
   ```
   ```
   [*P2-LoopBack1] quit
   ```
   ```
   [*P2] commit
   ```
5. Configure the TE metric attribute.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] te attribute enable
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] te metric 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] te metric 10
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure P1.
   
   ```
   [~P1] te attribute enable
   ```
   ```
   [*P1] interface gigabitethernet0/1/0
   ```
   ```
   [*P1-GigabitEthernet0/1/0] te metric 10
   ```
   ```
   [*P1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P1] interface gigabitethernet0/2/0
   ```
   ```
   [*P1-GigabitEthernet0/2/0] te metric 10
   ```
   ```
   [*P1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P1] interface gigabitethernet0/3/0
   ```
   ```
   [*P1-GigabitEthernet0/3/0] te metric 100
   ```
   ```
   [*P1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*P1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] te attribute enable
   ```
   ```
   [*PE2] interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] te metric 20
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] te metric 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure P2.
   
   ```
   [~P2] te attribute enable
   ```
   ```
   [*P2] interface gigabitethernet0/1/0
   ```
   ```
   [*P2-GigabitEthernet0/1/0] te metric 20
   ```
   ```
   [*P2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*P2] interface gigabitethernet0/2/0
   ```
   ```
   [*P2-GigabitEthernet0/2/0] te metric 20
   ```
   ```
   [*P2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*P2] interface gigabitethernet0/3/0
   ```
   ```
   [*P2-GigabitEthernet0/3/0] te metric 100
   ```
   ```
   [*P2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*P2] commit
   ```
6. Establish BGP-LS address family peer relationships.
   
   
   
   To allow a PE to report topology information to a controller through BGP-LS, you must enable IS-IS-based topology advertisement on the PE. Typically, this configuration needs to be performed on only one device in an IGP domain. In this example, this configuration is performed on both PE1 and PE2 to improve reliability.
   
   # Enable IS-IS SR-MPLS TE on PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [~PE1-isis-1] bgp-ls enable level-1
   ```
   ```
   [*PE1-isis-1] commit
   ```
   ```
   [~PE1-isis-1] quit
   ```
   
   # Enable IS-IS SR-MPLS TE on PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [~PE2-isis-1] bgp-ls enable level-1
   ```
   ```
   [*PE2-isis-1] commit
   ```
   ```
   [~PE2-isis-1] quit
   ```
   
   # Configure the BGP-LS address family peer relationship on PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 10.3.1.2 as-number 100
   ```
   ```
   [*PE1-bgp] link-state-family unicast
   ```
   ```
   [*PE1-bgp-af-ls] peer 10.3.1.2 enable
   ```
   ```
   [*PE1-bgp-af-ls] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the BGP-LS address family peer relationship on PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 10.4.1.2 as-number 100
   ```
   ```
   [*PE2-bgp] link-state-family unicast
   ```
   ```
   [*PE2-bgp-af-ls] peer 10.4.1.2 enable
   ```
   ```
   [*PE2-bgp-af-ls] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure the BGP-LS address family peer relationship on the controller.
   
   ```
   [~Controller] bgp 100
   ```
   ```
   [*Controller-bgp] peer 10.3.1.1 as-number 100
   ```
   ```
   [*Controller-bgp] peer 10.4.1.1 as-number 100
   ```
   ```
   [*Controller-bgp] link-state-family unicast
   ```
   ```
   [*Controller-bgp-af-ls] peer 10.3.1.1 enable
   ```
   ```
   [*Controller-bgp-af-ls] peer 10.4.1.1 enable
   ```
   ```
   [*Controller-bgp-af-ls] quit
   ```
   ```
   [*Controller-bgp] quit
   ```
   ```
   [*Controller] commit
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
8. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.9
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 3.3.3.9
   ```
   ```
   [*PE2] commit
   ```
9. Establish a BGP EVPN peer relationship between the PEs, apply export route-policies to the BGP EVPN peers, and set the color extended community for routes.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 3.3.3.9 as-number 100
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
   [*PE1-bgp-af-evpn] peer 3.3.3.9 route-policy color100 export
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.9 advertise irb
   ```
   ```
   [*PE1-bgp-af-evpn] commit
   ```
   ```
   [~PE1-bgp-af-evpn] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] peer 1.1.1.9 as-number 100
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
   [*PE2-bgp-af-evpn] peer 1.1.1.9 route-policy color200 export
   ```
   ```
   [*PE2-bgp-af-evpn] peer 1.1.1.9 advertise irb
   ```
   ```
   [*PE2-bgp-af-evpn] commit
   ```
   ```
   [~PE2-bgp-af-evpn] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After completing the configuration, run the **display bgp evpn peer** command on the PEs to check whether the BGP peer relationship has been established. If the **Established** state is displayed in the command output, the BGP peer relationship has been established successfully. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp evpn peer
   ```
   ```
    BGP local router ID : 1.1.1.9
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     3.3.3.9         4   100   12      18         0     00:09:38   Established   0
   ```
10. Configure an ODN template.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] segment-routing policy constraint-template tp200
    ```
    ```
    [*PE1-sr-policy-constraint-template-tp200] metric-type te
    ```
    ```
    [*PE1-sr-policy-constraint-template-tp200] max-cumulation te 20
    ```
    ```
    [*PE1-sr-policy-constraint-template-tp200] quit
    ```
    ```
    [*PE1] segment-routing
    ```
    ```
    [*PE1-segment-routing] on-demand color 200
    ```
    ```
    [*PE1-segment-routing-odn-200] dynamic-computation-seq pcep
    ```
    ```
    [*PE1-segment-routing-odn-200] constraint-template tp200
    ```
    ```
    [*PE1-segment-routing-odn-200] candidate-path preference 100
    ```
    ```
    [*PE1-segment-routing-odn-200] quit
    ```
    ```
    [*PE1] commit
    ```
    
    
    
    # Configure PE2.
    
    ```
    [~PE2] segment-routing policy constraint-template tp100
    ```
    ```
    [*PE2-sr-policy-constraint-template-tp100] metric-type te
    ```
    ```
    [*PE2-sr-policy-constraint-template-tp100] max-cumulation te 20
    ```
    ```
    [*PE2-sr-policy-constraint-template-tp100] quit
    ```
    ```
    [*PE2] segment-routing
    ```
    ```
    [*PE2-segment-routing] on-demand color 100
    ```
    ```
    [*PE2-segment-routing-odn-200] dynamic-computation-seq pcep
    ```
    ```
    [*PE2-segment-routing-odn-100] constraint-template tp100
    ```
    ```
    [*PE2-segment-routing-odn-100] candidate-path preference 100
    ```
    ```
    [*PE2-segment-routing-odn-100] quit
    ```
    ```
    [*PE2] commit
    ```
11. Configure PCEP delegation.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] pce-client
    ```
    ```
    [*PE1-pce-client] capability segment-routing
    ```
    ```
    [*PE1-pce-client] connect-server 10.10.10.10
    ```
    ```
    [*PE1-pce-client] quit
    ```
    ```
    [*PE1] commit
    ```
    
    
    
    # Configure PE2.
    
    ```
    [~PE2] pce-client
    ```
    ```
    [*PE2-pce-client] capability segment-routing
    ```
    ```
    [*PE2-pce-client] connect-server 10.10.10.10
    ```
    ```
    [*PE2-pce-client] quit
    ```
    ```
    [*PE2] commit
    ```
    
    After the configuration is complete, the PEs can receive the SR-MPLS TE Policy paths delivered by the controller and then generate SR-MPLS TE Policies. You can run the [**display sr-te policy**](cmdqueryname=display+sr-te+policy) command to check SR-MPLS TE Policy information. The following example uses the command output on PE1.
    
    ```
    [~PE1] display sr-te policy
    PolicyName : policy200
    Endpoint             : 3.3.3.9              Color                : 200
    TunnelId             : 1                    TunnelType           : SR-TE Policy
    Binding SID          : -                    MTU                  : 1000
    Policy State         : Up                   State Change Time    : 2023-02-18 15:37:15
    Admin State          : Up                   Traffic Statistics   : Disable
    BFD                  : Disable              Backup Hot-Standby   : Disable
    DiffServ-Mode        : -
    Active IGP Metric    : -
    Candidate-path Count : 1                    
    
    Candidate-path Preference: 200
    Path State           : Active               Path Type            : Primary
    Protocol-Origin      : PCEP(10)             Originator           : 0, 0.0.0.0
    Discriminator        : 200                  Binding SID          : -
    GroupId              : 2                    Policy Name          : policy200
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
    ```
12. Create a VPN instance and enable the IPv4 address family on each PE. Then, bind each PE's interface connected to a CE to the corresponding VPN instance.
    
    
    
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
    [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both evpn
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
    [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both evpn
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
13. Configure a tunnel selection policy on each PE to preferentially select an SR-MPLS TE Policy.
    
    
    
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
    [*PE1] ip vpn-instance vpna
    ```
    ```
    [*PE1-vpn-instance-vpna] evpn mpls routing-enable
    ```
    ```
    [*PE1-vpn-instance-vpna] ipv4-family
    ```
    ```
    [*PE1-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
    ```
    ```
    [*PE1-vpn-instance-vpna-af-ipv4] quit
    ```
    ```
    [*PE1-vpn-instance-vpna] quit
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
    [*PE2] ip vpn-instance vpna
    ```
    ```
    [*PE2-vpn-instance-vpna] evpn mpls routing-enable
    ```
    ```
    [*PE2-vpn-instance-vpna] ipv4-family
    ```
    ```
    [*PE2-vpn-instance-vpna-af-ipv4] tnl-policy p1 evpn
    ```
    ```
    [*PE2-vpn-instance-vpna-af-ipv4] quit
    ```
    ```
    [*PE2-vpn-instance-vpna] quit
    ```
    ```
    [*PE2] commit
    ```
14. Establish an EBGP peer relationship between each CE-PE pair.
    
    
    
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
    [*CE1-LoopBack1] ip address 10.11.1.1 32
    ```
    ```
    [*CE1-LoopBack1] quit
    ```
    ```
    [*CE1] interface gigabitethernet0/1/0
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] ip address 10.1.1.1 24
    ```
    ```
    [*CE1-GigabitEthernet0/1/0] quit
    ```
    ```
    [*CE1] bgp 65410
    ```
    ```
    [*CE1-bgp] peer 10.1.1.2 as-number 100
    ```
    ```
    [*CE1-bgp] network 10.11.1.1 32
    ```
    ```
    [*CE1-bgp] quit
    ```
    ```
    [*CE1] commit
    ```
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of CE2 is similar to the configuration of CE1. For detailed configurations, see Configuration Files.
    
    After completing the configuration, run the **display ip vpn-instance verbose** command on the PEs to check VPN instance configurations. Check that each PE can ping its connected CE.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If a PE has multiple interfaces bound to the same VPN instance, specify a source IP address using the **-a** *source-ip-address* parameter in the **ping -vpn-instance** *vpn-instance-name* **-a** *source-ip-address dest-ip-address* command to ping the CE that is connected to the remote PE. If the source IP address is not specified, the ping operation may fail.
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 100
    ```
    ```
    [~PE1-bgp] ipv4-family vpn-instance vpna
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
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configuration of PE2 is similar to the configuration of PE1. For detailed configurations, see Configuration Files.
    
    After completing the configuration, run the **display bgp vpnv4 vpn-instance peer** command on the PEs to check whether BGP peer relationships have been established between the PEs and CEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
    
    The following example uses the peer relationship between PE1 and CE1.
    
    ```
    [~PE1] display bgp vpnv4 vpn-instance vpna peer
    ```
    ```
     BGP local router ID : 1.1.1.9
     Local AS number : 100
    
     VPN-Instance vpna, Router ID 1.1.1.9:
     Total number of peers : 1                 Peers in established state : 1
    
      Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
      10.1.1.1        4       65410       91       90     0 01:15:39 Established        1
    ```
15. Verify the configuration.
    
    
    
    After completing the configuration, run the **display ip routing-table vpn-instance** command on each PE to check information about the loopback interface route toward a CE.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display ip routing-table vpn-instance vpna
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table: vpna
             Destinations : 7        Routes : 7
    Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
         10.1.1.0/24    Direct 0    0        D     10.1.1.2        GigabitEthernet0/2/0
         10.1.1.2/32    Direct 0    0        D     127.0.0.1       GigabitEthernet0/2/0
       10.1.1.255/32    Direct 0    0        D     127.0.0.1       GigabitEthernet0/2/0
        10.11.1.1/32     EBGP   255  0        RD    10.1.1.1        GigabitEthernet0/2/0
        10.22.2.2/32     IBGP   255  0        RD    3.3.3.9         policy200
          127.0.0.0/8   Direct 0    0        D     127.0.0.1       InLoopBack0
    255.255.255.255/32  Direct 0    0        D     127.0.0.1       InLoopBack0
    ```
    
    Run the **display ip routing-table vpn-instance vpna verbose** command on each PE to check details about the loopback interface route toward a CE.
    
    The following example uses the command output on PE1.
    
    ```
    [~PE1] display ip routing-table vpn-instance vpna 10.22.2.2 verbose
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpna
    Summary Count : 1
    
    Destination: 10.22.2.2/32         
         Protocol: IBGP               Process ID: 0              
       Preference: 255                      Cost: 0              
          NextHop: 3.3.3.9             Neighbour: 3.3.3.9
            State: Active Adv Relied         Age: 01h18m38s           
              Tag: 0                    Priority: low            
            Label: 48180                 QoSInfo: 0x0           
       IndirectID: 0x10000B9            Instance:                                 
     RelayNextHop: 0.0.0.0             Interface: policy200
         TunnelID: 0x000000003200000041 Flags: RD
    ```
    
    The command output shows that the VPN route has successfully recursed to the specified SR-MPLS TE Policy.
    
    CEs in the same VPN can ping each other. For example, CE1 can ping CE2 at 10.22.2.2.
    
    ```
    [~CE1] ping -a 10.11.1.1 10.22.2.2
    ```
    ```
      PING 10.22.2.2: 56  data bytes, press CTRL_C to break
        Reply from 10.22.2.2: bytes=56 Sequence=1 ttl=251 time=72 ms
        Reply from 10.22.2.2: bytes=56 Sequence=2 ttl=251 time=34 ms
        Reply from 10.22.2.2: bytes=56 Sequence=3 ttl=251 time=50 ms
        Reply from 10.22.2.2: bytes=56 Sequence=4 ttl=251 time=50 ms
        Reply from 10.22.2.2: bytes=56 Sequence=5 ttl=251 time=34 ms
      --- 10.22.2.2 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 34/48/72 ms  
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  te attribute enable
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.9
  #               
  mpls            
  #               
  segment-routing 
   on-demand color 200
    dynamic-computation-seq pcep
    constraint-template tp200
    candidate-path preference 100
  #               
  isis 1          
   is-level level-1
   cost-style wide
   bgp-ls enable level-1
   network-entity 10.0000.0000.0001.00
   traffic-eng level-1 
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.13.1.1 255.255.255.0
   isis enable 1  
   te metric 20
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.11.1.1 255.255.255.0
   isis enable 1  
   te metric 10
  #               
  interface GigabitEthernet0/1/8
   undo shutdown  
   ip address 10.3.1.1 255.255.255.0
   isis enable 1
  #               
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 10
  #               
  bgp 100         
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   peer 10.3.1.2 as-number 100
   #              
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
    peer 10.3.1.2 enable
   #
   link-state-family unicast
    peer 10.3.1.2 enable
   #              
   l2vpn-family evpn
    peer 3.3.3.9 enable
    peer 3.3.3.9 route-policy color100 export
    peer 3.3.3.9 advertise irb
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.1.1.1 as-number 65410
    advertise l2vpn evpn
  #
  segment-routing policy constraint-template tp200
   metric-type te
   max-cumulation te 20
  # 
  pce-client
   capability segment-routing
   connect-server 10.10.10.10
  #
  route-policy color100 permit node 1
   apply extcommunity color 0:100
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
  te attribute enable
  #
  mpls lsr-id 2.2.2.9
  #               
  mpls            
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-1 
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.11.1.2 255.255.255.0
   isis enable 1  
   te metric 10
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.12.1.1 255.255.255.0
   isis enable 1
   te metric 10
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.23.1.1 255.255.255.0
   isis enable 1 
   te metric 100
  #               
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 20
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  te attribute enable
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
    tnl-policy p1 evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 3.3.3.9
  #               
  mpls   
  #               
  segment-routing
   on-demand color 100
    dynamic-computation-seq pcep
    constraint-template tp100
    candidate-path preference 100
  #               
  isis 1          
   is-level level-1
   cost-style wide
   bgp-ls enable level-1
   network-entity 10.0000.0000.0003.00
   traffic-eng level-1 
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.14.1.2 255.255.255.0
   isis enable 1  
   te metric 20
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.12.1.2 255.255.255.0
   isis enable 1  
   te metric 10
  #               
  interface GigabitEthernet0/1/8
   undo shutdown  
   ip address 10.4.1.1 255.255.255.0
   isis enable 1 
  #               
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 30
  #               
  bgp 100         
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   peer 10.4.1.2 as-number 100 
   #              
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
    peer 10.4.1.2 enable
   #
   link-state-family unicast
    peer 10.4.1.2 enable
   #              
   l2vpn-family evpn
    peer 1.1.1.9 enable
    peer 1.1.1.9 route-policy color200 export
    peer 1.1.1.9 advertise irb
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    peer 10.2.1.1 as-number 65420
    advertise l2vpn evpn
  #
  segment-routing policy constraint-template tp100
   metric-type te
   max-cumulation te 20
  # 
  pce-client
   capability segment-routing
   connect-server 10.10.10.10
  #
  route-policy color200 permit node 1
   apply extcommunity color 0:200
  #               
  tunnel-policy p1
   tunnel select-seq sr-te-policy load-balance-number 1 unmix
  #
  evpn source-address 3.3.3.9
  #
  return
  ```
* P2 configuration file
  
  ```
  #
  sysname P2
  #
  te attribute enable
  #
  mpls lsr-id 4.4.4.9
  #               
  mpls            
  #               
  segment-routing 
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   traffic-eng level-1 
   segment-routing mpls
   segment-routing global-block 16000 23999
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.13.1.2 255.255.255.0
   isis enable 1  
   te metric 20
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ip address 10.14.1.1 255.255.255.0
   isis enable 1 
   te metric 20 
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ip address 10.23.1.2 255.255.255.0
   isis enable 1
   te metric 100
  #               
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1  
   isis prefix-sid index 40
  #
  return
  ```
* Controller configuration file
  
  ```
  #
  sysname Controller
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.2 255.255.255.0
  #               
  interface LoopBack1
   ip address 10.10.10.10 255.255.255.255
  #
  bgp 100
   peer 10.3.1.1 as-number 100
   peer 10.4.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 10.3.1.1 enable
    peer 10.4.1.1 enable
   #
   link-state-family unicast
    peer 10.3.1.1 enable
    peer 10.4.1.1 enable
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
   ip address 10.1.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 10.11.1.1 255.255.255.255
  #
  bgp 65410
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    network 10.11.1.1 255.255.255.255
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
   ip address 10.22.2.2 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.2 as-number 100
   #
   ipv4-family unicast
    network 10.22.2.2 255.255.255.255
    peer 10.2.1.2 enable
  #
  return
  ```