Configuring a Suppression Period for an Alarm
=============================================

You can configure a suppression period for an alarm to prevent the alarm from being reported frequently.

#### Context

Alarm reporting frequently affects fault locating efficiency. To prevent the system from reporting a large number of invalid alarms, you can enable delayed alarm reporting and configure a suppression period for an alarm, so that the alarm is not reported to the NMS within the period.

After a suppression period is configured for an alarm, the following situations occur:

* If the alarm is generated but its clear alarm is not generated, the alarm is reported to the NMS only after the suppression period elapses.
* If both the alarm and its clear alarm are generated during this period, they are both deleted from the alarm queue and will not be reported to the NMS.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**suppression alarm-name**](cmdqueryname=suppression+alarm-name) *alarm-name* { **cause-period** *cause-seconds* | **clear-period** *clear-seconds* } command to set the alarm suppression period.
   
   
   
   **cause-period** *cause-seconds* specifies the period after which a generated alarm is reported.
   
   **clear-period** *clear-seconds* specifies the period after which a generated clear alarm is reported.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.