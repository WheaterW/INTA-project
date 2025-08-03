Configuring a Threshold for Memory Usage
========================================

You can configure a threshold for memory usage to monitor the memory usage.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set memory-usage threshold**](cmdqueryname=set+memory-usage+threshold) *threshold* [ **restore** *restore-threshold-value* ] [ **slot** *slot-id* ]
   
   
   
   Alarm triggering and clearing thresholds for memory usage are set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

* Run the [**display memory-usage threshold**](cmdqueryname=display+memory-usage+threshold) [ **slot** *slot-id* ] command to check the alarm triggering threshold for memory usage.
* Run the [**display memory-monitor information**](cmdqueryname=display+memory-monitor+information) [ **all** | **slot** *slot-id* ] command to check the memory overloading status of boards.