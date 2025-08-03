Configuring a Static Bidirectional Co-routed LSP
================================================

A static bidirectional co-routed label switched path (LSP) is composed of two static constraint-based routed (CR) LSPs in opposite directions. Multiprotocol Label Switching (MPLS) Traffic Engineering (TE) supports MPLS forwarding in both directions along such an LSP.

#### Usage Scenario

A static CR-LSP is easy to configure because its labels are manually assigned, and no signaling protocol is used to exchange control packets. The setup of a static CR-LSP consumes only a few resources, and you do not need to configure IGP TE or CSPF for the static CR-LSP. As a static CR-LSP cannot dynamically adapt to network changes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The value of the outgoing label on each node is the value of the incoming label on its next hop.
* The destination address of a static bidirectional co-routed LSP is the destination address specified on the tunnel interface.



#### Pre-configuration Tasks

Before configuring a static bidirectional co-routed LSP, complete the following tasks:

* Configure unicast static routes or an IGP to implement connectivity between LSRs.
* Configure an LSR ID for each LSR.
* Enable MPLS globally and on interfaces on all LSRs.


[Enabling MPLS TE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0153.html)

Before setting up a static bidirectional co-routed LSP, you must enable MPLS TE.

[(Optional) Configuring Link Bandwidth](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0177_copy.html)

By configuring the link bandwidth, you can constrain the bandwidth of a CR-LSP. This section describes how to configure link bandwidth so that nodes can reserve the configured link bandwidth for an LSP to be established.

[Configuring a Tunnel Interface on the Ingress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0155.html)

A tunnel interface must be created before an MPLS TE tunnel is established on an ingress.

[(Optional) Configuring Global Dynamic BandwidthPre-verification](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0215_copy.html)

Global dynamic bandwidth pre-verification enables a device to check dynamic bandwidth usage before a static CR-LSP, or a static bidirectional co-routed LSP is established.

[Configuring the Ingress of a Static Bidirectional Co-routed LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0156.html)

The ingress of a static bidirectional co-routed LSP needs to be manually specified.

[(Optional) Configuring a Transit Node of a Static Bidirectional Co-routed LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0157.html)

The transit node of a static bidirectional co-routed LSP needs to be manually specified. This configuration is optional because a static bidirectional co-routed LSP may have no transit node.

[Configuring the Egress of a Static Bidirectional Co-routed CR-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0158.html)

The egress of a static bidirectional co-routed CR-LSP needs to be manually specified.

[Configuring the Tunnel Interface on the Egress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0159.html)

The reverse tunnel attribute is configured, and the tunnel interface is bound to a static bidirectional co-routed LSP on the egress.

[Verifying the Configuration of a Static Bidirectional Co-routed LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0160.html)

After configuring a static bidirectional co-routed LSP, you can view its status.