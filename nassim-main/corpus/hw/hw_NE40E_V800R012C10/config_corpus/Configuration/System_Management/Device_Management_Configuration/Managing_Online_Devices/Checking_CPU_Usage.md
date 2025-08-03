Checking CPU Usage
==================

During the routine maintenance of the device or when the device cannot run normally, you can check the CPU usage and the CPU usage configuration.

#### Procedure

* You can check the CPU usage or the CPU usage configuration in any of the following methods:
  
  
  + Run the [**display cpu-usage service**](cmdqueryname=display+cpu-usage+service) [ **slot** *slot-id* ] command to check the CPU usage based on service types.
  + Run the [**display cpu-usage history**](cmdqueryname=display+cpu-usage+history) [ **1hour** | **24hour** | **72hour** ] [ **slot** *slot-id* ] command to check CPU usage statistics within a period.
  + Run the [**display cpu-usage configuration**](cmdqueryname=display+cpu-usage+configuration) [ **slot** *slot-id* ] command to check the CPU usage configuration of a board.![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    You can run the [**set cpu-usage threshold**](cmdqueryname=set+cpu-usage+threshold) *threshold-value* [ **restore** *restore-threshold-value* ] [ **interval** *interval-value* ] [ **slot** *slot-id* ] command to set the thresholds for triggering and clearing CPU usage alarms of a main control board.