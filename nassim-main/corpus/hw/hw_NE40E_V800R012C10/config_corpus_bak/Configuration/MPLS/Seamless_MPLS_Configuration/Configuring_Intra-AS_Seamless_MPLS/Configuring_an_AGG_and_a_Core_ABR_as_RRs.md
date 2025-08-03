Configuring an AGG and a Core ABR as RRs
========================================

In the intra-AS seamless MPLS networking, the AGG and core ABR can be configured as RRs so that CSGs and MASGs can learn loopback routes from one another. The loopback route information is used to establish an MP-IBPG peer relationship between each CSG and MASG.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
   
   
   
   An RR is configured, and the peer is specified as a client.
   
   The AGG's clients are its connected CSG and core ABR. The core ABR's clients are its connected AGG and MASG.
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
   
   
   
   The device is configured to use its own IP address as the next-hop address of routes when advertising these routes.
   
   
   
   To enable the AGG or core ABR to advertise routes with the next-hop address set to its own IP address, run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command on the AGG or core ABR.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.