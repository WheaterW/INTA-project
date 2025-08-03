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
   [multicast layer-2 invalid-packet igmp snooping](cmdqueryname=multicast+layer-2+invalid-packet+igmp+snooping) max-count max-Num
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | ****include** **multicast** **layer-2** **invalid-packet**** command to check the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the multicast device.
* Run the [**display igmp snooping invalid-packet**](cmdqueryname=display+igmp+snooping+invalid-packet) **bridge-domain** [ *bd-id* ] [ **message-type** { **leave** | **query** | **report** | **hello** } ] command to check statistics about invalid multicast protocol messages stored on the device.
* Run the [**display igmp snooping invalid-packet**](cmdqueryname=display+igmp+snooping+invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about invalid protocol messages stored on the multicast device.