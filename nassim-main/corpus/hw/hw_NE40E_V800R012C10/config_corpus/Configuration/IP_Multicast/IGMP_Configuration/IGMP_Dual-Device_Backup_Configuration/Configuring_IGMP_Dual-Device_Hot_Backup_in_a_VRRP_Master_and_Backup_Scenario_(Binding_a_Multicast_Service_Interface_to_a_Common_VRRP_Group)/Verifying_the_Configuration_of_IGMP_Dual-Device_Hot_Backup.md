Verifying the Configuration of IGMP Dual-Device Hot Backup
==========================================================

After configuring IGMP dual-device hot backup, verify the configuration.

#### Prerequisites

IGMP dual-device hot backup has been configured.


#### Procedure

* Run the [**display remote-backup-profile**](cmdqueryname=display+remote-backup-profile) [ **profile-name** ] command to check information about RBPs.
* Run the [**display remote-backup-service**](cmdqueryname=display+remote-backup-service) [ *service-name* [ [**verbose**](cmdqueryname=verbose) ] ] command to check information about RBSs.
* Run the [**display multicast rui**](cmdqueryname=display+multicast+rui) [ **vpn** *vpn-name* ] **source** *source-address* **group** *group-address* **eth-trunk** *eth-trunk-id* command to check whether a specified Eth-Trunk interface can forward the traffic of a specified multicast group.