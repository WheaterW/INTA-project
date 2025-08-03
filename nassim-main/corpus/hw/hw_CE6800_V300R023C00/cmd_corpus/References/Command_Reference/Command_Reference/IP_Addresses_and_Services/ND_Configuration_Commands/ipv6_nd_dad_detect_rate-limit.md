ipv6 nd dad detect rate-limit
=============================

ipv6 nd dad detect rate-limit

Function
--------



The **ipv6 nd dad detect rate-limit** command configures a limit on the rate at which NS messages are sent for DAD to continue detection in an address conflict self-recovery scenario.

The **undo ipv6 nd dad detect rate-limit** command restores the default configuration.



By default, the limit on the rate at which NS messages are sent for DAD to continue detection in an address conflict self-recovery scenario is 50 messages per second.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd dad detect rate-limit** *rate-value*

**undo ipv6 nd dad detect rate-limit** *rate-value*

**undo ipv6 nd dad detect rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rate-value* | Specifies a limit on the rate at which NS messages are sent for DAD to continue detection in an address conflict self-recovery scenario. | The value is an integer ranging from 1 to 100, in messages per second. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When DAD detects a conflict, the IPv6 protocol status of the interface remains Down, and the interface can go Up only after manual intervention. To address this issue, deploy address conflict self-recovery. After detecting an IPv6 address conflict, DAD continues detection until the conflict is removed and the IPv6 protocol status of the interface becomes up. By default, address conflict self-recovery is enabled, and the limit on the rate at which NS messages are sent for DAD to continue detection is 50 messages per second. To adjust this limit, run the ipv6 nd dad detect rate-limit command.


Example
-------

# Set a limit on the rate at which NS messages are sent for DAD to continue detection in an address conflict self-recovery scenario to 100 messages per second.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd dad detect rate-limit 100

```