Configuring Source Address Check for RIP Messages in a Broadcast Domain
=======================================================================

Configuring Source Address Check for RIP Messages in a Broadcast Domain

#### Context

By default, RIP interfaces check the source address in received messages to improve network security. If the source address is from a network segment different from the local interface IP address, the local interface discards the RIP message.

As such, the local RIP interface only receives the packets from the network where the source address resides.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure source address check for RIP messages on a broadcast network.
   
   
   ```
   [verify-source](cmdqueryname=verify-source)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```