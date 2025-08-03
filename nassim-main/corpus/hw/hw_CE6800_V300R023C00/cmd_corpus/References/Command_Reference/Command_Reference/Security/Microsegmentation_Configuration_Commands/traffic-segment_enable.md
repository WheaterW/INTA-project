traffic-segment enable
======================

traffic-segment enable

Function
--------



The **traffic-segment enable** command enables microsegmentation.

The **undo traffic-segment enable** command disables microsegmentation.



By default, microsegmentation is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**traffic-segment enable**

**undo traffic-segment enable**


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

**Usage Scenario**

To enable microsegmentation, run the **traffic-segment enable** command.

**Precautions**

The traffic-segment enable and **remark vxlan reserved-value** commands cannot be used together on the same device.The traffic-segment enable and **inof** commands cannot be configured on the same device at the same time.The traffic-segment enable and **npcc enable** commands cannot be configured on the same device at the same time.The traffic-segment enable and **ipv6 npcc enable** commands cannot be used together on the same device.


Example
-------

# Enable microsegmentation.
```
<HUAWEI> system-view
[~HUAWEI] traffic-segment enable

```