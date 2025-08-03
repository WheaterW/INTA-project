Configuring Route Exchange Between a Hub-PE and a Spoke-PE
==========================================================

By importing extended community attributes to BGP, MP-IBGP can advertise VPNv6 routes between PEs.

#### Context

MP-IBGP peer relationships need be established between the Hub-PE and each Spoke-PE. Spoke-PEs need not exchange routes directly and therefore they do not need to establish MP-IBGP peer relationships.

Perform the following steps on the Hub-PE and all the Spoke-PEs:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address* **as-number** *as-number*
   
   
   
   The remote PE is configured as a BGP peer.
4. Run [**peer**](cmdqueryname=peer) *peer-address* **connect-interface** **loopback** *interface-number*
   
   The interface used to establish a TCP connection is specified.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PEs must use the loopback interface addresses with 32-bit masks to establish an MP-IBGP peer relationship so that routes can recurse to the tunnel. The route to the loopback interface is advertised to the peer PE through IGP on the MPLS backbone network.
5. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** [**unicast**]
   
   
   
   The BGP-VPN IPv6 address family view is displayed.
6. Run [**peer**](cmdqueryname=peer) *peer-address* **enable**
   
   
   
   The capability of exchanging BGP VPNv6 routing information with the peer is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.