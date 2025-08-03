(Optional) Configuring Whitelist Session-CAR for QX TCP Connections
===================================================================

You can configure whitelist session-CAR for QX TCP Connections to limit the rate of sessions. This configuration prevents bandwidth preemption among QX TCP sessions if traffic bursts occur.

#### Context

If unauthorized QX TCP packets are used to launch a DDoS attack, authorized QX TCP packets may not reach the QX component in a timely manner, interrupting the QX TCP connection. To address this issue and ensure that authorized QX TCP connections are not interrupted, configure the session-CAR function for QX TCP connections.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car qx-tcp**](cmdqueryname=whitelist+session-car+qx-tcp) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   The whitelist session-CAR parameters for QX TCP connections are configured.
   
   
   
   In normal cases, you are advised to use the default values.
3. (Optional) Run [**whitelist session-car qx-tcp disable**](cmdqueryname=whitelist+session-car+qx-tcp+disable)
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

Run the following command to check the preceding configuration.

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **qx-tcp** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for QX TCP connections on a specified interface board.

To check such statistics generated within a specific period of time, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **qx-tcp** **statistics** **slot** *slot-id* command to clear the existing statistics on the specified interface board. Then, after a certain period of time, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **qx-tcp** **statistics** **slot** *slot-id* command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Cleared whitelist session-CAR statistics cannot be restored. Exercise caution when running the reset command.