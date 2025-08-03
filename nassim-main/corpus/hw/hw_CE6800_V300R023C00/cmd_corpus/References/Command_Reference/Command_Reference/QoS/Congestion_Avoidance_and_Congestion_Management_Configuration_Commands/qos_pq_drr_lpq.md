qos pq drr lpq
==============

qos pq drr lpq

Function
--------

The **qos pq drr lpq** command configures a scheduling mode for an interface queue.

The **undo qos pq drr lpq** command restores the default scheduling mode for an interface queue.

By default, the scheduling mode of queues on an interface is PQ.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos** { **pq** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> | **drr** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> | **lpq** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> } \*

**undo qos** { **pq** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> | **drr** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> | **lpq** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pq** | Sets the scheduling mode to PQ. | - |
| *start-queue-index* | Start queue index. | The value is an integer that ranges from 0 to 7. |
| **to** *end-queue-index* | End queue index. | The value is an integer that ranges from 0 to 7. |
| **drr** | Sets the scheduling mode to WDRR and specifies the WDRR weight. | - |
| **lpq** | Sets the scheduling mode to LPQ. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When congestion occurs on a network, configure a combination of queue scheduling modes to adjust the delay and jitter of various service packets as follows:

* Packets of delay-sensitive services, such as the voice and video services, are processed preferentially.
* Among the delay-insensitive services, such as the email service, the packets with the same priority are processed equally and the packets with different priorities are processed based on their weights.
  
  The device supports PQ+WDRR+LPQ. When a combination of queue scheduling modes is used, the device first schedules the packets in queues using PQ scheduling. When all packets in the queues using PQ scheduling are sent out, the device schedules the packets in queues using WDRR scheduling. When all packets in the queues using WDRR scheduling are sent out, the device schedules the packets in queues using LPQ scheduling. Packets from the queues using PQ or LPQ scheduling are scheduled based on packet priorities.

**Precautions**

For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ series, SP scheduling is used for the CIR token bucket by default. The user-configured scheduling mode takes effect only on the EIR token bucket. To achieve the scheduling effect similar to the effect of DRR scheduling if the bandwidth of services is not guaranteed, you can run the qos queue queue-index shaping cir 64 kbps pir < port bandwidth > gbps command to minimize the rate limit of the CIR token bucket.


Example
-------

# Set the scheduling mode of queue 1 through queue 4 to WDRR.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos drr 1 to 4
```