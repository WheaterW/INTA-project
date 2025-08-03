ETS
===

ETS

#### Context

A converged data center network has SAN traffic, IPC traffic, and LAN traffic. The QoS requirements of these traffic types differ greatly. For example, SAN traffic is sensitive to packet loss and relies on in-order delivery. IPC traffic is exchanged between servers and requires low latency. LAN traffic allows some packet loss and is delivered on a BE basis. Packet loss and disorder can be processed by the hosts at both ends, and does not require much intervention by network nodes. Traditional QoS cannot meet these requirements, which can instead be met by ETS that uses hierarchical scheduling.


#### Fundamentals

ETS provides two-level scheduling: scheduling based on priority groups and scheduling based on queues, as shown in [Figure 1](#EN-US_CONCEPT_0000001513149646__fig_dc_fd_dcb_000502). An interface first schedules priority groups, and then schedules priority queues.**Figure 1** ETS process  
![](figure/en-us_image_0000001512670542.png)

In contrast with common QoS, ETS provides scheduling based on priority groups. ETS adds traffic of the same type to a priority group, ensuring traffic of the same type obtains the same CoS.


#### Scheduling Based on Priority Groups

A priority group is a group of priority queues that use the same scheduling mode. You can add queues with different priorities to a priority group. Scheduling based on the priority group is called level-1 scheduling.

ETS defines three priority groups by default: PG0, PG1, and PG15, which process LAN traffic, SAN traffic, and IPC traffic respectively.

The following table describes the default attributes of priority groups.

**Table 1** Scheduling based on priority groups
| Priority Group ID | Priority Queue | Scheduling Mode | Bandwidth Usage |
| --- | --- | --- | --- |
| PG0 | 0, 1, 2, 4, 5 | DRR | 50% |
| PG1 | 3 | DRR | 50% |
| PG15 | 6, 7 | PQ | - |


As defined by ETS, PG0 and PG1 use deficit round robin (DRR), and PG15 uses priority queuing (PQ) to schedule latency-sensitive IPC traffic. Bandwidth can be allocated to priority groups according to actual network requirements.

![](public_sys-resources/note_3.0-en-us.png) 

The scheduling mode of each priority group cannot be changed.

Assume that an outbound interface has eight queues and their priorities range from 0 to 7. The queue with priority 3 carries Fibre Channel over Ethernet (FCoE) traffic, and so is added to the SAN group (PG1). Queues with priorities 0, 1, 2, 4, and 5 carry LAN traffic, and so are added to the LAN group (PG0). Queues with priorities 6 and 7 carry IPC traffic, and so are added to the IPC group (PG15). The total bandwidth of the interface is 10 Gbit/s. PG15 obtains 2 Gbit/s, and PG1 and PG0 split the remaining bandwidth 50/50, each obtaining 4 Gbit/s.

**Figure 2** Congestion management based on priority groups  
![](figure/en-us_image_0000001512830142.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001513149646__fig_dc_fd_dcb_000501), at t1 and t2, all traffic can be forwarded because the total traffic on the interface is within the interface bandwidth. At t3, the total traffic exceeds the interface bandwidth and LAN traffic exceeds the given bandwidth. At this time, LAN traffic is scheduled based on ETS parameters and 1 Gbit/s LAN traffic is discarded.

ETS also provides traffic shaping based on priority groups. This traffic shaping mechanism limits traffic bursts in a priority group to ensure that traffic in this group is sent out at an even rate.


#### Priority-based Scheduling

ETS also provides priority-based queue scheduling, also known as level-2 scheduling.

In addition, ETS provides priority-based queue congestion management, queue shaping, and queue congestion avoidance. For details, see "QoS Configuration" in Configuration Guide.