Configuring a User ACL Rule
===========================

Packets can be matched based on the source/destination IP address, source/destination service group, source/destination user group, source/destination port number, and protocol type.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl+name+ucl+ucl+number+number+match-order+auto+config) { **name** *ucl-acl-name* [ **ucl** | [ **ucl** ] **number** *ucl-acl-number* ] | [ **number** ] *ucl-acl-number* } [ **match-order** { **auto** | **config** } ]
   
   
   
   The user ACL view is displayed.
3. Run any of the following commands to create a user ACL rule:
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When a user ACL is applied to the if-match field in the traffic classifier of a global traffic policy, user-group must be specified for each rule in the user ACL. Otherwise, the user ACL cannot take effect. In addition, ACL rules take effect depending on both the user/network side and upstream/downstream traffic. For details, see the [**traffic-policy match-type destination-user inbound**](cmdqueryname=traffic-policy+match-type+destination-user+inbound) and [**traffic-policy match-type interface-acl**](cmdqueryname=traffic-policy+match-type+interface-acl) commands.
   
   
   
   * Create a user ACL rule when *protocol* is UDP.
     
     [**rule**](cmdqueryname=rule+name+permit+deny+udp+source+ip-address+0+any+source-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **udp** | *17* } [ [ **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **source-port** { *operator* { *port-number* | *udp-src-bport-enum* } | **range** { *port-number* | *udp-src-bport-enum* } { *port-number* | *udp-src-eport-enum* } } ] | [ **destination-port** { *operator* { *port-number* | *udp-dst-bport-enum* } | **range** { *port-number* | *udp-dst-bport-enum* } { *port-number* | *udp-dst-eport-enum* } } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment-type** *fragment-enum* ] | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
   * Create a user ACL rule when *protocol* is TCP.
     
     [**rule**](cmdqueryname=rule+name+permit+deny+tcp+source+ip-address+0+any+source-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *6* | **tcp** } [ [ **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **source-port** { *operator* { *port-number* | *tcp-src-bport-enum* } | **range** { *port-number* | *tcp-src-bport-enum* } { *port-number* | *tcp-src-eport-enum* } } ] | [ **destination-port** { *operator* { *port-number* | *tcp-dst-bport-enum* } | **range** { *port-number* | *tcp-dst-bport-enum* } { *port-number* | *tcp-dst-eport-enum* } } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* } ] | [ **time-range** *time-name* ] | [ **syn-flag** { *syn-flag* [ **mask** *mask-value* ] | { **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** | **ece** | **cwr** | **ns** } } } ] | [ **logging** ] | [ **fragment-type** *fragment-enum* ] | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
   * Create a user ACL rule when *protocol* is ICMP.
     
     [**rule**](cmdqueryname=rule+name+permit+deny+icmp+source+ip-address+0+any+source-pool) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **icmp** | *1* } [ [ **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **icmp-type** { *icmp-type* *icmp-code* | *icmp-name* } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment-type** *fragment-enum* ] | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
   * Create a user ACL rule when *protocol* is any other protocol except the preceding well-known protocols.
     
     [**rule**](cmdqueryname=rule+name+permit+deny+zero+gre+igmp+ip+ipinip+ospf+source) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { **zero** | *protocol* | **gre** | **igmp** | **ip** | **ipinip** | **ospf** | *7-16* | *18-255* } [ [ **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } | **url** *destination-url-address* ] } ] | [ **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } ] | [ { { **precedence** { *precedence* | *precedence-enum* } | **tos** { *tos* | *tos-enum* } } \* | **dscp** *dscp* } ] | [ **time-range** *time-name* ] | [ **logging** ] | [ **fragment-type** *fragment-enum* ] | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
   
   
   * Adding new rules to an ACL will not affect the existing rules.
   * If an existing rule is edited and the edited content conflicts with the original one, the edited content takes effect.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the wildcard mask configured for an IPv4 rule is all Fs or all 0s, services may be adversely affected. In addition, if you delete the IPv4 addresses specified in an ACL IPv4 rule by running the **undo rule** command, filtering will not be performed based on IPv4 addresses, potentially causing service interruptions. In this case, the service interruption risk warning function is enabled by default, indicating that the configuration may adversely affect services. If the risk warning function is disabled, run the **undo configuration prevent-misoperation disable** command to enable it.
4. (Optional) Run [**rule**](cmdqueryname=rule) *rule-id* [**description**](cmdqueryname=description) *destext*
   
   
   
   The description for an ACL rule is configured.
   
   
   
   The description of an ACL rule can contain the functions of the ACL rule. Configuring a description for an ACL rule is recommended to prevent misuse of the rule in the following situations:
   * A large number of ACL rules are configured, and their functions are difficult to identify.
   * An ACL rule is used at a long interval, and its function may be left forgotten.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.