Configuring Flow Sampling
=========================

Flow sampling is based on data packets. An sFlow agent samples packets in a given direction on a specified interface based on a sampling rate. It then encapsulates the analysis result into sFlow packets and sends them to an sFlow collector.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**sflow enable**](cmdqueryname=sflow+enable)
   
   
   
   sFlow is enabled on the board in the slot.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
7. Run [**sflow flow-sampling collector**](cmdqueryname=sflow+flow-sampling+collector) *collector-id* [ **secondary** *secondary-collector-id* ] { **inbound** | **outbound** }
   
   
   
   Flow sampling is enabled on the interface, and an sFlow agent is configured to send flow sampling data to a specified collector.
8. Run [**sflow flow-sampling rate**](cmdqueryname=sflow+flow-sampling+rate) *rate* { **inbound** | **outbound** }
   
   
   
   A sampling rate is configured for the interface.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.