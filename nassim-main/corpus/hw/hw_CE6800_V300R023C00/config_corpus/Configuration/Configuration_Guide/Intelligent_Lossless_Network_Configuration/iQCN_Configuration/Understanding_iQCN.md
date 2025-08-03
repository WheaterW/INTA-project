Understanding iQCN
==================

Understanding iQCN

#### Context

As shown in [Figure 1](#EN-US_CONCEPT_0000001512840010__fig58123141845), the three roles in DCQCN are as follows:

* **Congestion Point (CP)**
  
  An ECN-enabled forwarding device functions as a CP. If the CP finds that the queue buffer of its outbound interface exceeds the ECN threshold, it performs ECN marking for forwarded packets (setting the ECN field to 11) based on a certain probability, indicating that congestion has occurred on the network.
* **Notification Point (NP)**
  
  The packet receiver functions as an NP. After receiving ECN-marked packets, the NP knows that congestion has occurred on the network, and then sends CNPs to the Reaction Point (RP) based on the source address in the ECN-marked packets, instructing the RP to reduce the packet sending rate.
* **Reaction Point (RP)**
  
  The packet sender functions as an RP. The NIC of the RP can adjust the packet sending rate based on the received CNPs. The process is as follows:
  
  1. After receiving CNPs, the RP knows that congestion occurs on the network and reduces the packet sending rate.
  2. If the RP receives CNPs within the configured interval between rate increase events of the NIC, the RP continues to decrease the packet sending rate.
  3. If the RP does not receive CNPs after the configured interval between rate increase events of the NIC expires, the RP determines that congestion has been removed and proactively increases the packet sending rate to improve the throughput (bandwidth usage).

**Figure 1** DCQCN implementation  
![](figure/en-us_image_0000001513159582.png)

Although congestion occurs on the CP, the device that reports the congestion is the NP at the end of the packet transmission path. As such, if congestion occurs on the network, the long congestion feedback path from the NP to the RP increases the forwarding delay of CNPs because of factors such as packets waiting in queues. As a result, the RP cannot receive the CNPs in a timely manner. Additionally, when the network is congested, the NP frequently receives ECN-marked packets, but cannot send CNPs for all congested queues promptly because the rate at which its NIC generates CNPs is limited. If the period during which the RP does not receive CNPs exceeds the interval between rate increase events of its NIC, the RP increases the packet sending rate. As a result, the buffer of the forwarding device may be further congested, and even devices on the entire network stop sending traffic due to PFC.

iQCN enables the forwarding device to intelligently detect network congestion. Based on the interval at which the NP sends CNPs and the interval between rate increase events of the NIC of the RP, the forwarding device proactively sends CNPs to the RP so that the RP can reduce the packet sending rate in a timely manner.


#### iQCN Implementation

[Figure 2](#EN-US_CONCEPT_0000001512840010__fig3772912145720) shows how iQCN is implemented.

1. If congestion does not occur on the CP when packets are sent from RP1 to NP1, the CP forwards the packets properly.
2. If congestion occurs on the outbound interface of the CP when packets are sent from RP2 and RP3 to NP2, the CP performs ECN marking for the packets and forwards the packets to NP2.
3. After receiving the ECN-marked packets, NP2 learns that congestion occurs on the network, and its NIC sends CNPs to RP2 and RP3, instructing their NICs to reduce the packet sending rate. If congestion persists on the outbound interface of the CP, NP2 continues to send CNPs.
4. The iQCN-enabled CP records the received CNPs and maintains a flow table that contains the CNP information and timestamp. Additionally, the CP keeps monitoring the congestion status of its outbound interface. When its outbound interface is heavily congested, the CP compares the interval at which CNPs are received with the interval between rate increase events of an RP's NIC.
   * If the interval at which CNPs are received from an NP is shorter than the interval between rate increase events of an RP's NIC, the CP determines that the RP's NIC can decrease the packet sending rate properly, and forwards CNPs to the RP.
   * If the interval at which CNPs are received from an NP is longer than the interval between rate increase events of an RP's NIC, the CP determines that the RP's NIC cannot decrease the packet sending rate in a timely manner and may increase the rate, and therefore proactively sends CNPs to the RP.

**Figure 2** iQCN implementation  
![](figure/en-us_image_0000001512840014.png)