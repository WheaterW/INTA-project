(Optional) Configuring an if-match Clause
=========================================

The **if-match** clauses define the matching rules that are used to match certain route attributes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
   
   
   
   The route-policy view is displayed.
3. Configure **if-match** clauses in the route-policy.
   
   
   * Based on a basic ACL:
     1. Run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
     2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \* command to configure a rule for the ACL.
     3. Run the [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* } command to configure an ACL-based matching rule.
     4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     
     When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
     
     When a filtering policy of a routing protocol is used to filter routes:
     + If the action specified in an ACL rule is **permit**, a route that matches the rule will be received or advertised by the system.
     + If the action specified in an ACL rule is **deny**, a route that matches the rule will not be received or advertised by the system.
     + If a route has not matched any ACL rules, the route will not be received or advertised by the system.
     + If an ACL does not contain any rules, all routes matching the **route-policy** that references the ACL will not be received or advertised by the system.
     + In the configuration order, the system first matches a route with a rule that has a smaller number and then matches the route with a rule with a larger number. Routes can be filtered using a blacklist or a whitelist:
       
       Route filtering using a blacklist: Configure a rule with a smaller number and specify the action **deny** in this rule to filter out the unwanted routes. Then, configure another rule with a larger number in the same ACL and specify the action **permit** in this rule to receive or advertise the other routes.
       
       Route filtering using a whitelist: Configure a rule with a smaller number and specify the action **permit** in this rule to permit the routes to be received or advertised by the system. Then, configure another rule with a larger number in the same ACL and specify the action **deny** in this rule to filter out unwanted routes.
   * To configure a rule to match routes against a specified cost, run the [**if-match cost**](cmdqueryname=if-match+cost) *cost* or [**if-match cost**](cmdqueryname=if-match+cost) { **greater-equal** *greater-equal-value* [ **less-equal** *less-equal-value* ] | **less-equal** *less-equal-value* } command.
   * To configure a rule to match routes against a specified outbound interface, run the [**if-match interface**](cmdqueryname=if-match+interface) { { *interface-name* | *interface-type* *interface-number* } &<1-16> } command.
   * To configure a rule to match routes against a specified route preference, run the [**if-match preference**](cmdqueryname=if-match+preference) *preference* command.
   * To configure a rule to match IPv4 routes against a specified next hop or source address, run the [**if-match ip**](cmdqueryname=if-match+ip) { **next-hop** | **route-source** | **group-address** } { **acl** { *acl-number* | *acl-name* } | **ip-prefix** *ip-prefix-name* } command.
   * To configure a rule to match routes against a specified IP prefix list, run the [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) *ip-prefix-name* command.
   * To configure a rule to IPv6 routes, run the [**if-match ipv6**](cmdqueryname=if-match+ipv6) { **address** | **next-hop** | **route-source** } { **acl** { *acl-number* | *acl-name* } | **prefix-list** *ipv6-prefix-name* } command.
   * Run any of the following commands as needed to match routes of a specific type:
     + To configure a rule to match OSPF routes of a specified type, run the [**if-match route-type**](cmdqueryname=if-match+route-type) { **external-type1** | **external-type1or2** | **external-type2** | **internal** | **nssa-external-type1** | **nssa-external-type1or2** | **nssa-external-type2** } command.
     + To configure a rule to match IS-IS routes of a specified level, run the [**if-match route-type**](cmdqueryname=if-match+route-type) { **is-is-level-1** | **is-is-level-2** } command.
     + To configure a rule to match BGP routes, run the [**if-match route-type**](cmdqueryname=if-match+route-type) { **ibgp** | **ebgp** } command.
     + To configure a rule to match MVPN routes, run the [**if-match route-type**](cmdqueryname=if-match+route-type) **mvpn** { **1** | **3** } \* command.
     + To configure a rule to match EVPN routes, run the [**if-match route-type**](cmdqueryname=if-match+route-type) **evpn** { **ad** | **es** | **inclusive** | **mac** | **prefix** | **join** | **leave** | **smet** } \* command.
     + To match BGP-LS routes, run the [**if-match route-type bgp-ls**](cmdqueryname=if-match+route-type+bgp-ls) { **node** | **link** | **ipv4-prefix** | **ipv6-prefix** } \* command.
   * To configure a rule to match routes carrying a specified tag value, run the [**if-match tag**](cmdqueryname=if-match+tag) *tag* command.
   * To configure a rule to match routes of a specific type of protocol, run the [**if-match protocol**](cmdqueryname=if-match+protocol) { **direct** | **static** | **rip** | **ripng** | **ospf** | **ospfv3** | **bgp** | **isis** | **unr** } \* command.
   * To configure a rule to match routes against a specified AS\_Path length, run the [**if-match as-path length**](cmdqueryname=if-match+as-path+length) command.
   * To configure a rule to match routes against a specified AS\_Path filter, run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) command.
   * To configure a rule to match routes against a specified community filter, run the [**if-match community-filter**](cmdqueryname=if-match+community-filter) command.
   * To configure a rule to match routes against a specified extcommunity filter, run any of the following commands as needed:
     + To match routes against a VPN target extcommunity filter, run the [**if-match extcommunity-filter**](cmdqueryname=if-match+extcommunity-filter) command.
     + To match routes against an encapsulation extcommunity filter, run the [**if-match extcommunity-list encapsulation**](cmdqueryname=if-match+extcommunity-list+encapsulation) *encapsulation-name* command.
     + To match routes against an SoO extcommunity filter, run the [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name* command.
     + To match routes against a segmented-nh extcommunity filter, run the [**if-match extcommunity-list segmented-nh**](cmdqueryname=if-match+extcommunity-list+segmented-nh) *segmented-nh-name* command.
   * To configure a rule to match routes against a specified Large-Community filter, run the [**if-match large-community-filter**](cmdqueryname=if-match+large-community-filter) *lcfName* [ **whole-match** ] command.
   * To configure a rule to match routes against a specified RD filter, run the [**if-match rd-filter**](cmdqueryname=if-match+rd-filter) *rd-filter-number* command.
   * To configure a rule to match BGP routes against a specified origin AS validation result, run the [**if-match rpki origin-as-validation**](cmdqueryname=if-match+rpki+origin-as-validation) { **valid** | **invalid** | **not-found** } command.
   * To configure a rule to match routes against a specified MPLS label, run the [**if-match mpls-label**](cmdqueryname=if-match+mpls-label) command.
   * To configure a rule to match routes against a specified MPLS Label2 value, run the [**if-match**](cmdqueryname=if-match) **mpls-label2** command.
   * To configure a rule to match routes against a specified Layer 2 VNI list, run the [**if-match l2vni**](cmdqueryname=if-match+l2vni) [ *l2vni-list-name* ] command.
   * To configure a rule to match routes against a specified Layer 3 VNI list, run the [**if-match l3vni**](cmdqueryname=if-match+l3vni) [ *l3vni-list-name* ] command.
   * To configure a rule to match routes against a specified MAC address list, run the [**if-match mac-list**](cmdqueryname=if-match+mac-list) *mac-list-name* command.
   * To configure a rule to match routes against a specified Ethernet tag list, run the [**if-match eth-tag-list**](cmdqueryname=if-match+eth-tag-list) *eth-tag-list-name* command.
   * To configure a rule to match routes against a multicast address, run the [**if-match ip**](cmdqueryname=if-match+ip) **group-address** { **acl** { *acl-number* | *acl-name* } | **ip-prefix** *ip-prefix-name* } command.
   * To configure a rule to match NG MVPN routes against the IP address of a route advertiser, run the [**if-match ip route-originator**](cmdqueryname=if-match+ip+route-originator) { **ip-prefix** *ip-prefix-name* | **acl** { *acl-number* | *acl-name* } } command.
   * To match non-optimal BGP routes, run the [**if-match route-state bgp-not-best**](cmdqueryname=if-match+route-state+bgp-not-best) command.
   * To configure a rule to match the source IP address in the BGP Flow Specification route prefix, run the [**if-match flowspec source ip-prefix**](cmdqueryname=if-match+flowspec+source+ip-prefix) *ip-prefix-name* command.
   * To configure a rule to match the source IPv6 address in the BGP Flow Specification route prefix, run the [**if-match flowspec source ipv6 prefix-list**](cmdqueryname=if-match+flowspec+source+ipv6+prefix-list) *ipv6-prefix-name* command.
   * To configure a rule to match the destination IP address in the BGP Flow Specification route prefix, run the [**if-match flowspec destination ip-prefix**](cmdqueryname=if-match+flowspec+destination+ip-prefix) *ip-prefix-name* command.
   * To configure a rule to match the destination IPv6 address in the BGP Flow Specification route prefix, run the [**if-match flowspec destination ipv6 prefix-list**](cmdqueryname=if-match+flowspec+destination+ipv6+prefix-list) *ipv6-prefix-name* command.
   
   The commands in Step 3 can be run in any required order. A node may have multiple **if-match** clauses or no **if-match** clause.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) If multiple **if-match** clauses of a node in a route-policy define the same matching condition type, the relationship between them is "OR"; if the **if-match** clauses define different matching condition types, the relationship between these clauses is "AND". If you run any of the following **if-match** commands more than once, the latest configuration overrides the previous one:
   * [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* }
   * [**if-match cost**](cmdqueryname=if-match+cost) *cost*
   * [**if-match extcommunity-list soo**](cmdqueryname=if-match+extcommunity-list+soo) *extcomm-filter-name*
   * [**if-match ip**](cmdqueryname=if-match+ip) **next-hop** { **acl** { *acl-number* | *acl-name* } | **ip-prefix** *ip-prefix-name* }
   * [**if-match ip**](cmdqueryname=if-match+ip) **route-source** { **acl** { *acl-number* | *acl-name* } | **ip-prefix** *ip-prefix-name* }
   * [**if-match ip**](cmdqueryname=if-match+ip) **group-address** { **acl** { *acl-number* | *acl-name* } | **ip-prefix** *ip-prefix-name* }
   * [**if-match ip route-originator**](cmdqueryname=if-match+ip+route-originator) { **ip-prefix** *ip-prefix-name* | **acl** { *acl-number* | *acl-name* } }
   * [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) *ip-prefix-name*
   * [**if-match ipv6**](cmdqueryname=if-match+ipv6) **address** { **acl** { *acl-number* | *acl-name* } | **prefix-list** *ipv6-prefix-name* }
   * [**if-match ipv6**](cmdqueryname=if-match+ipv6) **next-hop**  { **acl** { *acl-number* | *acl-name* } | **prefix-list** *ipv6-prefix-name* }
   * [**if-match ipv6**](cmdqueryname=if-match+ipv6) **route-source**  { **acl** { *acl-number* | *acl-name* } | **prefix-list** *ipv6-prefix-name* }
   * [**if-match rd-filter**](cmdqueryname=if-match+rd-filter) *rd-filter-number*
   * [**if-match rpki origin-as-validation**](cmdqueryname=if-match+rpki+origin-as-validation) { **invalid** | **not-found** | **valid** }
   * [**if-match tag**](cmdqueryname=if-match+tag) *tag*
   * [**if-match preference**](cmdqueryname=if-match+preference) *preference*
   * [**if-match protocol**](cmdqueryname=if-match+protocol) { **direct** | **static** | **rip** | **ripng** | **ospf** | **ospfv3** | **bgp** | **isis** | **unr** } \*
   * [**if-match**](cmdqueryname=if-match) { **mpls-label** | **mpls-label2** } \*
   * [**if-match as-path length**](cmdqueryname=if-match+as-path+length)
   * [**if-match l2vni**](cmdqueryname=if-match+l2vni) [ *l2vni-list-name* ]
   * [**if-match l3vni**](cmdqueryname=if-match+l3vni) [ *l3vni-list-name* ]
   * [**if-match mac-list**](cmdqueryname=if-match+mac-list) *mac-list-name*
   * [**if-match eth-tag-list**](cmdqueryname=if-match+eth-tag-list) *eth-tag-list-name*
   * [**if-match extcommunity-list encapsulation**](cmdqueryname=if-match+extcommunity-list+encapsulation) *encapsulation-name*
   * [**if-match extcommunity-list segmented-nh**](cmdqueryname=if-match+extcommunity-list+segmented-nh) *segmented-nh-name*
   * [**if-match route-state bgp-not-best**](cmdqueryname=if-match+route-state+bgp-not-best)
   * [**if-match flowspec source ip-prefix**](cmdqueryname=if-match+flowspec+source+ip-prefix) *ip-prefix-name*
   * [**if-match flowspec source ipv6 prefix-list**](cmdqueryname=if-match+flowspec+source+ipv6+prefix-list) *ipv6-prefix-name*
   * [**if-match flowspec destination ip-prefix**](cmdqueryname=if-match+flowspec+destination+ip-prefix) *ip-prefix-name*
   * [**if-match flowspec destination ipv6 prefix-list**](cmdqueryname=if-match+flowspec+destination+ipv6+prefix-list) *ipv6-prefix-name*
   
   If no **if-match** clause is specified, all routes will match the route-policy node.
   
   You are advised not to use the same route-policy to filter both IPv4 and IPv6 routes when the **[**route-policy address-family mismatch-deny**](cmdqueryname=route-policy+address-family+mismatch-deny)** command is not configured. Otherwise, services may be interrupted in the following scenarios:
   1. For the same **route-policy**, some nodes match IPv4 routes, and some nodes match IPv6 routes.
   2. A **route-policy** matches only IPv4 routes, but the **route-policy** is referenced by IPv6.
   3. A **route-policy** matches only IPv6 routes, but the **route-policy** is referenced by IPv4.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.