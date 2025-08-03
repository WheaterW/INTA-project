ipv6 route-static
=================

ipv6 route-static

Function
--------



The **ipv6 route-static** command configures an IPv6 static route on the public network.

The **undo ipv6 route-static** command deletes a configured IPv6 static route of the public network.



By default, no IPv6 static route is configured on the public network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route-static** *dest-ipv6-address* *prefix-length* **vpn-instance** *vpn-instance-name* *nexthop-ipv6-address* [ **recursive-lookup** **host-route** ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**ipv6 route-static** *dest-ipv6-address* *prefix-length* [ **vpn-instance** *vpn-instance-name* ] *nexthop-ipv6-address* [ **recursive-lookup** **host-route** ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] **inherit-cost** [ **inter-protocol-ecmp** ] [ **description** *text* ]

**ipv6 route-static** *dest-ipv6-address* *prefix-length* **vpn-instance** *vpn-instance-name* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]

**undo ipv6 route-static** *dest-ipv6-address* *prefix-length* **vpn-instance** *vpn-instance-name* *nexthop-ipv6-address*

**undo ipv6 route-static** *dest-ipv6-address* *prefix-length* **vpn-instance** *vpn-instance-name*

**ipv6 route-static** *dest-ipv6-address* *prefix-length* *nexthop-ipv6-address* [ **recursive-lookup** **host-route** ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**ipv6 route-static** *dest-ipv6-address* *prefix-length* { *interface-name* | *interface-type* *interface-number* } [ *nexthop-ipv6-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dest-ipv6-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of an IPv6 prefix. | It is an integer ranging from 0 to 128. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of an IPv6 address family-enabled VPN instance. If a VPN instance is specified, the static route searches the routing table of the VPN instance for an outbound interface based on the configured nexthop-ipv6-address. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (").  If nexthop-ipv6-address is not specified, the next-table function is configured. After receiving a packet, the searches the public network forwarding table for a forwarding path, finds the destination VPN instance, and then searches the destination VPN instance forwarding table for a forwarding path. |
| *nexthop-ipv6-address* | Specifies the next-hop IPv6 address. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **recursive-lookup** | Recursive route lookup policy. | - |
| **host-route** | Recurses the static route to a 128-bit host route. | - |
| **preference** *preference* | Specifies a priority for static routes. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies the tag value of a static route. You can configure different tag values to classify static routes and implement different routing management policies. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **bfd** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **enable** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **track** | Specifies a monitored object. | - |
| **bfd-session** *cfg-name* | Associates a static BFD session with the static route to fast detect faults.  The undo ip route-static [ track bfd-session ] all command with track bfd-session cfg-name specified dissociates the static route from the current BFD session only without deleting the static route. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| **nqa** *admin-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| *test-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| **inter-protocol-ecmp** | Enables inter-protocol load balancing among static routes and the routes of dynamic routing protocols.  If the static route is the optimal or suboptimal route and the optimal and suboptimal routes have the same priority, inter-protocol load balancing can be implemented between the static route and the routes of other routing protocols.  If this parameter is specified for any of the static routes, all the static routes with the specified prefix in the routing table carry out inter-protocol load balancing.  Intra-protocol inter-process load balancing and inter-protocol load balancing cannot coexist. Intra-protocol inter-process load balancing takes precedence over inter-protocol load balancing.  Inter-protocol load balancing does not take effect in the following cases:   * import-rib and non-import-rib routes. * Blackhole route and non-blackhole route. * Vlink routes and routes of other protocols. | - |
| **description** *text* | Specifies the description of a static route.  You can run the display this (system view) and display current-configuration commands to view the description.  Other command parameters, such as bfd and preference, cannot be configured after the description keyword. The content is only used as the description. For example, if ipv6 route-static 2001:db8::1 128 NULL0 description aa preference 10 is configured, aa preference 10 is used as the description. | The value is a string of 1 to 150 characters, spaces supported. |
| *interface-type* | Specifies the type of an interface. | -  - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **inherit-cost** | Enables the static route to inherit the cost of recursive routes. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a simple network or when the device cannot use a dynamic routing protocol to establish a route to a destination, you can configure static routes.If you specify a VPN instance for a static route, a device searches the routing table of the VPN instance for an outbound interface of the static route and adds the static route to the public routing table. To configure a static route in a VPN instance, run the **ipv6 route-static vpn-instance** command.

**Prerequisites**



BFD must have been enabled when you bind a static route to a BFD session.An NQA test instance must have been created when you bind it to a static route.



**Precautions**



If a totable static route and another static route with a next hop or outbound interface specified have the same prefix and preference, the two static routes overwrite each other.For static routes with the same prefix but different preferences, you can configure a static route with a specified next-hop IP address and a static route with only a VPN instance specified as the next hop; in addition, you can configure a static route with a specified outbound interface and a static route with only a VPN instance specified as the next hop; you can also configure multiple static routes with only VPN instances specified as next hops.




Example
-------

# Configure IPv6 static routes on the public network.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static 2001:db8:1::1 64 2001:db8:2::1

```

# Configure an IPv6 static route and enable inter-protocol load balancing among static routes and the routes of dynamic routing protocols.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static 2001:db8:2::1 64 2001:db8:1::1 inter-protocol-ecmp

```