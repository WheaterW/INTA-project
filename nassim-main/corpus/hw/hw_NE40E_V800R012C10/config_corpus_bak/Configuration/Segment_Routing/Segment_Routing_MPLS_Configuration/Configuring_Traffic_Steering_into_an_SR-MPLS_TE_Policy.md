Configuring Traffic Steering into an SR-MPLS TE Policy
======================================================

This section describes how to configure traffic steering to recurse a route to an SR-MPLS TE Policy so that traffic can be forwarded through a path of the SR-MPLS TE Policy.

#### Usage Scenario

After an SR-MPLS TE Policy is configured, traffic needs to be steered into the policy for forwarding. This process is called traffic steering. Currently, SR-MPLS TE Policies can be used for various routes and services, such as BGP and static routes as well as BGP4+ 6PE, BGP L3VPN and EVPN services. This section describes how to configure services to recurse to an SR-MPLS TE Policy through a specified tunnel policy.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

EVPN VPWS and EVPN VPLS packets do not support DSCP-based traffic steering because they do not carry DSCP values.



#### Pre-configuration Tasks

Before configuring traffic steering, complete the following tasks:

* Configure BGP routes, static routes, BGP4+ 6PE services, BGP L3VPN services, BGP L3VPNv6 services, or EVPN services correctly.
* Configure an IP prefix list and a tunnel policy if you want to restrict the route to be recursed to the specified SR-MPLS TE Policy.

#### Procedure

1. Configure a tunnel policy.
   
   
   
   The tunnel policy can be implemented by means of tunnel type prioritizing (configured using the [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) command) or tunnel binding (configured using the [**tunnel binding**](cmdqueryname=tunnel+binding) command). You can select only one of these modes.
   
   
   
   Use either of the following procedures based on the traffic steering mode you select:
   
   
   
   * Color-based traffic steering
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Color-based traffic steering only steers traffic into an SR-MPLS TE Policy. In this case, only the tunnel type prioritizing mode is supported.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
        
        A tunnel policy is created and the tunnel policy view is displayed.
     3. (Optional) Run [**description**](cmdqueryname=description) *description-information*
        
        A description is configured for the tunnel policy.
     4. Run [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **sr-te-policy** **load-balance-number** *load-balance-number* **unmix**
        
        The tunnel selection sequence and the number of tunnels used for load balancing are configured.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     6. Run [**quit**](cmdqueryname=quit)
        
        Exit the tunnel policy view.
   * DSCP-based traffic steering
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     DSCP-based traffic steering steers traffic only to an SR-MPLS TE Policy group. In this case, only the tunnel binding mode is supported.
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**segment-routing**](cmdqueryname=segment-routing)
        
        The Segment Routing view is displayed.
     3. Run [**sr-te-policy group**](cmdqueryname=sr-te-policy+group) *group-value*
        
        An SR-MPLS TE Policy group is created, and its view is displayed.
     4. Run [**endpoint**](cmdqueryname=endpoint) *ipv4-address*
        
        An endpoint is configured for the SR-MPLS TE Policy group.
     5. Run [**color**](cmdqueryname=color) *color-value* **match** **dscp** { **ipv4** | **ipv6** } { { *dscp-value1* [ **to** *dscp-value2* ] } &<1-64> | **default** }
        
        The mapping between the color values of SR-MPLS TE Policies in an SR-MPLS TE Policy group and the DSCP values of packets is configured.
        
        Each SR-MPLS TE Policy in an SR-MPLS TE Policy group has its own color attribute. You can run the [**color match dscp**](cmdqueryname=color+match+dscp) command to configure the mapping between color and DSCP values, thereby associating DSCP values, color values, and SR-MPLS TE Policies in an SR-MPLS TE Policy group. IP packets can then be steered into the specified SR-MPLS TE Policy based on their DSCP values.
        
        When using the [**color match dscp**](cmdqueryname=color+match+dscp) command, pay attention to the following points:
        1. You can configure a separate color-DSCP mapping for both the IPv4 address family and IPv6 address family. In the same address family (IPv4/IPv6), each DSCP value can be associated with only one SR-MPLS TE Policy. Furthermore, the association can be performed for an SR-MPLS TE Policy only if this policy is up.
        2. The [**color**](cmdqueryname=color) *color-value* **match** **dscp** { **ipv4** | **ipv6** } **default** command can be used to specify a default SR-MPLS TE Policy in an address family (IPv4/IPv6). If a DSCP value is not associated with any SR-MPLS TE Policy in an SR-MPLS TE Policy group, the packets carrying this DSCP value are forwarded over the default SR-MPLS TE Policy. Each address family (IPv4/IPv6) in an SR-MPLS TE Policy group can have only one default SR-MPLS TE Policy.
        3. In scenarios where no default SR-MPLS TE Policy is specified for an address family (IPv4/IPv6) in an SR-MPLS TE Policy group:
           1. If the mapping between color and DSCP values is configured for the group but only some of the DSCP values are associated with SR-MPLS TE Policies, the packets carrying DSCP values that are not associated with SR-MPLS TE Policies are forwarded over the SR-MPLS TE Policy associated with the smallest DSCP value in the address family.
           2. If no DSCP value is associated with an SR-MPLS TE Policy in the group (for example, the mapping between color and DSCP values is not configured, or DSCP values are not successfully associated with SR-MPLS TE Policies after the mapping is configured), the default SR-MPLS TE Policy in the other address family (IPv4/IPv6) is used to forward packets. If no default SR-MPLS TE Policy is specified for the other address family, packets are forwarded over the SR-MPLS TE Policy associated with the smallest DSCP value in the local address family.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the SR-MPLS TE Policy group view.
     7. Run [**quit**](cmdqueryname=quit)
        
        Return to the SR view.
     8. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     9. Run [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name*
        
        A tunnel policy is created and the tunnel policy view is displayed.
     10. (Optional) Run [**description**](cmdqueryname=description) *description-information*
         
         A description is configured for the tunnel policy.
     11. Run [**tunnel binding**](cmdqueryname=tunnel+binding) **destination** *dest-ip-address* **sr-te-policy group** *sr-te-policy-group-id* [ **ignore-destination-check** ] [ **down-switch** ]
         
         A tunnel binding policy is configured to bind the specified destination address and SR-MPLS TE Policy group.
         
         The **ignore-destination-check** keyword is used to disable the function to check the consistency between the destination address specified using **destination** *dest-ip-address* and the endpoint of the corresponding SR-MPLS TE Policy.
     12. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
     13. Run [**quit**](cmdqueryname=quit)
         
         Exit the tunnel policy view.
2. Configure recursion to an SR-MPLS TE Policy.
   * Configure a non-labeled public BGP route to recurse to an SR-MPLS TE Policy.
     
     For detailed BGP configurations, see [Configuring Basic BGP Functions](dc_vrp_bgp_cfg_3004.html).
     
     1. Run [**route recursive-lookup tunnel**](cmdqueryname=route+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ]
        
        The function to recurse a non-labeled public route to an SR-MPLS TE Policy is enabled.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a static route to recurse to an SR-MPLS TE Policy.
     
     For detailed static route configurations, see [Configuring IPv4 Static Routes](dc_vrp_static-route_disjoin_cfg_0003.html).
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The color attribute cannot be added to static routes. Therefore, static routes support only DSCP-based traffic steering to SR-MPLS TE Policies, not color-based traffic steering to SR-MPLS TE Policies.
     
     1. Run [**ip route-static recursive-lookup tunnel**](cmdqueryname=ip+route-static+recursive-lookup+tunnel) [ **ip-prefix** *ip-prefix-name* ] [ **tunnel-policy** *policy-name* ]
        
        The function to recurse a static route to an SR-MPLS TE Policy for MPLS forwarding is enabled.
     2. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a BGP L3VPN service to recurse to an SR-MPLS TE Policy.
     
     For detailed BGP L3VPN configurations, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family)
        
        The VPN instance IPv4 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the VPN instance IPv4 address family.
     4. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the L3VPN service to recurse to an SR-MPLS TE Policy. If a remote VPN route without carrying the color extended community is leaked to a local VPN instance, the default color value is used for the recursion to an SR-MPLS TE Policy.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a BGP L3VPNv6 service to recurse to an SR-MPLS TE Policy.
     
     For detailed BGP L3VPNv6 configurations, see [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
     
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the VPN instance IPv6 address family.
     4. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the L3VPNv6 service to recurse to an SR-MPLS TE Policy. If a remote VPN route without carrying the color extended community is leaked to a local VPN instance, the default color value is used for the recursion to an SR-MPLS TE Policy.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure a BGP4+ 6PE service to recurse to an SR-MPLS TE Policy.
     
     For detailed BGP4+ 6PE configurations, see [Configuring BGP4+ 6PE](dc_vrp_bgp6_cfg_0056.html).
     
     1. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain* | *as-number-dot* }
        
        The BGP view is displayed.
     2. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
        
        The BGP IPv6 unicast address family view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
        
        A 6PE peer is enabled.
     4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **tnl-policy** *tnl-policy-name*
        
        A tunnel policy is applied to the 6PE peer.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Configure an EVPN service to recurse to an SR-MPLS TE Policy.
     
     For detailed EVPN configurations, see [Configuring EVPN VPLS over MPLS (BD EVPN Instance)](dc_vrp_evpn_cfg_0065.html).
     
     To apply a tunnel policy to an EVPN L3VPN instance, perform the following steps:
     1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     2. Run [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family)
        
        The VPN instance IPv4/IPv6 address family view is displayed.
     3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
        
        A tunnel policy is applied to the EVPN L3VPN instance.
     4. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value* **evpn**
        
        The default color value is specified for the EVPN L3VPN service to recurse to an SR-MPLS TE Policy.
        
        If a remote EVPN route without carrying the color extended community is leaked to a local VPN instance, the default color value is used for the recursion to an SR-MPLS TE Policy.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to a BD EVPN instance, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
        
        The BD EVPN instance view is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the BD EVPN instance.
     3. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the EVPN service to recurse to an SR-MPLS TE Policy. If a remote EVPN route without carrying the color extended community is leaked to a local EVPN instance, the default color value is used for the recursion to an SR-MPLS TE Policy.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to an EVPN instance that works in EVPN VPWS mode, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
        
        The view of the EVPN instance that works in EVPN VPWS mode is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the EVPN instance that works in EVPN VPWS mode.
     3. (Optional) Run [**default-color**](cmdqueryname=default-color) *color-value*
        
        The default color value is specified for the EVPN service to recurse to an SR-MPLS TE Policy. If a remote EVPN route without carrying the color extended community is leaked to a local EVPN instance, the default color value is used for the recursion to an SR-MPLS TE Policy.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     To apply a tunnel policy to a basic EVPN instance, perform the following steps:
     1. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name*
        
        The EVPN instance view is displayed.
     2. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
        
        A tunnel policy is applied to the basic EVPN instance.
     3. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.