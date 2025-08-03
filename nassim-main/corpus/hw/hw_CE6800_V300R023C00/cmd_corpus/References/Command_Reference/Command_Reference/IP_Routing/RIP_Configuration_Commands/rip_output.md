rip output
==========

rip output

Function
--------



The **rip output** command enables the interface to send RIP packets.

The **undo rip output** command disables the interface from sending RIP packets.



By default, an interface is enabled to send RIP packets.


Format
------

**rip output**

**undo rip output**


Parameters
----------

None

Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device running RIP is connected to a network running other routing protocols, run the **rip output** command on the interface that connects the device to the network to prevent the interface from sending useless packets to the network.

**Precautions**

The **silent-interface** command that is run in a RIP process takes precedence over the rip input or **rip output** command that is run on an interface.


Example
-------

# Disable 100GE 1/0/1 from sending RIP packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip output

```