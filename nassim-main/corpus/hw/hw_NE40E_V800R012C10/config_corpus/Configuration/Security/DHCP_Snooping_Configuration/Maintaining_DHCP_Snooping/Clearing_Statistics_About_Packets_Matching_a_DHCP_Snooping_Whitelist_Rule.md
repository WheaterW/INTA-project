Clearing Statistics About Packets Matching a DHCP Snooping Whitelist Rule
=========================================================================

This section describes how to clear statistics about packets
matching a DHCP snooping whitelist rule.

#### Usage Scenario

After the DHCP snooping whitelist
function is configured, the system collects statistics about packets
matching DHCP snooping whitelists. You can run the [**display dhcp snooping white-list**](cmdqueryname=display+dhcp+snooping+white-list) [ **rule-id** *rule-id* ] [ **slot** *slot-id* ] **statistics** command to check statistics about packets matching a DHCP snooping
whitelist rule. Before running the display command to check statistics
about packets matching a DHCP snooping whitelist rule, clear existing
statistics.![](../../../../public_sys-resources/notice_3.0-en-us.png) The statistics about packets matching
a DHCP snooping whitelist rule cannot be restored after you clear
them. Therefore, excise cautions before you clear the statistics.


#### Procedure

Run the [**reset
dhcp snooping white-list**](cmdqueryname=reset+dhcp+snooping+white-list) [ **rule-id** *rule-id* ] [ **slot** *slot-id* ] **statistics** command
in the system view to clear statistics about packets matching a DHCP
snooping whitelist rule.