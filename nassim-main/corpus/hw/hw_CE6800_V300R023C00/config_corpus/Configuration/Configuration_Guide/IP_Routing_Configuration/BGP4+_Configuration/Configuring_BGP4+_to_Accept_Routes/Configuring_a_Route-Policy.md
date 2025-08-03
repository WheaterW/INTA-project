Configuring a Route-Policy
==========================

Configuring a Route-Policy

#### Context

A route-policy is used to match routes or route attributes, and to change the attributes of routes that meet specific conditions.

A route-policy consists of multiple nodes, and each node can comprise the following clauses:

* **if-match** clauses
  
  These clauses define the filtering conditions for a route-policy to match routes using route attributes.
* **apply** clauses
  
  These clauses specify actions, that is, configuration commands that are executed after routes meet the filtering conditions specified by the **if-match** clauses. The **apply** clauses are used to change certain route attributes.

![](public_sys-resources/note_3.0-en-us.png) 

This section describes BGP4+ related routing policies only. For details on how to configure a route-policy, see  Configuration Guide > IP Routing > Routing Policy Configuration.



#### Procedure

1. Create a route-policy.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a route-policy node and enter the route-policy view.
      
      
      ```
      [route-policy](cmdqueryname=route-policy+permit+deny+node) route-policy-name { permit | deny } node node
      ```
2. (Optional) Configure **if-match** clauses.
   
   
   
   Configure **if-match** clauses for the current route-policy node.
   
   **Table 1** **if-match** clauses
   | Operation | Command | Description |
   | --- | --- | --- |
   | Match routes against an ACL. | [**if-match ipv6**](cmdqueryname=if-match+ipv6+address+next-hop+route-source+acl) { **address** | **next-hop** | **route-source** } **acl** { *acl-number* | *acl-name* } | An IPv6 ACL has been configured. |
   | Match routes against an IPv6 prefix list. | [**if-match ipv6**](cmdqueryname=if-match+ipv6+address+next-hop+route-source+prefix-list) { **address** | **next-hop** | **route-source** } **prefix-list** *ipv6-prefix-name* | An IPv6 prefix list has been configured.  [**ip ipv6-prefix**](cmdqueryname=ip+ipv6-prefix+index+greater-equal+less-equal) *name* [ **index**  *nodeseq* ] *matchMode* *address* *maskLen* [ **greater-equal** *geVal* ] [ **less-equal** *leVal* ]  NOTE:  The [**if-match ipv6 acl**](cmdqueryname=if-match+ipv6+acl) and [**if-match ipv6 prefix-list**](cmdqueryname=if-match+ipv6+prefix-list) commands cannot both be used in the same route-policy node, because the latter configuration overrides the previous one. |
   | Match BGP4+ routes against an AS\_Path filter. | [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) *apfIndex* &<1-16> | - |
   | Match BGP4+ routes against a community filter. | * [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) { *basic-comm-filter-num* [ **whole-match** ] | *adv-comm-filter-num* } \* &<1-16> * [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) *comm-filter-name* [ **whole-match** ] * [**if-match community-filter**](cmdqueryname=if-match+community-filter+sort-match) { *adv-comm-filter-num* **sort-match** } \* &<1-16> * [**if-match community-filter**](cmdqueryname=if-match+community-filter+sort-match) *comm-filter-name* **sort-match** | - |
   | Match BGP4+ routes against a Large-Community filter. | [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter+whole-match) *large-comm-filter-name* [ **whole-match** ] | - |
   | Match BGP4+ routes against a VPN-Target extended community filter. | [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { { *basic-extcomm-filter-num* [ **matches-all** | **whole-match** ] | *adv-extcomm-filter-num* } &<1-16> | *extcomm-filter-name* [ **matches-all** | **whole-match** ] } | - |
   | Match BGP4+ routes against an SoO extended community filter. | [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name* | - |
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The relationship between **if-match** clauses in a route-policy node is AND, meaning that a route must match all matching conditions before the action defined by an **apply** clause is taken on this route.
   * If no **if-match** clause is specified, all routes will match the route-policy node.
3. (Optional) Configure **apply** clauses.
   
   
   
   **apply** clauses can be used to set attributes for the routes matching the **if-match** clauses. If this step is not performed, the attributes of these routes remain unchanged.
   
   **Table 2** **apply** clauses
   | Operation | Command | Description |
   | --- | --- | --- |
   | Replace or add a specified AS number in the AS\_Path attribute of matched BGP4+ routes. | [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete) *as-path-value* &<1-128> { **additive** | **overwrite** | **delete** }  [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete) *asValues* { **additive** | **overwrite** | **delete** } | - |
   | Delete a specified community attribute from matched BGP4+ routes. | [**apply comm-filter**](cmdqueryname=apply+comm-filter) *cmntyName* [**delete**](cmdqueryname=delete) | NOTE:  The [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command deletes a specified community attribute from matched routes based on the referenced community filter. To delete multiple community attributes through one community filter, you need to run the [**ip community-filter**](cmdqueryname=ip+community-filter) command multiple times to configure multiple indexes for the filter, with each index corresponding to only one community attribute. If multiple community attributes are specified in the same index of the same community filter, none of them can be deleted in this case. For specific examples, see *Command Reference*. |
   | Delete all the community attributes from a matched BGP4+ route. | [**apply community**](cmdqueryname=apply+community+none) **none** | - |
   | Set community attributes for matched BGP4+ routes. | * [**apply community**](cmdqueryname=apply+community+internet+no-advertise+no-export) { { *community-number* | *aa:nn* } &<1-32> | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } \* [ **additive** ] * [**apply community community-list**](cmdqueryname=apply+community+community-list+additive) *community-list-name* [ **additive** ] | NOTE:  Before running the [**apply community**](cmdqueryname=apply+community) **community-list** *community-list-name* command, you need to run the [**ip community-list**](cmdqueryname=ip+community-list) command to configure a BGP community list and run the [**community**](cmdqueryname=community) command to configure community attributes for the list. |
   | Delete the Large-Community attribute from matched BGP4+ routes. | **apply large-community none** | - |
   | Set Large-Community attributes for matched BGP4+ routes. | [**apply large-community**](cmdqueryname=apply+large-community+additive+overwrite+delete) { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** } or [**apply large-community-list**](cmdqueryname=apply+large-community-list+additive+overwrite+delete) *large-community-list-name* { **additive** | **overwrite** | **delete** } | - |
   | Set the MED attribute for matched BGP4+ routes. | [**apply cost**](cmdqueryname=apply+cost+inherit) { [ *apply-type* ] *cost* | **inherit** } | - |
   | Set the MED of a matched BGP4+ route to be the same as the cost of the IGP route to which the BGP4+ route recurses. | [**apply cost-type**](cmdqueryname=apply+cost-type+internal) **internal** | - |
   | Set VPN-Target extended community attributes for matched BGP4+ routes. | [**apply extcommunity**](cmdqueryname=apply+extcommunity+rt+additive) { **rt** { *as-number:nn* | *ipv4-address:nn* } } &<1-16> [ **additive** ] | - |
   | Set the BGP4+ link bandwidth extended community attribute. | * [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+none) { *extCmntyString* | **none** } * [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+aggregate+limit) **aggregate** [ **limit** *bandwidth-value* ] | - |
   | Set the Local\_Pref for matched BGP4+ routes. | [**apply local-preference**](cmdqueryname=apply+local-preference+%2B+-) [ **+** | **-** ] *preference* | - |
   | Set the Origin attribute for matched BGP4+ routes. | [**apply origin**](cmdqueryname=apply+origin+igp+egp+incomplete) { **igp** | **egp** { *egpVal* } | **incomplete** } | - |
   | Set the PrefVal for matched BGP4+ routes. | [**apply preferred-value**](cmdqueryname=apply+preferred-value) *preferredVal* | - |
   | Set the dampening parameters for matched EBGP routes. | [**apply dampening**](cmdqueryname=apply+dampening) *half-life-reach* *reuse* *suppress* *ceiling* | - |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```