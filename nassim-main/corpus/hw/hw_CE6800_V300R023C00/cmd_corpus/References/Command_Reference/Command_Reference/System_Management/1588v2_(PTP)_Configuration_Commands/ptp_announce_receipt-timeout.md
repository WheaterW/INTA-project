ptp announce receipt-timeout
============================

ptp announce receipt-timeout

Function
--------

The **ptp announce receipt-timeout** command sets the maximum number of Announce message receiving timeouts on a 1588v2 interface.

The **undo ptp announce receipt-timeout** command restores the default maximum number of Announce message receiving timeouts on a 1588v2 interface.

By default, the maximum number of Announce message receiving timeouts on a 1588v2 interface is 3.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp announce receipt-timeout** *receipt-timeout*

**undo ptp announce receipt-timeout**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **receipt-timeout** *receipt-timeout* | Specifies the maximum number of Announce message receiving timeouts on a 1588v2 interface. | In 1588v2 mode, the value is an integer ranging from 2 to 255, and the default value is 3. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

Two 1588v2 devices exchange Announce messages to determine the master-slave hierarchy. The master device sends Sync messages to notify the slave device of time signal parameters and uses a delay measurement mechanism to achieve time signal accuracy.To set the maximum number of Announce message receiving timeouts on a 1588v2 interface, run the ptp announce receipt-timeout command. If the number of Announce message receiving timeouts on a 1588v2 interface exceeds the configured receipt-timeout value, the local device sets the 1588v2 interface status to Master, does not synchronize the time with other 1588v2 devices, and uses the BMC algorithm to select a clock source for time synchronization. To prevent frequent clock source switching resulting from Announce message receiving timeouts, set receipt-timeout to a larger value. To switch clock sources in time, set receipt-timeout to a smaller value. In most cases, the default value is recommended.

**Precautions**

The following formula applies:

Local timeout period of receiving Announce messages = Locally configured receipt-timeout x Remotely configured announce-intervalThe
**ptp announce-interval announce-interval** command sets the interval at which Announce messages are sent.

Example
-------

# Set the maximum number of Announce message receiving timeouts on
100GE
1/0/1 of a 1588v2 device to 4.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp announce receipt-timeout 4

```