Configuring BGP Filters
=======================

BGP filters can be used to flexibly filter routes to be advertised.

#### Context

BGP uses the following types of filters:

* [Access Control List (ACL)](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301901)
* [IP prefix list](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301902)
* [AS\_Path](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301903)
* [Community](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301904)
* [Large-community](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301907)
* [Extended community](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301905)
* [Route-policy](#EN-US_TASK_0000001398457589__step_dc_vrp_bgp_cfg_301906)
* [IP address list](#EN-US_TASK_0000001398457589__step123810234257)


#### Procedure

* Configure an ACL.
  
  
  
  An ACL is a series of sequential rules composed of permit and deny clauses. These rules specify source addresses, destination addresses, port numbers, and other information of data packets. ACL rules are used to classify data packets, and after the rules are applied to an interface on the Router, the Router uses the rules to permit or deny data packets.
  
  For details on ACL configurations, see HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - IP Services.
  
  An ACL can be used as a matching condition of a route-policy or directly used in the following commands:
  
  + [**filter-policy**](cmdqueryname=filter-policy+acl-name+export+direct+isis+ospf+rip+static) { *acl-number* | **acl-name** *acl-name* } **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ]
  + [**peer**](cmdqueryname=peer+filter-policy) { *group-name* | *ipv4-address* } [**filter-policy**](cmdqueryname=peer+filter-policy) { *acl-number* | **acl-name** *acl-name* } **export**
* Configure an IP prefix list.
  
  
  
  An IP prefix list is a type of filter used to filter routes based on destination addresses, and is identified by its name. An IP prefix list can be used flexibly to implement precise filtering. For example, it can be used to filter one route or routes to a network segment. If a large number of routes with different prefixes need to be filtered, configuring an IP prefix list to filter the routes is very complex.
  
  An IP prefix list can be used as a matching condition of a route-policy or directly used in the following commands:
  
  + [**filter-policy**](cmdqueryname=filter-policy+ip-prefix+export+direct+isis+ospf+rip+static) **ip-prefix** *ip-prefix-name* **export** [ **direct** | **isis** *process-id* | **ospf** *process-id* | **rip** *process-id* | **static** ]
  + [**peer**](cmdqueryname=peer+ip-prefix) { *group-name* | *ipv4-address* } [**ip-prefix**](cmdqueryname=peer+ip-prefix) *ip-prefix-name* **export**
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix+index+match-network+greater-equal+less-equal) *ip-prefix-name* [ **index** *index-number* ] *matchMode* *ipv4-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ] command to configure an IPv4 prefix list.
     
     
     
     The mask length range can be expressed as *mask-length* <= *greater-equal-value* <= *less-equal-value* <= 32. If only **greater-equal** is specified, the prefix range is [*greater-equal-value*, 32]. If only **less-equal** is specified, the prefix range is [*mask-length*, *less-equal-value*].
     
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
     
     During route matching, the system checks the entries identified by indexes in ascending order. If a route matches an entry, it is no longer matched against the next entry.
     
     The IP prefix list on the NE40E denies all unmatched routes by default. If all entries are in **deny** mode, all routes will be denied by the IP prefix list. In this case, after multiple entries are specified in **deny** mode, define an entry **permit 0.0.0.0 0 less-equal 32** to permit all the other IPv4 routes.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If more than one entry is defined in a prefix list, at least one of them must be set to **permit** mode.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure an AS\_Path filter.
  
  
  
  An AS\_Path filter is used to filter BGP routes based on the AS\_Path attributes they carry. If you do not want traffic to traverse some ASs, you can configure an AS\_Path filter to filter out the routes whose AS\_Path attributes contain the corresponding AS numbers. In addition, configuring an ACL or an IP prefix list to filter BGP routes may be complicated (as multiple ACLs or IP prefix lists need to be defined) and complicate maintenance of new routes. In this case, you can configure an AS\_Path filter.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If AS\_Path information is lost after route summarization, an AS\_Path filter can no longer filter summary routes. However, it can still filter specific routes, which carry AS\_Path information.
  
  An AS\_Path filter can be used as a filtering condition of a route-policy or be directly used in the [**peer as-path-filter**](cmdqueryname=peer+as-path-filter) command.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip as-path-filter**](cmdqueryname=ip+as-path-filter+index) { *as-path-filter-number* | *as-path-filter-name* } [ **index** *index-number* ]  **matchMode** *regular-expression* command to configure an AS\_Path filter.
     
     
     
     AS\_Path filters use regular expressions to define matching rules. A regular expression consists of metacharacters and values. For details, see [Table 1](#EN-US_TASK_0000001398457589__tab_dc_vrp_bgp_cfg_301901).
     
     + Metacharacter: defines matching rules.
     + Value: defines a matching object.
     
     **Table 1** Description of metacharacters
     | Metacharacter | Function | Example |
     | --- | --- | --- |
     | . | Matches any single character. | .\* matches any string in an AS\_Path and is used to match all routes. |
     | ^ | Indicates the beginning of a matched string. | ^65 matches strings beginning with 65.  + Examples of matched strings: 65, 651, 6501, and 65001 + Examples of unmatched strings: 165, 1650, 6650, and 60065 |
     | $ | Indicates the end of a matched string. | 65$ matches strings ending with 65.  + Examples of matched strings: 65, 165, 1065, 10065, and 60065 + Examples of unmatched strings: 651, 1650, 6650, 60650, and 65001 ^65$ matches AS\_Path 65.  NOTE:  ^$ matches an empty string (empty AS\_Path) and is usually used to match routes in the local AS. |
     | \_ | Matches a sign, such as a comma (,), left brace ({), right brace (}), left parenthesis ((), right parenthesis ()), and space. In addition, it can be used at the beginning of a regular expression with the same function as the caret sign (^) or at the end of a regular expression with the same function as the dollar sign ($). | + ^65001\_ matches the AS\_Paths that begin with 65001 followed by a sign. Specifically, ^65001\_ matches AS\_Paths with 65001 as the leftmost AS number (the number of the last AS through which a route passes), that is, the routes sent by peers in AS 65001. + \_65001\_ matches the strings (AS\_Paths) that contain 65001, that is, the routes that pass through AS 65001. + \_65001$ matches the AS\_Paths that end with a sign followed by 65001. Specifically, \_65001$ matches AS\_Paths with 65001 as the rightmost AS number (the number of the first AS through which a route passes), that is, the routes that originate in AS 65001. |
     | \ | Defines an escape character, which is used to mark the next character (common or special) as a common character. | An AS\_Confed\_Sequence contains parentheses. The parentheses in regular expressions provide special functions. To match such special characters by removing their special meanings, you can use the backslash (\). For example:  + \(65002\_ matches the AS\_Confed\_Sequences that begin with (65002 followed by a sign. Specifically, \(65002\_ matches AS\_Confed\_Sequences with 65002 as the leftmost AS number (the number of the last AS through which a route passes), that is, the routes sent by peers in AS 65002. + \(.\*\_65003\_.\*\) matches the AS\_Confed\_Sequence that contains AS number 65003, that is, the routes that pass through AS 65003 in a confederation. + \_65004\) matches a character string that ends with 65004) and is preceded by a sign. Specifically, \_65004\) matches AS\_Confed\_Sequences with the rightmost AS number (origin AS number), that is, the routes originating in AS 65004 in a confederation and the routes directly advertised by AS 65004 in the confederation. \_65004\) provides the same function as 65004\). Similarly, backslashes (\) can be used to remove the special meanings of the left bracket ([) and right bracket (]) used in an AS\_Confed\_Set and the left brace ({) and right brace (}) used in an AS\_Set. |
     | \* | Matches the strings in which the preceding character occurs zero or multiple times. | 65\* matches the AS\_Paths that begin with 6 and contain zero or multiple 5s.  + Examples of matched strings: 6, 65, 655, 6559, 65259, and 65529 + Examples of unmatched strings: 5, 56, 556, 5669, 55269, and 56259 |
     | + | Matches the strings in which the preceding character occurs one or more times. | 65+ matches the AS\_Paths that begin with 6 and contain one or multiple 5s.  + Examples of matched strings: 65, 655, 6559, 65259, and 65529 + Examples of unmatched strings: 56, 556, 5669, 55269, and 56259 |
     | ? | Matches the strings in which the preceding character occurs zero or one time. | 65? matches the AS\_Paths that begin with 6 and contain zero or one 5.  + Examples of matched strings: 6 and 65 + Examples of unmatched strings: 655, 6559, and 65529 |
     | () | Matches a sub-regular expression within the parentheses, and obtains the matching result. The parentheses can also be empty. | 100(200)+ matches 100200, 100200200, and so on. |
     | x|y | Matches x or y. | 100|65002|65003 matches 100, 65002, or 65003. |
     | [xyz] | Matches any character in the regular expression. | [896] matches 8, 9, or 6. |
     | [^xyz] | Matches any character that is not contained in the regular expression. | [^896] matches any character, except 8, 9, and 6. |
     | [a-z] | Matches any character within the specified range. | [2-4] matches 2, 3, and 4; [0-9] matches any digits from 0 to 9.  NOTE:  The values in the square brackets ([]) must be digits from 0 to 9. For example, to match a number ranging from 735 to 907, use the regular expression of (73[5-9]|7[4-9][0-9]|8[0-9][0-9]|90[0-7]). |
     | [^a-z] | Matches any character beyond the specified range. | [^2-4] matches characters other than 2, 3, and 4. [^0-9] matches characters other than digits 0 through 9. |
     
     You can define multiple rules (permit or deny) for the same filter. During the matching, the relationship between these rules is OR. If a route meets one of the matching rules, it matches this AS\_Path filter.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + For details about a regular expression, see the *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - Basic Configurations*.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a community filter.
  
  
  
  A BGP community attribute is used to identify a group of routes with the same properties. Routes can be classified through the community attribute, which facilitates route management.
  
  In actual application, some AS internal routes may not need to be advertised to other ASs, while some AS external routes need to be advertised to other ASs. Both internal and external routes may have different prefixes (making an IP prefix list unsuitable), and may come from different ASs (making an AS\_Path filter unsuitable). In this case, you can set a community value for the AS internal routes and another community value for the AS external routes on an AS edge device to control and filter routes.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ip community-filter**](cmdqueryname=ip+community-filter+index) **adv-comm-filter-num** [ ****index**** **index-number** ] **matchMode** **regular-expression** command to configure a community filter.
     
     
     + To configure a standard community filter, run the [**ip community-filter basic**](cmdqueryname=ip+community-filter+basic+index+internet+no-advertise+no-export) *basCfName* [ **index** *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20> or [**ip community-filter**](cmdqueryname=ip+community-filter+index+internet+no-advertise+no-export) *cfIndex* [ **index** *index-val* ] *matchMode* [ *cmntyStr* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** ] &<1-20> command.
     + To configure an advanced community filter, run the [**ip community-filter**](cmdqueryname=ip+community-filter+advanced+advanced+index+permit+deny) { **advanced** *comm-filter-name* | **advanced** *adv-comm-filter-num* } [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a Large-community filter.
  
  
  
  The Large-community attribute can completely represent a 2-byte or 4-byte AS number, and has two 4-byte LocalData fields, allowing the administrator to flexibly use route-policies. As an enhancement to community attributes, Large-Community can be used together with community attributes.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Configure a Large-Community filter.
     
     
     + To configure a basic Large-Community filter, run the [**ip large-community-filter**](cmdqueryname=ip+large-community-filter+basic+index+permit+deny) **basic** *large-comm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } { *aa:bb:cc* } &<1-16> command.
     + To configure an advanced Large-Community filter, run the [**ip large-community-filter**](cmdqueryname=ip+large-community-filter+advanced+index+permit+deny) **advanced** *large-comm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure an extended community filter.
  
  
  
  Similar to a community filter, an extended community filter is mainly used to filter VPN routes.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Configure the following extended community filters as needed.
     
     
     
     To configure a VPN-Target extended community filter:
     
     + To configure a basic VPN-Target extended community filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter+basic+index+deny+permit+rt) { *basic-extcomm-filter-num* | **basic** *basic-extcomm-filter-name* } [ **index** *index-number* ] { **deny** | **permit** } { **rt** *extCmntyStr* } &<1-16> command.
     + To configure an advanced VPN-Target extended community filter, run the [**ip extcommunity-filter**](cmdqueryname=ip+extcommunity-filter+advanced+index+deny+permit) { *advanced-extcomm-filter-num* | **advanced** *advanced-extcomm-filter-name* }[ **index** *index-number* ]  { **deny** | **permit** } *regular-expression* command.
     
     To configure an SoO extended community filter:
     
     + To configure a basic SoO extended community filter, run the [**ip extcommunity-list soo basic**](cmdqueryname=ip+extcommunity-list+soo+basic+index+permit+deny) *basic-extcomm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } { *site-of-origin* } &<1-16> command.
     + To configure an advanced SoO extended community filter, run the [**ip extcommunity-list soo advanced**](cmdqueryname=ip+extcommunity-list+soo+advanced+index+permit+deny) *advanced-extcomm-filter-name* [ **index** *index-number* ] { **permit** | **deny** } *regular-expression* command.
     
     Multiple entries can be defined in one extended community filter identified either by a name or number. The relationship between the entries is "OR". This means that if a route matches one of the rules, the route matches the filter.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure a route-policy.
  
  
  
  A route-policy is used to match routes or route attributes, and to change route attributes when the matching rules are met. As the preceding filters can be used as matching conditions of a route-policy, the route-policy offers powerful functions and can be used flexibly.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* **matchMode** **node** *node* command to configure a route-policy with a node and enter the route-policy view.
     
     
     
     A route-policy may consist of multiple nodes. For example, the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command defines node 10 and the [**route-policy**](cmdqueryname=route-policy) **route-policy-example deny node 20** command defines node 20. Both nodes belong to the route-policy named **route-policy-example**. The relationship between the nodes of a route-policy is OR. There are two situations:
     
     + If a route matches one node, it matches the route-policy and will not be matched against the next node. In the preceding example, if a route matches the node defined using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command, the route will not be matched against the node defined using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example deny node 20** command.
     + If a route does not match any node, the route fails to match the route-policy.
     
     When a route-policy is used to filter routes, the routes are first matched against the node with the smallest node ID. For example, if two nodes are configured using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** and [**route-policy**](cmdqueryname=route-policy) **route-policy-example deny node 20** commands, routes are first matched against the node configured using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     On the NE40E, all unmatched routes are denied by the route-policy by default. If more than one node is defined in a route-policy, at least one of them must be in **permit** mode.
  3. (Optional) Configure **if-match** clauses for the current route-policy node.
     
     
     
     **if-match** clauses are used to filter routes. If no **if-match** clause is specified for a node, all routes will match the node.
     
     + To configure an ACL-based matching rule, run the [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* } command.
     + To match routes against an IP prefix list, run the [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) *ip-prefix-name* command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the [**if-match acl**](cmdqueryname=if-match+acl) and [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) commands are both configured in the same route-policy node, the latter configuration overrides the previous one.
     + To match the AS\_Path attribute of BGP routes, run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) *apfIndex* &<1-16> command.
     + To match the community attribute of BGP routes, run either of the following commands:
       
       - [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) { *basic-comm-filter-num* [ **whole-match** ] | *adv-comm-filter-num* [ **sort-match** ] }\* &<1-16>
       - [**if-match community-filter**](cmdqueryname=if-match+community-filter+whole-match) *comm-filter-name* [ **whole-match** | **sort-match** ]
     + To match the Large-Community attribute of BGP routes, run the [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter+whole-match) *large-comm-filter-name* [ **whole-match** ] command.
     + To match the VPN target extended community attribute of BGP routes, run the [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) { { *basic-extcomm-filter-num* [ **matches-all** | **whole-match** ] | *adv-extcomm-filter-num* } &<1-16> | *extcomm-filter-name* [ **matches-all** | **whole-match** ] } command.
     + To match the SoO extended community attribute of BGP routes, run the [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name* command.
     
     The operations in Step 3 can be performed in any order. A node may have multiple **if-match** clauses or none at all.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The relationship between **if-match** clauses in a route-policy node is AND, meaning that a route must match all matching conditions before the action defined by an **apply** clause is taken on this route. For example, if two **if-match** clauses (**if-match acl 2003** and **if-match as-path-filter 100**) are defined in the route-policy node specified using the [**route-policy**](cmdqueryname=route-policy) **route-policy-example permit node 10** command, a route is considered to match node 10 only when it matches both **if-match** clauses.
  4. (Optional) Configure **apply** clauses for the current route-policy node.
     
     
     
     **apply** clauses can be used to set attributes for the routes matching the **if-match** clauses. If this step is not performed, the attributes of the routes matching the **if-match** clause remain unchanged.
     
     + To replace the AS numbers in the AS\_Path attribute of BGP routes or add the specified AS number to the AS\_Path attribute, run the [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete+additive+overwrite) { *as-path-value* } &<1-128>{ **additive** | **overwrite** | **delete** } or [**apply as-path**](cmdqueryname=apply+as-path+additive+overwrite+delete) *asValues* { **additive** | **overwrite** | **delete** } command.
     + To delete a specified BGP community attribute, run the [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The [**apply comm-filter delete**](cmdqueryname=apply+comm-filter+delete) command deletes a specified community attribute from matched routes based on the referenced community filter. To delete multiple community attributes through one community filter, you need to run the [**ip community-filter**](cmdqueryname=ip+community-filter) command multiple times to configure multiple indexes for the filter, with each index corresponding to only one community attribute. If multiple community attributes are specified in the same index of the same community filter, none of them can be deleted in this case. For detailed examples, see the HUAWEI NE40E-M2 seriesUniversal Service Router Command Reference.
     + To delete community attributes from matched BGP routes, run the [**apply community**](cmdqueryname=apply+community+none) **none** command.
     + To set the community attribute of matched BGP routes, run the [**apply community**](cmdqueryname=apply+community+internet+no-advertise+no-export) { *cmntyValue* | *cmntyNum* | **internet** | **no-advertise** | **no-export** | **no-export-subconfed** } &<1-32> [ **additive** ] or [**apply community**](cmdqueryname=apply+community+community-list) **community-list** *community-list-name* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       A BGP community list must have been configured using the [**ip community-list**](cmdqueryname=ip+community-list) command and community attributes must have been configured for the list using the [**community**](cmdqueryname=community) command before you run the [**apply community**](cmdqueryname=apply+community+community-list) **community-list** *community-list-name* command.
     + To delete the Large-Community attribute of BGP routes, run the [**apply large-community**](cmdqueryname=apply+large-community+none) **none** command.
     + To set the Large-Community attribute for BGP routes, run the [**apply large-community**](cmdqueryname=apply+large-community+additive+overwrite+delete+additive) { *aa:bb:cc* } &<1-16> { **additive** | **overwrite** | **delete** } or [**apply large-community-list**](cmdqueryname=apply+large-community-list+additive+overwrite+delete) *large-community-list-name* { **additive** | **overwrite** | **delete** } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Before running the [**apply large-community-list**](cmdqueryname=apply+large-community-list) *large-community-list-name* command to set the BGP Large-Community attribute, run the [**ip large-community-list**](cmdqueryname=ip+large-community-list) command to configure a BGP Large-Community list and run the [**large-community**](cmdqueryname=large-community) command to configure values for the Large-Community list.
     + To set the BGP VPN target extended community attribute, run the [**apply extcommunity**](cmdqueryname=apply+extcommunity+rt+additive) { **rt** *extCmntyValue* } &<1-16> [ **additive** ] command.
     + To set the BGP SoO extended community attribute, run the [**apply extcommunity soo**](cmdqueryname=apply+extcommunity+soo+additive) { *site-of-origin* } &<1-16> **additive** command.
     + To set the bandwidth extended community attribute, run the [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+none) { *extCmntyString* | **none** } or [**apply extcommunity bandwidth**](cmdqueryname=apply+extcommunity+bandwidth+aggregate+limit) **aggregate** [ **limit** *bandwidth-value* ] command.
     + To set the Local\_Pref attribute for matched BGP routes, run the [**apply local-preference**](cmdqueryname=apply+local-preference+%2B+-) [ **+** | **-** ] *preference* command.
     + To set the Origin attribute for matched BGP routes, run the [**apply origin**](cmdqueryname=apply+origin+egp+igp+incomplete) { **egp** { *egpVal* } | **igp** | **incomplete** } command.
     + To set a preferred value for matched BGP routes, run the [**apply preferred-value**](cmdqueryname=apply+preferred-value) *preferred-value* command.
     + To set dampening parameters for EBGP routes, run the [**apply dampening**](cmdqueryname=apply+dampening) *half-life-reach* *reuse* *suppress* *ceiling* command.
     
     The operations in Step 4 can be performed in any order. A node may have multiple **apply** clauses or no **apply** clause.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure an IP address list.
  
  
  
  Before configuring a conditional BGP route advertisement policy, you need to create an IP address list.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the **filter-list ip-prefix** *name* command to create an IP address list and enter the ip-prefix-list view.
  3. Run the [**prefix**](cmdqueryname=prefix) *address* *maskLen* command to configure an IP address and mask for the IP address list.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.