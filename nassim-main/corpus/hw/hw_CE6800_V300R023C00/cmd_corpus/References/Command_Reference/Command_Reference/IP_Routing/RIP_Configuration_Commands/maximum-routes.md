maximum-routes
==============

maximum-routes

Function
--------



The **maximum-routes** command sets the maximum number of routes that RIP can process.

The **undo maximum-routes** command restores the default value.



By default, RIP can process 150,000 routes.


Format
------

**maximum-routes** *max-number* [ **threshold** *threshold-value* ]

**undo maximum-routes**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-number* | Specifies the maximum number of routes that RIP can process. | The value is an integer that ranges from 1 to 300000. The default value is 150000. |
| **threshold** *threshold-value* | Specifies an alarm threshold for RIP routes. | The value is an integer ranging from 0 to 100, in percentages. The default value is 80. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set the maximum number of routes that RIP can process, run the maximum-routes command.After the number of routes exceeds the maximum number, RIP does not receive any routes until the number of routes falls below the set alarm threshold.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.


Example
-------

# Set the maximum number of routes that RIP can process to 2,00,000 and the alarm threshold to 75%.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] maximum-routes 200000 threshold 75

```