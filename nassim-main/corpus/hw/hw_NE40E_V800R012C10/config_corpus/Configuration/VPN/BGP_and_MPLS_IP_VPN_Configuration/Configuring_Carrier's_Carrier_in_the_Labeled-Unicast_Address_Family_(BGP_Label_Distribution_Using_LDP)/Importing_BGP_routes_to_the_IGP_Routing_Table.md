Importing BGP routes to the IGP Routing Table
=============================================

To enable LDP to allocate labels for BGP, you need first import BGP routes to the relevant IGP routing table.

#### Context

Import BGP routes to the IGP routing table. IS-IS is used as an example. Perform the following steps on the Level 1 carrier CE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**import-rib public labeled-unicast**](cmdqueryname=import-rib+public+labeled-unicast)
   
   
   
   Labeled routes are imported to the routing table of the public network unicast address family.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the upper-level view.
5. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
6. Run [**import-route**](cmdqueryname=import-route) **bgp** [ **cost** *cost* ] [ **route-policy** *route-policy-name* ]
   
   
   
   BGP routes are imported to the IGP routing table.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.