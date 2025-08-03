display pm measure-info
=======================

display pm measure-info

Function
--------



The **display pm measure-info** command displays information about performance statistics counters.




Format
------

**display pm measure-info** [ **instance-type** *instance-type* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance-type** *instance-type* | Specifies the type of an instance bound to a performance statistics task. The instance type is predefined in each feature. Each instance type is defined in a feature. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Before running the **measure disable** command to configure performance statistics counters for instances of a specific type, run the display pm measure-info command to view information about available performance statistics counters, including the name, type, maximum value, and minimum value of each counter.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about performance statistics counters of the instance of the interface type.
```
<HUAWEI> system-view
[~HUAWEI] pm
[~HUAWEI-pm] statistics-task huawei
[*HUAWEI-pm-statistics-huawei] display pm measure-info instance-type interface
Total instance types: 1, total measures: 29
--------------------------------------------------------------------------------
Instance Type: interface, Measures Count: 29
  Measure Name                : in-discards
  Measure Type                : Increase
  Measure Counter Size(bits)  : 32
  Measure MaxValue            : 4294967295
  Measure MinValue            : 0

  Measure Name                : in-errors
  Measure Type                : Increase
  Measure Counter Size(bits)  : 32
  Measure MaxValue            : 4294967295
  Measure MinValue            : 0

  Measure Name                : out-discards
  Measure Type                : Increase
  Measure Counter Size(bits)  : 32
  Measure MaxValue            : 4294967295
  Measure MinValue            : 0
......

```

**Table 1** Description of the **display pm measure-info** command output
| Item | Description |
| --- | --- |
| Total instance types | Total number of instance types. |
| Instance Type | Type of an instance. |
| Measure Name | Name of a performance statistics counter. |
| Measure Type | Type of a performance statistics counter:   * Increase: Accumulated performance statistics are compared with the counter. * Actual: The collected performance statistics are compared with the counter. * Maximum: The maximum performance statistics are compared with the counter. * Minimum: The minimum performance statistics are compared with the counter. * Average: The average performance statistics are compared with the counter. |
| Measure Counter Size(bits) | Size of a performance statistics counter, 32 bits or 64 bits. |
| Measure MaxValue | Maximum value of a performance statistics counter. |
| Measure MinValue | Minimum value of a performance statistics counter. |