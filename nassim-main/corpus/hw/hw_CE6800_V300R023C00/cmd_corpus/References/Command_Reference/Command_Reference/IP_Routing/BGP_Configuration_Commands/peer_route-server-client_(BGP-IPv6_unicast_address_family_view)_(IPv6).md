peer route-server-client (BGP-IPv6 unicast address family view) (IPv6)
======================================================================

peer route-server-client (BGP-IPv6 unicast address family view) (IPv6)

Function
--------



The **peer route-server-client** command enables the route server function on a device and specifies an EBGP peer as its client.

The **peer route-server-client disable** command disables the route server function on a device and cancels the client configuration.

The **undo peer route-server-client** command cancels the route server function and client configuration.

The **undo peer route-server-client disable** command restores the default configuration and takes effect only when the peer route-server-client disable command is run.



By default, the route server function is not enabled on a device, and no EBGP peer is configured as its client.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **route-server-client**

**peer** *ipv6-address* **route-server-client** **disable**

**undo peer** *ipv6-address* **route-server-client**

**undo peer** *ipv6-address* **route-server-client** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The format is X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In some scenarios on the live network, to achieve network traffic interworking, EBGP full-mesh connections may be required. However, establishing full-mesh connections among Routers that function as ASBRs is costly and places high requirements on the performance of the Routers, which adversely affects the network topology and Router expansion. The route server function is similar to the RR function in IBGP scenarios and allows Routers to advertise routes to their clients (ASBR Routers) without changing route attributes, such as AS\_Path, Nexthop, and MED. With the route server function, EBGP full-mesh connections are not required among the ASBR Routers, which reduces network resource consumption.


Example
-------

# Enable the route server function on a device and specify an EBGP peer as its client.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 route-server-client

```