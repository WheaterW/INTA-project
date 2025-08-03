Adjusting RSVP Signaling Parameters
===================================

RSVP-TE supports various signaling parameters, which meet requirements for reliability and network resources, and requirements of MPLS TE advanced functions.

#### Usage Scenario

RSVP TE supports diversified signaling parameters, which meet requirements of reliability, network resources, and some advanced MPLS TE features.


#### Pre-configuration Tasks

Before adjusting RSVP signaling parameters, complete the following task:

* [Enable MPLS TE and RSVP-TE.](dc_vrp_te-p2p_cfg_0004.html)


[Configuring the RSVP Hello Extension](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0012.html)

The RSVP Hello extension rapidly monitors the connectivity of RSVP neighbors.

[Configuring an RSVP Timer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0013.html)

An RSVP timer is configured to define the interval at which Path and Resv messages are refreshed, and the timeout multiplier associated with the RSVP blocked state is also configured.

[(Optional) Configuring Reliable RSVP Message Transmission](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0245.html)

When BFD is not configured on a network, reliable RSVP message transmission can be configured to increase the success rate of detecting link faults, which minimize long-time traffic loss inducted by link intermittent disconnections.

[Configuring RSVP-TE Srefresh](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0014.html)

Enabling Summary Refresh (Srefresh) on interfaces connecting two RSVP neighboring nodes reduces the network cost and improves network performance. 

[Enabling RSVP-TE Reservation Confirmation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0015.html)

RSVP-TE reservation confirmation configured on the egress of a tunnel verifies that resources are successfully reserved.

[Changing the PSB and RSB Timeout Multiplier](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0016.html)

The PSB and RSB timeout multiplier defines the maximum number of signaling packets that can be discarded in a weak signaling environment.

[Verifying the Configuration of Adjusting RSVP Signaling Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0017.html)

After adjusting RSVP signaling parameters, you can view the refresh parameters, RSVP reservation confirmation status, RSVP Hello extension status, and RSVP timer parameters.