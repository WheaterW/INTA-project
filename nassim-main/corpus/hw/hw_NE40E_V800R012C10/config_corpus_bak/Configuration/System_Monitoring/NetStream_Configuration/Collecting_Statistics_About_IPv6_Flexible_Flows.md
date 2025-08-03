Collecting Statistics About IPv6 Flexible Flows
===============================================

Before collecting statistics about IPv6 flexible flows, familiarize yourself with the applicable environment and complete the pre-configuration tasks. This can help you complete the configuration task quickly and accurately.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_CONCEPT_0172373001__fig_dc_vrp_ns_cfg_000301), a carrier enables NetStream on the Router functioning as an NDE to obtain detailed network application information. The user can use the information to monitor abnormal network traffic, analyze users' operation modes, and plan networks between ASs.

Flexible flow packets provide user-defined templates for users to customize matching and collected fields as required. The user-defined template improves traffic analysis accuracy and reduces network bandwidth occupation, CPU usage, and storage space usage.

**Figure 1** Networking diagram for collecting IPv6 flow statistics  
![](images/fig_dc_vrp_ns_cfg_000305.png)  


#### Pre-configuration Tasks

Before collecting the statistics about IPv6 flexible flows, configure static routes or enable an IGP to implement network connectivity.


[Specifying a NetStream Service Processing Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0058.html)

After sampling packets, each NetStream-enabled interface board sends sampled packets to the NetStream service processing board for aggregation and output.

[Configuring a Flexible Flow Statistics Template](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0059.html)

When configuring the flexible flow statistics output function, configure a flexible flow statistics template, customize matching and collected fields, and apply the template to an interface.

[Outputting Flexible Flow Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0064.html)

To ensure that flexible flow packets can be correctly output to the NMS, specify the related parameters for flexible flows.

[(Optional) Configuring NetStream Monitoring Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0061.html)

NetStream services can be configured on the NetStream Data Exporter (NDE), enabling carriers to implement more delicate traffic statistics collection and management over IPv6 flexible flows.

[(Optional) Adjusting the AS Field Mode and Interface Index Type](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0062.html)

For the NSC to properly receive and parse NetStream packets output by the NDE, ensure that the AS field modes and interface index types configured on the NDE and the NSC are the same.

[(Optional) Configuring NetStream Interface Option Packets and Setting Option Template Refreshing Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_3027_2.html)

This section describes how to configure NetStream interface option packets and set option template refreshing parameters.

[Sampling IPv6 Flows](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0066.html)

You can enable NetStream to sample and analyze the incoming or outgoing flows on an interface as required.

[Verifying the Configuration of IPv6 Flexible Flow Statistics Collection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ns_cfg_0068.html)

After NetStream configurations are complete, you can run the display commands in any view to verify the running status of NetStream functions.