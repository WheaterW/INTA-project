multicast cpu-forward disable
=============================

multicast cpu-forward disable

Function
--------



The **multicast cpu-forward disable** command disables soft forwarding for multicast packets.

The **undo multicast cpu-forward disable** command restores the default configuration.



By default, soft forwarding for multicast packets is enabled.


Format
------

**multicast cpu-forward disable**

**undo multicast cpu-forward disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In most cases, the Router forwards packets based on software before the hardware forwarding is completed. After that, the forwards packets based on hardware.Soft forwarding for multicast packets must be disabled on the router to prevent the low forwarding speed and first packet cache mechanism of soft forwarding from causing disorder of the first packet transmitted at a high speed.

**Prerequisites**

The **multicast routing-enable** command is run.


Example
-------

# Disable soft forwarding for multicast packets in the system view.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] multicast cpu-forward disable

```