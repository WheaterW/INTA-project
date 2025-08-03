Configuring the Route Calculation Delay Function to Suppress Frequent LSA Flapping
==================================================================================

A route calculation delay can suppress frequent OSPF LSA flapping.

#### Context

Frequent OSPF LSA flapping on the remote device may lead to route flapping on the local device, affecting services. To address this problem, run the [**maxage-lsa route-calculate-delay**](cmdqueryname=maxage-lsa+route-calculate-delay) command to configure the local device to delay route calculation in the case of frequent OSPF LSA flapping, which suppresses route flapping locally.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**maxage-lsa route-calculate-delay**](cmdqueryname=maxage-lsa+route-calculate-delay) *delay-interval*
   
   
   
   The route calculation delay function is configured to suppress frequent OSPF LSA flapping.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.