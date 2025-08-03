Configuring Dynamic BFD for LDP LSPs
====================================

Dynamic bidirectional forwarding detection (BFD) for LDP LSPs is used to rapidly check LDP LSP connectivity to improve network reliability.

#### Usage Scenario

Dynamic BFD for LDP LSPs detects link faults rapidly and reduces configuration workloads. It can be used together with LDP FRR to reduce the impact of link faults on services.

Note that dynamic BFD can be used to check LDP LSPs established only using host routes.


#### Pre-configuration Tasks

Before configuring dynamic BFD for LDP LSPs, complete the following tasks:

* Configure network layer parameters to implement network layer connectivity.
* [Enable MPLS LDP on each node and establish an LDP session.](dc_vrp_ldp-p2p_cfg_0003.html)
* [Configure an LDP LSP.](dc_vrp_ldp-p2p_cfg_0015.html)


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2040.html)

BFD-related configurations can be performed only after BFD is enabled globally.

[Enabling the Function to Dynamically Create BFD Sessions in MPLS Scenarios](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2041.html)

Enable BFD on the ingress and egress in an MPLS domain, after which BFD sessions can be dynamically created.

[Configuring a Policy for Triggering Dynamic BFD for LDP LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2042.html)

Configure a policy for dynamically establishing a BFD session to monitor LDP LSPs and create a BFD session.

[(Optional) Modifying BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2043.html)

BFD parameters, such as BFD detection intervals and detection multipliers, can be modified.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2044.html)

After configuring dynamic BFD for LDP LSP, you can view BFD configurations and session information on the ingress and egress of a specified LDP LSP.