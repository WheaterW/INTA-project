Configuring MPLS TE Manual FRR
==============================

MPLS TE manual fast reroute (FRR) is a local protection mechanism that protects traffic on a link or a node of a CR-LSP.

#### Usage Scenario

FRR provides rapid local protection for MPLS TE networks requiring high reliability. If a local failure occurs, FRR rapidly switches traffic to a bypass tunnel, minimizing the impact on traffic.

A backbone network has a large capacity and its reliability requirements are high. If a link or node failure occurs on the backbone network, a mechanism is required to provide automatic protection and rapidly remove the fault. MPLS TE LSPs are typically established using the RSVP protocol in the downstream on demand (DoD) mode. If a failure occurs, Constraint Shortest Path First (CSPF) can re-calculate a reachable path only after the ingress is notified of the failure. The failure may trigger reestablishment of multiple LSPs and the reestablishment fails if bandwidth is insufficient. These factors contribute to extended recovery time for MPLS TE networks following local failures.

Configuring TE FRR on MPLS TE-enabled interfaces allows traffic to automatically switch to a protection link if a link or node on a primary tunnel fails. After the primary tunnel recovers or is reestablished, traffic switches back to the primary tunnel. In this way, the MPLS TE network's reliability requirements are met.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* FRR requires reserved bandwidth for a bypass tunnel that needs to be pre-established. If available bandwidth is insufficient, FRR should protect only important nodes or links on a tunnel.
* RSVP-TE tunnels using bandwidth reserved in shared explicit (SE) style support FRR, but static TE tunnels do not.


#### Pre-configuration Tasks

Before configuring MPLS TE manual FRR, complete the following tasks:

* Establish a primary RSVP-TE tunnel.
* Enable MPLS TE and RSVP-TE in the MPLS and physical interface views on every node along a bypass tunnel. (See [Enabling MPLS TE and RSVP TE](dc_vrp_te-p2p_cfg_0004.html).)
* Enable CSPF on a point of local repair (PLR).
* (Optional) Configure TE attributes for the links of bypass tunnel. (See [(Optional) Configuring TE Attributes](dc_vrp_te-p2p_cfg_0006.html).)
* (Optional) Configure an explicit path for the bypass tunnel.


[Enabling TE FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0049.html)

TE FRR must be enabled on the ingress of a primary LSP before TE FRR is manually configured.

[Configuring a Bypass Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0050.html)

A path and attributes must be configured for a bypass tunnel after TE manual FRR is enabled on a PLR.

[(Optional) Setting the FRR Switching Delay Time](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0250.html)

After the FRR switching delay time is set, FRR entry delivery is delayed, preventing traffic from being switched twice when both HSB and FRR are enabled.

[(Optional) Enabling the Coexistence of Rapid FRR Switching and MPLS TE HSB](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_te-p2p_cfg_0015.html)

When FRR and HSB are enabled for MPLS TE tunnels, enabling the coexistence of MPLS TE HSB and rapid FRR switching improves switching performance.

[Verifying the MPLS TE Manual FRR Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0052.html)

After configuring MPLS TE manual FRR, you can view detailed information about the bypass tunnel.