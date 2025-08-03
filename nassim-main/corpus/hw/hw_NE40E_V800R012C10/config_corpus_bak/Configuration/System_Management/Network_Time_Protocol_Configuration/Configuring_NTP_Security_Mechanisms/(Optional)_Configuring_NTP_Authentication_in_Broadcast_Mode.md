(Optional) Configuring NTP Authentication in Broadcast Mode
===========================================================

After NTP authentication is enabled, you can configure the authentication key ID used in synchronization with the NTP broadcast server on the local Router to apply NTP authentication in broadcast mode. Perform the following steps on the NTP broadcast server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ntp-service broadcast-server**](cmdqueryname=ntp-service+broadcast-server) [ **authentication-keyid** *key-id* | **version** *version-number* | **port** *port-number* ] \*
   
   
   
   The authentication key ID used by the NTP broadcast server is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.