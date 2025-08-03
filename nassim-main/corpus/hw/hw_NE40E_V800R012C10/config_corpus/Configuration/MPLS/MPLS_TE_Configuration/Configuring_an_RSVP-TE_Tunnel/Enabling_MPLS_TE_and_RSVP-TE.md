Enabling MPLS TE and RSVP-TE
============================

MPLS TE and RSVP-TE must be enabled on each LSR in an MPLS domain before TE functions are configured.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If MPLS TE is disabled in the MPLS view, MPLS TE enabled in the interface view is also disabled. As a result, all CR-LSPs configured on this interface go Down, and all configurations associated with these CR-LSPs are deleted.
* If MPLS TE is disabled in the interface view, all CR-LSPs on the interface go Down.
* If RSVP-TE is disabled on an LSR, RSVP-TE is also disabled on all interfaces on this LSR.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is set for a local node.
   
   
   
   When configuring an LSR ID, note the following:
   * Configuring an LSR ID is the prerequisite of all MPLS configurations.
   * An LSR ID must be manually configured because no default LSR ID is available.
   * It is recommended that the IP address of a loopback interface on the LSR be used as the LSR ID.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     The [**undo mpls**](cmdqueryname=undo+mpls) command deletes all MPLS configurations, including the established LDP sessions and LSPs.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
4. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled globally.
5. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te)
   
   
   
   RSVP-TE is enabled.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the interface on which the MPLS TE tunnel is established is displayed.
8. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled on an interface.
9. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled on the interface.
10. Run [**mpls rsvp-te**](cmdqueryname=mpls+rsvp-te) RSVP-TE is enabled on the interface.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    A secondary IP address cannot be configured on an RSVP-TE-enabled interface of an RSVP-TE tunnel. If a secondary IP address is configured for such an interface, the RSVP-TE tunnel may fail to be established.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.