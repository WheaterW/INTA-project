Configuring the Payload Length of ARP Packets to Be Sent
========================================================

Configuring_the_Payload_Length_of_ARP_Packets_to_Be_Sent

#### Context

If the payload lengths of ARP packets are different on two interconnected devices, ARP negotiation fails and ARP entries cannot be learned. To prevent this issue, you can configure the same payload length for ARP packets to be sent on the interconnected devices.


#### Procedure

* In the system view, configure the payload length of ARP packets to be sent.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**arp packet payload**](cmdqueryname=arp+packet+payload) *payloadLen* command to configure the payload length of ARP packets to be sent.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* In the interface view, configure the payload length of ARP packets to be sent.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the view of the interface where the payload length of ARP packets to be sent needs to be configured.
  3. Run the [**arp packet payload**](cmdqueryname=arp+packet+payload) *payloadLen* command to configure the payload length of ARP packets to be sent.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.