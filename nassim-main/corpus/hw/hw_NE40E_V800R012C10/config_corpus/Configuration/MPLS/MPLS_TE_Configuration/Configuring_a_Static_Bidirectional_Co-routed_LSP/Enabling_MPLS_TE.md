Enabling MPLS TE
================

Before setting up a static bidirectional co-routed LSP, you must enable MPLS TE.

#### Context

Perform the following steps on each node along the CR-LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled on the node globally.
   
   To enable MPLS TE on each interface, you must first enable MPLS TE globally in the MPLS view.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
6. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled on the interface.
7. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled on the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When the MPLS TE is disabled in the interface view, all CR-LSPs on the current interface go Down.
   
   When the MPLS TE is disabled in the MPLS view, the MPLS TE on each interface is disabled, and all CR-LSPs are deleted.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.