Configuring the RMON Alarm Function
===================================

After the RMON alarm function is configured on a device, the device will generate a log or an alarm if the sampling value exceeds the alarm threshold.

#### Context

The RMON alarm function is implemented based on the event table and alarm table.

* Event table (corresponding to the event group in RMON MIB): When an event occurs, the system generates a log or sends a trap message to the NMS.
* Alarm table (corresponding to the alarm group in RMON MIB): A specified alarm variable identified by its OID is monitored at a specified sampling interval. A log or an alarm is generated when the monitored variable exceeds the defined threshold.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**rmon event**](cmdqueryname=rmon+event) **entry-number** [ **description** *string* ] { **log** | **trap** *object* | **log-trap** *object* | **none** } [ **owner** *owner-name* ]
   
   The event function is configured. The parameters in the command are described as follows:
   * **log**: The system only generates a log.
   * **log-trap**: The system generates a log and sends a trap message to the NMS.
   * **none**: The system does not take any action.
   * **trap**: The system only sends a trap message to the NMS.
3. Run [**rmon alarm**](cmdqueryname=rmon+alarm) *entry-number* *alarm-OID* *sampling-time* { **delta** | **absolute** | **changeratio** } **rising-threshold** *threshold-value1* *event-entry1* **falling-threshold** *threshold-value2* *event-entry2* [ **startup-alarm** { **falling** | **rising** | **risingorfalling** } ] [ **owner** *owner-name* ]
   
   
   
   The alarm threshold function is configured. If the events corresponding to the upper and lower alarm thresholds (*event-entry1* and *event-entry2*) are not configured, no alarm is generated even if the alarm conditions are satisfied. At this time, the alarm is in the Undercreation state rather than in the Valid state.
   
   If the event corresponding to either the upper or lower alarm threshold is configured, an alarm is triggered once the alarm conditions are satisfied. At this time, the alarm is in the Valid state. If an incorrect monitored object is configured, for example, a nonexistent OID is specified, the alarm is in the invalid state and no alarm is generated.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.