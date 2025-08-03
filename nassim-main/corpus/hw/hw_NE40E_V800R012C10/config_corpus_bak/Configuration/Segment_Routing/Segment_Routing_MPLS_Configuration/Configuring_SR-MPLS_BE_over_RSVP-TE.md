Configuring SR-MPLS BE over RSVP-TE
===================================

SR-MPLS BE over RSVP-TE applies to scenarios where the core area of a network supports RSVP-TE but the edge areas of the network use SR-MPLS BE. With this function configured, an RSVP-TE tunnel can be considered as a hop of an SR LSP.

#### Usage Scenario

SR-MPLS BE over RSVP-TE enables an SR-MPLS LSP to span an RSVP-TE area for the specified VPN server to use. On a network with VPN services, carriers find it difficult to deploy TE on the entire network in order to implement MPLS traffic engineering. To address this issue, carriers can plan a core TE area and then deploy SR-MPLS BE on edge PEs in this area.


#### Pre-configuration Tasks

Before configuring SR-MPLS BE over RSVP-TE, complete the following tasks:

* Configure an IGP to ensure connectivity between LSRs at the network layer.
* Configure basic MPLS functions on nodes and interfaces.
* Enable SR-MPLS on the edge devices of the TE area and the interfaces outside the TE area.
* Establish an RSVP-TE tunnel between TE nodes.
* Configure tunnel IP addresses.
* Configure virtual TE interfaces.


[Configuring IGP Shortcut](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0176.html)

After IGP shortcut is configured on the ingress of an RSVP-TE tunnel, the associated LSP is not advertised to or used by neighbors.

[Configuring the Forwarding Adjacency Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0177.html)

Configure the forwarding adjacency function on the ingress of an RSVP-TE tunnel so that the ingress can advertise an LSP to neighbors for use.

[Enabling SR-MPLS BE over RSVP-TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0178.html)

Enable SR-MPLS route recursion to RSVP-TE tunnels, thereby enabling SR-MPLS BE over RSVP-TE.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0179.html)

After configuring SR-MPLS BE over RSVP-TE, check tunnel information on the ingress of the involved SR LSP.