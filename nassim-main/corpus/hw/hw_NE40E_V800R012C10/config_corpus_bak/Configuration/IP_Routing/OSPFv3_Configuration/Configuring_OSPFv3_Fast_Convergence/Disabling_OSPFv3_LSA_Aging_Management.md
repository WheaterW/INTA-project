Disabling OSPFv3 LSA Aging Management
=====================================

By default, the OSPFv3 LSA aging management function is enabled. To disable this function, perform this task.

#### Context

LSAs are aged out if their LS age field encounters an exception, and this may cause LSA flapping or incorrect route calculation. For example, if the aging time carried in a received LSA is 2500 seconds, the device considers the LSA abnormal and reduces the aging time to 500 seconds. As a result, the LSA is aged out far sooner than expected. To address this issue, the OSPFv3 LSA aging management function is enabled by default. If the aging time in a received LSA is longer than 1800 seconds, OSPFv3 considers the LSA abnormal and changes the aging time to 1700 seconds. This operation is performed for each abnormal LSA until the aging time values of all LSAs in the area are the same. This ensures that routes can be calculated correctly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**lsa-age refresh disable**](cmdqueryname=lsa-age+refresh+disable)
   
   
   
   OSPFv3 LSA aging management is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.