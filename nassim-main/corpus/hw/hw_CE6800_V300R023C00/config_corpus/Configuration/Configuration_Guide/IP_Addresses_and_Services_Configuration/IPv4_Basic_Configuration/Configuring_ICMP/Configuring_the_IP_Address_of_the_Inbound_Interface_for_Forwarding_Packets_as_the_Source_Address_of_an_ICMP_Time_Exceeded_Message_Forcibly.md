Configuring the IP Address of the Inbound Interface for Forwarding Packets as the Source Address of an ICMP Time Exceeded Message Forcibly
==========================================================================================================================================

Configuring the IP Address of the Inbound Interface for Forwarding Packets as the Source Address of an ICMP Time Exceeded Message Forcibly

#### Context

Tracert is used to test the path through which a packet is sent from a host to the destination. After receiving the packet, an intermediate device sends an ICMP Time Exceeded message to the host. The host then identifies the device according to the source IP address of the ICMP Time Exceeded message. To easily observe the inbound interface of a device along the path, you can forcibly configure the IP address of the inbound interface for forwarding packets as the source address of an ICMP Time Exceeded message.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the IP address of the inbound interface for forwarding packets as the source address of an ICMP Time Exceeded message forcibly.
   
   
   ```
   [ip icmp ttl-exceeded source-address ingress-interface](cmdqueryname=ip+icmp+ttl-exceeded+source-address+ingress-interface)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```