ip route-static vpn-instance (VPN)
==================================

ip route-static vpn-instance (VPN)

Function
--------



The **ip route-static vpn-instance** command configures an IPv4 static route for a VPN instance.

The **undo ip route-static vpn-instance** command deletes an IPv4 static route from a VPN instance.



By default, no IPv4 static routes are configured for a VPN instance.


Format
------

**ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } **vpn-instance** *vpn-destination-name* *nexthop-address* [ **recursive-lookup** **host-route** [ **arp-vlink-only** ] ] [ **preference** *preference* | **tag** *tag* ] \* [ [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inherit-cost** ] | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**undo ip route-static vpn-instance** *vpn-source-name* *destination-address* { *mask* | *mask-length* } **vpn-instance** *vpn-destination-name* *nexthop-address* [ **inherit-cost** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-source-name* | Specifies the name of a source VPN instance. Each VPN instance has its own routing table. The configured static route is added to the routing table of the specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *destination-address* | Specifies the destination IP address of a static route. | It is in dotted decimal notation. |
| *mask* | Specifies the subnet mask of the destination address. | It is in dotted decimal notation. |
| *mask-length* | Specifies the mask length. | The value is an integer ranging from 0 to 32. |
| **vpn-instance** *vpn-destination-name* | Specifies the name of the destination VPN instance. If the name of the destination VPN instance is specified, the device searches the routing table of the destination VPN instance for the static route's outbound interface based on the configured next hop address. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *nexthop-address* | Specifies the next hop address of a static route. If the outbound interface is a broadcast interface, the next hop address must be specified. | - |
| **recursive-lookup** | Recursive route lookup policy. | - |
| **host-route** | Recurses the static route to a 32-bit host route. | - |
| **arp-vlink-only** | Recurses the static route only to an ARP Vlink route. | - |
| **preference** *preference* | Specifies a priority for static routes. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies a tag value for the static route. The tag can be used by a routing policy. For example, the tag can be used during route import. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **bfd** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **enable** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **track** | Specify a track object. | - |
| **bfd-session** *cfg-name* | Associates a static BFD session with the static route to fast detect faults.  The undo ip route-static [ track bfd-session ] all command with track bfd-session cfg-name specified dissociates the static route from the current BFD session only without deleting the static route. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| **nqa** *admin-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| *test-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| **inherit-cost** | Enables the static route to inherit the cost of recursive routes. | - |
| **permanent** | Configures permanent advertisement of the static route.  If service traffic needs to be forwarded along a specified path, regardless of the link status, you can specify permanent to configure permanent advertisement of static routes. | - |
| **arp-detect** *arp-interface-type* | Configures the device to learn the ARP entry of the next hop proactively.  The parameter is used in the following scenarios:   * ARP entries can be learned by the local end or triggered by packet loss during traffic forwarding. Considering that packet loss-triggered ARP entry learning involves packet loss, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. * If the arp-vlink-only parameter is configured to enable the device to recurse the static route only to an ARP Vlink route and the peer end has not the local ARP entry, an ARP Vlink route cannot be generated due to the lack of the ARP entry. Consequently, the static route cannot recurse to an ARP Vlink route. As a result, the static route is not Up. If traffic can be imported only after the static route is advertised by another protocol, traffic cannot be imported because the static route cannot be advertised by another protocol. As a result, the ARP entry cannot be learned. To address this problem, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. | - |
| *arp-interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **inter-protocol-ecmp** | Enables inter-protocol load balancing among static routes and the routes of dynamic routing protocols.  If a static route is the optimal or suboptimal route and the optimal and suboptimal routes share the same priority, the static route and the routes of dynamic routing protocols can participate in inter-protocol load balancing.  If inter-protocol load balancing among static routes and the routes of dynamic routing protocols is enabled for any static route in the routing table, the other static routes in the routing table that have the same prefix as that of this static route can also participate in inter-protocol load balancing with the routes of dynamic routing protocols.  Intra-protocol and inter-process load balancing and inter-protocol load balancing are mutually exclusive. If you configure them both, the former takes effect.  Inter-protocol load balancing does not take effect in the following cases:   * Among routes imported using the import-rib command and other routes. * Among black-hole routes and non-black-hole routes. * Among Vlink routes and non-Vlink routes. | - |
| **description** *text* | Specifies the description of a static route. You can configure the description parameter to add a description for a static route so that the administrator can view and maintain the static route.  Description:  You can run the display this (system view) and display current-configuration commands to view the description.  Other command parameters, such as bfd and preference, cannot be configured after the description keyword. The content is only used as the description. For example, if ip route-static 1.1.1.1 255.255.255.255 NULL0 description aa preference 10 is configured, aa preference 10 is used as the description. | The value is a string of 1 to 150 characters, spaces supported. |



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

A VPN instance has been created using the **ip vpn-instance** command.BFD has been enabled so that static routes can be associated with the BFD session.An NQA test instance has been created so that static routes can be associated with the NQA test instance.

**Follow-up Procedure**

If a configured static route needs to be sent to the peer PE, import the static route into BGP running between the PEs.


Example
-------

# Configure a static route for the VPN instance named vpn1. The destination address of the static route is 10.1.1.1/32, and the next hop address is 172.16.1.2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[~HUAWEI] ip route-static vpn-instance vpn1 10.1.1.1 32 172.16.1.2

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

# Configure a static route for the VPN instance named vpn1 and configure the device to learn the ARP entry of the next hop 10.11.0.1 proactively.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[~HUAWEI] ip route-static vpn-instance vpn1 1.1.1.1 32 10.11.0.1 arp-detect 100GE1/0/1

```

# Configure a static route for the VPN instance named vpn1 and enable inter-protocol load balancing among static routes and the routes of dynamic routing protocols.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[~HUAWEI] ip route-static vpn-instance vpn1 1.1.1.1 32 10.11.0.1 inter-protocol-ecmp

```