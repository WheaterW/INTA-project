Configuring a DS-Lite Traffic Diversion Policy
==============================================

You can configure a DS-Lite traffic diversion policy to distribute user traffic to DS-Lite service boards for translation.

#### Context

A DS-Lite service board does not provide any interface. Therefore, an inbound interface board must direct user traffic to a DS-Lite service board for DS-Lite processing. You can configure a traffic diversion policy to direct packets matching the configured traffic diversion policy to the DS-Lite service board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a traffic classification rule.
   1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **number** *ucl-acl6-number* [ **match-order** { **auto** | **config** } ] A user ACL6 (the ACL number ranges from 6000 to 9999) is configured, and the ACL6 view is displayed.
   2. Create a user ACL6 rule based on the protocol type:
      
      
      
      [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { **ipv6-address** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { **ipv6-address** { *destination-ipv6-address* { *prefix-length* | *destination-wildcard* } | *destination-ipv6-address*/*prefix-length* | **any** } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **fragment** | **traffic-class** *traffic-class* | **time-range** *time-name* ] \*
      
      The preceding configuration uses UDP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule** command in the UCL6 view.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Generally, the source IP address is matched against in an ACL rule. To specify multiple ACL rules, repeat Step [2.b](#EN-US_TASK_0172374709__substep_02).
      
      Rules in an ACL to which traffic is matched against are used based on the depth-first rule (with **auto** configured) or in a configuration order (with **config** configured). By default, rules are used in a configuration order (with **config** configured).
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a traffic classifier.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured, and the traffic classifier view is displayed.
   2. Run [**if-match ipv6 acl**](cmdqueryname=if-match+ipv6+acl) *acl-number*
      
      
      
      An ACL-based matching rule for MF traffic classification is configured.
      
      
      
      To specify multiple ACL-based matching rules, repeat this step.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a traffic behavior.
   1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured, and the traffic behavior view is displayed.
   2. Run [**ds-lite bind instance**](cmdqueryname=ds-lite+bind+instance) *instance-name*
      
      
      
      The traffic behavior is bound to the DS-Lite instance.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The flow that has been processed by DS-lite cannot be redirected. This command is mutually exclusive with the [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) command.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Configure a traffic policy.
   1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is configured, and the traffic policy view is displayed.
   2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
      
      
      
      A traffic behavior is specified for a specified traffic classifier in the traffic policy.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
6. Globally apply the traffic classification policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound**
      
      
      
      The traffic diversion policy is applied on the user side.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.