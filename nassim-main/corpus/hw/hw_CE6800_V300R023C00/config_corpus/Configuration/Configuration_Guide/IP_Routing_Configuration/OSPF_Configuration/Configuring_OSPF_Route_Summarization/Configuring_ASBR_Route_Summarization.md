Configuring ASBR Route Summarization
====================================

Configuring ASBR Route Summarization

#### Prerequisites

Before configuring ASBR route summarization, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
3. Configure OSPF route summarization on the ASBR.
   
   
   ```
   [asbr-summary](cmdqueryname=asbr-summary) ip-address mask [ [ not-advertise | generate-null0-route ] | tag tag-value | cost cost-value | distribute-delay interval ] *
   ```
   
   After route summarization is configured on the ASBR, the routing table on the local OSPF device remains unchanged. The routing table on an OSPF neighbor, however, contains only one summary route and no specific route. This summary route stays in the routing table until all the summarized specific routes on the network are withdrawn.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```