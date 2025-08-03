reset qos headroom-usage
========================

reset qos headroom-usage

Function
--------



The **reset qos headroom-usage** command clears headroom buffer usage statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset qos headroom-usage** [ **slot** *slot-id* | **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters without spaces. |
| **interface** | Specifies an interface. | - |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before checking the headroom buffer usage of a device or a card or interface of the device in a specified period, you can run this command to clear headroom buffer usage statistics of the device, card, or interface. Then, run the **display qos headroom-usage** command to check the headroom buffer usage within the corresponding scope.

**Precautions**

Headroom buffer usage statistics cannot be restored after being cleared. Exercise caution when running this command.


Example
-------

# Clear headroom buffer usage statistics on 100GE1/0/1.
```
<HUAWEI> reset qos headroom-usage interface 100GE 1/0/1

```