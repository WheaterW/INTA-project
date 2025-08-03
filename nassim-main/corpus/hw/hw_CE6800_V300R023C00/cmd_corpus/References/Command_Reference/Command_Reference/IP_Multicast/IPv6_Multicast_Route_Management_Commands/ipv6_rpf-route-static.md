ipv6 rpf-route-static
=====================

ipv6 rpf-route-static

Function
--------



The **ipv6 rpf-route-static** command configures an IPv6 multicast static route.

The **undo ipv6 rpf-route-static** command deletes an IPv6 multicast static route.



By default, no IPv6 multicast static route is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 rpf-route-static** [ **vpn-instance** *vpn-instance-name* ] *source-address* *mask-Length* { *rpf-nbr6* | { *interface-name* | *interface-type* *interface-number* } } [ **preference** *preValue* ]

**undo ipv6 rpf-route-static** [ **vpn-instance** *vpn-instance-name* ] *source-address* *mask-Length* [ *rpf-nbr6* | { *interface-name* | *interface-type* *interface-number* } ] [ **preference** *preValue* ]

**undo ipv6 rpf-route-static all**

**undo ipv6 rpf-route-static vpn-instance** *vpn-instance-name* **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of case-sensitive characters. By default, the instance is a public network instance. |
| *source-address* | Specifies the address of a multicast source. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *mask-Length* | Specifies the mask length of an IPv6 multicast source address. | It is an integer ranging from 0 to 128. |
| *rpf-nbr6* | Specifies the IPv6 address of a Reverse Path Forwarding (RPF) neighbor. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *interface-name* | Specifies the name of the outbound interface of a static route. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type of the outbound interface of a static route. | - |
| *interface-number* | Specifies the number of the outbound interface of a static route. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **preference** *preValue* | Specifies the preference of routes. The greater the value is, the lower the preference is. | The value is an integer that ranges from 1 to 255. The default value is 1. |
| **all** | Deletes all multicast static routes. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Multicast static routes are an important basis for RPF check. By configuring multicast static routes, you can specify an RPF interface and RPF neighbor for the specific source of packets on the current device.Multicast static routes provide the following functions:Changing RPF RoutesWhen the multicast topology structure is the same as the unicast topology structure on the network, the transmission path of multicast data is the same as that of unicast data. By configuring multicast static routes, you can change the RPF route and create a transmission path different from that of unicast for multicast data.Connecting RPF RoutesOn the network segment where unicast routes are blocked, if multicast static routes are not configured, packets cannot be forwarded because there is no RPF route. You can configure multicast static routes to generate RPF routes, complete the RPF check, create routing entries, and guide packet forwarding.

**Precautions**

When configuring a multicast static route, you can configure the next hop interface in the command if the next hop interface is a point-to-point interface. If the next hop interface is not a point-to-point interface, the next hop address must be used.After the **ipv6 rpf-route-static** command is run, the multicast static route may not take effect because the outbound interface may fail to be recursed or the specified interface may go Down. Therefore, after this configuration, you are advised to run the **display ipv6 routing-table table-name msr** command to check whether the route is successfully configured or takes effect.


Example
-------

# Configure an IPv6 multicast static route.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 rpf-route-static 2001:db8:1::1 128 2001:db8:2::1

```