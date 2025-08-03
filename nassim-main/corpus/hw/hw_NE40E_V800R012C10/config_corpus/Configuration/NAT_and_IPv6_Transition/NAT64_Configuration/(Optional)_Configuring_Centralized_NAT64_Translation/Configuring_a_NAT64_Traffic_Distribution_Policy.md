Configuring a NAT64 Traffic Distribution Policy
===============================================

You can configure a NAT64 traffic distribution policy to distribute user traffic to NAT64 service boards for translation.

#### Context

A service board does not provide any interfaces. Therefore, an interface board must distribute user traffic to a service board for NAT64 treatment. You can configure a traffic distribution policy to distribute the packets matching the traffic distribution policy to the NAT64 service board.


#### Procedure

1. Configure a traffic classification rule.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run either of the following commands:
      
      
      * For a basic ACL (ACL number ranging from 2000 to 2999), run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
      * For an advanced ACL (ACL number ranging from 3000 to 3999), run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ] command.
   3. Run either of the following commands to create an ACL rule:
      
      
      * For a basic ACL6 (ACL number ranging from 2000 to 2999), run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \* command.
      * For an advanced ACL6 (ACL number ranging from 3000 to 3999), run:
        
        [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } { *protocol* | **udp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **destination-port** *operator* *port* | **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } **source-pool** *source-pool-name* } | **source-port** *operator* *port* | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
        
        The preceding configuration uses UDP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule (Advanced ACL6 view) (tcp)**, **rule (Advanced ACL6 view) (icmpv6)**, and **rule (Advanced ACL6 view) (protocol)** commands.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A source IP address is usually configured in an ACL rule.
      
      To add multiple rules in an ACL, repeat Step c.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure a traffic classifier.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured, and the traffic classifier view is displayed.
   3. Run [**if-match ipv6 acl**](cmdqueryname=if-match+ipv6+acl) *acl-number*
      
      
      
      A matching rule for multi-field (MA) traffic classification based on an ACL is configured.
      
      To configure multiple matching rules based on ACLs, repeat Step c. Traffic matching the ACL rule must have the destination addresses with the prefix defined in the NAT64 instance.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a traffic behavior.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured, and the traffic behavior view is displayed.
   3. Run [**nat64 bind instance**](cmdqueryname=nat64+bind+instance) *instance-name*
      
      
      
      The traffic behavior is bound to a NAT64 instance.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a traffic policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is configured, and the traffic policy view is displayed.
   3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
      
      
      
      A traffic behavior is specified for a specified traffic classifier in the traffic policy.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Apply the traffic policy to an interface.
   
   
   
   # In centralized NAT64 scenarios, apply the traffic policy to Layer 3 interfaces for Layer 3 traffic sent by the network side.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** [ **link-layer** | **all-layer** | **mpls-layer** ]
      
      
      
      A traffic policy is applied to an interface.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   
   
   
   # In centralized NAT64 scenarios, apply the traffic policy to Layer 2 VLANIF member interfaces for VLANIF interface traffic sent by the network side.
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The interface view is displayed.
   3. Run [**portswitch**](cmdqueryname=portswitch)
      
      
      
      The Layer 3 interface is switched to a Layer 2 interface.
   4. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** **vlan** { **all** | *vlan-id1* [ **to** *vlan-id2* ] } [ **link-layer** | **all-layer** | **mpls-layer** ]
      
      
      
      A traffic policy is applied to the Layer 2 interface.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.