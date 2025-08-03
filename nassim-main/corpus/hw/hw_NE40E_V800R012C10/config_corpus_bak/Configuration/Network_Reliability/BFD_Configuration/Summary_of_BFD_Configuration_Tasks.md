Summary of BFD Configuration Tasks
==================================

BFD is a unified detection mechanism that is used across a network and can work with multiple protocols. This section describes BFD features supported by the NE40E.

#### BFD Session Establishment Modes

BFD uses local and remote discriminators to differentiate multiple BFD sessions between a pair of systems. Based on the differences in methods of creating the local and remote discriminators, the NE40E supports the following types of BFD sessions:

* Static BFD sessions with manually specified discriminators
  
  Local and remote discriminators must be set manually.
* Static BFD sessions with automatically negotiated discriminators
  
  BFD monitors a static route and helps a node communicate with a remote node on which a dynamic BFD session is established. No local or remote discriminator needs to be set.
* BFD sessions dynamically triggered by protocolsNo local or remote discriminator needs to be set. BFD sessions are further classified into the following types:
  + BFD sessions with dynamically allocated local discriminators
  + BFD sessions with self-learned remote discriminators

If the two ends of a BFD session create discriminators in different modes, the following conditions must be satisfied:

* In a static BFD session, if discriminators on the local end are manually specified, then discriminators on the remote end must also be manually specified.
* If static discriminators on the local end are automatically negotiated, discriminators on the remote end can be automatically negotiated or a dynamic BFD session can be established on the remote end.
* On the local end, if a static BFD session with automatically negotiated discriminators and a dynamic BFD session are established, the following principles are applicable:
  + If a dynamic BFD session and a static BFD session with automatically negotiated discriminators are configured with the same 5-tuple set (source and destination addresses, outbound interface, VPN index, and VS identifier), the NE40E uses the shared BFD session to which both the dynamic BFD session and static BFD session with automatically negotiated discriminators belong.
  + If the dynamic BFD session named DYN\_local discriminator is configured and then the static BFD session with automatically negotiated discriminators is configured, the name of the shared BFD session is updated to the name of the static BFD session.
  + The smaller values of parameters between two BFD sessions are adopted.


#### Detection Modes

The NE40E supports asynchronous detection. Each system sends BFD control packets at negotiated intervals. If a system does not receive packets from the peer within a detection period, the BFD session goes down.

Echo is also supported in asynchronous mode. When the echo function is activated, the local system sends a BFD control packet and the remote system loops the packet back through the forwarding channel. If several consecutive echo packets are not received, the session is declared to be down.


#### Single- and Multi-hop BFD

The NE40E supports single- and multi-hop BFD. Single- and multi-hop BFD monitors IP route continuity.

On the NE40E, single-hop BFD can monitor the following types of interfaces and links:

* Layer 3 physical interfaces
* Ethernet sub-interfaces including Eth-Trunk sub-interfaces
  
  If a physical Ethernet interface has multiple sub-interfaces, BFD sessions can be established separately on the physical Ethernet interface and each of its sub-interfaces.
* IP-Trunk
* Layer 3 Eth-Trunk
* ATM interfaces or ATM sub-interfaces

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Both IP-Trunks and Eth-Trunks consist of multiple member links, which provide high bandwidth or enhance reliability.

A trunk remains up only when a certain number of member links are up.




#### Dynamically Modifying BFD Parameters

After a BFD session is set up, you can modify BFD parameters, such as the minimum intervals at which BFD packets are sent and received and detection mode. This modification does not affect the current session status.


#### Binding a BFD Session to a VPN Instance

On the NE40E, a BFD session can be bound to a VPN instance to allow BFD control packets to be sent over a specified VPN.


#### Usage Scenario of BFD

**Table 1** Usage scenario of BFD
| BFD for Everything | Usage Scenario | Configuration Reference |
| --- | --- | --- |
| BFD for default-ip | A single-hop BFD session rapidly detects faults on direct links over a network. If the link interface is a Layer 3 physical interface or Layer 2 interface that does not have an IP address, configure static BFD for default-ip for link detection. | [Configuring BFD to Monitor an IP Link](dc_vrp_bfd_cfg_0003.html) |
| BFD for static route | Different from dynamic routing protocols, static routes do not have a detection mechanism. As a result, if a fault occurs on the network, the administrator needs to handle it. By binding IP static routes to BFD sessions, you can use BFD sessions to provide link detection for IP static routes on the public network. The routing management (RM) module determines whether static routes are available based on the BFD session status. | [Configuring Dynamic BFD for IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0012.html)  [Configuring Dynamic BFD for IPv6 Static Routes](dc_vrp_static-route_disjoin_cfg_0023.html)  [Configuring Static BFD for IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0027.html)  [Configuring Static BFD for IPv6 Static Routes](dc_vrp_static-route_disjoin_cfg_0028.html) |
| BFD for OSPF | OSPF enables a device to periodically send Hello packets to a neighboring router for fault detection. Detecting a fault takes more than 1s. As technologies become more advanced, voice, video, and other VOD services become widely used. These services are sensitive to the packet loss and delay. When the data transmission rate reaches the level of Gbit/s, such slow detection will cause a large amount of data to be lost. As a result, the requirement for high reliability of carrier-class networks cannot be met. BFD for OSPF is introduced to resolve this problem. After BFD for OSPF is configured in a specified process or on a specified interface, the link status can be rapidly detected and fault detection can be completed in milliseconds. This speeds up OSPF convergence when the link status changes. | [Configuring BFD for OSPF](dc_vrp_ospf_cfg_0048.html) |
| BFD for OSPFv3 | To increase the convergence speed of OSPFv3 when the link status changes, you can configure BFD on OSPFv3 links. BFD keeps track of the liveliness of network links and detects any faults in links much faster than the normal keep-alive protocols. If OSPFv3 is associated with BFD sessions, BFD can notify OSPFv3 of link failures immediately. OSPFv3 then performs route calculation and convergence based on the new network topology. | [Configuring BFD for OSPFv3](dc_vrp_ospfv3_cfg_2036.html) |
| BFD for BGP | As technologies become more advanced, voice and video services are more widely applied. These services are sensitive to the packet loss and delay. BGP periodically sends Keepalive packets to its peers to detect the status of its peers. This mechanism, however, takes more than one second to detect a fault. When the data transmission rate reaches the level of Gbit/s, it causes a large amount of data to be lost. As a result, the requirement for high reliability of carrier-class networks cannot be met. To address this problem, configure BFD for BGP. BFD for BGP detects faults on links between BGP peers within 50 ms. The fast detection ensures fast BGP route convergence and minimizes traffic loss. | [Configuring BFD for BGP](dc_vrp_bgp_cfg_4056.html) |
| BFD for BGP4+ | BFD can rapidly detect IPv6 forwarding failures. By adopting the BFD fast detection mechanism, an IPv6 network can transmit voice services, video services, and VoD services with high QoS. This enables service providers to provide their customers with highly available and reliable VoIP and other real-time services. BGP periodically sends Keepalive packets to its peers to detect the status of its peers. This mechanism, however, takes more than one second to detect a fault. When the data transmission rate reaches the level of Gbit/s, it causes a large amount of data to be lost. As a result, the requirement for high reliability of carrier-class networks cannot be met. To address this problem, configure BFD for BGP4+. BFD for BGP4+ detects faults on links between BGP4+ peers within milliseconds. If a fault is detected, it notifies BGP of the fault. Therefore, BGP4+ routes can undergo fast convergence. | [Configuring BFD for BGP4+](dc_vrp_bgp6_cfg_0046.html) |
| BFD for LDP LSP | BFD for LDP LSP speeds up the detection of link faults and reduces the configuration workload to minimize the impact of link faults on services. | [Configuring Static BFD to Monitor an LDP LSP](dc_vrp_ldp-p2p_cfg_2033.html)  [Configuring Dynamic BFD for LDP LSPs](dc_vrp_ldp-p2p_cfg_2039.html) |
| BFD for LDP tunnel | Dynamic BFD can be configured to establish a dynamic BFD session to monitor both primary and backup LDP LSPs in an LDP tunnel. If BFD detects a fault, BFD instructs a specific LDP upper-layer application to perform a protection switchover. | [Configuring Dynamic BFD to Monitor an LDP Tunnel](dc_vrp_ldp-p2p_cfg_0073.html) |
| BFD for BGP tunnel | BFD for BGP tunnel rapidly detects faults in E2E BGP tunnels. | [Configuring Dynamic BFD to Monitor a BGP Tunnel](dc_vrp_seamless_mpls_cfg_0037.html) |
| BFD for RSVP | If BFD is disabled and a Layer 2 device exists between RSVP neighbors, the neighboring node cannot rapidly detect faults after links fail, resulting in a great loss of data. BFD detects faults at millisecond level in protected links or nodes. BFD for RSVP rapidly detects faults in an RSVP neighbor, allowing packets to switch to a backup LSP rapidly. BFD for RSVP is applied to a scenario where TE FRR is used and a Layer 2 device exists on the primary LSP between a PLR and its downstream neighbors. On a network where GR is enabled on the PLR and MP, BFD for RSVP is also recommended. | [Configuring Dynamic BFD for RSVP](dc_vrp_te-p2p_cfg_0067.html) |
| BFD for TE CR-LSP | BFD for TE CR-LSP can quickly detect faults on TE CR-LSPs. After detecting a fault on a TE CR-LSP, BFD immediately notifies the forwarding plane of the fault to rapidly trigger a traffic switchover. BFD for TE CR-LSP is used together with a hot-standby CR-LSP or TE FRR. | [Configuring Static BFD for TE CR-LSP](dc_vrp_te-p2p_cfg_0121.html)  [Configuring Dynamic BFD for TE CR-LSP](dc_vrp_te-p2p_cfg_0144.html) |
| BFD for TE tunnel | BFD for TE tunnel allows applications such as VPN FRR to fast switch traffic if the primary tunnel fails, minimizing the impact on services. | [Configuring Static BFD for TE Tunnel](dc_vrp_te-p2p_cfg_0126.html) |
| BFD for IS-IS | Connection status between an IS-IS device and its neighbors can be monitored by exchanging Hello packets at intervals. The minimum allowable sending interval is 3s, and a neighbor is declared down after at least three intervals during which no response Hello packet is received from the neighbor. IS-IS takes more than one second to detect that a neighbor becomes down, resulting in loss of a large amount of high-speed data. To solve this problem, BFD must be configured for IS-IS. BFD provides millisecond-level fault detection. After detecting a link or node failure, BFD will notify IS-IS of the failure, accelerating the IS-IS route convergence speed. | [Configuring Static BFD for IS-IS](dc_vrp_isis_cfg_0039.html)  [Configuring Dynamic BFD for IS-IS](dc_vrp_isis_cfg_0043.html)  [Configuring Dynamic BFD for IPv6 IS-IS](dc_vrp_isis_cfg_2003.html) |
| BFD for RIP | Generally, RIP uses timers to receive and send Update messages to maintain neighbor relationships. If a RIP device does not receive an Update message from a neighbor after the Age timer expires, the RIP device will announce that its neighbor is down. The default value of the Age timer is 180s. If a link fault occurs, RIP can detect this fault after 180s. If high-rate data services are deployed on a network, a great deal of data will be lost during the aging time. BFD provides millisecond-level fault detection. It can rapidly detect faults in protected links or nodes and report them to RIP. This speeds up RIP processes' response to network topology changes and achieves rapid RIP route convergence. | [Configuring Static BFD for RIP](dc_vrp_rip_cfg_0058.html)  [Configuring Dynamic BFD for RIP](dc_vrp_rip_cfg_0055.html) |
| BFD for PIM | Generally, if the current DR in a shared network segment is faulty, other PIM neighbors trigger a new round of DR election only after the neighbor relationship times out. The duration that data transmission is interrupted (usually in seconds) is not shorter than the timeout period of the neighbor relationship. BFD features the fast detection of faults, of up to the millisecond level. BFD can detect the status of PIM neighbors in the shared network segment. When BFD detects that a peer is faulty, BFD immediately reports it to PIM. PIM then triggers a new round of DR election without waiting for the timeout of the neighbor relationship. This shortens the interruption of data transmission and enhances the reliability of the network. | [Configuring BFD for IPv4 PIM](dc_vrp_multicast_cfg_0099.html)  [Configuring BFD for IPv6 PIM](dc_vrp_multicast_cfg_2175.html) |
| BFD for PW | If provider edge devices (PEs) on a Multiprotocol Label Switching (MPLS) Layer 2 virtual private network (L2VPN) communicate over pseudo wires (PWs), service protection can be enhanced by configuring static BFD to detect PW connectivity. | [Configuring BFD for VPWS PW](dc_vrp_vpws_cfg_6021.html) |
| BFD for VSI PW (default-ip) | In the VPLS convergence MAN solution, you can establish multiple service VSI PWs and bind them to an mVSI PW. In this manner, if a BFD session is bound to the mVSI PW, you can monitor the service VSI only by monitoring the status of the mVSI PW. | [Configuring Static BFD to Detect the Connectivity of a VPLS SS-PW](dc_vrp_vpls_cfg_5034.html) |
| BFD for VRRP | BFD can rapidly detect faults in links or IP routes. BFD for VRRP enables a master/backup VRRP switchover to be completed within 1 second, preventing user traffic loss. A BFD session is established between the master and backup devices in a VRRP group and is bound to the VRRP group. BFD immediately detects communication faults in the VRRP group and instructs the VRRP group to perform a master/backup switchover, minimizing service interruptions. | [Associating a VRRP Group with a BFD Session](dc_vrp_vrrp_cfg_0116.html) |
| BFD for E-Trunk | An E-Trunk implements inter-device link aggregation. After a BFD session is bound to an E-Trunk, BFD can rapidly detect changes in the protocol link between devices with the E-Trunk deployed. If the protocol link fails, the status of the BFD session goes down.  Two devices with the E-Trunk deployed can use BFD to rapidly detect faults and change the master/backup status, ensuring proper traffic forwarding. | [Configuring an E-Trunk for Backup in a Link Aggregation Group](dc_vrp_ethtrunk_cfg_0042.html) |
| BFD for multicast VPLS | To meet the reliability requirements of multicast services, configure BFD for multicast VPLS to monitor multicast VPLS links. When a link or node fails, BFD on the leaf nodes can rapidly detect the fault and trigger protection switching so that the leaf nodes receive traffic from the backup multicast tunnel. | [Configuring mLDP P2MP Tunnels with Dual-Root Protection](dc_vrp_vpls_cfg_6044.html) |
| BFD for link-bundle | When two devices are directly connected over a Layer 3 Eth-Trunk, you can configure a BFD for link-bundle session to detect link faults.  After a BFD for link-bundle session is bound to an Eth-Trunk interface, the system creates a dynamic unicast BFD sub-session for each Eth-Trunk member interface. Each sub-session independently negotiates and monitors the link status and reports the monitored link status. The system also creates a main session, which processes the link status reported by the sub-sessions and reports its status to the APP. The main session goes down only when all sub-sessions go down. | [Configuring a BFD for Link-Bundle Session to Detect Eth-Trunk Member Link Faults](dc_vrp_bfd_cfg_0116.html) |
| SBFD for SR-MPLS TE Policy | SBFD for SR-MPLS TE Policy can quickly detect segment list faults. If all the segment lists of a candidate path are faulty, SBFD triggers a candidate path switchover to reduce impacts on services. | [Configuring SBFD for SR-MPLS TE Policy](dc_vrp_sr_all_cfg_0074.html) |
| SBFD for SRv6 TE Policy | SBFD for SRv6 TE Policy can quickly detect segment list faults. If all the segment lists of a candidate path are faulty, SBFD triggers a candidate path switchover to reduce impacts on services. | [Configuring SBFD for SRv6 TE Policy](dc_vrp_cfg_sbfd1_over_srv6-te_poliy.html) |