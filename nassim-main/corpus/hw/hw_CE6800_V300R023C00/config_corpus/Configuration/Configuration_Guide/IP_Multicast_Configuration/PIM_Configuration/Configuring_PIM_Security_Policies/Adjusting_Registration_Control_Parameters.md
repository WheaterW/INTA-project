Adjusting Registration Control Parameters
=========================================

Adjusting Registration Control Parameters

#### Context

A multicast source DR on a PIM-SM network encapsulates received multicast data into Register messages and unicasts these messages to an RP. The RP then decapsulates the messages and forwards the extracted multicast data to receivers along the RPT. To prevent Register message attacks, a filtering policy can be configured to allow the RP to permit or deny Register messages that match the filtering policy.

After the RP completes the SPT switchover, the multicast data reaches the RP along the SPT in multicast mode. The RP then sends a Register-Stop message to the source DR. After receiving the message, the source DR stops sending Register messages and enters the register-suppression state. During the register-suppression period, the DR periodically sends a Probe message (Null-Register message) to notify the RP that the multicast source is still in the active state. After the register-suppression period expires, the DR resends Register messages.

The multicast source DR adds a registration outbound interface while sending Register messages to the RP. However, sending redundant Register messages deteriorates system processing performance, slowing down convergence. To prevent the redundant Register messages from affecting system performance, configure the multicast source DR to send Probe messages instead of Register messages.

A device with the default settings can work properly. The registration parameters can also be adjusted based on real-world situations. The default settings are recommended for general use.


#### Procedure

* Control the receipt of Register messages on a C-RP.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an advanced ACL and enter the ACL view.
     
     
     ```
     [acl](cmdqueryname=acl) { name advance-acl-name [ advance | [ advance ] number advance-acl-number ] | [ number ] advance-acl-number } [ match-order { config | auto } ]
     ```
  3. Configure a rule for the advanced ACL.
     
     
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } ip [ destination { destination-ip-address { destination-wildcard | 0 } | any } | source { source-ip-address { source-wildcard | 0 } | any } ]
     ```
     
     
     
     In the [**rule**](cmdqueryname=rule) command, the **source** parameter is used to specify a multicast source address, and the **destination** parameter is used to specify a multicast group address.
  4. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Enter the PIM view.
     
     
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  6. Configure a policy for filtering Register messages.
     
     
     ```
     [register-policy](cmdqueryname=register-policy) { advanced-acl-number | acl-name acl-name }
     ```
     
     
     
     The ACL rule functions as follows:
     
     + If the ACL rule with the **permit** action is matched, the RP permits the Register messages within the specified address range.
     + If the ACL rule with the **deny** action is matched, the RP rejects the Register messages within the specified address range.
     + If an ACL rule is not matched, the RP rejects the Register messages within the specified address range.
     + If the applied ACL or ACL rule does not exist, the RP rejects all Register messages.
  7. Configure the function to calculate a checksum based on the content of a Register message.
     
     
     ```
     [register-packet-checksum](cmdqueryname=register-packet-checksum)
     ```
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Control registration suppression on the source DR.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the PIM view.
     
     
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  3. Set a period for keeping the register-suppression state.
     
     
     ```
     [register-suppression-timeout](cmdqueryname=register-suppression-timeout) interval
     ```
     
     
     
     By default, a source DR keeps the register-suppression state for 60s.
     
     + If *interval* is set to a small value, the RP receives burst multicast data more frequently.
     + If *interval* is set to a large value, when the (S, G) entry on the RP times out, the delay for new receivers to join the multicast group is prolonged.
  4. Set an interval at which Probe messages are sent.
     
     
     ```
     [probe-interval](cmdqueryname=probe-interval) interval
     ```
     
     
     
     By default, a source DR sends Probe messages to the RP at an interval of 5 seconds.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Control the sending of Register messages on the source DR.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the PIM view.
     
     
     ```
     [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
     ```
  3. Configure the source DR to send Probe messages instead of Register messages when receiving multicast traffic from the multicast source. This prevents redundant Register messages from affecting device performance.
     
     
     ```
     [register-with-probe](cmdqueryname=register-with-probe)
     ```
     
     By default, Register messages are sent without control.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```