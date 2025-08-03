Applying a Tunnel Policy to Services
====================================

After configuring a traffic steering policy, you can apply a tunnel policy to specified services for them to recurse to an SRv6 TE Policy.

#### Context

After an SRv6 TE Policy is configured, traffic needs to be steered into the SRv6 TE Policy for forwarding. This process is called traffic steering. Currently, SRv6 TE Policies can be used for various services, such as BGP L3VPN and EVPN services. This section describes how to apply a tunnel policy to allow services to recurse to an SRv6 TE Policy.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

EVPN VPWS and EVPN VPLS services do not support DSCP-based traffic steering.



#### Procedure

1. Configure BGP L3VPNv4 service recursion to an SRv6 TE Policy.
   
   
   
   For details about how to configure BGP L3VPNv4, see [Configuring a Basic BGP/MPLS IP VPN](dc_vrp_mpls-l3vpn-v4_cfg_0154.html).
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      The VPN instance view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      The VPN instance IPv4 address family view is displayed.
   4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
      
      A tunnel policy is applied to the VPN instance IPv4 address family.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
2. Configure BGP L3VPNv6 service recursion to an SRv6 TE Policy.
   
   
   
   For details about how to configure BGP L3VPNv6, see [Configuring a Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2057.html).
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      The VPN instance view is displayed.
   3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
      
      The VPN instance IPv6 address family view is displayed.
   4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
      
      The specified tunnel policy is applied to the VPN instance IPv6 address family.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
3. Configure EVPN service recursion to an SRv6 TE Policy.
   
   To apply a tunnel policy to an EVPN L3VPN instance, perform the following steps:
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      The VPN instance view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family) or [**ipv6-family**](cmdqueryname=ipv6-family)
      
      The VPN instance IPv4 or IPv6 address family view is displayed.
   4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name* **evpn**
      
      A tunnel policy is applied to the EVPN L3VPN instance.
   5. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
   To apply a tunnel policy to a BD EVPN instance, perform the following steps:
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
      
      The BD EVPN instance view is displayed.
   3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
      
      A tunnel policy is applied to the BD EVPN instance.
   4. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
   To apply a tunnel policy to an EVPN instance that works in EVPN VPWS mode, perform the following steps:
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **vpws**
      
      The view of the EVPN instance that works in EVPN VPWS mode is displayed.
   3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
      
      A tunnel policy is applied to the EVPN instance that works in EVPN VPWS mode.
   4. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
   
   To apply a tunnel policy to a basic EVPN instance, perform the following steps:
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name*
      
      The basic EVPN instance view is displayed.
   3. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
      
      A tunnel policy is applied to the basic EVPN instance.
   4. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
4. Configure public network IPv4 service recursion to an SRv6 TE Policy.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**tunnel-selector**](cmdqueryname=tunnel-selector)*name* *matchMode* **node** *node*
      
      A tunnel selector is created, and its view is displayed.
   3. Run [**apply tunnel-policy**](cmdqueryname=apply+tunnel-policy)*tunnel-policy-name*
      
      A tunnel policy is applied to the tunnel selector.
   4. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   5. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   6. Run [**ipv4-family**](cmdqueryname=ipv6-family+unicast) **unicast**
      
      The IPv4 unicast address family view is displayed.
   7. Run [**unicast-route recursive-lookup tunnel-v6 tunnel-selector**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v6+tunnel-selector)*tunnel-selector-name*
      
      The device is enabled to recurse IPv4 unicast routes received from a BGP IPv6 peer to tunnels.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.
5. Configure public network IPv6 service recursion to an SRv6 TE Policy.
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**tunnel-selector**](cmdqueryname=tunnel-selector)*name* *matchMode* **node** *node*
      
      A tunnel selector is created, and its view is displayed.
   3. Run [**apply tunnel-policy**](cmdqueryname=apply+tunnel-policy)*tunnel-policy-name*
      
      A tunnel policy is applied to the tunnel selector.
   4. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   5. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      The BGP view is displayed.
   6. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
      
      The IPv6 unicast address family view is displayed.
   7. Run [**unicast-route recursive-lookup tunnel-v6 tunnel-selector**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v6+tunnel-selector)*tunnel-selector-name*
      
      The device is enabled to recurse IPv6 unicast routes received from a BGP IPv6 peer to tunnels.
   8. Run [**commit**](cmdqueryname=commit)
      
      The configuration is committed.