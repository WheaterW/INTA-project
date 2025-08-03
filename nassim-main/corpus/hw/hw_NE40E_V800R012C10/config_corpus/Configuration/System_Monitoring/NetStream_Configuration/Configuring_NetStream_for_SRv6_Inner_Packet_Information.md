Configuring NetStream for SRv6 Inner Packet Information
=======================================================

This section describes how to configure NetStream for SRv6 inner packet information.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0307029339__fig199891203279), you can deploy NetStream on an SRv6 network to obtain detailed network application information. When inner packet statistics reach the NDE, the NDE can collect both outer IPv6 information and inner IPv4 information. After the NDE sends flow statistics to the NSC, the NSC collects the statistics and sends them to the NSA for analysis.

**Figure 1** Configuring NetStream for SRv6 inner packet information  
![](figure/en-us_image_0307029340.png)

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. To sample outer IPv6 packets, configure IPv6 flow statistics collection as required. For details, see [Collecting Statistics About IPv6 Original Flows](../vrp/dc_vrp_ns_cfg_2001.html), [Collecting Statistics About IPv6 Flexible Flows](../vrp/dc_vrp_ns_cfg_0057.html), or [Collecting Statistics About IPv6 Aggregated Flows](../vrp/dc_vrp_ns_cfg_2008.html).
3. To sample inner packet information carried by SRv6, perform the following operations as required:
   
   
   * In an IPv6 over SRv6 scenario, run the [**ipv6 netstream srv6-aware inner-header**](cmdqueryname=ipv6+netstream+srv6-aware+inner-header) command to enable NetStream for SRv6 inner packet information to sample inner IPv6 packets.
   * In an IPv4 over SRv6 scenario:
     1. Configure IPv4 flow statistics collection as required. For details, see [Collecting Statistics About IPv4 Original Flows](../vrp/dc_vrp_ns_cfg_0003.html), [Collecting Statistics About IPv4 Flexible Flows](../vrp/dc_vrp_ns_cfg_0052.html), or [Collecting Statistics About IPv4 Aggregated Flows](../vrp/dc_vrp_ns_cfg_0010.html).
     2. Run the [**ipv6 netstream srv6-aware inner-header**](cmdqueryname=ipv6+netstream+srv6-aware+inner-header) command to enable NetStream for SRv6 inner packet information to sample inner IPv4 packets.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.