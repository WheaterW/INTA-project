Configuring DHCP Relay Proxy
============================

To isolate a DHCP server and defend against attacks, you can enable DHCP relay proxy on the DHCP relay agent.

#### Context

When accessing a network, a DHCP client can obtain the IP address of a DHCP server by exchanging messages with it. This brings security risks to the DHCP server. To hide the real IP address of the server from the client, you can enable DHCP relay proxy on the DHCP relay agent. When the DHCP relay agent working in DHCP relay proxy mode forwards response messages from the DHCP server to the DHCP client, it replaces the IP address of the server with the IP address of the interface connected to the client. This isolates the DHCP server and defends against attacks.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
   
   
   
   DHCP is enabled globally.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured for the interface.
5. Run [**dhcp select relay proxy-mode**](cmdqueryname=dhcp+select+relay+proxy-mode)
   
   
   
   DHCP relay proxy is enabled.
6. (Optional) Run [**dhcp relay proxy server-id-override**](cmdqueryname=dhcp+relay+proxy+server-id-override) *ip-address*
   
   
   
   The DHCP relay agent working in DHCP relay proxy mode is configured to reply with the replaced DHCP server address to clients.
7. Run [**ip relay address**](cmdqueryname=ip+relay+address) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
   
   
   
   The DHCP server IP address associated with options is configured on the relay interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.