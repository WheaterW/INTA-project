(Optional) Configuring Session-CAR for Whitelisted FTP Sessions
===============================================================

You can configure Session-CAR for whitelisted FTP sessions to limit the rate at which packets of the whitelisted FTP sessions are sent to the FTP server. This configuration prevents non-whitelisted FTP sessions from preempting bandwidth if the FTP server encounters a traffic burst.

#### Context

When packets sent to the FTP server form a traffic burst, sessions may preempt bandwidth. To resolve this problem, you can configure Session-CAR for whitelisted FTP sessions. This configuration isolates bandwidth resources between sessions. If the default Session-CAR parameters for whitelisted FTP sessions do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car ftp-server**](cmdqueryname=whitelist+session-car+ftp-server){ **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* }\*
   
   
   
   Session-CAR parameters are configured for whitelisted FTP sessions.
3. (Optional) Run [**whitelist session-car ftp-server disable**](cmdqueryname=whitelist+session-car+ftp-server+disable)
   
   
   
   Session-CAR for whitelisted FTP sessions is disabled.
4. Run **commit**
   
   
   
   The configuration is committed.