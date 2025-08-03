Verifying the Configuration
===========================

After the configurations are complete, check the status of the interface, statistics on the interface, and the control-flap operation.

#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type interface-number* ] command to check the status of the interface and statistics on the interface.
* Run the [**display control-flap**](cmdqueryname=display+control-flap) **interface** *interface-type* *interface-number* command to check the configuration and running status of the control-flap function on interfaces.
* Run the [**display counters**](cmdqueryname=display+counters) [ **bit** ] [ **inbound** | **outbound** ] [ **interface** *interface-type* [ *interface-number* ] ] [ **slot** *slot-id* ] command to check the interface traffic statistics.
* Run the [**display counters**](cmdqueryname=display+counters) [ **bit** ] **rate** [ **inbound** | **outbound** ] [ **interface** *interface-type* [ *interface-number* | [**slot**](cmdqueryname=slot) *slot-id* ] ] command to check the interface traffic rates.
* Run the [**display port split**](cmdqueryname=display+port+split) or [**display port split slot**](cmdqueryname=display+port+split+slot) command to check the splitting capability and status of the interface.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  This command is supported only on the NE40E-M2K and NE40E-M2K-B.
* Run the [**display interface neighbor**](cmdqueryname=display+interface+neighbor) [ *interface-type* *interface-number* | **slot** *slot-id* [ **card** *card-number* ] ] command to check information about the neighboring devices and interfaces of a physical interface on the device.
* Run the [**display interface description**](cmdqueryname=display+interface+description) [ *interface-type* [ *interface-number* ] | **slot** *slot-id* [ **card** *card-number* ] ][ **full-name** ] command to check the interface description.