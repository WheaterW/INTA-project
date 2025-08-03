(Optional) Prohibiting a Local Device from Adding the Peer Host Route to the Local Routing Table of Direct Routes
=================================================================================================================

To avoid incorrect routing information in the local routing
table, you can prohibit a local device from adding the peer host route
to the local routing table of direct routes.

#### Context

Devices on both ends of a PPP link may have IP addresses
at different network segments. When the two devices communicate with
each other, one device automatically adds the host route of the other
end to the local routing table of direct routes. If one end has an
incorrect IP address configured, incorrect routing information will
be advertised on the network. To prevent incorrect routing information,
prohibit the local device from adding the peer host route to the local
routing table of direct routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ppp peer hostroute-suppress**](cmdqueryname=ppp+peer+hostroute-suppress)
   
   
   
   The device is prohibited from adding the peer
   host route to the local routing table of direct routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.