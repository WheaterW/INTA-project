Understanding Congestion Management
===================================

As network services continue to increase and users demand even higher network quality, the limited bandwidth cannot meet such lofty requirements. As a result, issues begin to arise due to congestion, such as longer delays and signal loss. Congestion management is required when a network is intermittently congested, and delay-sensitive services require higher QoS than delay-insensitive services. If congestion persists on the network after congestion management is configured, it is necessary to increase the bandwidth. Congestion management implements queuing and scheduling when sending packet flows.

The device has eight queues on each interface in the outbound direction, and the queues are identified by index numbers ranging from 0 to 7. The device automatically sends classified packets to queues based on mappings between local priorities and queues, and then schedules the packets using queue scheduling mechanisms.

#### Common Queue Scheduling Mechanisms

* Priority Queuing (PQ) scheduling
  
  PQ scheduling, also referred to as strict priority (SP) scheduling, schedules packets in descending order of queue priority. This means that packets in queues with a low priority can be scheduled only after all packets in high priority queues have been scheduled. The device places core services into high-priority queues and non-core services (such as email services) into low-priority queues, ensuring that core services are processed preferentially. In this case, non-core services are processed only when all core services are processed.
  
  In [Figure 1](#EN-US_CONCEPT_0000001513150686__fig1613810482017), queues 7 to 0 are arranged in descending order of priority. When the link transmits packets, queue 7 is preferentially processed, with subsequent queues processed only when queue 7 becomes empty. Packets in lower-priority queues are sent at the link rate when higher-priority queues are empty. The packets in queue 6 are sent at the link rate when packets in queue 6 need to be sent and queue 7 is empty. The packets in queue 5 are sent at the link rate when queue 6 and queue 7 are empty, and so on.
  
  PQ scheduling is valid for short-delay services. If we assume that data flow X is placed in queue 7 on each node, the packets of data flow X are processed first when they reach a node.
  
  PQ scheduling, however, may result in the starvation of packets in queues with lower priorities. For example, if data flows placed into queue 7 arrive at 100% link rate in a period, the scheduler does not process flows in queues 0 to 6.
  
  To prevent starvation of packets in some queues, upstream devices must accurately define the service characteristics of data flows so that data flows placed in queue 7 do not exceed a given percentage of the link capacity. Consequently, queue 7 is not full and the scheduler can process packets in queues with lower priorities.
  
  **Figure 1** PQ scheduling  
  ![](figure/en-us_image_0000001563990969.png)
* Weighted Deficit Round Robin (WDRR) scheduling
  
  WDRR schedules packets by taking the packet length into account, ensuring that packets in all the queues are scheduled in turn.
  
  In WDRR scheduling, the deficit indicates the bandwidth deficit of each queue. The initial value is 0, and the system allocates bandwidth to each queue based on the weight, with the deficit calculated as follows: If the deficit of a queue is greater than 0, the queue participates in scheduling. The device sends a packet and calculates the deficit based on that packet's length. If the deficit of a queue is less than 0, the queue does not participate in scheduling, and the current deficit is used as the initial value in the next round of scheduling.
  
  **Figure 2** Queue weights  
  ![](figure/en-us_image_0000001512831170.png)
  
  In [Figure 2](#EN-US_CONCEPT_0000001513150686__fig999280222), the weights of queues 7, 6, 5, 4, 3, 2, 1, and 0 are set to 40, 30, 20, 10, 40, 30, 20, and 10, respectively. During scheduling, queues 7, 6, 5, 4, 3, 2, 1, and 0 obtain 20%, 15%, 10%, 5%, 20%, 15%, 10%, and 5% of the bandwidth, respectively. Queues 7 and 6 are used as examples to describe WDRR scheduling. For this example, assume that queue 7 obtains 400 byte/s bandwidth and queue 6 obtains 300 byte/s bandwidth.
  
  + First round of scheduling
    
    Deficit[7][1] = 0 + 400 = 400
    
    Deficit[6][1] = 0 + 300 = 300
    
    After a packet of 900 bytes in queue 7 and a packet of 400 bytes in queue 6 are sent, the values are as follows:
    
    Deficit[7][1] = 400 â 900 = â500
    
    Deficit[6][1] = 300 â 400 = â100
  + Second round of scheduling
    
    Deficit [7][2] = â500 + 400 = â100
    
    Deficit [6][2] = â100 + 300 = 200
    
    The packet in queue 7 is not scheduled because the deficit of queue 7 is negative. After a packet of 300 bytes in queue 6 is sent, the value is as follows:
    
    Deficit [6][2] = 200 â 300 = â100
  + Third round of scheduling
    
    Deficit[7][3] = â100 + 400 = 300
    
    Deficit[6][3] = â100 + 300 = 200
    
    After a packet of 600 bytes in queue 7 and a packet of 500 bytes in queue 6 are sent, the values are as follows:
    
    Deficit[7][3] = 300 â 600 = â300
    
    Deficit[6][3] = 200 â 500 = â300
    
    This process is repeated, leading to queue 7 and queue 6 respectively obtaining 20% and 15% of the bandwidth. As such, you can obtain the required bandwidth by setting proper weights.
  
  WDRR scheduling prevents packets in queues with lower priorities from being starved out for a long time in PQ scheduling and uneven bandwidth allocation when the packet lengths of queues are different or vary greatly. However, WDRR scheduling has a disadvantage that services requiring a short delay (such as voice services) cannot be scheduled in a timely manner.
* LPQ scheduling
  
  Low priority queuing (LPQ), also known as strict priority low (SPL) or absolute priority scheduling, offers a scheduling mode similar to that of PQ queues. The difference is that while PQ queues can preempt the bandwidth of WDRR queues, LPQ queues cannot do so in case of congestion. After packets in PQ and WDRR queues are all scheduled, the remaining bandwidth can be assigned to packets in LPQ queues.
  
  In practice, Best-Effort (BE) flows can be put into LPQ queues. When a network is overloaded, all BE flows are limited so that other services can be processed preferentially.

#### Scheduling Sequence in Different Scheduling Modes

All eight interface queues can be configured with one scheduling mode or a combination of different scheduling modes. PQ+WDRR is the most commonly used scheduling mode.

If only PQ scheduling is used, the packets in lower priority queues may fail to obtain bandwidth for long periods. If only WDRR scheduling is used, short-delay services such as voice services cannot be scheduled preferentially. PQ+WDRR scheduling offers the advantages of both PQ and WDRR scheduling while offsetting their disadvantages.

Eight queues on the device interface are classified into two groups, and you can specify PQ scheduling for certain queues and WDRR scheduling for others.

**Figure 3** PQ+WDRR scheduling  
![](figure/en-us_image_0000001513030722.png)

In [Figure 3](#EN-US_CONCEPT_0000001513150686__fig188171214422), the device first schedules traffic in queues 7, 6, and 5 in PQ mode, before then scheduling traffic in queues 4, 3, 2, 1, and 0 in WDRR mode. Queues 4, 3, 2, 1, and 0 have their own weights.

Important protocol packets or short-delay service packets must be placed in queues using PQ scheduling in order to be scheduled first. Other packets are placed in queues using WDRR scheduling.

In addition to the combination of any two of the scheduling modes, the device also supports the combination of PQ+WDRR+LPQ. In this case, the device schedules packets in PQ, WDRR, and LPQ queues in sequence, as shown in [Figure 4](#EN-US_CONCEPT_0000001513150686__fig_qos_feature_04008).

**Figure 4** PQ+WDRR+LPQ scheduling  
![](figure/en-us_image_0000001512831178.png)

[Figure 5](#EN-US_CONCEPT_0000001513150686__fig_qos_feature_04009) shows the scheduling process.

**Figure 5** PQ+WDRR+LPQ scheduling process  
![](figure/en-us_image_0000001513150698.png)

* Packets in PQ queues are preferentially scheduled, and packets in WDRR queues are scheduled only when no packets are buffered in PQ queues. When all PQ queues are empty, packets in WDRR queues start to be scheduled. If packets are then added to PQ queues, these packets are again scheduled preferentially.
* Packets in WDRR queues start to be scheduled only after all PQ queues are empty. During WDRR scheduling, PQ queues are scheduled preferentially if packets reach PQ queues.
* Packets in LPQ queues start to be scheduled only after all WDRR queues are empty.

Bandwidths are preferentially allocated to PQ queues to guarantee the peak information rate (PIR) of packets in those queues. The remaining bandwidth is allocated to WDRR queues based on the weight. If the bandwidth is not exhausted, the remaining bandwidth is allocated to WDRR queues whose PIRs are higher than the obtained bandwidth, until the PIRs of all WDRR queues are guaranteed. If any bandwidth resources remain at this time, they are allocated to LPQ queues.