(Optional) Disabling the Time Adjustment Function
=================================================

(Optional) Disabling the Time Adjustment Function

#### Context

After the IEEE 1588v2 protocol is configured, frequency synchronization and time synchronization are enabled. After the time synchronization function is enabled, the device time is adjusted, which affects the frequency synchronization. Disabling the time adjustment function can eliminate the impact on frequency synchronization. You can disable the time adjustment function as required.

![](public_sys-resources/note_3.0-en-us.png) 

This function disables time adjustment. After the function is executed, time synchronization cannot be performed.

You are advised to disable time synchronization only during maintenance fault locating.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the time adjustment function.
   
   
   ```
   [ptp time-adjustment disable](cmdqueryname=ptp+time-adjustment+disable)
   ```
   
   
   
   By default, the time adjustment function is disabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```