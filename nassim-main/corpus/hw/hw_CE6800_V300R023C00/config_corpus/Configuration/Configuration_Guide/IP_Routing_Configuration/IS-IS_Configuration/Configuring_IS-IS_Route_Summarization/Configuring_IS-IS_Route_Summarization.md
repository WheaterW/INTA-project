Configuring IS-IS Route Summarization
=====================================

Configuring IS-IS Route Summarization

#### Prerequisites

Before configuring IS-IS route summarization, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).

#### Context

On medium- or large-sized IS-IS networks, the IS-IS routing table may contain many routing entries. Storing these entries consumes a large number of memory resources, and transmitting and processing the corresponding routing information consumes significant network resources. IS-IS route summarization can resolve this problem by summarizing routes that share the same next hop, but are destined for different subnets of a network segment, into one summary route, and then advertising it to other network segments. Route summarization reduces both the routing table size and system resource consumption. In addition, if a link within one of the subnets to which specific routes belong frequently alternates between up and down, the link status changes will not be advertised to devices whose IP addresses are not on the network segment of the summary route, preventing route flapping and improving network stability.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Configure IS-IS route summarization.
   
   
   ```
   [summary](cmdqueryname=summary) ip-address mask [ avoid-feedback | generate_null0_route | tag tag-value | cost cost-value | [ level-1 | level-2 | level-1-2 ] ] *
   ```
   
   After IPv4 IS-IS route summarization is configured on a device, the local IPv4 routing table still contains all specific routes that are summarized.
   
   The IPv4 routing tables on neighbors that receive LSPs from the local IS-IS device contain the summary route rather than the specific routes. The summary route is only deleted after all its specific routes are deleted.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis route**](cmdqueryname=display+isis+route) [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \* command to check summary routes in the IPv4 IS-IS routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) [ **verbose** ] command to check summary routes in the IPv4 routing table.