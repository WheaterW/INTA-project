(Optional) Configuring Refined IPv6 Route Advertisement
=======================================================

Refined IPv6 route advertisement can classify routes and advertise them to different networks.

#### Context

IPv6 network segment routes are generated based on Delegated-IPv6-Prefix attributes (IPv6 PD prefix) that are delivered by a RADIUS server. IPv6 network segment routes and address pool routes are classified based on tags and imported using routing policies. This process allows various routes to be advertised to specific networks.


#### Procedure

* Configure a route tag for a specified type of address pool, such as local or remote address pools.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 unr**](cmdqueryname=ipv6+unr) { **delegated-ipv6-prefix-tag** *tag-value* | **delegated-pool-tag** *tag-value* | **framed-ipv6-address-tag** *tag-value* | **framed-ipv6-prefix-tag** *tag-value* | **framed-ipv6-route-tag** *tag-value* | **local-pool-tag** *tag-value* | **relay-pool-tag** *tag-value* | **remote-pool-tag** *tag-value* } \*
     
     
     
     A route tag is configured for a local or remote address pool.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a route tag for a single address pool.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipv6 pool (system view)**](cmdqueryname=ipv6+pool+%28system+view%29)
     
     
     
     The IPv6 address pool view is displayed.
  3. Run [**unr tag**](cmdqueryname=unr+tag) *tag-value*
     
     
     
     A route tag is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

Create a routing policy, specify a route tag to classify routes, and use OSPFv3 or BGP+ to import different routes. For details, see routing policy configuration.