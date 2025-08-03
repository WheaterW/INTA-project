Configuring Community Attribute Advertisement
=============================================

A community attribute defined in a routing policy takes effect only after community attribute advertisement is configured.

#### Procedure

* Use a route-policy to define specific community attributes when configuring BGP community attribute advertisement.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-policy+export) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=peer+route-policy+export) *route-policy-name* **export**
     
     
     
     An export route-policy is configured.
  5. Run [**peer**](cmdqueryname=peer+advertise-community) { *ipv4-address* | *group-name* } [**advertise-community**](cmdqueryname=peer+advertise-community)
     
     
     
     The device is configured to advertise standard community attributes to the specified peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Use a route-filter to define specific community attributes when configuring BGP community attribute advertisement.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+route-filter+export) { *ipv4-address* | *group-name* } [**route-filter**](cmdqueryname=peer+route-filter+export) *route-filter-name* **export**
     
     
     
     An export route-filter is configured.
  5. Run [**peer**](cmdqueryname=peer+advertise-community) { *ipv4-address* | *group-name* } [**advertise-community**](cmdqueryname=peer+advertise-community)
     
     
     
     The device is configured to advertise standard community attributes to the specified peer.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.