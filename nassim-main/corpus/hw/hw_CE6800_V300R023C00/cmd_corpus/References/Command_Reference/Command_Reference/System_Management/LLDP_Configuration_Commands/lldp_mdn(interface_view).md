lldp mdn(interface view)
========================

lldp mdn(interface view)

Function
--------



The **lldp mdn enable** command enables MAC Address Discovery Neighbor (MDN) on an interface.

The **lldp mdn disable** command disables MDN on an interface.

The **undo lldp mdn** command restores the MDN configuration on an interface to be the same as the global MDN configuration.



By default, the value is the same as the global MDN configuration.


Format
------

**lldp mdn enable**

**lldp mdn disable**

**undo lldp mdn** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables neighbor discovery based on MAC addresses. | - |
| **enable** | Neighbor discovery based on MAC addresses. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After MDN is enabled globally, all interfaces can receive packets discovered using non-standard protocols and identify MDN neighbors based on source MAC addresses of packets. This increases the consumption of system resources and affects the normal running of user services. You can run the **lldp mdn disable** command on a specified interface to disable MDN.To ensure that the local device can discover and identify non-Huawei neighbors, run the **lldp mdn enable** command to enable MDN on the local device. After the MDN function is enabled, the device can receive non-standard discovery protocol packets from neighbors and identify neighbors based on the source MAC addresses and port names in the packets.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**



After MDN is disabled on an interface, the interface cannot receive non-LLDP packets, and the device cannot discover MDN neighbors. The device cannot detect the network topology.



**Precautions**

After you run the **lldp mdn disable** command to disable MDN on an interface, you can run the undo lldp mdn disable or **lldp mdn enable** command on the interface to enable MDN again. The differences between the two commands are as follows:

* After the **undo lldp mdn disable** command is run, MDN on the interface uses the global configuration policy.
* After the **lldp mdn enable** command is run on an interface, MDN on the interface uses the configuration policy of the interface.

After MDN is enabled globally on a device, all interfaces on the device can receive non-standard discovery protocol packets from neighbors and identify neighbors based on the source MAC addresses and port names in the packets. This increases the consumption of system resources and affects the normal running of user services. You can run the **lldp mdn disable** command on a specified interface to disable MDN on the interface.The MDN function adopts the most precise matching principle.

* If MDN is configured both globally and on an interface, the configuration on the interface takes effect.
* If MDN is not configured on an interface, the global configuration policy is used.
* If MDN is not configured globally, the interface-based configuration policy is used.If you run the **undo lldp mdn enable** command on an interface when MDN is configured globally and on the interface, the interface uses the global configuration policy and MDN is still enabled. To disable MDN on the interface, run the **lldp mdn disable** command on the interface.


Example
-------

# Disable MDN on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] lldp mdn disable

```

# Enable MDN on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] lldp mdn enable

```