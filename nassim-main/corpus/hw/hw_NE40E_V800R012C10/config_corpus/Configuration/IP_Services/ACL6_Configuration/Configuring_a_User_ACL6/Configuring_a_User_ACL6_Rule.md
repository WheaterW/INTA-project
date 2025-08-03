Configuring a User ACL6 Rule
============================

User ACL6s match packets based on the source/destination IPv6 address, source/destination service group, source/destination user group, source/destination port number, and protocol type.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+ucl+number+match-order+auto+config) { **name** *ucl-acl6-name* **ucl** | **number** *ucl-acl6-number* } [ **match-order** { **auto** | **config** } ]
   
   
   
   The user ACL6 view is displayed.
3. Run any of the following commands to create a user ACL6 rule:
   
   
   * When *protocol* is specified as UDP, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+udp+source+ipv6-address+any+source-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **udp** | *17* } [ [ **source** { { **ipv6-address** { *source-ipv6-address* *source-wildcard* | **any** | *source-wildcard* } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ipv6-address** { *destination-ipv6-address* *destination-wildcard* | **any** | *destination-wildcard* } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **source-port** { *operator* { *port-number* | *src-begin-udp-port-enum* } | **range** { *port-number* | *src-begin-udp-port-enum* } { *port-number* | *src-end-udp-port-enum* } } ] | [ **destination-port** { *operator* { *port-number* | *dst-begin-udp-port-enum* } | **range** { *port-number* | *dst-begin-udp-port-enum* } { *port-number* | *dst-end-udp-port-enum* } } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* | **traffic-class** *traffic-class* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment** ] ] \* \*
   * When *protocol* is specified as TCP, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+tcp+source+ipv6-address+any+source-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *6* | **tcp** } [ [ **source** { { **ipv6-address** { *source-ipv6-address* *source-wildcard* | **any** | *source-wildcard* } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ipv6-address** { *destination-ipv6-address* *destination-wildcard* | **any** | *destination-wildcard* } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **source-port** { *operator* { *port-number* | *src-begin-tcp-port-enum* } | **range** { *port-number* | *src-begin-tcp-port-enum* } { *port-number* | *src-end-tcp-port-enum* } } ] | [ **destination-port** { *operator* { *port-number* | *dst-begin-tcp-port-enum* } | **range** { *port-number* | *dst-begin-tcp-port-enum* } { *port-number* | *dst-end-tcp-port-enum* } } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* | **traffic-class** *traffic-class* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment** ] ] \*
   * When *protocol* is specified as ICMPv6, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+icmpv6+source+ipv6-address+any+source-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **icmpv6** | *58* } [ [ **source** { { **ipv6-address** { *source-ipv6-address* *source-wildcard* | **any** | *source-wildcard* } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ipv6-address** { *destination-ipv6-address* *destination-wildcard* | **any** | *destination-wildcard* } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **icmp6-type** { *icmp6-type* *icmp6-code* | *icmp6-type-name* } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* | **traffic-class** *traffic-class* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment** ] ] \*
   * When *protocol* is specified as a protocol other than TCP, UDP, and ICMPv6, run:
     
     [**rule**](cmdqueryname=rule+name+permit+deny+gre+ipv6-esp+ipv6+ipv6-ah+ospf+source) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *protocol* | **gre** | **ipv6-esp** | **ipv6** | **ipv6-ah** | **ospf** | *7-16* | *18-57* | *59-255* } [ [ **source** { { **ipv6-address** { *source-ipv6-address* *source-wildcard* | **any** | *source-wildcard* } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ipv6-address** { *destination-ipv6-address* *destination-wildcard* | **any** | *destination-wildcard* } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *d**estination-url-address* ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* | **traffic-class** *traffic-class* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment** ] ] \*
   
   
   
   Adding new rules to an ACL6 will not affect the existing rules.
   
   When an existing rule is edited and the edited contents conflict with the original contents, the edited contents take effect.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   A description is configured for the rule.
   
   
   
   The description of an ACL6 rule can contain the functions of the ACL6 rule. Configuring a description for an ACL6 rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL6s are configured, and their functions are difficult to identify.
   * An ACL6 is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.