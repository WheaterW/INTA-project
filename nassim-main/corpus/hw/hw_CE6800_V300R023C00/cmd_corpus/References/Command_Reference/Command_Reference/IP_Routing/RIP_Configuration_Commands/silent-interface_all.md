silent-interface all
====================

silent-interface all

Function
--------



The **silent-interface all** command enables all interfaces to receive RIP packets to update its routing table but disables it from sending RIP packets.

The **undo silent-interface all** command re-enables all interfaces to send updated packets.



By default, an interface is not suppressed.


Format
------

**silent-interface all**

**undo silent-interface all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Suppresses all interfaces. | - |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device running RIP is connected to a network running other routing protocols, you can run the **silent-interface** command on the interface that connects the device to the network. This disables the interface from sending packets to the network and also prevents routing loops.This command can be used together with the peer (RIP) command to advertise routes to a specified device.

**Precautions**



The **silent-interface** command run in a RIP process takes precedence over the rip input or rip output command run on an interface.If the **undo silent-interface all** command has been run in the current process, running the **silent-interface all** command deletes the **undo silent-interface all** command. As a result, the RIP neighbor relationships established on the interfaces covered by the **undo silent-interface all** command go down.




Example
-------

# Set all the interfaces silent.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] silent-interface all

```