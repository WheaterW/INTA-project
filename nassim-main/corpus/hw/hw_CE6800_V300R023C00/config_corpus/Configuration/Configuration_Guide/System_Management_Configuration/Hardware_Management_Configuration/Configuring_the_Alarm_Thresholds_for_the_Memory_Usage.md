Configuring the Alarm Thresholds for the Memory Usage
=====================================================

Configuring the Alarm Thresholds for the Memory Usage

#### Context

The memory usage is an important metric that is used to measure device performance. A high memory usage may cause service faults. To avoid the occurrence of such faults, you can configure alarm thresholds for the memory usage, which, when exceeded, cause the device to generate an alarm. In this way, you can effectively monitor the memory usage and optimize system performance, ensuring system stability.

Two types of alarm thresholds are available: alarm threshold and alarm clearance threshold. After an alarm threshold is set for the memory usage, the system will generate an alarm if the threshold is exceeded. Similarly, after an alarm clearance threshold is set for the memory usage, the system clears the alarm after it falls below the threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the memory usage alarm threshold and alarm clearance threshold.
   
   
   ```
   [set memory threshold](cmdqueryname=set+memory+threshold) threshold-value [ restore restore-threshold-value ] [ slot slot-id [ cpu cpu-id ] ]
   ```
   
   By default:
   
   * For a device whose total physical memory is greater than 4 GB, the memory usage alarm threshold is 95% and the alarm clearance threshold is 75%.
   * For a device whose total physical memory is less than or equal to 4 GB, the memory usage alarm threshold is 92% and the alarm clearance threshold is 75%.
   
   To check the total physical memory size, run the [**display memory**](cmdqueryname=display+memory) command and check the **Total Physical Available Memory** field in the command output.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display memory**](cmdqueryname=display+memory) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to check the memory usage statistics.
* Run the [**display memory threshold**](cmdqueryname=display+memory+threshold) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to check the memory usage alarm threshold and memory usage alarm clearance threshold.