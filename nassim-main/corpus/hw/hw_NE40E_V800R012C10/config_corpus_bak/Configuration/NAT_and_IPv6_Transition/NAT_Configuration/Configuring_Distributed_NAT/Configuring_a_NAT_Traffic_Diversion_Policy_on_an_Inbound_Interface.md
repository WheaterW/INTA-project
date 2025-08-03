Configuring a NAT Traffic Diversion Policy on an Inbound Interface
==================================================================

You can configure a NAT traffic diversion policy to distribute user traffic to NAT service boards for NAT processing.

#### Context

A NAT service board does not provide any interface. Therefore, an inbound interface board must direct user traffic to a NAT service board for NAT processing. You can configure a traffic policy to direct packets matching the configured traffic policy to the NAT service board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a traffic classification rule.
   1. Create a user ACL (UCL) and enter the ACL view.
      
      
      
      A UCL number ranges from 6000 to 9999. To create a UCL, run the **[**acl name**](cmdqueryname=acl+name)** **ucl-acl-name** [ **ucl** | [ **ucl** ] **number** **ucl-acl-number** ] ] [ **match-order** { **auto** | **config** } ] command.
   2. Create a user ACL rule based on the protocol used.
      
      
      
      [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **source** { { **ip-address** { *source-ip-address* { *source-ip-address-mask* | **0** } | **any** } | **source-pool** *source-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **destination** { { **ip-address** { *destination-ip-address* { *destination-ip-address-mask* | **0** } | **any** } | **destination-pool** *destination-pool-name* } | **any** | [ **service-group** { *service-group-name* | **any** } | **user-group** { *user-group-name* | **any** } ] } | **source-port** *operator* *port-number* | **destination-port** *operator* *port-number* | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **time-range** *time-name*| **vlan** *vlan-id* | **inner-vlan** *cvlan-id* ]\*
      
      The preceding configuration uses UDP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule** command in the UCL view.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * Generally, source IP addresses are matched against in ACL rules. To specify multiple ACL rules, repeat Step [2.b](#EN-US_TASK_0000001139936979__en-us_task_0172374506_substep_02).
      * Rules in an ACL to which traffic is matched against are used based on the depth first principle (with **auto** configured) or the configuration order (with **config** configured). By default, rules are matched against in the configuration order (with **config** configured).
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a traffic classifier.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured, and the traffic classifier view is displayed.
   2. Run [**if-match acl**](cmdqueryname=if-match+acl) *acl-number*
      
      
      
      An ACL-based matching rule is defined for multi-field traffic classification.
      
      
      
      To configure multiple ACL-based matching rules, repeat this step.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a traffic behavior.
   1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured, and the traffic behavior view is displayed.
   2. Run [**nat bind instance**](cmdqueryname=nat+bind+instance) *instance-name*
      
      
      
      A traffic behavior is bound to a NAT instance.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The [**nat bind instance**](cmdqueryname=nat+bind+instance) and [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) commands are mutually exclusive.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Configure a traffic policy.
   1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is configured, and its view is displayed.
   2. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
      
      
      
      The traffic behavior is bound to the traffic classifier in the traffic policy.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
6. Globally apply the traffic policy.
   1. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound**
      
      
      
      The traffic policy is applied to online users.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.