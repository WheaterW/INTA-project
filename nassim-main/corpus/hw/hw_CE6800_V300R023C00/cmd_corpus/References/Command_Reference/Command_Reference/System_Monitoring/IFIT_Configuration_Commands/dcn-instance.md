dcn-instance
============

dcn-instance

Function
--------



The **dcn-instance** command creates a DCN instance and displays the DCN instance view, or displays the view of an existing DCN instance.

The **undo dcn-instance** command deletes a DCN instance.



By default, no DCN instance is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcn-instance**

**undo dcn-instance**


Parameters
----------

None

Views
-----

IFIT view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To use IFIT to monitor or measure traffic, run this command to enter a DCN instance view.


Example
-------

# Create a DCN instance and enter the DCN instance view.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance

```