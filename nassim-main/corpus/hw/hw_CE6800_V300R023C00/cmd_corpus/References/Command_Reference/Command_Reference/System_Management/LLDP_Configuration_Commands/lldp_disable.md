lldp disable
============

lldp disable

Function
--------



The **lldp disable** command run in the interface view disables Link Layer Discovery Protocol (LLDP) on an interface.

The **undo lldp disable** command run in the interface view enables LLDP on an interface.



If LLDP is enabled globally, LLDP by default takes effect on all interfaces on the device. If LLDP is disabled globally, LLDP does not take effect on any interface.


Format
------

**lldp disable**

**undo lldp disable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If LLDP is enabled on a device, the device can use specified interfaces to exchange LLDP packets with neighbors, learning neighbor status information while sending local status information to neighbors. By collecting status information stored on each network device, the NMS can discover the overall network topology.Note that LLDP takes effect on a device only after LLDP is enabled globally and on specified interfaces. If LLDP is disabled on an interface, the device cannot use this interface to exchange LLDP packets with neighbors. The **lldp enable** command allows you to enable LLDP on a specific interface.



**Prerequisites**



LLDP has been enabled globally using the **lldp enable** command in the system view.



**Precautions**

LLDP can be enabled globally or on interfaces. The relationships are as follows:

* By default, LLDP is enabled on all interfaces supporting LLDP after LLDP is enabled globally.
* LLDP is disabled on all interfaces supporting LLDP after LLDP is disabled globally.Note: Disabling LLDP globally does not affect the LLDP alarm function.
* An interface can send and receive LLDP packets only when LLDP is enabled globally and on the interface.
* When LLDP is disabled globally, the lldp disable or **undo lldp disable** command does not take effect.


Example
-------

# Enable LLDP on an interface.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo lldp disable

```