port transceiver-power-low trigger error-down
=============================================

port transceiver-power-low trigger error-down

Function
--------



The **port transceiver-power-low trigger error-down** command enables the Error-Down function triggered by low optical power on an Ethernet optical interface.

The **undo port transceiver-power-low trigger error-down** command disables the Error-Down function triggered by low optical power on an Ethernet optical interface.



By default, an Ethernet optical interface does not transit to the Error-Down state when the optical power is too low.


Format
------

**port transceiver-power-low trigger error-down**

**undo port transceiver-power-low trigger error-down**


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

When the receive optical power of the device is too low, services are interrupted intermittently. To prevent services from being affected, you need to configure the interface to enter the Error-Down state when the receive optical power of the optical module is too low so that services can be switched immediately when a fault occurs. When a device detects a fault on an interface, the device sets the interface status to Error-Down. The interface cannot send or receive packets, and the interface indicator is off.

**Follow-up Procedure**

If an interface enters the Error-Down state, you are advised to locate the cause first. For details, see the possible causes and handling procedure.You can use either of the following methods to restore the interface status:

* Manually rectify the fault (after the Error-Down event occurs).If only a few interfaces are in Error-Down state, run the **shutdown** and **undo shutdown** commands in the interface view or run the **restart** command in the interface view to restart the interfaces.
* Automatic recovery (before an Error-Down event occurs)If a large number of interfaces are in Error-Down state, manually restoring the interfaces one by one will cause a lot of repeated work and some interfaces may not be configured. To prevent this problem, run the **error-down auto-recovery cause transceiver-power-low interval** command in the system view to enable the auto-recovery function and set the auto-recovery delay. You can run the **display error-down recovery** command to check information about automatic interface recovery.

Example
-------

# Enable the Error-Down function triggered by low optical power on the 100GE1/0/1 interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port transceiver-power-low trigger error-down

```