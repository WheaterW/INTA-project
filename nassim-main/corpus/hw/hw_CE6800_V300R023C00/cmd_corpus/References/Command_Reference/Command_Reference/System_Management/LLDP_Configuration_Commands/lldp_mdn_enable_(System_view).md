lldp mdn enable (System view)
=============================

lldp mdn enable (System view)

Function
--------



The **lldp mdn enable** command enables MAC Address Discovery Neighbor (MDN) globally.

The **undo lldp mdn enable** command disables MDN globally.



By default, the MDN function is disabled globally.


Format
------

**lldp mdn enable**

**undo lldp mdn enable**


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



To ensure that the local device can discover and identify non-Huawei neighbors, run the ndp enable command to enable MDN on the local device. After the MDN function is enabled, the device can receive non-standard discovery protocol packets from neighbors and identify neighbors based on the source MAC addresses and port names in the packets.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Precautions**



After MDN is enabled globally on a device, all interfaces on the device can receive non-standard discovery protocol packets from neighbors and identify neighbors based on the source MAC addresses and port names in the packets. This increases the consumption of system resources and affects the normal running of user services. You can run the **lldp mdn disable** command on a specified interface to disable MDN on the interface.




Example
-------

# Enable MDN globally.
```
<HUAWEI> system-view
[~HUAWEI] lldp mdn enable

```

# Disable MDN.
```
<HUAWEI> system-view
[~HUAWEI] undo lldp mdn enable

```