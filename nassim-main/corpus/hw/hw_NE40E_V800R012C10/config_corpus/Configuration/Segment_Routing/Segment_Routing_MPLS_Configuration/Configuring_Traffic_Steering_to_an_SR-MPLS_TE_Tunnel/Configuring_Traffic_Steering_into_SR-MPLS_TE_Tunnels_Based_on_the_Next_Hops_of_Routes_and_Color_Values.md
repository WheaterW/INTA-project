Configuring Traffic Steering into SR-MPLS TE Tunnels Based on the Next Hops of Routes and Color Values
======================================================================================================

This section describes how to configure traffic steering into SR-MPLS TE tunnels based on the next hops of routes and color values.

#### Context

Currently, BGP L3VPNv4, BGP L3VPNv6, EVPN L3VPNv4, and EVPN L3VPNv6 services support SR-MPLS TE tunnels with the color attribute. If you want services to be transmitted over SR-MPLS TE tunnels with the color attribute, specify the **colored-sr-te** parameter in the [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) command when configuring a tunnel policy. If the route of the services carries the color attribute, the involved device selects the SR-MPLS TE tunnel whose destination address and color attribute match the next hop and color attribute of the route, respectively. However, if the route does not carry the color attribute, the device cannot select any tunnel carrying this attribute. Instead, it can only select an SR-MPLS TE tunnel that does not carry the color attribute and whose destination address matches the next hop of the route.


#### Pre-configuration Tasks

Before configuring traffic steering into SR-MPLS TE tunnels, complete the following tasks:

* Configure an SR-MPLS TE tunnel.
* Configure BGP L3VPNv4, BGP L3VPNv6, and EVPN L3VPNv4/L3VPNv6 services.
* Configure a filter, such as an IP prefix list, if you want to restrict the routes that can recurse to SR-MPLS TE tunnels.

#### Procedure

1. Configure the color attribute for the specified SR-MPLS TE tunnel.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
      
      
      
      The SR-MPLS TE tunnel interface view is displayed.
   3. Run [**color**](cmdqueryname=color) *color-value*
      
      
      
      The color attribute is configured for the SR-MPLS TE tunnel.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the SR-MPLS TE tunnel interface view.
2. Configure a route-policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **deny** | **permit** } **node** *node*
      
      
      
      A route-policy with a specified node is created, and the route-policy view is displayed.
   3. (Optional) Configure an if-match clause for the route-policy. The community attributes of routes can be added or modified only if the routes match specified if-match clauses.
      
      
      
      For configuration details, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
   4. Run [**apply extcommunity**](cmdqueryname=apply+extcommunity) **color** *color*
      
      
      
      The BGP color extended community is configured.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the route-policy view.
3. Apply the route-policy to add the color attribute to routes.
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
        
        The import route-policy is applied to the VPN instance IPv4 address family.
     5. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name*
        
        The export route-policy is applied to the VPN instance IPv4 address family.
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
        
        The import route-policy is applied to the VPN instance IPv6 address family.
     5. Run [**export route-policy**](cmdqueryname=export+route-policy) *policy-name*
        
        The export route-policy is applied to the VPN instance IPv6 address family.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
4. Configure a tunnel policy.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
      
      A tunnel policy is created, and the tunnel policy view is displayed.
   3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
      
      A description is configured for the tunnel policy.
   4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **colored-sr-te** **load-balance-number** *load-balance-number* **unmix**
      
      The tunnel selection sequence and the number of tunnels used for load balancing are configured.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      Exit the tunnel policy view.
5. Configure service recursion to SR-MPLS TE tunnels.
   * Configure BGP L3VPN service recursion to SR-MPLS TE tunnels.
     
     For configuration details about BGP L3VPN services, see [BGP/MPLS IP VPN Configuration](dc_vrp_mpls-l3vpn-v4_cfg_0000.html). For configuration details about BGP L3VPNv6 services, see [BGP/MPLS IPv6 VPN Configuration](dc_vrp_mpls-l3vpn-v6_cfg_2000.html).
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv4/IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        The specified tunnel policy is applied to the VPN instance IPv4/IPv6 address family.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure EVPN L3VPN service recursion to SR-MPLS TE tunnels.
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv4/IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
        
        The specified tunnel policy is applied to the EVPN L3VPN instance.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.