zero-metric-check
=================

zero-metric-check

Function
--------



The **zero-metric-check** command configures a device to reject the route with metric 0.

The **undo zero-metric-check** command configures a device to accept the route with metric 0.



By default, routes with the metric being 0 are rejected.


Format
------

**zero-metric-check**

**undo zero-metric-check**


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

Non-Huawei devices may send RIP packets with metric 0. To enable a Huawei device that does not accept RIP packets with metric 0 and a non-Huawei device that can send RIP packets with metric 0, run the **undo zero-metric-check** command on the Huawei device.


Example
-------

# Configure the route with metric 0 to be rejected in RIP process 1.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] zero-metric-check

```