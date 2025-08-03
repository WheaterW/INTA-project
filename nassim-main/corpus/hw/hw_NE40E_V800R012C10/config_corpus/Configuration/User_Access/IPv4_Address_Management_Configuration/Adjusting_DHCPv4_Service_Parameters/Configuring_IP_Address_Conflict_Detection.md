Configuring IP Address Conflict Detection
=========================================

The DHCPv4 server sends ping packets to detect the usage of an IP address to prevent an IP address conflict.

#### Context

Before assigning an IP address to a client, the DHCPv4 server needs to detect whether the IP address is used by another client. This prevents an IP address conflict.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This function can be configured on network-side devices only.

Perform the following steps on the device that functions as a DHCPv4 server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp server ping**](cmdqueryname=dhcp+server+ping) **timeout** **timeout-interval**
   
   
   
   The longest time for the DHCPv4 server to wait for a ping response is configured.
3. Run [**dhcp server ping**](cmdqueryname=dhcp+server+ping) **packets** **packet-number**
   
   
   
   The maximum number of ping packets sent by the DHCPv4 server is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

The [**ping**](cmdqueryname=ping) command is used to check whether a ping response can be received within a specified period. If there is no response after a specific time, a ping packet continues to be sent until the allowed maximum number of ping packets are sent. If there is still no response, the device considers that the IP address is not in use. This ensures that a unique IP address is assigned to the client.