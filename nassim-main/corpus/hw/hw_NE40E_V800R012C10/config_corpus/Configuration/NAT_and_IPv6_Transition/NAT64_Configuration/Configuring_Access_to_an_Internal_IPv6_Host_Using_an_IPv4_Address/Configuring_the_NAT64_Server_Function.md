Configuring the NAT64 Server Function
=====================================

IPv4 users can access an IPv6 server if the device is configured with NAT64.

#### Usage Scenario

NAT64 allows IPv6 users to initiate access to IPv4 services. IPv4 users, however, cannot access IPv6 users.

To address this problem, the internal server function can be configured on the private network where a NAT64 device resides. The internal server function in a NAT64 instance implements reverse translation from IPv4 addresses to IPv6 addresses based on statically configured mapping between IPv4 addresses and pairs of IPv6 addresses and prefixes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT64 instance view is displayed.
3. Run [**nat64 server global**](cmdqueryname=nat64+server+global) *global-address* [ **vpn-instance** *vpn-instance-name* ] **inside** *host-address* **prefix-id** *prefix-id*
   
   
   
   The internal server is configured in the NAT64 instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address of the internal server must be different from the IP address of a DHCP server. Otherwise, a message about the address conflict is displayed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.