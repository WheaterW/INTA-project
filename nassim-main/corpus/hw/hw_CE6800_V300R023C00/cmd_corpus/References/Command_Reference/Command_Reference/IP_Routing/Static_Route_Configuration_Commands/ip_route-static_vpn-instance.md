ip route-static vpn-instance
============================

ip route-static vpn-instance

Function
--------



The **ip route-static vpn-instance** command configures an IPv4 static route for a VPN instance.

The **undo ip route-static vpn-instance** command deletes an IPv4 static route from a VPN instance.



By default, no IPv4 static routes are configured for a VPN instance.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } { *interface-name* | *interface-type* *interface-number* } [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } *nexthop-address* [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**undo ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } { { *interface-name* | *interface-type* *interface-number* } [ *nexthop-address* ] }

**undo ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } *nexthop-address* [ **public** ] [ **recursive-lookup** **host-route** [ **arp-vlink-only** ] ] [ **preference** *preference* | **tag** *tag* ] \* [ [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inherit-cost** ] | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**undo ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } *nexthop-address* [ **public** ] [ **inherit-cost** ]

**undo ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } { **public** | **vpn-instance** *vpn-destination-name* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } { **public** | **vpn-instance** *vpn-destination-name* } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-source-name* | Specifies the name of a source VPN instance. Each VPN instance has its own routing table. The configured static route is added to the routing table of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *destination-address* | Specifies the destination IP address of a static route. | The value is in dotted decimal notation. |
| *mask* | Specifies the subnet mask. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length. | The value is an integer ranging from 0 to 32. |
| *interface-type* | Specifies the type of the outbound interface of the static route. | - |
| *interface-number* | Specifies the number of the outbound interface of the static route. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *nexthop-address* | Specifies the next hop address of a static route. If the outbound interface is a broadcast interface, the next hop address must be specified. | - |
| **preference** *preference* | Specifies a priority for the static route. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies the tag value of a static route. You can configure different tag values to classify static routes and implement different routing management policies. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **bfd** | Associates a dynamic BFD session with the static route to fast detect faults. | - |
| **enable** | Associates a dynamic BFD session with the static route to fast detect faults. | - |
| **track** | Specify a track object. | - |
| **bfd-session** *cfg-name* | Associates a static BFD session with the static route to fast detect faults.  The undo ip route-static [ track bfd-session ] all command with track bfd-session cfg-name specified dissociates the static route from the current BFD session only without deleting the static route. | The value is a string of 1 to 64 case-sensitive characters. It cannot contain spaces. |
| **nqa** *admin-name* | Associates a static route with an NQA test instance to fast detect faults. The system determines whether to activate a static route based on the link test result of NQA. This helps control static route advertisement and correctly forward the traffic from the remote end.  Currently, only ICMP and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| *test-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| **permanent** | Configures permanent advertisement of the static route.  If service traffic needs to be forwarded along a specified path, regardless of the link status. You can specify permanent to configure permanent advertisement of static routes. | - |
| **arp-detect** *arp-interface-type* | Configures the device to learn the ARP entry of the next hop proactively.  The parameter is used in the following scenarios:   * ARP entries can be learned proactively by the local end, or the learning can be triggered by packet loss during traffic forwarding. Considering that packet loss-triggered ARP entry learning involves packet loss, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. * If the arp-vlink-only parameter is configured to enable the device to recurse the static route only to an ARP Vlink route and the peer end has not the local ARP entry, an ARP VLINK route cannot be generated due to the lack of the ARP entry. Consequently, the static route cannot recurse to an ARP VLINK route. As a result, the static route is not Up. If traffic can be imported only after the static route is advertised by another protocol, traffic cannot be imported because the static route cannot be advertised by another protocol. As a result, the ARP entry cannot be learned. To address this problem, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. | - |
| *arp-interface-number* | Specifies the number of the interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **inter-protocol-ecmp** | Enables inter-protocol load balancing among static routes and the routes of dynamic routing protocols.  If a static route is the optimal or suboptimal route and the optimal and suboptimal routes share the same priority, the static route and the routes of dynamic routing protocols can participate in inter-protocol load balancing.  If inter-protocol load balancing among static routes and the routes of dynamic routing protocols is enabled for any static route in the routing table, the other static routes in the routing table that have the same prefix as that of this static route can also participate in inter-protocol load balancing with the routes of dynamic routing protocols.  Intra-protocol and inter-process load balancing and inter-protocol load balancing are mutually exclusive. If you configure them both, the former takes effect.  Inter-protocol load balancing does not take effect in the following cases:   * Among routes imported using the import-rib command and other routes. * Among black-hole routes and non-black-hole routes. * Among Vlink routes and non-Vlink routes. | - |
| **description** *text* | Specifies the description of a static route. You can configure the description parameter to add a description for a static route so that the administrator can view and maintain the static route.  Description:  You can run the display this (system view) and display current-configuration commands to view the description.  Other command parameters, such as bfd and preference, cannot be configured after the description keyword. The content is only used as the description. For example, if ip route-static 1.1.1.1 255.255.255.255 NULL0 description aa preference 10 is configured, aa preference 10 is used as the description. | The value is a string of 1 to 150 characters, spaces supported. |
| **public** | Indicates that the specified nexthop-address is a public network address. If the nexthop-address parameter is not specified, a device searches the public network forwarding table if the device fails to find a forwarding path in the current VPN instance forwarding table. | - |
| **recursive-lookup** | Recursive route lookup policy. | - |
| **host-route** | Recurses the static route to a 32-bit host route. | - |
| **arp-vlink-only** | Recurses the static route only to an ARP Vlink route. | - |
| **inherit-cost** | Enables the static route to inherit the cost of recursive routes.  If you have specified an outbound interface for a static route, you can no longer specify inherit-cost for the static route. | - |
| *vpn-destination-name* | Specifies the name of the destination VPN instance. If the destination VPN instance is specified and no next hop address is specified, the Next-Table function is configured. In this case, after receiving packets, the device searches the forwarding table of the source VPN instance for a forwarding entry with the destination VPN instance. Then, the device searches the forwarding table of the destination VPN instance for the corresponding forwarding entry. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a simple IPv4 VPN, the **ip route-static vpn-instance** command can be used to configure static routes for this VPN.If the destination address and mask of a static route are all 0s, the static route is a default route.

**Prerequisites**

A VPN instance has been configured using the **ip vpn-instance** command.BFD has been enabled so that static routes can be associated with the BFD session.An NQA test instance has been created so that static routes can be associated with the NQA test instance.

**Follow-up Procedure**

After a static route is configured, import it to the routing protocol running between PEs if you want the route to be sent to the peer PE.

**Precautions**



If a network fault occurs or the network topology changes, static routes do not change automatically. Therefore, exercise caution when configuring static routes.When you configure a static route for a VPN instance, the next hop address can belong to either the VPN instance or the public network. If the next hop of a static route is a public network address, you need to specify public after nexthop-address.If the outbound interface is a broadcast interface, you must specify the next hop address.After the **undo ip route-static vpn-instance** command is executed, all static routes and configurations in the specified VPN instance are deleted. Therefore, exercise caution when running this command.If a static route with a specified next-hop IP address or outbound interface and a static route with only a VPN instance specified as the next hop (no outbound interface or next-hop address, that is, the Next-Table function is configured) are configured for the same destination address, and the two static routes have the same priority, the last configured static route takes effect, and the previous static route is overwritten.For static routes with the same prefix but different priorities, you can configure both a static route with a specified next-hop IP address and a static route with only a VPN instance specified as the next-hop IP address, and a static route with a specified outbound interface and a static route with only a VPN instance specified as the next-hop IP address. Multiple static routes with only VPN instances specified as next hops can be configured.After the static route configuration is saved and the device is restarted in CFG mode, the configuration file sequence may be different from that before the restart.When a static route is associated with a BFD session, if the negotiation status of the BFD session is Up or Admin down, the static route is active. If the negotiation status of the BFD session is Detect Down or the negotiation times out, the static route is inactive. After the device is restarted, the BFD status may change. The active status of static routes is subject to the latest BFD status.If vpn-instance is incorrectly configured, traffic diversion may be abnormal.For example, to recurse the static route 10.1.1.1 in vpn1 to the route 192.168.1.0 in vpn1, run the ip route-static vpn-instance vpn1 10.1.1.1 32 192.168.1.0 command. However, if the ip route-static 10.1.1.1 32 vpn-instance vpn1 192.168.1.0 command is run, the public network static route is recursed to the route 192.168.1.0 of vpn1, which is not as expected.After the **undo bfd** command is run, the BFD parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.After the **undo nqa all-test-instance** command is run, the **NQA** command parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.




Example
-------

# Configure a static route for the VPN instance named vpn1 and configure the device to learn the ARP entry of the next hop 10.11.0.1 proactively.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ip route-static vpn-instance vpn1 1.1.1.1 32 10.11.0.1 arp-detect 100GE1/0/1

```

# Configure a static route for the VPN instance named vpn1. The destination address of the static route is 10.1.1.1/32, and the next hop address is the VPN instance vpn2 address 172.16.1.2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ip vpn-instance vpn2
[*HUAWEI-vpn-instance-vpn2] ipv4-family
[*HUAWEI-vpn-instance-vpn2-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn2] quit
[*HUAWEI] ip route-static vpn-instance vpn1 10.1.1.1 32 vpn-instance vpn2 172.16.1.2

```

# Configure a static route for the VPN instance named vpn1 and enable inter-protocol load balancing among static routes and the routes of dynamic routing protocols.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ip route-static vpn-instance vpn1 1.1.1.1 32 10.11.0.1 inter-protocol-ecmp

```