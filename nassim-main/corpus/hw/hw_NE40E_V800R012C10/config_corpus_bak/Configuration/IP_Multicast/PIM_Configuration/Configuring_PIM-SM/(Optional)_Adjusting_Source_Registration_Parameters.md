(Optional) Adjusting Source Registration Parameters
===================================================

A new multicast source must register with a Rendezvous Point (RP). You can configure policies of filtering Register messages on the Candidate-Rendezvous Points (C-RPs) and configure a device to calculate the checksum of each Register message based on all the contents of a Register message. In addition, you can set the holdtime of the register-suppression state and the interval for sending null Register messages on the source's Designated router (DR) or disable the source's DR from sending Register messages.

#### Context

On a PIM-SM network, the source's DR encapsulates multicast data into a Register message and sends the message to the RPs in unicast mode. The RP then decapsulates the message and forwards the extracted multicast data to receivers along the rendezvous point tree (RPT). To prevent the attack of invalid Register messages, you can configure the RP to accept or deny the Register messages matching specified rules.

After the RP completes the shortest path tree (SPT) switchover, the multicast data reaches the RP along the source tree in multicast mode. The RP then sends a Register-Stop message to the source's DR. After receiving the message, the source's DR stops sending Register messages and enters the register-suppression state. In the register-suppression period, the DR periodically sends a Probe message (null Register message) to notify the RP that the multicast source is still in the active state. After the register-suppression period expires, the DR resends Register messages.

The Router can work normally with default control parameters. You are allowed to adjust registration parameters based on the specific networking environment.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If there is no special requirement, default parameter values are recommended.



#### Procedure

* Control the receiving of Register messages on the C-RP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
     
     
     
     An advanced ACL is created, and the advanced ACL view is displayed.
  3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
     
     
     
     Rules are configured for the advanced ACL.
     
     Run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a multicast source address, and set the **destination** parameter to a multicast group address.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  6. Run [**register-policy**](cmdqueryname=register-policy) { *advanced-acl-number* | **acl-name** *acl-name* }
     
     
     
     A policy is configured to filter Register messages.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If a Register message matches an ACL rule and the action is **permit**, the RP permits this message.
     + If a Register message matches an ACL rule and the action is **deny**, the RP denies this message.
     + If a Register message does not match any ACL rule, the RP denies this message.
     + If a specified ACL does not exist or does not contain rules, the RP denies all Register messages.
  7. Run [**register-packet-checksum**](cmdqueryname=register-packet-checksum)
     
     
     
     The checksum is calculated based on all the contents of a Register message.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Control register suppression on the source's DR.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The PIM view is displayed.
  3. Run [**register-suppression-timeout**](cmdqueryname=register-suppression-timeout) *interval*
     
     
     
     The holdtime of the register-suppression state is set.
     
     + If *interval* is small, the RP receives burst multicast data more frequently.
     + If *interval* is large, when the (S, G) entry on the RP times out, the delay for new receivers to join the multicast group is prolonged.
  4. Run [**probe-interval**](cmdqueryname=probe-interval) *interval*
     
     
     
     The interval for sending Probe messages (null Register messages) is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.