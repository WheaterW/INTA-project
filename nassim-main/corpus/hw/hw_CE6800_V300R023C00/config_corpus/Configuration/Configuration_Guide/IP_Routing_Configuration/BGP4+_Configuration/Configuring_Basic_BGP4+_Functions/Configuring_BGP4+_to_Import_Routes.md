Configuring BGP4+ to Import Routes
==================================

Configuring BGP4+ to Import Routes

#### Context

BGP4+ itself cannot discover routes. It needs to import routes from other protocols (such as static routes or OSPFv3 routes) to the BGP4+ routing table so that they can be transmitted within an AS or between ASs.

BGP4+ can import routes in either Import or Network mode.

* Import mode: BGP4+ imports routes by protocol type, such as RIPng, OSPFv3, IPv6 IS-IS, static routes, and direct routes.
* Network mode: BGP4+ imports a route with the specified prefix and mask to the BGP4+ routing table. Network mode is more precise than Import mode.

#### Procedure

* Import mode
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the BGP-IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  4. Configure BGP4+ to import routes from another routing protocol.
     
     
     ```
     [import-route](cmdqueryname=import-route+direct+isis+ospfv3+ripng+static+med+route-policy) { direct | isis process-id | ospfv3 process-id | ripng process-id | static } [ med med | route-policy route-policy-name ] *
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     When configuring route import from IPv6 IS-IS, OSPFv3, or RIPng, specify the process ID of the corresponding protocol.
  5. (Optional) Enable BGP4+ to import default routes.
     
     
     ```
     [default-route imported](cmdqueryname=default-route+imported)
     ```
     
     Default routes can be imported only if both the [**default-route imported**](cmdqueryname=default-route+imported) and [**import-route**](cmdqueryname=import-route) commands are run. Using only the [**import-route**](cmdqueryname=import-route) command cannot import default routes, and using only the [**default-route imported**](cmdqueryname=default-route+imported) command imports the default routes that exist in the local routing table.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Network mode
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the BGP-IPv6 unicast address family view.
     
     
     ```
     [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
     ```
  4. Configure the device to import local IPv6 routes.
     
     
     ```
     [network](cmdqueryname=network+route-policy) ipv6-address prefix-length [ route-policy route-policy-name ]
     ```
     
     If no mask or mask length is specified, the address is processed as a classful address.
     
     The local routes to be advertised must exist in the local IPv6 routing table.
     
     You can specify the **route-policy** *route-policy-name* parameter to filter the routes imported from another protocol.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + The destination address and mask specified in the [**network**](cmdqueryname=network) command must be consistent with those in the corresponding entry in the local IPv6 routing table. Otherwise, the specified route will not be advertised.
     + When using the [**undo network**](cmdqueryname=undo+network) command to clear the existing configuration, specify the correct mask.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```