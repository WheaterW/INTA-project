ptp enable(system view)
=======================

ptp enable(system view)

Function
--------



The **ptp enable** command enables 1588v2 on a device.

The **undo ptp enable** command disables 1588v2 on a device.



1588v2 is disabled on a device by default.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp enable**

**undo ptp enable**


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

1588v2 is enabled in the system and interface views:

* Run the **ptp enable** command to enable 1588v2 on the device and then configure 1588v2 in the system view.
* Run the **ptp enable** command to enable 1588v2 on the interface and then configure 1588v2 in the interface view.


Example
-------

# Enable 1588v2 on a device.
```
<HUAWEI> system-view
[~HUAWEI] ptp enable

```