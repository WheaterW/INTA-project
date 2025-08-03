default ipv4-unicast
====================

default ipv4-unicast

Function
--------



The **default ipv4-unicast** command enables the IPv4 unicast address family for all peers.

The **undo default ipv4-unicast** command disables the IPv4 unicast address family for all peers.



By default, the IPv4 unicast address family is enabled.


Format
------

**default ipv4-unicast**

**undo default ipv4-unicast**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the IPv4 unicast address family needs to be enabled by default for created BGP peers, run the **default ipv4-unicast** command to set the default address family of BGP to the IPv4 unicast address family.If the IPv4 unicast address family does not need to be enabled by default for created BGP peers, run the **undo default ipv4-unicast** command to disable the IPv4 unicast address family for all peers.

**Configuration Impact**

After the **default ipv4-unicast** command is run, the IPv4 unicast address family is enabled by default for created BGP peers.

**Precautions**



The **default ipv4-unicast** command cannot be delivered through YANG. When a BGP peer is created in YANG mode, the IPv4 unicast address family is not enabled by default. The configurations delivered in YANG mode are based on packets. When a peer is created, the unicast address family is enabled for the peer only when the YANG packet carries the subtable of the peer address family and the type of the IPv4 unicast address family is specified. The function that packets do not carry subtables does not take effect by default.




Example
-------

# Disable the IPv4 unicast address family for all peers.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] undo default ipv4-unicast

```