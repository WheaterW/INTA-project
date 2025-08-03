Configuring BGP to Import Routes
================================

Configuring BGP to Import Routes

#### Context

BGP itself cannot discover routes. It needs to import routes from other protocols (such as IGP routes) to the BGP routing table so that they can be transmitted within an AS or between ASs.

BGP can import routes in either of the following modes:

* Import mode: BGP imports routes by protocol type, such as RIP, OSPF, IS-IS, static routes, and direct routes.
* Network mode: BGP imports a route with the specified prefix and mask. This mode is more precise than the Import mode.

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
  3. (Optional) Enter the BGP-IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
     
     By default, configurations performed in the BGP view take effect in the IPv4 unicast address family view.
  4. Configure BGP to import routes from another routing protocol.
     
     
     ```
     [import-route](cmdqueryname=import-route+direct+isis+ospf+rip+static+med+route-policy) { direct | isis process-id | ospf process-id | rip process-id | static } [ med med | route-policy route-policy-name ] *
     ```
     
     To set an MED value for the imported routes, specify the *med* parameter. An EBGP peer selects the route with the lowest MED value to guide traffic entering the AS where the peer resides.
     
     To filter the routes imported from a non-BGP protocol, specify the **route-policy** *route-policy-name* parameter.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     When configuring the device to import the routes discovered by a dynamic routing protocol, such as OSPF, RIP,  or IS-IS, specify the process ID of the protocol.
  5. (Optional) Enable BGP to import the existing default route from the local IP routing table.
     
     
     ```
     [default-route imported](cmdqueryname=default-route+imported)
     ```
     
     BGP can import default routes only if both the [**default-route imported**](cmdqueryname=default-route+imported) and [**import-route**](cmdqueryname=import-route) commands are run.
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
  3. (Optional) Enter the BGP-IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
     
     By default, the configuration is performed in the IPv4 unicast address family view.
  4. Configure BGP to import local routes.
     
     
     ```
     [network](cmdqueryname=network+route-policy) ipv4-address [ mask | mask-length ] [ route-policy route-policy-name ]
     ```
     
     If no mask or mask length is specified, the address is processed as a classful address. The local routes to be imported must exist in the local IP routing table.
     
     To use a route-policy to filter the routes to be imported, specify the **route-policy** *route-policy-name* parameter.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + The specified route can be imported only when the destination address and mask specified in the [**network**](cmdqueryname=network) command are the same as those in the corresponding entry in the local IP routing table.
     + When using the [**undo network**](cmdqueryname=undo+network) command to clear the existing configuration, specify the correct mask.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```