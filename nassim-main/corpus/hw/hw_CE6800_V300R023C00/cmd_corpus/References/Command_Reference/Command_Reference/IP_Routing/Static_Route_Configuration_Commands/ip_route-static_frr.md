ip route-static frr
===================

ip route-static frr

Function
--------



The **ip route-static frr** command enables Fast ReRoute (FRR) for a static route.

The **undo ip route-static frr** command disables FRR for a static route.



By default, FRR is disabled for an IPv4 static route.


Format
------

**ip route-static frr**

**undo ip route-static frr**


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

To protect IPv4 static routes, configure FRR for IPv4 static routes using the ip route-static frr command.


Example
-------

# Enable FRR for the static route.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static frr

```