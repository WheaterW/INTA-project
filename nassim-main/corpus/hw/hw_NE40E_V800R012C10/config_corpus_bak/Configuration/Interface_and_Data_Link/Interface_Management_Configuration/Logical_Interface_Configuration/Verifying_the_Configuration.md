Verifying the Configuration
===========================

After the configuration is completed on the Global-VE interface, FlexE interface license, FlexE interface, loopback interface, and Null interface, check the configurations.

#### Prerequisites

The Global-VE interface, FlexE interface license, FlexE interface, loopback interface, and NULL interface have been configured.


#### Procedure

* Run the [**display interface global-ve**](cmdqueryname=display+interface+global-ve) [ *ve-number* ] command to check the status of the Global-VE interface.
* Run the [**display license resource usage port-flexe**](cmdqueryname=display+license+resource+usage+port-flexe) { **all** | **slot** *slot-id* } [ **active** | **deactive** ] command to check information about FlexE interface licenses on boards.
* Run the [**display license resource usage port-mode-channel**](cmdqueryname=display+license+resource+usage+port-mode-channel) { **all** | **slot** *slotid* } [ **active** | **deactive** ] command to check authorization information about the channelized sub-interface license on boards.
* Run the [**display interface loopback**](cmdqueryname=display+interface+loopback) [ *loopback-number* ] command to check the status of the Loopback interface.
* Run the [**display interface null**](cmdqueryname=display+interface+null) [ **0** ] command to check the status of the Null interface.
* Run the [**display flexe group information**](cmdqueryname=display+flexe+group+information) **slot** *slotID* **card** *cardID* command to check information about groups, FlexE physical interfaces added to the groups, and timeslot allocation in the groups on a FlexE subcard.