(Optional) Configuring the Short Sequence Number for Negotiation
================================================================

A sequence number in the packet header indicates the sequence of a fragmented packet. Using short sequence number for negotiation shortens the packet length and improves communication reliability.

#### Context

A sequence number in the packet header indicates the sequence of a fragmented packet. The header of an MP packet can use either a 12-bit short sequence number or a 24-bit long sequence number. To configure an MP-group interface to use the short sequence number contained in packet headers to perform negotiation, run the [**short-sequence**](cmdqueryname=short-sequence) command. Using short sequence number for negotiation shortens the packet length and improves communication reliability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface mp-group**](cmdqueryname=interface+mp-group) *number*
   
   
   
   An MP-Group interface is created, and the MP-Group interface view is displayed.
3. Run [**short-sequence**](cmdqueryname=short-sequence)
   
   
   
   The MP-group interface is configured to use the short sequence number contained in packet headers to perform negotiation.
4. Restart the MP-Group interface.
   1. Run [**shutdown**](cmdqueryname=shutdown)
      
      
      
      The interface is shut down.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   3. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
      
      
      
      The interface is restarted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**shutdown**](cmdqueryname=shutdown), [**commit**](cmdqueryname=commit), and [**undo shutdown**](cmdqueryname=undo+shutdown) commands must be run in sequence so that the preceding configuration can take effect after the interface is restarted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.