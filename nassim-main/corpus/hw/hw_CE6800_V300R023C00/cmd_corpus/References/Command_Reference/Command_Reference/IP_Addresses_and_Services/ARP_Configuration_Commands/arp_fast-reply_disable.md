arp fast-reply disable
======================

arp fast-reply disable

Function
--------



The **arp fast-reply disable** command disables ARP fast reply.

The **undo arp fast-reply disable** command enables ARP fast reply.



By default, ARP fast reply is enabled.


Format
------

**arp fast-reply disable**

**undo arp fast-reply disable**


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

When a device functions as an access gateway, it needs to process a large number of ARP request packets. As a result, the ARP response speed is slow. To speed up the response to ARP request packets, run the **undo arp fast-reply disable** command to enable ARP fast reply on the device.

**Precautions**

By default, ARP fast reply is enabled. Therefore, after receiving an ARP request packet, the device checks whether the ARP entry corresponding to the source IP address in the ARP request packet exists on the device.When tunnel encapsulation is used, the device can only quickly respond to ARP request packets encapsulated with VXLAN tunnel information.The **undo arp fast-reply disable** command does not take effect in the following situations:

* In scenarios where the arp anti-attack gateway-duplicate enable command is run in the system view to enable ARP gateway anti-collision on the device, ARP fast reply does not take effect.
* In scenarios where the arp ip-conflict-detect enable command is run in the system view to enable IP address conflict detection on the device, ARP fast reply does not take effect.
* In scenarios where a secondary IP address is configured on an interface, ARP fast reply does not take effect on the interface.
* In scenarios where multiple vrrp vrid commands are configured in the interface view, ARP fast reply does not take effect on the interface.

Example
-------

# Disable ARP fast reply.
```
<HUAWEI> system-view
[~HUAWEI] arp fast-reply disable

```