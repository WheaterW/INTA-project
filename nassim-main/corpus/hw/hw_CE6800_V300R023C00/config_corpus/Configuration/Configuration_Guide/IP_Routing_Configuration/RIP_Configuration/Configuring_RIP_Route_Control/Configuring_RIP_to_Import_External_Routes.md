Configuring RIP to Import External Routes
=========================================

Configuring RIP to Import External Routes

#### Context

On a large-scale network, different routing protocols may be configured for devices in different areas. In such a situation, configure RIP to import routes from other processes or other routing protocols.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. (Optional) Set the cost for imported routes.
   
   
   ```
   [default-cost](cmdqueryname=default-cost) cost
   ```
   
   
   
   If the cost for importing external routes is not specified, the default value of 0 takes effect.
4. Import external routes.
   
   
   * To import direct routes, static routes, IS-IS routes, OSPF routes, or routes of another RIP process, run the following command:
     ```
     [import-route](cmdqueryname=import-route) { static | direct | bgp | { isis | ospf | rip } [ process-id ] } [ cost cost | route-policy route-policy-name  ] *
     ```
   * To import IBGP routes, run the following command:
     ```
     [import-route](cmdqueryname=import-route) bgp permit-ibgp [ cost cost | route-policy route-policy-name  ] * or [import-route](cmdqueryname=import-route) bgp [ permit-ibgp ] { cost transparent route-policy route-policy-name  | route-policy route-policy-name  cost transparent | cost transparent }
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   Importing routes from other protocols to a RIP process may lead to routing loops. Therefore, exercise caution when running the [**import-route**](cmdqueryname=import-route) command.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```