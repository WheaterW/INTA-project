Globally Enabling MPLS and LDP on an Interface
==============================================

Before you configure a local LDP session, globally enabling MPLS and LDP on an interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface on which an LDP session is to be established is displayed.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled on an interface.
4. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   MPLS LDP is enabled on the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Disabling MPLS LDP from an interface leads to interruptions of all LDP sessions on the interface and deletions of all LSPs established over these LDP sessions.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.