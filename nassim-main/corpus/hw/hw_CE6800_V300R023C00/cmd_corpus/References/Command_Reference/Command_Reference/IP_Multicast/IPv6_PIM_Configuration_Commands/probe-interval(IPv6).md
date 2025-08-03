probe-interval(IPv6)
====================

probe-interval(IPv6)

Function
--------



The **probe-interval** command sets an interval at which Probe messages (null Register message) are sent to the rendezvous point (RP).

The **undo probe-interval** command restores the default value.



By default, Probe messages are sent to the RP at an interval of 5 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**probe-interval** *interval*

**undo probe-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which Probe messages are sent to the RP. | The value is an integer ranging from 1 to 1799, in seconds. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After receiving a Register-Stop message, the source's designated router (DR) stops sending Register messages and enters the register suppression state. During register suppression, the source's DR sends Probe messages to notify the RP that the multicast source is still in the Active state. After register suppression times out, the source's DR starts to send Register messages. To set the interval at which Probe messages are sent to the RP, run the probe-interval command.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the public network instance view.

**Configuration Impact**

If the probe-interval command is run several times, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 6 seconds as the interval at which Probe messages are sent to the RP.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] probe-interval 6

```