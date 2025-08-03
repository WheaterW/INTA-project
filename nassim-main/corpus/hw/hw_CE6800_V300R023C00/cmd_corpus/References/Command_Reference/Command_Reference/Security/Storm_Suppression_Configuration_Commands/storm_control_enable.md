storm control enable
====================

storm control enable

Function
--------



The **storm control enable** command is used to enable logging or reporting alarms during storm control.

Use the undo storm control command to disable logging or report alarms when storm control is enabled.



By default, the device is disabled from recording logs or reporting traps.


Format
------

**storm control enable** { **log** | **trap** }

**undo storm control enable** { **log** | **trap** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **log** | Enables the device to record logs. | - |
| **trap** | Enables the device to report traps. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After storm control is configured, the switch monitors the broadcast, unknown multicast, and unknown unicast packets received on an interface. When the packet rate within a detection interval exceeds the upper limit, the switch executes the storm control action (block packets or shut down the interface) on the interface. This may affect services. You can configure the log or trap for storm control so that the administrator can quickly take actions to protect the switch.


Example
-------

# Enable the trap function for storm control on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] storm control enable trap

```