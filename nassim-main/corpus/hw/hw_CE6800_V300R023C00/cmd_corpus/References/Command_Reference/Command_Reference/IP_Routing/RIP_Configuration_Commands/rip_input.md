rip input
=========

rip input

Function
--------



The **rip input** command enables an interface to receive RIP packets.

The **undo rip input** command disables an interface from receiving RIP packets.



By default, an interface is enabled to receive RIP packets.


Format
------

**rip input**

**undo rip input**


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

When a device running RIP is connected to a network running other routing protocols, you can run the **rip input** command on the interface that connects the device to the network to prevent the interface from receiving useless packets from the network.

**Implementation Procedure**

The **silent-interface** command that is run in a RIP process takes precedence over the rip input or rip output command that is run on an interface.


Example
-------

# Disable 100GE1/0/1 from receiving RIP packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] undo rip input

```