Configuring RIP to Advertise Default Routes
===========================================

Default routes are destined for 0.0.0.0.

#### Context

In a routing table, the default route is a route to 0.0.0.0 with mask 0.0.0.0. You can run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check whether the default route is configured. When the destination address of a packet does not match any entry in the routing table, the Router forward this packet along a default route.

If the default route and the destination address of the packet do not exist in the routing table, the Router discards the packet and sends an Internet Control Message Protocol (ICMP) packet, informing the originating host that the destination address or network is unreachable.

After the [**default-route originate**](cmdqueryname=default-route+originate) command is run, default routes are advertised to RIP neighbors only when there are default routes in the routing table, and the default route that is learned from a neighbor is deleted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**default-route originate**](cmdqueryname=default-route+originate) [ **cost** *cost* | **tag** *tag* | { **match default** | { **route-policy** *route-policy-name* [ **advertise-tag** ] | **route-filter** *route-filter-name* } } [ **avoid-learning** ] ] \*
   
   
   
   RIP is enabled to advertise default routes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.