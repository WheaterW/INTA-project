Configuring P2MP TE Auto FRR
============================

Auto fast reroute (FRR) is a local protection mechanism in MPLS TE. Auto FRR deployment is easier than manual FRR deployment.

#### Usage Scenario

FRR protection is configured for networks requiring high reliability. If P2MP TE manual FRR is used (configured by following the steps in [Configuring P2MP TE FRR](dc_vrp_te-p2p_cfg_0138.html)), a lot of configurations are needed on a network with complex topology and a great number of links to be protected. In this situation, P2MP TE Auto FRR can be configured.

Unlike [P2MP TE manual FRR](dc_vrp_te-p2p_cfg_0138.html), P2MP TE Auto FRR automatically creates a bypass tunnel that meets traffic requirements, which simplifies configurations.

The NE40E supports upgrade binding that if a bypass tunnel with a priority higher than an existing bypass tunnel is calculated, the primary tunnel will be automatically unbound from the existing bypass tunnel and bound to the one with the higher priority. A bypass tunnel is selected based on the following rules prioritized in descending order:

* An SRLG attribute is configured for a bypass tunnel.
* If P2MP TE Auto FRR and an SRLG attribute are configured, the primary and bypass tunnels must be in different SRLGs. If these two tunnels are in the same SRLG, the bypass tunnel may fail to be established.
* A bypass tunnel with bandwidth protection configured takes preference over that with non-bandwidth protection configured.

A bypass tunnel provides link protection, not node protection, for its primary tunnel.

#### Pre-configuration Tasks

Before configuring P2MP TE Auto FRR, complete the following tasks:

* Configure a primary P2MP TE tunnel.
* Enable MPLS, MPLS TE, and RSVP-TE globally and in the physical interface view on each node along a bypass tunnel to be established. For configuration details, see [Enabling MPLS TE and RSVP-TE](dc_vrp_te-p2p_cfg_0004.html).
* (Optional) To protect bandwidth of the primary tunnel, set the physical link bandwidth for the bypass tunnel to be established. For configuration details, see [(Optional) Configuring Link TE Attributes](dc_vrp_te-p2p_cfg_0006.html).
* Enable CSPF on each node along the bypass tunnel to be established.


[Enabling P2MP TE Auto FRR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0203.html)

Enabling P2MP TE Auto FRR on the ingress or a transit node of the primary tunnel is the prerequisite of configuring TE Auto FRR.

[Enabling the TE FRR and Configuring the AutoBypass Tunnel Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0055_copy.html)

After MPLS TE FRR is enabled on the ingress of a primary LSP, a bypass LSP is established automatically.

[(Optional) Configuring Auto Bypass Tunnel Re-Optimization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0185_copy.html)

Auto bypass tunnel re-optimization allows paths to be recalculated at certain intervals for an auto bypass tunnel. If an optimal path is recalculated, a new auto bypass tunnel will be set up over this optimal path. In this manner, network resources are optimized.

[Verifying the P2MP TE Auto FRR Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0204.html)

After configuring P2MP TE Auto FRR, verify P2MP TE Auto FRR information.