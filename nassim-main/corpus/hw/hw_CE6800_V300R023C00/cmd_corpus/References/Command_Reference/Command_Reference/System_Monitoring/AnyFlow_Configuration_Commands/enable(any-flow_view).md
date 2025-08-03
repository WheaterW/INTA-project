enable(any-flow view)
=====================

enable(any-flow view)

Function
--------



The **enable** command enables the AnyFlow function.

The **undo enable** command disables the AnyFlow function.



By default, the AnyFlow function is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**enable**

**undo enable**


Parameters
----------

None

Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the AnyFlow function is enabled on a device, the device will create flow entries for TCP/UDP/VXLAN traffic entering it based on fields such as 5-tuple to collect traffic statistics and detect abnormal traffic.


Example
-------

# Enable the AnyFlow function.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] enable

```