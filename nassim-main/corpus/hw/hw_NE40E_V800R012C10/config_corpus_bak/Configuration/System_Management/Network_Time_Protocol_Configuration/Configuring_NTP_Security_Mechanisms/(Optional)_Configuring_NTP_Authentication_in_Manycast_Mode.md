(Optional) Configuring NTP Authentication in Manycast Mode
==========================================================

By configuring the authentication key ID used in the synchronization with the NTP manycast client on the local Router, you can apply NTP authentication in manycast mode.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ntp-service manycast-client**](cmdqueryname=ntp-service+manycast-client) [ *ip-address* | **ipv6** [ *ipv6-address* ] ] [ [ **authentication-keyid** *key-id* ] | **ttl** *ttl-number* | **port** *port-number* ] \*
   
   
   
   The authentication key ID used by the NTP manycast client is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.