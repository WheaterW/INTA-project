Configuring Multicast VPLS
==========================

Multicast VPLS simplifies multicast service deployment and sustains MPLS's advantages in TE, QoS guarantee, and reliability assurance.

#### Usage Scenario

Multicast services, such as IPTV services, video conferences, and Massively Multiplayer OnlineRole-Playing Games (MMORPGs), are increasingly used in daily life. These services are transmitted over service transport networks that need to:

* Smoothly forward multicast traffic during network congestion.
* Rapidly detect network faults and switch traffic to a backup link.

Multicast VPLS meets these requirements. Multicast VPLS establishes an MPLS P2MP tunnel on a network. Multicast traffic is imported into the P2MP tunnel on the ingress (root node) and exported from the P2MP tunnel on the egresses (leaf nodes) through static configuration or VPN. Multicast VPLS eliminates the need to configure PIM and H-VPLS on the transit nodes of tunnels, simplifying multicast service deployment. In addition, multicast VPLS can sustain the advantages of MPLS in TE, QoS guarantee, and reliability assurance.

On a multicast VPLS network, multicast traffic can be carried over either mLDP P2MP or P2MP TE tunnels. [Table 1](#EN-US_TASK_0172370194__tab_dc_vrp_vpls_cfg_604201) lists the differences between mLDP P2MP and P2MP TE tunnels.

**Table 1** Comparison of P2MP TE and mLDP P2MP tunnels
| Category | P2MP TE | mLDP P2MP |
| --- | --- | --- |
| Usage scenario | Networks that require control over destination nodes | Networks that do not require control over destination nodes |
| Creation mode | The root node initiates LSP setup. | The leaf nodes initiate LSP setup. |
| Signaling usage | Signaling packets need to be periodically sent to maintain the tunnel. If a large number of leaf nodes exist, network congestion is likely to occur. | Signaling packets do not need to be periodically sent, reducing network pressure. |


In scenarios where P2MP TE tunnels with dual-root protection are used to carry services, the root nodes send two copies of traffic, but leaf nodes receive and process traffic from only the primary P2MPTE tunnel. If the primary P2MP tunnel fails, service traffic is quickly switched to the backup P2MP TE tunnel, ensuring reliable transmission of traffic.


#### Pre-configuration Tasks

Before configuring multicast VPLS, complete the following tasks:

* Create a VSI and configure the signaling type as BGP AD or BGP multi-homing on the root and leaf nodes.
* For an mLDP P2MP tunnel, [configure the tunnel](dc_vrp_ldp-p2p_cfg_0060.html) on the root, bud, and leaf nodes.
* For a P2MP TE tunnel, [configure the tunnel](dc_vrp_te-p2p_cfg_0133.html) on the root, bud, and leaf nodes.


[Configuring a Single-Root mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6043.html)

This section describes how to configure a single-root mLDP P2MP tunnel to minimize redundant traffic.

[Configuring mLDP P2MP Tunnels with Dual-Root Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6044.html)

This section describes how to configure mLDP P2MP tunnels with dual-root protection to ensure reliable transmission of multicast traffic.

[Configuring a Single-Root P2MP TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6045.html)

This section describes how to configure a single-root P2MP TE tunnel to minimize traffic redundancy.

[Configuring P2MP TE Tunnels with Dual-Root Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6046.html)

This section describes how to configure P2MP TE tunnels with dual-root protection to ensure reliable transmission of multicast traffic.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vpls_cfg_6047.html)

After configuring multicast VPLS, check mLDP P2MP and P2MP TE tunnel information.