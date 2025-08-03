Filtering ARP Packets
=====================

This section describes how to filter out ARP packets, including invalid ARP packets, gratuitous ARP packets, and ARP packets with non-null destination MAC addresses.

#### Context

Perform the following on the Router to filter out ARP packets on its interfaces:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [*sub-interface-number*]
   
   
   
   The interface view is displayed.
3. Run [**arp filter**](cmdqueryname=arp+filter) { **gratuitous** | **mac-illegal** | **tha-filled-request** }
   
   The interface is configured to filter out invalid ARP packets.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can decide which types of ARP packets are to be filtered out according to actual situations. The NE40E can filter out the following ARP packets:
   
   * Invalid ARP packets
   * Gratuitous ARP packets
   * ARP packets whose destination MAC addresses are not null
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.