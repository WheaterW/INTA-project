clock freq-deviation-detect
===========================

clock freq-deviation-detect

Function
--------



The **clock freq-deviation-detect enable** command enables frequency deviation detection for clock signals.

The **undo clock freq-deviation-detect enable** command disables frequency deviation detection for clock signals.



By default, frequency deviation detection is disabled for clock signals.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock freq-deviation-detect enable**

**undo clock freq-deviation-detect enable**


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

If a clock synchronization network has higher requirements for the frequency deviation of clock signals, enable frequency deviation detection. When frequency deviation detection is enabled, the device performs frequency deviation detection for clock signals. If a detected frequency deviation exceeds a normal range, the clock source is unreliable. In this situation, the device may automatically reselect a clock source.


Example
-------

# Enable frequency deviation detection for clock signals.
```
<HUAWEI> system-view
[~HUAWEI] clock freq-deviation-detect enable

```