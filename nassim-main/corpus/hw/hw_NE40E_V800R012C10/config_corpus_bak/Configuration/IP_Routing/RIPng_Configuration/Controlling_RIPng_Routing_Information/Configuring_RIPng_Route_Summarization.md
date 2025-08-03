Configuring RIPng Route Summarization
=====================================

Configuring RIPng route summarization reduces the routing table size and prevents route flapping.

#### Context

The RIPng routing table of a device on a medium or large RIPng network contains a large number of routes. Storing the routes consumes a large number of memory resources, and transmitting and processing these routes consume lots of network resources. To address this issue, configure RIPng route summarization.

With RIPng route summarization, a device summarizes routes destined for different subnets of a network segment into one route destined for one network segment and then advertises the summary route to other network segments. RIPng route summarization reduces the number of routes in a routing table and minimizes system resource consumption. In addition, if a specific link frequently alternates between Up and Down, the link status changes will not be advertised to devices that are located beyond the summarized route network segment, which prevents route flapping and improves network stability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ripng summary-address**](cmdqueryname=ripng+summary-address) *ipv6-address* *prefix-length* [ **avoid-feedback** ]
   
   
   
   RIPng route summarization is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After RIPng route summarization is configured on a device, the local routing table still contains all specific routes before the summarization, while the routing tables of neighbors of the local device contain only the summarized route.
   
   The cost of the summarized route is the smallest cost of the routes that have been summarized.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.