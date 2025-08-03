(Optional) Preventing BGP4+ from Adding Routes to the IP Routing Table
======================================================================

Disabling BGP4+ route delivery to the IP routing table on an RR can prevent traffic from being forwarded by the RR, improving route advertisement efficiency.

#### Context

In most cases, BGP4+ routes are added to the IP routing table on the Router for traffic forwarding. If the Router does not need to forward traffic, prevent the Router from adding BGP4+ routes to the IP routing table.

Preventing a device from adding BGP4+ routes to the IP routing table is mainly used in RR scenarios. In an AS, an RR transmits routes and forwards traffic. If an RR is connected to many clients and non-clients, route transmission will consume a lot of CPU resources of the RR and cause the RR to be unable to implement traffic forwarding. To improve route transmission efficiency, prevent the RR from adding BGP4+ routes to the IP routing table.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
   
   
   
   BGP4+ is prevented from adding routes to the IP routing table.
   
   If **route-policy** *route-policy-name* or **route-filter** *route-filter-name* is configured in the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) command, matched routes are not added to the IP routing table, and unmatched routes are added to the IP routing table, with the route attributes unchanged.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.