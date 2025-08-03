(Optional) Configuring an LDP Label Advertisement Mode
======================================================

An LDP label advertisement mode can be configured to control LSP establishment.

#### Context

By default, a downstream device sends Label Mapping messages to an upstream device. This means that if a fault occurs on the network, services can be rapidly switched to the backup path, improving network reliability. Digital subscriber line access multiplexers (DSLAMs) deployed on an MPLS network for user access, however, have low performance. On a large-scale network, a DSLAM can be configured to send Label Mapping messages to only upstream LSRs only after receiving requests for labels. This minimizes the number of unwanted MPLS forwarding entries forwarded by the DSLAM.


#### Procedure

* Configure a label advertisement mode for the local LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mpls ldp advertisement**](cmdqueryname=mpls+ldp+advertisement+dod+du) { **dod** | **du** }
     
     
     
     A label advertisement mode is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When multiple links exist between neighbors, all interfaces must use the same label advertisement mode.
     + Modifying a configured label advertisement mode leads to the reestablishment of an LDP session, resulting in service interruptions.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a label advertisement mode for the remote LDP session.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
     
     
     
     A remote MPLS LDP peer is created, and the remote MPLS-LDP peer view is displayed.
  3. Run [**mpls ldp advertisement**](cmdqueryname=mpls+ldp+advertisement+dod+du) { **dod** | **du** }
     
     
     
     A label advertisement mode is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When the local and remote LDP sessions coexist, they must have the same label advertisement mode.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.