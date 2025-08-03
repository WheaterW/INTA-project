Configuring IPv6 Static Routes
==============================

On a network, you can control route selection by configuring IPv6 static routes.

#### Usage Scenario

On a small IPv6 network, you can achieve network connectivity by configuring IPv6 static routes. Compared with the use of dynamic routing protocols, configuring static routes saves bandwidth resources.


#### Pre-configuration Tasks

Before configuring an IPv6 static route, configure link layer protocol parameters and IPv6 addresses for interfaces and ensure that the status of the link layer protocol of the interface is Up.


[Creating IPv6 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0009.html)

To create an IPv6 static route, configure its destination IP address, outbound interface, and next hop.

[(Optional) Setting the Default Priority for IPv6 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0010.html)

You can change default priority for IPv6 static routes.

[(Optional) Enabling a Device to Recurse IPv6 Static Routes to ND Vlink Direct Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0057.html)

To prevent blackhole routes from being generated in a scenario where a Layer 2 network accesses a Layer 3 network, you can enable a device to recurse IPv6 static routes to ND Vlink direct routes.

[(Optional) Enabling a Device to Recurse IPv6 Static Routes to SRv6 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0066.html)

In EVPN L3VPN HoVPN over SRv6 BE or EVPN L3VPN HoVPN over SRv6 TE Policy scenarios, you can configure a device to recurse static routes to SRv6 routes to prevent traffic black holes. 

[(Optional) Preventing an IPv6 Static Route from Being Selected If the BFD Session Associated with It Is in the AdminDown State](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0054.html)

This section describes how to configure the Router not to select an IPv6 static route if the BFD session associated with it is in the AdminDown state. This ensures that Huawei devices can interwork with non-Huawei devices.

[Verifying the IPv6 Static Route Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0011.html)

After configuring an IPv6 static route, verify the configuration.