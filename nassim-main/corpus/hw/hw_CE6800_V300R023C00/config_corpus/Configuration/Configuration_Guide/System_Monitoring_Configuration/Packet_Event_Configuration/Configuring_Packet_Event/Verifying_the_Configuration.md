Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* When packet loss occurs on a device, run the [**display drop-event flow-cache [ ipv4 | ipv6 | vxlan | ethernet ]**](cmdqueryname=display+drop-event+flow-cache+%5B+ipv4+%7C+ipv6+%7C+vxlan+%7C+ethernet+%5D) **slot** *slot-id* command to check the packet loss visualization flow table.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The **ethernet** parameter is not supported by the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
* Run the [**display drop-event flow-cache statistics**](cmdqueryname=display+drop-event+flow-cache+statistics) **slot** *slot-id* command to check statistics about the packet loss visualization flow table.
* When the packet latency exceeds the threshold on a device, run the [**display latency-event flow-cache [ ipv4 | ipv6 | vxlan | ethernet ]**](cmdqueryname=display+latency-event+flow-cache+%5B+ipv4+%7C+ipv6+%7C+vxlan+%7C+ethernet+%5D) **slot** *slot-id* command to check the latency visualization flow table.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The **ethernet** parameter is not supported by the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.
* Run the [**display latency-event flow-cache statistics**](cmdqueryname=display+latency-event+flow-cache+statistics) **slot** *slot-id* command to check statistics about the latency visualization flow table.