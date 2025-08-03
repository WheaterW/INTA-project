Specifying an MPLS TTL Handling Mode
====================================

An MPLS time to live (TTL) handling mode defines how a node propagates TTL information between the IP header and label stack in each MPLS packet.

#### Usage Scenario

MPLS nodes handle TTLs as follows:

* Nodes process TTLs in either uniform or pipe mode before the TTLs expire. You can configure an MPLS TTL processing mode on the ingress PE.
  
  Configure the pipe mode on the ingress for an MPLS virtual private network (VPN) so that the MPLS backbone network structure can be hidden, which improves network security.
* Nodes process expired MPLS TTLs and reply with ICMP reply messages.
  
  On an ISP backbone network that transmits VPN traffic over MPLS tunnels, after an MPLS node receives an MPLS packet with two labels and an expired TTL, the MPLS node replies to the source with an ICMP reply message. Because the MPLS node cannot send the ICMP reply message over IP routes, the ICMP reply message travels along an LSP to the egress. The egress forwards the ICMP reply message to the source over IP routes.
  
  On an ISP backbone that transmits VPN traffic over MPLS tunnels, after an MPLS node receives MPLS packets each with a single label and an expired TTL, the MPLS node replies to the source with an ICMP reply message over IP routes, without forwarding the message to the egress along the LSP. If the MPLS node has no reachable route to the transmit end, the ICMP reply message is discarded. As a result, traceroute results do not contain node information.
  
  On an autonomous system boundary router (ASBR) in the inter-AS VPN Option B and a superstratum provider edge (SPE) of the hierarchy of virtual private networks (HoVPNs), each MPLS packet that contains VPN information carries a single label. If the TTL in the MPLS packet expires, a node replies with an ICMP reply message over an IP route, and the ICMP reply message does not carry MPLS node information. Therefore, before you perform the traceroute operation on the ASBR or SPE, run the [**undo ttl expiration pop**](cmdqueryname=undo+ttl+expiration+pop) command on the ASBR or SPE to enable ICMP reply messages to travel along original LSPs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For details about HoVPN and SPE, see the chapter "VPN" in *Universal Service Router Configuration Guide*.



#### Pre-configuration Task

Before configuring an MPLS TTL processing mode, configure MPLS or the MPLS IP VPN.


[Specifying the TTL Mode for MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0005.html)

MPLS nodes process TTLs in either uniform or pipe mode.

[Configuring the Path for ICMP Reply Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsm_cfg_0006.html)

The path along which ICMP reply messages travel must be specified on both the ingress and egress.