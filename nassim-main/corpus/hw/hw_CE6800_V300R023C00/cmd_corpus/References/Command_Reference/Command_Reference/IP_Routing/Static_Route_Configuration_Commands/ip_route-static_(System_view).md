ip route-static (System view)
=============================

ip route-static (System view)

Function
--------



The **ip route-static** command configures an IPv4 unicast static route on the public network.



By default, no IPv4 unicast static route is configured on the public network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip route-static** *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *mask* | Specifies a subnet mask of an IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length. A 32-bit mask is represented by consecutive 1s, and the mask in dotted decimal notation can be replaced by the mask length. | The value is an integer ranging from 0 to 32. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the destination VPN instance. If the destination VPN instance is specified and no next hop address is specified, the Next-Table function is configured. In this case, after receiving packets, the device searches the public network forwarding table for a forwarding entry with the destination VPN instance. Then, the device searches the forwarding table of the destination VPN instance for the corresponding forwarding entry. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **preference** *preference* | Specifies a priority for the static route. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies a tag value for the static route. The tag can be used by a routing policy to import desired static routes. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **description** *text* | Specifies the description of a static route.  Description:  You can run the display this (system view) and display current-configuration commands to view the description.  Other command parameters, such as bfd and preference, cannot be configured after the description keyword. The content is only used as the description. For example, if ip route-static 1.1.1.1 255.255.255.255 NULL0 description aa preference 10 is configured, aa preference 10 is used as the description. | The value is a string of 1 to 150 characters, spaces supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a simple network, static routes alone can ensure that the network runs properly. If the Device cannot run dynamic routing protocols to generate routes to the destination, configure static routes on the Device.

**Precautions**



If a totable static route and another static route with a next hop or outbound interface specified have the same prefix and preference, the two static routes overwrite each other.For static routes with the same prefix but different preferences, you can configure a static route with a specified next-hop IP address and a static route with only a VPN instance specified as the next hop; in addition, you can configure a static route with a specified outbound interface and a static route with only a VPN instance specified as the next hop; you can also configure multiple static routes with only VPN instances specified as next hops.




Example
-------

# Configure an IPv4 static route and set the destination address to 1.2.3.4.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 1.2.3.4 32 vpn-instance vpn1

```