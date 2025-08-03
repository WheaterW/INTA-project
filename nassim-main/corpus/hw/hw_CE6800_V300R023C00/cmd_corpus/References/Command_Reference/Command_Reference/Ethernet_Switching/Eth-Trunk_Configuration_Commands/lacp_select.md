lacp select
===========

lacp select

Function
--------



The **lacp select** command configures the mode for selecting active interfaces of an Eth-Trunk interface in static Link Aggregation Control Protocol (LACP) mode.



By default, active interfaces are selected according to the interface priority.


Format
------

**lacp select speed**

**lacp select priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** | Indicates that active interfaces are selected according to the interface priority. The interfaces with high priorities are preferentially selected as active interfaces. | - |
| **speed** | Indicates that active interfaces are selected according to the interface speed. High-speed interfaces are preferentially selected as active interfaces. | - |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



As defined in LACP, active interfaces are selected according to the interface priority by default. If member interfaces of an Eth-Trunk interface in static LACP mode are of different rates, such as 100 Mbit/s and 1 Gbit/s, low-speed member interfaces may be selected as active interfaces because of their high priorities. If you intend to select high-speed interfaces to be active interfaces, you can run the lacp selected command to set the mode for selecting active interfaces to speed.If you intend to select active interface according to the interface priority, you can run the **lacp select priority** command.




Example
-------

# Configure Eth-Trunk 1 to work in static LACP mode and select active interfaces according to the interface rate.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp select speed

```