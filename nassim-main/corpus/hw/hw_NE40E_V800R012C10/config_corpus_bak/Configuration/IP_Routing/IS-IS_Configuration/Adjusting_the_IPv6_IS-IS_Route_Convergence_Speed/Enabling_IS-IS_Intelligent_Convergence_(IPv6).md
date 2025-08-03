Enabling IS-IS Intelligent Convergence (IPv6)
=============================================

Enabling IS-IS IPv6 intelligent convergence can speed up IS-IS route convergence, thereby improving convergence performance.

#### Context

In a fault-triggered switching scenario where the local device receives a route from a single node, IS-IS intelligent convergence can be enabled to allow IS-IS to perform fast route convergence by using the fast convergence algorithm. This improves convergence performance.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**isis**](cmdqueryname=isis) [ *process-id* ] command to enter the IS-IS view.
3. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) [ **topology** { **compatible** [ **enable-mt-spf** ] | **ipv6** | **standard** } ] command to enable IPv6 for the IS-IS process.
4. Run the [**ipv6 intelligent-convergence enable**](cmdqueryname=ipv6+intelligent-convergence+enable) command to configure IS-IS IPv6 intelligent convergence.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In the same networking scenario, the convergence speeds of devices with the [**ipv6 intelligent-convergence enable**](cmdqueryname=ipv6+intelligent-convergence+enable) command configuration increase significantly, far higher than those of the devices without this command configuration. As a result, routing loops may occur. Therefore, exercise caution when running this command.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.