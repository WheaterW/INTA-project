ripng poison-reverse
====================

ripng poison-reverse

Function
--------



The **ripng poison-reverse** command enables poison reverse for RIPng Update packets.

The **undo ripng poison-reverse** command disables poison reverse for RIPng Update packets.



On non-broadcast multiple access (NBMA) networks, poison reverse is enabled on interfaces by default. On other types of networks, poison reverse is disabled on interfaces by default.


Format
------

**ripng poison-reverse**

**undo ripng poison-reverse**


Parameters
----------

None

Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Poison reverse is used to prevent routing loops. Poison reverse enables a RIPng-enabled interface to set the cost of the route learned from a neighbor to 16 (indicating that the route is unreachable) and then send the route back to the neighbor.

**Precautions**

When split horizon and poison reverse are both configured, only poison reverse takes effect.


Example
-------

# Enable poison reverse for RIPng Update packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng poison-reverse

```