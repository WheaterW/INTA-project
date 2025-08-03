Configuring IPv4 IS-IS Route Recursion to IPv6 Next Hops
========================================================

Configuring IPv4 IS-IS route recursion to IPv6 next hops allows IPv4 routes to be forwarded on IPv6 networks, improving network compatibility.

#### Context

During the evolution from IPv4 to IPv6, some IPv4 services may fail to adapt to IPv6 in a short period of time. To ensure compatibility with these IPv4 services on the IPv6 network, you can configure IPv4 route recursion to IPv6 next hops.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**ipv4-prefix ipv6-nexthop enable**](cmdqueryname=ipv4-prefix+ipv6-nexthop+enable)
   
   
   
   IPv4 route recursion to IPv6 next hops is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.