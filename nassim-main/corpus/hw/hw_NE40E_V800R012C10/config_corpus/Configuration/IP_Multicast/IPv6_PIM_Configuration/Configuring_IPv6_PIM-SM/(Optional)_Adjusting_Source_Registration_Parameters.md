(Optional) Adjusting Source Registration Parameters
===================================================

A new multicast source must register with a Rendezvous Point (RP). You can configure policies of filtering Register messages on the Candidate-Rendezvous Points (C-RPs) and set the holdtime of the register-suppression state and the interval for sending null Register messages on the source's DR or disable the source's DR from sending Register messages.

#### Context

On an IPv6 PIM-SM network, the source's Designated router (DR) encapsulates multicast data into a Register message and sends the message to the RPs in unicast mode. The RP then decapsulates the message and forwards the extracted IPv6 multicast data to receivers along the rendezvous point tree (RPT). To prevent the attack of invalid Register messages, you can configure the RP to accept or deny the Register messages matching specified rules.

After the RP completes the shortest path tree (SPT) switchover, the IPv6 multicast data reaches the RP along the source tress in multicast mode. The RP then sends a Register-Stop message to the source's DR. After receiving the message, the source's DR stops sending Register messages and enters the suppression state. In the register suppression period, the DR periodically sends a probe messages (null Register message) to notify the RP that the multicast source is still in the active state. After the register suppression period expires, the DR resends the Register messages carrying multicast data

The Router can work normally with default control parameters. You are allowed to adjust registration parameters based on the specific networking environment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Procedure

* Control the receiving of Register messages on a C-RP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ]
     
     
     
     An advanced ACL6 is created, and the advanced ACL6 view is displayed.
  3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ipv6** [ **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
     
     
     
     Rules are configured for the advanced ACL6.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
     
     Run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a multicast source address, and set the **destination** parameter to a multicast group address.
  6. Run [**register-policy**](cmdqueryname=register-policy) { *registerPolicyAclNum* | **acl6-name** *regPolicyName* }
     
     
     
     A policy is configured to filter Register messages.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a Register message matches an ACL rule and the action is **permit**, the RP permits this message.
     + If a Register message matches an ACL rule and the action is **deny**, the RP denies this message.
     + If a Register message does not match any ACL rule, the RP denies this message.
     + If a specified ACL does not exist or does not contain rules, the RP denies all Register messages.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Suppress multicast source registration on the source's DR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
     
     
     
     The IPv6 PIM view is displayed.
  3. Run [**register-suppression-timeout**](cmdqueryname=register-suppression-timeout) *interval*
     
     
     
     The timeout period during which the source's DR keeps the register suppression state is set.
     
     
     
     + If the value of interval is small, the RP frequently receives burst multicast data.
     + If the value of interval is large, when an (S, G) entry on the RP times out, the delay during which new receivers join a multicast group is prolonged.
  4. Run [**probe-interval**](cmdqueryname=probe-interval) *interval*
     
     
     
     The interval for sending Probe messages is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.