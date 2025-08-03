Configuring the Topology Change Notification Function
=====================================================

Configuring the Topology Change Notification Function

#### Context

If an upper-layer Layer 2 network is not notified of the topology change in an ERPS ring, MAC address entries on the upper-layer Layer 2 network are not updated. As a result, user traffic is interrupted. To ensure nonstop traffic transmission, configure the topology change notification function and specify the ERPS rings that will be notified of the topology change.

Frequent topology change notifications degrade the CPU processing capability of devices in an ERPS ring and cause the devices to frequently update Flush-FDB messages, consuming bandwidth resources. To prevent this problem, suppress topology change notification messages. You can set the topology change protection interval to suppress topology change notification messages and set the maximum number of topology change notification messages that can be processed during the topology change protection interval to prevent frequent MAC address and ARP entry deletion.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of a created ERPS ring.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
3. Configure the ERPS ring to notify other ERPS rings of its topology change.
   
   
   ```
   [tc-notify erps ring](cmdqueryname=tc-notify+erps+ring) { ring-id1 [ to ring-id2 ] } &<1-10>   
   ```
   
   The *ring-id1* [ **to** *ring-id2* ] parameter specifies the start and end IDs of the ERPS rings that will be notified of the topology change. Ensure that the rings specified by *ring-id1* and *ring-id2* exist. Otherwise, the configuration does not take effect.
   
   After devices in the ERPS rings receive topology change notification messages from an ERPS ring, they send Flush-FDB messages on their own rings to instruct other devices in the rings to delete MAC addresses and learn new MAC addresses to ensure nonstop traffic transmission.
4. (Optional) Set the topology change protection interval to suppress topology change notification messages.
   
   
   ```
   [tc-protection interval](cmdqueryname=tc-protection+interval) interval-value   
   ```
5. (Optional) Set the maximum number of topology change notification messages that devices in an ERPS ring can process within the topology change protection interval.
   
   
   ```
   [tc-protection threshold](cmdqueryname=tc-protection+threshold) threshold-value
   ```
   
   The topology change protection interval is specified using the [**tc-protection interval**](cmdqueryname=tc-protection+interval) command.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```