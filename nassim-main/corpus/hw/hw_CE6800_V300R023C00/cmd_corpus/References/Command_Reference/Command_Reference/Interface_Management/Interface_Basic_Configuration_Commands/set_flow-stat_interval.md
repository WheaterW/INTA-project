set flow-stat interval
======================

set flow-stat interval

Function
--------



The **set flow-stat interval** command sets the interval at which traffic statistics are collected on an interface.

The **undo set flow-stat interval** command restores the default interval.



By default, the interval for collecting traffic statistics on an interface is 300 seconds.


Format
------

**set flow-stat interval** *interval*

**undo set flow-stat interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which traffic statistics are collected on an interface. | The value is an integer ranging from 10 to 600 and must be a multiple of 10, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The interval configured in the system view for collecting traffic statistics takes effect on all the interfaces using the default traffic statistics interval.



**Precautions**

The interval configured in the interface view has a higher priority than that configured in the system view.

* A newly configured interval takes effect only after an existing interval expires and traffic statistics are updated during the second interval after the new interval takes effect.
* Management network interfaces do not support the configuration of an interval at which interface statistics are collected.


Example
-------

# In the system view, set the interval at which traffic statistics are collected on interfaces to 200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] set flow-stat interval 200

```