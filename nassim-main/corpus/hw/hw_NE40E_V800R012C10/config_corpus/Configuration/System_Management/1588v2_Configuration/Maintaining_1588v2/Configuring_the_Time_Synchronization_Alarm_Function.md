Configuring the Time Synchronization Alarm Function
===================================================

The time synchronization alarm function can be configured to help monitor the time synchronization status. When a time synchronization alarm is generated, the alarm information will be reported to the NMS for further troubleshooting and maintenance.

#### Context

Perform the following steps on a device:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run any of the following commands:
   
   
   * To configure the alarm threshold for the clock class value of a PTP source, run the [**ptp alarm-threshold**](cmdqueryname=ptp+alarm-threshold) **clock-class** *clock-class-value* command.
   * To configure the alarm threshold for the absolute time offset of a PTP source, run the [**ptp alarm-threshold standard-time-offset**](cmdqueryname=ptp+alarm-threshold+standard-time-offset) *time-offset-value* command.
   * To configure the alarm threshold of the peak value of the accumulated time offsets of a PTP source, run the [**ptp alarm-threshold time-offset-sum**](cmdqueryname=ptp+alarm-threshold+time-offset-sum) *time-offset-sum* command.
   * To configure the alarm threshold for frequency offset at the physical layer, run the **[**clock alarm-threshold frequency-offset**](cmdqueryname=clock+alarm-threshold+frequency-offset)** **frequency-offset-value** command.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.