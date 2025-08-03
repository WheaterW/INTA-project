Configuring a Route Calculation Delay to Suppress Frequent LSA Flapping
=======================================================================

Configuring a Route Calculation Delay to Suppress Frequent LSA Flapping

#### Context

Frequent OSPFv3 LSA flapping may lead to route flapping, adversely affecting services. To address this problem, run the [**maxage-lsa route-calculate-delay**](cmdqueryname=maxage-lsa+route-calculate-delay) command to configure the device to delay route calculation when it receives a MaxAge Router LSA, which suppresses the frequent OSPFv3 LSA flapping that may occur.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**maxage-lsa route-calculate-delay**](cmdqueryname=maxage-lsa+route-calculate-delay) *delay-interval*
   
   
   
   A route calculation delay is configured and will be triggered when the device receives a MaxAge Router LSA.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.