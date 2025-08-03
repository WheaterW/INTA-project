Verifying the Inter-Chassis Hot Backup Configuration
====================================================

After inter-chassis hot backup is configured, check whether the configured members of the HA inter-chassis hot backup and master/slave relationships are correct.

#### Prerequisites

All CGN inter-chassis hot backup configurations have been performed.


#### Procedure

* Run the [**display service-location**](cmdqueryname=display+service-location) *service-location-id* command on the master and backup devices to view configurations of the HA backup group.
* Run the [**display vrrp**](cmdqueryname=display+vrrp) *virtual-router-id* command on the master and backup devices to view configurations of the VRRP group.