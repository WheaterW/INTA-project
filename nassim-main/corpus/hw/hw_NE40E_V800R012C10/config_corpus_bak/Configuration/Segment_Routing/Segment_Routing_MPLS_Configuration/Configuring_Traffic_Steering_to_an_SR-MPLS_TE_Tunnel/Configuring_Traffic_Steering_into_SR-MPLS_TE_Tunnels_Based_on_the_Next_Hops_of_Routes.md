Configuring Traffic Steering into SR-MPLS TE Tunnels Based on the Next Hops of Routes
=====================================================================================

This section describes how to configure traffic steering into SR-MPLS TE tunnels based on the next hops of routes.

#### Usage Scenario

After an SR-MPLS TE tunnel is configured, traffic needs to be steered into the tunnel for forwarding. This process is called traffic steering. Currently, SR-MPLS TE tunnels can be used for various routes and services, such as BGP and static routes as well as BGP4+ 6PE, BGP L3VPN and EVPN services. The main traffic steering modes supported by SR-MPLS TE tunnels are as follows:

* Static route: When configuring a static route, set the outbound interface of the route to an SR-MPLS TE tunnel interface so that traffic transmitted over the route is steered into the SR-MPLS TE tunnel. For configuration details, see [Creating IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0004.html).
* Auto route: An IGP uses an auto route related to an SR-MPLS TE tunnel that functions as a logical link to compute a path. The tunnel interface is used as an outbound interface in the auto route. For configuration details, see [Configuring IGP Shortcut](dc_vrp_te-p2p_cfg_0034.html) and [Configuring Forwarding Adjacency](dc_vrp_te-p2p_cfg_0035.html).
* Policy-based routing (PBR): SR-MPLS TE PBR has the same definition as IP unicast PBR. PBR is implemented by defining a series of matching rules and behavior. An outbound interface in an apply clause is set to an interface on an SR-MPLS TE tunnel. If packets do not match PBR rules, they are properly forwarded using IP; if they match PBR rules, they are forwarded over specific tunnels. For configuration details, see [Policy-based Routing Configuration](../ne/dc_ne_qos_cfg_7001.html).
* Tunnel policy: The tunnel policy mode is implemented through tunnel selector or tunnel binding configuration. This mode allows both VPN services and non-labeled public routes to recurse to SR-MPLS TE tunnels. The configuration varies according to the service type.


#### Pre-configuration Tasks

Before configuring traffic steering into SR-MPLS TE tunnels, complete the following tasks:

* Configure BGP routes, static routes, BGP4+ 6PE services, BGP L3VPN services, BGP L3VPNv6 services, and EVPN services correctly.
* Configure a filter, such as an IP prefix list, if you want to restrict the route recursive to a specified SR-MPLS TE tunnel.

#### Procedure

1. Configure a tunnel policy.
   
   
   
   Select either of the following modes based on the traffic steering mode you select.
   
   The tunnel binding mode rather than the tunnel selection sequence mode allows you to specify the SR-MPLS TE tunnel to be used, facilitating QoS deployment. The tunnel selector mode applies to inter-AS VPN Option B and inter-AS VPN Option C scenarios.
   
   
   
   * Tunnel selection sequence
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
        
        A tunnel policy is created and the tunnel policy view is displayed.
     3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
        
        Description information is configured for the tunnel policy.
     4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **sr-te** **load-balance-number** *load-balance-number* [ **unmix** ]
        
        The tunnel selection sequence and the number of tunnels used for load balancing are configured.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
   * Tunnel binding
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
        
        A tunnel policy is created and the tunnel policy view is displayed.
     3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
        
        Description information is configured for the tunnel policy.
     4. Run [**tunnel binding**](cmdqueryname=tunnel+binding) **destination** *dest-ip-address* **te** { *tunnel-name* } &<1-32> [ **ignore-destination-check** ] [ **down-switch** ]
        
        A tunnel binding policy is configured to bind the specified destination IP address and SR-MPLS TE tunnel.
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
2. Configure routes and services to recurse to SR-MPLS TE tunnels.
   * Configure non-labeled public BGP routes and static routes to recurse to SR-MPLS TE tunnels.
     
     1. Run [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ]
        
        The function to recurse non-labeled public BGP routes and static routes to SR-MPLS TE tunnels is enabled.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure non-labeled public BGP routes to recurse to SR-MPLS TE tunnels.
     
     For detailed BGP configurations, see [Configuring Basic BGP Functions](dc_vrp_bgp_cfg_3004.html).
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) [ **tunnel-selector** *tunnel-selector-name* ]
        
        The function to recurse non-labeled public BGP routes to SR-MPLS TE tunnels is enabled.
        
        The [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) command and [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command are mutually exclusive. You can select either of them for configuration.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure static routes to recurse to SR-MPLS TE tunnels.
     
     For detailed static route configurations, see [Creating IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0004.html).
     
     1. Run [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ]
        
        The function to recurse static routes to SR-MPLS TE tunnels for MPLS forwarding is enabled.
        
        The [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) command and [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command are mutually exclusive. You can select either of them for configuration.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure BGP L3VPN services to recurse to SR-MPLS TE tunnels.
     
     For detailed BGP L3VPN configurations, see [BGP/MPLS IP VPN Configuration](dc_vrp_mpls-l3vpn-v4_cfg_0000.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
        
        The VPN instance-specific IPv4 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the VPN instance-specific IPv4 address family.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure BGP L3VPNv6 services to recurse to SR-MPLS TE tunnels.
     
     For detailed BGP L3VPNv6 configurations, see [BGP/MPLS IPv6 VPN Configuration](dc_vrp_mpls-l3vpn-v6_cfg_2000.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance-specific IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A specified tunnel policy is applied to the VPN instance-specific IPv6 address family.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure BGP4+ 6PE services to recurse to SR-MPLS TE tunnels.
     
     For detailed BGP4+ 6PE configurations, see [Configuring BGP4+ 6PE](dc_vrp_bgp6_cfg_0056.html).
     
     **Method 1: Apply a tunnel policy to a specified BGP4+ peer.**
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The BGP IPv6 unicast address family view is displayed.
     3. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
        
        The local device is enabled to exchange routes with a specified 6PE peer.
     4. Run [**peer**](cmdqueryname=peer+tnl-policy) *ipv4-address* **tnl-policy** *tnl-policy-name*
        
        A tunnel policy is applied to the 6PE peer.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     
     **Method 2: Apply a tunnel selector to all the routes of a specified BGP IPv6 unicast address family.**
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The BGP IPv6 unicast address family view is displayed.
     3. Run [**unicast-route recursive-lookup tunnel-v4**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v4) [ **tunnel-selector** *tunnel-selector-name* ]
        
        The function to recurse non-labeled public BGP routes to SR-MPLS TE tunnels is enabled.
        
        The [**unicast-route recursive-lookup tunnel**](cmdqueryname=unicast-route+recursive-lookup+tunnel) command and [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) command are mutually exclusive. You can select either of them for configuration.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure EVPN services to recurse to SR-MPLS TE tunnels.
     
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