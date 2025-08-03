ipv6 nd dad detect attempts
===========================

ipv6 nd dad detect attempts

Function
--------



The **ipv6 nd dad detect attempts** command configures a threshold for DAD to consider an address available in an address conflict self-recovery scenario.

The **undo ipv6 nd dad detect attempts** command restores the default configuration.



By default, the threshold for DAD to consider an address available in an address conflict self-recovery scenario is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd dad detect attempts** *attempts-value*

**undo ipv6 nd dad detect attempts** *attempts-value*

**undo ipv6 nd dad detect attempts**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *attempts-value* | Specifies a threshold for DAD to consider an address available in an address conflict self-recovery scenario. | The value is an integer ranging from 1 to 5. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If an address conflict occurs on an interface in an address conflict self-recovery scenario, DAD continues detection on the interface until the address conflict is removed. The device considers the address conflict removed when DAD does not receive conflict packets for a specified number of consecutive times. This number, referred to as the address conflict removal threshold, can be configured using the ipv6 nd dad detect attempts command. In this case, DAD considers the address available. Otherwise, DAD considers the address unavailable and continues detection.


Example
-------

# Set a threshold for DAD to consider an address available in an address conflict self-recovery scenario to 5.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd dad detect attempts 5

```