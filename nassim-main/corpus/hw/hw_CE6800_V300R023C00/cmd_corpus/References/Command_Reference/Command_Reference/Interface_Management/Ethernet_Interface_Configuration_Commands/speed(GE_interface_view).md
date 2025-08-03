speed(GE interface view)
========================

speed(GE interface view)

Function
--------



The **speed** command configures an Ethernet interface to work at a specified rate.

The **undo speed** command restores the default rate of an Ethernet interface.



By default, an Ethernet interface works at its highest rate.


Format
------

**speed** { **1000** | **100** | **10** }

**undo speed** [ **1000** | **100** | **10** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **1000** | Indicates the 1000 Mbit/s rate mode. | - |
| **100** | Indicates the 100 Mbit/s rate mode. | - |
| **10** | Indicates the 10 Mbit/s rate mode. | - |



Views
-----

Layer 2 10GE interface view,10GE interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In non-auto negotiation mode, if interfaces on two connected devices work at different rates, use the **speed** command to change the rates of the interfaces to be the same so that the two devices can communicate.

**Prerequisites**

* Before running the **speed** command, run the **negotiation disable** command to configure the optical interface that has an O/E conversion module installed to work in non-auto-negotiation mode.
* For 10GE optical interfaces numbered 13 to 16 and 25 to 28 on the CE6881H-48S6CQ and CE6881H-48S6CQ-K, you do not need to run the **negotiation disable** command to configure the interfaces to work in non-auto-negotiation mode before running the **speed** command.
* On the CE6863H and CE6863H-K, 25GE interfaces that have copper modules installed do not support the **speed** command.

**Precautions**

* Only electrical interfaces and the optical interfaces that have copper modules installed support the **speed** command.
* If an optical interface has a copper module installed, the speed 10 command cannot be run.

* On the CE6881H and CE6881H-K, 10GE optical interfaces numbered from 13 to 16 and from 25 to 28 do not support the speed 10 and speed 100 commands after GE media are installed. The interfaces can go Up only after the speed 1000 command is run to change the rate to 1000 Mbit/s, interfaces 13 to 16 and interfaces 25 to 28 are switched together. For example, if you run the speed 1000 command on interface 13 that has a GE medium installed, the rates of interfaces 14, 15, and 16 are switched together.
* 10GE and GE optical interfaces that have copper modules installed do not support the speed 10 command.


Example
-------

# Configure 10GE1/0/1 to work at 1000 Mbit/s when a GE optical/electrical module is inserted.
```
<HUAWEI> system-view
[~HUAWEI] interface 10ge 1/0/1
[*HUAWEI-10GE1/0/1] speed 1000

```