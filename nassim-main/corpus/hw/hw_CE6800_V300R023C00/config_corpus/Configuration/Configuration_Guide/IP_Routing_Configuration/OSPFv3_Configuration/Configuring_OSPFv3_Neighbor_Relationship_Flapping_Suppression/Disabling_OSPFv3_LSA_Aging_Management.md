Disabling OSPFv3 LSA Aging Management
=====================================

Disabling OSPFv3 LSA Aging Management

#### Prerequisites

Before disabling OSPFv3 LSA aging management, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

LSAs are aged out if an exception occurs in their LS age field, potentially resulting in LSA flapping or incorrect route calculation. For example, if the aging time carried in a received LSA is 2500 seconds, the device considers the LSA to be abnormal and reduces the aging time to 500 seconds. As a result, the LSA is aged out sooner than expected. To address this issue, the OSPFv3 LSA aging management function is enabled by default. If the aging time in a received LSA is longer than 1800 seconds, OSPFv3 considers the LSA to be abnormal and changes the aging time to 1700 seconds. This operation is performed for each abnormal LSA until the aging time values of all LSAs in the area are the same. As a result, routes can be calculated correctly.

To disable this function, perform the following steps.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   ```
3. Disable OSPFv3 LSA aging management.
   
   
   ```
   [lsa-age refresh disable](cmdqueryname=lsa-age+refresh+disable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **statistics maxage-lsa** command to check information about router-LSAs that have reached the maximum aging time.