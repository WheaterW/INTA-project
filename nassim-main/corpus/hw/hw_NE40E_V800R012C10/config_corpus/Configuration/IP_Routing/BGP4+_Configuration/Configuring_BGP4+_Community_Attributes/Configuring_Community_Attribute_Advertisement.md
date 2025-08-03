Configuring Community Attribute Advertisement
=============================================

A community attribute defined in a rout-policy takes effect only after community attribute advertisement is configured.

#### Procedure

* Use a route-policy to define specific community attributes before configuring BGP4+ community attribute advertisement.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**route-policy**](cmdqueryname=route-policy+export) *route-policy-name* **export**
     
     
     
     An export route-policy is configured.
  5. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**advertise-community**](cmdqueryname=advertise-community)
     
     
     
     The device is configured to advertise standard community attributes to the specified peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Use a route-filter to define specific community attributes when configuring BGP4+ community attribute advertisement.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**route-filter**](cmdqueryname=route-filter+export) *route-filter-name* **export**
     
     
     
     An export route-filter is configured.
  5. Run [**peer**](cmdqueryname=peer) *ipv6-address* [**advertise-community**](cmdqueryname=advertise-community)
     
     
     
     The device is configured to advertise standard community attributes to the specified peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.