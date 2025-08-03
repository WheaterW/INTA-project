Configuring a Stub Router
=========================

To ensure that a route is not interrupted during flapping-triggering maintenance operations such as upgrade, you can configure a Router as a stub router to allow traffic to bypass the route on the stub router.

#### Context

After a stub router is configured, the route on the stub router will not be preferentially selected. After the route cost is set to the maximum value 65535, traffic generally bypasses the Router. This ensures an uninterrupted route on the Router during maintenance operations such as upgrade.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**stub-router**](cmdqueryname=stub-router) [ [ **on-startup** [ *interval* ] ] | [ **include-stub** ] | [ **external-lsa** [ *externallsa-metric* ] ] | [ **summary-lsa** [ *summarylsa-metric* ] ] ] \*
   
   
   
   A stub router is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The stub router configured in this manner is irrelevant to the Router in the stub area.
4. (Optional) Run [**maximum-link-cost**](cmdqueryname=maximum-link-cost) *cost*
   
   
   
   The maximum cost of OSPF is set.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.