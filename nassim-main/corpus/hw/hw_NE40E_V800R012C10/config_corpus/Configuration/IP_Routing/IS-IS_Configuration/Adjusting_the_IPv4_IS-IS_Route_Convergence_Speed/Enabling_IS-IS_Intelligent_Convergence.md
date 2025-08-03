Enabling IS-IS Intelligent Convergence
======================================

Enabling IS-IS intelligent convergence can speed up IS-IS route convergence, thereby improving convergence performance.

#### Context

In a fault-triggered switching scenario where the local device receives a route from a single node, IS-IS intelligent convergence can be enabled to allow IS-IS to perform fast route convergence by using the fast convergence algorithm. This improves convergence performance.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**intelligent-convergence enable**](cmdqueryname=intelligent-convergence+enable)
   
   
   
   IS-IS intelligent convergence is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the same networking scenario, the convergence speeds of devices with the [**intelligent-convergence enable**](cmdqueryname=intelligent-convergence+enable) command configuration increase significantly, far higher than those of the devices without this command configuration. As a result, routing loops may occur. Therefore, exercise caution when you run this command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.