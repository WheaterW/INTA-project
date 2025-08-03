(Optional) Configuring CPU Usage Alarm Thresholds and a Detection Period
========================================================================

You can configure the CPU usage alarm thresholds and a detection period based on service deployment on the device. Alarm thresholds include the level-1 alarm triggering threshold, level-1 alarm clearing threshold, level-2 alarm triggering threshold, and level-2 alarm clearing threshold.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set cpu-reliability**](cmdqueryname=set+cpu-reliability) **first-recover** *first-recover-value* **first-alarm** *first-alarm-value* **second-recover** *second-recover-value* **second-alarm** *second-alarm-value* **period** *period-value* [ **slot** *slotId* ]
   
   
   
   The detection period and the level-1 and level-2 alarm triggering and clearing thresholds for CPU usage are set.

#### Follow-up Procedure

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the detection period and the level-1 and level-2 alarm triggering and clearing thresholds for CPU usage.