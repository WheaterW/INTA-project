ip route-static (VPN)
=====================

ip route-static (VPN)

Function
--------



The **ip route-static** command configures an IPv4 static route on the public network.



By default, no IPv4 static route is configured on the public network.


Format
------

**ip route-static** *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* *nexthop-address* [ **recursive-lookup** **host-route** [ **arp-vlink-only** ] ] [ **preference** *preference* | **tag** *tag* ] \* [ [ **bfd** **enable** | **track** { **bfd-session** *cfg-name* | **nqa** *admin-name* *test-name* } ] [ **inherit-cost** ] | **permanent** ] [ **arp-detect** { *arp-interface-name* | *arp-interface-type* *arp-interface-number* } ] [ **inter-protocol-ecmp** ] [ **description** *text* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *mask* | Specifies a subnet mask. | The value is in dotted decimal notation. |
| *mask-length* | Specifies a mask length. The 32-bit mask requires consecutive 1s. Therefore, the mask in dotted decimal notation can be replaced by the mask length. | The value is an integer in the range from 0 to 32. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the destination VPN instance. If the name of the destination VPN instance is specified, the device searches the routing table of the destination VPN instance for the static route's outbound interface based on the configured next hop address. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *nexthop-address* | Specifies the next-hop IP address. | The value is in dotted decimal notation. |
| **recursive-lookup** | Recurses the static route to a 32-bit host route. | - |
| **host-route** | Recurses the static route to a host route. | - |
| **arp-vlink-only** | Recurses the static route only to an ARP Vlink route. | - |
| **preference** *preference* | Specifies a priority for the static route. | The value is an integer that ranges from 1 to 255. The default value is 60. A smaller value indicates a higher preference. |
| **tag** *tag* | Specifies a tag value for the static route. The tag can be used by a routing policy. For example, the tag can be used during route import. | The value is an integer ranging from 1 to 4294967295. The default value is 0. |
| **bfd** | Associates a dynamic BFD session with the static route to fast detect faults. | - |
| **enable** | Binds a dynamic BFD session to static routes to quickly detect faults. | - |
| **track** | Specifies the object to be traced. | - |
| **bfd-session** *cfg-name* | Associates a static BFD session with the static route to fast detect faults.  The undo ip route-static [ track bfd-session ] all command with track bfd-session cfg-name specified dissociates the static route from the current BFD session only without deleting the static route. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| **nqa** *admin-name* | Associates a static route with an NQA test instance to fast detect faults. The system determines whether to activate a static route based on the link test result of NQA. This helps control static route advertisement and correctly forward the traffic from the remote end.  Currently, only ICMP and TCP NQA test instances can be bound to static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| *test-name* | Associates a static route with an NQA test instance to fast detect faults. The system determines whether to activate a static route based on the NQA link detection result to control route advertisement and guide traffic from the remote end.  Currently, only ICMP NQA test instances can be associated with static routes to implement fast fault detection. | The value is a string of 1 to 32 case-sensitive characters. |
| **inherit-cost** | Enables the static route to inherit the cost of recursive routes.  If you have specified an outbound interface for a static route, you can no longer specify inherit-cost for the static route. | - |
| **permanent** | Configures permanent advertisement of the static route. | - |
| **arp-detect** *arp-interface-type* | Configures the device to learn the ARP entry of the next hop proactively.  The parameter is used in the following scenarios:   * ARP entries can be learned proactively by the local end, or the learning can be triggered by packet loss during traffic forwarding. Considering that packet loss-triggered ARP entry learning involves packet loss, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. * If the arp-vlink-only parameter is configured to enable the device to recurse the static route only to an ARP Vlink route and the peer end has not the local ARP entry, an ARP VLINK route cannot be generated due to the lack of the ARP entry. Consequently, the static route cannot recurse to an ARP VLINK route. As a result, the static route is not Up. If traffic can be imported only after the static route is advertised by another protocol, traffic cannot be imported because the static route cannot be advertised by another protocol. As a result, the ARP entry cannot be learned. To address this problem, specify arp-detect interface-type interface-number to configure the device to learn the ARP entry of the next hop proactively. | - |
| *arp-interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **inter-protocol-ecmp** | Enables inter-protocol load balancing among static routes and the routes of dynamic routing protocols.  If a static route is the optimal or suboptimal route and the optimal and suboptimal routes share the same priority, the static route and the routes of dynamic routing protocols can participate in inter-protocol load balancing. If inter-protocol load balancing among static routes and the routes of dynamic routing protocols is enabled for any static route in the routing table, the other static routes in the routing table that have the same prefix as that of this static route can also participate in inter-protocol load balancing with the routes of dynamic routing protocols.  Intra-protocol and inter-process load balancing and inter-protocol load balancing are mutually exclusive. If you configure them both, the former takes effect.  Inter-protocol load balancing does not take effect in the following cases:   * Among routes imported using the import-rib command and other routes. * Among black-hole routes and non-black-hole routes. * Among Vlink routes and non-Vlink routes. | - |
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

**Prerequisites**



BFD must have been enabled when you bind a static route to a BFD session.An NQA test instance must have been created when you bind it to a static route.The function that allows static routes to recurse to ARP Vlink direct routes must have been enabled globally using the **ip route recursive-lookup arp vlink-direct-route protocol static** command when you enable a device to recurse a static route only to an ARP Vlink route.



**Precautions**

When configuring unicast static routes, pay attention to the following points:

* Only public network routes can recurse to tunnels.
* When deleting a route, you can specify the preference, tag, and description attributes, but these attributes are not displayed in the command help.
* If both the destination IP address and the mask are 0.0.0.0, the configured route is a default route. If a static default route is incorrectly configured, it may preempt the default route delivered by another protocol. As a result, traffic is transmitted along an incorrect path. If the device fails to find a matching entry in the routing table, it uses the default route to forward packets. In this case, if the Next-Table function, such as ip route-static 0.0.0.0 0 vpn-instance vpn1, is configured, all traffic that matches the default public network route is imported to the VPN instance. To configure a default VPN route, run the **ip route-static vpn-instance** command, for example, ip route-static vpn-instance vpn1 0.0.0.0 0 1.1.1.1.
* Setting different preferences can implement different routing management policies. For example, if multiple routes with the same preference value are configured for the same destination, load balancing is implemented among the routes. If different preference values are configured for these routes, route backup is implemented.
* When configuring a static route, you can specify an outbound interface using interface-type interface-number, a nexthop address using nexthop-address, or both as required. Each routing entry requires a next hop address. When sending a packet, the device searches the routing table for the matched route based on the destination address of the packet (following the longest match rule). The corresponding link-layer address can be found and packets can be forwarded only after the next-hop IP address is specified. Note the following when specifying an outbound interface:
  + When a P2P interface is specified as an outbound interface, this operation also implicitly specifies a next-hop IP address. This is because the IP address of the interface directly connected to the outbound interface is used as the next-hop IP address.
  + Non-Broadcast Multiple-Access (NBMA) interfaces apply to point-to-multipoint (P2MP) networks. In addition to IP routes, mappings between IP and link-layer addresses must be established. In this case, next hop IP addresses need to be configured.
  + An Ethernet interface is a broadcast interface and a virtual-template (VT) interface can be associated with multiple virtual access (VA) interfaces. If an Ethernet or VT interface is specified as the outbound interface of a static route, the next hop cannot be determined because multiple next hops exist. Therefore, do not specify a broadcast interface (Ethernet interface for example) or a VT interface as the outbound interface of a static route unless necessary. In actual applications, to specify a broadcast interface (such as an Ethernet interface) or a VT interface as the outbound interface, you need to specify a next hop address along with the outbound interface.
* The following routes are blackhole routes:
  + The static route with the outbound interface NULL0 is a blackhole route.
  + The static route that recurses to a blackhole route is also a blackhole route.
* If the next hop address and outbound interface address of a static route are not on the same network segment, traffic may fail to be forwarded.
* If the IP address of the outbound interface specified for a static route is changed to an IP address that is not on the same network segment as the next-hop IP address of the static route, traffic may fail to be forwarded.
* If the **undo ip route-static all** command is run, all static routes and configurations on the public network are deleted. Therefore, exercise caution when running the command.
* After the static route configuration is saved and the device is restarted in CFG mode, the configuration file sequence may be different from that before the restart.
* The **undo ip route-static** command deletes an IPv4 unicast static route.
* If two static routes with the same destination address and the same preference value are configured, one of the static routes has a next-hop IP address or outbound interface specified, and the other static route has only a VPN instance (without an outbound interface or next-hop IP address, that is, the Next-Table function is enabled) specified for the next hop, the latest configuration overrides the previous one.
* For static routes with the same prefix but different preferences, you can configure a static route with a specified next-hop IP address and a static route with only a VPN instance specified as the next hop; in addition, you can configure a static route with a specified outbound interface and a static route with only a VPN instance specified as the next hop; you can also configure multiple static routes with only VPN instances specified as next hops.
* If the prefix of the host route generated after an IPv4 address is configured on an interface conflicts with that of an existing static route, the static route may be replaced in the routing table, which may cause traffic changes.
* When a static route is associated with a BFD session, if the negotiation status of the BFD session is Up or Admin down, the static route is active. If the negotiation status of the BFD session is Detect Down or the negotiation times out, the static route is inactive. After the device is restarted, the BFD status may change. The active status of static routes is subject to the latest BFD status.
* If vpn-instance is incorrectly configured, traffic diversion may be abnormal.
  + For example, to configure a device to recurse a public network static route to the route 192.168.1.0 of vpn1, run the ip route-static 10.1.1.1 32 vpn-instance vpn1 192.168.1.0 command. If the ip route-static vpn-instance vpn1 10.1.1.1 32 192.168.1.0 command is run, the static route 10.1.1.1 in vpn1 is recursed to the route 192.168.1.0 in vpn1, which does not meet the expectation.
* If a static default route is incorrectly configured or deleted, unexpected changes may occur in route selection.
* The network segment of the static route must be properly planned. If the mask of the static route is incorrectly configured, traffic will be abnormal.
* If the **undo bfd** command is run, the BFD parameters bound to the static route are deleted. As a result, the static route status may change, and services may be interrupted.
* Running the **undo nqa all-test-instance** command will delete the parameters of the NQA test instance bound to the static route. As a result, the static route status may change, and services may be interrupted.


Example
-------

# Configure an IPv4 static route and set the next hop address to 10.11.0.1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ip route-static 1.2.3.4 32 vpn-instance vpn1 10.11.0.1

```