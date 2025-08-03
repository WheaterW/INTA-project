Configuring RIPng to Import External Routes
===========================================

Configuring RIPng to Import External Routes

#### Context

You can accurately control the sending and receiving of RIPng messages to meet the requirements of complex networks.

On a large-scale network, multiple routing protocols can be configured for devices in different areas. In this scenario, RIPng devices must be configured to import routing information learned from a non-RIPng routing protocol.

If RIPng is required to advertise the routing information of other RIPng processes or other routing protocols (such as direct, static, OSPFv3, IS-IS, or BGP), you can specify the *protocol* parameter to filter this routing information. If *protocol* is not specified, all routes, including the imported routes and local RIPng routes (direct routes), are filtered.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIPng process and enter the RIPng view.
   
   
   ```
   [ripng](cmdqueryname=ripng) [ process-id ]
   ```
3. (Optional) Configure the default metric for imported routes.
   
   
   ```
   [default-cost](cmdqueryname=default-cost) cost
   ```
   
   
   
   If no metric is specified for external routes, the default metric value of 0 takes effect.
4. Import external routes.
   
   
   * To import direct routes, static routes, IS-IS routes, OSPF routes, or routes of another RIPng process, run the following command:
     ```
     [import-route](cmdqueryname=import-route) { static | direct | bgp | { isis | ospfv3 | ripng } [ process-id ] } [ [ cost cost | inherit-cost ] | route-policy route-policy-name  ] *
     ```
   * To import IBGP routes, run the following command:
     ```
     [import-route](cmdqueryname=import-route) bgp permit-ibgp [ [ cost cost | inherit-cost ] | route-policy route-policy-name  ] * 
     ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```