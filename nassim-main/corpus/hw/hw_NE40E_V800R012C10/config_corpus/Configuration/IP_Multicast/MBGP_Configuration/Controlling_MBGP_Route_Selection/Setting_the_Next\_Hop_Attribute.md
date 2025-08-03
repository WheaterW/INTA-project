Setting the Next\_Hop Attribute
===============================

MBGP route selection can be flexibly controlled by setting the Next\_Hop attribute.

#### Context

Different from that in IGP, the next-hop address in MBGP may not be the IP address of a peer Router.


#### Procedure

* Configure a device to change the next-hop address when it advertises a route to an IBGP peer.
  
  
  
  Perform the following steps on the IBGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run the [**ipv4-family multicast**](cmdqueryname=ipv4-family+multicast) command to enter the BGP-IPv4 multicast address family view, or run the **[**ipv4-multicast vpn-instance**](cmdqueryname=ipv4-multicast+vpn-instance)** **vpn-instance-name** command to enter the BGP-multicast VPN instance IPv4 address family view.
  4. Run [**peer**](cmdqueryname=peer) { *peer-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
     
     
     
     The local address is configured as the next-hop address for route advertisement.
     
     
     
     To ensure that an IBGP peer can find the correct next hop, configure the local device to change the next-hop address of a route to be its own address when the local device advertises the route to the IBGP peer.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If MBGP load balancing is configured, the local Router changes the next-hop address to be its own address when advertising routes to IBGP peer groups, regardless of whether the [**peer**](cmdqueryname=peer) { *group-name* | *peer-address* } [**next-hop-local**](cmdqueryname=next-hop-local) command is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.