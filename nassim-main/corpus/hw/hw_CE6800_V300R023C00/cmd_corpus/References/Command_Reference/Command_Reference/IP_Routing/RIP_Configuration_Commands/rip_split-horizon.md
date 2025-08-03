rip split-horizon
=================

rip split-horizon

Function
--------



The **rip split-horizon** command enables split horizon for RIP Update packets.

The **undo rip split-horizon** command disables split horizon.



By default, split horizon is enabled on broadcast and Point-to-Point (P2P) interfaces and disabled on Non Broadcast Multiple Access (NBMA) and Point-to-Multipoint (P2MP) interfaces.


Format
------

**rip split-horizon**

**undo rip split-horizon**


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

Split horizon prevents a RIP-enabled interface from sending back the routes it learns, which reduces bandwidth consumption and prevents routing loops. To enable split horizon for RIP update packets, run the rip split-horizon command.Do not disable split horizon for RIP update packets.

**Precautions**

When split horizon and poison reverse are both configured, only poison reverse takes effect.


Example
-------

# Enable split horizon on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip split-horizon

```