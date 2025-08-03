Configuring an OSPF SR-MPLS TE Tunnel (Path Computation on a Forwarder)
=======================================================================

If no controller is deployed to compute paths, CSPF can be configured on the ingress to perform SR-MPLS TE.

#### Usage Scenario

SR-MPLS TE is a new TE tunneling technology that uses SR as a control protocol. If no controller is deployed to compute paths, CSPF can be configured on the ingress to perform SR-MPLS TE.


#### Pre-configuration Tasks

Before configuring an OSPF SR-MPLS TE tunnel, configure OSPF to implement connectivity at the network layer.


[Enabling MPLS TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0007_2.html)

Before configuring an SR-MPLS TE tunnel, you need to enable MPLS TE on each involved node in the SR-MPLS domain.

[Configuring TE Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0200_3.html)

Configure TE attributes for links so that SR-MPLS TE paths can be adjusted based on the TE attributes during path computation.

[Globally Enabling the SR Capability](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0008_2.html)

Globally enabling the SR capability on forwarders is a prerequisite for configuring an SR-MPLS TE tunnel.

[Configuring Basic SR-MPLS TE Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0027.html)

This section describes how to configure basic SR-MPLS TE functions.

[Enabling the Ingress to Compute a Path](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0029_1.html)

CSPF is configured on the ingress to compute a path for an SR-MPLS TE tunnel.

[Configuring an SR-MPLS TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0030_1.html)

A tunnel interface must be configured on an ingress so that the interface is used to establish and manage an SR-MPLS TE tunnel.

[(Optional) Configuring UCMP for SR-MPLS TE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0101_5.html)

When multiple SR-MPLS TE tunnels are destined for a downstream device, you can configure weights to load balance traffic among the SR-MPLS TE tunnels in unequal cost multipath (UCMP) mode.

[Verifying the OSPF SR-MPLS TE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0014_2.html)

After configuring an automatic SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.