Configuring the BGP4+ GR Helper
===============================

A BGP4+ GR helper helps its neighbor complete BGP4+ GR.

#### Usage Scenario

When BGP4+ restarts, peer relationships are re-established and traffic forwarding is interrupted. Enabling Graceful restart (GR) can prevent traffic interruption.

BGP4+ GR needs to be enabled to prevent traffic interruption in the event of BGP4+ restart. A GR restarter and its BGP4+ peer negotiate to establish a GR-capable BGP4+ session.


#### Pre-configuration Tasks

Before configuring BGP4+ GR helper, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Enabling BGP4+ GR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0052.html)

Enabling or disabling GR may delete and re-establish all sessions and instances.

[Configuring BGP4+ GR Session Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0053.html)

You can change the restart time to reestablish a BGP peer relationship.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0054.html)

After configuring BGP4+ GR helper, check the BGP4+ GR status.