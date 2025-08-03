(Optional) Configuring the Local Port Forwarding Service for the SSH Server
===========================================================================

After the local port forwarding service is enabled on the SSH server, a forwarding channel can be established between the SSH server and a host with a specified IP address and port number.

#### Context

The SSH server can receive forwarding request messages from the SSH client and establish a TCP connection (forwarding channel) with a host with a specified IP address and port number to forward data received from the client to the host only after the local port forwarding function is enabled on the SSH server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssh server tcp forwarding enable**](cmdqueryname=ssh+server+tcp+forwarding+enable)
   
   
   
   The local port forwarding service is enabled on the SSH server.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.