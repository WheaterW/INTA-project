(Optional) Enabling a Device to Recurse IPv6 Static Routes to ND Vlink Direct Routes
====================================================================================

To prevent blackhole routes from being generated in a scenario where a Layer 2 network accesses a Layer 3 network, you can enable a device to recurse IPv6 static routes to ND Vlink direct routes.

#### Context

In a scenario where a Layer 2 network accesses a Layer 3 network, you can enable a device to recurse IPv6 static routes to ND Vlink direct routes. This prevents blackhole routes from being generated.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 route recursive-lookup nd vlink-direct-route protocol static**](cmdqueryname=ipv6+route+recursive-lookup+nd+vlink-direct-route+protocol+static)
   
   
   
   The device is configured to recurse IPv6 static routes to ND Vlink direct routes.
   
   
   
   The [**ipv6 route recursive-lookup nd vlink-direct-route protocol static**](cmdqueryname=ipv6+route+recursive-lookup+nd+vlink-direct-route+protocol+static) command is mainly used in scenarios where Layer 2 accesses Layer 3. To allow IPv6 static routes to recurse only to ND Vlink direct routes, run the [**ipv6 route-static**](cmdqueryname=ipv6+route-static) command with the **recursive-lookup** **host-route** parameter specified in addition to running the [**ipv6 route recursive-lookup nd vlink-direct-route protocol static**](cmdqueryname=ipv6+route+recursive-lookup+nd+vlink-direct-route+protocol+static) command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.