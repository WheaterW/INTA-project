Verifying the DS-Lite Reliability Configuration
===============================================

After DS-Lite reliability is configured, you can run the following display commands to verify the DS-Lite reliability configuration.

#### Prerequisites

The single-chassis inter-board DS-Lite hot backup and inter-chassis DS-Lite hot backup have been configured.


#### Procedure

* Run the [**display service-ha global-information**](cmdqueryname=display+service-ha+global-information) command to check the inter-board backup delay time of the VSM HA module, the inter-board switchback time, and whether hot backup is enabled.
* Run the [**display service-location**](cmdqueryname=display+service-location) *service-location-id* command to check the configuration of a service-location group.
* Run the [**display service-instance-group**](cmdqueryname=display+service-instance-group) *service-instance-group-name* command to check the configuration of a service-instance group.
* Run the [**display ds-lite instance**](cmdqueryname=display+ds-lite+instance) [ *instance-name* ] command to check the configuration of a DS-Lite instance.