Configuring an SRv6 TE Policy (Manual Configuration + IS-IS as an IGP)
======================================================================

SRv6 TE Policy is a tunneling technology developed based on SRv6.

#### Pre-configuration Tasks

Before configuring an SRv6 TE Policy, complete the following task:

* Configure an IGP to implement network layer connectivity.

#### Context

SRv6 TE Policy is a tunneling technology developed based on SRv6. A specific SRv6 TE Policy is a set of candidate paths consisting of one or more segment lists, that is, segment ID (SID) lists. Each SID list identifies an end-to-end path from the source to the destination, instructing a device to forward traffic through the path rather than the shortest path computed using an IGP. The header of a packet steered into an SRv6 TE Policy is augmented with an ordered list of segments associated with that SR Policy, so that other devices on the network can execute the instructions encapsulated into the list.

An SRv6 TE Policy consists of the following parts:

* Headend: node where an SRv6 TE Policy is generated.
* Color: extended community attribute of an SRv6 TE Policy. A BGP route can recurse to an SRv6 TE Policy if the route has the same color attribute as the policy.
* Endpoint: destination address of an SRv6 TE Policy.

Color and endpoint information is added to an SRv6 TE Policy through configuration. During path computation, a forwarding path is computed based on the color attribute that meets SLA requirements. The headend steers traffic into an SRv6 TE Policy whose color and endpoint attributes match the color value and next-hop address in the associated route, respectively. By defining an application-level network SLA policy, the color attribute allows network paths to be planned based on specific SLA requirements for services, realizing service value in a refined manner, and helping build new business models.


[Enabling SRv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0071.html)

Other SRv6 TE Policy configurations can be performed only after SRv6 is enabled.

[Configuring SRv6 SIDs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0111.html)

The headend can orchestrate network paths only if SIDs are allocated to adjacencies and nodes on the network.

[Configuring an SRv6 TE Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0112.html)

An SRv6 TE Policy can either be configured manually or be delivered by a controller. This section describes how to configure an SRv6 TE Policy manually.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0115.html)

After configuring SRv6 TE Policies, verify the configuration.