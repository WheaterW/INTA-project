Example for Configuring IP FPM Hop-by-Hop Performance Statistics Collection
===========================================================================

This section provides an example for configuring IP Flow Performance Monitor (FPM) hop-by-hop performance statistics collection.

#### Networking Requirements

As networks rapidly develop and applications become diversified, various value-added services are widely used. Link connectivity and network performance directly affect services carried over the networks. Therefore, performance measurement is especially important for service transmission channels.

* When voice services are deployed, users will not detect any change in the voice quality if the packet loss rate on links is lower than 5%. If the packet loss rate is higher than 10%, the voice quality will deteriorate significantly.
* Real-time services, such as VoIP, online games, and video conferencing, require a delay lower than 100 ms, or even 50 ms. As the delay increases, user experience worsens.

To meet higher quality requirements for real-time services, such as VoIP, online gaming, and online video, it is required that the network node where a performance fault occurs be quickly located when service quality deteriorates, so that the fault can be promptly rectified and user experience improved.

The IPRAN network shown in [Figure 1](#EN-US_TASK_0172372902__fig_dc_vrp_ipfpm_cfg_001401) transmits video services. A unidirectional service flow enters the network through the UPE, travels across SPE1, and leaves the network through the NPE.

To locate faults when network performance deteriorates, configure hop-by-hop packet loss and delay measurement on the UPE and NPE to locate faults segment by segment.

**Figure 1** IP FPM hop-by-hop performance statistics collection  
![](images/fig_dc_vrp_ipfpm_cfg_001401.png)

**Table 1** Interfaces connecting devices and their IP addresses
| Device (Role) | Interface Name | Interface | Remote Device (Role) | IP Address |
| --- | --- | --- | --- | --- |
| UPE (DCP1/MCP) | - | Loopback1 | - | 1.1.1.1/32 |
| interface1 | GE0/1/0 | eNodeB | 192.168.1.1/24 |
| interface2 | GE0/1/1 | SPE1 (DCP2) | 172.16.1.1/24 |
| interface3 | GE0/1/2 | SPE2 | 172.16.2.1/24 |
| SPE1 (DCP2) | - | Loopback1 | - | 2.2.2.2/32 |
| interface1 | GE0/1/1 | UPE (DCP1/MCP) | 172.16.1.2/24 |
| interface2 | GE0/1/2 | NPE (DCP3) | 172.16.4.1/24 |
| interface3 | GE0/1/3 | SPE2 | 172.16.3.1/24 |
| interface4 | GE0/1/4 | BITS | 172.16.6.1/24 |
| SPE2 | - | Loopback1 | - | 3.3.3.3/32 |
| interface1 | GE0/1/1 | NPE (DCP3) | 172.16.5.1/24 |
| interface2 | GE0/1/2 | UPE (DCP1/MCP) | 172.16.2.2/24 |
| interface3 | GE0/1/3 | SPE1 (DCP2) | 172.16.3.2/24 |
| NPE (DCP3) | - | Loopback1 | - | 4.4.4.4/32 |
| interface1 | GE0/1/1 | SPE2 | 172.16.5.2/24 |
| interface2 | GE0/1/2 | SPE1 (DCP2) | 172.16.4.2/24 |
| interface3 | GE0/1/3 | EPC | 192.168.2.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each interface so that all provider edge devices (PEs) can communicate at the network layer. This example uses Open Shortest Path First (OSPF) as the routing protocol.
2. Configure MPLS functions and public network tunnels to carry L3VPN services. In this example, RSVP-TE tunnels are established between the UPE and SPEs, and Label Distribution Protocol (LDP) LSPs are established between the SPEs and between the NPE and SPEs.
3. Create a VPN instance on the UPE and NPE and import the local direct routes on the UPE and NPE to their respective VPN instance routing tables.
4. Establish MP-IBGP peer relationships between the UPE and SPEs and between the NPE and SPEs.
5. Configure the SPEs as route reflectors (RRs) and specify the UPE and NPE as RR clients.
6. Configure VPN FRR on the UPE and NPE.
7. Configure the Network Time Protocol (1588v2) to synchronize the clocks of the UPE, SPE1, and the NPE.
8. Configure hop-by-hop packet loss and delay measurement on the UPE and NPE to locate faults segment by segment.
9. Configure the packet loss and two-way delay alarm thresholds and clear alarm thresholds on the UPE.


#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each interface listed in [Table 1](#EN-US_TASK_0172372902__tab_dc_vrp_ipfpm_cfg_001401)
* IGP type (OSPF), process ID (1), and area ID (0)
* Label switching router (LSR) IDs of the UPE (1.1.1.1), SPE1 (2.2.2.2), and SPE2 (3.3.3.3)
* Tunnel interface names (Tunnel11), tunnel IDs (100), and tunnel interface addresses (loopback interface addresses) for the forward and reverse tunnels between the UPE and SPE1
* Tunnel interface names (Tunnel12), tunnel IDs (200), and tunnel interface addresses (loopback interface addresses) for the forward and reverse tunnels between the UPE and SPE2
* Tunnel policy names (policy1) for the tunnels between the UPE and SPEs and tunnel selector names (BindTE) on the SPEs
* Name (vpna), RD (100:1), and VPN targets (1:1) of the VPN instances on the UPE and NPE
* UPE's DCP ID and MCP ID (both 1.1.1.1); SPE1's DCP ID (2.2.2.2); NPE's MCP ID (4.4.4.4)
* IP FPM instance ID (1) and statistical period (10s)
* Target flow's source IP address (10.1.1.1) and destination IP address (10.2.1.1)
* ACH1 {TLP100, TLP200} and ACH2 {TLP200, TLP310}
* Packet loss and delay measurement flags (respectively the third and fourth bits in the ToS field of the IPv4 packet header)![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Before you deploy IP FPM for packet loss and delay measurement, if two or more bits in the IPv4 packet header have not been planned for other purposes, they can be used for packet loss and delay measurement at the same time. If only one bit in the IPv4 packet header has not been planned, it can be used for either packet loss or delay measurement in one IP FPM instance.
* Authentication mode (HMAC-SHA256), password (YsHsjx\_202206), key ID (1), and UDP port number (2048) on the UPE, SPE, and NPE.
* Hop-by-hop packet loss and delay measurement intervals (30s)
* Packet loss alarm threshold and its clear alarm threshold (respectively 10% and 5%); two-way delay alarm threshold and its clear alarm threshold (respectively 100 ms and 50 ms)


#### Procedure

1. Configure interface IP addresses.
   
   
   
   Assign an IP address to each interface according to [Table 1](#EN-US_TASK_0172372902__tab_dc_vrp_ipfpm_cfg_001401) and create a loopback interface on each node. For configuration details, see [Configuration Files](#EN-US_TASK_0172372902__section_05) in this section.
2. Configure OSPF.
   
   
   
   Configure OSPF on each node to allow the nodes to communicate at the network layer. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172372902__section_05) in this section.
3. Configure basic MPLS functions and public network tunnels.
   
   
   * Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and Constraint Shortest Path First (CSPF).
     
     # Configure the UPE.
     
     ```
     <UPE> system-view
     ```
     ```
     [~UPE] mpls lsr-id 1.1.1.1
     ```
     ```
     [*UPE] mpls
     ```
     ```
     [*UPE-mpls] mpls te
     ```
     ```
     [*UPE-mpls] mpls rsvp-te
     ```
     ```
     [*UPE-mpls] mpls te cspf
     ```
     ```
     [*UPE-mpls] quit
     ```
     ```
     [*UPE] interface gigabitethernet 0/1/1
     ```
     ```
     [*UPE-GigabitEthernet0/1/1] mpls
     ```
     ```
     [*UPE-GigabitEthernet0/1/1] mpls te
     ```
     ```
     [*UPE-GigabitEthernet0/1/1] mpls rsvp-te
     ```
     ```
     [*UPE-GigabitEthernet0/1/1] quit
     ```
     ```
     [*UPE] interface gigabitethernet 0/1/2
     ```
     ```
     [*UPE-GigabitEthernet0/1/2] mpls
     ```
     ```
     [*UPE-GigabitEthernet0/1/2] mpls te
     ```
     ```
     [*UPE-GigabitEthernet0/1/2] mpls rsvp-te
     ```
     ```
     [*UPE-GigabitEthernet0/1/2] quit
     ```
     ```
     [*UPE] ospf 1
     ```
     ```
     [*UPE-ospf-1] opaque-capability enable
     ```
     ```
     [*UPE-ospf-1] area 0
     ```
     ```
     [*UPE-ospf-1-area-0.0.0.0] mpls-te enable
     ```
     ```
     [*UPE-ospf-1-area-0.0.0.0] quit
     ```
     ```
     [*UPE-ospf-1] quit
     ```
     ```
     [*UPE] commit
     ```
     
     # Configure SPE1.
     
     ```
     <SPE1> system-view
     ```
     ```
     [~SPE1] mpls lsr-id 2.2.2.2
     ```
     ```
     [*SPE1] mpls
     ```
     ```
     [*SPE1-mpls] mpls te
     ```
     ```
     [*SPE1-mpls] mpls rsvp-te
     ```
     ```
     [*SPE1-mpls] mpls te cspf
     ```
     ```
     [*SPE1-mpls] quit
     ```
     ```
     [*SPE1] mpls ldp
     ```
     ```
     [*SPE1-mpls-ldp] quit
     ```
     ```
     [*SPE1] interface gigabitethernet 0/1/1
     ```
     ```
     [*SPE1-GigabitEthernet0/1/1] mpls
     ```
     ```
     [*SPE1-GigabitEthernet0/1/1] mpls te
     ```
     ```
     [*SPE1-GigabitEthernet0/1/1] mpls rsvp-te
     ```
     ```
     [*SPE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*SPE1] interface gigabitethernet 0/1/3
     ```
     ```
     [*SPE1-GigabitEthernet0/1/3] mpls
     ```
     ```
     [*SPE1-GigabitEthernet0/1/3] mpls ldp
     ```
     ```
     [*SPE1-GigabitEthernet0/1/3] quit
     ```
     ```
     [*SPE1] ospf 1
     ```
     ```
     [*SPE1-ospf-1] opaque-capability enable
     ```
     ```
     [*SPE1-ospf-1] area 0
     ```
     ```
     [*SPE1-ospf-1-area-0.0.0.0] mpls-te enable
     ```
     ```
     [*SPE1-ospf-1-area-0.0.0.0] quit
     ```
     ```
     [*SPE1-ospf-1] quit
     ```
     ```
     [*SPE1] commit
     ```
     
     # Configure SPE2.
     
     ```
     <SPE2> system-view
     ```
     ```
     [~SPE2] mpls lsr-id 3.3.3.3
     ```
     ```
     [*SPE2] mpls
     ```
     ```
     [*SPE2-mpls] mpls te
     ```
     ```
     [*SPE2-mpls] mpls rsvp-te
     ```
     ```
     [*SPE2-mpls] mpls te cspf
     ```
     ```
     [*SPE2-mpls] quit
     ```
     ```
     [*SPE2] mpls ldp
     ```
     ```
     [*SPE2-mpls-ldp] quit
     ```
     ```
     [*SPE2] interface gigabitethernet 0/1/2
     ```
     ```
     [*SPE2-GigabitEthernet0/1/2] mpls
     ```
     ```
     [*SPE2-GigabitEthernet0/1/2] mpls te
     ```
     ```
     [*SPE2-GigabitEthernet0/1/2] mpls rsvp-te
     ```
     ```
     [*SPE2-GigabitEthernet0/1/2] quit
     ```
     ```
     [*SPE2] interface gigabitethernet 0/1/3
     ```
     ```
     [*SPE2-GigabitEthernet0/1/3] mpls
     ```
     ```
     [*SPE2-GigabitEthernet0/1/3] mpls ldp
     ```
     ```
     [*SPE2-GigabitEthernet0/1/3] quit
     ```
     ```
     [*SPE2] ospf 1
     ```
     ```
     [*SPE2-ospf-1] opaque-capability enable
     ```
     ```
     [*SPE2-ospf-1] area 0
     ```
     ```
     [*SPE2-ospf-1-area-0.0.0.0] mpls-te enable
     ```
     ```
     [*SPE2-ospf-1-area-0.0.0.0] quit
     ```
     ```
     [*SPE2-ospf-1] quit
     ```
     ```
     [*SPE2] commit
     ```
     
     # Configure NPE.
     
     ```
     <NPE> system-view
     ```
     ```
     [~NPE] mpls lsr-id 4.4.4.4
     ```
     ```
     [*NPE] mpls
     ```
     ```
     [*NPE-mpls] quit
     ```
     ```
     [*NPE] mpls ldp
     ```
     ```
     [*NPE-mpls-ldp] quit
     ```
     ```
     [*NPE] interface gigabitethernet 0/1/1
     ```
     ```
     [*NPE-GigabitEthernet0/1/1] mpls
     ```
     ```
     [*NPE-GigabitEthernet0/1/1] mpls ldp
     ```
     ```
     [*NPE-GigabitEthernet0/1/1] quit
     ```
     ```
     [*NPE] interface gigabitethernet 0/1/2
     ```
     ```
     [*NPE-GigabitEthernet0/1/2] mpls
     ```
     ```
     [*NPE-GigabitEthernet0/1/2] mpls ldp
     ```
     ```
     [*NPE-GigabitEthernet0/1/2] quit
     ```
     ```
     [*NPE] commit
     ```
   * Enable the egress of each unidirectional tunnel to be created to assign a non-null label to the penultimate hop.
     
     # Configure the UPE.
     ```
     [~UPE] mpls
     ```
     ```
     [*UPE-mpls] label advertise non-null
     ```
     ```
     [*UPE-mpls] quit
     ```
     ```
     [*UPE] commit
     ```
     
     # Configure SPE1.
     ```
     [~SPE1] mpls
     ```
     ```
     [*SPE1-mpls] label advertise non-null
     ```
     ```
     [*SPE1-mpls] quit
     ```
     ```
     [*SPE1] commit
     ```
     
     # Configure SPE2.
     ```
     [~SPE2] mpls
     ```
     ```
     [*SPE2-mpls] label advertise non-null
     ```
     ```
     [*SPE2-mpls] quit
     ```
     ```
     [*SPE2] commit
     ```
   * Configure MPLS TE tunnel interfaces.
     
     # Configure the UPE.
     
     ```
     [~UPE] interface Tunnel 11
     ```
     ```
     [*UPE-Tunnel11] ip address unnumbered interface loopback 1
     ```
     ```
     [*UPE-Tunnel11] tunnel-protocol mpls te
     ```
     ```
     [*UPE-Tunnel11] destination 2.2.2.2
     ```
     ```
     [*UPE-Tunnel11] mpls te tunnel-id 100
     ```
     ```
     [*UPE-Tunnel11] mpls te signal-protocol rsvp-te
     ```
     ```
     [*UPE-Tunnel11] mpls te reserved-for-binding
     ```
     ```
     [*UPE-Tunnel11] quit
     ```
     ```
     [*UPE] interface Tunnel 12
     ```
     ```
     [*UPE-Tunnel12] ip address unnumbered interface loopback 1
     ```
     ```
     [*UPE-Tunnel12] tunnel-protocol mpls te
     ```
     ```
     [*UPE-Tunnel12] destination 3.3.3.3
     ```
     ```
     [*UPE-Tunnel12] mpls te tunnel-id 200
     ```
     ```
     [*UPE-Tunnel12] mpls te signal-protocol rsvp-te
     ```
     ```
     [*UPE-Tunnel12] mpls te reserved-for-binding
     ```
     ```
     [*UPE-Tunnel12] quit
     ```
     ```
     [*UPE] commit
     ```
     
     # Configure SPE1.
     
     ```
     [~SPE1] interface Tunnel 11
     ```
     ```
     [*SPE1-Tunnel11] ip address unnumbered interface loopback 1
     ```
     ```
     [*SPE1-Tunnel11] tunnel-protocol mpls te
     ```
     ```
     [*SPE1-Tunnel11] destination 1.1.1.1
     ```
     ```
     [*SPE1-Tunnel11] mpls te tunnel-id 100
     ```
     ```
     [*SPE1-Tunnel11] mpls te signal-protocol rsvp-te
     ```
     ```
     [*SPE1-Tunnel11] mpls te reserved-for-binding
     ```
     ```
     [*SPE1-Tunnel11] quit
     ```
     ```
     [*SPE1] commit
     ```
     
     # Configure SPE2.
     
     ```
     [~SPE2] interface Tunnel 12
     ```
     ```
     [*SPE2-Tunnel12] ip address unnumbered interface loopback 1
     ```
     ```
     [*SPE2-Tunnel12] tunnel-protocol mpls te
     ```
     ```
     [*SPE2-Tunnel12] destination 1.1.1.1
     ```
     ```
     [*SPE2-Tunnel12] mpls te tunnel-id 200
     ```
     ```
     [*SPE2-Tunnel12] mpls te signal-protocol rsvp-te
     ```
     ```
     [*SPE2-Tunnel12] mpls te reserved-for-binding
     ```
     ```
     [*SPE2-Tunnel12] quit
     ```
     ```
     [*SPE2] commit
     ```
   * Configure tunnel policies.
     
     # Configure the UPE.
     
     ```
     [~UPE] tunnel-policy policy1
     ```
     ```
     [*UPE-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel 11
     ```
     ```
     [*UPE-tunnel-policy-policy1] tunnel binding destination 3.3.3.3 te Tunnel 12
     ```
     ```
     [*UPE-tunnel-policy-policy1] quit
     ```
     ```
     [*UPE] commit
     ```
     
     # Configure SPE1.
     
     ```
     [~SPE1] tunnel-policy policy1
     ```
     ```
     [*SPE1-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel 11
     ```
     ```
     [*SPE1-tunnel-policy-policy1] quit
     ```
     ```
     [*SPE1] commit
     ```
     
     # Configure SPE2.
     
     ```
     [~SPE2] tunnel-policy policy1
     ```
     ```
     [*SPE2-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel 12
     ```
     ```
     [*SPE2-tunnel-policy-policy1] quit
     ```
     ```
     [*SPE2] commit
     ```
4. Create a VPN instance on the UPE and NPE and import the local direct routes on the UPE and NPE to their respective VPN instance routing tables.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpna
   ```
   ```
   [*UPE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] vpn-target 1:1
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*UPE-vpn-instance-vpna] quit
   ```
   ```
   [*UPE] interface gigabitethernet 0/1/0
   ```
   ```
   [*UPE-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*UPE-GigabitEthernet0/1/0] ip address 192.168.1.1 24
   ```
   ```
   [*UPE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*UPE] bgp 100
   ```
   ```
   [*UPE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*UPE-bgp-vpna] import-route direct
   ```
   ```
   [*UPE-bgp-vpna] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] ip vpn-instance vpna
   ```
   ```
   [*NPE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*NPE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*NPE-vpn-instance-vpna-af-ipv4] vpn-target 1:1
   ```
   ```
   [*NPE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*NPE-vpn-instance-vpna] quit
   ```
   ```
   [*NPE] interface gigabitethernet 0/1/3
   ```
   ```
   [*NPE-GigabitEthernet0/1/3] ip binding vpn-instance vpna
   ```
   ```
   [*NPE-GigabitEthernet0/1/3] ip address 192.168.2.1 24
   ```
   ```
   [*NPE-GigabitEthernet0/1/3] quit
   ```
   ```
   [*NPE] bgp 100
   ```
   ```
   [*NPE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*NPE-bgp-vpna] import-route direct
   ```
   ```
   [*NPE-bgp-vpna] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
5. Establish MP-IBGP peer relationships between the UPE and SPEs and between the NPE and SPEs.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bgp 100
   ```
   ```
   [*UPE-bgp] router-id 1.1.1.1
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*UPE-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*UPE-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*UPE-bgp] ipv4-family vpnv4
   ```
   ```
   [*UPE-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*UPE-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*UPE-bgp-af-vpnv4] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure SPE1.
   
   ```
   [~SPE1] bgp 100
   ```
   ```
   [*SPE1-bgp] router-id 2.2.2.2
   ```
   ```
   [*SPE1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*SPE1-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*SPE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*SPE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*SPE1-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*SPE1-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*SPE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*SPE1-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 4.4.4.4 enable
   ```
   ```
   [*SPE1-bgp-af-vpnv4] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to the configuration of SPE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172372902__section_05) in this section.
   
   # Configure the NPE.
   
   ```
   [~NPE] bgp 100
   ```
   ```
   [*NPE-bgp] router-id 4.4.4.4
   ```
   ```
   [*NPE-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*NPE-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*NPE-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*NPE-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*NPE-bgp] ipv4-family vpnv4
   ```
   ```
   [*NPE-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*NPE-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*NPE-bgp-af-vpnv4] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
6. Configure SPEs as RRs and specify UPEs and NPEs as RR clients. This step uses SPE1 as an example.
   
   
   ```
   [~SPE1] bgp 100
   ```
   ```
   [*SPE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 1.1.1.1 reflect-client
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 1.1.1.1 next-hop-local
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 4.4.4.4 reflect-client
   ```
   ```
   [*SPE1-bgp-af-vpnv4] peer 4.4.4.4 next-hop-local
   ```
   ```
   [*SPE1-bgp-af-vpnv4] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
7. Apply the tunnel policy on the UPE and configure a tunnel selector on each SPE because SPEs do not have VPN instances, so that the UPE and SPEs use RSVP-TE tunnels to transmit traffic.
   
   
   
   # Apply the tunnel policy on the UPE.
   
   ```
   [~UPE] ip vpn-instance vpna
   ```
   ```
   [*UPE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] tnl-policy policy1
   ```
   ```
   [*UPE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*UPE-vpn-instance-vpna] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure a tunnel selector on SPE1 to use TE tunnels to transmit traffic.
   
   ```
   [~SPE1] tunnel-selector bindTE permit node 10
   ```
   ```
   [*SPE1-tunnel-selector] apply tunnel-policy policy1
   ```
   ```
   [*SPE1-tunnel-selector] quit
   ```
   ```
   [*SPE1] bgp 100
   ```
   ```
   [*SPE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*SPE1-bgp-af-vpnv4] tunnel-selector bindTE
   ```
   ```
   [*SPE1-bgp-af-vpnv4] quit
   ```
   ```
   [*SPE1-bgp] quit
   ```
   ```
   [*SPE1] commit
   ```
   
   The configuration of SPE2 is similar to the configuration of SPE1. For configuration details, see [Configuration Files](#EN-US_TASK_0172372902__section_05).
8. Configure VPN FRR on the UPE and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bgp 100
   ```
   ```
   [*UPE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*UPE-bgp-vpna] auto-frr
   ```
   ```
   [*UPE-bgp-vpna] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   
   After completing the configurations, run the [**display bgp vpnv4 vpn-instance vpna routing-table**](cmdqueryname=display+bgp+vpnv4+vpn-instance+vpna+routing-table) command on the UPE and NPE to view detailed information about received routes.
   ```
   [~UPE] display bgp vpnv4 vpn-instance vpna routing-table
   ```
   ```
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    VPN-Instance vpna, Router ID 1.1.1.1:
   
    Total Number of Routes: 4
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   192.168.1.0/24       0.0.0.0         0                     0      ?
    *>   192.168.1.1/32       0.0.0.0         0                     0      ?
    *>i  192.168.2.0/24       2.2.2.2         0          100        0      ?
    * i                       3.3.3.3         0          100        0      ? 
   ```
   ```
   [~NPE] display bgp vpnv4 vpn-instance vpna routing-table
   ```
   ```
    BGP Local router ID is 4.4.4.4
    Status codes: * - valid, > - best, d - damped,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    VPN-Instance vpna, Router ID 4.4.4.4:
   
    Total Number of Routes: 4
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  192.168.1.0/24       2.2.2.2         0          100        0      ?
    * i                       3.3.3.3         0          100        0      ?
    *>   192.168.2.0/24       0.0.0.0         0                     0      ?
    *>   192.168.2.1/32       0.0.0.0         0                     0      ?
   ```
   
   The command output shows that the UPE and NPE both preferentially select the routes advertised by SPE1 and use UPE-SPE1-NPE as the primary path.
9. Configure 1588v2 to synchronize the clocks of the UPE, SPE1, and the NPE.
   
   
   1. # Import BITS0 signals to SPE1.
      
      ```
      [~SPE1] clock bits-type bits0 2mhz
      ```
      ```
      [*SPE1] clock source bits0 synchronization enable
      ```
      ```
      [*SPE1] clock source bits0 priority 1
      ```
      ```
      [*SPE1] commit
      ```
   2. # Enable 1588v2 globally.
      
      # Configure SPE1.
      ```
      [~SPE1] ptp enable 
      ```
      ```
      [*SPE1] ptp domain 1 
      ```
      ```
      [*SPE1] ptp device-type bc
      ```
      ```
      [*SPE1] ptp clock-source local clock-class 185
      ```
      ```
      [*SPE1] clock source ptp synchronization enable
      ```
      ```
      [*SPE1] clock source ptp priority 1
      ```
      ```
      [*SPE1] commit
      ```
      
      # Configure UPE.
      ```
      [~UPE] ptp enable 
      ```
      ```
      [*UPE] ptp domain 1 
      ```
      ```
      [*UPE] ptp device-type bc
      ```
      ```
      [*UPE] ptp clock-source local clock-class 185
      ```
      ```
      [*UPE] clock source ptp synchronization enable
      ```
      ```
      [*UPE] clock source ptp priority 1
      ```
      ```
      [*UPE] commit
      ```
      
      # Configure NPE.
      ```
      [~NPE] ptp enable 
      ```
      ```
      [*NPE] ptp domain 1 
      ```
      ```
      [*NPE] ptp device-type bc
      ```
      ```
      [*NPE] ptp clock-source local clock-class 185
      ```
      ```
      [*NPE] clock source ptp synchronization enable
      ```
      ```
      [*NPE] clock source ptp priority 1
      ```
      ```
      [*NPE] commit
      ```
   3. Enable 1588v2 on an interface.
      
      # Configure SPE1.
      ```
      [~SPE1] interface gigabitethernet 0/1/1
      ```
      ```
      [~SPE1-GigabitEthernet0/1/1] ptp enable
      ```
      ```
      [*SPE1-GigabitEthernet0/1/1] commit
      ```
      ```
      [~SPE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [~SPE1] interface gigabitethernet 0/1/2
      ```
      ```
      [~SPE1-GigabitEthernet0/1/2] ptp enable
      ```
      ```
      [*SPE1-GigabitEthernet0/1/2] commit
      ```
      ```
      [~SPE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [~SPE1] interface gigabitethernet 0/1/4
      ```
      ```
      [~SPE1-GigabitEthernet0/1/4] ptp enable
      ```
      ```
      [*SPE1-GigabitEthernet0/1/4] commit
      ```
      ```
      [~SPE1-GigabitEthernet0/1/4] quit
      ```
      
      # Configure UPE.
      ```
      [~UPE] interface gigabitethernet 0/1/0
      ```
      ```
      [~UPE-GigabitEthernet0/1/0] ptp enable
      ```
      ```
      [*UPE-GigabitEthernet0/1/0] commit
      ```
      ```
      [~UPE-GigabitEthernet0/1/0] quit
      ```
      ```
      [~UPE] interface gigabitethernet 0/1/1
      ```
      ```
      [~UPE-GigabitEthernet0/1/1] ptp enable
      ```
      ```
      [*UPE-GigabitEthernet0/1/1] commit
      ```
      ```
      [~UPE-GigabitEthernet0/1/1] quit
      ```
      
      # Configure NPE.
      ```
      [~NPE] interface gigabitethernet 0/1/2
      ```
      ```
      [~NPE-GigabitEthernet0/1/2] ptp enable
      ```
      ```
      [*NPE-GigabitEthernet0/1/2] commit
      ```
      ```
      [~NPE-GigabitEthernet0/1/2] quit
      ```
      ```
      [~NPE] interface gigabitethernet 0/1/3
      ```
      ```
      [~NPE-GigabitEthernet0/1/3] ptp enable
      ```
      ```
      [*NPE-GigabitEthernet0/1/3] commit
      ```
      ```
      [~NPE-GigabitEthernet0/1/3] quit
      ```
10. Configure hop-by-hop packet loss and delay measurement on the UPE, SPE1, and the NPE; configure two ACHs on the link between the UPE and NPE: ACH1 {TLP100, TLP200} and ACH2 {TLP200, TLP310}.
    
    # Configure UPE.
    * Configure the MCP.
      ```
      [~UPE] nqa ipfpm mcp
      ```
      ```
      [*UPE-nqa-ipfpm-mcp] mcp id 1.1.1.1
      ```
      ```
      [*UPE-nqa-ipfpm-mcp] protocol udp port 2048
      ```
      ```
      [*UPE-nqa-ipfpm-mcp] authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
      ```
      ```
      [*UPE-nqa-ipfpm-mcp] instance 1
      ```
      ```
      [*UPE-nqa-ipfpm-mcp] description Instanceforpoint-by-pointtest
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1] dcp 1.1.1.1
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1] dcp 2.2.2.2
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1] dcp 4.4.4.4
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1] ach 1
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-1] flow forward
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-1] in-group dcp 1.1.1.1 tlp 100
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-1] out-group dcp 2.2.2.2 tlp 200
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-1] quit
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1] ach 2
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-2] flow forward
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-2] in-group dcp 2.2.2.2 tlp 200
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-2] out-group dcp 4.4.4.4 tlp 310
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1-ach-2] quit
      ```
      ```
      [*UPE-nqa-ipfpm-mcp-instance-1] quit
      ```
      ```
      [*UPE-nqa-ipfpm-mcp] quit
      ```
      ```
      [*UPE] commit
      ```
      
      After completing the configuration, run the [**display ipfpm mcp**](cmdqueryname=display+ipfpm+mcp) command on the UPE. The command output shows MCP configurations on the UPE.
      ```
      [~UPE] display ipfpm mcp
      ```
      ```
      Specification Information:
       Max Instance Number                       :64
       Max DCP Number Per Instance               :256
       Max ACH Number Per Instance               :16
       Max TLP Number Per ACH                    :16
      
      Configuration Information:
       MCP ID                                    :1.1.1.1
       Status                                    :Active
       Protocol Port                             :2048
       Current Instance Number                   :1
      ```
    * Configure a DCP.
      ```
      [~UPE] nqa ipfpm dcp
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] dcp id 1.1.1.1
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] mcp 1.1.1.1 port 2048
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] color-flag loss-measure tos-bit 3 delay-measure tos-bit 4
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] instance 1
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] description Instanceforpointbypointtest
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] interval 10
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] flow forward source 10.1.1.1 destination 10.2.1.1
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] tlp 100 in-point ingress
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] quit
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] quit
      ```
      ```
      [*UPE] commit
      ```
      
      After completing the configuration, run the [**display ipfpm dcp**](cmdqueryname=display+ipfpm+dcp) command on the UPE. The command output shows DCP configurations on the UPE.
      ```
      [~UPE] display ipfpm dcp
      ```
      ```
      Specification Information(Main Board):
       Max Instance Number                       :64
       Max 10s Instance Number                   :64
       Max 1s Instance Number                    :--
       Max TLP Number                            :512
       Max TLP Number Per Instance               :8
      
      Configuration Information:
       DCP ID                                    : 1.1.1.1
       Loss-measure Flag                         : tos-bit3
       Delay-measure Flag                        : tos-bit4
       Authentication Mode                       : hmac-sha256
       Test Instances MCP ID                     : 1.1.1.1
       Test Instances MCP Port                   : 2048
       Current Instance Number                   : 1
      ```
    * Bind the TLP to an interface.
      ```
      [~UPE] interface GigabitEthernet0/1/0
      ```
      ```
      [~UPE-GigabitEthernet0/1/0] ipfpm tlp 100
      ```
      ```
      [*UPE-GigabitEthernet0/1/0] quit
      ```
      ```
      [*UPE] commit
      ```
    * Enable hop-by-hop packet loss and delay measurement.
      ```
      [~UPE] nqa ipfpm dcp
      ```
      ```
      [*UPE-nqa-ipfpm-dcp] instance 1
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] loss-measure enable time-range 30
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] delay-measure enable one-way tlp 100 time-range 30
      ```
      ```
      [*UPE-nqa-ipfpm-dcp-instance-1] commit
      ```
    # Configure SPE1.
    * Configure a DCP.
      ```
      [~SPE1] nqa ipfpm dcp
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] dcp id 2.2.2.2
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] color-flag loss-measure tos-bit 3 delay-measure tos-bit 4
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] mcp 1.1.1.1 port 2048
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] instance 1
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] description Instanceforpointbypointtest
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] interval 10
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] flow forward source 10.1.1.1 destination 10.2.1.1
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] tlp 200 mid-point flow forward ingress vpn-label 17 lsp-label 18
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] quit
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] quit
      ```
      ```
      [*SPE1] commit
      ```
      
      After completing the configuration, run the [**display ipfpm dcp**](cmdqueryname=display+ipfpm+dcp) command on SPE1. The command output shows DCP configurations on SPE1.
      ```
      [~SPE1] display ipfpm dcp
      ```
      ```
      Specification Information(Main Board):
       Max Instance Number                       :64
       Max 10s Instance Number                   :64
       Max 1s Instance Number                    :--
       Max TLP Number                            :512
       Max TLP Number Per Instance               :8
      
      Configuration Information:
       DCP ID                                    : 2.2.2.2
       Loss-measure Flag                         : tos-bit3
       Delay-measure Flag                        : tos-bit4
       Authentication Mode                       : hmac-sha256
       Test Instances MCP ID                     : 1.1.1.1
       Test Instances MCP Port                   : 2048
       Current Instance Number                   : 1 
      ```
    * Bind the TLP to an interface.
      ```
      [~SPE1] interface GigabitEthernet0/1/1
      ```
      ```
      [~SPE1-GigabitEthernet0/1/1] ipfpm tlp 200
      ```
      ```
      [*SPE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*SPE1] commit
      ```
    * Enable hop-by-hop packet loss and delay measurement.
      ```
      [~SPE1] nqa ipfpm dcp
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp] instance 1
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] loss-measure enable mid-point time-range 30
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] delay-measure enable one-way tlp mid-point time-range 30
      ```
      ```
      [*SPE1-nqa-ipfpm-dcp-instance-1] commit
      ```
    # Configure the NPE.
    * Configure a DCP.
      ```
      [~NPE] nqa ipfpm dcp
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] dcp id 4.4.4.4
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] authentication-mode hmac-sha256 key-id 1 cipher YsHsjx_202206
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] color-flag loss-measure tos-bit 3 delay-measure tos-bit 4
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] mcp 1.1.1.1 port 2048
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] instance 1
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] description Instanceforpointbypointtest
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] interval 10
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] flow forward source 10.1.1.1 destination 10.2.1.1
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] tlp 310 out-point egress
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] quit
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] quit
      ```
      ```
      [*NPE] commit
      ```
      
      After completing the configuration, run the [**display ipfpm dcp**](cmdqueryname=display+ipfpm+dcp) command on the NPE. The command output shows DCP configurations on the NPE.
      ```
      [~NPE] display ipfpm dcp
      ```
      ```
      Specification Information(Main Board):
       Max Instance Number                       :64
       Max 10s Instance Number                   :64
       Max 1s Instance Number                    :--
       Max TLP Number                            :512
       Max TLP Number Per Instance               :8
      
      Configuration Information:
       DCP ID                                    : 4.4.4.4
       Loss-measure Flag                         : tos-bit3
       Delay-measure Flag                        : tos-bit4
       Authentication Mode                       : hmac-sha256
       Test Instances MCP ID                     : 1.1.1.1
       Test Instances MCP Port                   : 2048
       Current Instance Number                   : 1
      ```
    * Bind the TLPs to interfaces.
      ```
      [*NPE] interface GigabitEthernet0/1/3
      ```
      ```
      [*NPE-GigabitEthernet0/1/3] ipfpm tlp 310
      ```
      ```
      [*NPE-GigabitEthernet0/1/3] quit
      ```
      ```
      [*NPE] commit
      ```
    * Enable hop-by-hop packet loss and delay measurement.
      ```
      [~NPE] nqa ipfpm dcp
      ```
      ```
      [*NPE-nqa-ipfpm-dcp] instance 1
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] loss-measure enable time-range 30
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] delay-measure enable one-way tlp 310 time-range 30
      ```
      ```
      [*NPE-nqa-ipfpm-dcp-instance-1] commit
      ```
11. Configure alarm thresholds and clear alarm thresholds for IP FPM performance counters on the UPE.
    
    # Configure the packet loss alarm threshold and its clear alarm threshold.
    ```
    [~UPE] nqa ipfpm mcp
    ```
    ```
    [*UPE-nqa-ipfpm-mcp] instance 1
    ```
    ```
    [*UPE-nqa-ipfpm-mcp-instance-1] loss-measure ratio-threshold upper-limit 10 lower-limit 5
    ```
    ```
    [*UPE-nqa-ipfpm-mcp-instance-1] commit
    ```
    
    # Configure the two-way delay alarm threshold and its clear alarm threshold.
    ```
    [~UPE-nqa-ipfpm-mcp-instance-1] delay-measure two-way delay-threshold upper-limit 100000 lower-limit 50000
    ```
    ```
    [*UPE-nqa-ipfpm-mcp-instance-1] commit
    ```
12. Verify the configuration.
    
    Run the [**display ipfpm statistic-type**](cmdqueryname=display+ipfpm+statistic-type) { **loss** | **oneway-delay** } **instance** *instance-id* **ach** *ach-id* command on the UPE to check the performance statistics for a specified IP FPM instance.
    * # The following example uses the packet loss statistics for ACH1.
      
      ```
      [~UPE] display ipfpm statistic-type loss instance 1 ach 1
      ```
      ```
      Latest loss statistics of forward flow:
      Unit: p - packet, b - byte
      ------------------------------------------------------------------------------------------
       Period               Loss(p)              LossRatio(p)  Loss(b)              LossRatio(b)
      ------------------------------------------------------------------------------------------
       136190088            10                   10.000000%    1000                 10.000000%
       136190087            10                   10.000000%    1000                 10.000000%
       136190086            10                   10.000000%    1000                 10.000000%
       136190085            10                   10.000000%    1000                 10.000000%
       136190084            10                   10.000000%    1000                 10.000000%
       136190083            10                   10.000000%    1000                 10.000000%
       136190082            10                   10.000000%    1000                 10.000000%
      
      Latest loss statistics of backward flow:
      Unit: p - packet, b - byte
      ------------------------------------------------------------------------------------------
       Period               Loss(p)              LossRatio(p)  Loss(b)              LossRatio(b)
      ------------------------------------------------------------------------------------------
      ```
    * # The following example uses the delay statistics for ACH1.
      ```
      [~UPE] display ipfpm statistic-type oneway-delay instance 1 ach 1
      ```
      ```
      Latest one-way delay statistics of forward flow:
      --------------------------------------------------
       Period               Delay(usec) Delay
                                        Variation(usec)
      --------------------------------------------------
       136190120            100         0
       136190119            100         0
       136190118            100         0
       136190117            100         0
       136190116            100         0
       136190115            100         0
       136190114            100         0
      
      Latest one-way delay statistics of backward flow:
      --------------------------------------------------
       Period               Delay(usec) Delay
                                        Variation(usec)
      --------------------------------------------------
      ```

#### Configuration Files

* UPE configuration file
  
  ```
  #                                                                               
  sysname UPE                                                                 
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  ptp clock-source local clock-class 185
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #                                                                               
  ip vpn-instance vpna                                                            
   ipv4-family                                                                    
    route-distinguisher 100:1
    apply-label per-instance                                                   
    tnl-policy policy1                                                            
    vpn-target 1:1 export-extcommunity                                            
    vpn-target 1:1 import-extcommunity                                            
  #                                                                               
  mpls lsr-id 1.1.1.1                                                             
  mpls                                                                            
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls te cspf                                                                   
  #                                                                               
  ntp-service sync-interval 180                    
  ntp-service refclock-master 1                                                   
  #                                                                               
  interface GigabitEthernet0/1/0                                                 
   undo shutdown                                                                  
   ip binding vpn-instance vpna                                                   
   ip address 192.168.1.1 255.255.255.0                                             
   ptp enable
   ipfpm tlp 100                                                                 
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 172.16.1.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 172.16.2.1 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface LoopBack1                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 2.2.2.2                                                            
   mpls te tunnel-id 100                                                          
   mpls te reserved-for-binding                                                   
  #                                                                               
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 3.3.3.3                                                            
   mpls te tunnel-id 200                                                          
   mpls te reserved-for-binding                                                   
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.1                                                              
   peer 2.2.2.2 as-number 100                                                     
   peer 2.2.2.2 connect-interface LoopBack1                                       
   peer 3.3.3.3 as-number 100                                                     
   peer 3.3.3.3 connect-interface LoopBack1                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization
    peer 2.2.2.2 enable                                                           
    peer 3.3.3.3 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    policy vpn-target                                                             
    peer 2.2.2.2 enable                                                           
    peer 3.3.3.3 enable                                                           
   #                                                                              
   ipv4-family vpn-instance vpna                                                  
    import-route direct                                                           
    auto-frr                                                                      
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 1.1.1.1 0.0.0.0                                                       
    network 172.16.1.0 0.0.0.255                                                   
    network 172.16.2.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 2.2.2.2 te Tunnel11                              
   tunnel binding destination 3.3.3.3 te Tunnel12                              
  #                                                                               
  nqa ipfpm dcp                                                                   
   dcp id 1.1.1.1                                                                 
   mcp 1.1.1.1 port 2048                                                          
   authentication-mode hmac-sha256 key-id 1 cipher #%#%=%uP:z;!;4\TdYHU#$z/1IR]#%#%
   color-flag loss-measure tos-bit 3 delay-measure tos-bit 4 
   instance 1                                                                     
    description Instanceforpointbypointtest                                       
    flow forward source 10.1.1.1 destination 10.2.1.1                           
    tlp 100 in-point ingress                                                               
  #                                                                               
  nqa ipfpm mcp                                                                   
   mcp id 1.1.1.1                                                                 
   protocol udp port 2048                                                         
   authentication-mode hmac-sha256 key-id 1 cipher #%#%i`R<<=hGt>i:|a;Ypy%~1E(U#%#%
   instance 1                                                                     
    description Instanceforpoint-by-pointtest                                     
    dcp 1.1.1.1     
    dcp 2.2.2.2    
    dcp 4.4.4.4   
    loss-measure ratio-threshold upper-limit 10.000000 lower-limit 5.000000       
    delay-measure two-way delay-threshold upper-limit 100000 lower-limit 50000    
    ach 1   
     flow forward      
     in-group dcp 1.1.1.1 tlp 100                                             
     out-group dcp 2.2.2.2 tlp 200                                           
    ach 2                                                                         
     flow forward                                                                 
     in-group dcp 2.2.2.2 tlp 200                                           
     out-group dcp 4.4.4.4 tlp 310                                          
  #                                                                               
  return 
  ```
* SPE1 configuration file
  
  ```
  #                                                                               
  sysname SPE1                                                                 
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  ptp clock-source local clock-class 185
  #
  clock source bits0 synchronization enable
  clock source bits0 priority 1
  clock source ptp synchronization enable
  clock source ptp priority 1
  clock bits-type bits0 2mhz
  #                                                                               
  tunnel-selector bindTE permit node 10                                           
   apply tunnel-policy policy1                                                    
  #                                                                               
  mpls lsr-id 2.2.2.2                                                             
  mpls                                                                            
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls te cspf                                                                   
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  ntp-service sync-interval 180                    
  ntp-service unicast-server 172.16.1.1                                            
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 172.16.1.2 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
   ptp enable
   ipfpm tlp 200                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 172.16.4.1 255.255.255.0                                             
   mpls                                                                           
   mpls ldp                                                                       
   ptp enable
  #                                                                               
  interface GigabitEthernet0/1/3                                                  
   undo shutdown                                                                  
   ip address 172.16.3.1 255.255.255.0                                             
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/4                                                  
   undo shutdown                                                                  
   ip address 172.16.6.1 255.255.255.0                                             
   ptp enable
  #                                                                               
  interface LoopBack1                                                             
   ip address 2.2.2.2 255.255.255.255                                                 
  #                                                                               
  interface Tunnel11                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 100                                                          
   mpls te reserved-for-binding                                                   
  #                                                                               
  bgp 100                                                                         
   router-id 2.2.2.2                                                              
   peer 1.1.1.1 as-number 100                                                     
   peer 1.1.1.1 connect-interface LoopBack1                                       
   peer 3.3.3.3 as-number 100                                                     
   peer 3.3.3.3 connect-interface LoopBack1                                       
   peer 4.4.4.4 as-number 100                                                     
   peer 4.4.4.4 connect-interface LoopBack1                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization
    peer 1.1.1.1 enable                                                           
    peer 3.3.3.3 enable                                                           
    peer 4.4.4.4 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    undo policy vpn-target                                                        
    tunnel-selector bindTE                                                        
    peer 1.1.1.1 enable                                                           
    peer 1.1.1.1 reflect-client                                                   
    peer 1.1.1.1 next-hop-local                                                   
    peer 3.3.3.3 enable                                                           
    peer 4.4.4.4 enable                                                           
    peer 4.4.4.4 reflect-client                                                   
    peer 4.4.4.4 next-hop-local                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 2.2.2.2 0.0.0.0                                                       
    network 172.16.1.0 0.0.0.255                                                   
    network 172.16.3.0 0.0.0.255                                                   
    network 172.16.4.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel11                              
  #                                                                               
  nqa ipfpm dcp                                                                   
   dcp id 2.2.2.2                                                                 
   mcp 1.1.1.1 port 2048                                                          
   authentication-mode hmac-sha256 key-id 1 cipher #%#%/#(8ARUz1+=(sUrXdsM1P.x#%#% 
   color-flag loss-measure tos-bit 3 delay-measure tos-bit 4 
   instance 1                                                                     
    description Instanceforpointbypointtest                                       
    flow forward source 10.1.1.1 destination 10.2.1.1                           
    tlp 200 mid-point flow forward ingress vpn-label 17 lsp-label 18  
  #                                                                               
  return
  ```
* SPE2 configuration file
  
  ```
  #                                                                               
  sysname SPE2                                                                 
  #                                                                               
  tunnel-selector bindTE permit node 10                                           
   apply tunnel-policy policy1                                                    
  #                                                                               
  mpls lsr-id 3.3.3.3                                                             
  mpls                                                                            
   mpls te                                                                        
   label advertise non-null                                                       
   mpls rsvp-te                                                                   
   mpls te cspf                                                                   
  #                                                                               
  mpls ldp                                                                        
  #                                                                               
  interface GigabitEthernet0/1/1                                                  
   undo shutdown                                                                  
   ip address 172.16.5.1 255.255.255.0                                             
   mpls                                                                           
   mpls ldp                                                                       
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   undo shutdown                                                                  
   ip address 172.16.2.2 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
   mpls rsvp-te                                                                   
  #                                                                               
  interface GigabitEthernet0/1/3                                                  
   undo shutdown                                                                  
   ip address 172.16.3.2 255.255.255.0                                             
   mpls                                                                           
   mpls te                                                                        
   mpls ldp                                                                       
  #                                                                               
  interface LoopBack1                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                               
  interface Tunnel12                                                           
   ip address unnumbered interface LoopBack1                                      
   tunnel-protocol mpls te                                                        
   destination 1.1.1.1                                                            
   mpls te tunnel-id 200                                                          
   mpls te reserved-for-binding                                                   
  #                                                                               
  bgp 100                                                                         
   router-id 3.3.3.3                                                              
   peer 1.1.1.1 as-number 100                                                     
   peer 1.1.1.1 connect-interface LoopBack1                                       
   peer 2.2.2.2 as-number 100                                                     
   peer 2.2.2.2 connect-interface LoopBack1                                       
   peer 4.4.4.4 as-number 100                                                     
   peer 4.4.4.4 connect-interface LoopBack1                                       
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization
    peer 1.1.1.1 enable                                                           
    peer 2.2.2.2 enable                                                           
    peer 4.4.4.4 enable                                                           
   #                                                                              
   ipv4-family vpnv4                                                              
    undo policy vpn-target                                                        
    tunnel-selector bindTE                                                        
    peer 1.1.1.1 enable                                                           
    peer 1.1.1.1 reflect-client                                                   
    peer 1.1.1.1 next-hop-local                                                   
    peer 2.2.2.2 enable                                                           
    peer 4.4.4.4 enable                                                           
    peer 4.4.4.4 reflect-client                                                   
    peer 4.4.4.4 next-hop-local                                                   
  #                                                                               
  ospf 1                                                                          
   opaque-capability enable                                                       
   area 0.0.0.0                                                                   
    network 3.3.3.3 0.0.0.0                                                       
    network 172.16.2.0 0.0.0.255                                                   
    network 172.16.3.0 0.0.0.255                                                   
    network 172.16.5.0 0.0.0.255                                                   
    mpls-te enable                                                                
  #                                                                               
  tunnel-policy policy1                                                           
   tunnel binding destination 1.1.1.1 te Tunnel12                              
  #                                                                               
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  ptp enable
  ptp domain 1
  ptp device-type bc
  ptp clock-source local clock-class 185
  #
  clock source ptp synchronization enable
  clock source ptp priority 1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  mpls
  #
  mpls ldp
  #
  ntp-service sync-interval 180
  ntp-service unicast-server 172.16.4.1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.5.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.4.2 255.255.255.0
   mpls
   mpls ldp
   ptp enable
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip binding vpn-instance vpna
   ip address 192.168.2.1 255.255.255.0
   ptp enable
   ipfpm tlp 310
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   router-id 4.4.4.4
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    auto-frr
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 172.16.4.0 0.0.0.255
    network 172.16.5.0 0.0.0.255
  #
  nqa ipfpm dcp
   dcp id 4.4.4.4
   mcp 1.1.1.1 port 2048
   authentication-mode hmac-sha256 key-id 1 cipher #%#%Se9P>q>D>~v\Es$K{z2H1VW##%#%
   color-flag loss-measure tos-bit 3 delay-measure tos-bit 4
   instance 1
    description Instanceforpointbypointtest
    flow forward source 10.1.1.1 destination 10.2.1.1 
    tlp 310 out-point egress
  #
  return
  ```