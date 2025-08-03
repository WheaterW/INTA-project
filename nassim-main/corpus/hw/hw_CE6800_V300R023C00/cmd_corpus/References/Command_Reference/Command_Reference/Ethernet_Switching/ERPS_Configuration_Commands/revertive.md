revertive
=========

revertive

Function
--------



The **revertive** command sets revertive switching or non-revertive switching for an ERPS ring.

The **undo revertive disable** command restores the default configuration.



By default, ERPS rings use revertive switching.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**revertive** { **disable** | **enable** }

**undo revertive disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables revertive switching, which means non-revertive switching is used for an ERPS ring. | - |
| **enable** | Enables revertive switching for an ERPS ring. | - |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After link faults are rectified, whether to re-block the ring protection link (RPL) owner port depends on the switching mode.

* In revertive switching, the RPL owner port is re-blocked after the WTR timer expires, and the traffic channel is blocked on the RPL.
* In non-revertive switching, the WTR timer is not started, and the traffic channel continues to use the RPL.

Example
-------

# Set non-revertive switching for ERPS ring 5.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 5
[*HUAWEI-erps-ring5] version v2
[*HUAWEI-erps-ring5] revertive disable

```