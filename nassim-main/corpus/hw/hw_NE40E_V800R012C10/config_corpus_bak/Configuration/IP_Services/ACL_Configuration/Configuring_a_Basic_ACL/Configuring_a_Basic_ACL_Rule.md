Configuring a Basic ACL Rule
============================

Basic ACL rules are defined based on whether the packets are the first fragments, packets' source IP addresses, and VPN instances to filter packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl+name+basic+basic+number+number+match-order+config+auto) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The basic ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule+name+permit+deny+fragment-type+fragment+fragment-subseq) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ [ **fragment-type** { **fragment** | **fragment-subseq** | **non-fragment** | **non-subseq** | **fragment-spe-first** } ] | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
   
   
   
   A rule is configured for the basic ACL.
   
   
   
   * Adding new rules to an ACL will not affect the existing rules.
   * If an existing rule is edited and the edited content conflicts with the original one, the edited content takes effect.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When you configure a basic ACL:
   
   * If a source IP address is specified by configuring **source**, the system filters only packets with this specified source IP address.
   * If all source IP addresses are specified by configuring **any**, the system does not check packets' source IP addresses, and considers that all packets have matched the rule and directly takes an action (**deny** or **permit**) on the packets.
   * If **time-range** is specified, the specified time range name must exist. Otherwise, the ACL rule configuration fails.
   * If the wildcard mask configured for an IPv4 rule is all Fs or all 0s, services may be adversely affected. In addition, if you delete the IPv4 addresses specified in an ACL IPv4 rule by running the **undo rule** command, filtering will not be performed based on IPv4 addresses, potentially causing service interruptions. In this case, the service interruption risk warning function is enabled by default, indicating that the configuration may adversely affect services. If the risk warning function is disabled, run the **undo configuration prevent-misoperation disable** command to enable it.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   The description for an ACL rule is configured.
   
   
   
   The description of an ACL rule can contain the functions of the ACL rule. Configuring a description for an ACL rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL rules are configured, and their functions are difficult to identify.
   * An ACL rule is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.