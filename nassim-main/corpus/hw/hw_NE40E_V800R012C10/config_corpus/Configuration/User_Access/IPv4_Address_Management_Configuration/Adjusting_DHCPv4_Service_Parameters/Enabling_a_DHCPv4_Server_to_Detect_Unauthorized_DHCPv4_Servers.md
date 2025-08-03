Enabling a DHCPv4 Server to Detect Unauthorized DHCPv4 Servers
==============================================================

Enabling a DHCPv4 server to detect unauthorized DHCPv4 servers help prevent unauthorized DHCPv4 servers from allocating invalid IP addresses to clients.

#### Context

If a private DHCPv4 server exists on the network, clients cannot obtain correct IP addresses and therefore cannot log in to the network because this private DHCPv4 server will interact with the DHCPv4 clients during address application. Such a private DHCPv4 server is an unauthorized DHCPv4 server.

The logs contain IP addresses of all the DHCPv4 servers that allocate IP addresses to clients. By viewing these logs, the administrator can determine whether an unauthorized DHCPv4 server exists.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp invalid-server-detecting**](cmdqueryname=dhcp+invalid-server-detecting) [ *interval* ]
   
   
   
   The interval at which unauthorized DHCPv4 servers are detected is configured.
   
   If the interval at which unauthorized DHCPv4 servers are detected is 0, the NE40E does not detect unauthorized DHCPv4 servers.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can perform this function on only the devices on the BAS side.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.