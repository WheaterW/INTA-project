Configuring a BGP IPv4 SR-MPLS TE Policy Peer Relationship Between a Controller and a Forwarder
===============================================================================================

This section describes how to configure a BGP IPv4 SR-MPLS TE Policy peer relationship between a controller and a forwarder, so that the controller can deliver SR-MPLS TE Policies to the forwarder. This improves SR-MPLS TE Policy deployment efficiency.

#### Context

The process for a controller to dynamically generate and deliver an SR-MPLS TE Policy to a forwarder is as follows:

1. The controller collects information, such as network topology and label information, through BGP-LS.
2. The controller and headend forwarder establish a BGP peer relationship of the IPv4 SR-MPLS TE Policy address family.
3. The controller computes an SR-MPLS TE Policy and delivers it to the headend forwarder through the BGP peer relationship. The headend forwarder then generates SR-MPLS TE Policy entries.

To implement the preceding operations, you need to establish a BGP-LS peer relationship and a BGP IPv4 SR-MPLS TE Policy peer relationship between the controller and the specified forwarder.


#### Procedure

* Configure a BGP IPv4 SR-MPLS TE Policy peer relationship.
  
  
  
  This example provides the procedure for configuring a BGP IPv4 SR-MPLS TE Policy peer relationship on the forwarder. The procedure on the controller is similar to that on the forwarder.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
     
     
     
     BGP is enabled, and the BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** { *as-number-plain* | *as-number-dot* }
     
     
     
     A BGP peer is created.
  4. Run [**ipv4-family sr-policy**](cmdqueryname=ipv4-family+sr-policy)
     
     
     
     The BGP IPv4 SR-MPLS TE Policy address family view is displayed.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
     
     
     
     The device is enabled to exchange routes with the specified BGP IPv4 SR-MPLS TE Policy peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Enable the SR-MPLS TE policy to report BGP-LS.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing**](cmdqueryname=segment-routing)
     
     
     
     SR is enabled globally, and the SR view is displayed.
  3. Run [**sr-te-policy bgp-ls enable**](cmdqueryname=sr-te-policy+bgp-ls+enable)
     
     
     
     The SR-MPLS TE policy is enabled to report BGP-LS.
     
     After the [**sr-te-policy bgp-ls enable**](cmdqueryname=sr-te-policy+bgp-ls+enable) command is run, the system sends the path information to the BGP-LS with the granularity of candidate path of the SR-MPLS TE policy.