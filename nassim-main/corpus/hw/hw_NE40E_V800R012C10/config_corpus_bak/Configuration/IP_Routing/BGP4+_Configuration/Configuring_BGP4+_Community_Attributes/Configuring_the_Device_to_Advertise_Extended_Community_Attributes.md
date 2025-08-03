Configuring the Device to Advertise Extended Community Attributes
=================================================================

The extended community attributes defined in a route-policy take effect only after the extended community attributes are advertised.

#### Procedure

* Use a route-policy to define specific extended community attributes before configuring BGP4+ to advertise the extended community attributes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *ipv6-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy+export) *route-policy-name* **export**
     
     
     
     An export route-policy is configured.
  5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**advertise-ext-community**](cmdqueryname=advertise-ext-community)
     
     
     
     BGP4+ is configured to send routes with extended community attributes to the specified peer.
     
     
     
     If a peer only needs to accept routes but not extended community attributes, you can run the [**peer discard-ext-community**](cmdqueryname=peer+discard-ext-community) command on the peer to discard the extended community attributes carried in received routes. If the peer only needs to discard the RPKI BGP origin AS validation result, specify [**origin-as-validation**](cmdqueryname=origin-as-validation) in the command.
  6. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**advertise ebgp link-bandwidth**](cmdqueryname=advertise+ebgp+link-bandwidth)
     
     
     
     The device is configured to advertise the link bandwidth extended community attribute to the specified EBGP peer.
  7. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } [**advertise link-bandwidth transitive**](cmdqueryname=advertise+link-bandwidth+transitive)
     
     
     
     The device is configured to convert the link bandwidth extended community attribute (optional non-transitive) carried in BGP4+ routes into an optional transitive attribute before advertising the routes to the specified peer. If the device changes the next-hop address of a received route carrying the link bandwidth extended community attribute to its own address, the device deletes this attribute before advertising the route to the specified peer.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Use a route-filter to define specific extended community attributes before configuring BGP4+ to advertise the extended community attributes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**route-filter**](cmdqueryname=route-filter+export) *route-filter-name* **export**
     
     
     
     An export route-filter is configured.
  5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**advertise-ext-community**](cmdqueryname=advertise-ext-community)
     
     
     
     BGP4+ is configured to send routes with extended community attributes to the specified peer.
     
     
     
     If a peer only needs to accept routes but not extended community attributes, you can run the [**peer discard-ext-community**](cmdqueryname=peer+discard-ext-community) command on the peer to discard the extended community attributes carried in received routes. If the peer only needs to discard the RPKI BGP origin AS validation result, specify [**origin-as-validation**](cmdqueryname=origin-as-validation) in the command.
  6. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**advertise ebgp link-bandwidth**](cmdqueryname=advertise+ebgp+link-bandwidth)
     
     
     
     The device is configured to advertise the link bandwidth extended community attribute to the specified EBGP peer.
  7. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } [**advertise link-bandwidth transitive**](cmdqueryname=advertise+link-bandwidth+transitive)
     
     
     
     The device is configured to convert the link bandwidth extended community attribute (optional non-transitive) carried in BGP4+ routes into an optional transitive attribute before advertising the routes to the specified peer. If the device changes the next-hop address of a received route carrying the link bandwidth extended community attribute to its own address, the device deletes this attribute before advertising the route to the specified peer.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.