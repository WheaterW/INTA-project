(Optional) Configuring a Server to Force a Client to Renew the IP Address
=========================================================================

(Optional) Configuring a Server to Force a Client to Renew the IP Address

#### Prerequisites

Before configuring a DHCP server to send FORCERENEW messages, you must configure a gateway IP address and address segment for an address pool.


#### Context

To force a DHCP client to enter the RENEW state, configure a DHCP server to send a unicast FORCERENEW message to the client.

* When the DHCP client attempts to renew its lease by unicasting a DHCPREQUEST message to the DHCP server according to the DHCP lease renewal process: If the DHCP server replies with a DHCPACK message, the lease is successfully renewed. If the DHCP server replies with a DHCPNAK message, the DHCP client needs to re-initiate a request.
* When the DHCP server does not receive any response from the DHCP client for a period of time: If address recycling is configured, the server reclaims the corresponding IP address. Otherwise, the server reclaims the IP address when the lease expires, but not when it receives no response in the period.

For example, if a client has gone offline unexpectedly, after you configure the DHCP server to send FORCERENEW messages, it unicasts a FORCERENEW message to the client; however, it does not receive any response from the client. In this case, if address recycling is configured, the server will reclaim the corresponding IP address, implementing efficient allocation of IP addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* [ **server** ]
   
   
   
   An address pool is created and its view is displayed.
3. Run [**gateway**](cmdqueryname=gateway) *ip-address* { *mask* | *mask-length* }
   
   
   
   A gateway IP address and mask are configured for the address pool.
4. Run [**section**](cmdqueryname=section) *section-index* *start-ip-address* [ *end-ip-address* ]
   
   
   
   An address segment is configured for the address pool.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**send forcerenew section**](cmdqueryname=send+forcerenew+section) *sectionNum* [ **ip** *startIp* [ *endIp* ] ] [ **recycle** ]
   
   
   
   The DHCP server is configured to send FORCERENEW messages.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If you run this command again before the DHCP server sends out all FORCERENEW messages, the system displays an error message.
   * To stop the server from sending FORCERENEW messages, run the [**stop send forcerenew**](cmdqueryname=stop+send+forcerenew) command.