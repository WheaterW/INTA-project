Configuring Alarm Suppression
=============================

In normal cases, the system suppresses repeated alarms, flapping alarms, and intermittent alarms. You can disable alarm suppression of alarms that you are concerned about, hardware alarms, and ambient alarms.

#### Context

Alarm suppression has the following impacts on the system:

* When alarm suppression is enabled, alarm suppression takes effect, and you can configure an alarm suppression period.
* When alarm suppression is disabled, alarm suppression does not take effect in the system.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**delay-suppression enable**](cmdqueryname=delay-suppression+enable) command to enable the alarm suppression function.
   
   
   
   To disable the alarm suppression function, run the [**undo delay-suppression enable**](cmdqueryname=undo+delay-suppression+enable) command.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Do not leave alarm suppression disabled. Otherwise, a large number of redundant alarms will be generated.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.