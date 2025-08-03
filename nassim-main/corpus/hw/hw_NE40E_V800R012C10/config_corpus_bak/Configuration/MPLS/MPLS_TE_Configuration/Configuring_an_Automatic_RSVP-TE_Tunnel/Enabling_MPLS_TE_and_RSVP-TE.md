Enabling MPLS TE and RSVP-TE
============================

Enabling MPLS TE and RSVP-TE on each node and interface in an MPLS domain is the prerequisites for all TE features.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is set for a local node.
   
   
   
   When configuring an LSR ID, note the following:
   * Configuring an LSR ID is the prerequisite of all MPLS configurations.
   * An LSR ID must be manually configured because no default LSR ID is available.
   * It is recommended that the IP address of a loopback interface on the LSR be used as the LSR ID.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
4. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled globally.
5. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
   
   
   
   RSVP-TE is enabled.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.