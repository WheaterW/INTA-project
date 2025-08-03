Creating a Remote CCC Connection
================================

Creating remote CCC connections enables two CEs that connect to different PEs to communicate.

#### Context

To create a remote CCC connection, configure the inbound interface, next hop IP address, in-label, and out-label for the connection on the PEs connecting to different CEs, and configure two bidirectional static CR-LSPs on the P devices deployed between the PEs. A remote CCC connection is unidirectional, and therefore two such connections must be created.


#### Procedure

* PE configurations
  
  
  
  Perform the following steps on the PEs on both ends of a VC:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ccc**](cmdqueryname=ccc) *ccc-connection-name* **interface** *interface-type1* *interface-number1* [ *interface-number1* ] **in-label** *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop-address* | **out-interface** *interface-type2* *interface-number2* } [ **control-word** | **no-control-word** ] or [**ccc**](cmdqueryname=ccc) **ip-interworking** *ccc-connection-name* **interface** *interface-type1* *interface-number1* [ *interface-number1* ] **in-label** *in-label-value* **out-label** *out-label-value* { **nexthop** *nexthop-address* | **out-interface** *interface-type2* *interface-number2* } [ **control-word** | **no-control-word** ]
     
     
     
     A remote CCC connection is created.
     
     
     
     If the outbound interface specified on a PE is a non-P2P interface (such as an Ethernet interface), you must configure **nexthop** to specify a next hop IP address in this command.
  3. (Optional) Run [**ccc**](cmdqueryname=ccc) *cccName* **description** *text*
     
     
     
     A description is configured for the remote CCC connection.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* P device configurations
  
  
  
  Perform the following steps on the P devices along the VC:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**static-cr-lsp transit**](cmdqueryname=static-cr-lsp+transit) *lsp-name* [ **incoming-interface** *i**ncoming-interfacetype* *incoming-interfacenum* ] **in-label** *in-label* { **nexthop** *next-hop-address* | **outgoing-interface** *outgoing-interfacetype* *outgoing-interfacenum*} \* **out-label** *out-label*
     
     
     
     The P device is configured as the transit LSR for a static CR-LSP.
     
     
     
     Bidirectional static CR-LSPs must be configured on all P devices deployed between the PEs for remote CCC connections to transmit CCC data only.
     
     If the outbound interface specified on a P device is a non-P2P interface, you must configure **nexthop** to specify a next hop IP address in this command.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.