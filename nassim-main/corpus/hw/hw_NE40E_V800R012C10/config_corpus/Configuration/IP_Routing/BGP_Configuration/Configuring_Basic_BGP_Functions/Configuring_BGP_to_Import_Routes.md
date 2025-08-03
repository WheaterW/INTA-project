Configuring BGP to Import Routes
================================

BGP can import the routes from other routing protocols. When routes are imported from dynamic routing protocols, the process IDs of the routing protocols must be specified. Importing routes from other protocols can enrich the BGP routing table. When importing IGP routes, BGP can filter the routes by routing protocol.

#### Context

BGP itself cannot discover routes. It needs to import routes from other protocols (such as IGPs) to the BGP routing table so that the routes can be transmitted within an AS or between ASs. When importing routes, BGP can filter these routes by routing protocol.

BGP imports routes in the following modes:

* Import mode: BGP imports routes into its routing table by protocol type, such as RIP, OSPF, IS-IS, static routes, or direct routes.
* Network mode: BGP imports a route with the specified prefix and mask. This mode is more precise than the Import mode.

#### Procedure

* Import mode
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**import-route**](cmdqueryname=import-route+isis+ospf+rip+direct++static+med+route-policy) { **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **direct** |**static** | **unr** } [ [ **med** *med* ] | [ **route-policy** *route-policy-name* ] | [ **route-filter** *route-filter-name* ] ] \* [ **non-relay-tunnel** ]
     
     
     
     BGP is configured to import routes from another protocol.
     
     
     
     To set an MED value for the imported routes, specify the *med* parameter. An EBGP peer selects the route with the lowest MED value to guide traffic entering the AS where the peer resides.
     
     To filter the routes imported from another protocol, you can specify the **route-policy** *route-policy-name* parameter.
     
     To filter the routes imported from another protocol, you can also specify the **route-filter** *route-filter-name* parameter.
     
     If **non-relay-tunnel** is specified, the routes imported by BGP do not recurse to tunnels. Generally, the routes imported by BGP can be recursed to tunnels. However, in some scenarios, if the routes imported by BGP are recursed to tunnels, problems may occur. For example, in a seamless MPLS scenario, egress protection is configured between egress MASGs, and a tunnel exists between the MASGs. If a BGP route imported by an MASG is recursed to the tunnel, the label action is not popping out but stitching tunnels. Consequently, traffic is diverted to the peer MASG, which prolongs the traffic switching time. As a result, egress protection fails to take effect. To solve this problem, specify the **non-relay-tunnel** parameter to prevent the routes imported by BGP from being recursed to tunnels. This prevents egress protection from becoming invalid due to tunnel stitching.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring the device to import the routes discovered by a dynamic routing protocol, such as OSPF, RIP,  or IS-IS, specify the process ID of the protocol.
     
     In a BAS device access scenario, to prevent BGP from importing the UNRs that cannot be advertised, run the [**access no-advertise-unr import disable**](cmdqueryname=access+no-advertise-unr+import+disable) command.
  5. (Optional) Run [**default-route imported**](cmdqueryname=default-route+imported)
     
     
     
     BGP is allowed to import default routes from the local IP routing table. BGP can import default routes only when both the [**default-route imported**](cmdqueryname=default-route+imported) and [**import-route**](cmdqueryname=import-route) commands have been run. Using only the [**import-route**](cmdqueryname=import-route) command cannot import default routes, and using only the [**default-route imported**](cmdqueryname=default-route+imported) command imports only the default routes that exist in the local routing table.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Network mode
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**network**](cmdqueryname=network+route-policy) *ipv4-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ **non-relay-tunnel** ]
     
     
     
     BGP is configured to import local routes.
     
     
     
     If no mask or mask length is specified, the address is processed as a classful address. The local routes to be imported must exist in the local IP routing table.
     
     To use a route-policy to filter the routes to be imported, specify the **route-policy** *route-policy-name* parameter.
     
     To use a route-filter to filter the routes to be imported, specify the **route-filter** *route-filter-name* parameter.
     
     If **non-relay-tunnel** is specified, the routes imported by BGP do not recurse to tunnels. Generally, the routes imported by BGP can be recursed to tunnels. However, in some scenarios, if the routes imported by BGP are recursed to tunnels, problems may occur. For example, in a seamless MPLS scenario, egress protection is configured between egress MASGs, and a tunnel exists between the MASGs. If a BGP route imported by an MASG is recursed to the tunnel, the label action is not popping out but stitching tunnels. Consequently, traffic is diverted to the peer MASG, which prolongs the traffic switching time. As a result, egress protection fails to take effect. To solve this problem, specify the **non-relay-tunnel** parameter to prevent the routes imported by BGP from being recursed to tunnels. This prevents egress protection from becoming invalid due to tunnel stitching.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The specified route can be imported only when the destination address and mask specified in the [**network**](cmdqueryname=network) command are the same as those in the corresponding entry in the local IP routing table.
     + When using the [**undo network**](cmdqueryname=undo+network) command to clear the existing configuration, specify the correct mask.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.