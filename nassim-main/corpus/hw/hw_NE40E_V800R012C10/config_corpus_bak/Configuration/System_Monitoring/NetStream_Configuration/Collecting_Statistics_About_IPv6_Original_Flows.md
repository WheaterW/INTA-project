Collecting Statistics About IPv6 Original Flows
===============================================

Before collecting statistics about IPv6 original flows, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172372966__fig_dc_vrp_ns_cfg_000301), a carrier enables NetStream on the Router to obtain detailed network application information. The carrier can use the information to monitor abnormal network traffic, analyze users' operation modes, and plan networks between ASs.

Statistics about original flows are collected based on the 7-tuple information. The NetStream data exporter (NDE) samples IPv6 flows passing through it, encapsulates information about the post-aging NetStream original flows into UDP packets, and sends the packets to the NetStream Collector (NSC) for further processing. Unlike collecting statistics about aggregated flows, collecting statistics about original flows imposes less impact on NDE performance. Original flows consume more storage space and network bandwidth resources of the NSC because the volume of original flows is greater than that of aggregated flows.

**Figure 1** Networking diagram for collecting IPv6 flow statistics
  
![](images/fig_dc_vrp_ns_cfg_000301.png)  



#### Pre-configuration Tasks

Before collecting the statistics about IPv6 original flows, complete the following task:

* Configure parameters of the link layer protocol and IP addresses for interfaces so that the link layer protocol on the interfaces can go Up.
* Configure static routes or enable an IGP to implement network connectivity.


[Specifying a NetStream Service Processing Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0043.html)

After sampling packets, each NetStream-enabled interface board sends sampled packets to the NetStream service processing board for aggregation and output. If the NE40E has more than one NetStream service processing board, these NetStream services boards work in redundancy mode to back up each other and balance traffic, which improves system reliability.

[Outputting Original Flow Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2005.html)

To ensure that original flow packets can be correctly output to the NMS, configure the aging time, output format, and source and destination addresses for original flows.

[(Optional) Configuring NetStream Monitoring Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0050.html)

NetStream monitoring services can be configured on the NetStream Data Exporter (NDE), enabling carriers to implement more delicate traffic statistics collection and management over IPv6 original flows.

[(Optional) Adjusting the AS Field Mode and Interface Index Type](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2018.html)

For the NetStream Collector (NSC) to properly receive and parse NetStream packets output by the NetStream Data Exporter (NDE), ensure that the AS field modes and interface index types configured on the NDE and the NSC are the same.

[(Optional) Enabling Statistics Collection of TCP Flags in Original Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2004.html)

There are six flag bits (URG, ACK, PSH, RST, SYN, and FIN) in a TCP packet header. The flag bits, together with the destination IP address, source IP address, destination port number, and source port number of a TCP packet, identify the function and status of the TCP packet on a TCP connection. TCP flags can be extracted from packets. Their statistics can be collected and sent to the NMS. The NMS checks the traffic volume of each flag and determines whether the network is attacked by TCP packets.

[(Optional) Configuring NetStream Interface Option Packets and Setting Option Template Refreshing Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_3027.html)

This section describes how to configure NetStream interface option packets and set option template refreshing parameters.

[Sampling IPv6 Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2003.html)

You can enable NetStream to sample and analyze the incoming or outgoing flows on an interface as required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_2007.html)

In routine maintenance or after NetStream configurations are complete, you can run the display commands in any view to check the running status of NetStream functions.