Enabling IPv6 IS-IS Intelligent Convergence
===========================================

Enabling IPv6 IS-IS Intelligent Convergence

#### Context

In a fault-triggered switching scenario where the local device receives a route from a single node, IPv6 IS-IS intelligent convergence can be enabled to allow IS-IS to perform fast route convergence by using the fast convergence algorithm. This improves convergence performance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Enable IPv6 for the IS-IS process.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable) [ topology { compatible [ enable-mt-spf ] | ipv6 | standard } ]
   ```
   
   By default, IPv6 is not enabled for an IS-IS process.
4. Enable IPv6 IS-IS intelligent convergence.
   
   
   ```
   [ipv6 intelligent-convergence enable](cmdqueryname=ipv6+intelligent-convergence+enable)
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   In the same networking scenario, the convergence speeds of devices with the [**ipv6 intelligent-convergence enable**](cmdqueryname=ipv6+intelligent-convergence+enable) command configuration increase significantly, far higher than those of the devices without this command configuration. As a result, routing loops may occur. Therefore, exercise caution when running this command.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```