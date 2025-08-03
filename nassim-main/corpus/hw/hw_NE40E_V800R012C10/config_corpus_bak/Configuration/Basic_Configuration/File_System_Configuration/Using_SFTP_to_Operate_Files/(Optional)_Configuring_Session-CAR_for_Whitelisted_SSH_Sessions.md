(Optional) Configuring Session-CAR for Whitelisted SSH Sessions
===============================================================

You can configure Session-CAR for whitelisted SSH sessions to limit the rate at which packets of the whitelisted SSH sessions are sent to the SSH server. This configuration prevents non-whitelisted SSH sessions from preempting bandwidth if the SSH server encounters a traffic burst.

#### Context

When packets sent to the SSH server form a traffic burst, sessions may preempt bandwidth. To resolve this problem, you can configure Session-CAR for whitelisted SSH sessions. This configuration isolates bandwidth resources between sessions. If the default Session-CAR parameters for whitelisted SSH sessions do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car ssh-server**](cmdqueryname=whitelist+session-car+ssh-server){ **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* }\*
   
   
   
   Session-CAR parameters are configured for whitelisted SSH sessions.
3. (Optional) Run [**whitelist session-car ssh-server disable**](cmdqueryname=whitelist+session-car+ssh-server+disable)
   
   
   
   Session-CAR for whitelisted SSH sessions is disabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Generally, you are advised not to disable this function.
4. Run **commit**
   
   
   
   The configuration is committed.