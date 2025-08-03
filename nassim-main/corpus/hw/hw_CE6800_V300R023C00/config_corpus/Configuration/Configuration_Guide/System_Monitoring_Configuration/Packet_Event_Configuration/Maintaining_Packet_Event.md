Maintaining Packet Event
========================

Maintaining Packet Event

#### Context

![](public_sys-resources/note_3.0-en-us.png) 

Only the following models support the latency visualization function: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, .



#### Clearing the Packet Loss Visualization Flow Table

During routine maintenance, you can clear the packet loss visualization flow table.

![](public_sys-resources/notice_3.0-en-us.png) 

The packet loss visualization flow table cleared using the [**reset drop-event flow-cache**](cmdqueryname=reset+drop-event+flow-cache) command cannot be restored. Exercise caution when you run this command.

* Run the [**reset drop-event flow-cache**](cmdqueryname=reset+drop-event+flow-cache) [ **slot** *slot-id* ] command in the user view to clear the packet loss visualization flow table on the device and send all the flow entries to the collector.

#### Clearing the Latency Visualization Flow Table

During routine maintenance, you can clear the latency visualization flow table.

![](public_sys-resources/notice_3.0-en-us.png) 

The latency visualization flow table cleared using the [**reset latency-event flow-cache**](cmdqueryname=reset+latency-event+flow-cache) command cannot be restored. Exercise caution when you run this command.

* Run the [**reset latency-event flow-cache**](cmdqueryname=reset+latency-event+flow-cache) [ **slot** *slot-id* ] command in the user view to clear the latency visualization flow table on the device and send all the flow entries to the collector.