Collecting Statistics About MPLS IPv4 Packets
=============================================

Collecting packet statistics on MPLS networks helps you monitor MPLS network status.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172373013__fig_dc_vrp_ns_cfg_000301), a carrier enables NetStream on the Router functioning as a NetStream Data Exporter (NDE) to obtain detailed network application information. The carrier can use the information to monitor abnormal network traffic, analyze users' operation modes, and plan networks between ASs.

If statistics about MPLS packets are collected on the P, the P sends statistics to inform the NetStream Collector (NSC) of the MPLS label-specific traffic volume.

**Figure 1** Networking diagram for collecting MPLS flow statistics  
![](images/fig_dc_vrp_ns_cfg_000301.png)  


#### Context

Before collecting statistics about MPLS IPv4 packets, enable MPLS on the device and interfaces and configure the MPLS network.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Output statistics about MPLS IPv4 packets in the form of original or aggregated flows.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   MPLS original and aggregated flows can be output in V9 or IPFIX format.
   
   * Statistics about original flows
     
     1. Run [**ip netstream mpls-aware**](cmdqueryname=ip+netstream+mpls-aware) { **label-only** | **ip-only** | **label-and-ip** }
        
        Statistics collection of MPLS packets is enabled.
        
        One of the following parameters can be configured to sample MPLS packets:
        
        + **label-only**: The device samples only MPLS labels, not inner IP packets.
        + **ip-only**: The device samples only inner IP packets, not MPLS labels.
        + **label-and-ip**: The device samples both MPLS labels and inner IP packets.
     2. For other configurations, see [Collecting Statistics About IPv4 Original Flows](dc_vrp_ns_cfg_0003.html).
   * Statistics about aggregated flows
     
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**ip netstream aggregation**](cmdqueryname=ip+netstream+aggregation) **mpls-label**
        
        The NetStream aggregation view is displayed.
     3. For other configurations, see [Collecting Statistics About IPv4 Aggregated Flows](dc_vrp_ns_cfg_0010.html).