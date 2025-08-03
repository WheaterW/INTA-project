Applying a Tunnel Policy to an IPv6 VPN
=======================================

This section describes how to apply a tunnel policy to an IPv6 VPN to change the tunnel used to carry VPN services or the tunnel selection sequence for VPN services.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family)
   
   
   
   The VPN instance IPv6 address family view is displayed.
   
   A VPN instance supports both the IPv4 address family and IPv6 address family. VPN configurations can be performed only if an IPv4 or IPv6 address family (which is determined by the forwarding route type) has been enabled for the VPN instance.
4. Run [**tnl-policy**](cmdqueryname=tnl-policy) *policy-name*
   
   
   
   A tunnel policy is applied to the VPN instance IPv6 address family.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.