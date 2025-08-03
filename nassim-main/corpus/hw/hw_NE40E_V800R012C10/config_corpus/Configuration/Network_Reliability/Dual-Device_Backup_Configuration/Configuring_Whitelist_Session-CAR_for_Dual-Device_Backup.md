Configuring Whitelist Session-CAR for Dual-Device Backup
========================================================

This section describes how to configure whitelist session-CAR for dual-device backup to isolate bandwidth resources per session for active/standby protocol packets.

#### Context

Whitelist session-CAR for dual-device backup isolates bandwidth resources per session for active/standby protocol packets transmitted between the master and backup devices. This configuration prevents packets over different active/standby protocol sessions from preempting bandwidth resources. You can adjust whitelist session-CAR bandwidth parameters if the defaults do not meet service requirements.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**whitelist session-car rbs-ipv4**](cmdqueryname=whitelist+session-car+rbs-ipv4) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** pbs-value } \* command to adjust bandwidth parameters of whitelist session-CAR for dual-device backup.
   
   
   
   If an excessive number of dual-device backup protocol session packets are sent to the CPU, you can adjust parameters to ensure that the packets are properly sent to the CPU. In normal cases, you are advised to use the default values of these parameters.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In IPv6 scenarios, you can run the [**whitelist session-car rbs-ipv6**](cmdqueryname=whitelist+session-car+rbs-ipv6) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** pbs-value } \* command instead.
3. (Optional) Run the [**whitelist session-car rbs-ipv4 disable**](cmdqueryname=whitelist+session-car+rbs-ipv4+disable) command to disable whitelist session-CAR for dual-device backup.
   
   
   
   You need to disable whitelist session-CAR only when it is abnormal, preventing this function from affecting the sending of dual-device backup protocol packets to the CPU. In normal circumstances, enabling whitelist session-CAR for dual-device backup is recommended.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In IPv6 scenarios, you can run the [**whitelist session-car rbs-ipv6 disable**](cmdqueryname=whitelist+session-car+rbs-ipv6+disable) command instead.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.