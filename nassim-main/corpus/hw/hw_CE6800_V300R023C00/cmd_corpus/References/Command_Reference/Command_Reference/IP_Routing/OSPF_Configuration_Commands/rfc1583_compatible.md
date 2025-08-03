rfc1583 compatible
==================

rfc1583 compatible

Function
--------



The **rfc1583 compatible** command configures a device to comply with the route selection rules defined in RFC 1583. This configuration facilitates OSPF route selection.

The **undo rfc1583 compatible** command configures a device to comply with the route selection rules defined in RFC 2328.

The **rfc1583 compatible** command configures a device to comply with the route selection rules defined in RFC 1583. This configuration facilitates OSPFv3 route selection.

The **undo rfc1583 compatible** command configures a device to comply with the route selection rules defined in RFC 5340.



By default, OSPF configures the rules defined in RFC 1583.

By default, OSPFv3 configures the rules defined in RFC 5340.




Format
------

**rfc1583 compatible**

**undo rfc1583 compatible**


Parameters
----------

None

Views
-----

OSPFv3 view,OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

RFC 2328 and RFC 1583 define two different route selection rules for the OSPF protocol. When enabling OSPF, you need to configure the route selection rules for the OSPF domain according to the networking plan to ensure that the route selection rules for the OSPF domain are the same. For example, OSPF supports the route selection rules defined in RFC 1583 by default. If other devices in the OSPF domain support the route selection rules defined in RFC 2328, run the **undo rfc1583 compatible** command to use the route selection rules defined in RFC 2328.RFC 5340 and RFC 1583 define two types of OSPFv3 route selection rules. When enabling OSPFv3, configure the same route selection rules for OSPFv3 domains based on the networking plan. For example, OSPFv3 supports the route selection rules defined in RFC 5340 by default. If other devices in the OSPFv3 domain support the route selection rules defined in RFC 1583, run the **rfc1583 compatible** command to use the route selection rules defined in RFC 1583.When multiple AS-External LSAs advertise routes to the same destination, RFC 1583, RFC 2328, and RFC 5340 define different rules for selecting the optimal route. RFC 1583 prefers intra-area routes. RFC 2328 and RFC 5340 prefer intra-area routes in non-backbone areas. Selecting RFC 2328 or 5340 can reduce the burden on the backbone area.


Example
-------

# Configure a device to comply with the route selection rules defined in RFC 1583.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] rfc1583 compatible

```

# Configure a device to comply with the route selection rules defined in RFC 2328.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] undo rfc1583 compatible

```