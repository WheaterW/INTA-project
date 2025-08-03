Configuring Topology Change Notification
========================================

The topology change notification function configured on the interconnection nodes of intersecting ERPS rings allows one ERPS ring to notify the other ERPS rings of its topology change. Then all devices on the other ERPS rings clear their MAC and ARP entries and relearn MAC addresses from the ring with a topology change. This function ensures that user traffic is not interrupted.

#### Context

If an upper-layer Layer 2 network is not notified of the topology change in an ERPS ring, the MAC address entries remain unchanged on the upper-layer network and therefore user traffic is interrupted. To ensure traffic transmission, you can configure the topology change notification function and specify the ERPS rings that will be notified of the topology change.

However, if an ERPS ring frequently receives topology change notification messages, its nodes will have lower CPU processing capability and repeatedly update Flush-FDB packets, consuming significant bandwidth. To resolve this problem, suppress the transmission of topology change notification messages. You can set the topology change protection interval at which topology change notification messages are sent to suppress the number of transmissions, and set the maximum number of topology change notification messages that can be processed during the topology change protection interval to prevent frequent MAC and ARP updates.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**erps ring**](cmdqueryname=erps+ring) *ring-id*
   
   
   
   The ERPS ring view is displayed.
3. Run [**tc-notify erps ring**](cmdqueryname=tc-notify+erps+ring) { *ring-id1* [ **to** *ring-id2* ] } &<1-10>
   
   
   
   The ERPS ring is configured to notify other ERPS rings of its topology change.
   
   
   
   *ring-id1* [ **to** *ring-id2* ] specifies the start and end ring IDs of the ERPS rings that will be notified of the topology change. Ensure that the ERPS rings specified by *ring-id1* and *ring-id2* exist. If the specified rings do not exist, the topology change notification function does not take effect.
   
   After the ERPS rings receive the topology change notification from an ERPS ring, they send Flush-FDB messages on their separate rings to instruct their devices to update MAC addresses so that user traffic is not interrupted.
4. (Optional) Run [**tc-protection interval**](cmdqueryname=tc-protection+interval) *interval-value*
   
   
   
   The topology change protection interval at which TC packets are sent is set for the ERPS ring.
5. (Optional) Run [**tc-protection threshold**](cmdqueryname=tc-protection+threshold) *threshold-value*
   
   
   
   The maximum number of TC packets that the ERPS ring can process within the topology change protection interval is set.
   
   
   
   The topology change protection interval is the one specified using the [**tc-protection interval**](cmdqueryname=tc-protection+interval) command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.