Configuring a Tunnel Selector
=============================

A tunnel selector comprises **if-match** and **apply** clauses. The **if-match** clause defines route filtering rules, whereas the **apply** clause applies a tunnel policy to routes that match the **if-match** clause.

#### Context

A tunnel selector allows routes to recurse to tunnels based on set route filtering rules as expected.

A tunnel selector comprises the following parts:

* **if-match** clause: filters routes by route attribute, such as the RD and next hop.
* **apply** clause: applies a tunnel policy to routes that match the **if-match** clause.

Perform the following steps on the PE or ASBR where a tunnel policy needs to be applied.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**tunnel-selector**](cmdqueryname=tunnel-selector) *tunnel-selector-name* { **permit** | **deny** } **node** *node* command to create a tunnel selector and enter the tunnel selector view.
3. (Optional) Configure the **if-match** clause.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the **if-match** clause is not configured, all routes are permitted.
   
   Run the following commands as needed to configure one or more route filtering rules for the current tunnel selector node. If you skip this step, all VPNv4, VPNv6, and labeled BGP-IPv4 routes are permitted.
   
   
   
   1. To match the RDs of routes, run the [**if-match rd-filter**](cmdqueryname=if-match+rd-filter) *rd-filter-number* command.
   2. To match the IPv4 next hops of routes, run the [**if-match ip next-hop**](cmdqueryname=if-match+ip+next-hop) { **acl** { *acl-number* | *acl-name* } | **ip-prefix** *ip-prefix-name* } command.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) The **acl** { *acl-number* | *acl-name* } parameter can be used only if either or both of the following steps have been performed:
      * Configure basic ACL rules:
        1. Run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
        2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \* command to configure ACL rules.
      * Configure advanced ACL rules:
        1. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
        2. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } | **time-range** *time-name*] \* command to configure ACL rules.
      The rules for using the **permit** and **deny** keywords are as follows:
      * If the action specified in an ACL rule is **permit**, a route that matches this rule is considered to have passed the check by the **if-match** clause.
      * If the action specified in an ACL rule is **deny**, a route that matches this rule is considered to have failed the check by the **if-match** clause.
      * If a route does not match any ACL rules, the route is considered to have failed the check by the **if-match** clause.
      * If an ACL does not contain any rules, all routes are considered to have failed the check by the **if-match** clause.
      * In a tunnel selector where the first node is a **permit** node, if a route has passed the check by the **if-match** clause, the system will take the action specified in the **apply** clause on this route. If the route has not passed the check by the **if-match** clause, the system will take the action specified in the **apply** clause in the next node in the tunnel selector.
      * In a tunnel selector where the first node is a **deny** node, if a route has passed the check by the **if-match** clause, the system will not take the action specified in the **apply** clause on this route. If the route has not passed the check by the **if-match** clause, the system will take the action specified in the **apply** clause in the next node in the tunnel selector.
   3. To match the IPv6 next hops of routes, run the [**if-match ipv6 next-hop**](cmdqueryname=if-match+ipv6+next-hop) **prefix-list** *ipv6-prefix-name* command.
   4. To match the IP prefixes of routes, run the [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) command.
   5. To match the community attributes of routes, run the [**if-match community-filter**](cmdqueryname=if-match+community-filter) command.
4. Run the [**apply tunnel-policy**](cmdqueryname=apply+tunnel-policy) *tunnel-policy-name* command to apply a tunnel policy to routes.
5. (Optional) Run the [**apply segment-routing ipv6**](cmdqueryname=apply+segment-routing+ipv6) { **best-effort** | **traffic-engineer** } \* command to enable route recursion based on the SID attributes carried in routes.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.