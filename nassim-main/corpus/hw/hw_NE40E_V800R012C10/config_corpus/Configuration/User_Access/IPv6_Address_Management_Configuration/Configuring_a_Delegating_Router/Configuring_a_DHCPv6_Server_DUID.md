Configuring a DHCPv6 Server DUID
================================

A DHCPv6 client uses a DHCP unique identifier (DUID) to identify the DHCPv6 server when the client communicates with the server.

#### Context

When the NE40E functions as a DHCPv6 server, its DUID must be configured.

When the NE40E functions as a DHCPv6 relay agent and encapsulates the Option 37 attribute to packets, its DUID must be configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 duid**](cmdqueryname=dhcpv6+duid) { **duid-value** | **llt** }
   
   
   
   A DUID is configured for the DHCPv6 server.
   
   
   
   When a DHCPv6 client interacts with a DHCPv6 server, each of the client and server is identified by a DUID. A DHCPv6 server identifies a DHCPv6 client with a client DUID and uses the client DUID in local address allocation; a DHCPv6 client identifies a DHCPv6 server with a server DUID.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.