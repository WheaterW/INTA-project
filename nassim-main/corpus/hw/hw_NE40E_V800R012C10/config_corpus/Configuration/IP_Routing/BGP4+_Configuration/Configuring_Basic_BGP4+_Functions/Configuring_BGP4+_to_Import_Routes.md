Configuring BGP4+ to Import Routes
==================================

BGP4+ can import routes from other protocols. When routes are imported from dynamic routing protocols, the process IDs of the routing protocols must be specified. Importing routes from other protocols can enrich the BGP4+ routing table. When importing IGP routes, BGP4+ can filter the routes by routing protocol.

#### Context

BGP4+ cannot discover routes by itself. Instead, it imports routes discovered by other protocols such as OSPFv3 or static routes to the BGP4+ routing table. These imported routes are then transmitted within an AS or between ASs. When importing routes, BGP4+ can filter these routes by routing protocol.

BGP4+ can import routes in either Import or Network mode.

* Import mode: BGP4+ imports routes into its routing table by protocol type, such as RIP, OSPF, IS-IS, static routes, or direct routes.
* Network mode: BGP4+ imports a route with the specified prefix and mask. This mode is more precise than the Import mode.

#### Procedure

* Import mode
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The BGP-IPv6 unicast address family view is displayed.
  4. Run [**import-route**](cmdqueryname=import-route) { **direct** | **static** | **unr** | { **ospfv3**| **isis** | **ripng** } *process-id* } [ [ **med** *med* ] | [ [ **route-policy** *route-policy-name* ] | [ **route-filter** *route-filter-name* ] ] ] \*
     
     
     
     BGP4+ is configured to import routes from another protocol.
     
     
     
     To filter the routes imported from another protocol, you can specify the **route-policy** *route-policy-name* parameter.
     
     To filter the routes imported from another protocol, you can also specify the **route-filter** *route-filter-name* parameter.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To import IS-IS, OSPF, or RIP routes, the process ID of the corresponding routing protocol needs to be specified.
     
     In a BAS device access scenario, to prevent BGP from importing the UNRs that cannot be advertised, run the [**access no-advertise-unr import disable**](cmdqueryname=access+no-advertise-unr+import+disable) command.
  5. Run [**default-route imported**](cmdqueryname=default-route+imported)
     
     
     
     BGP4+ is configured to import default routes. Default routes can be imported only if both the [**default-route imported**](cmdqueryname=default-route+imported) and [**import-route**](cmdqueryname=import-route) commands are run. Using only the [**import-route**](cmdqueryname=import-route) command cannot import default routes, and using only the [**default-route imported**](cmdqueryname=default-route+imported) command imports the default routes that exist in the local routing table.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Network mode
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The BGP-IPv6 unicast address family view is displayed.
  4. Run [**network**](cmdqueryname=network) *ipv6-address* *prefix-length* [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
     
     
     
     The device is configured to advertise local IPv6 routes.
     
     
     
     If no mask or mask length is specified, the address is processed as a classful address.
     
     The local routes to be advertised must exist in the local IP routing table.
     
     To use a route-policy to filter the routes to be imported, specify the **route-policy** *route-policy-name* parameter.
     
     To filter the routes imported from another protocol, you can also specify the **route-filter** *route-filter-name* parameter.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The destination address and mask specified in the [**network**](cmdqueryname=network) command must be consistent with those in the corresponding entry in the local IP routing table. Otherwise, the specified route will not be advertised.
     
     When using the [**undo network**](cmdqueryname=undo+network) command to clear the existing configuration, specify the correct mask.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.