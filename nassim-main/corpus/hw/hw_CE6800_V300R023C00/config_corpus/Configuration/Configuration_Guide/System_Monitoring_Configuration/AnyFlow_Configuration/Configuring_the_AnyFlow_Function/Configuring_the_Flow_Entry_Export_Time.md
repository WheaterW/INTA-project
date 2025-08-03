Configuring the Flow Entry Export Time
======================================

Configuring the Flow Entry Export Time

#### Context

A device has two flow tables: the hardware flow table and the flow table created on the chip built in the CPU. When original traffic enters the device, it first creates related hardware flow entries, exports them to the chip built in the CPU, and then exports the flow entries created on the CPU's chip to the analyzer. If flow aggregation is configured, the chip built in the CPU aggregates original flows and sends aggregated flow statistics to the analyzer.

Flow entries can be exported in either of the following modes:

1. Export upon flow aging: If the aging time of a flow expires, the flow is aged out and the corresponding flow entry is exported.
2. Scheduled export: Flow entries are exported at a scheduled time. This mode ensures that entries of the flows that are not aged out can be quickly exported.

#### Procedure

1. Configure the time for exporting hardware flow entries.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the AnyFlow view.
      
      
      ```
      [any-flow](cmdqueryname=any-flow) 
      ```
   3. Configure the aging time for hardware flow entries.
      
      
      ```
      [hardware aging-time](cmdqueryname=hardware+aging-time) time-value
      ```
   4. Configure the interval for exporting hardware flow entries.
      
      
      ```
      [hardware export interval](cmdqueryname=hardware+export+interval) interval-time
      ```
   5. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Configure the time for exporting flow entries on the chip built in the CPU.
   * Original flow entry export
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Enter the AnyFlow view.
        ```
        [any-flow](cmdqueryname=any-flow)
        ```
     3. Configure the aging time for flow entries on the chip built in the CPU.
        ```
        [aging-time](cmdqueryname=aging-time) time-value
        ```
     4. Configure the interval for exporting flow entries on the chip built in the CPU.
        ```
        [export interval](cmdqueryname=export+interval) interval-time
        ```
     5. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     6. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```
   * Aggregated flow entry export
     1. Enter the system view.
        ```
        [system-view](cmdqueryname=system-view)
        ```
     2. Enter the AnyFlow view.
        ```
        [any-flow](cmdqueryname=any-flow)
        ```
     3. Configure the aging time for aggregated flow entries.
        ```
        [flow-aggregation aging-time](cmdqueryname=flow-aggregation+aging-time) time-value
        ```
     4. Configure the interval for exporting aggregated flow entries.
        ```
        [flow-aggregation export interval](cmdqueryname=flow-aggregation+export+interval) interval-time
        ```
     5. Return to the system view.
        ```
        [quit](cmdqueryname=quit)
        ```
     6. Commit the configuration.
        ```
        [commit](cmdqueryname=commit)
        ```