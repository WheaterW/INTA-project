(Optional) Configuring an **apply** Clause
==========================================

(Optional) Configuring an **apply** Clause

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name matchMode node node
   ```
3. Configure apply clauses in the route-policy. See [Table 1](#EN-US_TASK_0000001130623986__table31174507411).
   
   
   
   **Table 1** apply clauses in a route-policy
   | Operation | Command |
   | --- | --- |
   | Set a cost for routes. | [**apply cost**](cmdqueryname=apply+cost) { [ **+** | **-** ] *cost* | **inherit** | **none** } |
   | Set the AS\_Path attribute. | [**apply as-path**](cmdqueryname=apply+as-path) *as-path-value* &<1-128> { **additive** | **overwrite** | **delete** }  [**apply as-path**](cmdqueryname=apply+as-path) *asValues* { **additive** | **overwrite** | **delete** } |
   | Clear the original AS\_Path attribute. | [**apply as-path**](cmdqueryname=apply+as-path) **none** **overwrite** |
   | Set the number of times the most recent AS number in AS\_Path is appended to routes. | [**apply as-path most-recent**](cmdqueryname=apply+as-path+most-recent) *most-recent-value* |
   | Set a cost type for routes. | [**apply cost-type**](cmdqueryname=apply+cost-type) { **external** | **internal** | **type-1** | **type-2** | **internal-inc-ibgp** | **med-plus-igp** } |
   | Set dampening parameters for EBGP routes. | [**apply dampening**](cmdqueryname=apply+dampening) *half-life-reach* *reuse* *suppress* *ceiling* |
   | Delete the BGP route community attribute of a specified value that is set in the community attribute filter. | [**apply comm-filter**](cmdqueryname=apply+comm-filter) { *basIndex* | *advIndex* } **delete** |
   | Set BGP community attributes. | [**apply community**](cmdqueryname=apply+community) { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-32> [ **additive** ]  [**apply community community-list**](cmdqueryname=apply+community+community-list) *community-list-name* [ **additive** ] |
   | Clear the existing extended community attributes of routes. | [**apply extcommunity**](cmdqueryname=apply+extcommunity) **rt** **none** |
   | Set the origin for BGP routes. | [**apply origin**](cmdqueryname=apply+origin) { **egp** { *egpVal* } | **igp** | **incomplete** } |
   | Set the Local\_Pref for BGP routes. | [**apply local-preference**](cmdqueryname=apply+local-preference) [ + | - ] *preference* |
   | Set a BGP Large-community attribute. | [**apply large-community-list**](cmdqueryname=apply+large-community-list) *large-community-list-name* { **additive** | **overwrite** | **delete** }  [**apply large-community**](cmdqueryname=apply+large-community) { *aa*:*bb*:*cc* } &<1-16> { **additive** | **overwrite** | **delete** } |
   | Set the VPN target extended community attribute for BGP routes. | [**apply extcommunity**](cmdqueryname=apply+extcommunity) { **rt** *extCmntyValue* } &<1-16> [ **additive** ] |
   | Set one or multiple SoO extended community attributes for BGP routes. | [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo) { *site-of-origin* } &<1-16> **additive** |
   | Set a bandwidth extended community attribute for BGP Routes. | [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) { *extCmntyString* | **none** }  [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) **aggregate** [ **limit** *bandwidth-value* ]  **[**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth) **aggregate-upstream**** [ ****limit**** **upstream-bandwidth** ] |
   | Set a preferred value for BGP routes. | [**apply preferred-value**](cmdqueryname=apply+preferred-value) *preferredVal* |
   | Set a local QoS ID. | [**apply qos-local-id**](cmdqueryname=apply+qos-local-id) *qos-local-id* |
   | Set a next-hop address for IPv4 routes. | [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) { *address* | **peer-address** | **blackhole** } |
   | Set a next-hop address for IPv6 routes. | [**apply ipv6 next-hop**](cmdqueryname=apply+ipv6+next-hop) { *address* | **peer-address** | **blackhole** }  NOTE:  The CE6885-LL does not support this command. |
   | Set a level for IS-IS routes. | [**apply isis**](cmdqueryname=apply+isis) { **level-1** | **level-1-2** | **level-2** } |
   | Set a preference value for a routing protocol. | [**apply preference**](cmdqueryname=apply+preference) *preference* |
   | Set a tag value for routes. | [**apply tag**](cmdqueryname=apply+tag) *tag* |
   | Set an IP gateway address for routes. | [**apply gateway-ip**](cmdqueryname=apply+gateway-ip) { **origin-nexthop** |  *address* } |
   | Set an IPv6 gateway address for routes. | [**apply ipv6 gateway-ip**](cmdqueryname=apply+ipv6+gateway-ip) { **origin-nexthop** | *address* }  NOTE:  The CE6885-LL does not support this command. |
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The commands in Step 3 can be run in any required order. A node can contain multiple or no apply clauses.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```