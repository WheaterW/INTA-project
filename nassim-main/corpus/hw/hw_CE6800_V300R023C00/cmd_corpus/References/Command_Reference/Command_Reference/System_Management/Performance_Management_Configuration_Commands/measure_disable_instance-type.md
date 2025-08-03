measure disable instance-type
=============================

measure disable instance-type

Function
--------



The **measure disable instance-type** command disables statistics counters of the instance bound to a performance statistics task.

The **undo measure disable instance-type** command restores the default configuration.



By default, all statistics counters of the instance bound to a performance statistics task are enabled.


Format
------

**measure disable instance-type** *pmoTypeName* *all*

**measure disable instance-type** *pmoTypeName* *measure* { *measureName* }

**undo measure disable instance-type** *pmoTypeName* *all*

**undo measure disable instance-type** *pmoTypeName* *measure* { *measureName* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *all* | Specifies statistics counters of statistics objects in all performance statistics tasks. | all |
| *measure* | Specifies the statistics counter in a performance statistics task. | measure |
| **instance-type** *pmoTypeName* | Specifies the type of an instance bound to a performance statistics task. The instance type is predefined in each feature. Each instance type is defined in a feature. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *measureName* | Specifies the name of a statistics counter in a performance statistics task. Each statistics counter is predefined in a specific feature. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To disable one or more statistics counters of the instance bound to a performance statistics task, run the measure disable command.

**Prerequisites**

An instance has been bound using the binding instance-type <instance-type> { <all> | <instance> { <vpn-instance-name> } &<1-8> } command.The statistics function has been enabled using the **statistics enable** command. Otherwise, this function does not take effect.


Example
-------

# Disable statistics counter in-errors of the interface instance bound to the performance statistics task named
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics enable
[*HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] binding instance-type interface instance 100GE1/0/1
[*HUAWEI-pm-statistics-huawei] measure disable instance-type interface measure in-errors

```