Configuring PCEP to Trigger SR-MPLS TE Policy Establishment
===========================================================

PCEP-based path computation for establishing SR-MPLS TE Policies enables devices to quickly respond to service requests and properly use network resources.

#### Usage Scenario

PCEP involves two PCE roles â PCE server and PCE client. The PCE server computes paths and stores network-wide path information. The PCE client receives and uses path information.

As each forwarder has a built-in PCE Client component, it functions as a PCE client. A controller typically functions as a PCE server.


#### Pre-configuration Tasks

Before configuring PCEP to trigger SR-MPLS TE Policy establishment, complete the following tasks:

* Configure IGP (IS-IS/OSPF) to enable nodes to communicate at the network layer.
* Enable SR-MPLS.


[Enabling a PCE Client to Process SR-MPLS TE Policies](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0023.html)

Configure a PCE client and establish a session between the PCE client and server so that the PCE client can receive SR-MPLS TE Policy information delivered by the PCE server.

[Specifying Candidate PCE Servers for a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0014a.html)

One or more candidate PCE servers can be specified to compute paths for a PCE client. If multiple such servers are specified, they work in backup mode, improving network reliability.

[Configuring Constraints for PCEP to Compute SR-MPLS TE Policy Paths](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0015.html)

Before configuring PCEP to compute an SR-MPLS TE Policy path, you can perform the following steps to configure specific path constraints.

[(Optional) Configuring Timers for a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0017a.html)

The Keepalive timer, Hold timer, and LSP Delegate-hold timer can be set for a PCE client.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0025.html)

After configuring PCE client functions, you can check PCEP session information and PCEP statistics to verify the configuration.