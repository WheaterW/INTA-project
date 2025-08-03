Clearing EDSG Service Information
=================================

If EDSG services fail, you can clear the historical information about EDSG service failures before attempting to reproduce the fault.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After you clear the historical information about EDSG service failures, the information cannot be restored. Exercise caution when clearing information about EDSG service failures.



#### Procedure

* Run the [**reset service activate-fail-record**](cmdqueryname=reset+service+activate-fail-record) command in the user view to clear information about EDSG service activation failures.
* Run the [**reset service deactivate-record**](cmdqueryname=reset+service+deactivate-record) command in the user view to clear EDSG service deactivation information.
* Run the [**reset service update-fail-record**](cmdqueryname=reset+service+update-fail-record) command in the user view to clear information about EDSG service update failures.
* Run the [**reset value-added-service edsg time-range process-information**](cmdqueryname=reset+value-added-service+edsg+time-range+process-information) command in the user view to clear the process of updating the EDSG service bandwidth based on a time range.
* Run the [**reset value-added-service user**](cmdqueryname=reset+value-added-service+user) **user-id** *user-id-val* [**edsg**](cmdqueryname=edsg) [ **service-index** *service-index-value* ] [**car-dropped-flow statistics**](cmdqueryname=car-dropped-flow+statistics) command in the user view to clear statistics about CAR-dropped EDSG service traffic.