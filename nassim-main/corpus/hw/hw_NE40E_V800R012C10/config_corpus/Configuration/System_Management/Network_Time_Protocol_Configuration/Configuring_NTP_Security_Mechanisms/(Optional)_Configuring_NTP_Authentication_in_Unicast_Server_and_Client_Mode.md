(Optional) Configuring NTP Authentication in Unicast Server/Client Mode
=======================================================================

By configuring the authentication key ID used in the synchronization with the specific NTP server on the NTP client, you can apply NTP authentication in client/server mode. Perform the following steps on the NTP unicast client.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a key ID for synchronization with a specified NTP server.
   
   
   * To specify an IP address for the NTP server, run the [**ntp-service unicast-server**](cmdqueryname=ntp-service+unicast-server) *ip-address* [ **version** *number* | **authentication-keyid** *key-id* | **source-interface** *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt** ] \* command.
   * To specify an IPv6 address for the NTP server, run the [**ntp-service
     unicast-server**](cmdqueryname=ntp-service+unicast-server) **ipv6** *ipv6-address* [ **authentication-keyid** *key-id* | **source-interface** *interface-type interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt** | **port** *port-number* ] \* command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.