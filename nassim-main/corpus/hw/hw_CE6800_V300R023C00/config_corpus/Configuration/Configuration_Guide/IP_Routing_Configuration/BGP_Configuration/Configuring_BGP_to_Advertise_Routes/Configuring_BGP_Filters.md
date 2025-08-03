Configuring BGP Filters
=======================

Configuring BGP Filters

#### Context

Configuring BGP filters allows you to flexibly filter routes to be advertised.


#### Procedure

* Configure an access control list (ACL).
  
  
  
  An ACL is a series of sequential rules composed of permit and deny clauses. These rules specify source addresses, destination addresses, port numbers, and other information of data packets. ACL rules are used to classify data packets, and after the rules are applied to a device interface, it uses the rules to permit or deny data packets.
  
  For details about ACL configuration, see  Configuration Guide > IP Addresses and Services > ACL Configuration.
  
  An ACL can be used as a filtering condition of a route-policy or directly used in the [**filter-policy**](cmdqueryname=filter-policy) { *acl-number* | **acl-name** *acl-name* } **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] or [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **filter-policy** { *acl-number* | **acl-name** *acl-name* } **export** command.
* Configure an IP prefix list.
  
  
  
  An IP prefix list is a type of filter used to filter routes based on destination addresses, and is identified by its name. In addition, an IP prefix list can be used flexibly to implement precise filtering. For example, it can be used to filter a specific route or routes to a network segment. If a large number of routes with different prefixes need to be filtered, configuring an IP prefix list to filter the routes is very complex.
  
  An IP prefix list can be used as a matching rule of a route-policy or directly used in the [**filter-policy**](cmdqueryname=filter-policy) **ip-prefix** *ip-prefix-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ] or [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **ip-prefix** *ip-prefix-name* **export** command.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure an IPv4 prefix list. 
     
     
     ```
     [ip ip-prefix](cmdqueryname=ip+ip-prefix+index+permit+deny+greater-equal+less-equal) ip-prefix-name [ index index-number ] { permit | deny } ip-address mask-length [ greater-equal greater-equal-value ] [ less-equal less-equal-value ]
     ```
     
     The range of the mask length must meet the following requirements: *mask-length* <= *greater-equal-value* <= *less-equal-value* <= 32. If only **greater-equal** is specified, the prefix range is [*greater-equal-value*, 32]. If only **less-equal** is specified, the prefix range is [*mask-length*, *less-equal-value*].
     
     An IPv4 prefix list is identified by its name, and each list contains one or multiple entries. Each entry is identified by an index, and can uniquely specify a matching range in the form of a network prefix. An IPv4 prefix list named **abcd** is used as an example.
     
     ```
     #
     ```
     ```
     ip ip-prefix abcd index 10 permit 1.0.0.0 8
     ```
     ```
     ip ip-prefix abcd index 20 permit 10.0.0.0 8
     ```
     
     During route matching, a device checks entries that are identified by indexes in ascending order. If a route matches an entry, the route does not continue to match against the next entry.
     
     By default, the device denies all routes that do not match any entries. If all entries in an IPv4 prefix list are set to deny mode, all routes will be denied based on the IPv4 prefix list. In this case, after multiple entries are set to deny mode, define an entry **permit 0.0.0.0 0 less-equal 32** to allow all the other IPv4 routes to be permitted by the IPv4 prefix list.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     If more than one entry is defined in a prefix list, at least one of them must be set to **permit** mode.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an AS\_Path filter.
  
  
  
  An AS\_Path filter is used to filter BGP routes based on the AS\_Path lists they carry. If you do not want traffic to traverse specific ASs, you can configure an AS\_Path filter to filter out routes carrying the AS numbers matching those in the AS\_Path filter. If the BGP routing table of each device on a network contains a large number of BGP routes, configuring ACLs or IP prefix lists to filter BGP routes is a complex process, which complicates maintenance of new routes. To address this issue, use an AS\_Path filter to filter routes.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  If the AS\_Path information of summary routes is lost, an AS\_Path filter can no longer filter them. However, it can still filter specific routes, which carry AS\_Path information.
  
  An AS\_Path filter can be used as a filtering condition of a route-policy or directly used in the [**peer as-path-filter**](cmdqueryname=peer+as-path-filter) command.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure an AS\_Path filter.
     
     
     ```
     [ip as-path-filter](cmdqueryname=ip+as-path-filter+index+permit+deny) { as-path-filter-number | as-path-filter-name } [ index index-number ] { permit | deny } regular-expression
     ```
     
     To define a matching rule, an AS\_Path filter uses a regular expression, which is composed of the following parts:
     
     + Metacharacter: defines a matching rule.
     + Literal character: defines a matching object.
     
     **Table 1** Description of metacharacters
     | Special Character | Function |
     | --- | --- |
     | \ | Defines an escape character, which is used to mark the next character (common or special) as a common character. |
     | ^ | Matches the start position of a string. |
     | $ | Matches the end position of a string. |
     | \* | Matches a sub-regular expression that it follows zero or multiple times. |
     | + | Matches a sub-regular expression that it follows once or multiple times. |
     | ? | Matches a sub-regular expression that it follows once or zero times. |
     | . | Matches any single character. |
     | () | Matches a sub-regular expression within the parentheses, and obtains the matching result. The parentheses can also be empty. |
     | \_ | Matches regular expressions with a sign, such as a comma (,), left brace ({), right brace (}), left parenthesis ((), right parenthesis ()), or space. In addition, the underscore (\_) can be used at the beginning of a regular expression with the same function as the caret sign (^) or at the end of a regular expression with the same function as the dollar sign ($). |
     | x|y | Matches *x* or *y*. |
     | [xyz] | Matches any character contained in a regular expression. |
     | [^xyz] | Matches any character that is not contained in a regular expression. |
     | [a-z] | Matches any character within a specified range in a regular expression. |
     | [^a-z] | Matches any character beyond a specified range. |
     
     For example, ^10 matches only the AS\_Path attribute beginning with 10, with ^ indicating that the beginning of a character string is matched.
     
     Multiple rules (permit or deny) can be specified in a filter, and the relationship between them is OR, which means that a route matches the AS\_Path filter if it meets one of the matching rules.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     For details about how to use regular expressions, see  Configuration Guide > Basic Configuration > CLI Overview.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a community filter.
  
  
  
  A BGP community attribute is used to identify a group of routes with the same properties. Routes can be classified manually by using community attributes, which facilitates route management.
  
  In actual application, some AS internal routes may not need to be advertised to other ASs, while some AS external routes need to be advertised to other ASs. Both internal and external routes may have different prefixes (making an IP prefix list unsuitable), and may come from different ASs (making an AS\_Path filter unsuitable). In this case, you can set a community value for the AS internal routes and another community value for the AS external routes on an AS edge device to control and filter routes.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a community filter.
     
     
     + Configure a standard community filter.
       
       ```
       [ip community-filter](cmdqueryname=ip+community-filter+basic+index+permit+deny+internet) basic comm-filter-name [ index index-number ] { permit | deny } [ community-number | aa:nn | internet [ strict-match ] | no-export-subconfed | no-advertise | no-export ] &<1-20>
       ```
       
       or
       
       ```
       [ip community-filter](cmdqueryname=ip+community-filter+index+permit+deny+internet) basic-comm-filter-num [ index index-number ] { permit | deny } [ community-number | aa:nn | internet | no-export-subconfed | no-advertise | no-export ] &<1-20>
       ```
     + Configure an advanced community filter.
       
       ```
       [ip community-filter](cmdqueryname=ip+community-filter+advanced+index+permit+deny) { advanced comm-filter-name | adv-comm-filter-num } [ index index-number ] { permit | deny } regular-expression
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a Large-Community filter.
  
  
  
  The Large-Community attribute can represent a 2-byte or 4-byte AS number completely, and has two 4-byte LocalData IDs. This enables the administrator to apply policies more flexibly. The Large-Community attribute extends and can be used together with the community attribute.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a Large-Community filter.
     
     
     + Configure a basic Large-Community filter.
       
       ```
       [ip large-community-filter](cmdqueryname=ip+large-community-filter+basic+index+permit+deny) basic large-comm-filter-name [ index index-number ] { permit | deny } { aa:bb:cc } &<1-16>
       ```
     + Configure an advanced Large-Community filter.
       
       ```
       [ip large-community-filter](cmdqueryname=ip+large-community-filter+advanced+index+permit+deny) advanced large-comm-filter-name [ index index-number ] { permit | deny } regular-expression
       ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an extended community filter.
  
  
  
  A BGP extended community filter is similar to a community filter and is mainly used to filter VPN routes.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Perform either of the following operations as needed to configure an extended community filter.
     
     
     
     Configure a VPN-Target extended community filter:
     
     + Configure a basic VPN-Target extended community filter.
       
       ```
       [ip extcommunity-filter](cmdqueryname=ip+extcommunity-filter+basic+index+deny+permit+rt) { basic-extcomm-filter-num | basic basic-extcomm-filter-name }[ index index-number ]  { deny | permit } { rt { as-number:nn | 4as-number:nn | ipv4-address:nn } } &<1-16>
       ```
     + Configure an advanced VPN-Target extended community filter.
       
       ```
       [ip extcommunity-filter](cmdqueryname=ip+extcommunity-filter+advanced+index+deny+permit) { advanced-extcomm-filter-num | advanced advanced-extcomm-filter-name }[ index index-number ]  { deny | permit } regular-expression
       ```
     
     Configure a Site of Origin (SoO) extended community filter:
     
     + Configure a basic SoO extended community filter.
       
       ```
       [ip extcommunity-list soo basic](cmdqueryname=ip+extcommunity-list+soo+basic+index+permit+deny) basic-extcomm-filter-name [ index index-number ] { permit | deny } { site-of-origin } &<1-16>
       ```
     + Configure an advanced SoO extended community filter.
       
       ```
       [ip extcommunity-list soo advanced](cmdqueryname=ip+extcommunity-list+soo+advanced+index+permit+deny) advanced-extcomm-filter-name [ index index-number ] { permit | deny } regular-expression
       ```
     
     Multiple entries (or rules) can be defined in an extended community filter, and the relationship between them is OR, which means that the route matches the extcommunity filter if it matches one of the rules.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a route-policy.
  
  
  
  A route-policy is used to match routes or route attributes, and to change the attributes of routes that meet specific conditions. As the preceding filters can be used as matching conditions of a route-policy, the route-policy offers powerful functions and can be used flexibly.
  
  
  
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a route-policy node and enter the route-policy view.
     
     
     ```
     [route-policy](cmdqueryname=route-policy+permit+deny+node) route-policy-name { permit | deny } node node
     ```
     
     A route-policy consists of multiple nodes. For example, the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command defines node 10 and the [**route-policy**](cmdqueryname=route-policy) **route-policy-example deny node 20** command defines node 20. Both the nodes belong to the route-policy named **route-policy-example**, and the relationship between the nodes of a route-policy is OR. The details are as follows:
     
     + If a route matches one node, it matches the route-policy and will not be matched against the next node. In the preceding example, if a route matches the node defined using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command, the route will not be matched against the node defined using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example deny node 20** command.
     + If a route does not match any node, the route fails to match the route-policy.
     
     When a route-policy is used to filter a route, the route is first matched against the node with the smallest node ID. For example, if two nodes are configured using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** and [**route-policy**](cmdqueryname=route-policy) **route-policy-example deny node 20** commands, routes are first matched against the node configured using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     A route-policy denies all unmatched routes by default. If more than one node is defined in a route-policy, at least one should be set to permit mode.
  3. (Optional) Configure **if-match** clauses for the current route-policy node.
     
     
     
     **if-match** clauses are used to filter routes. If no **if-match** clause is specified, all routes will match the route-policy node.
     
     **Table 2** **if-match** clauses
     | Operation | Command | Description |
     | --- | --- | --- |
     | Match routes against an ACL. | [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* }  [**if-match ip next-hop acl**](cmdqueryname=if-match+ip+next-hop+acl) { *acl-number* | *acl-name* }  [**if-match ip route-source acl**](cmdqueryname=if-match+ip+route-source+acl) { *acl-number* | *acl-name* } | An ACL has been configured. |
     | Match routes against an IPv4 prefix list. | [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) *ip-prefix-name*  [**if-match ip next-hop**](cmdqueryname=if-match+ip+next-hop+ip-prefix) **ip-prefix** *ip-prefix-name*  [**if-match ip route-source**](cmdqueryname=if-match+ip+route-source+ip-prefix) **ip-prefix** *ip-prefix-name* | An IPv4 prefix list has been configured.  NOTE:  If the [**if-match acl**](cmdqueryname=if-match+acl) and [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) commands are both run in the same route-policy node, the latter configuration overrides the previous one. |
     | Match BGP routes against an AS\_Path filter. | [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) *apfIndex* &<1-16> | - |
     | Match BGP routes against a community filter. | + [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) { *basic-comm-filter-num* [ **whole-match** ] | *adv-comm-filter-num* } \* &<1-16> + [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) *comm-filter-name* [ **whole-match** ] + [**if-match community-filter**](cmdqueryname=if-match+community-filter+sort-match) { *adv-comm-filter-num* **sort-match** } \* &<1-16> + [**if-match community-filter**](cmdqueryname=if-match+community-filter+sort-match) *comm-filter-name* **sort-match** | - |
     | Match BGP routes against a Large-Community filter. | [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter+whole-match) *large-comm-filter-name* [ **whole-match** ] | - |
     | Match BGP routes against a VPN-Target extended community filter. | [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { { *basic-extcomm-filter-num* [ **matches-all** | **whole-match** ] | *adv-extcomm-filter-num* } &<1-16> | *extcomm-filter-name* [ **matches-all** | **whole-match** ] } | - |
     | Match BGP routes against an SoO extended community filter. | [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name* | - |
     
     There is no sequence between **if-match** clauses, and a node may have multiple **if-match** clauses or none at all.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The relationship between **if-match** clauses in a route-policy node is AND, meaning that a route must match all matching conditions before the action defined by an **apply** clause is taken on this route. For example, if two **if-match** clauses (**if-match acl 2003** and **if-match as-path-filter 100**) are defined in the route-policy node specified using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command, a route is considered to match node 10 only when it matches both **if-match** clauses.
  4. (Optional) Configure **apply** clauses for the current route-policy node.
     
     
     
     **apply** clauses can be used to set attributes for the routes matching the **if-match** clauses. If this step is not performed, the attributes of these routes remain unchanged.
     
     **Table 3** **apply** clauses
     | Operation | Command | Description |
     | --- | --- | --- |
     | Replace or add a specified AS number in the AS\_Path attribute of matched BGP routes. | [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete) *as-path-value* &<1-128> { **additive** | **overwrite** | **delete** }  [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete) *asValues* { **additive** | **overwrite** | **delete** } | - |
     | Delete a specified community attribute from matched BGP routes. | [**apply comm-filter**](cmdqueryname=apply+comm-filter+delete) { *basIndex* | *advIndex* } **delete** | NOTE:  The [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command deletes a specified community attribute from matched routes based on the referenced community filter. To delete multiple community attributes through one community filter, you need to run the [**ip community-filter**](cmdqueryname=ip+community-filter) command multiple times to configure multiple indexes for the filter, with each index corresponding to only one community attribute. If multiple community attributes are specified in the same index of the same community filter, none of them can be deleted in this case. |
     | Delete all the community attributes from a matched BGP route. | [**apply community**](cmdqueryname=apply+community+none) **none** | - |
     | Set community attributes for matched BGP routes. | + [**apply community**](cmdqueryname=apply+community+internet+no-advertise+no-export) { { *community-number* | *aa:nn* } &<1-32> | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } \* [ **additive** ] + [**apply community community-list**](cmdqueryname=apply+community+community-list+additive) *community-list-name* [ **additive** ] | NOTE:  Before running the [**apply community**](cmdqueryname=apply+community) **community-list** *community-list-name* command, you need to run the [**ip community-list**](cmdqueryname=ip+community-list) command to configure a BGP community list and run the [**community**](cmdqueryname=community) command to configure community attributes for the list. |
     | Delete Large-Community attributes from matched BGP routes. | [**apply large-community**](cmdqueryname=apply+large-community+none) **none** | - |
     | Set Large-Community attributes for matched BGP routes. | + [**apply large-community**](cmdqueryname=apply+large-community+additive+overwrite+delete) { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** } + [**apply large-community-list**](cmdqueryname=apply+large-community-list+additive+overwrite+delete) *large-community-list-name* { **additive** | **overwrite** | **delete** } | NOTE:  Before running the [**apply large-community-list**](cmdqueryname=apply+large-community-list) *large-community-list-name* command to set the BGP Large-Community attribute, run the [**ip large-community-list**](cmdqueryname=ip+large-community-list) command to configure a BGP Large-Community list and run the [**large-community**](cmdqueryname=large-community) command to configure values for the Large-Community list. |
     | Set VPN-Target extended community attributes for matched BGP routes. | [**apply extcommunity**](cmdqueryname=apply+extcommunity+rt+additive) { **rt** { *as-number:nn* | *ipv4-address:nn* } } &<1-16> [ **additive** ] | - |
     | Set SoO extended community attributes for matched BGP routes. | [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo+additive) { *site-of-origin* } &<1-16> **additive** | - |
     | Set the link bandwidth extended community attribute. | + [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+none) { *extCmntyString* | **none** } + [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+aggregate+limit) **aggregate** [ **limit** *bandwidth-value* ] | - |
     | Set the Local\_Pref for matched BGP routes. | [**apply local-preference**](cmdqueryname=apply+local-preference+%2B+-) [ **+** | **-** ] *preference* | - |
     | Set the Origin attribute for matched BGP routes. | [**apply origin**](cmdqueryname=apply+origin+egp+igp+incomplete) { **egp** { *egpVal* } | **igp** | **incomplete** } | - |
     | Set the PrefVal for matched BGP routes. | [**apply preferred-value**](cmdqueryname=apply+preferred-value) *preferredVal* | - |
     | Set the dampening parameters for matched EBGP routes. | [**apply dampening**](cmdqueryname=apply+dampening) *half-life-reach* *reuse* *suppress* *ceiling* | - |
     
     The **apply** clauses can be applied in any order, and a node may have multiple **apply** clauses or none at all.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```