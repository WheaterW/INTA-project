Configuring the Function to Send ARP Packets at a Constant Speed
================================================================

This section describes how to enable a device to send ARP packets at a constant rate, so that normal services of the peer device are not affected.

#### Background

By default, a device broadcasts ARP aging probe and Miss messages at varied rates. If the number of ARP packets received by the peer device exceeds its processing capability in milliseconds, packets may be lost and services may be affected. To resolve the problem, enable the device to send ARP packets at a constant rate and adjust the constant rate as required so that normal services of the peer device are not affected.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**arp constant-send enable**](cmdqueryname=arp+constant-send+enable)
   
   
   
   The function to send ARP packets at a constant rate is enabled.
3. Run [**arp constant-send maximum**](cmdqueryname=arp+constant-send+maximum) *maximum-value*
   
   
   
   The constant rate at which ARP packets are sent is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.