Disabling OSPF LSA Aging Management
===================================

Disabling OSPF LSA Aging Management

#### Prerequisites

Before disabling OSPF LSA aging management, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

LSAs are aged out if their LS age field encounters an exception, and this may cause LSA flapping or incorrect route calculation. For example, if the aging time carried in a received LSA is 2500 seconds, the device considers the LSA to be abnormal and reduces the aging time to 500 seconds. As a result, the LSA is aged out far sooner than expected. To address this issue, the OSPF LSA aging management function is enabled by default. If the aging time in a received LSA is longer than 1800 seconds, OSPF considers the LSA to be abnormal and changes the aging time to 1700 seconds. This operation is performed for each abnormal LSA until the aging time values of all LSAs in the area are the same. As a result, routes can be calculated correctly.

If you want to disable this function, perform the following steps.


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
3. Disable OSPF LSA aging management.
   
   
   ```
   [lsa-age refresh disable](cmdqueryname=lsa-age+refresh+disable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **statistics maxage-lsa** command to check information about router LSAs that have reached the maximum aging time.