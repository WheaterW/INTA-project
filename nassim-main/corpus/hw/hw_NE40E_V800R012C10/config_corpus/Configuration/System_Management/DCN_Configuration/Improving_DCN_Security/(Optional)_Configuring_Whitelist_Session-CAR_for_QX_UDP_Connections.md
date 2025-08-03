(Optional) Configuring Whitelist Session-CAR for QX UDP Connections
===================================================================

You can configure whitelist session-CAR for QX UDP Connections to limit the rate of sessions. This configuration prevents bandwidth preemption among QX UDP sessions if traffic bursts occur.

#### Context

If unauthorized QX UDP packets are used to launch a DDoS attack, authorized QX UDP packets may not reach the QX component in a timely manner, interrupting the QX UDP connection. To address this issue and ensure that authorized QX UDP connections are not interrupted, configure the session-CAR function for QX UDP connections.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car qx-udp**](cmdqueryname=whitelist+session-car+qx-udp) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   The whitelist session-CAR parameters for QX UDP connections are configured.
   
   
   
   In normal cases, you are advised to use the default values.
3. (Optional) Run [**whitelist session-car qx-udp disable**](cmdqueryname=whitelist+session-car+qx-udp+disable)
   
   
   
   Whitelist session-CAR is disabled for QX UDP connections.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

Run the following command to check the preceding configuration.

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **qx-udp** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for QX UDP connections on a specified interface board.

To check such statistics generated within a specific period of time, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **qx-udp** **statistics** **slot** *slot-id* command to clear the existing statistics on the specified interface board. Then, after a certain period of time, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **qx-udp** **statistics** **slot** *slot-id* command.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Cleared whitelist session-CAR statistics cannot be restored. Exercise caution when running the reset command.