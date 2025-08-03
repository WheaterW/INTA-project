Configuring LDP over TE
=======================

The LDP over TE function applies to the network on which core devices support TE, whereas edge devices support LDP. A TE tunnel functions as one hop of the entire LDP LSP.

#### Usage Scenario

LDP over TE is a technique used to establish LDP LSPs across an RSVP TE domain and provide services for a VPN. To deploy MPLS TE on a network transmitting VPN services, a carrier has difficulties in deploying TE on an entire network. The carrier can plan a core area in which TE is deployed, and implement LDP on PEs on the edge of the TE area.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the IGP route used by LDP is switched from a TE interface to a non-TE tunnel interface, ensure that IGP and LDP are configured on the non-TE tunnel interface. Otherwise, the LDP LSP may fail to be established after the switchover, causing service interruptions.



#### Pre-configuration Tasks

Before configuring LDP over TE, complete the following tasks:

* Configure an IGP to ensure connectivity between LSRs at the network layer.
* Configure basic MPLS functions on nodes and interfaces.
* Enable MPLS LDP on the edge devices of the TE area and the interfaces outside the TE area.
* Establish an RSVP-TE tunnel along the TE nodes.
* Configure tunnel IP addresses.
* Configure virtual TE interfaces.


[Configuring IGP Shortcut](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0034_1.html)

After IGP shortcut is configured on the ingress of a CR-LSP, the CR-LSP is not advertised to or used by neighbors.

[Configuring Forwarding Adjacency](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0035_1.html)

The forwarding adjacency is configured on the ingress of a CR-LSP. The forwarding adjacency allows a route of a CR-LSP to be advertised to neighbors so that these neighbors can use this CR-LSP to transmit traffic.

[Creating Remote LDP Peers on Both Ends of a TE Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0029.html)

Configure nodes on both ends of a TE tunnel as remote LDP peers.

[(Optional) Configuring a Policy for Triggering LSP Establishment](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0030.html)

A policy can be configured to allow LDP to establish LSPs for eligible routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0031.html)

After configuring LDP over TE, you can view information about an LDP LSP on the ingress.