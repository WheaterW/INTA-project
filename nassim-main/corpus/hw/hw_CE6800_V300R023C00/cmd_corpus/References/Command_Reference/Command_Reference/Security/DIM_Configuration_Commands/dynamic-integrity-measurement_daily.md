dynamic-integrity-measurement daily
===================================

dynamic-integrity-measurement daily

Function
--------



The **dynamic-integrity-measurement daily** command enables the periodic dynamic integrity measurement (DIM) function and sets the time for triggering DIM every day.

The **undo dynamic-integrity-measurement daily** command disables the periodic DIM function.



By default, periodic DIM is disabled.


Format
------

**dynamic-integrity-measurement daily** *time-value*

**undo dynamic-integrity-measurement daily**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the time when DIM is performed every day. The format is HH:MM. | HH specifies the hour, which is an integer ranging from 0 to 23. MM specifies the minute, which is an integer ranging from 0 to 59. |



Views
-----

Trust environment management


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to enable the periodic DIM function so that the system checks whether the memory of processes in running state is tampered with at a specified time every day.

**Configuration Impact**

If the **dynamic-integrity-measurement daily** command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The DIM function is triggered only when the CPU usage of the device is lower than 85%. If the CPU usage is greater than or equal to 85%, the DIM function is triggered when the CPU usage falls below 85%.


Example
-------

# Disable periodic DIM.
```
<HUAWEI> system-view
[~HUAWEI] trustem
[~HUAWEI-trustem] undo dynamic-integrity-measurement daily

```

# Enable the periodic DIM function and configure the DIM function to be triggered at 03:00 every day.
```
<HUAWEI> system-view
[~HUAWEI] trustem
[~HUAWEI-trustem] dynamic-integrity-measurement daily 03:00

```