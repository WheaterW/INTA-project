Enabling Latency Visualization
==============================

Enabling Latency Visualization

#### Context

After latency visualization is configured, when the packet latency exceeds the threshold on a device, the device reports related flow entries to the collector.

![](public_sys-resources/note_3.0-en-us.png) 

Only the following models support the latency visualization function: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, .



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable 1588v2 globally.
   
   
   ```
   [ptp enable](cmdqueryname=ptp+enable)
   ```
   
   By default, 1588v2 is not enabled globally.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   1588v2 needs to be enabled so that latency visualization can be configured.
3. Enter the packet monitoring view.
   
   
   ```
   [packet event monitor](cmdqueryname=packet+event+monitor)
   ```
4. (Optional) Enable the NVMe packet parsing function. (Only the following models support this function: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.)
   
   
   ```
   [nvme enable](cmdqueryname=nvme+enable)
   ```
5. Enable the latency visualization function.
   1. Enter the latency visualization view.
      
      
      ```
      [capture latency-event](cmdqueryname=capture+latency-event)
      ```
   2. Set the latency threshold.
      
      
      ```
      [latency threshold](cmdqueryname=latency+threshold) threshold-value
      ```
      
      When the latency of packets passing through a device exceeds the specified threshold, the device considers the packets to be high-latency packets, and creates latency visualization flow entries for those packets. The high-precision flow entry information includes the peak latency, number of packets, and inbound and outbound interfaces. By default, no latency threshold is configured for latency visualization.
   3. Exit the latency visualization view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
6. Exit the packet monitoring view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```