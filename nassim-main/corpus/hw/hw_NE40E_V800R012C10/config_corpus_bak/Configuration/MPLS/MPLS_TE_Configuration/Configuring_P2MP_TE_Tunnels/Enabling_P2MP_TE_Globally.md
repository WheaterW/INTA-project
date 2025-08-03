Enabling P2MP TE Globally
=========================

This section describes how to enable P2MP TE globally on each node before a P2MP TE tunnel is established.

#### Context

You can configure a P2MP TE tunnel only after P2MP TE is globally enabled on each node.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled.
4. Run [**mpls te p2mp-te**](cmdqueryname=mpls+te+p2mp-te)
   
   
   
   P2MP TE is globally enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.