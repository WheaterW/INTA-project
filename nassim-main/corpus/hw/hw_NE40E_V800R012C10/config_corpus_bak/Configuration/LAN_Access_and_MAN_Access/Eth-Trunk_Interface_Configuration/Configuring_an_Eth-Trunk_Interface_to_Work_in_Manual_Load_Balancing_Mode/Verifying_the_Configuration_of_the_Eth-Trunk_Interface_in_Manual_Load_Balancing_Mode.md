Verifying the Configuration of the Eth-Trunk Interface in Manual Load Balancing Mode
====================================================================================

After an Eth-Trunk interface in manual load balancing mode is successfully configured, verify the configuration, including the Eth-Trunk ID, working mode, and status of member interfaces.

#### Prerequisites

An Eth-Trunk interface in manual load balancing mode has been configured.


#### Procedure

* Run the [**display trunkmembership eth-trunk**](cmdqueryname=display+trunkmembership+eth-trunk) *trunk-id* command to check information about member interfaces of the Eth-Trunk interface.
* Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) [ *trunk-id* [ **interface** *interface-type* *interface-number* |*interface-name* |**verbose**] ] command to check information about the Eth-Trunk interface and its active member interfaces.
* Run the [**display interface eth-trunk**](cmdqueryname=display+interface+eth-trunk) [ *trunk-id* ] command to check the status of the Eth-Trunk interface.
* Run the [**display interface brief**](cmdqueryname=display+interface+brief) command to check brief information about the Eth-Trunk interface, including the physical status, link protocol status, and bandwidth usage.
* Run the [**display trunkfwdtbl eth-trunk**](cmdqueryname=display+trunkfwdtbl+eth-trunk) *trunk-id* [ **slot** *slot-id* ] command to check the forwarding table on the Eth-Trunk interface.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The **slot** *slot-id* parameter in this command is supported only by the admin VS.