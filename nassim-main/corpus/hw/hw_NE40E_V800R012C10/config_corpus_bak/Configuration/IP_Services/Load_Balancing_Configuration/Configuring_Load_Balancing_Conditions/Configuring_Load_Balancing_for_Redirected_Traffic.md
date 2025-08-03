Configuring Load Balancing for Redirected Traffic
=================================================

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   A traffic classifier is created and its view is displayed.
3. Configure match clauses for the traffic classifier. Currently, the match clauses that can be configured is shown in [Table 1](#EN-US_CONCEPT_0172365023__tab_load-balancel_feature_04801).
4. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behaviorâname*
   
   A traffic behavior is created and its view is displayed.
5. Run [**redirect**](cmdqueryname=redirect) **ipv4-multinhp** { **nhp** *ip-address* **interface** *interface-type interface-number* } &<2-42> **loadbalance**
   
   The device is configured to forward redirected packets in load-balancing mode.
   
   The outbound interface cannot be a QinQ sub-interface.
6. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   A traffic policy is created and its view is displayed.
7. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence* ]
   
   The traffic behavior is associated with the traffic classifier in the traffic policy.
8. Apply the traffic policy.
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
   2. Run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** [ **link-layer** | **all-layer** ] command to apply the traffic policy to the inbound direction of the interface.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The traffic policy containing the redirection action can be applied only to the inbound direction of an interface.
      * To apply a traffic policy to a BAS interface, run the [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** command in the system view.
9. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

**Table 1** Match clauses that can be configured in a traffic classifier
| Command Format | Function |
| --- | --- |
| **if-match** [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* } | Matching against ACL rules |
| **if-match** [ **ipv6** ] **dscp** *dscp-value* | Matching against a DSCP value |
| **if-match tcp syn-flag** *tcpflag-value* | Matching against an IPv4 TCP flag |
| **if-match ipv6 tcp syn-flag** *tcpflag-value* | Matching against an IPv6 TCP flag |
| **if-match ip-precedence** *ip-precedence* | Matching against an IP precedence |
| **if-match mpls-exp** *exp-value* | Matching against an MPLS EXP value |
| **if-match 8021p** *8021p-value* | Matching against the 802.1p value in VLAN packets |
| **if-match destination-mac** *mac-address* | Matching against the destination MAC address in VLAN packets |
| **if-match source-mac** *mac-address* | Matching against the source MAC address in VLAN packets |
| **if-match** [ **ipv6** ] **any** | Matching all IP packets |
| **if-match ipv6 next-header** *header-number* **first-next-header** | Matching against the IPv6 next header |
| **if-match ipv6 source-address** *ipv6-address prefix-length* | Matching against the source address of IPv6 packets |
| **if-match ipv6 destination-address** *ipv6-address prefix-length* | Matching against the destination address of IPv6 packets |


#### Follow-up Procedure

Run the **save** command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.