Configuring Traffic Steering into a Flex-Algo LSP
=================================================

The traffic steering configuration allows you to recurse routes to Flex-Algo-based SR-MPLS BE tunnels (also called Flex-Algo LSPs) for traffic forwarding.

#### Context

After a Flex-Algo LSP is configured, traffic needs to be steered into the LSP for forwarding. Currently, Flex-Algo LSPs can be used for various routes, such as BGP and static routes, as well as various services, such as BGP L3VPN, BGP4+ 6PE, and EVPN services. This section describes how to use tunnel policies to recurse a service to a Flex-Algo LSP.


#### Pre-configuration Tasks

Before configuring traffic steering, complete the following tasks:

* Configure BGP routes, static routes, BGP4+ 6PE services, BGP L3VPN services, BGP L3VPNv6 services, or EVPN services correctly.
* Configure an IP prefix list and a tunnel policy to limit the number of routes that can recurse to a Flex-Algo LSP.

#### Procedure

1. Configure a tunnel policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
      
      
      
      A tunnel policy is created, and the tunnel policy view is displayed.
   3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
      
      
      
      A description is configured for the tunnel policy.
   4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **flex-algo-lsp** **load-balance-number** *load-balance-number* [ **unmix** ]
      
      
      
      The tunnel selection sequence and the number of tunnels used for load balancing are configured.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the tunnel policy view.
2. Configure services to recurse to Flex-Algo LSPs.
   * Configure non-labeled public BGP routes to recurse to Flex-Algo LSPs.
     
     For detailed BGP configurations, see [Configuring Basic BGP Functions](dc_vrp_bgp_cfg_3004.html).
     
     1. Run [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] **tunnel-policy** *policy-name*
        
        Non-labeled public BGP routes are configured to recurse to Flex-Algo LSPs.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure static routes to recurse to Flex-Algo LSPs.
     
     For detailed static route configurations, see [Configuring IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0003.html).
     
     1. Run [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] **tunnel-policy** *policy-name*
        
        Static routes are configured to recurse to Flex-Algo LSPs for MPLS forwarding.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a BGP L3VPN service to recurse to a Flex-Algo LSP.
     
     For detailed BGP L3VPN configurations, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
        
        The VPN instance IPv4 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the VPN instance IPv4 address family.
     4. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the L3VPN service to recurse to a Flex-Algo LSP. If a remote VPN route without the color extended community attribute is leaked to a local VPN instance, the default color value is used for the recursion to a Flex-Algo LSP.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a BGP L3VPNv6 service to recurse to a Flex-Algo LSP.
     
     For detailed BGP L3VPNv6 configurations, see [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the VPN instance IPv6 address family.
     4. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the L3VPNv6 service to recurse to a Flex-Algo LSP. If a remote VPN route without the color extended community attribute is leaked to a local VPN instance, the default color value is used for the recursion to a Flex-Algo LSP.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a BGP4+ 6PE service to recurse to a Flex-Algo LSP.
     
     For detailed BGP4+ 6PE configurations, see [Configuring BGP4+ 6PE](dc_vrp_bgp6_cfg_0056.html).
     
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
   * Configure an EVPN service to recurse to a Flex-Algo LSP.
     
     For detailed EVPN configurations, see [Configuring EVPN VPLS over MPLS (BD EVPN Instance)](dc_vrp_evpn_cfg_0065.html).
     
     To apply a tunnel policy to an EVPN L3VPN instance, perform the following steps:
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv4/IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
        
        A tunnel policy is applied to the EVPN L3VPN instance.
     4. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value* **evpn**
        
        The default color value is specified for the EVPN L3VPN service to recurse to a Flex-Algo LSP.
        
        If a remote EVPN route without the color extended community attribute is leaked to a local VPN instance, the default color value is used for the recursion to a Flex-Algo LSP.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to a BD EVPN instance, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
        
        The BD EVPN instance view is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the BD EVPN instance.
     3. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the EVPN service to recurse to a Flex-Algo LSP. If a remote EVPN route without the color extended community attribute is leaked to a local EVPN instance, the default color value is used for the recursion to a Flex-Algo LSP.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to an EVPN instance that works in EVPN VPWS mode, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
        
        The view of the EVPN instance in EVPN VPWS mode is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the EVPN instance in EVPN VPWS mode.
     3. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the EVPN service to recurse to a Flex-Algo LSP. If a remote EVPN route without the color extended community attribute is leaked to a local EVPN instance, the default color value is used for the recursion to a Flex-Algo LSP.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to a basic EVPN instance, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name*
        
        The EVPN instance view is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the basic EVPN instance.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.