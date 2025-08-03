(Optional) Configuring IPv4 Address Pool Route Leaking
======================================================

This section describes how to configure a VPN import policy for address pool subnet routes in order to achieve VPN-based automatic IPv4 address pool route leaking.

#### Context

If the BAS user side and network side belong to different VPNs, you can configure the policy of VPN-based automatic address pool route leaking so that the address pool subnet routes in the user-side VPN can be imported to the network-side VPN. In this case, the interfaces in the network-side VPN routing table belong to the user-side VPN. This configuration retains the flexibility of static routes and optimizes the configuration synchronization of the static routes that are updated in an address pool subnet or VPN.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ip unr net-route import source vpn-instance**](cmdqueryname=ip+unr+net-route+import+source+vpn-instance) *vpn-instance-name* **destination vpn-instance** *vpn-instance-name* command to configure the device to automatically import the address pool subnet routes from the source VPN to the destination VPN.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.