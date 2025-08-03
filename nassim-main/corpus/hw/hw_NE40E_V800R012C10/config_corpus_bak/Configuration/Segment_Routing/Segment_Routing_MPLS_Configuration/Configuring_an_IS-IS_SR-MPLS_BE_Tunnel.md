Configuring an IS-IS SR-MPLS BE Tunnel
======================================

This section describes the detail steps for configuring an IS-IS SR-MPLS BE tunnel.

#### Usage Scenario

Creating an IS-IS SR-MPLS BE tunnel involves the following operations:

* Devices report topology information to a controller (if the controller is used to create a tunnel) and are assigned labels.
* The devices compute paths.

#### Pre-configuration Tasks

Before configuring an IS-IS SR-MPLS BE tunnel, complete the following tasks:

* Configure IS-IS to implement network layer connectivity for NEs.


[Enabling MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0011.html)

Enabling MPLS on each node in an SR-MPLS domain is the prerequisites for configuring an SR-MPLS BE tunnel.

[Configuring Basic SR-MPLS BE Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0001.html)

This section describes how to configure basic SR-MPLS BE functions.

[(Optional) Configuring Strict SR-MPLS Capability Check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0019.html)

Strict SR-MPLS capability check enables a node, when computing an SR-MPLS BE LSP (SR LSP for short), to check whether all nodes along the SR LSP support SR-MPLS. This prevents forwarding failures caused by the existence of SR-MPLS-incapable nodes on the SR LSP.

[(Optional) Configuring a Policy for Triggering SR-MPLS BE LSP Establishment](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0002.html)

A policy can be configured to allow the ingress node to establish SR-MPLS BE LSPs based on eligible routes.

[(Optional) Configuring a Policy to Prioritize SR-MPLS BE Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0003.html)

You can configure a policy to prioritize SR-MPLS BE tunnels so that they can be preferentially selected.

[Verifying the IS-IS SR-MPLS BE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr-be_cfg_0009.html)

After configuring an SR-MPLS BE tunnel, verify the configuration of the SR-MPLS BE tunnel.