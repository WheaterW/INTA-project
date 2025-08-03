Configuring Alarm Thresholds for CPU Usage
==========================================

Configuring Alarm Thresholds for CPU Usage

#### Context

The CPU is the core of a device. When the system is busy processing information, a large number of CPU resources are used. This causes system performance to deteriorate; for example, delaying data processing and increasing the packet loss rate. To avoid this issue, you can configure alarm thresholds for CPU usage, which, when exceeded, cause the device to generate an alarm. This helps you effectively monitor the CPU usage and optimize system performance, ensuring system stability.

Two types of alarm thresholds facilitate the CPU usage monitoring in real time: alarm triggering threshold for CPU usage and alarm clearing threshold for CPU usage. After an alarm triggering threshold for CPU usage is set, the system will generate an alarm if the threshold is exceeded. Similarly, after an alarm clearing threshold for CPU usage is set, the system clears the alarm after the CPU usage falls below the threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the alarm triggering threshold for CPU usage and alarm clearing threshold for CPU usage.
   
   
   ```
   [set cpu-usage threshold](cmdqueryname=set+cpu-usage+threshold) threshold-value [ restore restore-threshold-value ] [ interval interval-time ] [ slot slot-id [ cpu cpuid ] ]
   ```
   
   By default, the alarm triggering threshold for CPU usage is 90%, the alarm clearing threshold for CPU usage is 75%, and the overload detection period is 1 minute.
3. Configure a CPU rate decreasing threshold.
   
   
   ```
   [set configuration operation cpu-limit](cmdqueryname=set+configuration+operation+cpu-limit) { percent-value access-type snmp | ncf-percent-value access-type netconf }
   ```
   
   By default, no CPU rate decreasing threshold is configured.
   
   A large number of CPU resources are occupied when the NMS collects data. To ensure proper running of other services, some resources must be released. To resolve this issue, configure a CPU rate decreasing threshold. If the CPU usage reaches the configured threshold, the device reduces CPU resources allocated to the NMS when the NMS collects data.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display cpu-usage threshold**](cmdqueryname=display+cpu-usage+threshold) [ **slot** *slot-id* [ **cpu** *cpuid* ] ] command to check the CPU usage thresholds.
* Run the [**display cpu-usage monitor**](cmdqueryname=display+cpu-usage+monitor) { **all** | **slot** *slot-id* [ **cpu** *cpuid* ] } command to check the CPU usage.