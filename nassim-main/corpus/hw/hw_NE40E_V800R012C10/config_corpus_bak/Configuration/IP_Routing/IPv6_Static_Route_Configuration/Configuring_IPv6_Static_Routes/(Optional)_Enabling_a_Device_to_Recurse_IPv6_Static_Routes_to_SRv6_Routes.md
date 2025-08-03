(Optional) Enabling a Device to Recurse IPv6 Static Routes to SRv6 Routes
=========================================================================

In EVPN L3VPN HoVPN over SRv6 BE or EVPN L3VPN HoVPN over SRv6 TE Policy scenarios, you can configure a device to recurse static routes to SRv6 routes to prevent traffic black holes.

#### Context

In an EVPN L3VPN HoVPN over SRv6 BE or EVPN L3VPN HoVPN over SRv6 TE Policy scenario, if the next hop of a default route on an SPE is the SPE itself and the link between the SPE and the corresponding NPE fails, the UPE cannot detect the link fault. As a result, a traffic black hole occurs after traffic reaches the SPE. To resolve this problem, you need to specify the NPE's address (public or private) as the next-hop address of the default static route on the SPE. In this manner, the validity of the static route depends on whether the link between the SPE and NPE is available. In addition, you need to enable the SPE to recurse static routes to SRv6 routes. This configuration allows the SPE to withdraw this inactive route when the SPE-NPE link fails so that the UPE can detect the route withdrawal and no longer sends traffic to the SPE, thereby preventing a traffic black hole.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 route-static recursive-lookup inherit-label-route segment-routing-ipv6**](cmdqueryname=ipv6+route-static+recursive-lookup+inherit-label-route+segment-routing-ipv6)
   
   
   
   The device is enabled to recurse IPv6 static routes to SRv6 routes.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.