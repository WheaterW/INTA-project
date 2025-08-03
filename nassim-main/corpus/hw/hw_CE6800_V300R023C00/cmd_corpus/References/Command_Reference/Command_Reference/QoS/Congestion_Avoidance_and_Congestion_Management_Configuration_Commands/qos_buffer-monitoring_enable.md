qos buffer-monitoring enable
============================

qos buffer-monitoring enable

Function
--------



The **qos buffer-monitoring enable** command enables queue-based congestion monitoring.

The **undo qos buffer-monitoring enable** command disables queue-based congestion monitoring.



By default, queue-based congestion monitoring is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos** [ **queue** *queue-index* ] **buffer-monitoring** **enable**

**undo qos** [ **queue** *queue-index* ] **buffer-monitoring** **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **queue** *queue-index* | Specifies the index of a queue. | The value is an integer that ranges from 0 to 7. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Congestion mainly affects network performance and results in problems such as transmission delay and signal loss. Congestion monitoring and analysis of each interface queue on a network device help you to learn the buffer usage of each queue and information about packets that cause congestion, providing guidance to planning and adjusting network traffic.


Example
-------

# Enable congestion monitoring of queue 4 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos queue 4 buffer-monitoring enable

```