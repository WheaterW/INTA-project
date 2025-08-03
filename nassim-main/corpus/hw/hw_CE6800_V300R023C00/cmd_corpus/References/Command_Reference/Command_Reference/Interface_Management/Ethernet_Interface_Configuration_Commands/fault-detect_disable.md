fault-detect disable
====================

fault-detect disable

Function
--------



The **fault-detect disable** command disables the fault detection function on an interface.

The **undo fault-detect disable** command restores the default setting.



By default, the fault detection function is enabled on an interface of a device.


Format
------

**fault-detect disable**

**undo fault-detect disable**


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

**Usage Scenario**

In a scenario where two devices are interconnected and fault detection is enabled, the remote interface is Up, but the status of the local interface alternates between Up and Down multiple times due to link signal jitter and the hwLocalFaultAlarm alarm is reported, affecting services. In this case, you are advised to run this command to disable the fault detection function on the interface. This ensures that the local interface does not go Down due to link signal jitter or other causes, ensuring service continuity.

**Precautions**

After the fault detection function is disabled on an interface, the interface at one end may be Up, while the interface at the other end may go Down.


Example
-------

# Disable the fault detection function on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] fault-detect disable

```