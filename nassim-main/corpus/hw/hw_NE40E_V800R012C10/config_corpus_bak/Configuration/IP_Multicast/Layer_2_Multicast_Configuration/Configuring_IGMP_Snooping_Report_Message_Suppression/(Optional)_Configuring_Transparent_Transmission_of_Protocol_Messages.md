(Optional) Configuring Transparent Transmission of Protocol Messages
====================================================================

(Optional)_Configuring_Transparent_Transmission_of_Protocol_Messages

#### Context

In dual-homing networking, IGMP snooping Report message suppression is enabled on dual-homing devices. The dual-homing devices learn the same multicast forwarding entries and forward IGMP Report messages to each other through router ports. If the downstream device leaves a multicast group, the corresponding multicast entry is not deleted because the router ports still maintain the Join state. As a result, multicast protocol messages and data packets are forwarded meaninglessly on the network.

To solve this problem, you can configure transparent transmission of protocol messages so that the device can transparently transmit the protocol messages received from a router port to other router ports on the device. This does not occupy too many multicast entries. When the downstream device leaves, the corresponding entry is deleted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**igmp-snooping report-suppress**](cmdqueryname=igmp-snooping+report-suppress)
   
   
   
   IGMP snooping Report message suppression is enabled.
4. Run [**igmp-snooping router-protocol-pass**](cmdqueryname=igmp-snooping+router-protocol-pass)
   
   
   
   Transparent transmission of protocol messages is enabled on the Layer 2 multicast device.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.