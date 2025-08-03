Collecting Statistics About MPLS IPv6 Packet
============================================

Collecting packet statistics on MPLS networks helps you to monitor MPLS network conditions.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172373014__fig_dc_vrp_ns_cfg_000301), a carrier enables NetStream on the Router to obtain detailed network application information. The carrier can use the information to monitor abnormal network traffic, analyze users' operation modes, and plan networks between ASs.

If statistics about MPLS packets are collected on the P (NDE), the P sends statistics to inform the NetStream Collector (NSC) of the MPLS label-specific traffic volume.![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NetStream can be functioned only in the user side of the MPLS network, if the SR-MPLS TE tunnel is applied in public network.



**Figure 1** Networking diagram for collecting MPLS flow statistics  
![](images/fig_dc_vrp_ns_cfg_000301.png)  


#### Context

Before collecting statistics about MPLS IPv6 packets, enable MPLS on the device and interfaces and configure the MPLS network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 netstream mpls-aware**](cmdqueryname=ipv6+netstream+mpls-aware) { **label-only** | **ip-only** | **label-and-ip** }
   
   
   
   Statistics collection for MPLS packets is enabled.
   
   
   
   One of the following parameters can be configured to sample MPLS packets:
   
   * **label-only**: The device samples only MPLS labels, not inner IP packets.
   * **ip-only**: The device samples only inner IP packets, not MPLS labels.
   * **label-and-ip**: The device samples both MPLS labels and inner IP packets.
3. Output statistics about MPLS IPv6 packets in the form of original or aggregated flows. See [Collecting Statistics About IPv6 Original Flows](dc_vrp_ns_cfg_2001.html) and [Collecting Statistics About IPv6 Aggregated Flows](dc_vrp_ns_cfg_2008.html) as required.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Statistics about MPLS original flows and aggregated flows can be collected in V9 or IPFIX format.