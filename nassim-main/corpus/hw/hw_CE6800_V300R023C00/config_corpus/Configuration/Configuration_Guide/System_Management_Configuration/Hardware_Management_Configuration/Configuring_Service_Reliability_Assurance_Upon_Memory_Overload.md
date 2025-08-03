Configuring Service Reliability Assurance Upon Memory Overload
==============================================================

Configuring Service Reliability Assurance Upon Memory Overload

#### Context

In most cases, the system generates an alarm when a board's memory usage exceeds the preset alarm threshold. If no effective measures are taken and the memory is continuously overloaded, services will be adversely affected. To improve service reliability when memory overload occurs, you can set alarm thresholds for memory overload on a device. The alarm thresholds are classified into a notice threshold, an overload threshold, and an exception threshold in an ascending order of memory overload severity. When the memory usage reaches a threshold, the system notifies all components of information about up to 10 components that occupy more than 5% of memory resources. After receiving the notification, the components execute their own reliability assurance mechanisms based on the overload severity in the notification.

![](public_sys-resources/note_3.0-en-us.png) 

Only the CE8851-32CQ8DQ-P, CE8851-32CQ8DQ-K, CE8850-HAM, CE8850-SAN, CE6866-48S8CQ-P, CE6866-48S8CQ-K, CE6860-HAM, and CE6860-SAN support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable service reliability assurance upon memory overload.
   
   
   ```
   [memory-usage reliability switch on](cmdqueryname=memory-usage+reliability+switch+on)
   ```
   
   By default, service reliability assurance upon memory overload is disabled.
3. Set the notice threshold, overload threshold, exception threshold, and recovery threshold of memory overload.
   
   
   ```
   [memory-usage reliability notice-threshold](cmdqueryname=memory-usage+reliability+notice-threshold) notice-threshold-value overload-threshold overload-threshold-value exception-threshold exception-threshold-value [ slot slotId ]
   ```
   
   The default notice, overload, and exception thresholds for memory usage reliability are 70, 85, and 95, respectively.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check memory usage thresholds and whether service reliability assurance upon memory overload is enabled.