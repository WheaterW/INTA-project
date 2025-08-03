Verifying the Configuration
===========================

After configuring a FlexE interface, verify the configuration.

#### Prerequisites

A FlexE interface has been configured.


#### Procedure

* Run the [**display license resource usage port-flexe**](cmdqueryname=display+license+resource+usage+port-flexe) { **all** | **slot** *slotid* } [ **active** | **deactive** ] command to check information about FlexE interface licenses on boards.
* Run the [**display flexe group information**](cmdqueryname=display+flexe+group+information) **slot** *slotID* **card** *cardID* command to check the group information of a FlexE card.
* Run any of the following commands to check information about FlexE service interfaces, FlexE physical interfaces, and physical interfaces bound to a FlexE group:
  
  
  + [**display flexe client information**](cmdqueryname=display+flexe+information) [ **interface** { *interface-type* *interface-number* | *interface-name* } ]
  + [**display flexe client information**](cmdqueryname=display+flexe+information) [ **index** *clientindex* ]
  + [**display flexe physical-interface information**](cmdqueryname=display+flexe+information) [ **interface** { *interface-type* *interface-number* | *interface-name* } ]
* Run the [**display interface ethernet brief**](cmdqueryname=display+interface+ethernet+brief) command to check brief information about FlexE interfaces.
* Run the [**display interface flexe**](cmdqueryname=display+interface+flexe) *interface-number* command to check the running status and statistics of a FlexE interface.
* Run the [**display lldp neighbor brief**](cmdqueryname=display+lldp+neighbor+brief) command to check brief information about LLDP neighbors of FlexE interfaces.