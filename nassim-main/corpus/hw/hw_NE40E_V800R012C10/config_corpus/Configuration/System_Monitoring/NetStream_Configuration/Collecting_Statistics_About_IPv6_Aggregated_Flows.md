Collecting Statistics About IPv6 Aggregated Flows
=================================================

Before collecting statistics about IPv6 aggregated flows, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172372978__fig_dc_vrp_ns_cfg_000301), a carrier enables NetStream on the Router to obtain detailed network application information. The carrier can use the information to monitor abnormal network traffic, analyze users' operation modes, and plan networks between ASs.

Statistics about NetStream aggregated flows contain information about original flows with the same attributes, whereas statistics about NetStream original flows contain information about sampled packets. The volume of aggregated flow statistics collection is greater than that of original flow statistics.

**Figure 1** Networking diagram for collecting IPv6 flow statistics
  
![](images/fig_dc_vrp_ns_cfg_000301.png)  



#### Pre-configuration Tasks

Before collecting the statistics about IPv6 aggregated flows, complete the following tasks:

* Configure parameters of the link layer protocol and IP addresses for interfaces so that the link layer protocol on the interfaces can go Up.
* Configure static routes or enable an IGP to implement network connectivity.
* Enable statistics collection for NetStream original flows.


[Specifying a NetStream Service Processing Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0047.html)

After sampling packets, each NetStream-enabled interface board sends sampled packets to the NetStream service processing board for aggregation and output. If the NE40E has more than one NetStream service processing board, these NetStream services boards work in redundancy mode to back up each other and balance traffic, which improves system reliability.

[Configuring an Aggregation Mode for IPv6 Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2009.html)

Configuring an aggregation mode is to specify an attribute type for original flows to be aggregated. An aggregation mode must be specified before original flows with the same attributes are aggregated as one flow and output to the NetStream Collector (NSC).

[Outputting Aggregation Flow Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2010.html)

To ensure that aggregation flow packets are correctly output to the NMS, configure the aging time, source address, and destination address for aggregated flows.

[(Optional) Adjusting the AS Field Mode and Interface Index Type](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2019.html)

For the NetStream Collector (NSC) to properly receive and parse NetStream packets output by the NetStream Data Exporter (NDE), ensure that the AS field modes and interface index types configured on the NDE and the NSC are the same.

[(Optional) Configuring NetStream Interface Option Packets and Setting Option Template Refreshing Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_3027_1.html)

This section describes how to configure NetStream interface option packets and set option template refreshing parameters.

[Sampling IPv6 Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0048.html)

You can enable NetStream to sample and analyze the incoming or outgoing flows on an interface as required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2012.html)

In routine maintenance or after NetStream configurations are complete, you can run the display commands in any view to check whether NetStream is enabled on the device.