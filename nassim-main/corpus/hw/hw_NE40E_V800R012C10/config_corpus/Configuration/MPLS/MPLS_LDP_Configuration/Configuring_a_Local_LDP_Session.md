Configuring a Local LDP Session
===============================

An MPLS LDP session can be configured only after LSR IDs are configured and MPLS LDP is enabled on both ends of the MPLS LDP session.

#### Usage Scenario

An LDP session is established over a TCP connection. After the TCP connection is set up, LSRs negotiate parameters of the LDP session. If the negotiation is successful, an LDP session can be established.

After the local LDP session is established, LSRs assign labels to establish an LDP LSP.

When LDP LSPs carry Layer 2 virtual private network (L2VPN) and Layer 3 virtual private network (L3VPN) services, you can specify an LSR ID for each local LDP session on the current LSR to isolate VPN services.


#### Pre-configuration Tasks

Before configuring a local LDP session, complete the following task:

* Configure static routes or an IGP to ensure IP route reachability among nodes.


[Configuring Global MPLS LDP Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0004.html)

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

[Globally Enabling MPLS and LDP on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0005.html)

Before you configure a local LDP session, globally enabling MPLS and LDP on an interface.

[(Optional) Configuring an LSR ID for a Local LDP Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0066.html)

To isolate services, configure an LSR ID for each local LDP session.

[(Optional) Configuring an LDP Transport Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0006.html)

Before establishing an LDP session, two LSRs confirm each other's LDP transport address and set up a TCP connection.

[(Optional) Configuring Timers for a Local LDP Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0007.html)

Timers of a local LDP session include the link Hello hold timer, link Hello send timer, Keepalive hold timer, Keepalive send timer, and Exponential backoff timer.

[(Optional) Enabling LDP Loop Detection Negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0069.html)

If the peer device is enabled with LDP loop detection, the local device must be enabled with the capability of negotiating LDP loop detection before it can set up an LDP session with the peer device.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0010.html)

After configuring a local MPLS LDP session, you can view information about interfaces with MPLS and MPLS LDP enabled, the LDP protocol, LDP session status, LDP adjacencies, and peers of the LDP session.