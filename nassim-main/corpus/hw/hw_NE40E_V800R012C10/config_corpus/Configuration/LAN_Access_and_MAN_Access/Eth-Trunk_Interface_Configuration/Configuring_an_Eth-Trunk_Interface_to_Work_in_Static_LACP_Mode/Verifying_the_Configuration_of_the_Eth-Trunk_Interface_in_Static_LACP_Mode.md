Verifying the Configuration of the Eth-Trunk Interface in Static LACP Mode
==========================================================================

After an Eth-Trunk interface is configured in static LACP mode, verify the configuration, including the interface ID, working mode, member interface status, LACP system priority, LACP interface priority, and LACP preemption delay.

#### Prerequisites

An Eth-Trunk interface has been configured in static LACP mode.


#### Procedure

* Run the [**display trunkmembership eth-trunk**](cmdqueryname=display+trunkmembership+eth-trunk) *trunk-id* command to check information about member interfaces of the Eth-Trunk interface.
* Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) [ *trunk-id* [ **interface** {*interface-type* *interface-number* | interface-name } ] ] command to check information about the Eth-Trunk interface and its active member interfaces.
* Run the [**display interface eth-trunk**](cmdqueryname=display+interface+eth-trunk) [ *trunk-id* ] command to check the Eth-Trunk interface status.
* Run the [**display interface brief**](cmdqueryname=display+interface+brief) command to check brief information about the Eth-Trunk interface, including the physical status, link protocol status, and bandwidth usage.
* Run the [**display trunkfwdtbl eth-trunk**](cmdqueryname=display+trunkfwdtbl+eth-trunk) *trunk-id* [ **slot** *slot-id* ] command to check the forwarding table on the Eth-Trunk interface.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The parameter **slot** *slot-id* in this command is supported only on the Admin-VS.