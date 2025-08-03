Configuring BGP-LS
==================

BGP-LS is used to collect network topology information in a more efficient and easier manner.

#### Context

To ensure that topology information can be reported correctly, you need to configure a BGP-LS peer relationship between the controller and forwarder. This example provides the procedure for configuring BGP-LS on the forwarder. The procedure on the controller is similar.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
   
   
   
   BGP is enabled, and the BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *ipv6-address* **as-number** { *as-number-plain* | *as-number-dot* }
   
   
   
   A BGP peer is created.
4. Run [**link-state-family unicast**](cmdqueryname=link-state-family+unicast)
   
   
   
   BGP-LS is enabled, and the BGP-LS address family view is displayed.
5. Run [**peer**](cmdqueryname=peer) *ipv6-address* **enable**
   
   
   
   The device is enabled to exchange BGP-LS routing information with the specified peer.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.