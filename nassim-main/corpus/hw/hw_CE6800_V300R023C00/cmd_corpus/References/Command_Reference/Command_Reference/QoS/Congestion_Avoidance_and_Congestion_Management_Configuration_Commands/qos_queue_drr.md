qos queue drr
=============

qos queue drr

Function
--------



The **qos queue drr** command sets the WDRR weight of queues that participate in WDRR scheduling.

The **undo qos queue drr** command restores the default WDRR weight of queues that participate in WDRR scheduling.



The default WDRR weight of queues that participate in DRR scheduling is 1.


Format
------

**qos queue** *queue-index* **drr** **weight** *weight-value*

**undo qos queue** *queue-index* **drr** **weight**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **weight** *weight-value* | Specifies a WDRR weight. | The value is an integer that ranges from 1 to 100. |
| **queue** *queue-index* | Specifies the index of a queue. | The value is an integer that ranges from 0 to 7. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

WDRR schedules packets based on the packet length used as the weight. If the packet length is too long, WDRR allows the negative weight value so that long packets can be scheduled. In the next round, the queue with the negative weight value is not scheduled until its weight value becomes positive.WDRR offsets the disadvantages of PQ scheduling. That is, in PQ scheduling, packets in queues with lower priorities cannot be scheduled for a long time.When WDRR scheduling is used, set the weight for each queue. The device schedules queues in turn according to the weights.

**Precautions**

* If you need to set the same WDRR weight on multiple interfaces, you can perform the configuration on a port group to reduce the workload.
* For the CE8855-32CQ4BQ, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-LL, CE6885-48YS8CQ, CE6885-48YS8CQ-T, CE6863E-48S8CQ, and CE6885-SAN-56F, SP scheduling is used for the CIR token bucket by default. The user-configured scheduling mode takes effect only on the EIR token bucket.


Example
-------

# Set the WDRR weight of queue 4 on the specified interface to 9.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos drr 4
[*HUAWEI-100GE1/0/1] qos queue 4 drr weight 9

```