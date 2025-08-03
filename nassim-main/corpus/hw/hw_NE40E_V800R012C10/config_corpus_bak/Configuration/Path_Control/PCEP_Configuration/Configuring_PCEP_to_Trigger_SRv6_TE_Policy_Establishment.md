Configuring PCEP to Trigger SRv6 TE Policy Establishment
========================================================

PCEP-based path computation for establishing SRv6 TE Policies enables devices to quickly respond to service requests and properly use network resources.

#### Usage Scenario

PCEP involves two PCE roles â PCE server and PCE client. The former computes paths and stores network-wide path information. The latter receives and uses path information.

As each forwarder has a built-in PCE Client component, it functions as a PCE client. A controller typically functions as a PCE server.


#### Pre-configuration Tasks

Before configuring PCEP to trigger SRv6 TE Policy establishment, complete the following tasks:

* Configure IGP (IS-IS/OSPFv3) to enable nodes to communicate at the network layer.
* Enable SRv6.


[Enabling a PCE Client to Process SRv6 TE Policies](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0013.html)

Configure a PCE client and establish a session between the PCE client and server so that the PCE client can receive SRv6 TE Policy information delivered by the PCE server.

[Specifying Candidate PCE Servers for a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0014.html)

One or more candidate PCE servers can be specified to compute paths for a PCE client. If multiple such servers are specified, they work in backup mode, improving network reliability.

[(Optional) Configuring Timers for a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0017.html)

The Keepalive timer, Hold timer, and LSP Delegate-hold timer can be set for a PCE client.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0018.html)

After configuring PCE client functions, you can check PCEP session information and PCEP statistics to verify the configuration.