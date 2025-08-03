ptp sync-interval
=================

ptp sync-interval

Function
--------

The **ptp sync-interval** command sets the interval at which a 1588v2 interface sends Sync messages.

The **undo ptp sync-interval** command restores the default interval at which a 1588v2 interface sends Sync messages.

By default, the interval at which a 1588v2 interface sends Sync messages is 8/1024s.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp sync-interval** *sync-interval*

**undo ptp sync-interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sync-interval** *sync-interval* | Sets the interval at which a 1588v2 interface sends Sync packets. | The value is an integer ranging from 0 to 20. In 1588v2 mode, the default value is 3, namely, 8/1024s. The mapping between sync-interval values and actual intervals is as follows:   * 0 1/1024s * 1 2/1024s * 2 4/1024s * 3 8/1024s * 4 16/1024s * 5 32/1024s * 6 64/1024s * 7 128/1024s * 8 256/1024s * 9 512/1024s * 10 1s * 11 2s * 12 4s * 13 8s * 14 16s * 15 32s * 16 64s * 17 128s * 18 256s * 19 512s * 20 1024s |




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

The master interface periodically sends multicast Sync messages. If sync-interval is set to a small value, 1588v2 devices frequently exchange Sync messages, occupying many bandwidth resources. If sync-interval is set to a large value, required time synchronization accuracy cannot be guaranteed. Therefore, if required time synchronization accuracy is guaranteed, set sync-interval to a larger value.

**Prerequisites**

1588v2 has been enabled on an interface using the ptp enable (interface view) command.

**Precautions**

The value of sync-interval in this command does not indicate the actual time. For the mapping between the value of sync-interval and the actual time, see the parameter description.

The time when the Sync packets can be stamped into the Sync packets if the one-step timestamping mode is used or into Follow\_Up packets if the two-step timestamping mode is used. To specify a timestamping mode, run the ptp clock-step { one-step | two-step } command.

Example
-------

# Set the interval at which
100GE
1/0/1 sends Sync messages to 128/1024s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp sync-interval 7

```