Configuring an SR-MPLS TE Policy (Manual Configuration)
=======================================================

SR-MPLS TE Policy is a tunneling technology developed based on SR.

#### Usage Scenario

An SR-MPLS TE Policy is a set of candidate paths consisting of one or more segment lists, that is, segment ID (SID) lists. Each SID list identifies an end-to-end path from the source to the destination, instructing a device to forward traffic through the path rather than the shortest path computed by an IGP. The header of a packet steered into an SR-MPLS TE Policy is augmented with an ordered list of segments associated with that SR-MPLS TE Policy, so that other devices on the network can execute the instructions encapsulated into the list.

You can configure an SR-MPLS TE Policy through CLI or NETCONF. For a manually configured SR-MPLS TE Policy, information, such as the endpoint and color attributes, the preference values of candidate paths, and segment lists, must be configured. Moreover, the preference values must be unique. The first-hop label of a segment list can be a node, adjacency, BGP EPE, parallel, or anycast SID, but cannot be any binding SID. Ensure that the first-hop label is a local incoming label, so that the forwarding plane can use this label to search the local forwarding table for the corresponding forwarding entry.


#### Pre-configuration Tasks

Before configuring an SR-MPLS TE Policy, configure an IGP to ensure that all nodes can communicate with each other at the network layer.


[Configuring IGP SR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0061.html)

This section describes how to configure IGP SR.

[Configuring an SR-MPLS TE Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0062.html)

SR-MPLS TE Policy is a tunneling technology developed based on SR.

[(Optional) Configuring Cost Values for SR-MPLS TE Policies](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0267.html)

Configure cost values for SR-MPLS TE Policies so that the ingress can select the optimal SR-MPLS TE Policy based on the values.

[Configuring the Color Extended Community](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0063.html)

This section describes how to configure the Color Extended Community for a route through a route-policy, enabling the route to recurse to an SR-MPLS TE Policy based on the color value and next-hop address in the route.

[Verifying the SR-MPLS TE Policy Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0066.html)

After configuring SR-MPLS TE Policies, verify the configuration.