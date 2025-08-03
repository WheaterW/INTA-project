Configuring a Payload Length for ARP Messages
=============================================

Configuring a Payload Length for ARP Messages

#### Context

An Ethernet frame in which an ARP message is encapsulated in the payload is called an ARP frame. An ARP message is only 28 bytes long. Data (payload) in an Ethernet frame is at least 46 bytes long. Padding bytes (payload of an ARP message) need to be added behind the ARP message to meet the requirement for the minimum data length. If the payload lengths of ARP messages are different on two interconnected devices, ARP negotiation fails and ARP entries cannot be learned. To prevent this issue, configure the same payload length for ARP messages on both devices.

![](public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enter the VLANIF interface view.
   
   
   ```
   [interface vlanif](cmdqueryname=interface+vlanif) vlan-id
   ```
3. Configure a payload length for ARP messages.
   
   
   ```
   [arp packet payload](cmdqueryname=arp+packet+payload) payloadLen
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```