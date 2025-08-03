Configuring an NBMA Network
===========================

Configuring an NBMA Network

#### Context

Interfaces send RIP messages in unicast mode only on a non-broadcast multi-access (NBMA) network. In contrast, RIP messages can be sent in broadcast or multicast mode on other networks. Therefore, you need to configure the interfaces on NBMA networks.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a RIP process and enter the RIP view.
   
   
   ```
   [rip](cmdqueryname=rip) [ process-id ]
   ```
3. Configure a RIP neighbor on an NBMA network.
   
   
   ```
   [peer](cmdqueryname=peer) ip-address
   ```
4. Set the interface status to suppressed on the NBMA network.
   
   
   ```
   [silent-interface](cmdqueryname=silent-interface) { all | interface-type interface-number }
   ```
   
   
   
   By default, interfaces can send RIP messages in broadcast or multicast mode. After a RIP interface is configured as a silent interface, the RIP interface only receives RIP messages and updates its routing table, instead of sending RIP messages.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If you want only a small number of interfaces to be active while the rest interfaces are suppressed, run the [**silent-interface**](cmdqueryname=silent-interface) **all** command to suppress all interfaces and then the [**silent-interface**](cmdqueryname=silent-interface) **disable** *interface-type* *interface-number* command to activate specified interfaces.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```