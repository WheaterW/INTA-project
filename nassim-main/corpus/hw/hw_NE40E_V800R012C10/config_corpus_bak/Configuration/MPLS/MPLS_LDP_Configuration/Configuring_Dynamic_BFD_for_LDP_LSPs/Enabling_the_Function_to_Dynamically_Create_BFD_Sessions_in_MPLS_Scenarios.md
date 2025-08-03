Enabling the Function to Dynamically Create BFD Sessions in MPLS Scenarios
==========================================================================

Enable BFD on the ingress and egress in an MPLS domain, after which BFD sessions can be dynamically created.

#### Procedure

* Perform the following steps on the ingress:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls bfd enable**](cmdqueryname=mpls+bfd+enable)
     
     
     
     The function to dynamically create BFD sessions for LDP LSPs is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After this step is complete, a BFD session can be established when the egress is configured and the ingress sends LSP Ping Request packets carrying BFD TLV objects.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on the egress:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     The BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The capability of passively creating a BFD session is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After this command is run, the egress does not create a BFD session immediately. Instead, the egress waits for an LSP ping request carrying the BFD TLV before creating a BFD session.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.