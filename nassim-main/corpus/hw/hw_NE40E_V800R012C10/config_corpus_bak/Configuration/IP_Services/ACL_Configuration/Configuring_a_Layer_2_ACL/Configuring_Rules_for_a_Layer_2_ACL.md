Configuring Rules for a Layer 2 ACL
===================================

This section describes how to configure rules for a Layer 2 ACL.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl+name+link+link+number+number+match-order+config+auto) { **name** *link-acl-name* { **link** | [ **link** ] **number** *link-acl-number* } | [ **number** ] *link-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The Layer 2 ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule+name+permit+deny+type+arp+ip+ipv6+mpls+rarp+source-mac) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ [ **type** { *type* | **arp** | **ip** | **ipv6** | **mpls** | **rarp** } [ *type-mask* ] ] | **source-mac** *source-mac* [ *source-mac-mask* ] | { **dest-mac** | **destination-mac** } *dest-mac* [ *dest-mac-mask* ] | **8021p** *8021p* | { **cvlan-8021p** | **8021p-inner** } *cvlan-8021p* | **time-range** *time-name* ] \*
   
   
   
   A Layer 2 ACL rule is configured.
   
   
   
   * Adding rules to an ACL will not affect the existing rules.
   * If an existing rule is edited and the edited content conflicts with the original one, the edited content takes effect.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) During the configuration of rules for the Layer 2 ACL:
   * If **time-range** is specified, the specified time range name must exist. Otherwise, the ACL rule configuration fails.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   The description for an ACL rule is configured.
   
   
   
   The description of an ACL rule can contain the functions of the ACL rule. Configuring a description for an ACL rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL rules are configured, and their functions are difficult to identify.
   * An ACL rule is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.