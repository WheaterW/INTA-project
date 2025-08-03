(Optional) Configuring NetStream Interface Option Packets and Setting Option Template Refreshing Parameters
===========================================================================================================

This section describes how to configure NetStream interface option packets and set option template refreshing parameters.

#### Context

Regardless of the flow format in which the traffic statistics are output, option packet data is exported to the NetStream Collector (NSC) as a supplement. In this way, the NetStream Data Exporter (NDE) can obtain information, such as the sampling ratio and whether the sampling function is enabled, to reflect the actual network traffic.

Currently, the option packets supported by IPv6 networks are interface option packets, which are used to send the NetStream configurations of all the boards on the NDE to the NSC in a scheduled manner. The configurations cover the interface index, statistics collection direction, and sampling value in the inbound/outbound direction.

Option packets, which are independent of statistics packets, are exported to the NSC in V9 or IPFIX format. Therefore, the corresponding option template is sent to the NMS for parsing option packets. You can set option template refreshing parameters as needed for the device to regularly refresh the template in order to notify the NSC of the latest option template format.


#### Procedure

* Run [**system-view**](cmdqueryname=system-view)
  
  
  
  The system view is displayed.
* Run the following commands as required to configure functions related to interface option packets.
  
  
  + Run the [**ipv6 netstream export template option sampler**](cmdqueryname=ipv6+netstream+export+template+option+sampler) command to enable the function of exporting statistics about interface option packets.
  + Run the [**ipv6 netstream export template option**](cmdqueryname=ipv6+netstream+export+template+option) { **refresh-rate** *packet-number* | **timeout-rate** *timeout-interval* } command to set the packet sending interval and timeout interval for option template refreshing.The packet sending interval and timeout interval are set for option template refreshing. An option template can be refreshed at a fixed packet sending interval or timeout interval. The two intervals can both take effect. In the command:
    - **refresh-rate** *packet-interval* indicates that the option template is refreshed at a fixed packet sending interval.
    - **timeout-rate** *timeout-interval* indicates that the option template is refreshed at a fixed timeout interval.
  + Run the [**ipv6 netstream export option sampler timeout-rate**](cmdqueryname=ipv6+netstream+export+option+sampler+timeout-rate) *tmval* command to set the interval for refreshing option packets.