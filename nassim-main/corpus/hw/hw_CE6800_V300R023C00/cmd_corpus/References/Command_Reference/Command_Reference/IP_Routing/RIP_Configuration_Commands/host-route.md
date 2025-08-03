host-route
==========

host-route

Function
--------



The **host-route** command allows host routes to be added to the routing table.

The **undo host-route** command prevents host routes from being added to the routing table.



By default, host routes can be added to the routing table.


Format
------

**host-route**

**undo host-route**


Parameters
----------

None

Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, a device selects a mask based on the following rules after receiving RIP-1 routes:

* If the RIP-1 route and the IP address of the interface that receives the RIP-1 route belong to the same network segment, the mask of the RIP-1 route is the mask of the interface IP address.
* If the IP address in the received RIP-1 route and the IP address of the interface that receives the RIP-1 route belong to different network segments, the mask of the RIP-1 route is a natural mask.After the **host-route** command is run, if the IP address carried in the received RIP-1 route and the IP address of the interface that receives the RIP-1 route belong to the same network segment, the mask carried in the RIP-1 route is adopted.

**Precautions**

This command applies to RIP-1. In RIP-2, host routes are added to the routing table, regardless of whether the command is run.


Example
-------

# Allow host routes to be added to the routing table.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] host-route

```