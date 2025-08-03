Configuring ARP Fast Reply
==========================

Configuring ARP Fast Reply

#### Prerequisites

Before configuring ARP fast reply, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable ARP fast reply.
   
   
   ```
   [undo arp fast-reply disable](cmdqueryname=undo+arp+fast-reply+disable)
   ```
   
   By default, ARP fast reply is enabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```