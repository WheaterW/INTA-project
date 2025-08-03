Enabling an MPLS Device to Dynamically Establish a BGP BFD Session
==================================================================

Before a dynamic BGP BFD session is established, the capability to dynamically establish BGP BFD sessions must be enabled on each MPLS device.

#### Procedure

* Perform the following steps on the ingress of an E2E BGP tunnel:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  5. Run [**mpls bgp bfd enable**](cmdqueryname=mpls+bgp+bfd+enable)
     
     
     
     The ability to dynamically establish BGP BFD sessions is enabled on the ingress.
     
     The [**mpls bgp bfd enable**](cmdqueryname=mpls+bgp+bfd+enable) command does not create a BFD session. A BGP BFD session can only be dynamically established only after a policy for dynamically establish BGP BFD session is configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on the egress of an E2E BGP tunnel:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bfd**](cmdqueryname=bfd)
     
     
     
     BFD is enabled globally, and the BFD view is displayed.
  3. Run [**mpls-passive**](cmdqueryname=mpls-passive)
     
     
     
     The capability of passively creating a BFD session is configured on the egress.
     
     The [**mpls-passive**](cmdqueryname=mpls-passive) command does not create a BFD session. The egress has to receive an LSP ping request carrying a BFD TLV before creating a BFD session with the ingress.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.