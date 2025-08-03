Configuring BGP Peer Relationships Between the Controller and Forwarder
=======================================================================

Configuring BGP peer relationships between a controller and a forwarder allows the controller to deliver SRv6 TE Policies to the forwarder. This improves the efficiency of automated SRv6 TE Policy deployment.

#### Context

The process for a controller to deliver an SRv6 TE Policy is as follows:

1. The controller collects information, such as network topology and SID information, through BGP-LS.
2. The controller and headend forwarder establish an IPv6 SR Policy address family-specific BGP peer relationship.
3. The controller computes an SRv6 TE Policy path based on network topology information and delivers it to the headend forwarder through the BGP peer relationship. The headend then generates an SRv6 TE Policy entry.

To implement the preceding operations, you need to establish a BGP-LS peer relationship and a BGP IPv6 SR Policy peer relationship between the controller and the specified forwarder.


#### Procedure

1. Configure a BGP-LS peer relationship.
   
   
   
   BGP-LS is used to collect network topology information in a more efficient and easier manner. To ensure that topology information can be reported correctly, you need to configure a BGP-LS peer relationship between the controller and forwarder. This example provides the procedure for configuring BGP-LS on the forwarder. The procedure on the controller is similar to that on the forwarder.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      BGP is enabled, and the BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* |*group-name* | *ipv6-address* } **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      A BGP peer is configured.
   4. Run [**link-state-family unicast**](cmdqueryname=link-state-family+unicast)
      
      
      
      BGP-LS is enabled and the BGP-LS address family view is displayed.
   5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* |*group-name* | *ipv6-address* } **enable**
      
      
      
      The device is enabled to exchange route information with a specified BGP-LS peer.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure a BGP IPv6 SR Policy peer relationship.
   
   
   
   This example provides the procedure for configuring a BGP IPv6 SR Policy peer relationship on the forwarder. The procedure on the controller is similar to that on the forwarder.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
      
      
      
      BGP is enabled and the BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* | *ipv6-address* } **as-number** { *as-number-plain* | *as-number-dot* }
      
      
      
      A BGP peer is created.
   4. Run [**ipv6-family sr-policy**](cmdqueryname=ipv6-family+sr-policy)
      
      
      
      The BGP IPv6 SR Policy address family view is displayed.
   5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* | *ipv6-address* } **enable**
      
      
      
      A specified BGP IPv6 SR Policy peer is enabled.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.