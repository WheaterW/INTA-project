queue
=====

queue

Function
--------



The **queue** command configures a scheduling mode for an interface queue.

The **undo queue** command restores the default scheduling mode for an interface queue.



By default, an interface queue uses priority queuing PQ.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**queue** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> { **pq** | **lpq** | **drr** [ **weight** *weight-value* ] }

**undo queue** *start-queue-index* { **lpq** | **drr** **weight** *weight-value* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-queue-index* | Specifies queue-start value. | The value is an integer that ranges from 0 to 7 . |
| **to** *end-queue-index* | Specifies queue-end value.  end-queue-index must be larger than or equal to start-queue-index. start-queue-index and end-queue-index determine a range of queues. If end-queue-index is not specified, a scheduling mode is configured for the queue specified by start-queue-index. | The value is an integer that ranges from 0 to 7 . |
| **pq** | Sets the scheduling mode to PQ. | - |
| **lpq** | Sets the scheduling mode to LPQ. | - |
| **drr** | Sets the scheduling mode to DRR. | - |
| **weight** *weight-value* | Specifies the DRR weight. | The value is an integer that ranges from 1 to 100 . |



Views
-----

ETS view of the DCB


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

ETS supports two-level scheduling: scheduling based on priority groups and queues. ETS provides fine-grained QoS services.ETS uses the following scheduling modes for queues in priority groups:

* PQ schedulingPriority queuing (PQ) schedules packets in descending order of priority. Queues with lower priories are processed only after all the queues with higher priorities have been processed. By using PQ scheduling, the device puts packets of delay-sensitive key services into queues with higher priorities and packets of other services into queues with lower priorities so that packets of key services can be transmitted first. In PQ scheduling, if a lot of packets exist in queues with higher priorities when congestion occurs, packets in queues with lower priorities cannot be transmitted for a long time.
* DRR schedulingDeficit Round Robin (DRR) ensures that packets in all the queues are scheduled in turn.When eight output queues are configured on an interface, each queue is configured with a weight, namely, w7, w6, w5, w4, w3, w2, w1, and w0. The weight values represent the percentage of resources that the queues can obtain. In addition, DRR schedules packets based on the packet length. If the packet length is too long, DRR allows the negative weight value so that long packets can be scheduled. In the next round, the queue with the negative weight value is not scheduled until its weight value becomes positive. DRR offsets the disadvantages of PQ scheduling and DRR scheduling. (PQ scheduling can cause starvation of packets in queues with lower priorities, and DRR scheduling cannot allocate bandwidth evenly when the packet length in each queue is different or variable.) However, DRR has its own disadvantage. It cannot schedule delay-sensitive services such as voice services in a timely manner.
* LPQ schedulingLPQ scheduling applies to LPQ queues. The difference is that when congestion occurs, the PQ queue can preempt the bandwidth of the DRR queue whereas the LPQ queue cannot. After packets in the PQ and DRR queues are all scheduled, the remaining bandwidth can be assigned to packets in the LPQ queue.In the actual application, best effort (BE) flows can be put into the LPQ queue. When the network is overloaded, BE flows can be limited so that other services can be processed preferentially.
* PQ+DRR schedulingPQ and DRR have their own advantages and disadvantages. If only PQ scheduling is used, packets in queues with lower priorities cannot obtain bandwidth. If only DRR scheduling is used, delay-sensitive services, such as voice services, cannot be scheduled in a timely manner. PQ+DRR scheduling integrates the advantages of PQ scheduling and DRR scheduling and offsets their disadvantages. PQ+DRR scheduling puts protocol packets and packets of delay-sensitive services into the PQ queue, and allocates bandwidth to the PQ queue. Then, other packets are put into DRR queues based on their priorities. The DRR queues can be scheduled in a polling manner.

**Precautions**



For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ:The default scheduling mode of the CIR token bucket based on interface queues is DRR scheduling and the default rate limit is 0. The interface queueâbased scheduling mode configured for the CIR token bucket does not take effect. The configured scheduling mode takes effect only for the EIR (EIR = PIR â CIR) token bucket.




Example
-------

# Configure PQ for queue 5. Configure DRR for queues 6 and 7, and set the DRR weights to 30.
```
<HUAWEI> system-view
[~HUAWEI] dcb ets-profile myets
[*HUAWEI-ets-myets] queue 5 pq
[*HUAWEI-ets-myets] queue 6 7 drr weight 30

```