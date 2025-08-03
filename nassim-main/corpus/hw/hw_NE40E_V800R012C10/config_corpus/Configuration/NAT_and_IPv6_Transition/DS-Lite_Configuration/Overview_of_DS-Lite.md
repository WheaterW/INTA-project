Overview of DS-Lite
===================

Dual-Stack Lite (DS-Lite) uses IPv4-in-IPv6 tunneling and IPv4 Network Address Translation (NAT) techniques to allow private IPv4 users to travel through IPv6 networks to access public IPv4 networks.

#### Background

In IPv4 to IPv6 transition, IPv6 networks are scaled up, and plans to establish IPv4 networks are being phased out. All backbone networks support the IPv4 and IPv6 dual-logic planes, and new devices on metropolitan area networks (MANs) primarily run either the IPv4/IPv6 dual stack or only IPv6 (by application service providers [ASPs]). IPv6 and IPv4 coexist dynamically and in an order. These network deployment methods help carriers achieve the following goals:

* Provide the same user experience when users access IPv6 and IPv4 services.
* Allow IPv6 users to properly access IPv4 networks.
* Ensure that services are not compromised after IPv4 users are migrated to IPv6 networks.

Since the mainstream operating systems support the IPv4 and IPv6 dual stack and user preferences differ, network providers have to provide both IPv4 and IPv6 services during the transition. This, however, does not mean that networks must support the IPv4 and IPv6 dual stack. In smooth evolution from IPv4 network to IPv6 network, network carriers use different evolution solutions and network models in each evolution phase based on infrastructure.

The tunneling technique is used in the primary phase of network IPv4-to-IPv6 evolution. In this phase, legacy access IPv4 networks cannot be upgraded to IPv6. A few IPv6 users are scattered on the networks. This means the cost of a network upgrade to IPv6 is high, and the input-output ratio is low, reducing the possibility of an upgrade to IPv6. As a result, the churn rate of IPv6 users increases. To address this problem, the tunneling technique can be used to allow IPv6 users to travel through IPv4 networks.

In addition to the tunneling technique, IPv4 and IPv6 dual-stack networks can be deployed. Such networks apply when both IPv4 traffic and IPv6 traffic are in a large volume during transition and when devices on new carrier networks are capable of IPv6. DS-Lite is used on such networks.


#### DS-Lite Technical Characteristics

A DS-Lite network consists of IPv4 and IPv6 dual-stack hosts and IPv6 networks. On a DS-Lite network, customer premises equipment (CPE) functioning as a home gateway and Carrier Grade NAT (CGN) devices functioning as carrier-class gateways run the IPv4 and IPv6 dual stack, and the other network devices run only IPv6. DS-Lite devices must support both IPv4-in-IPv6 tunnels and NAT44. Home users obtain both IPv6 and private IPv4 addresses and send user packets to a CPE. The CPE forwards the packets as follows:

* Forwards IPv6 user packets directly to an IPv6-only network.
* Forwards IPv4 packets to a DS-Lite device through an IPv4-in-IPv6 tunnel established between the CPE and DS-Lite device. Upon receipt of the packets, the DS-Lite device forwards them to a CGN device. The CGN device decapsulates tunnel information, converts each private IPv4 address to a public IPv4 address, and sends each packet to an IPv4 network.

IPv6-only DS-Lite networks are used when the networks are incapable of maintaining a large number of tunnels on a network, for example, a wireless network that focuses on transport efficiency, whereas tunnels increase costs. IPv6-only DS-Lite networks are also used on new sites or in the later phase of IPv6 evolution.


#### DS-Lite Functions

DS-Lite functions are as follows:

* Supports inter-board hot and warm backup.
* Supports the application level gateway (ALG) function, internal server function, and one-to-one and one-to-multiple translation between private and public network information.
* Supports distributed and centralized DS-Lite scenarios.
* Uses a NAT policy template delivered by a Remote Authentication Dial In User Service (RADIUS) server to implement the ALG, to adjust the aging time, and assign ports.