Verifying the Configuration
===========================

After configuring EDSG services successfully, check information about the configured service policies and users' value-added services and ensure that EDSG services run properly.

#### Procedure

* Run the [**display service-policy**](cmdqueryname=display+service-policy) { **configuration** [ **name** *config-policy-name* ] | **cache** [ **name** *config-policy-name* ] } command to check the EDSG service policy configuration.
* Run the [**display service-policy configuration global**](cmdqueryname=display+service-policy+configuration+global) command to check global service policy configurations.
* Run the [**display prepaid-profile**](cmdqueryname=display+prepaid-profile) [ **name** *prepaid-profile-name* ] command to check information about a specified prepaid profile.
* Run the [**display value-added-service update-online-edsg process-information**](cmdqueryname=display+value-added-service+update-online-edsg+process-information) command to check online EDSG service update information.
* Run the [**display value-added-service policy**](cmdqueryname=display+value-added-service+policy) command to check service policy information.
* Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) command to check information about users' value-added services.
* Run the [**display value-added-service edsg time-range process-information**](cmdqueryname=display+value-added-service+edsg+time-range+process-information) command to check the process of updating the EDSG service bandwidth based on a time range.
* Run the **display value-added-service user edsg with-car-dropped-flow** command to check information about users whose EDSG service traffic is dropped by CAR.
* Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) **user-id** *user-id* **edsg** command to check information about a specified user's EDSG services whose traffic is dropped by CAR.
* Run the [**display value-added-service user**](cmdqueryname=display+value-added-service+user) **user-id** *user-id* **edsg** **service-index** *service-index-value* command to check information about a specified user's specified EDSG service whose traffic is dropped by CAR.