(Optional) Configuring IPv6 Address Pool Route Leaking
======================================================

This section describes how to configure a VPN import policy for address pool subnet routes in order to achieve VPN-based automatic leaking of IPv6 address pool routes.

#### Context

If the BAS user side and network side belong to different VPNs, you can configure the policy of VPN-based automatic address pool route leaking so that the address pool subnet routes in the user-side VPN can be imported to the network-side VPN. In this case, the interfaces in the network-side VPN routing table reside in the user-side VPN. Compared with static route configuration, configuring the automatic route leaking function reduces the inconvenience brought by updating configurations when the address pool subnet or VPN is updated.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ipv6 unr net-route import source vpn-instance**](cmdqueryname=ipv6+unr+net-route+import+source+vpn-instance) *vpn-instance-name* **destination vpn-instance** *vpn-instance-name* command to configure the device to automatically import the address pool subnet routes from the source VPN to the destination VPN.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.