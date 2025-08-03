Per-Flow and Per-Packet Load Balancing
======================================

Load balancing works in per-flow or per-packet mode, irrespective of whether it is route, tunnel, or trunk load balancing.

#### Per-Flow Load Balancing

Per-flow load balancing classifies packets into different flows based on a certain rule, such as the IP 5-tuple (source IP address, destination IP address, protocol number, source port number, and destination port number). Packets of the same flow go over the same link.

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001564001377__fig_load-balance_feature_00501), DeviceA sends six packets, P1, P2, P3, P4, P5, and P6 in sequence to DeviceB over links A and B in load balancing mode. P2, P3, and P5 are destined for DeviceC, and P1, P4, and P6 for DeviceD. If per-flow load balancing is used, packets destined for DeviceC can go over link A, and packets destined for DeviceD can go over link B. Alternatively, packets destined for DeviceC can go over link B, and packets destined for DeviceD can go over link A.

**Figure 1** Network diagram of per-flow load balancing  
![](figure/en-us_image_0000001512841634.png)

**Symmetric load balancing**

Symmetric load balancing is a special per-flow load balancing mode.

This mode distinguishes data flows based on the IP addresses of packets. In this way, the same data flow goes over the same link.

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001564001377__fig_load-balance_feature_00503), DeviceA forwards the same data flow to DeviceB over link A; DeviceB obtains the same link index by exchanging the source and destination IP addresses, and then hashes the flow to link A.

**Figure 2** Network diagram of symmetric load balancing  
![](figure/en-us_image_0000001513041190.png)

Symmetric load balancing ensures packet sequence but not bandwidth utilization.


#### Per-Packet Load Balancing

Per-packet load balancing evenly distributes packets among links used for load balancing based on their incoming sequence, as shown in [Figure 3](#EN-US_CONCEPT_0000001564001377__fig_load-balance_feature_00502).

**Figure 3** Network diagram of per-packet load balancing  
![](figure/en-us_image_0000001564001433.png)
![](public_sys-resources/note_3.0-en-us.png) 

Per-packet load balancing improves bandwidth utilization but does not ensure the order in which packets are delivered. As such, it applies only to scenarios where no strict requirements are imposed on the packet order.