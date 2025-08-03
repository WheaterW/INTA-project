(Optional) Configuring the Alarm Function for IPv6/MAC Spoofing Attacks
=======================================================================

This section describes how to configure the device to generate an alarm when the number of discarded IPv6/MAC spoofing attack packets reaches the specified threshold.

#### Context

After a DHCPv6 snooping binding table is configured, if the information in an IPv6 packet under an IPv6/MAC spoofing attack is inconsistent with that in the binding table, the IPv6 packet will be discarded. You can also configure an alarm threshold for discarding packets. An alarm is generated when the number of discarded packets exceeds the specified threshold.


#### Procedure

1. Run the **system-view** command to enter the system view.
2. Run the **interface** *interface-type* *interface-number* command to enter the interface view.
3. Run the [**dhcpv6 snooping check ipv6 enable**](cmdqueryname=dhcpv6+snooping+check+ipv6+enable) command to enable the IPv6 packet check function on the interface.
4. Run the **dhcpv6 snooping alarm ipv6 enable** command to enable the alarm function for IPv6/MAC spoofing attacks on the interface.
5. (Optional) Run the [**dhcpv6 snooping alarm ipv6 threshold**](cmdqueryname=dhcpv6+snooping+alarm+ipv6+threshold) *threshold-value* command to set an alarm threshold for discarding IPv6 packets on the interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Alternatively, you can run the [**dhcpv6 snooping alarm threshold**](cmdqueryname=dhcpv6+snooping+alarm+threshold) *threshold-value* command in the system view to set a global alarm threshold for IPv6 packet discarding.
   
   If the alarm function for discarding IPv6 packets has been enabled on an interface but no alarm threshold is configured on the interface, the alarm threshold configured in the system view is used. If an alarm threshold is configured both globally and on the interface, the alarm threshold configured on the interface is used.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.