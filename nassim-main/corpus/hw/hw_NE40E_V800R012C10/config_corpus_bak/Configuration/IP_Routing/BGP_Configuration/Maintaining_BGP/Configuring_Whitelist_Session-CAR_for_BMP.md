Configuring Whitelist Session-CAR for BMP
=========================================

You can configure whitelist session-CAR for BMP to isolate bandwidth resources by session for BMP messages.

#### Context

The function of whitelist session-CAR for BMP sets an independent CAR channel for each BMP session to ensure that the bandwidth of each BMP session is not preempted by other traffic (including traffic of other sessions of the same protocol and traffic of other protocols). When BMP messages form a traffic burst, you can adjust the bandwidth for each BMP session in whitelist session-CAR for BMP to ensure that BMP messages can be sent to the CPU properly.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the function becomes abnormal or affects other services, you can run the [**whitelist session-car bmp disable**](cmdqueryname=whitelist+session-car+bmp+disable) command to disable whitelist session-CAR for BMP. In normal cases, you are advised to keep whitelist session-CAR for BMP enabled.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car bmp**](cmdqueryname=whitelist+session-car+bmp+cir+cbs+pir+pbs) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for BMP are configured.
   
   
   
   In normal cases, you are advised to use the default values.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+bmp+statistics+slot) **bmp** **statistics** **slot** *slot-id* command to check statistics about IPv4 whitelist session-CAR for BMP on a specified interface board. To check the statistics within a specific period of time, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car+bmp+statistics+slot) **bmp** **statistics** **slot** *slot-id* command to clear the existing statistics about IPv4 whitelist session-CAR for BMP on the specified interface board; after a certain period of time, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+bmp+statistics+slot) **bmp** **statistics** **slot** *slot-id* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 

The statistics about whitelist session-CAR for BMP on a specified interface board cannot be restored after being cleared. Therefore, exercise caution before clearing them.