Understanding Anycast RP
========================

Understanding Anycast RP

#### Application Scenarios

In a conventional PIM-SM domain, each multicast group is mapped to only one RP. However, problems may occur if the network becomes overloaded or if traffic concentrates on an RP. For example, the RP may be overloaded, routes may converge slowly if the RP fails, or the multicast forwarding path may not be optimal. MSDP anycast RP offers a solution to these problems.

MSDP anycast RP allows you to configure multiple loopback interfaces as RPs in a PIM-SM domain, assign the same IP address to these loopback interfaces, and set up MSDP peer relationships between these RPs. This allows multicast sources to register with the closest RP and receivers to join the closest RP.

Anycast RP offers the following advantages:

* Optimal path between RPs: A multicast source registers with the closest RP to set up an optimal SPT. Receivers send Join messages to the closest RP to set up an optimal RPT.
* Load balancing between RPs: Each RP only needs to maintain information about some of the sources and groups in the PIM-SM domain, and is only required to forward some multicast packets.
* RP redundancy backup: When an RP fails, the multicast sources and receivers registered with this RP choose the next closest RP to register and join.

#### Implementation

In a PIM-SM domain on the network shown in [Figure 1](#EN-US_CONCEPT_0000001130623934__fig_dc_vrp_multicast_feature_001901), multicast sources S1 and S2 send multicast data to multicast group G, and U1 and U2 are members of group G.

**Figure 1** Network diagram of anycast RP  
![](figure/en-us_image_0000001130623954.png)

The implementation process of anycast RP in a PIM-SM domain is as follows:

1. RP1 and RP2 establish an MSDP peer relationship to implement intra-domain multicast.
2. Receivers send Join messages to the closest RPs to set up RPTs, and multicast sources register with the closest RP. RPs exchange SA messages through MSDP to share multicast source information.
3. Each RP joins an SPT with the source DR at the root to receive and forward multicast data. After the receiver receives the multicast data, it determines whether to initiate an SPT switchover.