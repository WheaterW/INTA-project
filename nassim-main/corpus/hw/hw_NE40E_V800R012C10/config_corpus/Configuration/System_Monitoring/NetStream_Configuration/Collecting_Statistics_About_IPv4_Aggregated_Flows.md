Collecting Statistics About IPv4 Aggregated Flows
=================================================

Before collecting statistics about IPv4 aggregated flows, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172372955__fig_dc_vrp_ns_cfg_000301), a carrier enables NetStream on the Router functioning as a NetStream Data Exporter (NDE) to obtain detailed network application information. The carrier can use the information to monitor abnormal network traffic, analyze users' operation modes, and plan networks between ASs.

Statistics about NetStream aggregated flows contain information about original flows with the same attributes, whereas statistics about NetStream original flows contain information about sampled packets. The volume of aggregated flow statistics is greater than that of original flow statistics.

**Figure 1** Networking diagram for collecting IPv4 flow statistics  
![](images/fig_dc_vrp_ns_cfg_000301.png)  


#### Pre-configuration Tasks

Before collecting statistics about IPv4 aggregated flows, complete the following tasks:

* Configure static routes or enable an IGP to implement network connectivity.
* Enable statistics collection for NetStream original flows.


[Specifying a NetStream Service Processing Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0044.html)

After sampling packets, each NetStream-enabled interface board sends sampled packets to the NetStream service processing board for aggregation and output. If the NE40E has more than one NetStream service processing board, these NetStream services boards work in redundancy mode to back up each other and balance traffic, which improves system reliability.

[Configuring an Aggregation Mode for IPv4 Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0011.html)

Configuring an aggregation mode is to specify an attribute type for original flows to be aggregated. An aggregation mode must be specified before original flows with the same attributes are aggregated as one flow and output to the NetStream Collector (NSC).

[Outputting Aggregation Flow Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0012.html)

To ensure that aggregation flow packets are correctly output to the NMS, specify the aging time, output format, and source and destination addresses for aggregation flows.

[(Optional) Adjusting the AS Field Mode and Interface Index Type](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0045.html)

For the NetStream Collector (NSC) to properly receive and parse NetStream packets output by the NetStream Data Exporter (NDE), ensure that the AS field modes and interface index types configured on the NDE and the NSC are the same.

[(Optional) Configuring NetStream Option Packets and Setting Option Template Refreshing Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_3026_1.html)

This section describes how to configure NetStream option packets and set option template refreshing parameters.

[Sampling IPv4 Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0046.html)

You can enable NetStream to sample and analyze the incoming or outgoing flows on an interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0014.html)

In routine maintenance or after pertaining configurations of NetStream are complete, you can run the display commands in any view to check whether NetStream is enabled on the device.