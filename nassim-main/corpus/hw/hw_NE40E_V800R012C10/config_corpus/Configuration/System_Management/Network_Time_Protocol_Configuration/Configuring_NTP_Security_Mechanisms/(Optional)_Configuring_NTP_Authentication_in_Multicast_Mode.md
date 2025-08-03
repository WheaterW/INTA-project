(Optional) Configuring NTP Authentication in Multicast Mode
===========================================================

By configuring the authentication key ID used in the synchronization with the NTP multicast server on the local Router, you can apply NTP authentication in multicast mode. Perform the following steps on the NTP multicast server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Configure a key ID for synchronization with a specified NTP multicast server.
   
   
   * To configure a key ID for synchronization with a specified NTP IPv4 multicast server, run the [**ntp-service multicast-server**](cmdqueryname=ntp-service+multicast-server) [ *ip-address* ] [ **authentication-keyid** *key-id* | **ttl** *ttl-number* | **version** *number* | **port** *port-number* ] \* command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.