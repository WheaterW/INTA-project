Configuring ABR Route Summarization
===================================

Configuring ABR Route Summarization

#### Prerequisites

Before configuring ABR route summarization, you have completed the following task:

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
3. Enter the OSPFv3 area view.
   
   
   ```
   [area](cmdqueryname=area+%28OSPFv3+view%29) area-id
   ```
4. Configure the ABR to summarize intra-area OSPFv3 routes.
   
   
   ```
   [abr-summary](cmdqueryname=abr-summary) ipv6-address prefix-length [ not-advertise | cost cost-value ] *
   ```
   
   
   
   In the preceding command:
   
   * The **not-advertise** parameter indicates that the routes in this network segment are not advertised.
   * The **cost** *cost-value* parameter specifies a cost for the summary route. By default, the highest cost among the specific routes for summarization is used as the cost of the summary route.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```