fault-detect filter disable
===========================

fault-detect filter disable

Function
--------



The **fault-detect filter disable** command disables the fault detection filter function on an interface.

The **undo fault-detect filter disable** command restores the default setting.



By default, the fault detection filter function is enabled on an interface.


Format
------

**fault-detect filter disable**

**undo fault-detect filter disable**


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

The filtering function of fault signals prevents the interface status from changing multiple times when link signals jitter, which affects the normal running of services. In a scenario where two devices are connected, if the peer device does not support fault signal filtering but the local device has fault signal filtering enabled, the peer interface may alternate between Up and Down. In this case, you are advised to run this command to disable fault signal filtering on the local interface.


Example
-------

# Disable the fault detection filter function on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] fault-detect filter disable

```