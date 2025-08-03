Configuring an MPLS LDP Tunnel
==============================

The EVPN E-Line model allows you to configure packets to traverse the backbone network through P2P MPLS LDP, TE, SR, or other tunnels.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   The LSR ID of the local node is configured.
   
   
   
   When configuring an LSR ID, note the following:
   * Configuring an LSR ID is the prerequisite of all MPLS configurations.
   * An LSR ID must be manually configured because no default LSR ID is available.
   * Using a loopback interface address of an LSR as the LSR ID is recommended.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     The [**undo mpls**](cmdqueryname=undo+mpls) command deletes all MPLS configurations, including the established LDP sessions and LSPs.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally, and the MPLS view is displayed.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   MPLS LDP is enabled globally, and the MPLS-LDP view is displayed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which an LDP session is to be established is displayed.
8. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled on the interface.
9. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   MPLS LDP is enabled on an interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Disabling MPLS LDP from an interface leads to interruptions of all LDP sessions on the interface and deletions of all LSPs established over these LDP sessions.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.