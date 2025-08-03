speed auto(GE interface view)
=============================

speed auto(GE interface view)

Function
--------



The **speed auto** command sets the auto-negotiation rate of an Ethernet interface.

The **undo speed auto** command restores the default auto-negotiation rate of an Ethernet interface.



By default, the auto-negotiation rate of an Ethernet interface is the maximum rate supported by the interface.


Format
------

**speed auto** { **10** | **100** | **1000** } \*

**undo speed auto** [ **10** | **100** | **1000** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **10** | Indicates the 10 Mbit/s rate mode. | - |
| **100** | Indicates the 100M port speed mode. | - |
| **1000** | Indicates the 1000M port speed mode. | - |



Views
-----

Layer 2 10GE interface view,10GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In auto-negotiation mode, the local interface negotiates the rate with the remote interface, but the negotiated rate may not meet the requirement. You can run this command to configure the auto-negotiation rate on an electrical interface or a GE/10GE optical interface that has a GE optical/electrical module installed.

**Prerequisites**

Run the **undo negotiation disable** command to configure the Ethernet interface to work in auto-negotiation mode.


Example
-------

# Configure the rate auto-negotiation capability of port group test to 10, 100.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] port-group test
[~HUAWEI-port-group-test] speed auto 10 100

```

# Unconfigure the rate auto-negotiation capability of the port group test.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] port-group test
[~HUAWEI-port-group-test] undo speed auto

```