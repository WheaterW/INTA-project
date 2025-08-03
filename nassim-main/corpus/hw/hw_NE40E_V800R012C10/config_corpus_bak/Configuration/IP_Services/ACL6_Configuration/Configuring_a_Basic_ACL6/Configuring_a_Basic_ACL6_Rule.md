Configuring a Basic ACL6 Rule
=============================

Basic ACL6 rules are defined based on whether the packets are the first fragments, packets' source IP addresses, and VPN instances to filter packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+basic+number+match-order+config+auto) { **name** *basic-acl6-name* [ **basic** ] | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The basic ACL6 view is displayed.
3. Run [**rule**](cmdqueryname=rule+name+permit+deny+fragment+source+any+time-range) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address/prefix-length* | **any** } | **time-range** *time-name* | [ { **vpn-instance** | **vpn6-instance** } *vpn-instance-name* | **vpn-instance-any** ] ] \*
   
   
   
   A rule is configured for the basic ACL6.
   
   
   
   * Adding new rules to an ACL6 will not affect the existing rules.
   * When an existing rule is edited and the edited contents conflict with the original contents, the edited contents take effect.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you configure a basic ACL6:
   
   * If a source IPv6 address is specified by configuring **source**, the system filters only packets with this specified source IPv6 address.
   * If all source IPv6 addresses are specified by configuring **any**, the system does not check packets' source IPv6 addresses, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
   * If a validity period is specified by configuring **time-range**, the time range name specified by *time-name* must already exist. Otherwise, the configuration does not take effect.
   * If you delete the IPv6 addresses specified in an ACL6 rule by running the **undo rule** command, filtering will not be performed based on IPv6 addresses, potentially causing service interruptions. The service interruption risk warning function, enabled by default, indicates that such configuration may adversely affect services. If the function is disabled, run the **undo configuration prevent-misoperation disable** command to enable it.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   A description is configured for the rule.
   
   
   
   The description of an ACL6 rule can contain the functions of the ACL6 rule. Configuring a description for an ACL6 rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL6s are configured, and their functions are difficult to identify.
   * An ACL6 is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.