speed(10GE interface view)
==========================

speed(10GE interface view)

Function
--------



The **speed** command configures an Ethernet interface to work at a specified rate.

The **undo speed** command restores the default rate of an Ethernet interface.



By default, interfaces work at the maximum supported rate.


Format
------

**speed** { **10000** | **1000** | **100** }

**undo speed** [ **10000** | **1000** | **100** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **10000** | Indicates the 10000M mode. | - |
| **1000** | Indicates the 1000M mode. | - |
| **100** | Indicates the 100M mode. | - |



Views
-----

Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In non-auto negotiation mode, if interfaces on two connected devices work at different rates, use the speed command to change the rates of the interfaces to be the same so that the two devices can communicate.



**Precautions**



You can run this command only when the device supports 10GE electrical interfaces.




Example
-------

# Set the rate of 10GE1/0/1 in non-auto-negotiation mode to 1000 Mbit/s.
```
<HUAWEI> system-view
[~HUAWEI] interface 10GE 1/0/1
[~HUAWEI-10GE1/0/1] negotiation disable
[*HUAWEI-10GE1/0/1] speed 1000

```