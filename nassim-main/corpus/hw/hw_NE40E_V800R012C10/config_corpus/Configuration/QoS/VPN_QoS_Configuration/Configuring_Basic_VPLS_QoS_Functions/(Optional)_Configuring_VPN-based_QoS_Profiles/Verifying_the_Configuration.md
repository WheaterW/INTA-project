Verifying the Configuration
===========================

After a VPN-based QoS profile is configured, verify the configuration.

#### Prerequisites

A VPN-based QoS profile has been configured.


#### Procedure

* Run the [**display flow-mapping configuration**](cmdqueryname=display+flow-mapping+configuration) [ **verbose** [ *mapping-name* ] ] command to check the configurations of an FQ mapping object and the referential relations of the object.
* Run the [**display flow-queue configuration**](cmdqueryname=display+flow-queue+configuration) [ **verbose** [ *flow-queue-name* ] ] command to check the configurations of an FQ profile.
* Run the [**display qos-profile configuration**](cmdqueryname=display+qos-profile+configuration) [ *profile-name* ] command to check the configurations of a QoS profile.
* Run the [**display qos-profile application**](cmdqueryname=display+qos-profile+application) *profile-name* command to check the application of a QoS profile.