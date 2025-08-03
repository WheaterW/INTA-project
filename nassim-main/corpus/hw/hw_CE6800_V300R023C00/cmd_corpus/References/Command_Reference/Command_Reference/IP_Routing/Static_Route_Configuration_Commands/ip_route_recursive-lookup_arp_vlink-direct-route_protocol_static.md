ip route recursive-lookup arp vlink-direct-route protocol static
================================================================

ip route recursive-lookup arp vlink-direct-route protocol static

Function
--------



The **ip route recursive-lookup arp vlink-direct-route protocol static** command configures a device to recurse static routes to ARP Vlink routes.

The **undo ip route recursive-lookup arp vlink-direct-route protocol static** command disables a device from recursing static routes to ARP Vlink routes.



By default, static routes cannot recurse to ARP Vlink routes.


Format
------

**ip route recursive-lookup arp vlink-direct-route protocol static**

**undo ip route recursive-lookup arp vlink-direct-route protocol static**


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



In a scenario where a Layer 2 VPN accesses a Layer 3 VPN, to configure a device to recurse static routes to ARP Vlink routes, run the ip route-static command with recursive-lookup host-route [ arp-vlink-only ] specified and ip route recursive-lookup arp vlink-direct-route protocol static.If a Layer 2 link fails, for example, the physical interface of a Layer 2 device fails, traffic can be switched to the backup path immediately, preventing traffic loss caused by a black-hole route.



**Precautions**



After the **ip route recursive-lookup arp vlink-direct-route protocol static** command is run, all static routes can recurse to ARP Vlink routes. After the **undo ip route recursive-lookup arp vlink-direct-route protocol static** command is run, static routes cannot recurse to ARP Vlink routes..




Example
-------

# Configure the device to recurse static routes to ARP Vlink routes.
```
<HUAWEI> system-view
[~HUAWEI] ip route recursive-lookup arp vlink-direct-route protocol static

```