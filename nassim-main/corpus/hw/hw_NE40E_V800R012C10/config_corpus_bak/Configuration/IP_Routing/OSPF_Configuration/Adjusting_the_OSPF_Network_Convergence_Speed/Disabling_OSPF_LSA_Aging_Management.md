Disabling OSPF LSA Aging Management
===================================

By default, the OSPF LSA aging management function is enabled. To disable this function, perform this task.

#### Context

LSAs are aged out if their LS age field encounters an exception, and this may cause LSA flapping or incorrect route calculation. For example, the actual LSA aging time of a device is 500 seconds and the device receives an LSA with the aging time of 2500 seconds, the LSA is aged too early because LSAs automatically age in 3600 seconds according to the protocol mechanism. To address this issue, the OSPF LSA aging management function is enabled by default. If the aging time in a received LSA is longer than 1800 seconds, OSPF considers the LSA abnormal and changes the aging time to 1700 seconds. This operation is performed for each abnormal LSA until the aging time values of all LSAs in the area are the same. This ensures that routes can be calculated correctly.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**lsa-age refresh disable**](cmdqueryname=lsa-age+refresh+disable)
   
   
   
   OSPF LSA aging management is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.