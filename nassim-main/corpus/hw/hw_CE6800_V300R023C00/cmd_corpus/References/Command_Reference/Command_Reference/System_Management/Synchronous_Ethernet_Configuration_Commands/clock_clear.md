clock clear
===========

clock clear

Function
--------



The **clock clear** command clears the manual or forcible clock source selection mode and restores the default automatic clock source selection mode.



By default, the automatic clock source selection mode is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock clear**


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

The device supports three clock source selection modes: automatic clock source selection, manual clock source selection, and forcible clock source selection. The default clock source selection mode is automatic clock source selection.If you have configured the manual or forcible clock source selection mode, run this command to restore the default automatic clock source selection mode.

**Configuration Impact**

The **clock clear** command configuration is not saved in the configuration file. After the device is restarted, the **clock clear** command configuration is not restored, and the system uses the default automatic clock source selection mode. After the device is upgraded to this version from an earlier version, the **clock clear** command run in the earlier version no longer takes effect, and the system uses the default automatic clock source selection mode.


Example
-------

# Restore the default automatic clock source selection mode.
```
<HUAWEI> system-view
[~HUAWEI] clock clear

```