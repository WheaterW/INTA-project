Configuring IPv4 Static Routes
==============================

On a network, you can control route selection by configuring IPv4 Static Routes.

#### Usage Scenario

IPv4 static routes can be configured for a network with simple structure to achieve connectivity.

The NE40E supports common static routes and those associated with VPN instances. The static routes associated with VPN instances are used to manage VPN routes. For details about VPN instances, see the *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN*.


#### Pre-configuration Tasks

Before configuring IPv4 Static Routes, configure parameters of the link layer protocol and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.


[Creating IPv4 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0004.html)

To create an IPv4 static route, configure its destination address, outbound interface, and next hop.

[(Optional) Setting the Default Priority for IPv4 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0005.html)

You can change the default priority for IPv4 static routes.

[(Optional) Configuring Recursion Depth-based Static Route Selection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0006.html)

To prevent inter-board service transmission or routing loop in a static route scenario, configure recursion depth-based static route selection.

[(Optional) Enabling a Device to Recurse Static Routes to ARP Vlink Direct Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0052.html)

To prevent blackhole routes from being generated when a Layer 2 network accesses a Layer 3 network, configure the device to recurse static routes to ARP Vlink direct routes.

[(Optional) Configuring a Device to Recurse Static Routes to SRv6 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0063.html)

In L3VPNv4 HoVPN over SRv6 BE, L3VPNv4 HoVPN over SRv6 TE Policy, EVPN L3VPN HoVPN over SRv6 BE, or EVPN L3VPN HoVPN over SRv6 TE Policy scenarios, you can configure a device to recurse static routes to SRv6 routes to prevent traffic black holes. 

[(Optional) Preventing an IPv4 Static Route from Being Selected If the BFD Session Associated with It Is in the AdminDown State](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0053.html)

This section describes how to configure the Router not to select an IPv4 static route if the BFD session associated with it is in the AdminDown state. This ensures that Huawei devices can interwork with non-Huawei devices.

[Verifying the IPv4 Static Route Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0007.html)

After configuring an IPv4 static route, verify the configuration.