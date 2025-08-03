measure enable
==============

measure enable

Function
--------



The **measure enable** command enables the statistics counters of an instance bound to a performance statistics task.

The **undo measure enable** command disables the statistics counters of an instance bound to a performance statistics task.



By default, all statistics counters of the instance bound to a performance statistics task are enabled.


Format
------

**measure enable instance-type** *instance-type* **measure** *measure-name*

**undo measure enable instance-type** *instance-type* **measure** *measure-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance-type** *instance-type* | Specifies the type of an instance bound to a performance statistics task. The instance type is predefined in a specific feature. Each instance type maps a feature. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |
| *measure-name* | Specifies the name of a statistics counter in a performance statistics task. Each statistics counter is predefined in a specific feature. | The value is a string of 1 to 63 case-insensitive characters, spaces not supported. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After you run the **binding instance-type instance** command to bind a statistics instance to a performance statistics task, run the **measure disable instance-type** command to disable all the statistics counters of this instance if the performance statistics task is no longer required. To enable one or more statistics counters of an instance bound to the performance statistics task, run the measure enable command.

**Prerequisites**

Before running this command, run the **binding instance-type instance** command to bind an instance to the performance statistics task and then the **measure disable instance-type** command to disable all the statistics counters of this instance.


Example
-------

# Enable statistics counter memory-usage of the card instance bound to the performance statistics task named huawei.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics enable
[*HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] binding instance-type card instance master
[*HUAWEI-pm-statistics-huawei] measure enable instance-type card measure memory-usage

```