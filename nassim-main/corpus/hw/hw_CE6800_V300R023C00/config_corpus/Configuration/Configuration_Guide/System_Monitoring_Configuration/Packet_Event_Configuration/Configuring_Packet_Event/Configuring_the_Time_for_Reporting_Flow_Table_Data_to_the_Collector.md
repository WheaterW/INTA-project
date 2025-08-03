Configuring the Time for Reporting Flow Table Data to the Collector
===================================================================

Configuring the Time for Reporting Flow Table Data to the Collector

#### Context

Packet loss visualization and latency visualization flow entries can be reported to the collector in either of the following modes:

* Reporting at a specified interval: All packet loss visualization and latency visualization flow entries on the device are periodically reported to the collector. This mode ensures that statistics about the flows that are not aged out can be quickly reported to the collector.
* Reporting by aging time: When the inactive time of a flow (the time elapsed since the last packet of the flow was received) exceeds the configured flow aging time, the device ages out the flow and sends it to the collector. This mode can be used to clear unnecessary entries so as not to waste entry resources. Inactive aging is suitable for the flows that span a relatively short period of time. The device exports flow statistics as soon as the flow stops, thereby saving memory.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the packet monitoring view.
   
   
   ```
   [packet event monitor](cmdqueryname=packet+event+monitor)
   ```
3. (Optional) Set the interval for reporting packet loss visualization and latency visualization flow entries to the collector.
   
   
   ```
   [export interval](cmdqueryname=export+interval) time-value
   ```
   
   By default, the interval for reporting packet loss visualization and latency visualization flow entries to the collector is 10 seconds.
4. (Optional) Configure the aging time as required.
   
   
   * (Optional) Configure the aging time for packet loss visualization flow entries.
     1. Enter the packet loss visualization view.
        ```
        [capture drop-event](cmdqueryname=capture+drop-event)
        ```
     2. Configure the aging time for packet loss visualization flow entries.
        ```
        [aging-time](cmdqueryname=aging-time) time-value
        ```
        
        By default, the aging time for packet loss flow entries is 30 seconds.
     3. Exit the packet loss visualization view.
        ```
        [quit](cmdqueryname=quit)
        ```
   * (Optional) Configure the aging time for latency visualization flow entries.
     1. Enter the latency visualization view.
        ```
        [packet event monitor](cmdqueryname=packet+event+monitor)
        ```
     2. Configure the aging time for latency visualization flow entries.
        ```
        [aging-time](cmdqueryname=aging-time) time-value
        ```
        
        By default, the aging time for latency visualization flow entries is 30 seconds.
     3. Exit the latency visualization view.
        ```
        [quit](cmdqueryname=quit)
        ```
5. Exit the packet monitoring view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```