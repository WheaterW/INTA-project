Configure an Alarm Threshold for the Number of Available VTY Channels
=====================================================================

By configuring an alarm threshold for the number available VTY channels, you can know information about available VTY channels on a device in a timely manner.

#### Context

When the number of available VTY channels on a device is less than or equal to the threshold, the device reports an alarm.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**user-interface vty available-vty-threshold**](cmdqueryname=user-interface+vty+available-vty-threshold) *threshold-value* command to configure an alarm threshold for the number of available VTY channels.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the configured alarm threshold is greater than the maximum number of VTY users, the system displays a message indicating that the configuration is invalid.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.