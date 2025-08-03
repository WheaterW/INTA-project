(Optional) Enabling an RR to Modify Route Attributes Using an Export Policy
===========================================================================

You can enable an RR to modify route attributes using an export policy to control BGP route selection.

#### Context

Route attributes cannot be modified using an export policy on an RR because it would cause routing loops. By default, an RR is disabled from modifying route attributes based on an export policy. However, if you need to re-plan the network traffic, you can enable the RR to modify route attributes based on an export policy.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute)
   
   
   
   The RR is configured to modify path attributes of BGP routes based on an export policy.
   
   
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on an RR, the configuration of modifying path attributes of routes based on an export policy takes effect. The configurations are as follows:
   * [**apply as-path**](cmdqueryname=apply+as-path): modifies the AS\_Path attribute of BGP routes.
   * [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete): deletes community attributes from BGP routes.
   * [**apply community**](cmdqueryname=apply+community): modifies the community attribute of BGP routes.
   * [**apply large-community**](cmdqueryname=apply+large-community): modifies the Large-Community attribute of BGP routes.
   * [**apply cost**](cmdqueryname=apply+cost): modifies the MED value of BGP routes.
   * [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop): modifies the next-hop IP address of BGP routes.
   * [**apply local-preference**](cmdqueryname=apply+local-preference): modifies the Local\_Pref value of BGP routes.
   * [**apply origin**](cmdqueryname=apply+origin): modifies the Origin attribute of BGP routes.
   * [**apply extcommunity**](cmdqueryname=apply+extcommunity): modifies the VPN target extended community attribute of BGP routes.
   * [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo+additive) { *site-of-origin* } &<1-16> **additive**: modifies the SoO extended community attribute of BGP routes.
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**reflect change-path-attribute**](cmdqueryname=reflect+change-path-attribute) command is run on the RR, the [**peer route-policy**](cmdqueryname=peer+route-policy+export) **export** command takes precedence over the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) and [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) commands.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.