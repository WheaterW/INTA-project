Configuring an RSVP-TE Tunnel
=============================

MPLS TE reserves resources for RSVP-TE tunnels. These tunnels are established along specified paths, not passing through congested nodes, balancing traffic on a network.

#### Usage Scenario

The dynamic RSVP-TE signaling protocol adjusts a path of a TE tunnel to adapt to network topology changes. To help implement advanced functions, such as TE FRR or CR-LSP backup, use the RSVP-TE signaling protocol to set up an MPLS TE tunnel.


#### Pre-configuration Tasks

Before configuring an RSVP-TE tunnel, complete the following tasks:

* Configure OSPF or IS-IS to implement connectivity between label switching routers (LSRs).
* Set the LSR ID for every LSR.
* Enable MPLS in the system and interface views on every LSR.


[Enabling MPLS TE and RSVP-TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0004.html)

MPLS TE and RSVP-TE must be enabled on each LSR in an MPLS domain before TE functions are configured.

[Configuring CSPF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0009.html)

Constrained Shortest Path First (CSPF) is configured to calculate the shortest path destined for a specified node.

[Configuring IGP TE (OSPF or IS-IS)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0005.html)

After IGP TE is configured on all LSRs in an MPLS domain, a TEDB is generated on each LSR.

[(Optional) Configuring TE Attributes for a Link](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0006.html)

TE link attributes, including the link bandwidth, administrative group, affinity, and SRLG, can be configured for you to select links for CR-LSP establishment.

[(Optional) Configuring an Explicit Path](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0007.html)

An explicit path is configured on the ingress of an MPLS TE tunnel. It defines the nodes through which the MPLS TE tunnel must pass or the nodes that are excluded from the MPLS TE tunnel.

[(Optional) Disabling TE LSP Flapping Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0246.html)

TE LSP flapping suppression prevents high CPU usage stemming from TE LSP flapping. This function can be disabled.

[Configuring an MPLS TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0008.html)

An MPLS TE tunnel is established and managed on a tunnel interface. Therefore, the tunnel interface must be configured on the ingress of an MPLS TE tunnel.

[(Optional) Configuring Soft Preemption for RSVP-TE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0252.html)

The setup and holding priorities and the preemption function are configured to allow TE tunnels to be established preferentially to transmit important services, preventing random resource competition during tunnel establishment.

[(Optional) Configuring Graceful Shutdown](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0248.html)

The graceful shutdown function can be enabled to help traffic migrate in seamless switching scenarios, which reduces the upgrade and maintenance expenses on an entire device.

[Verifying the RSVP-TE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0010.html)

After configuring the RSVP-TE tunnel, you can view statistics about the RSVP-TE tunnel and its status.