speed auto
==========

speed auto

Function
--------



The **speed auto** command configures the auto-negotiation rate of an Ethernet electrical interface.

The **undo speed auto** command restores the default auto-negotiation rate of an Ethernet electrical interface.



By default, the auto-negotiation rate of an Ethernet electrical interface is the maximum rate supported by the interface.


Format
------

**speed auto** { **100** | **1000** | **10000** } \*

**undo speed auto** [ **100** | **1000** | **10000** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **100** | Indicates the 100M mode. | - |
| **1000** | Indicates the 1000M mode. | - |
| **10000** | Indicates the 10000M mode. | - |



Views
-----

Layer 2 10GE interface view,10GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In auto-negotiation mode, the rate of an interface is negotiated with the peer interface, but the negotiated rate may not meet the actual requirement. You can run the command to set the negotiated rate.



**Prerequisites**



Run the **undo negotiation disable** command to configure the Ethernet interface to work in auto-negotiation mode.



**Precautions**



You can run this command only when the device supports 10GE electrical interfaces.




Example
-------

# Set the rate auto-negotiation capability of a 10GE electrical interface to 100 Mbit/s or 1000 Mbit/s.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] interface 10GE 1/0/1
[~HUAWEI-10GE1/0/1] speed auto 100 1000

```

# Disable rate auto-negotiation on a 10GE electrical interface.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] interface 10GE 1/0/1
[~HUAWEI-10GE1/0/1] undo speed auto

```