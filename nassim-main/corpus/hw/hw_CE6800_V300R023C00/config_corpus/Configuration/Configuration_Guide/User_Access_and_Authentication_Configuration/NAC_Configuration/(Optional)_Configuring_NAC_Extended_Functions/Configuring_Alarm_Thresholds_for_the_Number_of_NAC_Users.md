Configuring Alarm Thresholds for the Number of NAC Users
========================================================

Configuring Alarm Thresholds for the Number of NAC Users

#### Context

You can configure the alarm threshold for the number of NAC users on the device. When the configured alarm threshold is reached, the device generates an alarm.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the alarm threshold for the number of NAC users on the device.
   
   
   ```
   [authentication user-alarm percentage](cmdqueryname=authentication+user-alarm+percentage) percent-lower-value percent-upper-value
   ```
   
   By default, the lower and upper alarm thresholds for the number of NAC users on the device are 50% and 100% respectively.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display authentication user-alarm configuration**](cmdqueryname=display+authentication+user-alarm+configuration) command to check the alarm thresholds for the number of NAC users, in percentage.