startup checkpoint auto-save disable
====================================

startup checkpoint auto-save disable

Function
--------



The **undo startup checkpoint auto-save disable** command enables the function of automatically creating a checkpoint.

The **startup checkpoint auto-save disable** command disables the function of automatically creating a checkpoint.



The function of automatically creating a checkpoint is enabled by default.


Format
------

**startup checkpoint auto-save disable**

**undo startup checkpoint auto-save disable**


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

When a system software package or a feature package needs to be specified for next startup or a feature package needs to be updated online, to enable the function of automatically creating a checkpoint, run the undo startup checkpoint auto-save disable command.To disable the function of automatically creating a checkpoint, run the startup checkpoint auto-save disable command.


Example
-------

# Enable the function of automatically creating a checkpoint.
```
<HUAWEI> system-view
[~HUAWEI] undo startup checkpoint auto-save disable

```

# Disable the function of automatically creating a checkpoint.
```
<HUAWEI> system-view
[~HUAWEI] startup checkpoint auto-save disable

```