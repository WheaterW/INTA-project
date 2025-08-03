Configuring a Rate for Sending ARP Broadcast Packets
====================================================

You can configure a proper rate for sending ARP broadcast packets to reduce CPU usage.

#### Context

ARP broadcast packets from a sub-interface are replicated to all VLANs. If the number of VLANs is 100 and the number of ARP broadcast packets sent per second is 50, the number of ARP broadcast packets replicated is 5000 (100 x 50). This may cause the peer device to be overloaded with ARP packets. As a result, the downstream device becomes abnormal. When replicating a large number of ARP broadcast packets, the local device may fail to send ARP packets promptly, causing ARP learning failures. In this case, you can configure a proper rate for sending ARP broadcast packets to reduce CPU usage.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a rate for sending ARP broadcast packets in the system or interface view.
   
   
   * To configure a rate for sending ARP broadcast packets in the system view, run the [**arp broadcast-send maximum**](cmdqueryname=arp+broadcast-send+maximum) *maximum-value* command.
   * To configure a rate for sending ARP broadcast packets in the interface view, perform the following steps:
     1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
     2. Run the [**arp broadcast-send maximum**](cmdqueryname=arp+broadcast-send+maximum) *maximum-value* command to configure a rate for sending ARP broadcast packets.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In actual situations, after a rate for sending ARP broadcast packets is configured on a device, the total number of ARP broadcast packets sent by the device is related to board performance.
   * If a rate for sending ARP broadcast packets is configured in both the system and interface views, the smaller value between the two rates is used.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.