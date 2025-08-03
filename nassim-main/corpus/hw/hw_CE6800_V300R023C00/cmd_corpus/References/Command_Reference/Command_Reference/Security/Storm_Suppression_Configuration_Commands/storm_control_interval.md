storm control interval
======================

storm control interval

Function
--------



The **storm control interval** command is to configure the detection interval of storm control.

The **undo storm control interval** command is to restore the storm control detection interval to the default value.



By default, the storm detection interval is 5s.


Format
------

**storm control interval** *interval-value*

**undo storm control interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-value* | Specifies the storm detection interval. | The value is an integer that ranges from 1 to 180, in seconds. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Before running the **storm control interval** command to configure the storm control detection interval, you need to execute the **storm control** command in the interface view to configure storm control. Otherwise, the configured storm control detection interval will not take effect.


Example
-------

# Set the storm detection interval to 10s on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] storm control interval 10

```