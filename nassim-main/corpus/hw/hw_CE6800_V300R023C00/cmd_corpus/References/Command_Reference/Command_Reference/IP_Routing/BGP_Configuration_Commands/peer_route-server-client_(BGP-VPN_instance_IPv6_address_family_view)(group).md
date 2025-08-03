peer route-server-client (BGP-VPN instance IPv6 address family view)(group)
===========================================================================

peer route-server-client (BGP-VPN instance IPv6 address family view)(group)

Function
--------



The **peer route-server-client** command enables the route server function on a device and specifies an EBGP peer group as its client.

The **undo peer route-server-client** command cancels the route server function and client configuration.



By default, the route server function is not enabled on a device, and no EBGP peer group is configured as its client.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerGroupName* **route-server-client**

**undo peer** *peerGroupName* **route-server-client**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In some scenarios on the live network, to achieve network traffic interworking, EBGP full-mesh connections may be required. However, establishing full-mesh connections among Routers that function as ASBRs is costly and places high requirements on the performance of the Routers, which adversely affects the network topology and Router expansion. The route server function is similar to the RR function in IBGP scenarios and allows Routers to advertise routes to their clients (ASBR Routers) without changing route attributes, such as AS\_Path, Nexthop, and MED. With the route server function, EBGP full-mesh connections are not required among the ASBR Routers, which reduces network resource consumption.


Example
-------

# Enable the route server function on a device and specify an EBGP peer group as its client.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] group test external
[*HUAWEI-bgp-6-vpna] peer test as-number 200
[*HUAWEI-bgp-6-vpna] peer test route-server-client

```