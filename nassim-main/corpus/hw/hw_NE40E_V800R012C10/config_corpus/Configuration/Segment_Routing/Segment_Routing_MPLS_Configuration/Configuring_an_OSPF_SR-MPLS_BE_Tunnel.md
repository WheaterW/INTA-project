Configuring an OSPF SR-MPLS BE Tunnel
=====================================

This section describes how to configure an OSPF SR-MPLS BE tunnel.

#### Usage Scenario

Creating an OSPF SR-MPLS BE tunnel involves the following operations:

* Devices report topology information to a controller (if the controller is used to create a tunnel) and are assigned labels.
* The devices compute paths.

#### Pre-configuration Tasks

Before configuring an OSPF SR-MPLS BE tunnel, complete the following tasks:

* Configure OSPF to implement the connectivity of NEs at the network layer.


[Enabling MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0011_1.html)

Enabling MPLS on each node in an SR-MPLS domain is the prerequisites for configuring an SR-MPLS BE tunnel.

[Configuring Basic SR-MPLS BE Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0002.html)

This section describes how to configure basic SR-MPLS BE functions.

[(Optional) Configuring Strict SR-MPLS Capability Check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0020.html)

Strict SR-MPLS capability check enables a node, when computing an SR-MPLS BE LSP (SR LSP for short), to check whether all nodes along the SR LSP support SR-MPLS. This prevents forwarding failures caused by the existence of SR-MPLS-incapable nodes on the SR LSP.

[(Optional) Configuring a Policy for Triggering SR-MPLS BE LSP Establishment](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0003.html)

A policy can be configured to allow the ingress node to establish SR-MPLS BE LSPs based on eligible routes.

[(Optional) Configuring a Policy to Prioritize SR-MPLS BE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0004.html)

You can configure a policy to prioritize SR-MPLS BE tunnels so that they can be preferentially selected.

[Verifying the OSPF SR-MPLS BE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0005.html)

After successfully configuring SR-MPLS BE, verify SR-MPLS BE configurations.