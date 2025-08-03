ptp announce-interval
=====================

ptp announce-interval

Function
--------

The **ptp announce-interval** command sets the interval at which a 1588v2 interface sends Announce messages.

The **undo ptp announce-interval** command restores the default interval.

By default, the interval at which a 1588v2 interface sends Announce messages is 128/1024s.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp announce-interval** *announce-interval*

**undo ptp announce-interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *announce-interval* | Specifies the interval at which Announce packets are sent. | In 1588v2 mode, the value is an integer ranging from 0 to 20. The default value is 7, which is 128/1024s.The mapping between announce-interval values and actual intervals is as follows:   * 0 1/1024s * 1 2/1024s * 2 4/1024s * 3 8/1024s * 4 16/1024s * 5 32/1024s * 6 64/1024s * 7 128/1024s * 8 256/1024s * 9 512/1024s * 10 1s * 11 2s * 12 4s * 13 8s * 14 16s * 15 32s * 16 64s * 17 128s * 18 256s * 19 512s * 20 1024s |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Two 1588v2 devices exchange Announce messages to determine the master-slave hierarchy. The master device sends Sync messages to notify the slave device of time signal parameters and uses a delay measurement mechanism to achieve time signal accuracy.

**Precautions**

If devices exchange 1588v2 messages frequently and consume a lot of bandwidth resources, increase the announce-interval value. If time synchronization accuracy is low, reduce the announce-interval value. If required time synchronization accuracy is guaranteed, set announce-interval to a larger value.

Remote timeout period of receiving Announce messages = Remotely configured receipt-timeout x Locally configured announce-intervalThe
**ptp announce receipt-timeout receipt-timeout** command sets the maximum number of Announce message receiving timeouts on a 1588v2 interface.

Example
-------

# Set the interval at which
100GE
1/0/1 sends Announce messages to 256/1024s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp announce-interval 8

```