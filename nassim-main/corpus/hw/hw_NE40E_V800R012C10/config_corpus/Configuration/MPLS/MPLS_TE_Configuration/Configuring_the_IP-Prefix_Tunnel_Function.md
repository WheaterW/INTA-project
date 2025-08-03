Configuring the IP-Prefix Tunnel Function
=========================================

The IP-prefix tunnel function can be configured and used to establish P2P RSVP-TE tunnels in a batch, which simplifies the configuration.

#### Usage Scenario

When you want to create a large number of P2P RSVP-TE tunnels or create P2P RSVP-TE tunnels to form a full-mesh network, creating them one by one is laborious and complex. To simplify MPLS RSVP-TE tunnel configuration, configure the IP-prefix tunnel function so that P2P RSVP-TE tunnels can be established in a batch.

The full-mesh network indicates that a P2P RSVP-TE tunnel is established between any two nodes on a network.


#### Pre-configuration Tasks

Before configuring the ip-prefix tunnel function, complete the following tasks:

* Configure an IGP to implement connectivity at the network layer.
* [Enable MPLS TE and RSVP-TE.](dc_vrp_te-p2p_cfg_0004.html)
* [Configure IGP TE (OSPF or IS-IS).](dc_vrp_te-p2p_cfg_0005.html)
* [(Optional) Configure TE attributes for links.](dc_vrp_te-p2p_cfg_0006.html)


[Configuring an IP Prefix List](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0206.html)

An IP prefix list can be configured to define destination IP addresses used in the ip-prefix tunnel function.

[(Optional) Configuring a P2P TE Tunnel Template](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0207.html)

A P2P TE tunnel template can be configured, and MPLS TE tunnel attributes can be set in the template.

[Using the Automatic Primary Tunnel Function to Establish P2P TE Tunnels in a Batch](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0208.html)

The automatic primary tunnel function can be used to establish P2P TE tunnels in a batch.

[Verifying the IP-Prefix Tunnel Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0209.html)

After configuring the IP-prefix tunnel function, verify the tunnel information, including the tunnel status, a P2P TE tunnel template used to establish tunnels, and IP prefix list.