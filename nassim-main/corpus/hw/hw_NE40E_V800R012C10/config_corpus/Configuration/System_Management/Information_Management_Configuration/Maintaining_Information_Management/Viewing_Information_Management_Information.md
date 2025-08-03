Viewing Information Management Information
==========================================

This section describes how to view information management information to quickly understand device running status.

#### Context

In routine maintenance, you can run the following commands in any view to display desired device information.


#### Procedure

* Run the [**display logbuffer**](cmdqueryname=display+logbuffer) [ **security** ] [ **slot** *slot-id* | **module** *module-name* | **starttime** *starttime-value* [ **endtime** *endtime-value* ] | **level** { *severity* | { **emergencies** | **alert** | **critical** | **error** | **warning** | **notification** | **informational** | **debugging** } } | **size** *value* ] \* command in any view to display log information.
* Run the [**display logfile**](cmdqueryname=display+logfile) *path* [ *offset* ] command in any view to display the information file.
* Run the [**display trapbuffer**](cmdqueryname=display+trapbuffer) [ **size** *buffersize* ] command in any view to display trap buffer information.
* Run the [**display event information**](cmdqueryname=display+event+information) [ **name** *event-name* ] command in any view to display registration information about the specified event or all events in the system.
* Run the [**display info-center**](cmdqueryname=display+info-center) [ **statistics** ] command in any view to display information recorded by the information management module.
* Run the [**display logfile**](cmdqueryname=display+logfile) [ **log** | **diagnose** ] **list** **starttime** *starttime-value* **endtime** *endtime-value* [ **slave** ] command in any view to display log files generated in the specified time range.
  
  
  
  The parameter **diagnose** is supported only on the Admin-VS.