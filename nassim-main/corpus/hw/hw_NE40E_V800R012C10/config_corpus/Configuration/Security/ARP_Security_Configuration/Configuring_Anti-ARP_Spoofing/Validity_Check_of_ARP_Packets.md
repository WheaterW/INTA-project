Validity Check of ARP Packets
=============================

After validity check of Address Resolution Protocol (ARP)
packets is enabled, when receiving an ARP packet, the device checks
whether the source and destination MAC addresses in the Ethernet header
match those in the Data field of the packet.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**arp validate**](cmdqueryname=arp+validate) { **destination-mac** **source-mac** | **source-mac** **destination-mac** }
   
   
   
   Validity check of ARP packets is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.