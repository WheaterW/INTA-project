peer advertise cmulticast-nexthop (BGP-MVPN address family view)
================================================================

peer advertise cmulticast-nexthop (BGP-MVPN address family view)

Function
--------



The **peer advertise cmulticast-nexthop** command configures the next hop of the AD route, which is used to transmit C-multicast routes.

The **undo peer advertise cmulticast-nexthop** command cancels the existing configuration.



By default, the next hop of AD route is not used to match packets.


Format
------

**peer** *group-name* **advertise** **cmulticast-nexthop**

**undo peer** *group-name* **advertise** **cmulticast-nexthop**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



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
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer test enable
[*HUAWEI-bgp-af-mvpn] peer test advertise cmulticast-nexthop

```