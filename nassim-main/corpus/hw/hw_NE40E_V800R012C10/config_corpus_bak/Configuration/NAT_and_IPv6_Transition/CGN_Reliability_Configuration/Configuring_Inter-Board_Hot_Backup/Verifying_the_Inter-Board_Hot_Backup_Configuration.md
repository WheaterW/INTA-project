Verifying the Inter-Board Hot Backup Configuration
==================================================

Verifying_the_Inter-Board_Hot_Backup_Configuration

#### Prerequisites

Single-chassis inter-board hot backup has been configured.


#### Procedure

* Run the [**display service-ha global-information**](cmdqueryname=display+service-ha+global-information) **delay-time** command to check the delay time configured for inter-board VSM HA hot backup on a single chassis.
* Run the [**display service-ha global-information**](cmdqueryname=display+service-ha+global-information) **preempt-time** command to check the switchback time for inter-board VSM HA hot backup on a single chassis.
* Run the [**display service-location**](cmdqueryname=display+service-location) *service-location-id* command to check the configuration of a service-location group.
* Run the [**display service-instance-group**](cmdqueryname=display+service-instance-group) *service-instance-group-name* command to check the configuration of a service-instance group.