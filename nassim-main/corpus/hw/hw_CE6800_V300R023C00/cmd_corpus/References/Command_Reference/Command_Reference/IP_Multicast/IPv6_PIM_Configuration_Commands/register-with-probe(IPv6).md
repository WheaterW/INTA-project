register-with-probe(IPv6)
=========================

register-with-probe(IPv6)

Function
--------



The **register-with-probe** command disables the source's DR from sending Register messages. When the DR receives multicast traffic, only Probe messages are sent to RP.

The **undo register-with-probe** command restores the default configuration.



By default, when the source DR receives multicast traffic, it sends Register or Probe messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**register-with-probe**

**undo register-with-probe**


Parameters
----------

None

Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the source's DR receives multicast data, it sends Register messages to the RP, and add registered egress interface. If too many redundant Register messages are sent to RP, the performance is affected. Run the register-with-probe command to disable Register messages sending function on the source's DR, the DR sends Probe messages instead of Register messages, so that the performance is not affected.


Example
-------

# In the public network instance, configure the source DP to send Probe messages but not Register messages to the RP.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] register-with-probe

```