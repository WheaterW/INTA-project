delay-measure(IFIT traffic-behavior view)
=========================================

delay-measure(IFIT traffic-behavior view)

Function
--------



The **delay-measure enable** command enables delay measurement.

The **undo delay-measure enable** command disables delay measurement.



By default, IFIT delay measurement is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**delay-measure enable**

**undo delay-measure enable**


Parameters
----------

None

Views
-----

IFIT traffic-behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, delay measurement is disabled. To disable delay measurement for IFIT flows, run the undo delay-measure enable command.

**Precautions**

This parameter controls only the common delay but not the per-packet delay.


Example
-------

# Disable IFIT delay measurement.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic behavior huawei
[*HUAWEI-ifit-dcn-instance-behavior-huawei] undo delay-measure enable

```