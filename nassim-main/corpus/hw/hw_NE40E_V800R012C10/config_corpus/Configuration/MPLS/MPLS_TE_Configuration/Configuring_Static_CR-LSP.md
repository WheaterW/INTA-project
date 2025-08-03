Configuring Static CR-LSP
=========================

This section describes how to configure a static CR-LSP. The configuration of a static CR-LSP is simple, and label allocation is performed manually, not by using a signaling protocol to exchange control packets, which consumes a few resources.

#### Usage Scenario

A static CR-LSP is easy to configure: Labels are manually allocated, and no signaling protocol is used to exchange control packets. The setup of a static CR-LSP consumes only a few resources, and you do not need to configure IGP TE or CSPF for the static CR-LSP. However, static CR-LSPs cannot be dynamically adjusted according to network changes. Therefore, static CR-LSPs have limited applications.

The static CR-LSP configurations involve the operations on the following types of nodes:

* Ingress: An LSP forwarding entry is configured, and an LSP configured on the ingress is bound to the TE tunnel interface.
* Transit node: An LSP forwarding entry is configured.
* Egress: An LSP forwarding entry is configured.


#### Pre-configuration Tasks

Before configuring a static CR-LSP, complete the following tasks:

* Configure the static route or IGP to implement the reachability between LSRs.
* Configure an LSR ID for each LSR.
* Enable MPLS globally and on interfaces on all LSRs.


[Enabling MPLS TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0176.html)

Before you set up a static CR-LSP, enable MPLS TE.

[(Optional) Configuring Link Bandwidth](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0177.html)

By configuring the link bandwidth, you can constrain the bandwidth of a CR-LSP. This section describes how to configure link bandwidth so that nodes can reserve the configured link bandwidth for an LSP to be established.

[Configuring the MPLS TE Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0178.html)

This section describes how to configure the MPLS TE tunnel interface. You must create a tunnel interface before setting up an MPLS TE tunnel.

[(Optional) Configuring Global Dynamic Bandwidth Pre-Verification](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0215.html)

Global dynamic bandwidth pre-verification enables a device to check dynamic bandwidth usage before a static CR-LSP, or a static bidirectional co-routed LSP is established.

[Configuring the Ingress of the Static CR-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0179.html)

This section describes how to configure the ingress of a static CR-LSP. Before you establish a static CR-LSP, specify the ingress of the CR-LSP.

[(Optional) Configuring the Transit Node of the Static CR-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0180.html)

This section describes how to configure the transit nodes of a static CR-LSP. Before you set up a static CR-LSP, specify the transit nodes of the CR-LSP. This procedure is optional because the CR-LSP may have no transit node.

[Configuring the Egress of the Static CR-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0181.html)

This section describes how to configure the egress of a static CR-LSP. Before you set up a static CR-LSP, specify the egress of the CR-LSP.

[(Optional) Configuring a Device to Check the Source Interface of a Static CR-LSP](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_te-p2p_cfg_6007.html)

A device uses the static CR-LSP's source interface check function to check whether the inbound interface of labeled packets is the same as that of a configured static CR-LSP. If the inbound interfaces match, the device forwards the packets. If the inbound interfaces do not match, the device discards the packets.

[Verifying the Static CR-LSP Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0182.html)

After the configuration of a static CR-LSP, you can view the static CR-LSP status.