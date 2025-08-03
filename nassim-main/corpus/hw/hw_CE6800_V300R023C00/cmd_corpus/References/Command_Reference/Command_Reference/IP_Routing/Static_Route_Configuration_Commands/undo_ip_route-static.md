undo ip route-static
====================

undo ip route-static

Function
--------



The **undo ip route-static** command deletes an IPv4 unicast static route.



By default, the system does not configure IPv4 unicast static routes.


Format
------

**undo ip route-static** *ip-address* { *mask* | *mask-length* } [ { *interface-name* | *interface-type* *interface-number* } [ *nexthop-address* ] | *nexthop-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of the IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies a mask length. The 1s in each 32-bit mask must be consecutive. Therefore, a mask in dotted decimal notation can be presented by a mask length. | The value is an integer ranging from 0 to 32. |
| *nexthop-address* | Specifies the next hop IP address of a route. | The value is in dotted decimal notation. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a simple network, static routes alone can ensure that the network runs properly. If the Device cannot run dynamic routing protocols to generate routes to the destination, configure static routes on the Device.You can configure description description-text to configure a description for static routes so that the administrator can check and maintain static routes easily. To check the configured description, run the display this or **display current-configuration** command in the system view.



**Precautions**

When configuring unicast static routes in a topology instance, pay attention to the following points:

* If no priority is configured for a static route, the default priority is 60.
* When deleting a route, you can specify the priority, tag, or description attribute, but no prompt of the attribute is displayed in the command help.
* If both the destination IP address and the subnet mask are 0.0.0.0, the configured route is the default route. If not matched route is found in the routing table, the default route is used to forward packets.
* You can configure different priorities to implement different routing management policies. For example, if multiple routes to the same destination are configured and they have the same priority, load balancing is implemented. If multiple routes to the same destination are configured but they have different priorities, route backup is implemented.
* When configuring a static route, you can specify the outbound interface or next hop address as required. For the interface that supports the resolution from the network address to the link-layer address or the point-to-point interface, you can specify the outbound interface or the next hop address. However, point-to-multipoint NBMA interfaces, such as X.25-encapsulated interfaces or dial-up interfaces, are not included. At the link layer, you need to configure the IP route and the secondary route, that is, the mapping from the IP address to the link-layer address (such as dialer map ip, x.25 map ip, or frame-relay map ip). In this case, when configuring a static route, you can set only the next hop address instead of the outbound interface.
* If the outbound interface type is not Point-to-Point (P2P), you must specify the next hop address.
* In some cases, for example, when the link layer is encapsulated by the Point-to-Point Protocol (PPP), you can specify the outbound interface during device configuration even if the peer address is unknown. In this way, the configuration of the device does not need to be changed even if the peer address changes.
* If you specify only the IP address and mask when deleting a static route, all static routes with the specified destination IP address and mask are deleted, and the following alarm message is displayed:Warning: All static routes with the destination address and mask will be deleted.
* If the prefix of the host route generated after an IPv4 address is configured on an interface conflicts with that of an existing static route, the static route may be replaced in the routing table, which may cause traffic changes.


Example
-------

# Delete an IPv4 static route and set the next hop address to 10.11.0.1.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 1.1.1.1 32 10.11.0.1
[~HUAWEI] undo ip route-static 1.1.1.1 32

```