Configuring an Automatic RSVP-TE Tunnel
=======================================

Automatic RSVP-TE tunnels are generated using the PCE Initiated LSP protocol. Such tunnels do not need to be manually configured.

#### Usage Scenario

In an SDN solution, a controller can run the PCE Initiated LSP protocol to generate RSVP-TE tunnels, without manual tunnel configuration. Dynamic RSVP-TE signaling adjusts paths of TE tunnels dynamically based on network changes. To implement reliability functions, such as TE FRR and CR-LSP backup, using RSVP-TE to establish MPLS TE tunnels is recommended.


#### Pre-configuration Tasks

Before configuring an automatic RSVP-TE tunnel, complete the following tasks:

* Configure IS-IS to implement network layer connectivity for LSRs.
* Set an LSR ID for each LSR.
* Enable MPLS globally and on interfaces on all LSRs.


[Enabling MPLS TE and RSVP-TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0218.html)

Enabling MPLS TE and RSVP-TE on each node and interface in an MPLS domain is the prerequisites for all TE features.

[(Optional) Configuring CSPF](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0226.html)

CSPF is configured to calculate the shortest path destined for a specified node.

[Configuring IGP TE (OSPF or IS-IS)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0005_copy.html)

After IGP TE is configured on all LSRs in an MPLS domain, a TEDB is generated on each LSR.

[Configuring the Automatic RSVP-TE Tunnel Capability on a PCC](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0219.html)

The PCE Initiated LSP protocol needs to be configured for automatic RSVP-TE tunnels. A controller runs this protocol to deliver tunnel and path information to the ingress on which a forwarder resides. Upon receipt of the information, the ingress automatically establishes an RSVP-TE tunnel.

[Configuring Dynamic BFD For Initiated RSVP-TE LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0220.html)

LSPs that a controller runs the PCE Initiated LSP protocol to establish can only be monitored by dynamic BFD.

[Configuring Dynamic BFD for Initiated RSVP-TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0221.html)

RSVP-TE tunnels that a controller runs the PCE Initiated LSP protocol to establish can only be monitored by dynamic BFD.

[(Optional) Enabling Traffic Statistics Collection for Automatic Tunnels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0222.html)

A device can be enabled to collect traffic statistics on RSVP-TE tunnels that are established by the PCE Initiated LSP protocol.

[Verifying the Automatic RSVP-TE Tunnel Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0223.html)

After configuring an automatic RSVP-TE tunnel, you can check information about the RSVP-TE tunnel and its status statistics.