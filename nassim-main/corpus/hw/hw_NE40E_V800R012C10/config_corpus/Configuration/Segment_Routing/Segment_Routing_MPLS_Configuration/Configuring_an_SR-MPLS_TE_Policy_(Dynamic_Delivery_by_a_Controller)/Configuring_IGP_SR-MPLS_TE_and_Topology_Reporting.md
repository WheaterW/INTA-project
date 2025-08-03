Configuring IGP SR-MPLS TE and Topology Reporting
=================================================

Before an SR-MPLS TE tunnel is established, you need to enable IGP SR-MPLS TE and topology reporting through BGP-LS.

#### Context

An IGP collects network topology information including the link cost, latency, and packet loss rate and advertises the information to BGP-LS, which then reports the information to a controller. The controller can compute an SR-MPLS TE tunnel based on link cost, latency, packet loss rate, and other factors to meet various service requirements.

This section mainly involves the following operations:

1. Configure IGP SR-MPLS TE.
2. Configure IGP topology information to be sent to BGP-LS.
3. Configure a BGP-LS peer relationship between the forwarder and controller so that the forwarder can report topology information to the controller through BGP-LS.

#### Procedure

* For details, see [Configuring IS-IS-based Topology Reporting](dc_vrp_sr-te_cfg_0022.html) or [Configuring OSPF-based Topology Reporting](dc_vrp_sr_all_cfg_0009.html).