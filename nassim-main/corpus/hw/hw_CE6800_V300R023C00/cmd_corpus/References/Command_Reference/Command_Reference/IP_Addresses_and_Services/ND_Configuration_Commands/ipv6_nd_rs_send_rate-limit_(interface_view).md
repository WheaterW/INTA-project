ipv6 nd rs send rate-limit (interface view)
===========================================

ipv6 nd rs send rate-limit (interface view)

Function
--------



The **ipv6 nd rs send rate-limit** command configures a rate limit for sending ND RS messages on an interface, that is, the maximum number of ND RS messages that can be sent per second.

The **undo ipv6 nd rs send rate-limit** command restores the default configuration.



By default, the rate limit for sending ND RS messages is not configured on an interface, and ND RS messages are sent at a globally configured rate limit.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd rs send rate-limit** *rate-limit*

**undo ipv6 nd rs send rate-limit** *rate-limit*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rate-limit** *rate-limit* | Specifies a rate limit for sending ND RS messages on an interface. | The value is an integer, in messages/second. The value ranges from 1 to 1000. |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a device is attacked, it receives a large number of messages within a short period of time. As a result, the CPU resources of the device are greatly consumed, affecting the processing of other services. To solve this problem, you can set a rate limit for sending ND RS messages on a specified interface. The device then counts the number of ND RS messages sent on the interface in a specified period. If the number of ND RS messages exceeds the configured rate limit, the device delays scheduling or ignores excess ND RS messages.


Example
-------

# Set a rate limit for sending RS messages to 550 messages/second.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[~HUAWEI-Eth-Trunk1] undo portswitch
[~HUAWEI-Eth-Trunk1] ipv6 enable
[*HUAWEI-Eth-Trunk1] ipv6 nd rs send rate-limit 550

```