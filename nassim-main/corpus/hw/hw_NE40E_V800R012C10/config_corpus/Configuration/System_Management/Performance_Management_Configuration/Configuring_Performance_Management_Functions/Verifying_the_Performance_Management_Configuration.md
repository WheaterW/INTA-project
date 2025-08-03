Verifying the Performance Management Configuration
==================================================

After configuring performance management (PM) functions, verify the configuration.

#### Prerequisites

PM has been configured.


#### Procedure

* Run the [**display pm brief**](cmdqueryname=display+pmbrief) command to check brief PM information.
* Run the [**display pm statistics-task**](cmdqueryname=display+pm+statistics-task) [ *task-name* ] command to check information about a specific performance statistics task.
* Run the [**display pm measure-info**](cmdqueryname=display+pm+measure-info) [ **instance-type** *instance-type* ] command to check information about the statistics indicators of a specific type of instances.
* Run the [**display pm statistics**](cmdqueryname=display+pm+statistics) *taskname* **data-index** *index* [ **instance-type** *instance-type-name* [ **measure** *measure-name* | **instance** { *vpn-instance-name* } &<1-8> ] \* ] command to check the performance statistics.
* Run the [**display pm statistics-file**](cmdqueryname=display+pm+statistics-file) [ *task-name* ] command to check the list of performance statistics files.