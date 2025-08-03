Configuring an RR and Specifying Its Clients
============================================

RRs reflect routes between clients, and therefore IBGP connections do not need to be established between the clients.

#### Context

In an AS, one Router functions as an RR, and the other Routers function as its clients. The clients establish IBGP connections with the RR. The RR and its clients form a cluster. The RR transmits or reflects routes among clients, but the clients do not need to establish any IBGP connections between each other.

An RR is easy to configure because its configurations only need to be configured on the Router that needs to function as an RR, and clients do not need to know whether they are clients.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *ipv4-address* | *group-name* } [**reflect-client**](cmdqueryname=reflect-client)
   
   
   
   An RR and its clients are configured.
   
   
   
   The Router where the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as the RR, and specified peers or peer groups function as the clients.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The reflect-client configuration in an address family is valid only in this address family and cannot be inherited by other address families.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.