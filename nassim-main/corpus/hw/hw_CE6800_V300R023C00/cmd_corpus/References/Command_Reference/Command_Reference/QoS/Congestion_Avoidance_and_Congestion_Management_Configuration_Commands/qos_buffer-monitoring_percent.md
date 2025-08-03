qos buffer-monitoring percent
=============================

qos buffer-monitoring percent

Function
--------



The **qos buffer-monitoring percent** command configures upper and lower buffer thresholds of queues.

The **undo qos buffer-monitoring percent** command restores the default upper and lower buffer thresholds of queues.



By default, the lower buffer threshold is 10% of the queue buffer space and the upper buffer threshold is 90% of the queue buffer space.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos** [ **queue** *queue-index* ] **buffer-monitoring** **percent** **low** *low-percent* **high** *high-percent*

**undo qos** [ **queue** *queue-index* ] **buffer-monitoring** **percent** [ **low** *low-percent* **high** *high-percent* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **queue** *queue-index* | Specifies the index of a queue. | The value is an integer that ranges from 0 to 7. |
| **low** *low-percent* | Specifies the lower buffer threshold. | The value is an integer that ranges from 0 to 99.The default value is 10. |
| **high** *high-percent* | Specifies the upper buffer threshold. | The value is an integer that ranges from low-percent to 100.The default is 90. |



Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In the congestion analysis scenario, when the buffer usage of a queue reaches the upper buffer threshold and then falls below the lower buffer threshold, the device saves read historical congestion monitoring information so that you can learn the buffer usage of the queue.


Example
-------

# Set the lower and upper buffer thresholds of queue 4 on 100GE1/0/1 to 20% and 70%, respectively.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos queue 4 buffer-monitoring percent low 20 high 70

```