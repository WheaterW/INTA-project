Configuring Forced IPv4 Packet Fragmentation
============================================

Configuring forced IPv4 packet fragmentation prevents long packets from being discarded in specific scenarios.

#### Usage Scenario

By default, forced IPv4 packet fragmentation is disabled. If the length of an IPv4 packet received by an interface is greater than the MTU of the interface and the Don't Fragment (DF) flag in the IPv4 packet is set to 1, indicating no fragmentation, the NE40E discards this packet and sends an ICMP packet to its upstream device. If you want the NE40E to fragment the packet before sending it, enable forced IPv4 packet fragmentation on the NE40E.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**ipv4 force-fragment enable**](cmdqueryname=ipv4+force-fragment+enable)
   
   
   
   Forced fragmentation is enabled for IPv4 packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.