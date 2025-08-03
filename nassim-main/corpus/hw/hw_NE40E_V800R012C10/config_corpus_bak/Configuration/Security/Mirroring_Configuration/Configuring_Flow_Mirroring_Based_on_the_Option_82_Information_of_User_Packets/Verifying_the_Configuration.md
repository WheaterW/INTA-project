Verifying the Configuration
===========================

After configuring flow mirroring, you can check the traffic behavior, traffic classifier, traffic policy, and port mirroring configurations.

#### Procedure

* Run the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) **global-acl** command to check global traffic policy statistics.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check the configurations of a specified or all traffic classifiers in a specified or all traffic policies as well as the configurations of the traffic behaviors associated with the traffic classifiers.
* Run the [**display service-policy**](cmdqueryname=display+service-policy) { **configuration** [ **name** *configuration-policy-name* | **global** ] | **cache** [ **name** *cache-policy-name* ] } command to check the service policy configuration and the service group bound to the service policy.
* Run the [**display port-observing interface**](cmdqueryname=display+port-observing+interface) [ *interface-type interface-number* | **slot** *slot-id* ] command to check the observing port configuration of a specified interface or interface board.