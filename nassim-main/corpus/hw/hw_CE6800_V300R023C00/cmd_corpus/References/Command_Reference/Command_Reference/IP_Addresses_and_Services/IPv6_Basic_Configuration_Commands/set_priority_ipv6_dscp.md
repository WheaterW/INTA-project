set priority ipv6 dscp
======================

set priority ipv6 dscp

Function
--------



The **set priority ipv6 dscp** command sets a priority for IPv6 protocol packets.

The **undo set priority ipv6 dscp** command deletes the priority of IPv6 protocol packets.



By default, the DSCP value is not configured for protocol packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**set priority ipv6 dscp** *dscp-value*

**undo set priority ipv6 dscp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dscp-value* | Specifies the DSCP value of protocol packets. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 63. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, each protocol has a default DSCP value. You can run this command to change the DSCP value of host protocol packets.

**Precautions**

The **set priority ipv6 dscp** command takes effect only for IPv6 packets to be sent to the CPU, but does not take effect for packets that are not sent to the CPU or non-IPv6 packets.Some protocols have the command for changing the DSCP value. If both the command for changing the DSCP value and the **set priority ipv6 dscp** command are configured, the DSCP value configured using the command for changing the DSCP value takes effect.


Example
-------

# Set the priority of IPv6 protocol packets to 44.
```
<HUAWEI> system-view
[~HUAWEI] set priority ipv6 dscp 44

```