Configuring IPv6 IS-IS Route Summarization
==========================================

Configuring IPv6 IS-IS Route Summarization

#### Prerequisites

Before configuring IPv6 IS-IS route summarization, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

On medium- or large-sized IPv6 IS-IS networks, the IPv6 IS-IS routing table may contain many routing entries. Storing these entries consumes a large number of memory resources, and transmitting and processing the corresponding routing information consumes significant network resources. IPv6 IS-IS route summarization can resolve this problem by summarizing routes that share the same next hop, but are destined for different subnets of a network segment, into one summary route, and then advertising it to other network segments. Route summarization reduces both the routing table size and system resource consumption. In addition, if a link within one of the subnets to which specific routes belong frequently alternates between up and down, the link status changes will not be advertised to devices whose IPv6 addresses are not on the network segment of the summary route, preventing route flapping and improving network stability.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure IPv6 IS-IS route summarization.
   
   
   ```
   [ipv6 summary](cmdqueryname=ipv6+summary) ipv6-address prefix-length [ explicit ] [ avoid-feedback | generate_null0_route | tag tag-value | [ level-1 | level-2 | level-1-2 ] ] *
   ```
   
   After IPv6 route summarization is configured, the IPv6 routing table on the local IS-IS device still contains the specific routes that participate in the summarization. The IPv6 routing tables on other IS-IS devices that receive the LSPs sent by the local device contain the summary route rather than the specific routes. The summary route is only deleted after all its specific routes are deleted.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis**](cmdqueryname=display+isis) *process-id* **route ipv6** [ *ipv6-address* [ *prefix-length* ] | { **level-1** | **level-2** } | **verbose** ]\* command to check information about summary routes in the IPv6 IS-IS routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) [ **verbose** ] command to check summary routes in the IPv6 routing table.