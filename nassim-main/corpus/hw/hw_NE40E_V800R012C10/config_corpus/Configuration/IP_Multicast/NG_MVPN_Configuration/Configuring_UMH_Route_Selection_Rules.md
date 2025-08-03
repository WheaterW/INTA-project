Configuring UMH Route Selection Rules
=====================================

This section describes how to configure upstream multicast hop (UMH) route selection rules on receiver PEs on an NG MVPN, so that the receiver PEs can select the same sender PE as their root node during VPN route selection.

#### Context

On an NG MVPN, when multiple sender PEs exist, receiver PEs select routes based on preferred unicast routes by default. In this case, different receiver PEs select different sender PEs as their root nodes. This requires multiple P2MP tunnels to be established. As a result, many public network tunnel resources are consumed. To resolve the preceding issue, enable the highest IP address to be selected as the UMH on receiver PEs, so that the receiver PEs select the same sender PE as their root node during VPN route selection.

Perform the following steps in the VPN instance MVPN view of a PE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
   
   
   
   The VPN instance view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
   
   
   
   The VPN instance IPv4 address family view is displayed.
4. Run [**mvpn**](cmdqueryname=mvpn)
   
   
   
   The VPN instance IPv4 address family MVPN view is displayed.
5. Run [**umh-select highest-ip**](cmdqueryname=umh-select+highest-ip)
   
   
   
   The maximum IP address is selected as the UMH in an MVPN instance.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.