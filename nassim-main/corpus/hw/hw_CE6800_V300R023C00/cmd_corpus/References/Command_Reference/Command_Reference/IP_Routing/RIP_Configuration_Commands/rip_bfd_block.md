rip bfd block
=============

rip bfd block

Function
--------



The **rip bfd block** command blocks BFD on a specified interface.

The **undo rip bfd block** command disables the blocking function.



By default, the blocking function is disabled.


Format
------

**rip bfd block**

**undo rip bfd block**


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

If the link status is unstable, BFD sessions may frequently alternate between Up and Down, which deteriorates network stability and reliability. In this situation, run the **rip bfd block** command to block BFD.

**Prerequisites**

BFD has been enabled using the **bfd** command.

**Precautions**

If the rip bfd block, rip bfd enable, rip bfd static, and rip bfd static binding commands override each other, and the latest configuration overrides the previous one.


Example
-------

# Block BFD on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip bfd block

```