(Optional) Enabling an RR to Modify Route Attributes Using an Export Policy
===========================================================================

Enabling an RR to modify route attributes using an export policy can change BGP4+ route selection results.

#### Context

The route attributes on the RR cannot be modified using the export policy because it may cause routing loops. By default, the RR is disabled from modifying the route attributes based on the export policy. However, if you need to re-plan the network traffic, you can enable the RR to modify route attributes based on an export policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) [ **unicast** ]
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute)
   
   
   
   The RR is configured to modify the path attributes of BGP4+ routes based on an export policy.
   
   
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on an RR, the configuration of modifying path attributes based on an export policy takes effect immediately. After the command is run, the following configurations can take effect:
   * [**apply as-path**](cmdqueryname=apply+as-path): This command configures the device to modify the AS\_Path attribute of BGP4+ routes.
   * [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete): This command configures the device to delete community attributes of BGP4+ routes.
   * [**apply community**](cmdqueryname=apply+community): This command configures the device to modify community attributes of BGP4+ routes.
   * [**apply large-community**](cmdqueryname=apply+large-community): This command configures the device to modify the Large-Community attribute of BGP4+ routes.
   * [**apply cost**](cmdqueryname=apply+cost): This command configures the device to modify the cost (MED) values of BGP4+ routes.
   * [**apply ipv6 next-hop**](cmdqueryname=apply+ipv6+next-hop): This command configures the device to modify the next-hop IP addresses of BGP4+ routes.
   * [**apply local-preference**](cmdqueryname=apply+local-preference): This command configures the device to modify the local preferences of BGP4+ routes.
   * [**apply origin**](cmdqueryname=apply+origin): This command configures the device to modify the Origin attribute of BGP4+ routes.
   * [**apply extcommunity**](cmdqueryname=apply+extcommunity): This command configures the device to modify the VPN target extended community attribute of BGP4+ routes.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on the RR, the [**peer route-policy**](cmdqueryname=peer+route-policy+export) **export** command takes precedence over the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command and the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.