host-car disable
================

host-car disable

Function
--------



The **host-car disable** command disables user-level rate limiting on interfaces.

The **undo host-car disable** command enables user-level rate limiting on interfaces.



By default, user-level rate limiting is not enabled on all interfaces.


Format
------

**host-car disable**

**undo host-car disable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After user-level rate limiting is enabled on an interface, the interface performs user-level rate limiting for users connected to the interface.If you are certain that the users under a specific interface are trusted, you can disable user-level rate limiting on that interface.

**Precautions**

The management interface does not support this command.You can configure this command only after running the **cpu-defend host-car enable** command to enable the user-level rate limiting function.After user-level rate limiting is disabled on an interface, the device does not limit the rate of packets received from the specified user MAC address and cannot protect the interface against attacks. In addition, the packets of the same type sent from other users may be affected.


Example
-------

# Disable user-level rate limiting on the interface.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend host-car enable
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] host-car disable

```