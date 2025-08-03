Importing Traffic to an MPLS TE Tunnel
======================================

Before importing traffic to an MPLS TE tunnel, familiarize yourself with the usage scenario, complete the pre-configuration tasks for the configuration.

#### Usage Scenario

An MPLS TE tunnel does not automatically import traffic. To enable traffic to travel along an MPLS TE tunnel, use one of the methods listed in [Table 1](#EN-US_TASK_0172368174__tab_dc_vrp_te-p2p_cfg_003301) to import the traffic to the MPLS TE tunnel.

**Table 1** Methods to import traffic to an MPLS TE tunnel
| Methods to Import Traffic to an MPLS TE Tunnel | Principles | Usage Scenario | Related Configuration Links |
| --- | --- | --- | --- |
| Use static routes | This is the simplest method for importing the traffic to an MPLS TE tunnel. You only need to configure a static route with a TE tunnel interface as the outbound interface. | Scenario where public-network routes are used to import traffic to a TE or LDP over TE tunnel | [Configuring IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0003.html) |
| Use the auto route mechanism | A TE tunnel is used as a logical link for IGP route calculation. A tunnel interface is used as an outbound interface of a route. The auto route mechanism can be implemented in either of the following modes:   * IGP shortcut: A device uses a TE tunnel for local route calculation and does not advertise the TE tunnel to its peers as a route. Therefore, the peers of this device cannot use the TE tunnel for route calculation. * Forwarding adjacency: A device uses a TE tunnel for local route calculation and advertises the TE tunnel to its peers as a route. Therefore, the peers of this device can use the TE tunnel for route calculation. | Scenario where public-network routes are used to import traffic to a TE or LDP over TE tunnel | [Configuring the IGP Shortcut](dc_vrp_te-p2p_cfg_0034.html)  [Configuring Forwarding Adjacency](dc_vrp_te-p2p_cfg_0035.html) |
| Policy-Based Routing | The policy-based routing (PBR) allows a device to select routes based on user-defined policies.  TE PBR, the same as IP unicast PBR, is implemented by defining a set of matching rules and behaviors. The rules and behaviors are defined using the apply clause with a TE tunnel interface used as an outbound interface. If packets do not match PBR rules, they are properly forwarded using IP; if they match PBR rules, they are forwarded over specific tunnels. | Scenario where public-network routes are used to import traffic to a TE or LDP over TE tunnel | - |
| Tunnel Policy | By default, VPN traffic is forwarded through LDP LSPs. If the default LDP LSPs cannot meet VPN traffic requirement, a tunnel policy is used to direct VPN traffic to a TE tunnel. The tunnel policy may be a tunnel type prioritizing policy or a tunnel binding policy. Select either of the following policies as needed:  * Select-seq mode: This policy changes the type of tunnel selected for VPN traffic. A TE tunnel is selected as a public tunnel for VPN traffic based on the prioritized tunnel types. * Tunnel binding mode: This policy defines a specific destination IP address, and this address is bound to a TE tunnel. | VPN scenario | [VPN Tunnel Management Configuration](dc_vrp_tnlm_cfg_0001.html) |



![](../../../../public_sys-resources/note_3.0-en-us.png) 

The preceding methods to import traffic to MPLS TE tunnels apply only to P2P tunnels.



#### Pre-configuration Tasks

Before you import traffic to an MPLS TE tunnel, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).


[Configuring IGP Shortcut](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0034.html)

After IGP shortcut is configured on the ingress of a CR-LSP, the CR-LSP is not advertised to or used by neighbors.

[Configuring Forwarding Adjacency](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0035.html)

The forwarding adjacency is configured on the ingress of a CR-LSP. The forwarding adjacency allows a route of a CR-LSP to be advertised to neighbors so that these neighbors can use this CR-LSP to transmit traffic.

[(Optional) Configuring CBTS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_te-p2p_cfg_0001.html)

Service class can be set for packets that MPLS TE tunnels allow to pass through.