Configuring the Color Extended Community
========================================

This section describes how to configure the Color Extended Community for a route through a route-policy, enabling the route to recurse to an SR-MPLS TE Policy based on the color value and next-hop address in the route.

#### Context

The route coloring process is as follows:

1. Configure a route-policy and set a specific color value for the desired route.
2. Apply the route-policy to a BGP peer or a VPN instance as an import or export policy.

#### Procedure

1. Configure a route-policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **deny** | **permit** } **node** *node*
      
      
      
      A route-policy with a specified node is created, and the route-policy view is displayed.
   3. (Optional) Configure an if-match clause as a route-policy filter criterion. You can add or modify the Color Extended Community only for a route-policy that meets the filter criterion.
      
      
      
      For details about the configuration, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
   4. Run [**apply extcommunity**](cmdqueryname=apply+extcommunity) **color** *color*
      
      
      
      The Color Extended Community is configured.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Apply the route-policy.
   * Apply the route-policy to a BGP IPv4 unicast peer.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
        
        A BGP peer is created.
     4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
        
        The IPv4 unicast address family view is displayed.
     5. Run [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
        
        A BGP import or export route-policy is configured.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Apply the route-policy to a BGP4+ 6PE peer.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
        
        A BGP4+ 6PE peer is created.
     4. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The IPv6 unicast address family view is displayed.
     5. Run [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
        
        A BGP4+ 6PE import or export route-policy is configured.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Apply the route-policy to a BGP VPNv4 peer.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
        
        A BGP peer is created.
     4. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4**
        
        The BGP VPNv4 address family view is displayed.
     5. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
        
        The BGP VPNv4 peer relationship is enabled.
     6. Run [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
        
        A BGP import or export route-policy is configured.
     7. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Apply the route-policy to a BGP VPNv6 peer.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer+as-number) { *ipv4-address* | *group-name* } **as-number** { *as-number-plain* | *as-number-dot* }
        
        A BGP peer is created.
     4. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6**
        
        The BGP VPNv6 address family view is displayed.
     5. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
        
        The BGP VPNv6 peer relationship is enabled.
     6. Run [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
        
        A BGP import or export route-policy is configured.
     7. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Apply the route-policy to a BGP EVPN peer.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
        
        The BGP EVPN address family view is displayed.
     4. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
        
        The BGP EVPN peer relationship is enabled.
     5. Run [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **import** | **export** }
        
        A BGP EVPN import or export route-policy is configured.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Apply the route-policy to a VPN instance IPv4 address family.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
        
        The VPN instance IPv4 address family view is displayed.
     4. Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
        
        An import route-policy is configured for the VPN instance IPv4 address family.
     5. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name*
        
        An export route-policy is configured for the VPN instance IPv4 address family.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Apply the route-policy to a VPN instance IPv6 address family.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv6 address family view is displayed.
     4. Run [**import route-policy**](cmdqueryname=import+route-policy) *policy-name*
        
        An import route-policy is configured for the VPN instance IPv6 address family.
     5. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name*
        
        An export route-policy is configured for the VPN instance IPv6 address family.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.