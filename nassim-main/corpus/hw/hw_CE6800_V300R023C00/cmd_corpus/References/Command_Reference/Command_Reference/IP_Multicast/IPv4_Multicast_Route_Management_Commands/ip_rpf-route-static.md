ip rpf-route-static
===================

ip rpf-route-static

Function
--------



The **ip rpf-route-static** command configures a multicast static route.

The **undo ip rpf-route-static** command deletes a multicast static route.



By default, no multicast static route is configured.


Format
------

**ip rpf-route-static** [ **vpn-instance** *vpn-instance-name* ] *source-address* { *mask* | *mask-length* } { *rpf-nbr* | { *interface-name* | *interface-type* *interface-number* } } [ **preference** *preValue* ]

**undo ip rpf-route-static** [ **vpn-instance** *vpn-instance-name* ] *source-address* { *mask* | *mask-length* } [ *rpf-nbr* | { *interface-name* | *interface-type* *interface-number* } ]

**undo ip rpf-route-static all**

**undo ip rpf-route-static vpn-instance** *vpn-instance-name* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. By default, the instance is a public network instance. |
| *source-address* | Specifies the address of the multicast source. | The address is in dotted decimal notation. |
| *mask* | Specifies the address mask of the multicast source. | The address is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of the multicast source address. | The value is an integer ranging from 0 to 32. |
| *rpf-nbr* | Specifies the IP address of the Reverse Path Forwarding (RPF) neighbor. | The address is in dotted decimal notation. |
| *interface-name* | Specifies the name of the outbound interface of a static route. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| **preference** *preValue* | Specifies the preference of routes. The greater the value is, the lower the preference is. | The value is an integer that ranges from 1 to 255. The default value is 1. |
| **all** | Indicates all multicast static routes in the multicast static routing table. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Multicast static routes are an important basis of the RPF check. By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for the specific source of packets on the current Device.Multicast static routes provide the following functions, depending on specific applicable environments:

* Changing RPF routesIf the topology of multicast is the same as that of unicast, the transmission path of multicast data is the same as that of unicast data. You can configure multicast static routes to change the RPF routes. Thus, a transmission path dedicated for the multicast data is established, which is different from the transmission path of unicast data.
* Connecting RPF routesOn the network segment where unicast routes are blocked, when multicast static routes are not configured, packets cannot be forwarded because there is no RPF route. In such a case, you can configure multicast static routes. Therefore, the system can generate RPF routes, complete the RPF check, create routing entries, and guide the forwarding of packets.

**Precautions**



When configuring a multicast static route, you can configure the next hop interface in the command if the next hop interface is a point-to-point interface. If the next hop interface is not a point-to-point interface, the next hop address must be used.After the ip rpf-route-static command is run, the multicast static route may not take effect because the outbound interface may fail to be recursed or the specified interface may go Down. Therefore, after this configuration, you are advised to run the **display ip routing-table table-name msr** command to check whether the route is successfully configured or takes effect.




Example
-------

# Configure multicast static routes.
```
<HUAWEI> system-view
[~HUAWEI] ip rpf-route-static 10.0.0.0 255.0.0.0 10.0.0.10

```