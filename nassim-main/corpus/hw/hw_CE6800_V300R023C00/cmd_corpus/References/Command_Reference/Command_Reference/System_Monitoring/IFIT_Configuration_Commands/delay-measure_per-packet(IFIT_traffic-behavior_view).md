delay-measure per-packet(IFIT traffic-behavior view)
====================================================

delay-measure per-packet(IFIT traffic-behavior view)

Function
--------



The **delay-measure per-packet enable** command enables per-packet delay measurement.

The **undo delay-measure per-packet enable** command disables per-packet delay measurement.



By default, per-packet delay measurement is disabled for IFIT.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**delay-measure per-packet enable**

**undo delay-measure per-packet enable**


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

To measure per-packet delay, run this command.


Example
-------

# Enable per-packet delay measurement for IFIT.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic behavior huawei
[*HUAWEI-ifit-dcn-instance-behavior-huawei] delay-measure per-packet enable

```