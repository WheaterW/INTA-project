Configuring an Edge Device to Replace the Multicast Destination MAC Address
===========================================================================

To prevent a backbone network edge device from sending the received Layer 2 protocol data units (PDUs) to its CPU for processing and ensure that the Layer 2 PDUs are tunneled across the backbone network, configure the edge device to replace the multicast destination MAC address in Layer 2 PDUs with a specified multicast MAC address.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2protocol-tunnel**](cmdqueryname=l2protocol-tunnel+group-mac) *protocol* [**group-mac**](cmdqueryname=l2protocol-tunnel+group-mac) *group-mac*
   
   
   
   The device is configured to replace the multicast destination MAC address in Layer 2 PDUs with a specified multicast MAC address.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.