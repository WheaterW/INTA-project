(Optional) Configuring Whitelist Session-CAR for Telnet
=======================================================

You can configure whitelist session-CAR for Telnet to limit the rate of Telnet packets based on sessions. This configuration prevents Telnet server sessions from preempting bandwidth if the Telnet server encounters a traffic burst.

#### Context

When packets sent to the Telnet server form a traffic burst, Telnet server sessions may preempt bandwidth. To resolve this problem, you can configure whitelist session-CAR for Telnet to limit the rate of Telnet packets based on sessions. This configuration isolates bandwidth resources between Telnet server sessions. If the default bandwidth parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car telnet-server**](cmdqueryname=whitelist+session-car+telnet-server){ **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* }\*
   
   
   
   Whitelist session-CAR parameters are configured for Telnet.
3. (Optional) Run [**whitelist session-car telnet-server disable**](cmdqueryname=whitelist+session-car+telnet-server+disable)
   
   
   
   Whitelist session-CAR is disabled for Telnet.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Generally, you are advised not to disable this function.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.