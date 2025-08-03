Enabling the Mode of Decoupling a Service Next Hop from LDP and SR-MPLS BE
==========================================================================

This section describes how to configure the mode of decoupling a service next hop from LDP and SR-MPLS BE.

#### Context

When private and public network separation services recurse to an LDP or SR-MPLS BE tunnel, packets may be dropped due to a change in the outbound interface of the LDP or SR-MPLS BE tunnel. To reduce the packet loss rate and improve link change-induced convergence performance, decouple the next hops from the LDP or SR-MPLS BE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp-srbe convergence enhance**](cmdqueryname=mpls+ldp-srbe+convergence+enhance)
   
   
   
   The mode of decoupling a service next hop from LDP and SR-MPLS BE is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

* Run the [**display mpls convergence mode**](cmdqueryname=display+mpls+convergence+mode) command to check whether the mode of decoupling a service next hop from LDP and SR-MPLS BE has taken effect.