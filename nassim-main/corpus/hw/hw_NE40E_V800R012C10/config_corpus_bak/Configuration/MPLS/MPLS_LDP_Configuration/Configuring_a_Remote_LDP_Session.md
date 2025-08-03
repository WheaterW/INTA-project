Configuring a Remote LDP Session
================================

A remote MPLS LDP session can only be established after LSR IDs are configured and MPLS LDP is enabled on both ends of the MPLS LDP session.

#### Usage Scenario

Remote LDP sessions are used in LDP over TE and L2VPN scenarios:

* LDP over TE: If the core area on an MPLS network supports TE and the edge devices run LDP, two LSRs on the edge establish a remote LDP session. LDP over TE allows a TE tunnel to function as a hop on an LDP LSP.
* L2VPN: Devices exchange protocol packets over an LDP session. If the devices are indirectly connected, a remote LDP session must be configured. However, no remote LDP session needs to be configured for a static PW.


#### Pre-configuration Tasks

Before configuring a remote LDP session, complete the following task:

* Configure static routes or an IGP to ensure IP route reachability among nodes.


[Configuring Global MPLS LDP Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_00041.html)

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

[Configuring a Remote LDP Peer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0012.html)

Before you configure a remote LDP session, specify the name and IP address of the remote peer.

[(Optional) Configuring an LSR ID for a Remote LDP session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0067.html)

To isolate services, configure an LSR ID for each remote LDP session.

[(Optional) Configuring Timers for a Remote LDP Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0013.html)

LDP timers include the target Hello hold timer, target Hello send timer, Keepalive hold timer, Keepalive send timer, and Exponential backoff timer.

[(Optional) Enabling LDP Loop Detection Negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_00691.html)

If the peer device is enabled with LDP loop detection, the local device must be enabled with the capability of negotiating LDP loop detection before it can set up an LDP session with the peer device.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0014.html)

After configuring a remote MPLS LDP session, you can view information about the LDP protocol, LDP session status, LDP adjacencies, and remote peers of the LDP session.