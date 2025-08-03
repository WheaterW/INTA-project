Configuring an NBMA Network
===========================

RIP packets on a Non-Broadcast Multiple Access (NBMA) network are sent in a mode different from those on networks of other types, and therefore, special configurations are required.

#### Usage Scenario

RIP packets are sent in unicast mode only on an NBMA network. On networks of other types, RIP packets are sent in either broadcast or multicast mode.

Therefore, you need to perform the following configurations for an NBMA network:

* Specify RIP neighbors.
* Prevent interfaces from sending RIP packets in either broadcast or multicast mode.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rip**](cmdqueryname=rip) [ *process-id* ]
   
   
   
   A RIP process is created, and the RIP view is displayed.
3. Run [**peer**](cmdqueryname=peer) *peer-address*
   
   
   
   RIP neighbors are configured on the NBMA network.
4. Perform either of the following operations as required:
   
   
   * Run the [**silent-interface**](cmdqueryname=silent-interface) **all** command to prevent all interfaces from sending RIP packets in either broadcast or multicast mode.
   * Run the [**silent-interface**](cmdqueryname=silent-interface) *interface-type* *interface-number* command to prevent a specified interface from sending RIP packets in either broadcast or multicast mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you want a small number of interfaces to send RIP packets in either broadcast or multicast mode, you can run the [**silent-interface**](cmdqueryname=silent-interface) **all** command first to prevent all interfaces from sending RIP packets in either broadcast or multicast mode and then run the [**silent-interface**](cmdqueryname=silent-interface) **disable** *interface-type* *interface-number* command to restore the capability to send RIP packets in either broadcast or multicast mode for the small number of interfaces.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.