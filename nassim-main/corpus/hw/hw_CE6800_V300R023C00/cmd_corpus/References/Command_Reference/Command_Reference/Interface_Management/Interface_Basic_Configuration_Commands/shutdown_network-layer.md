shutdown network-layer
======================

shutdown network-layer

Function
--------

The **shutdown network-layer** command disables the protocol layer status of an interface.

The **undo shutdown network-layer** command enables the protocol layer status of an interface.

By default, the protocol layer status of an interface is not disabled.



Format
------

**shutdown network-layer**

**undo shutdown network-layer**



Parameters
----------

None


Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

When the **shutdown** command is run to shut down a physical interface, the link layer and protocol layer status of the interface becomes Down. In scenarios where fault locating is implemented for optical modules or fibers, users require that only the protocol status of an interface becomes Down but the physical and link layer status remains unchanged. To meet this requirement, run the **shutdown network-layer** command to disable the protocol status of the interface. After faults are located at the physical and link layers, run the undo **shutdown network-layer** command to restart the protocol status of the interface.

**Precautions**

* The **shutdown network-layer** command cannot be run in the port-group view when the Layer 3 Ethernet physical interface has been added to an interface group.
* The **shutdown network-layer** and **protocol up-delay-time time-value** commands cannot be configured together.



Example
-------

# Disable the protocol status of
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] shutdown network-layer

```