Setting the Maximum Number of Invalid Layer 2 Multicast Protocol Messages That Can Be Stored
============================================================================================

Setting the Maximum Number of Invalid Layer 2 Multicast Protocol Messages That Can Be Stored

#### Context

If forwarding entries cannot be created on a multicast network, you can set the maximum number of invalid Layer 2 multicast protocol messages that can be stored on a device. This facilitates troubleshooting, as it enables you to locate and rectify faults based on the statistics and detailed information about invalid Layer 2 multicast protocol messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the device.
   
   
   ```
   [multicast layer-2 invalid-packet](cmdqueryname=multicast+layer-2+invalid-packet) mld snooping max-count max-number
   ```
   
   By default, a maximum of 10 invalid Layer 2 multicast protocol messages can be stored.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```