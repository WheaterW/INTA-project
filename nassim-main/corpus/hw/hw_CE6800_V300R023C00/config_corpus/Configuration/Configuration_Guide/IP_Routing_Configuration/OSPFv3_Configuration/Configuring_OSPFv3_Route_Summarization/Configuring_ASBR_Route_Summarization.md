Configuring ASBR Route Summarization
====================================

Configuring ASBR Route Summarization

#### Prerequisites

Before configuring ASBR route summarization, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure the ASBR to summarize routes imported by OSPFv3.
   
   
   ```
   [asbr-summary](cmdqueryname=asbr-summary) ipv6-address prefix-length [ not-advertise | [ tag tag-value ] | [ cost cost-value ] | [ distribute-delay interval ] ] *
   ```
   
   In the preceding command:
   
   
   
   * The **not-advertise** parameter prevents the summary route with the specified IPv6 prefix length from being advertised.
   * The **tag** *tag-value* parameter specifies a tag value used to control summary route advertisement.
   * The **cost** *cost-value* parameter specifies a cost for the summary route. By default, the highest cost among the specific routes for summarization is used as the cost of the summary route.
   * The **distribute-delay** *interval* parameter specifies a delay for advertising summary routes. This ensures that a summary route advertised each time carries information about more valid routes.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```