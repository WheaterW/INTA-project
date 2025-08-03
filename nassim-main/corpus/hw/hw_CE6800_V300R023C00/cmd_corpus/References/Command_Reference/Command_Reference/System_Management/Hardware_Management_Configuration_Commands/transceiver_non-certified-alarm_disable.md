transceiver non-certified-alarm disable
=======================================

transceiver non-certified-alarm disable

Function
--------



The **transceiver non-certified-alarm disable** command disables the alarm function for non-Huawei-certified optical modules.

The **undo transceiver non-certified-alarm disable** command enables the alarm function for non-Huawei-certified optical modules.



By default, the alarm function is enabled for non-Huawei-certified optical modules.


Format
------

**transceiver non-certified-alarm disable**

**undo transceiver non-certified-alarm disable**


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

If non-Huawei-certified optical modules are used on devices, the devices will generate a large number of alarms to prompt users to replace these optical modules with Huawei-certified ones. This facilitates optical module management and maintenance. To shield these alarms, disable the alarm function for non-Huawei-certified optical modules.


Example
-------

# Disable the alarm function for non-Huawei-certified optical modules.
```
<HUAWEI> system-view
[~HUAWEI] transceiver non-certified-alarm disable

```