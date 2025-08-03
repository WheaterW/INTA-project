sample-interval
===============

sample-interval

Function
--------



The **sample-interval** command configures the sampling interval for a performance statistics task.

The **undo sample-interval** command restores the default setting.



By default, the sampling interval varies with the performance statistics interval as follows:

* If the interval at which the performance statistics are collected is 5 minutes, the default sampling interval is 1 minute.
* If the interval at which the performance statistics are collected is 10 minutes, the default sampling interval is 2 minutes.
* If the interval at which the performance statistics are collected is 15 minutes, the default sampling interval is 3 minutes.
* If the interval at which the performance statistics are collected is 30 minutes, the default sampling interval is 5 minutes.
* If the interval at which the performance statistics are collected is 60 minutes, the default sampling interval is 5 minutes.
* If the interval at which the performance statistics are collected is 1440 minutes, the default sampling interval is 15 minutes.


Format
------

**sample-interval** *interval*

**undo sample-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which the performance statistics collected in a performance statistics task is sampled. | The value can be 1, 2, 3, 5, 10, 15, 30, or 60, in minutes:   * If the interval at which performance statistics are collected is 5 minutes, the sampling interval can be set to 1 minute or 5 minutes. * If the interval at which performance statistics are collected is 10 minutes, the sampling interval can be set to 1, 2, 5, or 10 minutes. * If the interval at which performance statistics are collected is 15 minutes, the sampling interval can be set to 1, 3, 5, or 15 minutes. * If the interval at which performance statistics are collected is 30 minutes, the sampling interval can be set to 1, 2, 3, 5, 10, 15, or 30 minutes. * If the interval at which performance statistics are collected is 60 minutes, the sampling interval can be set to 1, 2, 3, 5, 10, 15, 30, or 60 minutes. * If the interval at which performance statistics are collected is 1440 minutes, the sampling interval can be set to 1, 2, 3, 5, 10, 15, 30, or 60 minutes. |



Views
-----

Statistics task view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the statistics task is configured, the system collects statistics at a specified sampling interval. The shorter the sampling interval is, the more accurate the statistics are. However, more system resources are consumed.

**Prerequisites**

A performance statistics task has been configured.


Example
-------

# Set the sampling interval to 5 minutes.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] statistics-cycle 30
[*HUAWEI-pm-statistics-huawei] sample-interval 5

```