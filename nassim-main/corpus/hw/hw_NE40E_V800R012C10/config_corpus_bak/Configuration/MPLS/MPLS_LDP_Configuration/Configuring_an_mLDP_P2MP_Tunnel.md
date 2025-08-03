Configuring an mLDP P2MP Tunnel
===============================

mLDP P2MP tunnels transmit multicast services over an IP/MPLS backbone network, simplifying backbone network deployment and saving network bandwidth resources.

#### Usage Scenario

Traditional core networks and backbone networks generally use IP/MPLS to transmit service packets. For unicast packets, this deployment is highly flexible and provides sufficient reliability and traffic engineering capabilities. The proliferation of applications, such as IPTV, video conference, and massively multiplayer online role-playing games (MMORPGs), amplifies demands on multicast transmission over IP/MPLS networks. The existing P2P MPLS technology requires a transmit end to deliver the same data packet to each receive end, which wastes bandwidth resources.

To address this problem, deploy mLDP P2MP tunnels on IP/MPLS networks. P2MP LDP establishes a tree-shaped tunnel from a root node to multiple leaf nodes and directs multicast traffic from the root node to the tunnel for forwarding. In actual forwarding, only one copy of the packet is sent on the root node, and the packet is replicated on the branch node. This ensures that the bandwidth is not repeatedly occupied.

mLDP P2MP tunnels can be manually or automatically established. [Table 1](#EN-US_TASK_0172368534__tab_dc_vrp_ldp-p2p_cfg_006001) compares manual P2MP tunnels with automatic P2MP TE tunnels.

**Table 1** Comparison between manual and automatic mLDP P2MP tunnels
| Item | Manual P2MP Tunnel | Automatic P2MP Tunnel |
| --- | --- | --- |
| Triggering mode | Manually triggered by users | Automatically triggered by services |
| Usage scenario | Multicast services, excluding multicast VPN, are transmitted. | NG MVPN or multicast VPLS services are transmitted. |
| Traffic steering modes | QoS redirection is used to statically steer traffic to tunnels. | Services are automatically steered to tunnels. |




#### Pre-configuration Tasks

Before configuring an mLDP P2MP tunnel, complete the following tasks:

* Configure network layer parameters to implement connectivity.
* [Configure MPLS LDP on each node to establish LDP sessions.](dc_vrp_ldp-p2p_cfg_0003.html)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

mLDP P2MP tunnels can be established only in DU session mode.



[Configuring a Manual mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0061.html)

A manual mLDP P2MP tunnel can be manually triggered and transmit multicast services, excluding multicast VPN services.

[Configuring an Automatic mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0062.html)

Automatic mLDP P2MP tunnels can only transmit NG MVPN and multicast VPLS traffic.

[(Optional) Configuring the Reliability Enhancement Function for a P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_te-p2p_cfg_6014-ldp2.html)

Configure a function to improve service reliability as needed.

[(Optional) Enabling the Capability of Establishing a Best-Effort Path for an mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0210.html)

The capability of establishing a best-effort path for an mLDP P2MP tunnel can be enabled to rectify link faults of outbound interfaces, which helps speed up route convergence and reduce traffic loss.

[(Optional) Configuring a Timer for mLDP P2MP Tunnel Re-optimization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2051.html)

A timer can be set so that mLDP P2MP tunnel re-optimization is triggered at the specified time if the network topology changes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0064.html)

After configuring an mLDP P2MP LSP, verify mLDP P2MP LSP information on each node along the LSP and mLDP P2MP LSP connectivity on the root node.