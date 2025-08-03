Adjusting Parameters for Establishing an MPLS TE Tunnel
=======================================================

Multiple attributes are used to establish MPLS TE tunnels flexibly.

#### Usage Scenario

During the establishment of an MPLS TE tunnel, special configurations are required.


#### Context

Before adjusting parameters for establishing an MPLS TE tunnel, complete the following task:

* [Configure an RSVP-TE tunnel.](dc_vrp_te-p2p_cfg_0003.html)


[Configuring an MPLS TE Explicit Path](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0115.html)

An explicit path is configured on the ingress of an MPLS TE tunnel to define the nodes through which the MPLS TE tunnel passes and the nodes that are excluded from the MPLS TE tunnel.

[Setting Priority Values for an MPLS TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0026.html)

The priority values are set on the ingress of an MPLS TE tunnel. Preemption is performed based on the setup and holding priorities during the establishment of an MPLS TE tunnel.

[Setting the Hop Limit for a CR-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0027.html)

The hop limit set on an ingress is the maximum number of hops on a path along which a CR-LSP is to be established. The hop limit is a constraint used during path selection.

[Associating CR-LSP Establishment with the Overload Setting](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0184.html)

CR-LSP establishment can be associated with the overload setting. This association ensures that CR-LSPs are established over paths excluding overloaded nodes.

[Configuring Route and Label Record](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0028.html)

An ingress can be configured to allow routes and labels to be recorded along a path over which an RSVP-TE CR-LSP will be established.

[Setting Switching and Deletion Delays](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0031.html)

The switching and deletion delays are set to ensure that a CR-LSP is torn down only after a new CR-LSP has been established, which prevents traffic interruption.

[Verifying the Configuration of Establishment of MPLS TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0032.html)

After adjusting the establishment of the MPLS TE tunnel, you can view information about the tunnel interface.