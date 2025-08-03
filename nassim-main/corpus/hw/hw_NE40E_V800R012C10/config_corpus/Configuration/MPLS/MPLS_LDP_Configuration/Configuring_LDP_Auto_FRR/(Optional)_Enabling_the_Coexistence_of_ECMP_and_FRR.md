(Optional) Enabling the Coexistence of ECMP and FRR
===================================================

The coexistence of ECMP and FRR can be enabled so that protection paths can be established for ECMP paths, preventing traffic loss stemming from an ECMP path disconnection.

#### Context

On a network with ECMP enabled, the same types of devices reside on both end of ECMP links. If an optical fiber between the two devices is disconnected, network-wide protection fails because backup path calculation is not supported. To prevent traffic loss from such a disconnection, enable the coexistence of ECMP and FRR so that protection paths can be established for ECMP paths.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**ecmp-frr-coexist enable**](cmdqueryname=ecmp-frr-coexist+enable)
   
   
   
   The coexistence of ECMP and FRR is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.