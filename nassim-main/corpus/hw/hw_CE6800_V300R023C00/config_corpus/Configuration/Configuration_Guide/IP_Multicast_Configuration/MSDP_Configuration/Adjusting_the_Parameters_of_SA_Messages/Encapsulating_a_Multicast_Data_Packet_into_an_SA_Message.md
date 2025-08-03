Encapsulating a Multicast Data Packet into an SA Message
========================================================

Encapsulating a Multicast Data Packet into an SA Message

#### Context

Some multicast sources send multicast data at intervals longer than the holdtime of (S, G) entries. This ultimately prevents remote hosts from receiving multicast data from these multicast sources. In this case, the source DR can only encapsulate multicast data into Register messages and send them to the source RP. After the source RP is enabled to encapsulate multicast data packets into SA messages, the source RP sends multicast data packets in SA messages to the remote RP.

You can also set a TTL threshold to limit the transmission scope of multicast data packets:

* Before creating an SA message that encapsulates a multicast data packet, a device checks the TTL value in the IP header of the multicast data packet. If the value is smaller than the configured threshold, the SA message is not created. If the value is greater than or equal to the configured threshold, the device encapsulates the multicast data packet into an SA message and forwards the message.
* After receiving the SA message with the multicast data packet encapsulated, a device reduces the TTL value in the IP header of the multicast data packet by 1, and then checks the TTL value. If the value is smaller than the configured threshold, the packet is no longer forwarded to the specified MSDP peer. If the value is greater than or equal to the configured threshold, the packet is forwarded.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MSDP view.
   
   
   ```
   [msdp](cmdqueryname=msdp) [ vpn-instance vpn-instance-name ]
   ```
3. Enable the device to encapsulate multicast data packets into SA messages.
   
   
   ```
   [encap-data-enable](cmdqueryname=encap-data-enable)
   ```
   
   
   
   By default, an SA message contains (S, G) information with no multicast data packet encapsulated.
4. (Optional) Set a TTL threshold for multicast data packets.
   
   
   ```
   [peer](cmdqueryname=peer) peer-address minimum-ttl ttl
   ```
   
   The default TTL threshold of multicast data packets encapsulated in SA messages is 0.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```