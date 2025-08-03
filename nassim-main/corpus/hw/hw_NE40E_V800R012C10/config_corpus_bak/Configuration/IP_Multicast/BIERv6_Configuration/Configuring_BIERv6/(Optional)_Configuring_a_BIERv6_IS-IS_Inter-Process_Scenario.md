(Optional) Configuring a BIERv6 IS-IS Inter-Process Scenario
============================================================

When a BIERv6 network is deployed across IS-IS areas, you need to configure IS-IS processes on area border routers (ABRs) to import external routes to implement BIER forwarding.

#### Context

As shown in [Figure 1](#EN-US_TASK_0000001266231616__fig18735195812346), AGGs reside at borders of different IS-IS areas. To enable devices in different IS-IS areas to receive multicast traffic from other IS-IS areas, the AGGs need to generate BIERv6 forwarding entries destined for devices in different IS-IS areas. To meet this need, you need to configure different IS-IS processes on the AGGs to import IPv6 routes from each other.

**Figure 1** BIERv6 IS-IS inter-process scenario  
![](figure/en-us_image_0000001266391476.png "Click to enlarge")
![](../../../../public_sys-resources/note_3.0-en-us.png) 

Currently, to learn routes, BIERv6 can be bound only to IS-IS (not to OSPF), and the BIERv6 inter-process scenario applies only to IS-IS processes. Therefore, IS-IS processes must have been created when you deploy the BIERv6 inter-process scenario to use BIERv6 to carry routes.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Configure an IS-IS process to import IPv6 routes from another IS-IS process.
   
   
   * To import IPv6 routes without BIER attributes from another process, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) **isis** [ *process-id* ] **no-bier** command.
   * To import IPv6 routes with BIER attributes from another process, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) **isis** [ *process-id* ] command.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the IS-IS view.
5. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The view of another IS-IS process is displayed. The *process-id* of this process must be different from the process ID in Step 2.
6. Configure an IS-IS process to import IPv6 routes from another IS-IS process.
   
   
   * To import IPv6 routes without BIER attributes from another process, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) **isis** [ *process-id* ] **no-bier** command.
   * To import IPv6 routes with BIER attributes from another process, run the [**ipv6 import-route**](cmdqueryname=ipv6+import-route) **isis** [ *process-id* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If two ABRs are used for access by access-side processes, the IS-IS import configurations on the two ABRs must be the same. If one ABR imports routes with BIER attributes whereas the other ABR imports routes without BIER attributes, the two ABRs advertise routes of the same prefix, and the optimal route selected by another device is the one received from the latter ABR, BIER forwarding entries cannot be calculated due to the loop prevention mechanism for BIER route calculation.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the IS-IS view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. (Optional) Repeat the steps from [1](#EN-US_TASK_0000001266231616__step127334244280) to [8](#EN-US_TASK_0000001266231616__step56492106710) for the other IS-IS processes or ABRs that need the function.