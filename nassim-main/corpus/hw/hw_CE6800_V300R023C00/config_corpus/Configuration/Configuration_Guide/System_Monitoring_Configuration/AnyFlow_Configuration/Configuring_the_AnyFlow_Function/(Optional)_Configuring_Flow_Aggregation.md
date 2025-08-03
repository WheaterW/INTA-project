(Optional) Configuring Flow Aggregation
=======================================

(Optional) Configuring Flow Aggregation

#### Context

After the AnyFlow function is enabled on a device, whereby the device exports original flow statistics by default. That is, the device sends statistics about each flow to the analyzer. The original flow statistics export occupies significant network bandwidth.

You can configure aggregation flow statistics export to reduce bandwidth consumption, whereby the chip built in the CPU aggregates original flows based on aggregation keywords and sends the aggregated flow statistics to the analyzer. You must set the service port number range to specify the flows to be aggregated. For example, you can aggregate HTTP service flows with the port number 80 and export the aggregated flow statistics.

![](public_sys-resources/note_3.0-en-us.png) 

If aggregated flow statistics export is configured, the device does not report original flow statistics. An appropriate service port number range must be set.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AnyFlow view.
   
   
   ```
   [any-flow](cmdqueryname=any-flow)
   ```
3. Specify the service port number for aggregating flows.
   
   
   ```
   [aggregation service-port](cmdqueryname=aggregation+service-port) { port-id1 [ to port-id2 ] }
   ```
4. Enable the flow aggregation function.
   
   
   ```
   [flow-aggregation enable](cmdqueryname=flow-aggregation+enable)
   ```
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```