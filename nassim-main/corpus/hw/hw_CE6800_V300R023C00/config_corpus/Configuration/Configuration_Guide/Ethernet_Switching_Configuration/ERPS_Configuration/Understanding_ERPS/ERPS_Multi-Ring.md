ERPS Multi-Ring
===============

In an ERPS multi-ring scenario, multiple ERPS rings are configured on an ERPS network. ERPSv1 supports only single-ring topologies, whereas ERPSv2 supports both single-ring and multi-ring topologies. An ERPS multi-ring network consists of one or more major rings and sub-rings. R-APS PDUs from sub-rings can be transmitted in VC or NVC mode, depending on whether the R-APS PDUs enter the major ring.

This section describes how ERPS is implemented on a multi-ring network where R-APS PDUs from sub-rings are transmitted in NVC mode when links are normal, when a link fails, and when the link recovers.

#### Normal Links

In [Figure 1](#EN-US_CONCEPT_0000001141938800__fig_dc_fd_erps_001001), DeviceA through DeviceE constitute a major ring. DeviceB, DeviceC, and DeviceF constitute sub-ring 1, and DeviceC, DeviceD, and DeviceG constitute sub-ring 2. The devices on each ring can communicate with each other.

1. To prevent loops, each ring blocks its RPL owner port.
2. The RPL owner port on the major ring sends R-APS NRRB messages to other nodes on the major ring at an interval of 5s. Similarly, the RPL owner ports on sub-rings 1 and 2 send R-APS NR messages to other nodes on their respective rings at an interval of 5s. The R-APS PDUs of the major ring are transmitted only on the major ring. The R-APS PDUs of the two sub-rings are terminated on the interconnected nodes and are not transmitted to the major ring.

Traffic exchanged between PC1 and the upstream network is transmitted along the path PC1 <-> DeviceF <-> DeviceB <-> DeviceA <-> Router1, and traffic exchanged between PC2 and the upstream network is transmitted along the path PC2 <-> DeviceG <-> DeviceD <-> DeviceE <-> Router2.

**Figure 1** ERPS multi-ring networking (normal links)  
![](figure/en-us_image_0000001261768219.png)

#### Link Fault

In [Figure 2](#EN-US_CONCEPT_0000001141938800__fig164623485137), if the link between DeviceD and DeviceG fails, the ERPS protection switching mechanism is triggered. The ports on both ends of the faulty link are blocked, and the RPL owner port on sub-ring 2 is unblocked to send and receive traffic. User traffic of PC1 is not affected. To ensure that downlink traffic of PC2 is not interrupted, interconnected nodes DeviceC and DeviceD need to notify the other nodes on the major ring of the topology change on sub-ring 2. Traffic exchanged between PC2 and the upstream network is transmitted along the path PC2 <-> DeviceG <-> DeviceC <-> DeviceB <-> DeviceA <-> DeviceE <-> Router2. The detailed process is as follows:

1. After DeviceD and DeviceG detect the link fault, they block their ports on the faulty link and update their FDB entries.
2. DeviceG sends three consecutive R-APS SF messages carrying local link fault information within sub-ring 2 immediately after detecting the link fault and then sends R-APS SF messages at an interval of 5s.
3. DeviceG where the RPL owner port resides unblocks the RPL owner port and updates its FDB entries.
4. After the interconnected node DeviceC receives R-APS SF messages, it updates its FDB entries. After detecting the topology change, DeviceC and DeviceD send R-APS Event messages within the major ring to notify the other nodes of the topology change on sub-ring 2.
5. After receiving R-APS Event messages, the other nodes on the major ring update their FDB entries.

**Figure 2** ERPS multi-ring networking (link fault)  
![](figure/en-us_image_0000001216729386.png)

#### Link Recovery

After the faulty link recovers, if the ERPS rings use the revertive switching mode, the device where the RPL owner port resides blocks the RPL again, and the link that has recovered is used to forward traffic. If the ERPS rings use the non-revertive switching mode, the link that has recovered is still blocked, and the RPL is not blocked. The following uses the revertive switching mode as an example to describe the recovery process:

1. After the link between DeviceD and DeviceG recovers, DeviceD and DeviceG start the Guard timer to avoid receiving out-of-date R-APS PDUs. They do not receive any R-APS PDUs before the timer expires. At the same time, DeviceD and DeviceG send R-APS NR messages within sub-ring 2.
2. DeviceG where the RPL owner port resides starts the WTR timer. After the WTR timer expires, DeviceG blocks the RPL owner port and unblocks its port on the link that has recovered. At the same time, DeviceG sends R-APS NRRB messages.
3. After receiving R-APS NRRB messages from DeviceG, DeviceD unblocks its blocked port, stops sending R-APS NR messages, and updates its FDB entries. After receiving R-APS NRRB messages from DeviceG, DeviceC also updates its FDB entries.
4. After DeviceC and DeviceD update their FDB entries, they send R-APS Event messages within the major ring to notify the other nodes of the topology change on sub-ring 2.
5. After receiving R-APS Event messages, the other nodes on the major ring update their FDB entries.

Finally, the user traffic of PC2 is switched back to the path shown in [Figure 1](#EN-US_CONCEPT_0000001141938800__fig_dc_fd_erps_001001).