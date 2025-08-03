Configuring an EDSG Traffic Policy
==================================

To distinguish user traffic over networks 1 and 2, create two service groups and configure an EDSG traffic policy for each service group. This section describes how to configure an EDSG traffic policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-group**](cmdqueryname=service-group) *service-group-name*
   
   
   
   A service group is created.
3. Define an ACL rule for matching the service group.
   1. Run [**acl**](cmdqueryname=acl) { **name** *ucl-acl-name* [ **ucl** | [ **ucl** ] **number** *ucl-acl-number* ] | [ **number** ] *ucl-acl-number* } [ **match-order** { **auto** | **config** } ]
      
      
      
      An ACL is created and its view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You need to use UCLs. The number of a UCL ranges from 6000 to 9999.
   2. Create an ACL rule based on protocol types.
      
      
      1. For TCP, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **syn-flag** { *syn-flag* [ **mask** *mask-value* ] | { **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** | **ece** | **crw** | **ns** } } } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
      2. For UDP, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
      3. For ICMP, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **icmp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **icmp-type** { *icmp-name* | *icmp-type* *icmp-code* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
      4. For other protocols, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { **zero** | *protocol* | **gre** | **ip** | **ipinip** | **igmp** | **ospf** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name* | **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ] \*
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. (Optional) Define an ACL6 rule for matching the service group.
   1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **number** *ucl-acl6-number* [ **match-order** { **auto** | **config** } ]
      
      
      
      An ACL6 is created and its view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      You need to use UCL6s. The number of a UCL6 ranges from 6000 to 9999.
   2. Create an ACL6 rule based on protocol types.
      
      
      1. For TCP, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { **ipv6-address** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { **ipv6-address** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *destination-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **fragment** | **traffic-class** *traffic-class* | **time-range** *time-name* ] \*
      2. For UDP, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { **ipv6-address** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { **ipv6-address** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *destination-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **fragment** | **traffic-class** *traffic-class* | **time-range** *time-name* ] \*
      3. For ICMP, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **icmpv6** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { **ipv6-address** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { **ipv6-address** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *destination-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **icmp6-type** { *icmp6-type-name* | *icmp6-type* *icmp6-code* } | **fragment** | **traffic-class** *traffic-class* | **time-range** *time-name* ] \*
      4. For other protocols, run:
         
         [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **gre** | **ipv6-esp** | **ipv6** | **ipv6-ah** | **ospf** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { **ipv6-address** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { **ipv6-address** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *destination-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **fragment** | **traffic-class** *traffic-class* | **time-range** *time-name* ] \*
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Configure a traffic classifier.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured and the traffic classifier view is displayed.
   2. Run [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }
      
      
      
      The traffic classifier references a specified ACL or ACL6.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
6. Configure a traffic behavior.
   1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured and the traffic behavior view is displayed.
   2. (Optional) Run [**service-class edsg keep-queue-level**](cmdqueryname=service-class+edsg+keep-queue-level)
      
      
      
      The device is configured to retain the service class of the original packets after the EDSG service is matched to a traffic behavior.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
7. Configure an EDSG traffic policy.
   1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* command
      
      
      
      An EDSG traffic policy is configured and the EDSG traffic policy view is displayed.
   2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]
      
      
      
      The traffic behavior is specified for the traffic classifier.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
8. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }
   
   
   
   The EDSG traffic policy is globally applied.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.