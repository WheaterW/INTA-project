Configuring RIP to Advertise Default Routes
===========================================

Configuring RIP to Advertise Default Routes

#### Context

In a routing table, the default route is that defined for the network 0.0.0.0 (with the mask also being 0.0.0.0). If the destination address of a packet does not match any entry in the routing table, the packet is forwarded by the routing device through the default route. If no default route exists and the destination address of the packet does not match any entry in the routing table, the routing device discards the packet and sends an Internet Control Message Protocol (ICMP) packet, informing the originating host that the destination address or network is unreachable.

By default, RIP does not advertise default routes to neighbors.

On real-world networks, you can configure RIP to advertise default routes as required in order to control routing information.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure RIP to advertise default routes.
   
   
   ```
   [default-route originate](cmdqueryname=default-route+originate) [ [ cost cost ] | [ tag tag ] | { { match default | route-policy route-policy-name [ advertise-tag ] } [ avoid-learning ] } ] *
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```