Configuring the BGP GR Helper
=============================

You can configure a device to function as a Graceful Restart (GR) helper to help a BGP peer with the BGP GR process.

#### Usage Scenario

When BGP restarts, the peer relationship is re-established, and traffic forwarding is interrupted. To address this issue, enable GR.

GR takes effect only when BGP GR is enabled and a GR-capable BGP session is established between the GR restarter and its peers.


#### Pre-configuration Tasks

Before configuring the BGP GR helper, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Enabling BGP GR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3059.html)

Enabling or disabling GR may delete and re-establish all sessions and instances.

[Configuring the Parameter for a BGP GR Session](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3060.html)

You can change the restart time to reestablish a BGP peer relationship.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3061.html)

After configuring a BGP GR helper, verify the BGP GR status.