(Optional) Configuring Zero Field Check for RIP-1 Messages
==========================================================

(Optional) Configuring Zero Field Check for RIP-1 Messages

#### Context

Unlike RIP-2 messages, RIP-1 messages contain fields that must be 0. These fields are also known as zero fields. By default, RIP-1 checks the zero fields of received messages and discards those messages in which any of the zero fields is not 0.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure zero field check for RIP-1 messages.
   
   
   ```
   [checkzero](cmdqueryname=checkzero)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```