statistics-cycle
================

statistics-cycle

Function
--------



The **statistics-cycle** command configures the performance statistics collection interval for a performance statistics task.

The **undo statistics-cycle** command restores the default interval.



The default interval is 15 minutes.


Format
------

**statistics-cycle** *STATSCYCLE*

**undo statistics-cycle**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *STATSCYCLE* | Specifies the performance statistics collection interval for a performance statistics task. | The value can be 5, 10, 15, 30, 60, or 1440, in minutes.  The system defines the interval 1440 minutes as a long interval and the interval 5, 10, 15, 30, or 60 minutes as a short interval. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A specific performance statistics collection interval is set for each performance statistics task. After the performance statistics collection interval is set, bind an instance to the performance statistics task and enable statistics counter measurement so that the system can collect performance statistics at the specified interval. If the statistics interval is set to a small value, the obtained performance statistics are more accurate, but more system resources are consumed.After the performance statistics collection interval is set using the statistics-cycle command, the system collects performance statistics at the specified interval. The set interval takes effect for all statistics counters of instances of a specified type.

**Prerequisites**

The performance statistics function has been enabled using the statistics enable command.

**Configuration Impact**

Running this command in the performance statistics task view has the following impacts:

* Performance statistics of the performance statistics task are deleted.
* The interval at which the system generates performance statistics files is restored to the default value. That is, if the short interval is used, the system generates performance statistics files at an interval of 4 performance statistics intervals; if the long interval is used, the system generates performance statistics files at an interval of 1 performance statistics interval.
* If task-type is set to the default value, the sampling interval of the performance statistics task is restored to the default value. For details about the default sampling interval, see the default sampling interval in the **sample-interval** command.


Example
-------

# Set the statistics collection interval of the performance statistics task task1 to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task task1
[*HUAWEI-pm-statistics-task1] statistics-cycle 5

```