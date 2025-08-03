Configuring the Mapping Between the Color Extended Community Attribute and Flex-Algo
====================================================================================

Service routes can be associated with Flex-Algo-based SR-MPLS BE tunnels only after mappings between their color attributes and Flex-Algos are configured.

#### Context

After the mapping between the color attribute and Flex-Algo is created for a VPN route, the VPN route is recursed based on the corresponding tunnel policy. If the tunnel policy specifies a preferential use of Flex-Algo-based SR-MPLS BE tunnels, the VPN route is recursed to the target Flex-Algo-based SR-MPLS BE tunnel based on the next hop address and color attribute of the route; if the tunnel policy specifies a preferential use of common SR-MPLS tunnels, the VPN route is recursed to the target common SR-MPLS BE tunnel based on the next hop address of the route.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**flex-algo color-mapping**](cmdqueryname=flex-algo+color-mapping)
   
   
   
   The Flex-Algo-color mapping view is displayed.
3. Run [**color**](cmdqueryname=color) *index* **flex-algo** *flexAlgoId*
   
   
   
   The mapping between the color attribute and Flex-Algo is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.