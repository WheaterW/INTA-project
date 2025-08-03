Configuring a Threshold for CPU Usage
=====================================

You can configure a threshold for CPU usage to monitor the CPU usage.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**monitor cpu-usage**](cmdqueryname=monitor+cpu-usage) [ **interval** *intervalValue* ] [ **slot** *slotid* ]
   
   
   
   The CPU usage is dynamically monitored.
3. Run [**set cpu-usage threshold**](cmdqueryname=set+cpu-usage+threshold) *threshold* [ **restore** *restore-threshold-value* ] [ **interval** *interval-value* ] [ **slot** *slot-id* ]
   
   
   
   Alarm triggering and clearing thresholds for CPU usage are set.
4. Run [**set configuration operation cpu-limit**](cmdqueryname=set+configuration+operation+cpu-limit) { *percent-value* **access-type** **snmp** | *ncf-percent-value* **access-type** **netconf** }
   
   
   
   The CPU rate decreasing threshold is set.
   
   When the CPU usage reaches the configured threshold, the NMS-based data collection operation releases some CPU resources to other services.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In VS mode, this configuration process is supported only by the admin VS.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

* Run the [**display cpu-usage configuration**](cmdqueryname=display+cpu-usage+configuration) [ **slot** *slot-id* ] command to check the CPU usage statistics and CPU usage configuration.
* Run the [**display cpu-monitor information**](cmdqueryname=display+cpu-monitor+information) { **slot** *slot-id* | **all** } command to check the CPU overloading status of boards.
* Run the [**reset cpu-usage record**](cmdqueryname=reset+cpu-usage+record) [ **slot** *slotId* | **all** ] command to clear CPU usage statistics.