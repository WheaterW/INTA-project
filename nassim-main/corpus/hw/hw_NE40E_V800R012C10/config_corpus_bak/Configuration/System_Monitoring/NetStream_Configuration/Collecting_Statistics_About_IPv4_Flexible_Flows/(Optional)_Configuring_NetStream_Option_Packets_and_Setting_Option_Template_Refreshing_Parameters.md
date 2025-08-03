(Optional) Configuring NetStream Option Packets and Setting Option Template Refreshing Parameters
=================================================================================================

This section describes how to configure NetStream option packets and set option template refreshing parameters.

#### Context

Regardless of the flow format in which traffic statistics are output, option packet data is output to the NetStream Collector (NSC) as supplementary information for traffic statistics. This allows the NSC to obtain information such as the sampling ratio and sampling enabling status of the NetStream Data Exporter (NDE), so that the actual network traffic can be reflected.

At present, the following four types of option packets are supported on IPv4 networks:

* Interface option packets: These packets are used to send the NetStream configurations of all the boards on the NDE to the NSC in a scheduled manner. The configurations cover the interface index, statistics collection direction, and sampling value in the inbound/outbound direction.
* Time application label (TAL) option packets: These packets are used to send application label data to the NSC. The application label option function provides data, such as the application type of system labels, for users to collect L3VPN NetStream statistics. For details, see [Collecting Statistics About BGP/MPLS VPN Flows](dc_vrp_ns_cfg_0042.html).
* VPN information option packets: These packets are used to periodically send VPN information (including the VPN name and index) on the NDE to the NSC.
* Interface information option packets: These packets are used to periodically send interface information (including the interface name and index) on the NDE to the NSC.

Option packets, which are independent of statistics packets, are output to the NSC in the V9 or IPFIX format. As such, the corresponding option template is sent to the NMS for parsing option packets. You can set option template refreshing parameters as needed for the device to regularly refresh the template in order to notify the NSC of the latest option template format.


#### Procedure

* Run [**system-view**](cmdqueryname=system-view)
  
  
  
  The system view is displayed
* Run the following commands as required to configure functions related to interface option packets.
  
  
  + Run the [**ip netstream export template option sampler**](cmdqueryname=ip+netstream+export+template+option+sampler) command to enable the function of exporting statistics about interface option packets.
  + Run the [**ip netstream export template option**](cmdqueryname=ip+netstream+export+template+option) { **refresh-rate** *packet-number* | **timeout-rate** *timeout-interval* } command to set the packet sending interval and timeout interval for option template refreshing.The packet sending interval and timeout interval are set for option template refreshing. An option template can be refreshed at a fixed packet sending interval or timeout interval. The two intervals can both take effect. In the command:
    - **refresh-rate** *packet-interval* indicates that the option template is refreshed at a fixed packet sending interval.
    - **timeout-rate** *timeout-interval* indicates that the option template is refreshed at a fixed timeout interval.
  + Run the [**ip netstream export option sampler timeout-rate**](cmdqueryname=ip+netstream+export+option+sampler+timeout-rate) *tmval* command to set the interval for refreshing option packets.
* Run the following commands as required to configure functions related to VPN information option packets.
  + Run the [**ip netstream export template option**](cmdqueryname=ip+netstream+export+template+option) **vpn-information** command to enable the function of sending VPN option template packets.
  + Run the [**ip netstream export option**](cmdqueryname=ip+netstream+export+option) **vpn-information** { **all-vpn-instance** | **vpn-instance** *vpn-name* | **timeout-rate** *tmval* } command to enable the function of sending VPN instance information and set the interval for refreshing VPN option packets.
* Run the following commands as required to configure functions related to interface information option packets.
  + Run the [**ip netstream export template option**](cmdqueryname=ip+netstream+export+template+option) **interface-information** command to enable the function of sending interface option template packets.
  + Run the [**ip netstream export option**](cmdqueryname=ip+netstream+export+option) **interface-information** { **all-interface** | **interface** *interface-name* | **timeout-rate** *tmval* } command to enable the function of sending interface information and set the interval for refreshing interface option packets.