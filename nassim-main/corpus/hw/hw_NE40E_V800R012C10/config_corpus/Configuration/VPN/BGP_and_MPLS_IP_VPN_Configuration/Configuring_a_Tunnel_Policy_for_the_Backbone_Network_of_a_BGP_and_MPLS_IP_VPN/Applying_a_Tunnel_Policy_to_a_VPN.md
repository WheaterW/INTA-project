Applying a Tunnel Policy to a VPN
=================================

This section describes how to apply a tunnel policy to a VPN to change the tunnel used to carry VPN services or the sequence in which tunnels are selected for VPN services.

#### Procedure

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