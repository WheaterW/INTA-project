Configure an AGG as an RR
=========================

In the inter-AS seamless MPLS networking, an AGG is configured as an RR to advertise the route to the CSG's loopback interface to an AGG ASBR, and the AGG ASBR advertises the route to the core layer over an EBGP peer connection. The loopback route information is used to establish an MP-EBGP peer relationship between each CSG and MASG.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
   
   
   
   An RR is configured, and the CSG and AGG ASBR are specified as its clients.
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
   
   
   
   The device is configured to use its own IP address as the next-hop address of routes when advertising these routes.
   
   To enable the AGG to advertise routes with the next-hop address set to its own address, run the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command on the AGG.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.