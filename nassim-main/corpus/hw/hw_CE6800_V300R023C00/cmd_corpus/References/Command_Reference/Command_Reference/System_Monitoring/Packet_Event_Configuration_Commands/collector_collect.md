collector collect
=================

collector collect

Function
--------



The **collector collect** command configures the ID of the collector to which data in the packet loss visualization and latency visualization flow tables is reported.

The **undo collector collect** command cancels the ID configuration for the collector to which data in the packet loss visualization and latency visualization flow tables is reported.



By default, the ID of the collector to which data in the packet loss visualization and latency visualization flow tables is reported is not configured.


Format
------

**collector collect** *collect-id*

**undo collector collect** [ *collect-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *collect-id* | Specifies the ID corresponding to the address of the collector to which data in the packet loss visualization and latency visualization flow tables is reported. Only one collector can be configured. | The value is an integer that ranges from 1 to 5. |



Views
-----

packet-event-monitor view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Flow entries generated after packet loss visualization and latency visualization analysis must be aged out locally and reported to a collector for further processing. Therefore, you need to specify the ID of the collector.

**Prerequisites**

The collector ID has been configured using the **collector** command.


Example
-------

# Configure the collector to which data in the packet loss visualization and latency visualization flow tables is reported as collector 2.
```
<HUAWEI> system-view
[~HUAWEI] packet event monitor
[*HUAWEI-packet-event-monitor] collector collect  2

```