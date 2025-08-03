Configuring an Interface-based ACL6 Rule
========================================

Interface-based ACL6 rules are defined based on packets' inbound interfaces to filter packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+interface+number+match-order+config+auto) { **name** *interface-based-acl6-name* **interface** | **number** *interface-based-acl6-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The interface-based ACL6 view is displayed.
3. Run [**rule**](cmdqueryname=rule+name+permit+deny+interface+any+time-range) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } **interface** { *interface-name* | **any** | *interface-type* *interface-number* } [ **time-range** *time-name* ] \*
   
   
   
   A rule is configured for the interface-based ACL6.
   
   
   
   * Adding new rules to an ACL6 will not affect the existing rules.
   * When an existing rule is edited and the edited contents conflict with the original contents, the edited contents take effect.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you configure an interface-based ACL6:
   
   * If an interface is specified by configuring **interface**, the system filters only packets received by this specified interface.
   * If all interfaces are specified by configuring **any**, the system does not check packets' inbound interfaces, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
   * If a validity period is specified by configuring **time-range**, the time range name specified by *time-name* must already exist. Otherwise, the configuration does not take effect.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   A description is configured for the rule.
   
   
   
   The description of an ACL6 rule can contain the functions of the ACL6 rule. Configuring a description for an ACL6 rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL6s are configured, and their functions are difficult to identify.
   * An ACL6 is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.