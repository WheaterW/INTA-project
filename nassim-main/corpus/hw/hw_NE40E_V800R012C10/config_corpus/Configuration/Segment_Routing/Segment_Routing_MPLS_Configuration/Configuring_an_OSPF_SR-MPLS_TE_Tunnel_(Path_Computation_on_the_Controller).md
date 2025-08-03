Configuring an OSPF SR-MPLS TE Tunnel (Path Computation on the Controller)
==========================================================================

An SR-MPLS TE tunnel is configured on a forwarder. The forwarder delegates the tunnel to a controller. The controller generates labels and calculates a path.

#### Usage Scenario

Currently, each LSP of a TE tunnel is allocated with a label, and tunnel creation and LSP generation are both completed by forwarders. This increases the burden on forwarders and consumes a lot of forwarder resources. To address this issue, SR-MPLS TE can be used to manually create tunnels. This method offers the following benefits:

* A controller generates labels, reducing the burden on forwarders.
* The controller computes paths and allocates a label to each route, reducing both the burden and resource usage on the forwarders. As such, the forwarders can focus more on core forwarding tasks, improving forwarding performance.

#### Pre-configuration Tasks

Before configuring an SR-MPLS TE tunnel, complete the following tasks:

* Configure OSPF to implement LSR connectivity at the network layer.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A controller must be configured to generate labels and calculate an LSP path for an SR-MPLS TE tunnel to be established.



[Enabling MPLS TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0007.html)

Before configuring an SR-MPLS TE tunnel, you need to enable MPLS TE on each involved node in the SR-MPLS domain.

[Configuring TE Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0200_1.html)

Configure TE attributes for links so that SR-MPLS TE paths can be adjusted based on the TE attributes during path computation.

[Globally Enabling the SR Capability](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0008.html)

Globally enabling the SR capability on forwarders is a prerequisite for configuring an SR-MPLS TE tunnel.

[Configuring Basic SR-MPLS TE Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0027_1.html)

This section describes how to configure basic SR-MPLS TE functions.

[Configuring OSPF-based Topology Reporting](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0009.html)

Before creating an SR-MPLS TE tunnel, enable OSPF to report network topology information.

[Configuring an SR-MPLS TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0010.html)

A tunnel interface must be configured on an ingress so that the interface is used to establish and manage an SR-MPLS TE tunnel.

[(Optional) Configuring UCMP for SR-MPLS TE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0101_1.html)

When multiple SR-MPLS TE tunnels are destined for a downstream device, you can configure weights to load balance traffic among the SR-MPLS TE tunnels in unequal cost multipath (UCMP) mode.

[(Optional) Configuring SR on a PCC](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0011.html)

Configure SR on a PCE client (PCC), so that a controller can deliver path information to the PCC (forwarder) after path computation.

[Verifying the OSPF SR-MPLS TE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0014.html)

After configuring an automatic SR-MPLS TE tunnel, verify information about the SR-MPLS TE tunnel and its status statistics.