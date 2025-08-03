hello-option holdtime (IPv6)
============================

hello-option holdtime (IPv6)

Function
--------



The **hello-option holdtime** command sets the neighbor timeout period carried in PIM Hello packets to be sent by a router.

The **undo hello-option holdtime** command restores the default value.



By default, the neighbor timeout period carried in PIM Hello packets to be sent by a router is 105s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**hello-option holdtime** *holdtimeValue*

**undo hello-option holdtime**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *holdtimeValue* | Specifies the neighbor timeout period carried in PIM Hello messages to be sent. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to set the neighbor timeout period carried in PIM Hello packets to be sent by a router. If the receive end does not receive any Hello packet from the local device within the timeout period, the receive end considers that the local neighbor is aged. If routers need to quickly detect PIM neighbor changes, set this parameter to a smaller value, but the value must be greater than the configured interval for sending Hello messages. The **timer hello** or **pim ipv6 timer hello** command can be used to set the interval at which a PIM neighbor sends Hello messages.Set a proper interval value based on the configuration of the **timer hello** or **pim ipv6 timer hello** command configured on PIM neighbors.


Example
-------

# In the public network instance, set the neighbor timeout period carried in PIM Hello packets to be sent by the router to 120 seconds.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] hello-option holdtime 120

```