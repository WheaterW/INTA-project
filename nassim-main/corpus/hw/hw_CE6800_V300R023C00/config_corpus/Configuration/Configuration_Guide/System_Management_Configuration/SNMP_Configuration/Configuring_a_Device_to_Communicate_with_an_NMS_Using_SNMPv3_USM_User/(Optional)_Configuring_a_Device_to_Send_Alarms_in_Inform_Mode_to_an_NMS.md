(Optional) Configuring a Device to Send Alarms in Inform Mode to an NMS
=======================================================================

(Optional) Configuring a Device to Send Alarms in Inform Mode to an NMS

#### Context

A device on which the SNMP agent function is enabled can generate two types of alarms: traps and informs. Traps are messages that notify the NMS of a condition on the network, and informs are alarms that require a reply from the NMS and are resent until a reply is received. Informs are more reliable than traps.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to send traps to the NMS.
   
   
   ```
   [snmp-agent trap enable](cmdqueryname=snmp-agent+trap+enable)
   ```
3. Enable the function of sending a specified trap of a feature to the NMS.
   
   
   ```
   [snmp-agent trap enable feature-name](cmdqueryname=snmp-agent+trap+enable+feature-name) feature-name trap-name trap-name
   ```
   ![](public_sys-resources/note_3.0-en-us.png) If the [**snmp-agent trap enable**](cmdqueryname=snmp-agent+trap+enable) command has been run to enable the trap functions of all modules, or the [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) command has been run to enable three or more trap functions of a module, note the following points:
   * To disable the trap functions of all modules, run the [**snmp-agent trap disable**](cmdqueryname=snmp-agent+trap+disable) command.
   * To restore the trap functions of all modules to the default status, run the [**undo snmp-agent trap enable**](cmdqueryname=undo+snmp-agent+trap+enable) or [**undo snmp-agent trap disable**](cmdqueryname=undo+snmp-agent+trap+disable) command.
   * To disable the trap function for a specified module, run the [**undo snmp-agent trap enable feature-name**](cmdqueryname=undo+snmp-agent+trap+enable+feature-name) command.
4. (Optional) Set the timeout period for waiting to receive Inform ACK messages, the number of times to resend Inform messages, and the maximum number of pending Inform messages (Inform messages that need to be acknowledged).
   
   
   ```
   [snmp-agent inform](cmdqueryname=snmp-agent+inform) { timeout seconds | resend-times times | pending number } *
   ```
   
   By default, the timeout period for waiting to receive an Inform ACK message is 15 seconds, the number of times to resend Inform messages is 3, and the maximum number of pending Inform messages is 39.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   On a network that is unstable, you are advised to increase these values from the default.
5. Set the timeout period for waiting to receive Inform ACK messages and the number of times to resend Inform messages.
   
   
   ```
   [snmp-agent inform](cmdqueryname=snmp-agent+inform) { timeout seconds | resend-times times } * { host-name target-host-name | { address udp-domain ip-address | ipv6 address udp-domain ipv6-address } [ vpn-instance vpn-instance-name ] params securityname { security-name | cipher security-name-cipher } }
   ```
6. Enable the alarm logging function.
   
   
   ```
   [snmp-agent notification-log](cmdqueryname=snmp-agent+notification-log) enable
   ```
   
   
   
   If the link between the managed device and the NMS is faulty, the route is unreachable. In this case, the managed device no longer sends Inform alarms but continues to record alarm logs. After the link recovers, the NMS obtains alarm logs generated during the fault period from the managed device.
   
   The alarm logging function logs only informs. By default, the alarm logging function is disabled.
7. Set the aging time of alarm logs and maximum number of alarm logs allowed to be stored in the log buffer.
   
   
   ```
   [snmp-agent notification-log](cmdqueryname=snmp-agent+notification-log) { global-ageout ageout [ minute minute ] | global-limit limit } *
   ```
   
   
   
   By default, the aging time of alarm logs is 24 hours. Alarm logs are automatically deleted after 24 hours.
   
   By default, a maximum of 500 alarm logs can be stored in the log buffer. If the number of alarm logs exceeds the limit, the earliest alarm log is deleted.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```