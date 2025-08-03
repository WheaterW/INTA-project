(Optional) Configuring CAR for Whitelisted DHCPv6 Sessions
==========================================================

You can configure an aging time and bandwidth parameters for CAR for whitelisted DHCPv6 sessions to flexibly isolate the sessions.

#### Context

By default, CAR for whitelisted DHCPv6 sessions is enabled to isolate the sessions. This prevents DHCPv6 packets from different DHCPv6 servers from preempting one another's bandwidth resources. A device generates whitelists based on information in DHCPv6 packets from different DHCPv6 servers. After a whitelist is generated, if the device does not receive packets from the DHCPv6 server to which the whitelist belongs within 30 minutes, it ages out the whitelist. If the default aging time and bandwidth parameters of a whitelist involved in CAR for whitelisted DHCPv6 sessions do not meet service requirements, you can adjust them.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car dhcpv6**](cmdqueryname=whitelist+session-car+dhcpv6) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** pbs-value } \*
   
   
   
   Bandwidth parameters are configured for CAR for whitelisted DHCPv6 sessions.
3. Run [**whitelist session-car dhcpv6 aging-time**](cmdqueryname=whitelist+session-car+dhcpv6+aging-time) *aging-time-value*
   
   
   
   An aging time is configured for a whitelist involved in CAR for whitelisted DHCPv6 sessions.
4. (Optional) Run [**whitelist session-car dhcpv6 disable**](cmdqueryname=whitelist+session-car+dhcpv6+disable)
   
   
   
   CAR for whitelisted DHCPv6 sessions is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.