collector (system view)
=======================

collector (system view)

Function
--------



The **collector** command configures an analyzer with a specified ID in the system view.

The **undo collector** command cancels the configuration of the analyzer with a specified ID in the system view.



By default, no analyzer is configured in the system view.


Format
------

**collector collect** *collect-id*

**undo collector collect** *collect-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **collect** *collect-id* | Specifies the analyzer ID. | The value is an integer that ranges from 1 to 5. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If service features such as AnyFlow and Packet Event that will collect traffic are deployed on a device and collected traffic needs to be exported to an analyzer for processing, you must first create an analyzer in the system view.


Example
-------

# Configure analyzer 3 in the system view.
```
<HUAWEI> system-view
[~HUAWEI] collector collect 3

```