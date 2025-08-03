undo ip route-static all
========================

undo ip route-static all

Function
--------



The **undo ip route-static all** command deletes all the configured IPv4 unicast static route.



By default, no IPv4 unicast static routes are configured in the system.


Format
------

**undo ip route-static all**

**undo ip route-static track bfd-session all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **track** | Specifies a track object. | - |
| **bfd-session** | Associates a static BFD session with the static route to fast detect faults. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **undo ip route-static all** command deletes all the configured IPv4 unicast static route.


Example
-------

# Deletes all IPv4 unicast static routes.
```
<HUAWEI> system-view
[~HUAWEI] undo ip route-static all

```