alarm disable (warranty view)
=============================

alarm disable (warranty view)

Function
--------



The **alarm disable** command disables the alarm function for the digital warranty.

The undo alarm disable command enables the alarm function for the digital warranty.



By default, the alarm function of a warranty is enabled.


Format
------

**alarm disable**

**undo alarm disable**


Parameters
----------

None

Views
-----

warranty view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

By default, the alarm function of a warranty is enabled on a device. Manually disable the alarm function if it is required. If you disable the alarm function, the reported alarms are cleared.


Example
-------

# Enable the alarm function for the digital warranty.
```
<HUAWEI> system-view
[~HUAWEI] warranty
[~HUAWEI-warranty] undo alarm disable

```

# Disable the alarm function for the digital warranty.
```
<HUAWEI> system-view
[~HUAWEI] warranty
[~HUAWEI-warranty] alarm disable

```