speed(Management interface view)
================================

speed(Management interface view)

Function
--------



The **speed** command sets the rate for an Ethernet interface.

The **undo speed** command restores the default rate of an Ethernet interface.



By default, an interface works at its highest rate.


Format
------

**speed** { **1000** | **100** | **10** }

**undo speed** [ **1000** | **100** | **10** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **1000** | 1000M port speed mode. | - |
| **100** | 100M port speed mode. | - |
| **10** | 10M port speed mode. | - |



Views
-----

Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In non-auto negotiation mode, if interfaces on two connected devices work at different rates, use the **speed** command to change the rates of the interfaces to be the same so that the two devices can communicate.

**Prerequisites**

Before running the **speed** command on an electrical interface or an optical interface with an optical-to-electrical conversion module installed, run the **negotiation disable** command to disable the auto-negotiation mode.


Example
-------

# Set the rate of MEth0/0/0 in non-auto-negotiation mode to 100 Mbit/s.
```
<HUAWEI> system-view
[~HUAWEI] interface MEth 0/0/0
[~HUAWEI-MEth0/0/0] negotiation disable
[*HUAWEI-MEth0/0/0] speed 100

```