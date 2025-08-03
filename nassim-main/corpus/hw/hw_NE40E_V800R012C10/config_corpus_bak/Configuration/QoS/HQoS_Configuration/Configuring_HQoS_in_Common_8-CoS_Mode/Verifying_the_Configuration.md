Verifying the Configuration
===========================

After profile-based HQoS is configured on an interface, you can view information about queue profiles and packet statistics on the interface.

#### Context

Run the following commands to check the configuration.


#### Procedure

* Run the [**display flow-mapping configuration**](cmdqueryname=display+flow-mapping+configuration) [ **verbose** [ *mapping-name* ] ] command to check the configuration and reference relationship of an FQ mapping object.
* Run the [**display flow-queue configuration**](cmdqueryname=display+flow-queue+configuration) [ **verbose** [ *flow-queue-name* ] ] command to check the configuration of an FQ profile.
* Run the [**display flow-wred configuration**](cmdqueryname=display+flow-wred+configuration) [ **verbose** [ *flow-wred-name* ] ] command to check the configuration of a flow WRED object.
* Run the [**display user-group-queue configuration**](cmdqueryname=display+user-group-queue+configuration) [ **verbose** [ *group-name* ] ] command to check the configuration and reference relationship of a GQ.
* Run the [**display user-group-queue statistics**](cmdqueryname=display+user-group-queue+statistics) command to check GQ statistics.
* Run the [**display qos-profile application**](cmdqueryname=display+qos-profile+application) command to check the application of QoS profiles.
* Run the [**display qos-profile statistics**](cmdqueryname=display+qos-profile+statistics) command to check QoS profile statistics.
* Run the [**monitor qos-profile statistics**](cmdqueryname=monitor+qos-profile+statistics) command to monitor QoS profile statistics.