Configuring a DS-Lite Traffic Diversion Policy on an Inbound Interface
======================================================================

A DS-Lite traffic diversion policy is configured on an inbound interface so that user traffic can be processed using DS-Lite.

#### Context

A DS-Lite service board does not provide any interface. Therefore, an inbound interface board must direct user traffic to a DS-Lite service board for DS-Lite processing. You can configure a traffic diversion policy to direct packets matching the configured traffic diversion policy to the DS-Lite service board.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a traffic classification rule.
   1. Run one of the following commands to create an ACL6 and enter the ACL6 view based on the ACL type:
      
      
      * For a basic ACL6 (the ACL number ranges from 2000 to 2999), run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
      * For an advanced ACL6 (the ACL number ranges from 3000 to 3999), run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
   2. Run one of the following commands to create an ACL6 rule based on the ACL type:
      
      
      * For a basic ACL6 (ACL number ranging from 2000 to 2999), run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \* command.
      * For an advanced ACL6 (ACL number ranging from 3000 to 3999), run:
        
        [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **destination-port** *operator* *port* | **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } **source-pool** *source-pool-name* } | **source-port** *operator* *port* | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
        
        The preceding configuration uses UDP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule (Advanced ACL6 view) (tcp)**, **rule (Advanced ACL6 view) (icmpv6)**, and **rule (Advanced ACL6 view) (protocol)** commands.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Generally, the source IP address is matched against in an ACL rule. To specify multiple ACL rules, repeat Step [2.b](#EN-US_TASK_0172374715__substep_02).
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a traffic classifier.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured, and the traffic classifier view is displayed.
   2. Run [**if-match ipv6 acl**](cmdqueryname=if-match+ipv6+acl) *acl-number*
      
      
      
      An ACL-based matching rule is configured for MF traffic classification.
      
      To configure multiple ACL-based matching rules, repeat this step.
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
      
      The [**ds-lite bind instance**](cmdqueryname=ds-lite+bind+instance) and [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) commands are mutually exclusive.
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
6. Apply the traffic policy to an interface.
   
   
   
   # Apply the traffic diversion policy to a user-side Layer 3 interface.
   
   
   
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   2. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** [ **link-layer** | **all-layer** | **mpls-layer** ]
      
      
      
      A traffic policy is applied to the interface.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   
   
   
   # Apply the traffic diversion policy to a user-side Layer 2 Ethernet interface that is added to a VLAN.
   
   
   
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   2. Run [**portswitch**](cmdqueryname=portswitch)
      
      
      
      The Layer 3 interface is switched to the Layer 2 mode.
   3. Run [**port link-type**](cmdqueryname=port+link-type) { **access** | **dot1q-tunnel**  | **hybrid** | **trunk** }
      
      
      
      Attributes are set for the Layer 2 Ethernet interface.
   4. Run one of the following commands to add an interface to a VLAN:
      
      
      * For an access or QinQ interface:
        
        1. Run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command.
           
           To add interfaces to a VLAN in batches, run the [**port**](cmdqueryname=port) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10> command in the VLAN view.
           
           ![](../../../../public_sys-resources/note_3.0-en-us.png) 
           
           *interface-number2* must be greater than *interface-number1*. *interface-number2* and *interface-number1* must specify the same type of interface. Interfaces in the range defined by *interface-number2* and *interface-number1* must exist.
           
           In a [**port**](cmdqueryname=port) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10> command instance, a maximum of 10 **to** parameters can be used to define 10 ranges of ports.
      * For a hybrid interface:
        
        1. Run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** } command.
        2. (Optional) Run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command to configure a default VLAN for the trunk interface.
   5. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** [ **vlan** { **all** | *vlan-id1* [ **to** *vlan-id2* ] } ] [ **link-layer** | **all-layer** | **mpls-layer** ]
      
      
      
      A traffic policy is applied to the Layer 2 interface.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.