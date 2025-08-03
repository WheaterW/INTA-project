lldp enable
===========

lldp enable

Function
--------



The **lldp enable** command enables Link Layer Discovery Protocol (LLDP) globally.

The **undo lldp enable** command disables LLDP globally.



By default, LLDP is disabled globally.


Format
------

**lldp enable**

**undo lldp enable**


Parameters
----------

None


Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



LLDP is a Layer 2 discovery protocol defined in IEEE 802.1ab. LLDP enables the NMS to learn Layer 2 information about managed devices. The information includes names of interfaces used by one device to connect to other devices and connections between devices. LLDP enables the NMS to learn and analyze Layer 2 topology information. With LLDP, the NMS can manage networks of larger scales and obtain more specific information about network topology and interface changes.Before you view the status of specific Layer 2 links between devices and analyze network topology, run the **lldp enable** command in the system view to enable LLDP globally.



**Configuration Impact**



After LLDP is enabled globally, LLDP is enabled on all LLDP-capable interfaces by default. That is, all interfaces exchange LLDP packets with neighbors. This consumes system resources and may affect user services.



**Follow-up Procedure**



Run the lldp disable command in the interface view to disable LLDP on specified interfaces if required, so that less system resources are consumed and user services can be properly handled.



**Precautions**

LLDP can be enabled globally or on an interface. The relationships between the two functions are as follows:

* After LLDP is enabled globally, LLDP is enabled on all interfaces of the device.
* After LLDP is disabled globally, LLDP is disabled on all interfaces of the device.

Disabling LLDP globally does not affect the LLDP trap function. That is, the LLDP trap function is still enabled.

* An interface can send and receive LLDP packets only when LLDP is enabled globally and on the interface.
* If LLDP is disabled globally, the command for enabling or disabling LLDP on an interface does not take effect.


Example
-------

# Enable LLDP globally.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable

```