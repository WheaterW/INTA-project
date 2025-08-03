Configuring a NAT Traffic Diversion Policy on an Inbound Interface
==================================================================

You can configure a NAT traffic policy on an inbound interface to perform NAT translation on user traffic.

#### Context

Before performing NAT translation on an inbound interface, configure a NAT traffic policy to match desired user traffic on the inbound interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a traffic classification rule.
   1. Run either of the following commands to create an ACL and enter the ACL view:
      
      
      * For a basic ACL (numbered from 2000 to 2999), run the [**acl**](cmdqueryname=acl+name+basic+basic+number+number+match-order+config+auto) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command.
      * For an advanced ACL (numbered from 3000 to 3999), run the [**acl**](cmdqueryname=acl+name+advance+advance+number+number+match-order+config+auto) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command.
   2. Run either of the following commands to create an ACL rule:
      
      
      * For a basic ACL (numbered from 2000 to 2999), run the following command:
        
        [**rule**](cmdqueryname=rule+name+deny+permit+fragment-type+fragment+non-fragment) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] | **logging** ] \*
      * For an advanced ACL (numbered from 3000 to 3999), run the following command as required by the protocol type:
        
        [**rule**](cmdqueryname=rule+name+deny+permit+tcp+dscp+precedence+tos+destination+0+any) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } { *protocol* | **tcp** } [ [ **dscp** *dscp* | [ **precedence** *precedence* | **tos** *tos* ] \* ] | { **destination** { *destination-ip-address* { *destination-wildcard* | **0** | *des-netmask* } | **any** } | **destination-pool** *destination-pool-name* } | { **destination-port** *operator* *port-number* | **destination-port-pool** *destination-port-pool-name* } | **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | { **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **source-pool** *source-pool-name* } | { **source-port** *operator* *port-number* | **source-port-pool** *source-port-pool-name* } | { **tcp-flag** | **syn-flag** } { *tcp-flag* [ **mask** *mask-value* ] | **established** |{ **ack** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **fin** [ **ack** | **psh** | **rst** | **syn** | **urg** ] \* } | { **psh** [ **fin** | **ack** | **rst** | **syn** | **urg** ] \* } | { **rst** [ **fin** | **psh** | **ack** | **syn** | **urg** ] \* } | { **syn** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } | { **urg** [ **fin** | **psh** | **rst** | **syn** | **urg** ] \* } } | **time-range** *time-name* | **ttl** *ttl-operation* *ttl-value* | **packet-length** *length-operation* *length-value* ] \*
        
        The preceding configuration uses TCP as the example protocol. The configurations of the other protocols are similar. For details, see the **rule (Advanced ACL view) (UDP)**, **rule (advanced ACL view) (ICMP)**, and **rule (Advanced ACL view) (gre-igmp-ip-ipinip-ospf)** commands.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * Generally, source IP addresses are matched against in ACL rules. To specify multiple ACL rules, repeat Step [2.b](#EN-US_TASK_0172374516__substep_02).
      * Rules in an ACL to which traffic is matched against are used based on the depth first principle (with **auto** configured) or the configuration order (with **config** configured). By default, rules are matched against in the configuration order (with **config** configured).
      * When an ACL rule is associated with an instance, the address wildcard of the ACL rule must be a subnet mask in consecutive mode (with 0s and 1s consecutively sequenced, such as 255.255.255.0), instead of a subnet mask in non-consecutive mode (with 0s and 1s non-consecutively sequenced, such as 255.0.255.0).
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a traffic classifier.
   1. Run [**traffic classifier**](cmdqueryname=traffic+classifier+operator+and+or) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is configured, and its view is displayed.
   2. Run [**if-match acl**](cmdqueryname=if-match+acl) *acl-number*
      
      
      
      An ACL-based matching rule is defined for multi-field traffic classification.
      
      To configure multiple ACL-based matching rules, repeat this step.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Configure a traffic behavior.
   1. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is configured, and its view is displayed.
   2. Run [**nat bind instance**](cmdqueryname=nat+bind+instance) *instance-name*
      
      
      
      A traffic behavior is bound to a NAT instance.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The same post-NAT traffic cannot be redirected. That is, the [**nat bind instance**](cmdqueryname=nat+bind+instance) and [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) commands are mutually exclusive.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
5. Configure a traffic policy.
   1. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is configured, and its view is displayed.
   2. Run [**classifier**](cmdqueryname=classifier+behavior) *classifier-name* **behavior** *behavior-name*
      
      
      
      The traffic behavior is bound to the traffic classifier in the traffic policy.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
6. Apply the traffic policy to an interface.
   
   
   
   For NAT user traffic on an inbound interface, apply the traffic policy to a user-side Layer 3 interface.
   
   
   
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* *interface-name*
      
      
      
      The interface view is displayed.
   2. Run [**traffic-policy**](cmdqueryname=traffic-policy+inbound+link-layer+all-layer+mpls-layer) *policy-name* **inbound** [ **link-layer** | **all-layer** | **mpls-layer** ]
      
      
      
      The traffic policy is applied to the interface.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   
   
   
   For NAT user traffic on an inbound interface, apply the traffic policy to a user-side Layer 2 Ethernet interface that is added to a VLAN.
   
   
   
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* *interface-name*
      
      
      
      The interface view is displayed.
   2. Run [**portswitch**](cmdqueryname=portswitch)
      
      
      
      The interface is switched to the Layer 2 mode.
   3. Run [**port link-type**](cmdqueryname=port+link-type+access+dot1q-tunnel+hybrid+trunk) { **access** | **dot1q-tunnel** | **hybrid** | **trunk** }
      
      
      
      A type is set for the Layer 2 Ethernet interface.
   4. Run either of the following commands to add an interface to a VLAN:
      
      
      * For an access or QinQ interface:
        
        1. Run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command to add the interface to the VLAN.
           
           To add one or more interfaces to a VLAN in a batch, run the [**port**](cmdqueryname=port+to) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10> command in the VLAN view.
           
           ![](../../../../public_sys-resources/note_3.0-en-us.png) 
           + The input interface format must be correct. *interface-number2* must be greater than *interface-number1*. *interface-number2* and *interface-number1* must specify the same type of interface. Interfaces in the range defined by *interface-number2* and *interface-number1* must exist.
           + In a [**port**](cmdqueryname=port+to+to) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10> command, a maximum of 10 **to** parameters can be used to define 10 ranges of interfaces.
      * For a hybrid interface:
        
        1. Run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan+to+all) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> | **all** } command to add the interface to a specified VLAN.
        2. (Optional) Run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command to specify a default VLAN for the trunk interface.
   5. Run [**traffic-policy**](cmdqueryname=traffic-policy+inbound+vlan+to+link-layer) *policy-name* **inbound** **vlan** { **all** | *vlan-id1* [ **to** *vlan-id2* ] } [ **link-layer** | **all-layer** | **mpls-layer** ]
      
      
      
      The traffic policy is applied to the Layer 2 interface.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   
   
   
   For NAT user traffic on an inbound interface, apply the traffic policy to a VPN instance.
   
   
   
   1. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      The VPN instance view is displayed.
   2. Run [**traffic-policy**](cmdqueryname=traffic-policy+network+inbound) *policy-name* **network** **inbound**
      
      
      
      The traffic policy is applied to the VPN instance.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.