Configuring a Route Reflector and Specifying Clients
====================================================

RRs reflect routes between clients, and therefore IBGP connections do not need to be established between the clients.

#### Context

In an AS, one Router functions as an RR, the other Routers function as clients. IBGP connections are established between the RR and its clients. The RR and its clients form a cluster. The RR transmits (or reflects) routes between clients, and clients do not need to establish IBGP connections.

An RR is easy to configure because its configurations only need to be configured on the Router that needs to function as an RR, and clients do not need to know whether they are clients.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The BGP-IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+reflect-client) { *group-name* | *ipv4-address* } [**reflect-client**](cmdqueryname=peer+reflect-client)
   
   
   
   The device is configured as an RR, and a client is specified for it.
   
   
   
   The Router on which the [**peer reflect-client**](cmdqueryname=peer+reflect-client) command is run functions as the RR, and the specified peer or peer group functions as a client.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of RRs and clients in an address family are valid only in this address family and cannot be inherited by other address families. Therefore, configure RRs and clients in the required address family.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.