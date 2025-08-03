(Optional) Configuring an **apply** Clause
==========================================

The **apply** clauses specify actions to set certain route attributes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
   
   
   
   The route-policy view is displayed.
3. Run the following commands as needed to configure **apply** clauses for the route-policy:
   
   
   * To set an AIGP value for matched BGP routes, run the [**apply aigp**](cmdqueryname=apply+aigp) { [ + | - ] cost | **inherit-cost** } command.
   * To set a cost for matched routes, run the [**apply cost**](cmdqueryname=apply+cost) { [ **+** | **-** ] *cost* | **inherit** | **none** } command.
   * To set the AS\_Path attribute, run the [**apply as-path**](cmdqueryname=apply+as-path) { *as-number-plain* | *as-number-dot* } &<1-128>{ **additive** | **overwrite** | **delete** } or [**apply as-path**](cmdqueryname=apply+as-path) *asValues* { **additive** | **overwrite** | **delete** } command.
   * To clear the original AS\_Path attribute, run the [**apply as-path none overwrite**](cmdqueryname=apply+as-path+none+overwrite) command.
   * To set the number of times the most recent AS number in AS\_Path is appended to routes, run the [**apply as-path most-recent**](cmdqueryname=apply+as-path+most-recent) <*most-recent-value*> command.
   * To delete a community attribute from BGP routes based on the specified value in a community filter, run the [**apply comm-filter**](cmdqueryname=apply+comm-filter) { *basIndex* | *advIndex* } **delete** or [**apply comm-filter**](cmdqueryname=apply+comm-filter) *cmntyName* **delete** command.
   * To set a BGP community attribute, run the [**apply community**](cmdqueryname=apply+community) { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-32> [ **additive** ] or [**apply community community-list**](cmdqueryname=apply+community+community-list) *community-list-name* [ **additive** ] command.
   * Set an extended community attribute for BGP routes.
     + To set the VPN target extcommunity attribute, run the [**apply extcommunity**](cmdqueryname=apply+extcommunity) { **rt** *extCmntyValue* } &<1-16> [ **additive** ] command.
     + To set the color extcommunity attribute, run the [**apply extcommunity color**](cmdqueryname=apply+extcommunity+color) *extCmntyValue* command.
     + To set the SoO extended community attribute, run the [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo) { *site-of-origin* } &<1-16> **additive** command.
     + To set the bandwidth extended community attribute, run the [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) { *extCmntyString* | **none** }, [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) **aggregate-upstream** [ *limit* *upstream-bandwidth* ], or [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) **aggregate** [ **limit** *bandwidth-value* ] command.
   * To clear the existing extended community attributes of routes, run the [**apply extcommunity**](cmdqueryname=apply+extcommunity) **rt** **none** command.
   * To set the redirection extended community attribute for matched BGP Flow Specification routes, run the [**apply extcommunity redirect ip**](cmdqueryname=apply+extcommunity+redirect+ip) *ipv4-address:nn* or [**apply extcommunity redirect vpn-target**](cmdqueryname=apply+extcommunity+redirect+vpn-target) *extCmntyValue* command.
   * To set the Large-Community attribute of BGP routes, run the [**apply large-community**](cmdqueryname=apply+large-community) { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** } or [**apply large-community-list**](cmdqueryname=apply+large-community-list) *large-community-list-name* { **additive** | **overwrite** | **delete** } command.
   * To set the Local\_Pref attribute for BGP routes, run the [**apply local-preference**](cmdqueryname=apply+local-preference) [ + | **-** ] *localPreference* command.
   * To allocate MPLS labels to public network routes, run the [**apply mpls-label**](cmdqueryname=apply+mpls-label) command.
   * To set the QoS parameter **ip-precedence** for matched routes, run the [**apply ip-precedence**](cmdqueryname=apply+ip-precedence) *ip-precedence* command.
   * To set the local QoS ID for matched routes, run the [**apply qos-local-id**](cmdqueryname=apply+qos-local-id) *qos-local-id* command.
   * To set the Origin attribute of BGP routes, run the [**apply origin**](cmdqueryname=apply+origin) { **egp** { *egpVal* } | **igp** | **incomplete** } command.
   * To set the PrefVal attribute of BGP routes, run the [**apply preferred-value**](cmdqueryname=apply+preferred-value) *preferredVal* command.
   * To set the BGP traffic index for statistics collection, run the [**apply traffic-index**](cmdqueryname=apply+traffic-index) *indexVal* command.
   * To set a cost type for matched routes, run the [**apply cost-type**](cmdqueryname=apply+cost-type) { **external** | **internal** | **type-1** | **type-2** | **internal-inc-ibgp** | **med-plus-igp** | **med-inherit-aigp** } command.
   * To set dampening parameters for EBGP routes, run the [**apply dampening**](cmdqueryname=apply+dampening) *half-life-reach* *reuse* *suppress* *ceiling* command.
   * To set a next-hop address for IPv4 routes, run the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) { *ipv4-address* | **peer-address** | **blackhole** | **original** } command.
   * To set a next-hop address for IPv6 routes, run the [**apply ipv6 next-hop**](cmdqueryname=apply+ipv6+next-hop) { *ipv6-address* | **peer-address** | **blackhole** | **original** } command.
   * To set a level for IS-IS routes, run the [**apply isis**](cmdqueryname=apply+isis) { **level-1** | **level-1-2** | **level-2** } command.
   * To set the preference of protocol routes, run the [**apply preference**](cmdqueryname=apply+preference) *preference* command.
   * To set a tag value for matched routes, run the [**apply tag**](cmdqueryname=apply+tag) *tag* command.
   * To set a gateway IP address for matched routes, run the [**apply gateway-ip**](cmdqueryname=apply+gateway-ip) { **origin-nexthop** | *ip-address* | **none** } command.
   * To set a gateway IPv6 address for matched routes, run the [**apply ipv6 gateway-ip**](cmdqueryname=apply+ipv6+gateway-ip) { **origin-nexthop** | *ipv6-address* | **none** } command.
   * To discard entropy labels of matched routes, run the [**apply entropy-label none**](cmdqueryname=apply+entropy-label+none) command.
   * To stitch PMSIs, run the [**apply stitch-pmsi**](cmdqueryname=apply+stitch-pmsi) { **incoming** { **rsvp-te** **p2mp-template** *p2mp-template-name* [ **mldp** **root-ip** *root-ip-address* ] } | **mldp** [ **root-ip** *root-ip-address* ] | **rsvp-te** **p2mp-template** *p2mp-template-name* } command.
   * To set a Flex-Algo ID for matched routes, run the **apply flex-algo** *flex-algo-id* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The commands in Step 3 can be run in any required order. A node can have multiple or no **apply** clauses.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.