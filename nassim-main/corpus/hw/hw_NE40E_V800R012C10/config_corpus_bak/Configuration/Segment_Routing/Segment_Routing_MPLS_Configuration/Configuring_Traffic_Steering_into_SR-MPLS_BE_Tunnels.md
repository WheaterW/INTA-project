Configuring Traffic Steering into SR-MPLS BE Tunnels
====================================================

Traffic steering into SR-MPLS BE tunnels is to recurse routes to SR-MPLS BE tunnels and forward data using these tunnels.

#### Usage Scenario

After an SR-MPLS BE tunnel is configured, traffic needs to be steered into the tunnel for forwarding. This process is called traffic steering. Currently, SR-MPLS BE tunnels can be used for various routes and services, such as BGP and static routes as well as BGP4+ 6PE, BGP L3VPN and EVPN services. The main traffic steering modes supported by SR-MPLS BE tunnels are as follows:

* Static route mode: When configuring a static route, set the next hop of the route to the destination address of an SR-MPLS BE tunnel. This ensures that traffic transmitted over the route can be steered into the SR-MPLS BE tunnel. For detailed configurations, see [Creating IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0004.html).
* Tunnel policy mode: This mode is implemented through tunnel selector configuration. It allows VPN service routes and non-labeled public network routes to recurse to SR-MPLS BE tunnels. The configuration varies according to the service type.

This section describes how to configure routes and services to recurse to SR-MPLS BE tunnels through tunnel policies.


#### Pre-configuration Tasks

Before configuring traffic steering into SR-MPLS BE tunnels, complete the following tasks:

* Configure BGP routes, static routes, BGP4+ 6PE services, BGP L3VPN services, BGP L3VPNv6 services, and EVPN services correctly.
* Configure a filter, such as an IP prefix list, if you want to restrict the route recursive to a specified SR-MPLS BE tunnel.

#### Procedure

1. Configure a tunnel policy.
   
   
   
   Select either of the following modes based on the traffic steering mode you select.
   
   Comparatively speaking, the tunnel selection sequence mode applies to all scenarios, and the tunnel selector mode applies to inter-AS VPN Option B and inter-AS VPN Option C scenarios.
   
   
   
   * Tunnel selection sequence
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
        
        A tunnel policy is created and the tunnel policy view is displayed.
     3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
        
        A description is configured for the tunnel policy.
     4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **sr-lsp** **load-balance-number** *load-balance-number* [ **unmix** ]
        
        The tunnel selection sequence and the number of tunnels used for load balancing are configured.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
   * Tunnel selector
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* { **permit** | **deny** } **node** *node*
        
        A tunnel selector is created and the view of the tunnel selector is displayed.
     3. (Optional) Configure [**if-match**](cmdqueryname=if-match) clauses.
     4. Run [**apply tunnel-policy**](cmdqueryname=apply+tunnel-policy) *tunnel-policy-name*
        
        A specified tunnel policy is applied to the tunnel selector.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
2. Configure routes and services to recurse to SR-MPLS BE tunnels.
   * Configure non-labeled public BGP routes and static routes to recurse to SR-MPLS BE tunnels.
     
     1. Run [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ]
        
        The function to recurse non-labeled public BGP routes and static routes to SR-MPLS BE tunnels is enabled.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure non-labeled public BGP routes to recurse to SR-MPLS BE tunnels.
     
     For detailed BGP configurations, see [Configuring Basic BGP Functions](dc_vrp_bgp_cfg_3004.html).
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) [ **tunnel-selector** *tunnel-selector-name* ]
        
        The function to recurse non-labeled public BGP routes to SR-MPLS BE tunnels is enabled.
        
        The [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) command and [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command are mutually exclusive. You can select either of them for configuration.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure static routes to recurse to SR-MPLS BE tunnels.
     
     For detailed static route configurations, see [Creating IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0004.html).
     
     1. Run [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ]
        
        The function to recurse static routes to SR-MPLS BE tunnels for MPLS forwarding is enabled.
        
        The [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) command and [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command are mutually exclusive. You can select either of them for configuration.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure BGP L3VPN services to recurse to SR-MPLS BE tunnels.
     
     For detailed BGP L3VPN configurations, see [BGP/MPLS IP VPN Configuration](dc_vrp_mpls-l3vpn-v4_cfg_0000.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
        
        The VPN instance-specific IPv4 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the VPN instance-specific IPv4 address family.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure BGP L3VPNv6 services to recurse to SR-MPLS BE tunnels.
     
     For detailed BGP L3VPNv6 configurations, see [BGP/MPLS IPv6 VPN Configuration](dc_vrp_mpls-l3vpn-v6_cfg_2000.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance-specific IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the VPN instance-specific IPv6 address family.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure BGP4+ 6PE services to recurse to SR-MPLS BE tunnels.
     
     For detailed BGP4+ 6PE configurations, see [Configuring BGP4+ 6PE](dc_vrp_bgp6_cfg_0056.html).
     
     **Method 1: Apply a tunnel policy to a specified BGP4+ peer.**
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The BGP IPv6 unicast address family view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
        
        A specified 6PE peer is enabled.
     4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **tnl-policy** *tnl-policy-name*
        
        A specified tunnel policy is applied to the 6PE peer.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     
     **Method 2: Apply a tunnel selector to all the routes of a specified BGP IPv6 unicast address family.**
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The BGP IPv6 unicast address family view is displayed.
     3. Run [**unicast-route recursive-lookup tunnel-v4**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v4) [ **tunnel-selector** *tunnel-selector-name* ]
        
        The function to recurse non-labeled public BGP routes to SR-MPLS BE tunnels is enabled.
        
        The [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) command and [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command are mutually exclusive. You can select either of them for configuration.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure EVPN services to recurse to SR-MPLS BE tunnels.
     
     For details on how to configure EVPN, see [EVPN Configuration](dc_vrp_evpn_cfg_0000.html). The configuration varies according to the service type.
     
     To apply a tunnel policy to an EVPN L3VPN instance, perform the following steps:
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv4/IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
        
        A specified tunnel policy is applied to the EVPN L3VPN instance.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to a BD EVPN instance, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
        
        The BD EVPN instance view is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the BD EVPN instance.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to an EVPN instance that works in EVPN VPWS mode, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
        
        The view of a specified EVPN instance that works in EVPN VPWS mode is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the EVPN instance that works in EVPN VPWS mode.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to a basic EVPN instance, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name*
        
        The EVPN instance view is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the basic EVPN instance.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.