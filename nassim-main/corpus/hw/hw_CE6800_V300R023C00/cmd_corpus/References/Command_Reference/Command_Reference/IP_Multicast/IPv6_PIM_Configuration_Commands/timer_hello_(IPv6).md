timer hello (IPv6)
==================

timer hello (IPv6)

Function
--------



The **timer hello** command sets the interval for all PIM interfaces to send Hello messages.

The **undo timer hello** command restores the default value.



By default, IPv6 PIM interfaces send Hello messages at an interval of 30 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**timer hello** *helloInterval*

**undo timer hello**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *helloInterval* | Specifies the interval at which IPv6 PIM interfaces send Hello messages. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A Router on an IPv6 PIM-SM network needs to send Hello messages periodically to maintain PIM neighbor relationships. To set the interval at which IPv6 PIM interfaces send Hello messages, run the timer hello command. To have a Router rapidly sense IPv6 PIM neighbor changes, set a Hello packet sending interval smaller than the configured neighbor timeout period.


Example
-------

# In the public network instance, specify 40 seconds as the interval at which IPv6 PIM interfaces send Hello messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] timer hello 40

```