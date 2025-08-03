Configuring AIGP Attributes for Routes
======================================

The Accumulated Interior Gateway Protocol (AIGP) attribute allows devices in an AIGP domain to use the optimal routes to forward data.

#### Context

Generally, a set of ASs managed by the same administrative department is called an AIGP administrative domain, or AIGP domain for short.

Routing protocols that run within a single administrative domain, such as IGPs, assign a metric to each link and select the path with the smallest metric. BGP, designed to provide routing over a large number of independent administrative domains, does not select paths based on metrics. If a single administrative domain (AIGP domain) consists of several BGP networks, it is desirable for BGP to select paths based on metrics, just as an IGP does.

After the AIGP attribute is configured in an AIGP domain, BGP selects optimal routes based on route metrics, just as an IGP does. This ensures that all devices in the AIGP domain forward data along the optimal paths.


#### Procedure

1. Enable AIGP capability for a specified peer or peer group.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer+aigp) { *group-name* | *ipv6-address* } **aigp**
      
      
      
      The AIGP capability is enabled for a BGP peer or peer group.
      
      
      
      BGP allows you to enable the AIGP capability for either a BGP peer or a BGP peer group. The configuration on a peer takes precedence over that on a peer group. If a BGP peer without the AIGP capability joins a BGP peer group that has the AIGP capability, the BGP peer inherits the AIGP capability of the BGP peer group. After a BGP peer inherits the AIGP capability of a BGP peer group, you can run the [**undo peer aigp**](cmdqueryname=undo+peer+aigp) command to delete the AIGP configuration from the BGP peer.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. (Optional) Allow IPv6 public network routes to participate in route selection using the AIGP attribute of the corresponding BGP LSP.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
   4. Run [**bestroute nexthop-resolved aigp**](cmdqueryname=bestroute+nexthop-resolved+aigp)
      
      
      
      IPv6 public network routes are allowed to participate in route selection using the AIGP attribute of the corresponding BGP LSP.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.