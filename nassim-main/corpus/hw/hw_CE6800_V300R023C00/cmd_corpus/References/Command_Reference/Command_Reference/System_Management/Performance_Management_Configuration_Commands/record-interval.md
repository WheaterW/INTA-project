record-interval
===============

record-interval

Function
--------



The **record-interval** command sets the number of performance statistics cycles after which the data is collected.

The **undo record-interval** command restores the default number of performance statistics cycles after which the data is collected.



By default, the interval at which the system generates performance statistics files is determined by the interval at which performance statistics are collected:

* If a short interval (5, 10, 15, 30, or 60 minutes) at which performance statistics are collected is set, the system generates performance statistics files every four performance statistics intervals.
* If a long interval (1440 minutes) at which performance statistics are collected is set, the system generates performance statistics files at every one performance statistics interval.


Format
------

**record-interval** *interval*

**undo record-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the number of performance statistics cycles after which the data is collected. | The value is an integer ranging from 1 to 16. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The system periodically records the performance statistics into performance statistics files. To set the number of performance statistics cycles after which the data is collected, run the record-interval command. Then the system generates performance statistics files every cycle x interval minutes and automatically saves the performance statistics in the file. The system generates a maximum of four statistics files for each performance statistics task and saves performance statistics files to the path flash:/pmdata by default.The default interval at which the system generates performance statistics files is determined by the interval at which the performance statistics are collected:

* If a short interval (5, 10, 15, 30, or 60 minutes) at which the performance statistics are collected is set, the system generates a performance statistics file every 16 performance statistics intervals at most.
* If a long interval (1440 minutes) at which the performance statistics are collected is set, the system generates a performance statistics file every 3 performance statistics intervals.

**Prerequisites**

The performance statistics function has been enabled using the statistics enable command.


Example
-------

# Configure the system to generate a performance statistics file every 15 minutes (The interval at which the system collects the performance statistics is 5 minutes and the number of performance statistics cycles after which the data is collected is 3).
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics enable
[*HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] statistics-cycle 5
Warning: All data of the statistics task will be deleted. Continue? [Y/N]:y
[*HUAWEI-pm-statistics-huawei] record-interval 3
Warning: This operation will cause some data to be lost. Continue? [Y/N]:y

```