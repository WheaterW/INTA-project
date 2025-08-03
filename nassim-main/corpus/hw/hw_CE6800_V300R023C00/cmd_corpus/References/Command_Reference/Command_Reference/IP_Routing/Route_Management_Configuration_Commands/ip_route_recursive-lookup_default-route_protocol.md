ip route recursive-lookup default-route protocol
================================================

ip route recursive-lookup default-route protocol

Function
--------



The **ip route recursive-lookup default-route protocol** command enables IPv4 route recursion to the default route.

The **undo ip route recursive-lookup default-route protocol** command disables IPv4 route recursion to the default route.



By default, IPv4 route recursion to the default route is not enabled.


Format
------

**ip route recursive-lookup default-route protocol** { **static** | **msr** }

**undo ip route recursive-lookup default-route protocol** { **static** | **msr** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **static** | Allows IPv6 static routes to recurse to the default route. | - |
| **msr** | Allows IPv4 multicast static routes to recurse to the default route. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The next hops of unicast static routes or multicast static routes may not be directly reachable. In this case, recursion is required so that such routes can be used for traffic forwarding. To allow the IPv4 unicast static routes or multicast static routes whose next hops are not directly reachable to recurse to the default route, run the **ip route recursive-lookup default-route protocol** command.



**Precautions**

After the **ip route recursive-lookup default-route protocol** command is run, IPv4 routes of the specified type can recurse to the default route, which may lead to a forwarding path change.


Example
-------

# Allow IPv4 unicast static routes to recurse to the default route.
```
<HUAWEI> system-view
[~HUAWEI] ip route recursive-lookup default-route protocol static

```