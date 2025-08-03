display pm statistics-task
==========================

display pm statistics-task

Function
--------



The **display pm statistics-task** command displays information about a performance statistics task.




Format
------

**display pm statistics-task** [ *task-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *task-name* | Displays the performance statistics files generated for a performance statistics task. | The value is a string of 1 to 31 characters, spaces not supported. The string contains letters, digits, and underscores (\_), and must start with letters or digits. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view performance statistics of a specified task, run the display pm statistics-task command. The command output shows the interval at which the performance statistics are collected, running status of the task, type of the instance bound to the task, interval at which the system generates performance statistics files, prefix of the performance statistics file, and existing performance statistics file.

**Prerequisites**

A performance statistics task has been configured and the performance statistics function is enabled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about performance statistics task huawei.
```
<HUAWEI> display pm statistics-task a
Task Name                : a
Task State               : running
Record-file Status       : enable
Task Cycle               : 15 minutes
Sample Interval          : 3 minutes
Instance Type            : interface
Record Interval(cycle)   : 4
File Format              : text
File Name Prefix         : a
File Transfer Mode       : passive
Current File Name        : a20110422210001.txt

```

**Table 1** Description of the **display pm statistics-task** command output
| Item | Description |
| --- | --- |
| Task Name | Name of a performance statistics task. |
| Task State | Running status of a performance statistics task. |
| Task Cycle | Interval at which the performance statistics are collected in a performance statistics task. |
| Record-file Status | Whether the function of generating performance statistics files is enabled. |
| Sample Interval | Interval at which the performance statistics collected in a performance statistics task is sampled. |
| Instance Type | Type of an instance bound to a performance statistics task. |
| Record Interval(cycle) | Interval at which the system generates performance statistics files. |
| File Format | Format of performance statistics files. |
| File Name Prefix | Name prefix of a performance statistics file. |
| File Transfer Mode | Mode in which performance statistics files are transmitted (Performance statistics files are sent to a PM server under the request of the NMS.). |
| Current File Name | Name of the existing performance statistics file that the system generates. |