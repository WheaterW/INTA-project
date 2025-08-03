Configuring an RSVP GR Helper
=============================

An RSVP GR Helper is configured to allow devices along an RSVP-TE tunnel to retain RSVP sessions during a master/backup switchover.

#### Usage Scenario

The NE40E can only function as a GR Helper to help a neighbor node to complete RSVP GR. Therefore, this function needs to be configured only when RSVP GR is deployed on the neighbor node. If a local device is only connected to NE40Es running the same version with the local device, there is no need to configure the RSVP GR Helper on the local device.


#### Pre-configuration Tasks

Before configuring an RSVP GR Helper, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0094.html).


[Enabling the RSVP Hello Extension](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0062.html)

The RSVP Hello extension is configured on a GR node and its neighbor to rapidly monitor reachability between these RSVP nodes.

[Enabling the RSVP GR Support Capability](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0063.html)

The RSVP GR support capability helps a node support its neighbors' GR capabilities.

[(Optional) Configuring a Hello Session Between RSVP GR Nodes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0064.html)

If TE FRR is deployed, a Hello session must be established between a PLR and an MP. A Hello session must be manually established if it cannot be automatically established between RSVP neighboring nodes.

[Verifying the RSVP GR Helper Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0066.html)

After configuring RSVP GR, you can verify that the TE tunnel properly forwards data during the GR process.