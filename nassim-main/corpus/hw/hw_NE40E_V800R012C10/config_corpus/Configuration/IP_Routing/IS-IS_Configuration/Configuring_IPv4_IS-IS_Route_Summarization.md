Configuring IPv4 IS-IS Route Summarization
==========================================

To speed up IPv4 route lookup and simplify route management on a large-scale IS-IS network, configure IS-IS route summarization to reduce the number of IS-IS routes in a routing table.

#### Usage Scenario

The IS-IS routing table of a device on a medium or large IS-IS network contains a large number of routing entries. Storing the routing table consumes a large number of memory resources, and transmitting and processing routing information consume lots of network resources. IS-IS route summarization can solve this problem.

Routes with the same IPv4 prefix can be summarized into one route. Route summarization on a large-scale IS-IS network reduces the number of routes in a routing table and minimizes system resource consumption. In addition, if a specific link frequently alternates between Up and Down, the link status changes will not be advertised to devices that are located beyond the summarized route network segment, which prevents route flapping and improves network stability.


#### Pre-configuration Tasks

Before configuring IS-IS route summarization, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**summary**](cmdqueryname=summary) *ip-address* *mask* [ **avoid-feedback** | **generate\_null0\_route** | **tag** *tag-value* | [**level-1** | **level-1-2** | **level-2** ] ] \*
   
   
   
   The specified IS-IS routes are summarized into one IS-IS route.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After route summarization is configured on an IS, the local IPv4 routing table still contains all specific routes before the summarization.
   
   The IPv4 routing tables on other ISs that receive the LSP from the local IS contain only the summarized route, and the summarized route is deleted only after all its specific routes are deleted.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After configuring route summarization, perform the following steps to check whether the route summarization function has taken effect.

* Run the [**display isis route**](cmdqueryname=display+isis+route) command to check summarized routes in the IS-IS routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) [ **verbose** ] command to check summarized routes in the IP routing table.