device power manage cycle
=========================

device power manage cycle

Function
--------



The **device power manage cycle** command sets the interval for updating power consumption data.

The **undo device power manage cycle** command restores the default interval for updating power consumption data.



By default, the interval for updating power consumption data is 1 hour.


Format
------

**device power manage cycle** *cycle-value*

**undo device power manage cycle** [ *cycle-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cycle-value* | Sets the interval for updating power consumption data. | The value is an integer ranging from 1 to 6.   * 1: 15 minutes * 2: 30 minutes * 3: one hour * 4: one day * 5: one week * 6: one month |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The average power consumption of a device is the average power consumption within a period of time. You can run the **device power manage cycle** command to set the interval for calculating the average power consumption. To obtain real-time power consumption, set a short interval.

**Precautions**

This command is supported only when the device has a power supply. Otherwise, the message "Error: This operation is not supported." is displayed.


Example
-------

# Set the interval for updating power consumption data to 30 minutes.
```
<HUAWEI> system-view
[~HUAWEI] device power manage cycle 2

```