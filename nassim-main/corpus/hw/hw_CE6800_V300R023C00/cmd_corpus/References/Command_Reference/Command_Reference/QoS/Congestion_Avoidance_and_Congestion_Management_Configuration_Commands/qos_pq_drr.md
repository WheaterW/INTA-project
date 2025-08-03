qos pq drr
==========

qos pq drr

Function
--------



The **qos pq drr** command configures a scheduling mode for an interface queue.

The **undo qos pq drr** command restores the default scheduling mode for an interface queue.



By default, the scheduling mode of queues on an interface is PQ.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**qos** { **pq** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> | **drr** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> } \*

**undo qos** { **pq** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> | **drr** { *start-queue-index* [ **to** *end-queue-index* ] } &<1-8> } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pq** | Sets the scheduling mode to PQ. | - |
| *start-queue-index* | Start queue index. | The value is an integer that ranges from 0 to 7. |
| **to** *end-queue-index* | End queue index. | The value is an integer that ranges from 0 to 7. |
| **drr** | Sets the scheduling mode to WDRR and specifies the WDRR weight. | - |



Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When congestion occurs on a network, configure a combination of queue scheduling modes to adjust the delay and jitter of various service packets as follows:

* Packets of delay-sensitive services, such as the voice and video services, are processed preferentially.
* Among the delay-insensitive services, such as the email service, the packets with the same priority are processed equally and the packets with different priorities are processed based on their weights.The device supports PQ+DRR. When a combination of queue scheduling modes is used, the device first schedules the packets in queues using PQ scheduling. When all packets in the queues using PQ scheduling are sent out, the device schedules the packets in queues using DRR scheduling. Packets from the queues using PQ scheduling are scheduled based on packet priorities.

Example
-------

# Set the scheduling mode of queue 1 through queue 4 to WDRR.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos drr 1 to 4

```