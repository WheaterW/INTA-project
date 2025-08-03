(Optional) Configuring Reliable RSVP Message Transmission
=========================================================

When BFD is not configured on a network, reliable RSVP message transmission can be configured to increase the success rate of detecting link faults, which minimize long-time traffic loss inducted by link intermittent disconnections.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is globally enabled.
4. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
   
   
   
   RSVP-TE is enabled.
5. Run [**mpls rsvp-te reliable-delivery**](cmdqueryname=mpls+rsvp-te+reliable-delivery)
   
   
   
   Reliable RSVP message transmission is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.