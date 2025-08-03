Checking the Running Status of EDSG Services
============================================

This section describes how to check the running
status of EDSG services.

#### Context

During routine maintenance, you can perform the following
operations to check the running status of EDSG services.


#### Procedure

* Run the [**display service activate-fail-record**](cmdqueryname=display+service+activate-fail-record) [ **time** *begin-time* *end-time* [ **date** *begin-date* *end-date* ] | **user-id** *user-id* | **policy-name** *policy-name* ] \* command in any view to view
  information about EDSG service activation failures.
* Run the [**display service deactivate-record**](cmdqueryname=display+service+deactivate-record) [ **time** *begin-time* *end-time* [ **date** *begin-date* *end-date* ] | **user-id** *user-id* | **policy-name** *policy-name* ] \* command in any view to view
  EDSG service deactivation information.
* Run the [**display service
  update-fail-record**](cmdqueryname=display+service+update-fail-record) [ **time** *begin-time* *end-time* [ **date** *begin-date* *end-date* ] | **user-id** *user-id* | **policy-name** *policy-name* ] \* command in any view to view information about EDSG
  service update failures.
* Run the [**display service update-fail-record statistics**](cmdqueryname=display+service+update-fail-record+statistics) command
  in any view to view statistics about EDSG service update failures.
* Run the [**display service-policy**](cmdqueryname=display+service-policy) { **configuration** [ **name** *configuration-policy-name* ] | **cache** [ **name** *cache-policy-name* ] } command in any view to
  view information about service policies, including locally configured
  service policies and cached service policies that are downloaded from
  a server.
* Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) command
  to view information about a value-added service.
* Run the [**display
  service-policy configuration global**](cmdqueryname=display+service-policy+configuration+global) command in any
  view to view global service policy configurations.
* Run the [**display service-policy download-configuration**](cmdqueryname=display+service-policy+download-configuration) command
  in any view to view the mode in which a service policy is obtained.
* Run the [**display prepaid-profile**](cmdqueryname=display+prepaid-profile) [ **name** *prepaid-profile-name* ] command
  in any view to view prepaid profile configurations.