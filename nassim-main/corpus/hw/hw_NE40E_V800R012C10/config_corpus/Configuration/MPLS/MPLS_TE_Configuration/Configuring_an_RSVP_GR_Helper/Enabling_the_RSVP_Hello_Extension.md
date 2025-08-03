Enabling the RSVP Hello Extension
=================================

The RSVP Hello extension is configured on a GR node and its neighbor to rapidly monitor reachability between these RSVP nodes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
   
   
   
   The RSVP Hello extension is enabled globally.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
5. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of an RSVP-enabled interface is displayed.
6. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
   
   
   
   The RSVP Hello extension is enabled on an interface.
   
   After RSVP Hello extension is enabled globally on a node, enable the RSVP Hello extension on each interface of the node.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.