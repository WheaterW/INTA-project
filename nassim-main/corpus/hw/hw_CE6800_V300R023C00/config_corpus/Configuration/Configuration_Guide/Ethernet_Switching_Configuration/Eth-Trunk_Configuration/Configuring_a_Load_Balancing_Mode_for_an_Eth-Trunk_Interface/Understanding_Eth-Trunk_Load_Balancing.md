Understanding Eth-Trunk Load Balancing
======================================

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM: An Eth-Trunk interface supports either static or dynamic load balancing.

For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S: An Eth-Trunk interface supports only static load balancing.

#### Static Load Balancing

When an Eth-Trunk is used to forward data frames, those from the same data flow may be transmitted over different physical links. As a result, data frames may arrive at the destination in an order different to that they were transmitted in, resulting in out-of-order packets.

Flow-based load balancing is introduced to prevent this problem and ensures that data frames of the same data flow are forwarded on the same physical link, implementing load balancing of flows. To achieve this, the system uses the hash algorithm to calculate the address in a data frame and generate a hash key, which is then used to search for the outbound interface in the Eth-Trunk forwarding table. Each MAC or IP address corresponds to a hash key, so the system uses different outbound interfaces to forward data.

**Flow-based Load Balancing**

In [Figure 1](#EN-US_CONCEPT_0000001130621716__fig_dc_fd_eth-trunk_000501), Eth-Trunk is located at the data link layer, between the MAC address and LLC sub-layers.

**Figure 1** Eth-Trunk in the Ethernet protocol stack  
![](figure/en-us_image_0000001176661357.png)

The Eth-Trunk module maintains a forwarding table consisting of the following fields:

* Hash key
  
  The hash key is calculated through the hash algorithm based on the MAC address or IP address in a data frame.
* Interface number
  
  Eth-Trunk forwarding entries are limited by the maximum number of member interfaces in an Eth-Trunk. Different hash keys map to different outbound interfaces.
  
  For example, if an Eth-Trunk supports a maximum of eight member interfaces, and physical interfaces 1, 2, 3, and 4 are bundled into an Eth-Trunk, the Eth-Trunk forwarding table contains eight entries, as shown in [Figure 2](#EN-US_CONCEPT_0000001130621716__fig_dc_fd_eth-trunk_000502). In the Eth-Trunk forwarding table, hash keys are 0, 1, 2, 3, 4, 5, 6, and 7, and the corresponding interface numbers are 1, 2, 3, 4, 1, 2, 3, and 4.

**Figure 2** Example of an Eth-Trunk forwarding table  
![](figure/en-us_image_0000001176661329.png)

The Eth-Trunk module uses the Eth-Trunk forwarding table to forward data frames according to the following process:

1. The Eth-Trunk module receives a data frame from the MAC sub-layer, and then extracts its source MAC/IP address or destination MAC/IP address.
2. The Eth-Trunk module calculates the hash key using the hash algorithm.
3. Using the hash key, the Eth-Trunk module searches for the corresponding interface in the Eth-Trunk forwarding table, and then sends the data frame from the interface.

**Selection of Load Balancing Modes**

In flow-based load balancing mode, packet flows are differentiated based on one or some of the following attributes: source MAC address, destination MAC address, source IP address, destination IP address, source TCP/UDP port number, and destination TCP/UDP port number. You can set the load balancing mode based on traffic models. When an attribute of traffic changes frequently, you can set the load balancing mode based on this attribute to ensure that the traffic is load balanced evenly. For example, if IP addresses in packets change frequently, use the load balancing mode based on the destination IP address, source IP address, or both. Likewise, if MAC addresses in packets change frequently and IP addresses are fixed, use the load balancing mode based on the destination MAC address, source MAC address, or both.

This can be further explained using the following example: DeviceA has two TCP packet flows. For one TCP packet flow, the source IP address is 192.168.1.1 (MAC address: a-a-a; source port number: 50), and the destination IP address is 172.16.1.1 (MAC address: b-b-b; destination port number: 2000). For the other TCP packet flow, the source IP address is 192.168.1.1 (MAC address: a-a-a; source port number: 60), and the destination IP address is 10.1.1.1 (MAC address: c-c-c; destination port number: 2000). If DeviceA is configured to load balance packets based on the source MAC address, only one outbound interface will be available for sending packets. In contrast, if DeviceA is configured to load balance packets based on the destination IP address, packets destined for different destination IP addresses can be sent from different outbound interfaces.

When configuring a load balancing mode, pay attention to the following points:

* The load balancing mode only takes effect on traffic leaving the outbound interface. If traffic entering the inbound interface is unevenly load balanced, change the load balancing mode of the uplink outbound interface.
* Ensure that packet flows are load balanced among as many active links as possible. Traffic congestion may occur if packet flows are transmitted over just one link, impacting services.
  
  For example, when all data frames in a data flow have the same destination MAC address and IP address, load balance the frames based on the source MAC address and IP address, instead of the destination addresses. Otherwise, traffic will be transmitted over just one link, causing congestion.

#### Dynamic Load Balancing

Flow-based static load balancing ensures the sequence of packets but cannot balance the usage of member links, resulting in congestion or even packet discarding on some member links in scenarios involving a large amount of data flows. Dynamic load balancing can solve this problem. During data packet forwarding, this mechanism checks the usage of each member link and selects that with the lightest load to forward data packets.

Three dynamic load balancing modes are available: [Eligible](#EN-US_CONCEPT_0000001130621716__li_eligible) (recommended), [Spray](#EN-US_CONCEPT_0000001130621716__li_spray), and [Fixed](#EN-US_CONCEPT_0000001130621716__li_fixed).

A flow refers to data packets with the same feature fields and is divided into multiple flowlets based on a specific interval.

* **Eligible mode**
  
  A transmission delay exists on links between two directly-connected devices. These links form an Eth-Trunk. If the interval for sending data packets is greater than the maximum transmission delay on Eth-Trunk member links, the data packets arrive at the receive end in the correct sequence when they are transmitted through different member links.
  
  The eligible load balancing mode is implemented based on this principle. In this mode, when forwarding a data packet, a device first determines the forwarding interval between this data packet and the previous one in the same flow. If the interval is greater than the maximum transmission delay on member links, the data packet is the first packet of a new flowlet, and the device selects a member link with the lightest load to forward it. If the interval is less than or equal to the maximum transmission delay on member links, the data packet is in the same flowlet as the previous one, and the device forwards it through the same link.
  
  **Figure 3** Eligible dynamic load balancing mode  
  ![](figure/en-us_image_0000001130781610.png "Click to enlarge")
  [Figure 3](#EN-US_CONCEPT_0000001130621716__fig_dc_cfg_low-latency_000802) describes how dynamic load balancing in eligible mode is implemented.
  1. Data packet 1 is the first packet of Flow 1. When receiving data packet 1, DeviceA detects that it is the first packet of a new flowlet (flowlet 1-1) and selects a member link with a lighter load to forward it. At this time, neither member link 1 or 2 carries traffic and DeviceA randomly selects one (in this case, member link 1).
  2. When receiving data packet 2, DeviceA detects that the interval between data packets 1 and 2 is less than or equal to the maximum transmission delay on the two member links, and forwards data packet 2 in the same flowlet as data packet 1 through the same link (member link 1).
  3. When receiving data packet 3, DeviceA detects that the interval between data packets 2 and 3 is less than or equal to the maximum transmission delay on the two member links, and forwards data packet 3 in the same flowlet as data packet 2 through the same link (member link 1).
  4. Data packet 4 is the first packet of Flow 2. When receiving data packet 4, DeviceA detects that it is the first packet of a new flowlet (flowlet 2-1) and selects a member link with a lighter load (member link 2) to forward it.
  5. When receiving data packet 5, DeviceA detects that the interval between data packets 4 and 5 is less than or equal to the maximum transmission delay on the two member links, and forwards data packet 5 in the same flowlet as data packet 4 through the same link (member link 2).
  6. When receiving data packet 6, DeviceA detects that the interval between data packets 3 and 6 is greater than the maximum transmission delay on the two member links, indicating that data packet 6 is the first packet of a new flowlet (flowlet 1-2). Then DeviceA forwards data packet 6 through a link with a lighter load (member link 2).
  7. When receiving data packet 7, DeviceA detects that the interval between data packets 6 and 7 is less than or equal to the maximum transmission delay on the two member links and forwards data packet 7 in the same flowlet as data packet 6 through the same link (member link 2).
* **Spray mode**
  
  The spray dynamic load balancing mode uses the packet-based load sharing mechanism, whereby a device forwards a data packet through an Eth-Trunk member link with the lightest load. In this mechanism, if the interval between two adjacent data packets in the same flow is less than or equal to the maximum transmission delay on member links, and the data packets are forwarded through different links, out-of-order packet delivery may occur when both packets arrive at the receive end. If this mode is used, the device must support packet reassembly in order to address out-of-order packet delivery.
  
  **Figure 4** Spray dynamic load balancing mode  
  ![](figure/en-us_image_0000001176661339.png)
  [Figure 4](#EN-US_CONCEPT_0000001130621716__fig_dc_cfg_low-latency_000803) describes how dynamic load balancing in spray mode is implemented. For example, assume that data packets 1, 2, 4, and 5 have the same size and data packet 3 is 4 times the size of data packet 1.
  1. When receiving data packet 1, DeviceA selects a member link with a lighter load between the two member links to forward this data packet. At this time, neither member link 1 or 2 carries traffic and DeviceA randomly selects one (in this case, member link 1).
  2. When receiving data packet 2, DeviceA selects a member link with a lighter load (member link 2) to forward it.
  3. When receiving data packet 3, DeviceA selects a member link with a lighter load (member link 1) to forward it.
  4. When receiving data packet 4, DeviceA selects a member link with a lighter load (member link 2) to forward it.
  5. When receiving data packet 5, DeviceA selects a member link with a lighter load (member link 2) to forward it.
  
  In this case, packets 2 and 4 arrive at DeviceB before packet 3, resulting in out-of-order packets.
* **Fixed mode**
  
  In fixed dynamic load balancing mode, a device forwards a data packet through the same link that forwarded the previous one. If the data packet to be forwarded is the first packet in a flow, the device forwards it through one of the member links in static load balancing mode based on the hash result.
  
  **Figure 5** Fixed dynamic load balancing mode  
  ![](figure/en-us_image_0000001176741263.png)
  [Figure 5](#EN-US_CONCEPT_0000001130621716__fig_dc_cfg_low-latency_000804) describes how dynamic load balancing in fixed mode is implemented.
  1. When receiving data packet 1, DeviceA selects one of the member links in static load balancing mode based on the hash result to forward it (in this case, member link 1).
  2. When receiving data packet 2 which is in the same flow (flow 1) as the previous packet (data packet 1), DeviceA also selects member link 1 to forward it.
  3. When receiving data packet 3, DeviceA detects that it is the first packet of Flow 2 and forwards it through one of the member links in static load balancing mode based on the hash result (in this case, member link 2).
  4. When receiving data packet 4 which is in the same flow as the previous packet (data packet 2), DeviceA selects member link 1 to forward it.