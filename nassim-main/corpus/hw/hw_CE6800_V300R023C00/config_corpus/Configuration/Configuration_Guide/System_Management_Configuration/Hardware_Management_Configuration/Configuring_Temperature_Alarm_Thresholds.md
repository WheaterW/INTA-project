Configuring Temperature Alarm Thresholds
========================================

Configuring Temperature Alarm Thresholds

#### Context

You can manually adjust the temperature alarm thresholds of a device to adapt to the change of the device's environment. When the temperature of the device reaches a configured alarm threshold, a corresponding alarm is generated, prompting maintenance personnel to adjust the environment variables of the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure temperature alarm thresholds.
   
   
   ```
   [device temperature threshold slot](cmdqueryname=device+temperature+threshold+slot) slot-id sensor sensor-id minor minor-value major major-value fatal fatal-value [ tmin tmin-value tmax tmax-value ]
   ```
   
   By default, the temperature alarm thresholds of a board vary according to the hardware used by the device.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display device temperature**](cmdqueryname=display+device+temperature) [ **slot** *slot-id* ] command. The **Minor**, **Major**, and **Fatal** fields in the command output indicate the upper thresholds for minor, major, and critical alarms, respectively.