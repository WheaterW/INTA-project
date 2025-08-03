(Optional) Enabling a Device to Recurse Static Routes to ARP Vlink Direct Routes
================================================================================

To prevent blackhole routes from being generated when a Layer 2 network accesses a Layer 3 network, configure the device to recurse static routes to ARP Vlink direct routes.

#### Context

In a scenario where a Layer 2 network accesses a Layer 3 network, you can enable a device to recurse static routes to ARP Vlink direct routes. This prevents blackhole routes from being generated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip route recursive-lookup arp vlink-direct-route protocol static**](cmdqueryname=ip+route+recursive-lookup+arp+vlink-direct-route+protocol+static)
   
   
   
   The device is configured to recurse static routes to ARP Vlink direct routes.
   
   
   
   In a scenario where a
   Layer 2 VPN accesses a Layer 3 VPN, to configure a device to recurse
   static routes to ARP Vlink routes, run the [**ip route-static**](cmdqueryname=ip+route-static) command with **recursive-lookup** **host-route** specified and **ip route
   recursive-lookup arp vlink-direct-route protocol static**.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.