port-status fast-detect enable
==============================

port-status fast-detect enable

Function
--------



The **port-status fast-detect enable** command enables the function of quickly detecting the interface physical status change.

The **undo port-status fast-detect enable** command restores the default setting.



By default, the function of quickly detecting the interface physical status change is disabled.


Format
------

**port-status fast-detect enable**

**undo port-status fast-detect enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

An Ethernet interface can be physically up or down. When a local device is connected to a transmission device or deployed on a network requiring high reliability, enable this device to rapidly detect interfaces' physical status changes, so that services can run properly.In addition, the carrier down-hold-time <hold-down> command is used to set the delay in reporting an interface Down event. If the hold-down time is set to a small value, for example, less than or equal to 2 seconds, the system may report a false alarm indicating an interface status change within the hold-down time. Enabling the chip to quickly detect the physical status change of an interface can effectively reduce such problems.


Example
-------

# Enable the function of quickly detecting the interface physical status change on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] port-status fast-detect enable

```