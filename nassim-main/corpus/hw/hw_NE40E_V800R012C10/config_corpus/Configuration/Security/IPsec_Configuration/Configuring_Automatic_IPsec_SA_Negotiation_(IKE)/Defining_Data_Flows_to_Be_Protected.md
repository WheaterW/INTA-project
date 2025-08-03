Defining Data Flows to Be Protected
===================================

IPsec can protect various data flows. In practice, you need to define data flows through an advanced ACL and apply the ACL in a security policy. Therefore, data flows are protected.

#### Context

Data flows to be protected are defined through advanced ACLs. For data flows that require different security levels, different advanced ACLs must be created.

According to ACL rules, IPsec identifies which packets need or do not need security protection. Data flows matching advanced ACLs (permit) are processed by IPsec for protection before being sent. Data flows that do not match advanced ACLs are forwarded directly. In addition, if data flows should have been encrypted but actually not, they are considered as attack data flows and discarded.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl+name+advance+advance+number+number+match-order+config+auto) { **name** *advance-acl-name* { **advance** | [ **advance** ] **number** *advance-acl-number* } | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
   
   
   
   The advanced ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule)
   
   
   
   Configure a rule for the advanced ACL.
   
   Pay attention to the following items:
   * It is recommended that you configure symmetrical ACL rules at two ends. Symmetrical ACL rules at two ends are not essential but are easier and not prone to errors in actual applications.
   * An IPsec policy can only apply a single ACL. The original configuration must be deleted before a new ACL is applied in the IPsec policy.
   * An ACL cannot include rules containing the deny keyword. The deny action is the same as the permit action. To discard some addresses, use the traffic filtering function. For details, see Applying an ACL to a Filter Policy.
   * ACLs configured in the same security policy group cannot include the same rules.
   * Rules in an ACL can match data flows according to the source or destination IP address, source or destination port, and protocol number only.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When multiple initiators negotiate with the same responder, the ACL rules of each initiator cannot overlap those of any other initiator. If rules overlap, some overlapping traffic cannot be properly encrypted, causing services to be compromised.
   
   During IKEv2 negotiation, intersection ACL rules take effect. If multiple rules are defined in an ACL, the rule that is defined first is used preferentially.
   
   
   IPsec processes the data stream to be protected as follows:
   
   * If packets match the ACL rule with the permit action, the packets are encrypted and sent to the peer end through tunnels.
   * If packets match no ACL rule, the packets are forwarded directly.
   * If a nonexistent ACL or an ACL in which no rule is defined applies to a security policy, packets are dropped.
   * To configure the source and destination port numbers in the ACL of the protected data flow, you must use the **eq** parameter, rather than the **lt**, **gt**, **range**, or **neq** parameter.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.