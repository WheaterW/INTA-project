Configuring a Client to Obtain an IP Address Through Negotiation
================================================================

After interface IP address negotiation is enabled on a client, the client can obtain an IP address from the server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface that directly connects to the server is displayed.
   
   IP address negotiation can be configured only on PPP-encapsulated interfaces.
3. Run [**ip address ppp-negotiate**](cmdqueryname=ip+address+ppp-negotiate)
   
   
   
   IP address negotiation is enabled on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.