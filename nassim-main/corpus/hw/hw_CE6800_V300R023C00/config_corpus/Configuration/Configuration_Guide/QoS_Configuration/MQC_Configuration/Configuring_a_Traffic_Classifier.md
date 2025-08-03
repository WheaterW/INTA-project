Configuring a Traffic Classifier
================================

Configuring a Traffic Classifier

#### Prerequisites

Before configuring a traffic classifier, complete the following task:

* Configure an ACL if it is required to classify packets.


#### Context

Multiple rules can be configured in a traffic classifier as long as they do not conflict with each other. You can configure rules based on your requirements.

![](public_sys-resources/note_3.0-en-us.png) 

* A traffic classifier in which matching rules are ANDed cannot define duplicate matching rules. For example, a traffic classifier cannot define both **if-match source-mac** and an ACL rule that matches the same source MAC address.

* To match multiple fields of packets of the same type (such as Layer 2/IPv6/IPv4 packets) in a view, apply one traffic policy in the view, and specify multiple traffic classifiers and associated traffic behaviors in the traffic policy. If both IPv4 and IPv6 packets need to be matched, create one traffic policy for each type of packet.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a traffic classifier and enter the traffic classifier view, or enter the view of an existing traffic classifier.
   
   
   ```
   [traffic classifier](cmdqueryname=traffic+classifier) classifier-name [ type { and | or } ]
   ```
   **and** is the logical operator between the rules in a traffic classifier, which means that:
   * If the traffic classifier contains ACL rules, packets must match one ACL rule and all the non-ACL rules in order to match the traffic classifier.
   * If the traffic classifier does not contain any ACL rules, packets must match all rules in order to match the traffic classifier.The logical operator **or** means that packets match a traffic classifier if they match one or more rules in the traffic classifier.
   
   By default, the relationship between rules in a traffic classifier is **OR**.
   
   The device supports a maximum of 2048 traffic classifiers.
3. Configure matching rules according to the following table.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   For details about precautions for each matching rule, see the corresponding commands in the *Command Reference*.
   
   A maximum of 2048 **if-match** commands can be configured in a traffic classifier.
   
   * Link-layer rule (Layer 2 rule)
     
     | Matching Rule | Command |
     | --- | --- |
     | Destination MAC address | [**if-match destination-mac**](cmdqueryname=if-match+destination-mac) *mac-address* [ *mac-address-mask* ] |
     | Source MAC address | [**if-match source-mac**](cmdqueryname=if-match+source-mac) *mac-address* [ *mac-address-mask* ] |
     | Protocol type in the Ethernet frame header | [**if-match l2-protocol**](cmdqueryname=if-match+l2-protocol) { **arp** | **ip** | **rarp** | *protocol-value* } |
     | VLAN ID in the outer tag of VLAN packets or VLAN ID in the inner and outer tags of QinQ packets | [**if-match vlan**](cmdqueryname=if-match+vlan) *start-vlan-value* [ **inner-vlan** *start-inner-vlan-value* [ **to** *end-inner-vlan-value* ] ]  [**if-match vlan**](cmdqueryname=if-match+vlan) *start-vlan-value* [ **to** *end-vlan-value* ] [ **inner-vlan** *start-inner-vlan-value* ] |
     | 802.1p value in the outer tag of VLAN packets | [**if-match 8021p**](cmdqueryname=if-match+8021p) *8021p-value* &<1-8> |
     | Inner VLAN ID in QinQ packets | [**if-match**](cmdqueryname=if-match) **inner-vlan** *start-inner-vlan-value* [ **to** *end-inner-vlan-value* ]  The CE6885-LL (low latency mode) does not support this command. |
     | 802.1p value in the inner tag of QinQ packets | [**if-match inner-8021p**](cmdqueryname=if-match+inner-8021p) *inner-8021p-value* &<1-8>  The CE6885-LL (low latency mode) does not support this command. |
     | Inner and outer VLAN IDs in QinQ packets | [**if-match double-tag**](cmdqueryname=if-match+double-tag)  The CE6885-LL (low latency mode) does not support this command. |
   * Network-layer rule (Layer 3 rule)
     
     | Matching Rule | Command |
     | --- | --- |
     | DSCP value in IP packets | [**if-match dscp**](cmdqueryname=if-match+dscp) *dscp-value* &<1-8> |
     | DSCP value in IPv6 packets | [**if-match ipv6 dscp**](cmdqueryname=if-match+ipv6+dscp) *dscp-value* &<1-8>  The CE6885-LL (low latency mode) does not support this command. |
     | IP precedence in IP packets | [**if-match ip-precedence**](cmdqueryname=if-match+ip-precedence) *ip-precedence* &<1-8> |
     | IP identifier in IP packets | [**if-match ip-identification**](cmdqueryname=if-match+ip-identification) *ip-id* [ **mask** *ip-id-mask* ] |
     | ECN marking in IP packets | [**if-match ecn**](cmdqueryname=if-match+ecn) *ecn-value* |
     | ECN marking in IPv6 packets | [**if-match**](cmdqueryname=if-match) **ipv6** **ecn** *ecn-value*  The CE6885-LL (low latency mode) does not support this command. |
   * Transport-layer rule (Layer 4 rule)
     
     | Matching Rule | Command |
     | --- | --- |
     | TCP flag in the TCP packet header | [**if-match tcp-flag**](cmdqueryname=if-match+tcp-flag) { *tcp-flag-value* | { **ack** | **fin** | **psh** | **rst** | **syn** | **urg** } \* } |
   * ACL rule
     
     | Matching Rule | Command |
     | --- | --- |
     | ACL rule | [**if-match acl**](cmdqueryname=if-match+acl) { *acl-number* | *acl-name* } |
     | ACL6 rule | [**if-match ipv6 acl**](cmdqueryname=if-match+ipv6+acl) { *acl-number* | *acl6-name* } [ **loose-mode** | **strict-mode** ]  The CE6885-LL (low latency mode) does not support this command. |
   * Forwarding rule
     
     | Matching Rule | Command |
     | --- | --- |
     | Dropped packets | [**if-match discard**](cmdqueryname=if-match+discard)  The CE6885-LL (low latency mode) does not support this command. |
     | All packets | [**if-match any**](cmdqueryname=if-match+any) |
     | Inbound interface | [**if-match inbound-interface**](cmdqueryname=if-match+inbound-interface) { { *interface-type* *interface-number1* | *interface-name1* } [ **to** { *interface-type* *interface-number2* | *interface-name2* } ] } &<1-8> |
     | Interface | [**if-match outbound-interface**](cmdqueryname=if-match+outbound-interface) { { *interface-type* *interface-number1* | *interface-name1* } [ **to** { *interface-type* *interface-number2* | *interface-name2* } ] } &<1-8>  The CE6885-LL (low latency mode) does not support this command. |
     | Known unicast packets | [**if-match unicast**](cmdqueryname=if-match+unicast)  The CE6885-LL (low latency mode) does not support this command. |
     | Unknown unicast packets | [**if-match unknown-unicast**](cmdqueryname=if-match+unknown-unicast)  The CE6885-LL (low latency mode) does not support this command. |
   * VXLAN packet rule
     
     | Matching Rule | Command |
     | --- | --- |
     | Inner information in VXLAN packets to be matched against ACL rules | [**if-match vxlan**](cmdqueryname=if-match+vxlan) [ **transit** ] **acl** { *acl-number* | *acl-name* } |
     | Inner information in VXLAN packets to be matched against ACL6 rules | [**if-match vxlan**](cmdqueryname=if-match+vxlan) [ **transit** ] **ipv6** **acl** { *acl-number* | *acl-name* } [ **loose-mode** | **strict-mode** ] |
     | Inner information in VXLAN packets | [**if-match vxlan**](cmdqueryname=if-match+vxlan) [ **transit** ] **vni** *vni-id* |
     | Reserved field in VXLAN packets | [**if-match vxlan [ transit ] reserved-value**](cmdqueryname=if-match+vxlan+%5B+transit+%5D+reserved-value) *reserved-value* |
     
     The commands for configuring VXLAN packet matching rules are not supported by the CE6885-LL (low latency mode).
     
     When the commands for configuring VXLAN packet matching rules are run on the CE6820H, CE6820H-K, and CE6820S, the **transit** parameter must be specified, indicating that VXLAN packets of a transmission device are matched.
   * Other rules
     
     | Matching Rule | Command |
     | --- | --- |
     | RoCEv2 packet information | [**if-match rocev2**](cmdqueryname=if-match+rocev2) { **opcode** *opcode-value* | **qpair** *qpair-value* | **nack** *nack-value* | **udf base** **l4-head** { *udf-data* *udf-mask* **offset** *offset-value* } &<1-4> } \*  [**if-match ipv6 rocev2**](cmdqueryname=if-match+ipv6++rocev2) { **opcode** *opcode-value* | **qpair** *qpair-value* | **nack** *nack-value* | **udf base** **l4-head** { *udf-data* *udf-mask* **offset** *offset-value* } &<1-4> } \*  This function is supported only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.  The CE6885-LL (low latency mode) does not support the [**if-match ipv6 rocev2**](cmdqueryname=if-match+ipv6+rocev2) command. |
     | Inner information in GRE packets | [**if-match gre**](cmdqueryname=if-match+gre) [ **inner-source-ip** *source-ip-address* [ **mask** *source-masklen* ] | **inner-destination-ip** *dest-ip-address* [ **mask** *dest-masklen* ] | **inner-protocol** *protocol* | **inner-source-port** *source-port-begin* | **inner-destination-port** *dest-port-begin* ] \*  The CE6885-LL (low latency mode) does not support this command. |
     | Next-hop address and outbound interface | [**if-match**](cmdqueryname=if-match) { **nexthop** *ip-address* | **ipv6 nexthop** *ipv6-address* } **interface** *interface-type interface-number*  This command is not supported by the CE6885-LL (low latency mode). |
     | QoS local ID | [**if-match qos-local-id**](cmdqueryname=if-match+qos-local-id) *qos-local-id*  This command is not supported by the CE6885-LL (low latency mode) |
4. Exit the traffic classifier view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. (Optional) Enable the device to provide nonstop services upon modification of MQC-based traffic classification rules.
   
   
   ```
   [traffic-policy atomic-update-mode](cmdqueryname=traffic-policy+atomic-update-mode)
   ```
   
   If a traffic classification rule is modified after this command is run, the system delivers the new rule and then deletes the old rule to ensure that traffic is not interrupted.
   
   With this function enabled, if a traffic policy that has been successfully applied fails to be applied again due to its configuration change, the original traffic policy still takes effect.
   
   By default, this function is disabled.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```