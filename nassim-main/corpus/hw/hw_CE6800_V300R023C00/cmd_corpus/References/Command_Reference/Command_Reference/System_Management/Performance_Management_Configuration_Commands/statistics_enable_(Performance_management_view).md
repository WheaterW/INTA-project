statistics enable (Performance management view)
===============================================

statistics enable (Performance management view)

Function
--------



The **statistics enable** command enables the performance statistics function.

The **undo statistics enable** command disables the performance statistics function.



By default, the performance statistics function is disabled.


Format
------

**statistics enable**

**undo statistics enable**


Parameters
----------

None

Views
-----

Performance management view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To collect performance statistics, run the statistics enable command to enable the performance statistics function.

**Precautions**

After the **undo statistics enable** command is run, the performance statistics task that is running will be stopped. Therefore, exercise caution when you run this command.


Example
-------

# Enable the performance statistics function.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics enable

```

# Disable the performance statistics function.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] undo statistics enable
Warning: This operation will stop all statistics tasks. Continue? [Y/N]:y

```