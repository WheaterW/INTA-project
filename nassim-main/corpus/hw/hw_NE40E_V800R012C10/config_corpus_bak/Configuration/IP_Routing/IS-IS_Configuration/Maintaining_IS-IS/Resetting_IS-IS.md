Resetting IS-IS
===============

Resetting an IS-IS process clears all the data of the IS-IS process and re-establishes the adjacency.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Resetting an IS-IS process may cause a service interruption. Therefore, exercise caution when running this command.



#### Procedure

* Run the [**reset isis all**](cmdqueryname=reset+isis+all) [ *process-id* | **vpn-instance** *vpn-instance-name* ] or [**reset isis**](cmdqueryname=reset+isis) *process-id* **all** command to restart the IS-IS process.
* Run the [**reset isis peer**](cmdqueryname=reset+isis+peer) *system-id* [ *process-id* | **vpn-instance** *vpn-instance-name* ] or [**reset isis**](cmdqueryname=reset+isis) *process-id* **peer** *system-id* command to reset the IS-IS neighbor relationship.