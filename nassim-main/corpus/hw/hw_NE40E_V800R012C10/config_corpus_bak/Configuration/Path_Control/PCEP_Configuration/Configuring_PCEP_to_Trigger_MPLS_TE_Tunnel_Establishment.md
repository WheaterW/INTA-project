Configuring PCEP to Trigger MPLS TE Tunnel Establishment
========================================================

The PCE function is used to calculate a path over which an MPLS TE tunnel is established, which more efficiently uses network resources than constrained shortest path first (CSPF).

#### Usage Scenario

Ingress nodes run the CSPF algorithm and use information stored in the traffic engineering database (TEDB) to calculate paths for MPLS TE tunnels. On an MPLS TE network, multiple tunnels originate from different ingress nodes and are established over paths that the ingress nodes independently calculate. As a result, network-wide resources cannot be efficiently used.

PCEP for MPLS TE can help resolve the preceding issue. PCEP involves two PCE roles â PCE server and PCE client. The PCE server computes paths and stores network-wide path information. The PCE client initiates path computation requests as the ingress of a tunnel. After receiving a path computation request from the PCE client, the PCE server computes a path based on network-wide resources to achieve optimal network resource usage.

Different from CSPF configured on the ingress, the PCE algorithm allows a PCE server to configure and manage network-wide TE information, including node, link, and tunnel attributes. Some steps in the following procedures are mandatory when CSPF is used, while are optional when PCE is used.


#### Pre-configuration Tasks

Before configuring PCEP to trigger MPLS TE tunnel establishment, complete the following tasks:

* Configure IS-IS to ensure that nodes can communicate at the network layer. For details, see [Configuring Basic IPv4 IS-IS Functions](dc_vrp_isis_cfg_1000.html).
* Perform the following operations by referring to [Configuring an RSVP-TE Tunnel](dc_vrp_te-p2p_cfg_0003.html):
  + Enable MPLS TE and RSVP-TE.
  + Enable IS-IS TE.
  + (Optional) Configure TE attributes for links.
  + Configure a tunnel interface.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a PCE server is used to configure and manage network-wide TE information and the PCE server and client have the same parameters, the configurations on the PCE server take precedence. For example, the bandwidth is set to 1000 kbit/s on a tunnel interface of a PCE client, and the bandwidth is set to 2000 kbit/s for the same tunnel on a PCE server. Only the bandwidth configured on the PCE server is used to calculate a path. If a tunnel attribute is configured for a PCE client, not for a PCE server, the attribute can take effect on the tunnel.

To improve the reliability of a TE tunnel established using PCEP, configure CR-LSP hot standby on the tunnel interface on which the TE tunnel is established.



[Configuring the Ingress as a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0003.html)

A PCE client can be configured on the ingress so that the ingress establishes a PCEP session with a PCE server and sends a request to the server over the session to calculate a path.

[Specifying Candidate PCE Servers for a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0004.html)

One or more candidate PCE servers can be specified to compute paths for a PCE client. If multiple such servers are specified, they work in backup mode, improving network reliability.

[(Optional) Configuring a PCE Client to Delegate TE LSPs to All PCE Servers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0008.html)

A PCE client can be configured to delegate TE LSPs to all PCE servers. This configuration prevents a PCE server path calculation failure that occurs when forwarders select a master PCE server different from that configured on a controller.

[(Optional) Configuring Timers for a PCE Client](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0006.html)

The Keepalive timer, Hold timer, PCReq retransmission timer, and LSP Delegate-hold timer can be set for a PCE client.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pcep_cfg_0011.html)

After configuring PCE client functions, you can check PCEP session information and PCEP statistics to verify the configuration.