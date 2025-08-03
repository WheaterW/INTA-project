rip bfd static
==============

rip bfd static

Function
--------



The **rip bfd static** command enables static BFD on a specified RIP interface.

The **undo rip bfd static** command disables static BFD from a specified RIP interface.



By default, static BFD is disabled on a RIP interface.


Format
------

**rip bfd static**

**undo rip bfd static**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network deployed with high-speed data services, if a fault occurs on a link, a large amount of data is lost because it takes a long time for RIP to detect the fault. Deploying BFD for RIP to accelerate fault detection is necessary.The **rip bfd static** command is used to enable BFD for RIP on a specified link to rapidly detect the fault on the link. In addition, because a large number of devices do not support BFD, you can run this command to implement one-arm BFD detection independently.

**Prerequisites**

BFD has been enabled using the **bfd** command.

**Precautions**

If the rip bfd block, rip bfd enable, rip bfd static, and rip bfd static binding commands override each other, and the latest configuration overrides the previous one.This command will change the existing BFD configuration mode.


Example
-------

# Enable static BFD on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip bfd static

```