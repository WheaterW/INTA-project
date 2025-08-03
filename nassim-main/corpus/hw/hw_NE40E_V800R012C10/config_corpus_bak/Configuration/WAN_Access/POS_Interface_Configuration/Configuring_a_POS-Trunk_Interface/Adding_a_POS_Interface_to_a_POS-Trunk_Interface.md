Adding a POS Interface to a POS-Trunk Interface
===============================================

After creating a POS-Trunk interface, add a POS interface to the POS-Trunk interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface pos**](cmdqueryname=interface+pos) *interface-number*
   
   
   
   The view of the POS interface to be added to a POS-Trunk interface is displayed.
3. Run [**link-protocol ppp**](cmdqueryname=link-protocol+ppp)
   
   
   
   The link layer protocol of the POS interface is configured as PPP.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The link layer protocol of POS interfaces added to a POS-Trunk interface must be configured as PPP.
4. Run [**pos-trunk**](cmdqueryname=pos-trunk) *trunk-id*
   
   
   
   The POS interface is added to a POS-Trunk interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before adding a POS interface to a POS-Trunk interface, run the [**aps group**](cmdqueryname=aps+group) command on the POS interface to add it to an LMSP group, and configure the interface as a working interface or a protection interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.