(Optional) Setting the Interval at Which Update Messages Are Sent
=================================================================

When routes change, the Router sends Update messages to notify its peers. If a route changes frequently, to prevent the Router from sending Update messages upon every change, you can set an interval at which Update messages are sent as required.

#### Context

Perform the following steps on a BGP4+ device:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **route-update-interval** *interval*
   
   
   
   The interval at which Update messages are sent is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.