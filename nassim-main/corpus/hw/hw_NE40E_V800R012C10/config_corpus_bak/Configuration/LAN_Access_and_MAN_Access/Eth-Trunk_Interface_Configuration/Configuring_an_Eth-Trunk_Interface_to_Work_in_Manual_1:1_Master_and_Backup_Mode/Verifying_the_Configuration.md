Verifying the Configuration
===========================

After configuring an Eth-Trunk interface in manual 1:1 master/backup mode, you can check the ID, working mode, and member interface status of the Eth-Trunk interface.

#### Prerequisites

An Eth-Trunk interface in manual 1:1 master/backup mode has been configured.


#### Procedure

* Run the [**display eth-trunk**](cmdqueryname=display+eth-trunk) [ *trunk-id* [ **interface** *interface-type* *interface-number* ] ] command to check the configuration of the Eth-Trunk interface in manual 1:1 master/backup mode and active interface information.
* Run the [**display trunkmembership eth-trunk**](cmdqueryname=display+trunkmembership+eth-trunk) *trunk-id* command to check information about Eth-Trunk member interfaces.