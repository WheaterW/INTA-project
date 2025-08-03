ptp domain
==========

ptp domain

Function
--------



The **ptp domain** command specifies the clock domain in which a 1588v2 device resides.

The **undo ptp domain** command restores the default clock domain.



By default, a 1588v2 device resides in clock domain 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp domain** *domain-value*

**undo ptp domain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-value* | Specifies the value of a 1588v2 clock domain. | In 1588v2 mode, the value is an integer ranging from 0 to 255. The default value is 0. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A 1588v2 network can be logically divided into multiple clock domains. Each clock domain has a single clock source, all 1588v2 devices in the clock domain synchronize clock signals with this clock source, and each 1588v2 device in the clock domain focuses only on the 1588v2 messages exchanged within this clock domain.


Example
-------

# Set domain-value to 4.
```
<HUAWEI> system-view
[~HUAWEI] ptp domain 4

```