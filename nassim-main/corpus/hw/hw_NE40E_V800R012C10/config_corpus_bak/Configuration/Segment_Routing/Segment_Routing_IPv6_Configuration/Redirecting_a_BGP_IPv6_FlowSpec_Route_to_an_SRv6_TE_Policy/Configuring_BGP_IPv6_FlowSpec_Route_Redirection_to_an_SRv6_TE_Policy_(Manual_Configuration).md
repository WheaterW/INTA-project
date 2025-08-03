Configuring BGP IPv6 FlowSpec Route Redirection to an SRv6 TE Policy (Manual Configuration)
===========================================================================================

Manually configure a BGP IPv6 FlowSpec route and define a redirection rule to redirect the route to an SRv6 TE Policy.

#### Prerequisites

Before configuring BGP IPv6 FlowSpec route redirection to an SRv6 TE Policy, complete the following tasks:

* [Configure a BGP peer relationship.](dc_vrp_bgp_cfg_3006.html)
* [Configure an SRv6 TE Policy in manual configuration mode.](dc_vrp_srv6_cfg_all_0110.html)

#### Context

In a scenario where no controller is deployed, you can manually configure BGP IPv6 FlowSpec route redirection to an SRv6 TE Policy. The configuration process mainly includes the following steps:

1. Manually configure an SRv6 TE Policy.
2. Manually configure a BGP IPv6 FlowSpec route and define a redirection rule. BGP IPv6 FlowSpec route redirection is implemented based on <Redirection IPv6 address, Color, Public network End.DT6 SID>. If the redirection IPv6 address, color, and public network End.DT6 SID attributes of a BGP IPv6 FlowSpec route match the endpoint, color, and public network End.DT6 SID attributes of an SRv6 TE Policy, the route can be successfully redirected to the SRv6 TE Policy.
3. To enable the device to advertise the BGP IPv6 FlowSpec route to another device, establish a BGP peer relationship in the BGP-Flow-IPv6 address family.

#### Procedure

* Configure a public network End.DT6 SID.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
     
     SRv6 is enabled, and the SRv6 view is displayed.
  3. Configure a source address for SRv6 VPN encapsulation. Note that you only need to perform one of the following operations. If both of the operations are performed, the latest configuration overrides the previous one.
     + Run the [**encapsulation source-address**](cmdqueryname=encapsulation+source-address) *ipv6-address* [ **ip-ttl** *ttl-value* ] command to specify a source address for SRv6 encapsulation.
     + Run the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) { *intfname* | *interfaceType* *interfaceNum* } [ **ip-ttl** *ttl-value* ] command to specify the interface to which the source address used for SRv6 encapsulation belongs.
       
       If no IPv6 global address is configured for the interface specified using the [**encapsulation source-interface**](cmdqueryname=encapsulation+source-interface) command, the source address for SRv6 encapsulation is not configured.
  4. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* ]
     
     An SRv6 locator is configured, and the SRv6 locator view is displayed.
  5. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt6**
     
     A public network End.DT6 SID is configured.
  6. Run [**quit**](cmdqueryname=quit)
     
     Exit the SRv6 locator view.
  7. Run [**quit**](cmdqueryname=quit)
     
     Exit the SRv6 view.
  8. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a BGP IPv6 FlowSpec route.
  1. Run [**flow-route**](cmdqueryname=flow-route) *flowroute-name* **ipv6**
     
     
     
     A static BGP IPv6 FlowSpec route is created, and the Flow-Route-IPv6 view is displayed.
  2. Configure [**if-match**](cmdqueryname=if-match) clauses. For details, see "BGP Flow Specification Configuration" in *Configuration* - *Security*.
  3. Run [**apply redirect**](cmdqueryname=apply+redirect) **ipv6** *redirectIPv6RT* **color** *colorValue* [ **prefix-sid** *prefix-sid-value* ]
     
     
     
     The traffic that matches the **if-match** clauses is precisely redirected to the specified SRv6 TE Policy.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the Flow-Route-IPv6 view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a BGP peer relationship in the BGP-IPv6-Flow address family.
  
  
  
  Establish a BGP IPv6 FlowSpec peer relationship between the headend of the SRv6 TE Policy and the device on which the BGP IPv6 FlowSpec route is manually configured.
  
  
  
  1. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  2. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
     
     
     
     The BGP-IPv6-Flow address family view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **enable**
     
     
     
     A BGP IPv6 FlowSpec peer relationship is established.
     
     
     
     After the BGP IPv6 FlowSpec peer relationship is established in the BGP-IPv6-Flow address family view, the manually configured BGP IPv6 FlowSpec route is imported automatically to the BGP routing table and then advertised to the specified BGP IPv6 FlowSpec peer.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-IPv6-Flow address family view.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP view.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Allow the device to recurse static BGP IPv6 FlowSpec routes to corresponding tunnels.
  1. Run [**tunnel-selector**](cmdqueryname=tunnel-selector)*name* *matchMode* **node** *node*
     
     
     
     A tunnel selector is created, and its view is displayed.
  2. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the tunnel selector view.
  3. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  4. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
     
     
     
     The BGP-IPv6-Flow address family view is displayed.
  5. Run [**local-route redirect ipv6 recursive-lookup tunnel**](cmdqueryname=local-route+redirect+ipv6+recursive-lookup+tunnel) **tunnel-selector** *tunnel-selector-name*
     
     
     
     The device is allowed to recurse static BGP IPv6 FlowSpec routes to corresponding tunnels.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bgp flow ipv6 peer**](cmdqueryname=display+bgp+flow+ipv6+peer) command to check BGP IPv6 FlowSpec peer information.
* Run the [**display bgp flow ipv6 routing-table**](cmdqueryname=display+bgp+flow+ipv6+routing-table) command to check BGP IPv6 FlowSpec routing information.
* Run the [**display bgp flow ipv6 routing-table statistics**](cmdqueryname=display+bgp+flow+ipv6+routing-table+statistics) command to check BGP IPv6 FlowSpec route statistics.