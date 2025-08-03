Enabling the RSVP GR Support Capability
=======================================

The RSVP GR support capability helps a node support its neighbors' GR capabilities.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
   
   
   
   RSVP-TE is enabled.
4. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
   
   
   
   The RSVP Hello extension is enabled on the local node.
5. Run [**mpls rsvp-te hello support-peer-gr**](cmdqueryname=mpls+rsvp-te+hello+support-peer-gr)
   
   
   
   The RSVP GR support function is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.