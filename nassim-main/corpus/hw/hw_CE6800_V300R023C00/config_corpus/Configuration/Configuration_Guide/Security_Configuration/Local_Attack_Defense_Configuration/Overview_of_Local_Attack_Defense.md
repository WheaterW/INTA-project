Overview of Local Attack Defense
================================

Overview of Local Attack Defense

#### Definition

Local attack defense is a central processing unit (CPU) protection mechanism designed to ensure that the CPU can properly process normal services. The CPU of a device may receive both normal service packets and malicious packets targeting the CPU.

* If a large number of normal service packets are sent to the CPU, its usage surges. This severely impacts device performance, ultimately disrupting services.

* If the CPU is busy processing attack packets for an extended period, normal services will be interrupted, and in some cases even the entire system will crash.

To solve these issues, the local attack defense function is introduced. With this function enabled, the CPU can run properly when receiving a large number of normal service packets or attack packets, ensuring normal service running.


#### Basic Functions

Basic functions of local attack defense include CPU attack defense, port attack defense, user-level rate limiting, attack defense, and attack source tracing. As shown in [Figure 1](#EN-US_CONCEPT_0000001563996773__fig1268154164311), local attack defense uses a multi-level security mechanism to provide hierarchical protection for the device.

**Figure 1** Hierarchical protection of local attack defense  
![](figure/en-us_image_0000001563876561.png)

**Level 1**: Discarding malicious packets sent to the CPU through a filter or the punishment function of attack source tracing.

**Level 2**: Control Plane Committed Access Rate (CPCAR) based on protocol packets, whereby the device rate-limits the packets sent to the CPU based on the protocol type, preventing excess packets of a protocol from being sent to the CPU.

CPCAR control is the core of CPU attack defense, rate-limiting the protocol packets on a per device basis. In contrast, user-level rate limiting rate-limits protocol packets based on the MAC address of the user who initiates an attack. Both approaches will be depicted in the subsequent sections.

**Level 3**: Queue-based scheduling and rate limiting. After the rate of protocol packets is limited by CPCAR, the device can allocate a queue to each type of protocol packets, and schedules these queues based on weights or priorities. When a conflict occurs, the device preferentially processes high-priority queues. Rate limiting can also be implemented to limit the maximum rate of packets in each queue sent to the CPU, with the device discarding the protocol packets that exceed the rate limit in a queue.

In port attack defense, rate limiting is implemented by moving protocol packets to low-priority queues for processing.

**Level 4**: Rate limiting on all packets. At this level, the total number of packets processed by the CPU is limited to ensure that the CPU can process as many packets as possible within its processing capability.

Before rate-limiting all packets, the device analyzes the contents and behaviors of the packets sent to the CPU to determine whether these packets are attack packets. If so, the device takes defense approaches such as discarding or rate-limiting the packets. Packet attack defense includes defense against malformed packet attacks, fragmentation attacks, TCP SYN flood attacks, UDP flood attacks, and ICMP flood attacks.