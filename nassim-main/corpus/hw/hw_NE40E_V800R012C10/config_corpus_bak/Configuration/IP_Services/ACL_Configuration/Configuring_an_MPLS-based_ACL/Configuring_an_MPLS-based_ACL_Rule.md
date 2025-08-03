Configuring an MPLS-based ACL Rule
==================================

MPLS-based ACL rules are defined based on MPLS packets' EXP, label, or TTL values to filter packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl+name+mpls+mpls+number+number) { **name** *mpls-acl-name* { **mpls** | [ **mpls** ] **number** *mpls-acl-number* } | [ **number** ] *mpls-acl-number* }
   
   
   
   The MPLS-based ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule+name+permit+deny+exp+any+label+any+ttl+lt+eq+gt+range+any) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ [ **exp** { *exp-value* | **any** } &<1-4> ] | [ **label** { *label-value* | **any** } &<1-4> ] | [ **ttl** { { **lt** | **eq** | **gt** } *ttlBegin* | **range** *ttlBegin* *ttlEnd* | **any** } &<1-3> ] ] \*
   
   
   
   Rules are configured for the MPLS-based ACL.
   
   
   
   * Adding new rules to an ACL will not affect the existing rules.
   * If an existing rule is edited and the edited content conflicts with the original one, the edited content takes effect.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) When you configure a rule for an MPLS-based ACL:
   * If an EXP value is specified by configuring **exp**, a label value is specified by configuring **label**, and a TTL value is specified by configuring **ttl**, the system filters only the packets with the specified EXP, label, and TTL values.
   * If all EXP, label, and TTL values are specified by configuring **any**, the system does not check MPLS packets' EXP, label, and TTL values, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   The description for an ACL rule is configured.
   
   
   
   The description of an ACL rule can contain the functions of the ACL rule. Configuring a description for an ACL rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL rules are configured, and their functions are difficult to identify.
   * An ACL rule is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.