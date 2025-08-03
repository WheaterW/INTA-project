Verifying the NAT Reliability Configuration
===========================================

After configuring NAT reliability, run the following **display** commands to check NAT reliability configurations.

#### Prerequisites

The single-chassis inter-board hot backup has been configured.


#### Procedure

* Run the [**display service-ha global-information**](cmdqueryname=display+service-ha+global-information) **delay-time** command to check the delay time configured for inter-board VSM HA hot backup on a single chassis.
* Run the [**display service-location**](cmdqueryname=display+service-location) *service-location-id* command to check the configuration of a service-location group.
* Run the [**display service-instance-group**](cmdqueryname=display+service-instance-group) *service-instance-group-name* command to check the configuration of a service-instance-group instance group.
* Run the [**display nat instance**](cmdqueryname=display+nat+instance) [ *instance-name* ] command to check the configuration of a NAT instance.