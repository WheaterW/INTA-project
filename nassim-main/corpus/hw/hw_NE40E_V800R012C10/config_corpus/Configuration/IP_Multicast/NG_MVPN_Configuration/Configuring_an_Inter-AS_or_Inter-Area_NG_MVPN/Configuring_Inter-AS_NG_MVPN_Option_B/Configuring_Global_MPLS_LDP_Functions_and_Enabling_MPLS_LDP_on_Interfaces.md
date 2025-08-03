Configuring Global MPLS LDP Functions and Enabling MPLS LDP on Interfaces
=========================================================================

Global LDP must be enabled on each node before LDP services can be configured in an MPLS domain.

#### Procedure

* Configuring Global MPLS LDP Functions
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     The LSR ID of the local node is configured.
     
     When configuring an LSR ID, note the following:
     + LSR IDs must be set before you run other MPLS commands.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + The LSR ID, MVPN ID, and IP address of the BGP peer interface (usually a loopback interface) configurations must be consistent.
     + Using the IP address of a loopback interface on an LSR as an LSR ID is recommended.
       
       ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
       
       The [**undo mpls**](cmdqueryname=undo+mpls) command deletes all MPLS configurations, including the established LDP sessions and LSPs.
     + In NG MVPN scenarios, LDP must be enabled on the interfaces between ASBRs to generate P2MP tunnels in end-to-end mode. In unicast scenarios, the outer labels of data exchanged between ASBRs are allocated by BGP instead of LDP.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally, and the MPLS view is displayed.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled globally, and the MPLS-LDP view is displayed.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.
* Enabling MPLS LDP on Interfaces
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which an LDP session is to be established is displayed.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled on an interface.
  4. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled on an interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Disabling MPLS LDP from an interface leads to interruptions of all LDP sessions on the interface and deletions of all LSPs established over these LDP sessions.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configurations are committed.