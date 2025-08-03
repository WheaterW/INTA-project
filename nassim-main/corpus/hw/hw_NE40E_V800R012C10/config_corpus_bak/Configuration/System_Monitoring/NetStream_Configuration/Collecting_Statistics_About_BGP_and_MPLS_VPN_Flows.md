Collecting Statistics About BGP/MPLS VPN Flows
==============================================

Collecting traffic statistics on BGP/MPLS VPN networks helps monitor the BGP/MPLS VPN network condition.

#### Usage Scenario

In [Figure 1](#EN-US_TASK_0172373015__fig_dc_vrp_ns_cfg_004201), statistics about MPLS flows sent by the P to the NetStream Collector (NSC) inform the NSC of the traffic volume and traffic type corresponding to each label. Such statistics, however, cannot tell to which VPN each traffic belongs. In this case, the PE sends the meaning of each MPLS label (1024 in the figure) to the NSC so that the NSC can determine to which VPN the received traffic belongs. The NSC can analyze the traffic data of each VPN and display the result.

In the MPLS flow statistics sent by the P, the corresponding label information is as follows:

* Out-label: indicates the outgoing label, which is a public network label and is used to guide packet forwarding.
* In-label: indicates the innermost label of the packet and is the VPN label of PE2.

**Figure 1** Collecting statistics about BGP/MPLS VPN flows  
![](figure/en-us_image_0000001987063309.png)

#### Context

Before collecting statistics about BGP/MPLS VPN flows, deploy the BGP/MPLS VPN network.


#### Procedure

* Enable the P to collect statistics about MPLS flows.
  
  
  
  Set the parameters according to [Collecting Statistics About MPLS IPv4 Packets](dc_vrp_ns_cfg_0015.html) or [Collecting Statistics About MPLS IPv6 Packet](dc_vrp_ns_cfg_0019.html).
* (Optional) Run the [**ip netstream export template option application-label**](cmdqueryname=ip+netstream+export+template+option+application-label) command to enable TAL option export and export the TAL option template to the NSC.
  
  
  
  After this command is run, the collector can parse labels only when it can parse the extended fields described in [Table 1](#EN-US_TASK_0172373015__table870874914268).
  
  **Table 1** Extended fields
  | Extended Field ID | Description |
  | --- | --- |
  | 1200 | Label generation time |
  | 1201 | VPN name |
  | 1202 | Label value of a VPN instance |
  | 1203 | Label range |
  | 1204 | Start label value |
  | 1205 | IP address of the remote PE |
  | 1206 | Local site ID in the L2VPN scenario |
  | 1207 | Remote site ID in the L2VPN scenario |
  | 1208 | VPN RD value |
  | 1209 | L2VPN vcID |
  | 1210 | L2VPN vcType |
  | 1211 | Label type |
  | 1212 | L2VPN mode |
  | 1227 | VPN type |
  | 1228 | VPN IP version |