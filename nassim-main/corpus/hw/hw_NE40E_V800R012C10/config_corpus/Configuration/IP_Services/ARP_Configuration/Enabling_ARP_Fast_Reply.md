Enabling ARP Fast Reply
=======================

Enabling ARP Fast Reply

#### Context

If a device receives and processes a large number of ARP request messages, it may be unable to reply quickly or may even fail to reply. In this case, the device ages out the ARP entries, resulting in packet loss or service interruption. ARP fast reply can effectively reduce the load placed on the device in processing ARP messages. In ARP fast reply, an ARP request message destined to the IP address of a local device that has learned the corresponding ARP entry is not sent to the CPU's upper-layer module for processing. Instead, the lower-layer module directly replies with an ARP reply message. This speeds up ARP response and ensures service continuity.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**undo arp fast-reply disable**](cmdqueryname=undo+arp+fast-reply+disable)
   
   
   
   ARP fast reply is enabled.