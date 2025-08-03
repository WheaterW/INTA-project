rip poison-reverse
==================

rip poison-reverse

Function
--------



The **rip poison-reverse** command enables poison reverse for RIP update packets.

The **undo rip poison-reverse** command disables poison reverse.



On non-broadcast multiple access (NBMA) networks, poison reverse is enabled on interfaces by default. On other types of networks, poison reverse is disabled on interfaces by default.


Format
------

**rip poison-reverse**

**undo rip poison-reverse**


Parameters
----------

None

Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Poison reverse allows a RIP-enabled interface to set the cost of the route that it learns from a neighbor to 16 (indicating that the route is unreachable) and then send the route back. After receiving this route, the neighbor deletes the useless route from its routing table, which prevents loops. To enable poison reverse for RIP update packets, run the rip poison-reverse command.

**Precautions**

When split horizon and poison reverse are both configured, only poison reverse takes effect.


Example
-------

# Enable poison reverse on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip poison-reverse

```