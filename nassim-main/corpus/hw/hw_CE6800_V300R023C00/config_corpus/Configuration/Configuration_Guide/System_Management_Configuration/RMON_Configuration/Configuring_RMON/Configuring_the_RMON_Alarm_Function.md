Configuring the RMON Alarm Function
===================================

Configuring the RMON Alarm Function

#### Context

After the RMON alarm function is configured on a device, the device will generate a log or an alarm if the sampling value exceeds the alarm threshold.

The RMON alarm function is implemented based on the event table and alarm table.

* Event table (corresponding to the event group in the RMON MIB): When an event occurs, the device generates a log or sends a trap message to the NMS.
* Alarm table (corresponding to the alarm group in the RMON MIB): A specified alarm variable identified by its OID is monitored at a specified sampling interval. When the monitored variable exceeds the defined threshold, the device generates a log or alarm.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the function of sending trap messages or recording logs for events.
   
   
   ```
   [rmon event](cmdqueryname=rmon+event) entry-number [ description string ] { log | trap object | log-trap object | none } [ owner owner-name ]
   ```
   
   
   The event function is configured. The parameters in the command are described as follows:
   * **log**: The system only generates a log.
   * **log-trap**: The system generates a log and sends a trap message to the NMS.
   * **none**: The system does not take any action.
   * **trap**: The system only sends a trap message to the NMS.
3. Configure the alarm threshold function.
   
   
   ```
   [rmon alarm](cmdqueryname=rmon+alarm) entry-number alarm-OID sampling-time { absolute | changeratio | delta } rising-threshold threshold-value1 event-entry1 falling-threshold threshold-value2 event-entry2 [ startup-alarm { falling | rising | risingorfalling } ] [ owner owner-name ]
   ```
   
   
   
   By default, the alarm threshold function is not configured.
   
   If the events corresponding to the upper and lower alarm thresholds (*event-entry1* and *event-entry2*) are not configured, no alarm is generated even if the alarm conditions are satisfied. In this case, the alarm is in the Undercreation state rather than in the Valid state.
   
   If the event corresponding to either the upper or lower alarm threshold is configured, an alarm is triggered once the alarm conditions are satisfied. In this case, the alarm is in the Valid state. If an incorrect monitored object is configured (for example, a nonexistent OID is specified), the alarm is in the Invalid state, and no alarm is generated.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```