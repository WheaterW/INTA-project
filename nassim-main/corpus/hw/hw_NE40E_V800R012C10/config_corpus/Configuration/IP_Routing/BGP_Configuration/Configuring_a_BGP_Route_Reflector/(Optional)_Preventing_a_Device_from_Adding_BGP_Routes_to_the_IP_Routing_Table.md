(Optional) Preventing a Device from Adding BGP Routes to the IP Routing Table
=============================================================================

After you prevent an RR from adding BGP routes to the IP routing table, the RR no longer forwards traffic, which improves route advertisement efficiency.

#### Context

In most cases, BGP routes are added to the IP routing table of the Router for traffic forwarding. If the Router does not need to forward traffic, prevent it from adding BGP routes to the IP routing table.

RRs need to be prevented from adding BGP routes to the IP routing table. An RR not only transmits routes but also forwards traffic. If the RR is connected to many clients and non-clients, the route transmission task will consume a lot of CPU resources of the RR, and as a result, the RR cannot forward traffic. To improve the route transmission efficiency, prevent the RR from adding BGP routes to the IP routing table so that the RR only transmits routes.

Perform the following steps on the Router that runs BGP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
   
   
   
   The device is prevented from adding BGP routes to the IP routing table.
   
   
   
   If **route-policy** *route-policy-name* or **route-filter** *route-filter-name* is configured in the [**routing-table rib-only**](cmdqueryname=routing-table+rib-only+route-policy) command, matched routes are not added to the IP routing table, and unmatched routes are added to the IP routing table, with the route attributes unchanged.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**routing-table rib-only**](cmdqueryname=routing-table+rib-only) and [**active-route-advertise**](cmdqueryname=active-route-advertise) commands are mutually exclusive.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.