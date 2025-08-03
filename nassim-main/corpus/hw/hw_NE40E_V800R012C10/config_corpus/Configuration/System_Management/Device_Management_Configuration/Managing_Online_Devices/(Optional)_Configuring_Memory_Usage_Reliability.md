(Optional) Configuring Memory Usage Reliability
===============================================

You can configure memory usage reliability based on service deployment on the device. In this way, when the memory usage of the device is too high, the device can detect the high memory usage in a timely manner and release memory to prevent unexpected board resets.

#### Context

When memory usage reliability is configured, the system takes actions based on the reliability thresholds when the memory usage is too high.

* When the memory usage of a board is higher than the notice threshold, the system notifies all components about the components whose memory usage is higher than 5% (for up to 10 components with the highest memory usage). When the memory usage of the board falls to 5% lower than the notice threshold, the system sends an alarm clearance message to all components.
* When the memory usage of a board is higher than the overload threshold, the system triggers the hwSystemMemoryOverload alarm and notifies all components about the components whose memory usage is higher than 5% (for up to 10 components with the highest memory usage). When the memory usage of the board falls to 5% lower than the overload threshold, the system triggers the hwSystemMemoryOverloadResume alarm and sends an alarm clearance message to all components.
* When the memory usage of a board is higher than the exception threshold, the system checks whether the process with the highest memory usage supports independent restart. If so, the system restarts the process. If not, the system does nothing. If the memory usage continues to increase, the board resets due to memory application failure.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**memory-usage reliability switch on**](cmdqueryname=memory-usage+reliability+switch+on)
   
   
   
   The memory usage reliability function is enabled.
3. Run [**memory-usage reliability notice-threshold**](cmdqueryname=memory-usage+reliability+notice-threshold) *notice-threshold-value* **overload-threshold** *overload-threshold-value* **exception-threshold** *exception-threshold-value* [ **slot** *slotId* ]
   
   
   
   The notice, overload, and exception thresholds are configured for memory usage reliability.

#### Follow-up Procedure

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the enabling status and thresholds of memory usage reliability.