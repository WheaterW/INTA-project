Configuring Route and Label Record
==================================

An ingress can be configured to allow routes and labels to be recorded along a path over which an RSVP-TE CR-LSP will be established.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the MPLS TE tunnel interface is displayed.
3. Run [**mpls te record-route**](cmdqueryname=mpls+te+record-route) [ **label** ]
   
   
   
   Routes and labels can be recorded during the establishment of a CR-LSP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.