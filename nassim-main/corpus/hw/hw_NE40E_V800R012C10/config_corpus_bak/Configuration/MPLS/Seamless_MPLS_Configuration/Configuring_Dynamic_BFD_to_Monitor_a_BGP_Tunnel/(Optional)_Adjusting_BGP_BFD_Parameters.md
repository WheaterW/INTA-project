(Optional) Adjusting BGP BFD Parameters
=======================================

You can adjust BGP BFD parameters, including the minimum interval at which BGP BFD packets are sent, the minimum interval at which BGP BFD packets are received, and the BGP BFD detection multiplier.

#### Context

Perform the following steps on the ingress of an E2E BGP tunnel:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. Run [**mpls ping interval**](cmdqueryname=mpls+ping+interval) *interval*
   
   
   
   The interval at which LSP ping packets are sent is set.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
6. Run [**mpls bgp bfd**](cmdqueryname=mpls+bgp+bfd+detect-multiplier+min-rx-interval+min-tx-interval)  { ****detect-multiplier**** **multiplier**| ****min-rx-interval**** **value-min-rx-interval**| ****min-tx-interval**** **value-min-tx-interval** } \*
   
   
   
   Time parameters are set for BGP BFD.
   
   
   
   The BFD detection intervals are calculated as follows:
   
   * Effective interval at which BFD packets are sent by the local end = Max { Configured minimum interval at which BFD packets are sent by the local end, Configured minimum interval at which BFD packets are received by the remote end }
   * Effective interval at which BFD packets are received by the local end = Max { Configured minimum interval at which BFD packets are sent by the remote end, Configured minimum interval at which BFD packets are received by the local end }
   * Effective detection interval on the local end = Effective interval at which BFD packets are received by the local end x Detection multiplier configured on the remote end
   
   The egress has the fixed minimum interval at which BGP BFD packets are sent, the fixed minimum interval at which BGP BFD packets are received, and the detection multiplier of 3. You can only change the time parameters on the ingress so that the BFD time parameters can be updated on both the ingress and egress.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.