ipv6 route-static vpn-instance
==============================

ipv6 route-static vpn-instance

Function
--------



The **ipv6 route-static vpn-instance** command configures IPv6 static routes for an IPv6 address family-enabled VPN instance.

The **undo ipv6 route-static vpn-instance** command deletes the IPv6 static routes configured for an IPv6 address family-enabled VPN instance.



By default, no IPv6 static routes are configured for an IPv6 address family-enabled VPN instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 route-static vpn-instance** *vpn-source-name* *dest-ipv6-address* *prefix-length* { **vpn-instance** *vpn-destination-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* [ **public** ] } [ **recursive-lookup** **host-route** ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**ipv6 route-static vpn-instance** *vpn-source-name* *dest-ipv6-address* *prefix-length* { **vpn-instance** *vpn-destination-name* | **public** } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]

**undo ipv6 route-static vpn-instance** *vpn-source-name* *dest-ipv6-address* *prefix-length* [ { *interface-name* | *interface-type* *interface-number* } [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-destination-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* [ **public** ] ]

**undo ipv6 route-static vpn-instance** *vpn-source-name* *dest-ipv6-address* *prefix-length* { **vpn-instance** *vpn-destination-name* | **public** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 route-static vpn-instance** *vpn-source-name* *dest-ipv6-address* *prefix-length* { *interface-name* | *interface-type* *interface-number* } [ *nexthop-ipv6-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ipv6 route-static vpn-instance** *vpn-source-name* *dest-ipv6-address* *prefix-length* { **vpn-instance** *vpn-destination-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* [ **public** ] } [ **recursive-lookup** **host-route** ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] **inherit-cost** [ **inter-protocol-ecmp** ] [ **description** *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-source-name* | Specifies the name of a source VPN instance. Each VPN instance has its own routing table. The configured static routes are added to the routing table of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. In addition, the VPN instance name must not be \_public\_. The character string can contain spaces if it is enclosed in double quotation marks (""). |
| *dest-ipv6-address* | Specifies a destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| *prefix-length* | Specifies the length of an IPv6 prefix. | It is an integer ranging from 0 to 128. |
| **vpn-instance** *vpn-destination-name* | Specifies the destination VPN instance. A static route searches the destination VPN instance for an outbound interface based on the configured nexthop-ipv6-address. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (").  If nexthop-ipv6-address is not specified, the next-table function is configured. After receiving a packet, the device searches the forwarding table of the source VPN instance for the destination VPN instance, and then searches the forwarding table of the destination VPN instance for the forwarding path. |
| *nexthop-ipv6-address* | Specifies the next hop IPv6 address of the device. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **public** | Indicates the public network address of a gateway. After a certain Device is configured in an IPv6 address family-enabled VPN instance, the next hop or the next hop gateway of the Device belongs to this IPv6 address family-enabled VPN instance and the public network. If the keyword public is specified in the command, the next hop is specified as a public network device. | - |
| **recursive-lookup** | Recursive route lookup policy. | - |
| **host-route** | Recurses the static route to a 128-bit host route. | - |
| **preference** *preference* | Specifies the priority of a route. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies the tag value of a static route. You can configure different tag values to classify static routes and implement different routing management policies. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **bfd** | Associates a dynamic BFD session with the static route to fast detect faults. | - |
| **enable** | Associates a dynamic BFD session with the static route to fast detect faults. | - |
| **track** | Specify a track object. | - |
| **bfd-session** *cfg-name* | Associates a static BFD session with the static route to fast detect faults.  The undo ip route-static [ track bfd-session ] all command with track bfd-session cfg-name specified dissociates the static route from the current BFD session only without deleting the static route. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **nqa** *admin-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| *test-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| **inter-protocol-ecmp** | If a static route is the optimal or suboptimal route and the optimal and suboptimal routes share the same priority, the static route and the routes of dynamic routing protocols can participate in inter-protocol load balancing.  If inter-protocol load balancing among static routes and the routes of dynamic routing protocols is enabled for any static route in the routing table, the other static routes in the routing table that have the same prefix as that of this static route can also participate in inter-protocol load balancing with the routes of dynamic routing protocols.  Intra-protocol and inter-process load balancing and inter-protocol load balancing are mutually exclusive. If you configure them both, the former takes effect.  Inter-protocol load balancing does not take effect in the following cases:   * Among routes imported using the import-rib command and other routes. * Among black-hole routes and non-black-hole routes. * Among Vlink routes and non-Vlink routes. | - |
| **description** *text* | Specifies a description of a static route.  You can run the display this (system view) and display current-configuration commands to view the description.  Other command parameters, such as bfd and preference, cannot be configured after the description keyword. The content is only used as the description. For example, if ipv6 route-static 2001:db8:1::1 128 NULL0 description aa preference 10 is configured, aa preference 10 is used as the description. | The value is a string of 1 to 150 characters, spaces supported. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **inherit-cost** | Enables a static route to inherit the cost of recursive routes. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure static routes for a simple IPv6 VPN, run the **ipv6 route-static vpn-instance** command.If the destination address and mask of a static route are all 0s, the static route is a default route.

**Prerequisites**

A VPN instance has been configured using the **ip vpn-instance** command.BFD has been enabled so that static routes can be associated with the BFD session.An NQA test instance has been created so that static routes can be associated with the NQA test instance.

**Configuration Impact**

A static route can be bound to only one BFD session. To bind a static route to another session, you need to unbind the static route from the current BFD session first.

**Follow-up Procedure**

After a static route is configured, import it to the routing protocol running between PEs if you want the route to be sent to the peer PE.

**Precautions**



If a network fault occurs or the network topology changes, static routes do not change automatically. Therefore, exercise caution when configuring static routes.When you configure a static route for a VPN instance, the next hop address can belong to either the VPN instance or the public network. If the next hop of a static route is a public network address, you need to specify public after nexthop-address.If the outbound interface is a broadcast interface, you must specify the next hop address.If a static route with a specified next-hop IP address or outbound interface and a static route with only a VPN instance specified as the next hop (no outbound interface or next-hop address, that is, the Next-Table function is configured) are configured for the same destination address, and the two static routes have the same priority, the last configured static route takes effect, and the previous static route is overwritten.For static routes with the same prefix but different priorities, you can configure both a static route with a specified next-hop IP address and a static route with only a VPN instance specified as the next-hop IP address, and a static route with a specified outbound interface and a static route with only a VPN instance specified as the next-hop IP address. Multiple static routes with only VPN instances specified as next hops can be configured at the same time.After the static route configuration is saved and the device is restarted in CFG mode, the configuration file sequence may be different from that before the restart.When a static route is associated with a BFD session, if the negotiation status of the BFD session is Up or Admin down, the static route is active. If the negotiation status of the BFD session is Detect Down or the negotiation times out, the static route is inactive. After the device is restarted, the BFD status may change. Whether the static route is active is subject to the latest BFD status.If vpn-instance is incorrectly configured, traffic diversion may be abnormal.For example, to recurse the static route 2001:db8:1::1 in vpn1 to the route 2001:db8:2::2 in vpn1, run the ipv6 route-static vpn-instance vpn1 2001:db8:1::1 128 2001:db8:2::2 command. However, if the ipv6 route-static 2001:db8:1::1 128 vpn-instance vpn1 2001:db8:2::2 command is run, the public network static route is recursed to the route 2001:db8:2::2 of vpn1, which is not as expected.If the default static route is incorrectly configured or deleted, unexpected changes may occur in route selection.The network segment of the static route must be properly planned. If the mask of the static route is incorrectly configured, traffic will be abnormal.After the **undo bfd** command is run, the BFD parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.After the **undo nqa all-test-instance** command is run, the **NQA** command parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.




Example
-------

# Configure an IPv6 static route for the VPN instance named vpn1 and enable inter-protocol load balancing among static routes and the routes of dynamic routing protocols.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[~HUAWEI] ip vpn-instance vpn2
[*HUAWEI-vpn-instance-vpn2] ipv6-family
[*HUAWEI-vpn-instance-vpn2-af-ipv6] quit
[*HUAWEI] ipv6 route-static vpn-instance vpn1 :: 0 vpn-instance vpn2 2001:db8:1::2 inter-protocol-ecmp

```

# Configure a default route with next hop 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI] ipv6 route-static vpn-instance vpn1 :: 0 2001:db8:1::1

```