Enabling MPLS TE
================

Before you set up a static CR-LSP, enable MPLS TE.

#### Context

Perform the following steps on each node along a static CR-LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled on the node globally.
   
   Before you enable MPLS TE on each interface, enable MPLS TE globally in the MPLS view.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
6. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled on the interface.
7. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled on the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After MPLS TE is disabled in the interface view, all CR-LSPs on the interface go down.
   
   After MPLS TE is disabled in the MPLS view, MPLS TE is disabled on all interfaces, and all CR-LSPs are deleted.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.