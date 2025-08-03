(Optional) Configuring a Hello Session Between RSVP GR Nodes
============================================================

If TE FRR is deployed, a Hello session must be established between a PLR and an MP. A Hello session must be manually established if it cannot be automatically established between RSVP neighboring nodes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
   
   
   
   RSVP-TE is enabled.
4. Run [**mpls rsvp-te hello**](cmdqueryname=mpls+rsvp-te+hello)
   
   
   
   The RSVP Hello extension is enabled on the local node.
5. Run [**mpls rsvp-te hello nodeid-session**](cmdqueryname=mpls+rsvp-te+hello+nodeid-session) *ip-address*
   
   
   
   A Hello session is established between two RSVP neighboring nodes.
   
   The *ip-address* parameter specifies the LSR ID of an RSVP neighboring node.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.