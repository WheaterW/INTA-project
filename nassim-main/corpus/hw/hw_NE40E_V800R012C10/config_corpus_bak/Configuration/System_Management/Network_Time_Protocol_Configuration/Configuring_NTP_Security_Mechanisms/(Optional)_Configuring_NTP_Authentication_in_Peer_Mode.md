(Optional) Configuring NTP Authentication in Peer Mode
======================================================

By configuring the authentication key ID used in the synchronization with the peer on the local end, you can apply NTP authentication in peer mode. Perform the following steps on the symmetric active end.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a key ID for synchronization with a specified NTP peer.
   
   
   * To specify an IP address for the remote peer, run the [**ntp-service unicast-peer**](cmdqueryname=ntp-service+unicast-peer) *ip-address* [ **version** *number* | **authentication-keyid** *key-id* | **source-interface** *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** | **port** *port-number* ] \* command.
   * To specify an IPv6 address for the remote peer, run the [**ntp-service unicast-peer**](cmdqueryname=ntp-service+unicast-peer) **ipv6** *ipv6-address* [ **authentication-keyid** *key-id* | **source-interface** *interface-type
     interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** | **port** *port-number* ] \* command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.