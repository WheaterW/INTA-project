Enabling an MPLS Device to Dynamically Establish a BFD Session
==============================================================

A dynamic BFD session that monitors both the primary and FRR LSPs can be established only after an MPLS device is enabled to dynamically establish the BFD session.

#### Procedure

* Perform the following steps on the ingress:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is globally enabled.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  5. Run [**mpls bfd enable**](cmdqueryname=mpls+bfd+enable)
     
     
     
     The capability of dynamically establishing a BFD session is configured.
     
     
     
     The command does not create a BFD session.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on the egress:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is globally enabled, and the BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The capability of passively creating a BFD session is configured.
     
     
     
     After this command is run, a BFD session will be established only after the egress receives an LSP ping request packet that carries a BFD TLV from the ingress.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.