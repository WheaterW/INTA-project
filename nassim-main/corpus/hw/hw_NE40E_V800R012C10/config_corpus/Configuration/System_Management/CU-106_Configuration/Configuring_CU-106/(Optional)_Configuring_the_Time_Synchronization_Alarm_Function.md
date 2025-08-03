(Optional) Configuring the Time Synchronization Alarm Function
==============================================================

The time synchronization alarm function can be configured to help monitor the time synchronization status. When a time synchronization alarm is generated, the alarm information will be reported to the NMS for further troubleshooting and maintenance.

#### Context

Perform the following steps on the T-BC:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the time synchronization alarm function as required.
   
   
   * Run the [**ptp alarm-threshold**](cmdqueryname=ptp+alarm-threshold) **clock-class** *clock-class-value* command to configure the alarm threshold for PTP source input deterioration.
   * Run the [**ptp alarm-threshold standard-time-offset**](cmdqueryname=ptp+alarm-threshold+standard-time-offset) *time-offset-value* command to configure the alarm threshold for the PTP source absolute time reference.
   * Run the [**ptp alarm-threshold time-offset-sum**](cmdqueryname=ptp+alarm-threshold+time-offset-sum) *time-offset-sum* command to configure the alarm threshold for the peak value of the accumulated PTP source time offsets.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.