Configuring an IS-IS SR-MPLS TE Tunnel (Explicit Path Used)
===========================================================

If no controller is deployed to compute paths, an explicit path can be manually configured to perform segment routing-traffic engineering (SR-MPLS TE).

#### Usage Scenario

SR-MPLS TE is a new TE tunneling technology that uses SR as a control protocol. If no controller is deployed for path computation, an explicit path can be manually configured to achieve SR-MPLS TE.


#### Pre-configuration Tasks

Before configuring an IS-IS SR-MPLS TE tunnel, configure IS-IS to implement network layer connectivity.


[Enabling MPLS TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-te_cfg_00201_1.html)

Before configuring an SR-MPLS TE tunnel, you need to enable MPLS TE on each involved node in the SR-MPLS domain.

[Enabling SR Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-te_cfg_00211_1.html)

Enabling SR globally on forwarders is a prerequisite for SR-MPLS TE tunnel configuration.

[Configuring Basic SR-MPLS TE Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0024.html)

This section describes how to configure basic SR-MPLS TE functions.

[Configuring an SR-MPLS TE Explicit Path](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-te_cfg_0026.html)

An explicit path over which an SR-MPLS TE tunnel is to be established is configured on the ingress. You can specify node or link labels for the explicit path.

[Configuring an SR-MPLS TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0028.html)

A tunnel interface must be configured on an ingress so that the interface is used to establish and manage an SR-MPLS TE tunnel.

[(Optional) Configuring UCMP for SR-MPLS TE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0101_2.html)

When multiple SR-MPLS TE tunnels are destined for a downstream device, you can configure weights to load balance traffic among the SR-MPLS TE tunnels in unequal cost multipath (UCMP) mode.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-te_cfg_0018_1.html)

After configuring an automatic SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.