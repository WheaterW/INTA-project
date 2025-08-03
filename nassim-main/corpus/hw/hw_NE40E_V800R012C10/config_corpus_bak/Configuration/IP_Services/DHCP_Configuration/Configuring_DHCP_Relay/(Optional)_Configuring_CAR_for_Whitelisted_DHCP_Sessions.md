(Optional) Configuring CAR for Whitelisted DHCP Sessions
========================================================

You can configure an aging time and bandwidth parameters for CAR for whitelisted DHCP sessions to flexibly isolate the sessions.

#### Context

By default, CAR for whitelisted DHCP sessions is enabled to isolate the sessions. This prevents DHCP packets from different DHCP servers from preempting one another's bandwidth resources. A device generates whitelists based on information in DHCP packets from different DHCP servers. After a whitelist is generated, if the device does not receive packets from the DHCP server to which the whitelist belongs within 30 minutes, it ages out the whitelist. If the default aging time and bandwidth parameters of a whitelist involved in CAR for whitelisted DHCP sessions do not meet service requirements, you can adjust them.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car dhcp**](cmdqueryname=whitelist+session-car+dhcp) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** pbs-value } \*
   
   
   
   Bandwidth parameters are configured for CAR for whitelisted DHCP sessions.
3. Run [**whitelist session-car dhcp aging-time**](cmdqueryname=whitelist+session-car+dhcp+aging-time) *aging-time-value*
   
   
   
   An aging time is configured for a whitelist involved in CAR for whitelisted DHCP sessions.
4. (Optional) Run [**whitelist session-car dhcp disable**](cmdqueryname=whitelist+session-car+dhcp+disable)
   
   
   
   CAR for whitelisted DHCP sessions is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.