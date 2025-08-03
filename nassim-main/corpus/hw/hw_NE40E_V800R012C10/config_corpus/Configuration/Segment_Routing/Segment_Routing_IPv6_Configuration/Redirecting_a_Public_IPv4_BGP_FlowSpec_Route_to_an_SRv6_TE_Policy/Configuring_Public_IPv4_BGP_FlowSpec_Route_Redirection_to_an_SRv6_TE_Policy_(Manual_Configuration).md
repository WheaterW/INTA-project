Configuring Public IPv4 BGP FlowSpec Route Redirection to an SRv6 TE Policy (Manual Configuration)
==================================================================================================

Manually generate a BGP FlowSpec route and configure redirection rules to redirect the route to an SRv6 TE Policy.

#### Prerequisites

Before redirecting a public IPv4 BGP FlowSpec route to an SRv6 TE Policy in manual configuration mode, complete the following tasks:

* [Configure a BGP peer relationship.](dc_vrp_bgp_cfg_3006.html)
* [Configure an SRv6 TE Policy in manual configuration mode.](dc_vrp_srv6_cfg_all_0110.html)

#### Context

If no controller is deployed, perform the following operations to manually redirect a public IPv4 BGP FlowSpec route to an SRv6 TE Policy:

1. Manually configure an SRv6 TE Policy.
2. Manually configure a BGP FlowSpec route and define redirection rules. BGP FlowSpec route redirection is based on <Redirection IP address, Color, Public End.DT4 SID>. If the redirection IP address, color, and public End.DT4 SID attributes of a BGP FlowSpec route match the endpoint, color, and public End.DT4 SID attributes of an SRv6 TE Policy, the route can be successfully redirected to the SRv6 TE Policy.
3. To enable the device to advertise the BGP FlowSpec route to another device, establish a BGP peer relationship in the BGP-Flow address family.

#### Procedure

* Configure a public End.DT4 SID.
  
  
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
  5. Run [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt4**
     
     A public End.DT4 SID is configured.
  6. Run [**quit**](cmdqueryname=quit)
     
     Exit the SRv6 locator view.
  7. Run [**quit**](cmdqueryname=quit)
     
     Exit the SRv6 view.
  8. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a BGP FlowSpec route.
  
  
  1. Run [**flow-route**](cmdqueryname=flow-route) *flowroute-name*
     
     A static BGP FlowSpec route is created, and the Flow-Route view is displayed.
  2. Configure [**if-match**](cmdqueryname=if-match) clauses. For details, see "BGP Flow Specification Configuration" in *Configuration* - *Security*.
  3. Run [**apply redirect**](cmdqueryname=apply+redirect) **ipv6** *redirectIPv6RT* **color** *colorValue* [ **prefix-sid** *prefix-sid-value* ]
     
     The traffic that matches the **if-match** clauses is precisely redirected to the specified SRv6 TE Policy.
  4. Run [**quit**](cmdqueryname=quit)
     
     Exit the Flow-Route view.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure a BGP peer relationship in the BGP-Flow address family.
  
  
  
  Establish a BGP FlowSpec peer relationship between the ingress of the SRv6 TE Policy and the device on which the BGP FlowSpec route is manually generated.
  
  
  
  1. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  2. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
     
     
     
     The BGP-Flow address family view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
     
     
     
     The BGP FlowSpec peer relationship is enabled.
     
     After the BGP FlowSpec peer relationship is established in the BGP-Flow address family view, the manually generated BGP FlowSpec route is automatically imported to the BGP-Flow routing table and then sent to each peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **redirect tunnelv6**
     
     
     
     The device is enabled to process the redirection next-hop IPv6 address, color, and prefix SID attributes carried in BGP FlowSpec routes received from a peer.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP-Flow address family view.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the BGP view.
* Allow the device to recurse static BGP IPv6 FlowSpec routes to corresponding SRv6 TE Policies.
  1. Run [**tunnel-selector**](cmdqueryname=tunnel-selector)*name* *matchMode* **node** *node*
     
     
     
     A tunnel selector is created and its view is displayed.
  2. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the tunnel selector view.
  3. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  4. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
     
     
     
     The BGP-Flow address family view is displayed.
  5. Run [**redirect tunnelv6 tunnel-selector**](cmdqueryname=redirect+tunnelv6+tunnel-selector) *tunnel-selector-name*
     
     
     
     The device is enabled to recurse received routes with the redirection next-hop IPv6 address, color, and prefix SID attributes to SRv6 TE Policies.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring the redirection, verify the configuration.

* Run the [**display bgp flow peer**](cmdqueryname=display+bgp+flow+peer) [ [ *ipv4-address* ] **verbose** ] command to check information about BGP FlowSpec peers.
* Run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table) command to check BGP FlowSpec routing information.
* Run the [**display flowspec statistics**](cmdqueryname=display+flowspec+statistics) *reindex* command to check statistics about traffic transmitted over BGP FlowSpec routes.