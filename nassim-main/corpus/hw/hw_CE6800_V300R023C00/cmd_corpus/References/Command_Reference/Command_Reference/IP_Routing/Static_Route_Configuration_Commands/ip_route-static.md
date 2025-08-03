ip route-static
===============

ip route-static

Function
--------



The **ip route-static** command configures an IPv4 unicast static route on the public network.

The **undo ip route-static** command deletes an IPv4 unicast static route from the public network.



By default, no IPv4 unicast static route is configured on the public network.


Format
------

**ip route-static** *ip-address* { *mask* | *mask-length* } *nexthop-address* [ **recursive-lookup** **host-route** [ **arp-vlink-only** ] ] [ **preference** *preference* | **tag** *tag* ] \* [ [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inherit-cost** ] | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**ip route-static** *ip-address* { *mask* | *mask-length* } { *interface-name* | *interface-type* *interface-number* } [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]

**undo ip route-static** *ip-address* { *mask* | *mask-length* } *nexthop-address* **inherit-cost**

**undo ip route-static** *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* *nexthop-address* [ **inherit-cost** ]

**undo ip route-static** *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a destination IP address. | It is in dotted decimal notation. |
| *mask* | Specifies the mask of the IP address. | It is in dotted decimal notation. |
| *mask-length* | Specifies a mask length. The 1s in each 32-bit mask must be consecutive. Therefore, a mask in dotted decimal notation can be presented by a mask length. | The value is an integer ranging from 0 to 32. |
| *nexthop-address* | Specifies the next hop IP address of a route. | It is in dotted decimal notation. |
| **recursive-lookup** | Recursive route lookup policy. | - |
| **host-route** | Recurses the static route to a 32-bit host route. | - |
| **arp-vlink-only** | Recurses the static route only to an ARP Vlink route. | - |
| **preference** *preference* | Specifies a priority for static routes. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies the tag value of a static route. You can configure different tag values to classify static routes and implement different routing management policies. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **bfd** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **enable** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **track** | Specifies a follow object. | - |
| **bfd-session** *cfg-name* | Associates a static BFD session with the static route to fast detect faults.  The undo ip route-static [ track bfd-session ] all command with track bfd-session cfg-name specified dissociates the static route from the current BFD session only without deleting the static route. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| **nqa** *admin-name* | Associates the static route with an NQA test instance to fast detect faults so that the system determines whether to activate the static route based on the NQA link detection result to control route advertisement and guide remote traffic.  Currently, only ICMP NQA test instances and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| *test-name* | Associates a static route with an NQA test instance to fast detect faults. The system determines whether to activate a static route based on the NQA link detection result to control route advertisement and guide traffic from the remote end.  Currently, only ICMP NQA test instances can be associated with static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| **inherit-cost** | Enables the static route to inherit the cost of recursive routes.  If you have specified an outbound interface for a static route, you can no longer specify inherit-cost for the static route. | - |
| **permanent** | Configures permanent advertisement of the static route. | - |
| **arp-detect** *arp-interface-type* | Configures the device to learn the ARP entry of the next hop proactively.  The parameter is used in the following scenarios:   * ARP entries can be learned by the local end or triggered by packet loss during traffic forwarding. Considering that packet loss-triggered ARP entry learning involves packet loss, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. * If the arp-vlink-only parameter is configured to enable the device to recurse the static route only to an ARP Vlink route and the peer end has not the local ARP entry, an ARP Vlink route cannot be generated due to the lack of the ARP entry. Consequently, the static route cannot recurse to an ARP Vlink route. As a result, the static route is not Up. If traffic can be imported only after the static route is advertised by another protocol, traffic cannot be imported because the static route cannot be advertised by another protocol. As a result, the ARP entry cannot be learned. To address this problem, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. | - |
| *arp-interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **inter-protocol-ecmp** | Enables inter-protocol load balancing among static routes and the routes of dynamic routing protocols.  If a static route is the optimal or suboptimal route and the optimal and suboptimal routes share the same priority, the static route and the routes of dynamic routing protocols can participate in inter-protocol load balancing.  If inter-protocol load balancing among static routes and the routes of dynamic routing protocols is enabled for any static route in the routing table, the other static routes in the routing table that have the same prefix as that of this static route can also participate in inter-protocol load balancing with the routes of dynamic routing protocols.  Intra-protocol and inter-process load balancing and inter-protocol load balancing are mutually exclusive. If you configure them both, the former takes effect.  Inter-protocol load balancing does not take effect in the following cases:   * Among routes imported using the import-rib command and other routes. * Among black-hole routes and non-black-hole routes. * Among Vlink routes and non-Vlink routes. | - |
| **description** *text* | Specifies the description of a static route.  Description:  You can run the display this (system view) and display current-configuration commands to view the description.  Other command parameters, such as bfd and preference, cannot be configured after the description keyword. The content is only used as the description. For example, if ip route-static 1.1.1.1 255.255.255.255 NULL0 description aa preference 10 is configured, aa preference 10 is used as the description. | The value is a string of 1 to 150 characters, spaces supported. |
| *interface-type* | Specifies the type of an interface. | -  - |
| *interface-number* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. If the name of a VPN instance is specified, a router searches the routing table of the VPN instance for an outbound interface of the static route based on the next hop IP address specified by the nexthop-address parameter. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces.  If the nexthop-address parameter is not specified, that is, the Next-Table function is configured, the device searches the forwarding table of the specified VPN instance for a forwarding path if no forwarding path is found in the public network forwarding table. |



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

When configuring unicast static routes, pay attention to the following points:

* Only public routes can be recursed to tunnels.
* A static route is associated with a BFD session. When the BFD session goes Down, the static route is inactive.
* When deleting a route, you can specify the preference, tag, and description attributes, but these attributes are not displayed in the command help.
* If both the destination IP address and the subnet mask are 0.0.0.0, the configured route is the default route. If a default static route is incorrectly configured, it may preempt the default route delivered by another protocol. As a result, traffic is forwarded in an incorrect direction. If the routing table fails to be checked, the default route is used to forward packets. In this case, if the Next-Table function, such as ip route-static 0.0.0.0 0 vpn-instance vpn1, is configured, all traffic matching the default public route is imported to the VPN instance. To configure a default private network route, run the **ip route-static vpn-instance** command, for example, ip route-static vpn-instance vpn1 0.0.0.0 0 1.1.1.1.
* Different priorities can be configured to implement different routing management policies. For example, if multiple routes to the same destination are configured with the same priority, load balancing is implemented. If multiple routes to the same destination are configured with different priorities, route backup is implemented.
* When configuring a static route, you can specify the outbound interface, next hop address, or both as required. In fact, the next hop address must be specified for all routing entries. Before sending a packet, the router searches the routing table for the matching route based on the destination address of the packet (following the longest match principle). The link layer can find the corresponding link layer address and forward packets only after the next hop address is specified. Note the following when specifying an outbound interface:
* For a point-to-point interface, specifying the outbound interface means specifying the next hop address. In this case, the address of the peer interface connected to the interface is the next hop address of the route.
* NBMA interfaces support point-to-multipoint networks. In this case, you need to configure IP routes and map IP addresses to link-layer addresses at the link layer. In this case, you need to configure the next hop IP address.
* When configuring a static route, you are not advised to specify a broadcast interface (such as an Ethernet interface) as the outbound interface. The Ethernet interface is a broadcast interface. As a result, multiple next hops exist and the next hop cannot be determined uniquely. In applications, if you must specify a broadcast interface (such as an Ethernet interface) as the outbound interface, you must also specify the next hop address corresponding to the broadcast interface.
* The route is a blackhole route in the following situations:
* Configure a static route and specify the outbound interface as NULL0. The static route is a blackhole route.
* Configure static route recursion. If the recursion result is a blackhole route, the static route is also a blackhole route.
* If the next hop address and outbound interface address of the configured static route are not on the same network segment, traffic may fail to be forwarded.
* An interface has been configured as the outbound interface of a static route. If the IP address of the outbound interface needs to be changed and the new IP address is not on the same network segment as the next hop address of the static route, traffic may fail to be forwarded.
* The **undo ip route-static all** command deletes all static routes and configurations on the public network. Exercise caution when running this command.
* If a static route with a specified next-hop IP address or outbound interface and a static route with only a VPN instance specified as the next hop (no outbound interface or next-hop address, that is, the Next-Table function is configured) are configured for the same destination address, and the two static routes have the same priority, the last configured static route takes effect, and the previous static route is overwritten.
* For static routes with the same prefix but different priorities, you can configure both a static route with a specified next-hop IP address and a static route with only a VPN instance specified as the next-hop IP address, or a static route with a specified outbound interface and a static route with only a VPN instance specified as the next-hop IP address, multiple static routes with only VPN instances specified as next hops can be configured at the same time.
* After the static route configuration is saved and the device is restarted in CFG mode, the configuration file sequence may be different from that before the restart.
* If the prefix of the host route generated after an IPv4 address is configured on an interface conflicts with that of an existing static route, the static route may be replaced in the routing table, which may cause traffic changes.
* When a static route is associated with a BFD session, if the negotiation status of the BFD session is Up or Admin down, the static route is active. If the negotiation status of the BFD session is Detect Down or the negotiation times out, the static route is inactive. After the device is restarted, the BFD status may change. The active status of static routes is subject to the latest BFD status.
* After the **undo bfd** command is run, the BFD parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.
* After the **undo nqa all-test-instance** command is run, the **NQA** command parameters bound to the static route are deleted. As a result, the static route status may change and services may be interrupted.
* If the default static route is incorrectly configured or deleted, unexpected changes may occur in route selection.
* The network segment of the static route must be properly planned. If the mask of the static route is incorrectly configured, traffic will be abnormal.


Example
-------

# Configure the device to learn the ARP entry of the next hop 10.11.0.1 proactively.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 1.1.1.1 32 10.11.0.1 arp-detect 100GE1/0/1

```

# Configure an IPv4 static route and set the next hop address to 10.11.0.1.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 1.1.1.1 32 10.11.0.1

```

# Set the next hop address of the default IPv4 route to 10.2.0.4.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 0.0.0.0 0.0.0.0 10.2.0.4

```

# Configure an IPv4 static route and enable inter-protocol load balancing among static routes and the routes of dynamic routing protocols.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 1.1.1.1 32 10.11.0.1 inter-protocol-ecmp

```

# Associate the IPv4 static route 1.1.1.1/32 with an NQA test instance.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin test
[*HUAWEI-nqa-admin-test] test-type icmp
[*HUAWEI-nqa-admin-test] destination-address ipv4 1.1.1.2
[*HUAWEI-nqa-admin-test] frequency 10
[*HUAWEI-nqa-admin-test] start now
[*HUAWEI-nqa-admin-test] quit
[*HUAWEI] ip route-static 1.1.1.1 32 2.2.2.2 track nqa admin test

```

# Configure an IPv4 static route, set the next hop address to 10.11.0.1, and configure the static route to inherit the cost of recursive routes.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static 1.1.1.1 32 10.11.0.1 inherit-cost

```