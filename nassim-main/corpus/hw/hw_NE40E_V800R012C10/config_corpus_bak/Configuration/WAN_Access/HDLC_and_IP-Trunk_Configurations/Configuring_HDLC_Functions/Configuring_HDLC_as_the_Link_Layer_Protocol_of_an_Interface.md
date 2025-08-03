Configuring HDLC as the Link Layer Protocol of an Interface
===========================================================

You can configure HDLC as a link layer protocol on an interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface
   view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Run the command [**controller**](cmdqueryname=controller)  **e3** *controller-number*, the E3 interface view is displayed.
3. Run [**link-protocol hdlc**](cmdqueryname=link-protocol+hdlc)
   
   
   
   HDLC is configured as a link layer protocol of
   the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.