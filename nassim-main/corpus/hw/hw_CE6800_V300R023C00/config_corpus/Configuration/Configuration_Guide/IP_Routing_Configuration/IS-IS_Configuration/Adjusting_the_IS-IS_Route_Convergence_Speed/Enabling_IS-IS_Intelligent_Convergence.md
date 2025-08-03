Enabling IS-IS Intelligent Convergence
======================================

Enabling IS-IS Intelligent Convergence

#### Context

In a fault-triggered switching scenario where the local device receives a route from a single node, IS-IS intelligent convergence can be enabled to allow IS-IS to perform fast route convergence by using the fast convergence algorithm. This improves convergence performance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Enable IS-IS intelligent convergence.
   
   
   ```
   [intelligent-convergence enable](cmdqueryname=intelligent-convergence+enable)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   In the same networking scenario, the convergence speeds of devices with the [**intelligent-convergence enable**](cmdqueryname=intelligent-convergence+enable) command configuration increase significantly, far higher than those of the devices without this command configuration. As a result, routing loops may occur. Therefore, exercise caution when you run this command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```