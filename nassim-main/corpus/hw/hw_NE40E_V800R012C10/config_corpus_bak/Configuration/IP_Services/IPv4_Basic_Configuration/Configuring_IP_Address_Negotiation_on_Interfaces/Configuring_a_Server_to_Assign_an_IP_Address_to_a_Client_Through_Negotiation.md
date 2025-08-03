Configuring a Server to Assign an IP Address to a Client Through Negotiation
============================================================================

After an IP address is specified on a server, the server can assign this IP address to a client.

#### Context

The IP address to be assigned to a client cannot be the same as the IP address of the server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section does not apply to the NE40E-M2K-B.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface that directly connects to the client is displayed.
   
   
   
   IP address negotiation can be configured only on PPP-encapsulated interfaces.
3. Run [**remote address**](cmdqueryname=remote+address) *ip-address*
   
   
   
   An IP address to be assigned to a client is specified.
   
   
   
   The IP address to be assigned to a client cannot be the same as the IP address of the server.
4. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The interface is shut down.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**undo shutdown**](cmdqueryname=undo+shutdown)
   
   
   
   The interface is enabled.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.