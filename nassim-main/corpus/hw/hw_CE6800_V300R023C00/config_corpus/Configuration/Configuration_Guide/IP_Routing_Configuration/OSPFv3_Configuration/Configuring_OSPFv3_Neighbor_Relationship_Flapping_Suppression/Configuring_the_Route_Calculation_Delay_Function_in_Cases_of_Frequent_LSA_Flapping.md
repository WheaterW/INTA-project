Configuring the Route Calculation Delay Function in Cases of Frequent LSA Flapping
==================================================================================

Configuring the Route Calculation Delay Function in Cases of Frequent LSA Flapping

#### Prerequisites

Before configuring the route calculation delay function in cases of frequent LSA flapping, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

Frequent OSPFv3 LSA flapping on a remote device may lead to route flapping on the local device, adversely affecting services. To locally suppress route flapping, configure the local device to delay route calculation when it receives router-LSAs that have reached the maximum aging time.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Configure the device to delay route calculation when it receives router-LSAs that have reached the maximum aging time.
   
   
   ```
   [maxage-lsa route-calculate-delay](cmdqueryname=maxage-lsa+route-calculate-delay) delay-interval
   ```
   
   By default, the delay is 10s.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3+statistics+updated-lsa) [ *process-id* ] **statistics updated-lsa** command to check the LSAs that are frequently updated in the local LSDB.