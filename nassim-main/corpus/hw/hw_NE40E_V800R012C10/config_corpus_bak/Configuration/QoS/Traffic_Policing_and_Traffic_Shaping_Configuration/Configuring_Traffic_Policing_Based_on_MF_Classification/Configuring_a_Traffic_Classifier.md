Configuring a Traffic Classifier
================================

You need to configure a traffic classifier before configuring class-based QoS. The traffic classifier can be configured based on the ACL rule, IP precedence, MAC address, protocol address, and so on.

#### Procedure

* Define a traffic classifier based on Layer 3 or Layer 4 information
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
     
     
     
     A traffic classifier is defined and its view is displayed.
     
     
     
     If you define multiple matching rules in a traffic classifier, you can set the logical relationship between the matching rules by specifying the **operator** parameter.
     
     + **and**: A packet belongs to the classifier only when it matches all the rules.
     + **or**: A packet belongs to the classifier if it matches any one of the rules.
  3. Define matching rules for the traffic classifier as required.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For IPv6 packets, you need to specify the keyword **ipv6** when defining a matching rule in Step 3. A matching rule defined to match packets based on the source or destination addresses applies to IPv6 packets, but not IPv4 packets.
     
     You can define different ACL rules as required, including the protocol type, source address, destination address, and ToS in packets. The [**if-match acl**](cmdqueryname=if-match+acl) command filters packets according to the ACL rules defined in the **rule** command. The system then performs the corresponding traffic behavior for the matching packets.
     
     + To define a matching rule based on an ACL, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* } [ **precedence** *precedence-value* ] command.
     + To define a matching rule to classify traffic based on the DSCP value, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **dscp** *dscp-value* command.
     + To define a matching rule to classify traffic based on the IPv4 TCP flag value, run the [**if-match tcp syn-flag**](cmdqueryname=if-match+tcp+syn-flag) { *tcpflag-value* [ **mask** *tcpflag-mask* ] | **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** | **ece** | **cwr** | **ns** } } command.
     + To define a matching rule to classify traffic based on the IPv6 TCP flag value, run the [**if-match ipv6 tcp syn-flag**](cmdqueryname=if-match+ipv6+tcp+syn-flag) { *tcpflag-value-ipv6* [ **mask** *tcpflag-mask-ipv6* ] | **bit-match** { **established** | **fin** | **syn** | **rst** | **psh** | **ack** | **urg** } } command.
     + To define a matching rule to classify traffic based on the precedence of an IP packet, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **ip-precedence** *ip-precedence* command.
     + To define a matching rule to classify traffic based on the MPLS EXP value, run the [**if-match mpls-exp**](cmdqueryname=if-match+mpls-exp) *exp-value* command.
     + To define a matching rule to match all packets, run the [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **any** command.
     + To define a matching rule to classify traffic based on the value of the next IPv6 header, run the [**if-match ipv6 next-header**](cmdqueryname=if-match+ipv6+next-header) *header-number* **first-next-header** command.
     + To define a matching rule to classify traffic based on the source IPv6 address, run the [**if-match ipv6 source-address**](cmdqueryname=if-match+ipv6+source-address) *ipv6-address* *prefix-length* command.
     + To define a matching rule to classify traffic based on a destination IPv6 address, run the [**if-match ipv6 destination-address**](cmdqueryname=if-match+ipv6+destination-address) *ipv6-address* *prefix-length* command.
     + To define a matching rule to classify IPv4 packets based on the QoS policy ID, run the [**if-match qos-local-id**](cmdqueryname=if-match+qos-local-id) *qos-local-id* command.
     + To define a matching rule to classify IPv4 packets based on the source and destination QoS policy IDs, run the [**if-match qos-local-id**](cmdqueryname=if-match+qos-local-id) **source** *source-qos-local-id* **destination** *destination-qos-local-id* command.
     + To define a matching rule to classify traffic based on the IPv6 QoS policy ID, run the [**if-match ipv6 qos-local-id**](cmdqueryname=if-match+ipv6+qos-local-id) *qos-local-id* command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Define a traffic classifier based on Layer 2 information
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
     
     
     
     A traffic classifier is defined and its view is displayed.
     
     
     
     If you define multiple matching rules in a traffic classifier, you can set the logical relationship between the matching rules by specifying the **operator** parameter.
     
     + **and**: A packet belongs to the classifier only when it matches all the rules.
     + **or**: A packet belongs to the classifier if it matches any one of the rules.
  3. Define matching rules on the Router as required.
     
     
     + To define a matching rule based on an ACL, run the [**if-match**](cmdqueryname=if-match) **acl** { *acl-number* | **name** *acl-name* } [ **precedence** *precedence-value* ] command.
     + To define a matching rule to classify traffic based on the 802.1p priority of VLAN packets, run the [**if-match 8021p**](cmdqueryname=if-match+8021p) *8021p-value* command.
     + To define a matching rule to classify traffic based on the CoS, run the [**if-match service-class**](cmdqueryname=if-match+service-class) *service-class-value* command.
     + To define a matching rule to classify traffic based on the source MAC address, run the [**if-match source-mac**](cmdqueryname=if-match+source-mac) *mac-address* command.
     + To define a matching rule to classify traffic based on the destination MAC address, run the [**if-match destination-mac**](cmdqueryname=if-match+destination-mac) *mac-address* command.
     + To define a matching rule to classify traffic based on the VLAN, run the [**if-match vlan**](cmdqueryname=if-match+vlan) *vlan-id* [ **cvlan** *ce-vlan-id* ] command.
     + To define a matching rule to classify traffic based on the packet offset, run the [**if-match**](cmdqueryname=if-match) { **offset** *offset-value* **match-value** *match-value* **match-mask** *match-mask* } <1-4> command.![](../../../../public_sys-resources/caution_3.0-en-us.png) 
       
       A matching rule based on the packet offset affects forwarding performance. Therefore, understand related precautions before using the [**if-match**](cmdqueryname=if-match) **offset** command.If multiple traffic classifiers are configured in one traffic policy, the traffic behaviors corresponding to these traffic classifiers are implemented in different orders.
     + When multiple traffic classifiers match different fields of an IP packet and the priorities of the traffic classifiers are not specified, the traffic classifier configured first in the traffic policy takes effect preferentially.
       
       For example, as shown in [Table 1](#EN-US_TASK_0000001833036249__en-us_task_0172371247_tab_dc_ne_qos_cfg_004201), Policy 1 defines two traffic classifiers and their corresponding traffic behaviors in sequence. If a packet matches both traffic classifiers, behavior1 is performed on the packet. That is, the 802.1p value is re-marked as 1.
       
       **Table 1** Traffic classifiers and behaviors defined in Policy 1
       | Traffic Classifier | Matching Rule | Traffic Behavior | Traffic Action |
       | --- | --- | --- | --- |
       | classifier1 | Matching the destination MAC address | behavior1 | Re-marking the 802.1p value as 1 |
       | classifier3 | Matching the source MAC address | behavior3 | Re-marking the 802.1p value as 3 |
     + When multiple traffic classifiers match the same field of an IP packet, the traffic behavior corresponding to the specific traffic classifier is implemented for the packet.
       
       For example, as shown in [Table 2](#EN-US_TASK_0000001833036249__en-us_task_0172371247_tab_dc_ne_qos_cfg_004202), Policy 2 defines three traffic classifiers and their corresponding traffic behaviors in sequence. If the destination MAC address of a packet is 2-2-2, behavior 2 is performed on the packet, and the 802.1p value of the packet is re-marked as 2.
       
       **Table 2** Traffic classifiers and behaviors defined in Policy 2
       | Traffic Classifier | Matching Rule | Traffic Behavior | Traffic Action |
       | --- | --- | --- | --- |
       | classifier1 | Matching the destination MAC address 1-1-1 | behavior1 | Re-marking the 802.1p value as 1 |
       | classifier2 | Matching the destination MAC address 2-2-2 | behavior2 | Re-marking the 802.1p value as 2 |
       | classifier3 | Matching the destination MAC address 3-3-3 | behavior3 | Re-marking the 802.1p value as 3 |
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.