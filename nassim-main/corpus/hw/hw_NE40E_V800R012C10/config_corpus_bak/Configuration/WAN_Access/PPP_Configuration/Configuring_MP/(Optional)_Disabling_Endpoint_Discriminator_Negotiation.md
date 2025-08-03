(Optional) Disabling Endpoint Discriminator Negotiation
=======================================================

The Link Control Protocol (LCP) status is Up only if the endpoint discriminators for the MP-Group interfaces on both ends are the same. If they are different, disable endpoint discriminator negotiation on both ends.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface mp-group**](cmdqueryname=interface+mp-group) *number*
   
   
   
   An MP-Group interface is created, and the MP-Group interface view is displayed.
3. Run [**undo discriminator**](cmdqueryname=undo+discriminator)
   
   
   
   Endpoint discriminator negotiation is disabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The endpoint discriminator negotiation configurations on both ends must be the same so that the LCP status can be Up. If the [**undo discriminator**](cmdqueryname=undo+discriminator) command is run on one end, whereas the [**discriminator**](cmdqueryname=discriminator) command on the other end, the parameters sent by the end with the [**undo discriminator**](cmdqueryname=undo+discriminator) command configured do not contain the endpoint discriminator, but this end accepts the endpoint discriminator of the other end. As a result, the MP link fails to be established.
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