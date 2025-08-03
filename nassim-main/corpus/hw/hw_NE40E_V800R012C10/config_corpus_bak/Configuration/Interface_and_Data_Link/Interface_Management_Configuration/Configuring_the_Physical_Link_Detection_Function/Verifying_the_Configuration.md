Verifying the Configuration
===========================

You can check the interface configuration and state information after configuring the physical link detection function.

#### Context

The physical link detection function has been configured.


#### Procedure

* Run the [**display trap-info**](cmdqueryname=display+trap-info) command in the interface view or run the [**display trap-info**](cmdqueryname=display+trap-info) { *interface-type* *interface-number* | *interface-name* | **slot** *slot-id* **card** *card-id* } command in the system view to check alarm configurations on the specified interface, including the alarm function status, alarm thresholds, detection interval, alarm blocking status, current alarm state, and the number of current alarms.
* Run the [**display port-error-info**](cmdqueryname=display+port-error-info) **interface** { *interface-type* *interface-number* | *interface-name* } command in the interface view to check the trap information about error codes/error packets on the interface.