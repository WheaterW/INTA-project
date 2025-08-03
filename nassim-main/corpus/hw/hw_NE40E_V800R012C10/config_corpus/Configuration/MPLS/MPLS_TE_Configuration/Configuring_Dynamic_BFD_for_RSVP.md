Configuring Dynamic BFD for RSVP
================================

This section describes how to configure a dynamic BFD session to detect faults in links between RSVP neighbors.

#### Usage Scenario

BFD for RSVP is used with TE FRR when a Layer 2 device exists on the primary LSP between a PLR and its downstream RSVP neighbor.

The interval at which a neighbor is declared Down is three times as long as the interval at which RSVP Hello messages are sent. This allows devices to detect a fault in an RSVP neighbor in seconds.

If a Layer 2 device exists on a link between RSVP nodes, an RSVP node cannot rapidly detect a link fault, which results in a great loss of data.

BFD rapidly detects faults in links or nodes on which RSVP adjacencies are deployed. If BFD detects a fault, it notifies the RSVP module of the fault and instructs the RSVP module to switch traffic to a bypass tunnel.


#### Pre-configuration Tasks

Before you configure BFD for RSVP, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0068.html)

To configure dynamic BFD for RSVP, you must enable BFD on both ends of RSVP neighbors.

[Enabling BFD for RSVP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0069.html)

You can enable BFD for RSVP either globally or on a specified interface.

[(Optional) Adjusting BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0070.html)

BFD parameters can be adjusted either globally or on a specific RSVP interface after BFD for RSVP is configured.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0071.html)

After configuring dynamic BFD for TE RSVP, you can view the status of a BFD session for RSVP.