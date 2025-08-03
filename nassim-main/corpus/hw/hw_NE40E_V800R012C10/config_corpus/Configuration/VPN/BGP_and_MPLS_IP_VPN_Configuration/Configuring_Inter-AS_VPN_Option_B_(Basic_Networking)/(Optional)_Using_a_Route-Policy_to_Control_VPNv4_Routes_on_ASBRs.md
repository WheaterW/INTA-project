(Optional) Using a Route-Policy to Control VPNv4 Routes on ASBRs
================================================================

ASBRs can use a route-policy to filter undesired VPNv4 routes.

#### Context

ASBRs can use a route-policy to filter VPNv4 routes based on:

* VPN targets
* RDs

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following commands:
   
   
   * Perform either of the following operations to configure an extcommunity filter.
     
     To configure a VPN target extcommunity filter:
     
     + To configure a basic VPN target extcommunity filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *basic-extcomm-filter-num* | **basic** *basic-extcomm-filter-name* } { **deny** | **permit** } { **rt** { *as-number:nn* | *4as-number:nn* | *ipv4-address*:*nn* } } &<1-16> command.
     + To configure an advanced VPN target extcommunity filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter) { *advanced-extcomm-filter-num* | **advanced** *advanced-extcomm-filter-name* } { **deny** | **permit** } *regular-expression* command.
     
     To configure an SoO extcommunity filter:
     
     + To configure a basic SoO extcommunity filter, run the [**ip extcommunity-list soo basic**](cmdqueryname=ip+extcommunity-list+soo+basic) *basic-extcomm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } { *site-of-origin* } &<1-16> command.
     + To configure an advanced SoO extcommunity filter, run the [**ip extcommunity-list soo advanced**](cmdqueryname=ip+extcommunity-list+soo+advanced) *advanced-extcomm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
   * Run the [**ip rd-filter**](cmdqueryname=ip+rd-filter) *rdfIndex* [ **index** *index-number* ] *matchMode* *rdStr* &<1-10> command to configure an RD filter.
3. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *node*
   
   
   
   A route-policy is configured.
4. Run any of the following commands to configure the apply clause of the route-policy for the current node as needed:
   
   
   * To configure a matching rule based on the VPN target filter for the route-policy, run the [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { { *basic-extcomm-filter-num* [ **matches-all** | **whole-match** ] | *adv-extcomm-filter-num* } &<1-16> | *basic-extcomm-filter-name* [ **matches-all** | **whole-match** ] | *advanced-extcomm-filter-name* } command.
   * To configure a match rule that is based on the SoO extended community attribute, run the [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name* command.
   * To configure a match rule that is based on the RD attribute, run the [**if-match rd-filter**](cmdqueryname=if-match+rd-filter) *rd-filter-number* command.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
7. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpnv4** [ **unicast** ]
   
   
   
   The BGP VPNv4 address family view is displayed.
8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* { **export** | **import** }
   
   
   
   The route-policy is applied to control the import and export of VPNv4 routes.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.