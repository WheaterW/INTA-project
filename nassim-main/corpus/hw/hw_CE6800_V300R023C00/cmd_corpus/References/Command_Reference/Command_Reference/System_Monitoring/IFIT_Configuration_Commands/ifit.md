ifit
====

ifit

Function
--------



The **ifit** command creates and displays an IFIT view, or displays an existing IFIT view.

The **undo ifit** command deletes the created IFIT view.



By default, no IFIT view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ifit**

**undo ifit**


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

To use IFIT to monitor or measure traffic, you can run this command to enter the IFIT view.

**Precautions**

Before enabling IFIT, you need to enable NTP synchronization, NTP high-precision synchronization, or 1588 synchronization.The IFIT service and the large MAC address table mode are mutually exclusive.


Example
-------

# Create and enter the IFIT view.
```
<HUAWEI> system-view
[~HUAWEI] ifit

```