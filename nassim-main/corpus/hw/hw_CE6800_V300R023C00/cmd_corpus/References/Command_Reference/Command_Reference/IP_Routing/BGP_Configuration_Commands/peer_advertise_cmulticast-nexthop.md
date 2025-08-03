peer advertise cmulticast-nexthop
=================================

peer advertise cmulticast-nexthop

Function
--------



The **peer advertise cmulticast-nexthop** command configures the next hop of the AD route, which is used to transmit C-multicast routes.

The **undo peer advertise cmulticast-nexthop** command cancels the existing configuration.



By default, the next hop of AD route is not used to match packets.


Format
------

**peer** *ipv4-address* **advertise** **cmulticast-nexthop**

**undo peer** *ipv4-address* **advertise** **cmulticast-nexthop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **peer advertise cmulticast-nexthop** command can be used to set the IP address of an MVPN neighbor to the next hop of the AD route, which is used to transmit C-multicast routes.


Example
-------

# Configure the IP address 2.2.2.9 as the next hop of the AD route.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2.2.2.9 as-number 200
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 2.2.2.9 enable
[*HUAWEI-bgp-af-mvpn] peer 2.2.2.9 advertise cmulticast-nexthop

```