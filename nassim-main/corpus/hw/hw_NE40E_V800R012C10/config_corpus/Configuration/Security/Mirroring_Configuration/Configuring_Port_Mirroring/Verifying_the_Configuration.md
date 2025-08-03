Verifying the Configuration
===========================

After configuring port mirroring, you can view the configuration of the mirrored port and observing port.

#### Procedure

* Run the [**display port-mirroring interface**](cmdqueryname=display+port-mirroring+interface) [ *interface-type interface-number* | **slot** *slot-id* ] command to check the configuration of the mirrored port.
* Run the [**display port-observing interface**](cmdqueryname=display+port-observing+interface) [ *interface-type interface-number* | **slot** *slot-id* ] command to check the configuration of the observing port.
* Run the [**display port-observing observe-index**](cmdqueryname=display+port-observing+observe-index) [ *observe-index* ] command to check the index of the observing port.
* Run the [**display mirror instance**](cmdqueryname=display+mirror+instance) [ *instance-name* ] **location** command to check the configuration of the specified mirroring instance on an EVC Layer 2 sub-interface.
* Run the [**display observe user-defined-filter**](cmdqueryname=display+observe+user-defined-filter) [ *id* ] command to check user-defined mirroring filter rules.
* Run the [**display port-mirroring integration**](cmdqueryname=display+port-mirroring+integration) [ **interface** *interface-type* *interface-number* ] command to check the configuration of port mirroring configured in integrated mode.
* Run the [**display port-observing slot**](cmdqueryname=display+port-observing+slot) [*slotid*] command to check the mapping between the observing port for board-based mirroring and the slot ID of the associated interface board.