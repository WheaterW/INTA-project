configuration checkpoint auto-save disable
==========================================

configuration checkpoint auto-save disable

Function
--------



The **configuration checkpoint auto-save disable** command disables a device from automatically generating a configuration rollback point.

The **undo configuration checkpoint auto-save disable** command enables a device to automatically generate a configuration rollback point.



By default, a device is enabled to automatically generate a configuration rollback point.


Format
------

**configuration checkpoint auto-save disable**

**undo configuration checkpoint auto-save disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After configurations are committed on a device, the device automatically generates a configuration rollback point and allocates an ID to identify the rollback point. If you find that configurations are incorrect or a fault caused by configurations affects network running, you can roll the configurations back to a specified configuration rollback point in batches.If you run the **configuration checkpoint auto-save disable** command and then the **commit** command, no configuration rollback point is automatically generated. However, if you run the **undo configuration checkpoint auto-save disable** command and then the **commit** command, a configuration rollback point is automatically generated.


Example
-------

# Disable a device from automatically generating a configuration rollback point.
```
<HUAWEI> system-view
[~HUAWEI] configuration checkpoint auto-save disable

```