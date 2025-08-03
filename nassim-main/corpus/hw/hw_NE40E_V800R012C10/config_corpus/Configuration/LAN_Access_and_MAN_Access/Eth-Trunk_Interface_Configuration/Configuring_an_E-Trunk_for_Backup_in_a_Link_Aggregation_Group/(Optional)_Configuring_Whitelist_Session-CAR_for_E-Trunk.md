(Optional) Configuring Whitelist Session-CAR for E-Trunk
========================================================

You can configure whitelist session-CAR for E-Trunk to isolate bandwidth resources by session for E-Trunk packets. This configuration prevents bandwidth preemption among E-Trunk sessions in the case of a traffic burst.

#### Context

When E-Trunk packets suffer a traffic burst, bandwidth may be preempted among E-Trunk sessions. To resolve this problem, you can configure whitelist session-CAR for E-Trunk to isolate bandwidth resources by session. If the default bandwidth parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure parameters for whitelist session-CAR for E-Trunk.
   
   
   * If the current network is an IPv4 network, run the [**whitelist session-car e-trunk-ipv4**](cmdqueryname=whitelist+session-car+e-trunk-ipv4) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \* command.
   * If the current network is an IPv6 network, run the [**whitelist session-car e-trunk-ipv6**](cmdqueryname=whitelist+session-car+e-trunk-ipv6) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \* command.
   
   In normal cases, you are advised to use the default values of these parameters.
3. (Optional) Disable whitelist session-CAR for E-Trunk.
   
   
   * If the current network is an IPv4 network, run the [**whitelist session-car e-trunk-ipv4 disable**](cmdqueryname=whitelist+session-car+e-trunk-ipv4+disable) command.
   * If the current network is an IPv6 network, run the [**whitelist session-car e-trunk-ipv6 disable**](cmdqueryname=whitelist+session-car+e-trunk-ipv6+disable) command.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.