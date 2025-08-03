clock source ptp synchronization enable
=======================================

clock source ptp synchronization enable

Function
--------



The **clock source ptp synchronization enable** command enables clock synchronization for a PTP clock source.

The **undo clock source ptp synchronization enable** command disables clock synchronization for a PTP clock source.



By default, clock synchronization is disabled for a PTP clock source.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock source ptp synchronization enable**

**undo clock source ptp synchronization enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, clock synchronization is disabled for a PTP clock source. To enable a PTP clock source to participate in clock source selection, enable clock synchronization for this PTP clock source.


Example
-------

# Enable clock synchronization for a PTP clock source.
```
<HUAWEI> system-view
[~HUAWEI] clock source ptp synchronization enable

```