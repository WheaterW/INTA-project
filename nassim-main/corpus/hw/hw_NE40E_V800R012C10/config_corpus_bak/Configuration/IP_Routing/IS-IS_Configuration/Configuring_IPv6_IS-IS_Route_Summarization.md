Configuring IPv6 IS-IS Route Summarization
==========================================

On a medium-or large-scale IS-IS network, a large number of IS-IS IPv6 routing entries may exist. Configuring route summarization helps reduce the IPv6 routing table size, which in turn speeds up route lookup.

#### Usage Scenario

The IS-IS routing table of a device on a medium or large IS-IS network contains a large number of routing entries. Storing the routing table consumes a large number of memory resources, and transmitting and processing routing information consume lots of network resources. IS-IS route summarization can solve this problem.

Routes with the same IPv6 prefix can be summarized into one route. This greatly reduces the number of routing entries and minimizes system resource consumption. In addition, if a specific link frequently alternates between up and down, the link state changes will not be advertised to devices that are located beyond the summary route network segment, preventing route flapping and improving network stability.


#### Pre-configuration Tasks

Before configuring IPv6 IS-IS route summarization, complete the following tasks:

* Configure IPv6 addresses for interfaces to ensure that neighboring devices are reachable at the network layer.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**ipv6 summary**](cmdqueryname=ipv6+summary) *ipv6-address* *prefix-length* [ **explicit** ] [ **avoid-feedback** | **generate\_null0\_route** | **tag** *tag-value* | **learning-avoid-loop** | [ **level-1** | **level-1-2** | **level-2** ] ] \*
   
   
   
   IS-IS is configured to generate an IPv6 summary route.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After IPv6 route summarization is configured, the IPv6 routing table on the local IS-IS device still contains the specific routes that participate in the summarization.
   * The IPv6 routing tables on other IS-IS devices that receive the LSPs sent by the local device contain the summary route rather than the specific routes.
   * If both **generate\_null0\_route** and **learning-avoid-loop** are specified and the device learns a route with the same prefix from another device and generates a loop-free path, the device preferentially selects the learned route. Otherwise, a blackhole route is generated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display isis route**](cmdqueryname=display+isis+route) command to check summary routes in the IS-IS routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) [ **verbose** ] command to check summary routes in the IPv6 routing table.