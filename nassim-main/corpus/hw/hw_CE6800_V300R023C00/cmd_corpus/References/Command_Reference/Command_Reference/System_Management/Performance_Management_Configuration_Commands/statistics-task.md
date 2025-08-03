statistics-task
===============

statistics-task

Function
--------



The **statistics-task** command creates a performance statistics task and displays the performance statistics task view. If there is an existing performance statistics task, run the statistics-task command to enter the view of the performance statistics task without creating a task.

The **undo statistics-task** command deletes a performance statistics task.



By default, no performance statistics task is created.


Format
------

**statistics-task** *task-name*

**undo statistics-task** *task-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-name* | Specifies the name of a performance statistics task. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |



Views
-----

Performance management view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A performance statistics task is the minimum statistics collection unit of PM. Before configuring the performance statistics function, run the statistics-task command to create a performance statistics task. Only one performance statistics collection interval can be configured for each performance statistics task. After a performance statistics task is configured, enable statistics counter measurement for the task.

**Prerequisites**

The performance statistics function has been enabled using the statistics enable command.

**Precautions**

After the undo statistics-task command is run to delete a performance statistics task, performance statistics and performance statistics files of the task are deleted.


Example
-------

# Configure a performance statistics task named huawei.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task test
[*HUAWEI-pm-statistics-test]

```