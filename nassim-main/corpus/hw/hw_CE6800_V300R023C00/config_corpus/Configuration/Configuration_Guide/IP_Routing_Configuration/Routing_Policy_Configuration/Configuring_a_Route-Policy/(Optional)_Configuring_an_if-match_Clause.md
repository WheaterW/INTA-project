(Optional) Configuring an if-match Clause
=========================================

(Optional) Configuring an if-match Clause

#### Context

An if-match clause defines matching rules related to route filters and attributes in a route-policy.

If no if-match clause is configured for a node in a route-policy, routes successfully match the node.

If one or more if-match clauses are configured in a node, the relationship between the clauses is "AND". This means that a route can match this node only if the route matches all if-match clauses of this node.

The [**if-match acl**](cmdqueryname=if-match+acl) and [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) commands are mutually exclusive in the same node of a route-policy. If both commands are run for a node, the latest configuration overrides the previous one.

![](public_sys-resources/note_3.0-en-us.png) 

In the same node of a route-policy, the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter), [**if-match community-filter**](cmdqueryname=if-match+community-filter), [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter), [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter), [**if-match interface**](cmdqueryname=if-match+interface), and [**if-match route-type**](cmdqueryname=if-match+route-type) commands can all be run. If they are all run, the relationship between these **if-match** clauses is OR, and the relationship between these **if-match** clauses and the **if-match** clauses configured using other commands is AND.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name matchMode node node
   ```
3. Configure if-match clauses in the route-policy. For details, see [Table 1](#EN-US_TASK_0000001176663537__table31174507411).
   
   
   
   **Table 1** if-match clauses in a route-policy
   | Operation | Command |
   | --- | --- |
   | Define a rule to match routes against one or multiple specified outbound interfaces. | [**if-match interface**](cmdqueryname=if-match+interface) { { *interface-name* | *interface-type interface-number* } &<1-16> } |
   | Define a rule to match routes against a specified ACL. | [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* } |
   | Define a rule to match routes against a specified cost. | [**if-match cost**](cmdqueryname=if-match+cost) *cost*  [**if-match cost**](cmdqueryname=if-match+cost) { **greater-equal** *greater-equal-value* [ **less-equal** *less-equal-value* ] | **less-equal** *less-equal-value* } |
   | Define a rule to match a specified preference value of routes. | [**if-match preference**](cmdqueryname=if-match+preference) *preference* |
   | Define a rule to match IPv4 routes. | [**if-match ip**](cmdqueryname=if-match+ip) { **next-hop** | **route-source** }  **ip-prefix** *ip-prefix-name*  [**if-match ip**](cmdqueryname=if-match+ip) { **next-hop** | **route-source** }  **acl** { *acl-number* | *acl-name* } |
   | Define a rule to match routes against a specified IP prefix list. | [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) *ip-prefix-name* |
   | Define a rule to match routes by route type. | [**if-match protocol**](cmdqueryname=if-match+protocol) { **direct** | **static** | **rip** | **ripng** | **ospf** | **ospfv3** | **bgp** | **isis** } \* |
   | Define a rule to match IPv6 routes. | [**if-match ipv6**](cmdqueryname=if-match+ipv6) { **address** | **next-hop** | **route-source** }  **prefix-list** *ipv6-prefix-name*  [**if-match ipv6**](cmdqueryname=if-match+ipv6) { **address** | **next-hop** | **route-source** }  **acl** { *acl-number* | *acl-name* }  NOTE:  The CE6885-LL does not support the preceding commands. |
   | Define a rule to match OSPF routes of a specified type. | [**if-match route-type**](cmdqueryname=if-match+route-type) { **external-type1** | **external-type1or2** | **external-type2** | **internal** | **nssa-external-type1** | **nssa-external-type1or2** | **nssa-external-type2** } |
   | Define a rule to match IS-IS routes of a specified level. | [**if-match route-type**](cmdqueryname=if-match+route-type) { **is-is-level-1** | **is-is-level-2** } |
   | Define a rule to match BGP routes. | [**if-match route-type**](cmdqueryname=if-match+route-type) { **ibgp** | **ebgp** } |
   | Define a rule to match EVPN routes. | [**if-match route-type evpn**](cmdqueryname=if-match+route-type+evpn) { **inclusive** | **mac** | **prefix** } |
   | Define a rule to match routes carrying a specified tag value. | [**if-match tag**](cmdqueryname=if-match+tag) *tag* |
   | Define a matching rule that is based on the route prefix modulo operation result. | [**if-match prefix mod**](cmdqueryname=if-match+prefix+mod) *mod-value* **equal** *mod-result* |
   | Define a rule to match routes against a specified AS\_Path length range. | [**if-match as-path length**](cmdqueryname=if-match+as-path+length) { **greater-equal** **greEqualVal**| l**ess-equal** *lessEqualVal* } |
   | Define a rule to match routes against one or multiple specified AS\_Path filters. | [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) { *apfIndex* } &<1-16> |
   | Define a rule to match routes against a specified RD filter. | [**if-match rd-filter**](cmdqueryname=if-match+rd-filter) *rd-filter-number* |
   | Define a rule to match routes against a community filter. | [**if-match community-filter**](cmdqueryname=if-match+community-filter) { *basIndex* [ **whole-match** ] | AdvIndex } &<1-16> |
   | Define a rule to match routes against a specified Large-Community filter. | [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter) *large-comm-filter-name* [ **whole-match** ] |
   | Define a rule to match routes against a specified VPN-Target extended community filter. | [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { *basIndex* [ **matches-all** | **whole-match** ] | *advIndex* } &<1-16>  [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) *ecfName* [ **matches-all** | **whole-match** ] |
   | Define a rule to match routes with a specified SoO extended community attribute. | [**if-match extcommunity-list**](cmdqueryname=if-match+extcommunity-list) **soo** *extcomm-filter-name* |
   | Define a rule to match routes with a specified encapsulation extended community attribute. | [**if-match extcommunity-list encapsulation**](cmdqueryname=if-match+extcommunity-list+encapsulation) *encapsulation-name* |
   | Define a rule to match non-optimal BGP routes. | [**if-match route-state bgp-not-best**](cmdqueryname=if-match+route-state+bgp-not-best) |
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The commands in Step 3 can be run in any required order. A node may contain multiple **if-match** clauses or no **if-match** clause. If no if-match clause is configured, all routes match the node.
   
   If multiple if-match clauses of a node in a route-policy define the same filter type, the bitwise OR is applied to the if-match clauses; if the if-match clauses define different filter types, the bitwise AND is applied to the if-match clauses.
   
   You are advised not to use the same route-policy to filter both IPv4 and IPv6 routes if the **route-policy address-family mismatch-deny** command is not run.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```