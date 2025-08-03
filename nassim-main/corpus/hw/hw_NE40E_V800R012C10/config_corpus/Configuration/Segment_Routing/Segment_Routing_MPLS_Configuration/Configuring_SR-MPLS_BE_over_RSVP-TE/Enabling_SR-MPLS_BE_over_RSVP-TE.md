Enabling SR-MPLS BE over RSVP-TE
================================

Enable SR-MPLS route recursion to RSVP-TE tunnels, thereby enabling SR-MPLS BE over RSVP-TE.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**segment-routing mpls over rsvp-te**](cmdqueryname=segment-routing+mpls+over+rsvp-te)
   
   
   
   SR-MPLS route recursion to RSVP-TE tunnels is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.