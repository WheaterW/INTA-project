(Optional) Setting the Delay Timer Value
========================================

When a faulty link recovers and an LDP session is reestablished on the link, LDP starts the Delay timer to wait for the establishment of an LSP. After the Delay timer expires, LDP notifies the IGP that the synchronization process is complete.

#### Procedure

* In the MPLS-LDP view:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     The MPLS-LDP view is displayed.
  3. Run [**igp-sync-delay timer**](cmdqueryname=igp-sync-delay+timer) *value*
     
     
     
     The Delay timer value is set. This value determines the period during which the device waits for LSP establishment after an LDP session is established.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* In the interface view:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mpls ldp timer igp-sync-delay**](cmdqueryname=mpls+ldp+timer+igp-sync-delay) *value*
     
     
     
     The Delay timer value is set. This value determines the period during which the device waits for LSP establishment after an LDP session is established.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.