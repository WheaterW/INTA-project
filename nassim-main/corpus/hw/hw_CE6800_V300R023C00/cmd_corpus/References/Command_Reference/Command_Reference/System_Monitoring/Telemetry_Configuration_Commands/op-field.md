op-field
========

op-field

Function
--------



The **op-field** command configures a filter criterion for telemetry sampling.

The **undo op-field** command restores the default configuration.



By default, no filter criterion is configured for telemetry sampling.


Format
------

**op-field** *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value*

**undo op-field** *field* **op-type** { **eq** | **gt** | **ge** | **lt** | **le** } **op-value** *value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *field* | Specifies the field for filtering sampled data. | The value is a string of 1 to 63 case-sensitive characters.  The field that can be specified is a unit32/uint64 node in the YANG model corresponding to the sampling path. |
| **op-type** | Specifies an operator. | The value is a character string, which can be:   * eq: equal to * ge: greater than or equal to * gt: greater than * le: less than or equal to * lt: less than |
| **op-value** *value* | Specifies a value involved in filter criterion operation. | The value is an integer ranging from 0 to 9223372036854775807.  The value range is the same as that defined in the YANG model for the field option. |



Views
-----

Telemetry filter view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To configure a filter criterion for telemetry sampling, run the op-field command. After the command is run, the data that meets the filter criterion can be collected and reported.

**Prerequisites**

A filter has been created using the **filter** command.

**Precautions**

A maximum of two filter criteria can be configured for a filter.


Example
-------

# Set a filter criterion with the value of the interval field in the data to be sampled equal to 30 for the filter abc of the sampling path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] sensor-group 1
[*HUAWEI-telemetry-sensor-group-1] sensor-path huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info self-defined-event
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path] filter abc
[*HUAWEI-telemetry-sensor-group-1-self-defined-event-path-filter-abc] op-field interval op-type eq op-value 30

```