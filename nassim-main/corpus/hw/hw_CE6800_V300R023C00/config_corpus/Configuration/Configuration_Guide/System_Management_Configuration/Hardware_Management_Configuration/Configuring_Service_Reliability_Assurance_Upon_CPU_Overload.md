Configuring Service Reliability Assurance Upon CPU Overload
===========================================================

Configuring Service Reliability Assurance Upon CPU Overload

#### Context

In most cases, the system generates an alarm when a board's CPU usage exceeds the preset alarm threshold. If no effective measures are taken and the CPU is continuously overloaded, services will be adversely affected. To improve service reliability when CPU overload occurs, you can set level-1 and level-2 alarm thresholds for CPU overload on a device, where the level-2 alarm threshold is greater than the level-1 alarm threshold. When the CPU usage of the device reaches either of the two thresholds, the system notifies all components of information about up to 10 components that occupy more than 5% of CPU resources on the device. The notified components then execute their own service reliability assurance mechanisms based on the CPU overload severity to ensure proper service operations.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the level-1 alarm threshold, level-2 alarm threshold, and detection period for CPU overload.
   
   
   ```
   [set cpu-reliability](cmdqueryname=set+cpu-reliability) first-recover first-recover-value first-alarm first-alarm-value second-recover second-recover-value second-alarm second-alarm-value period period-value slot slot-id
   ```
   
   By default, the level-1 alarm threshold, level-1 clear alarm threshold, level-2 alarm threshold, level-2 clear alarm threshold, and detection period for CPU overload are 60, 50, 80, 70, and 60, respectively.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the level-1 and level-2 alarm thresholds for CPU overload.