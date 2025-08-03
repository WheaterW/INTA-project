Configuring the Route Calculation Delay Function in Cases of Frequent LSA Flapping
==================================================================================

Configuring the Route Calculation Delay Function in Cases of Frequent LSA Flapping

#### Prerequisites

Before configuring the route calculation delay function in cases of frequent LSA flapping, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

Frequent OSPF LSA flapping on a remote device may lead to route flapping on the local device, which adversely affects services. To address this problem, configure the local device to delay route calculation in cases of frequent LSA flapping, as this suppresses route flapping locally.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPF view.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   ```
   
   The *process-id* parameter specifies the ID of a process, and the default value is 1.
3. Configure the device to delay route calculation in cases of frequent OSPF LSA flapping.
   
   
   ```
   [maxage-lsa route-calculate-delay](cmdqueryname=maxage-lsa+route-calculate-delay) delay-interval
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf+statistics+updated-lsa)[ *process-id* ] **statistics** **updated-lsa** command to check information about the LSAs that are frequently updated in the LSDB.