peer route-server-client (BGP-IPv4 unicast address family view)
===============================================================

peer route-server-client (BGP-IPv4 unicast address family view)

Function
--------



The **peer route-server-client** command enables the route server function on a device and specifies an EBGP peer as its client.

The **peer route-server-client disable** command disables the route server function on a device and cancels the client configuration.

The **undo peer route-server-client** command cancels the route server function and client configuration.

The **undo peer route-server-client disable** command restores the default configuration and takes effect only when the peer route-server-client disable command is run.



By default, the route server function is not enabled on a device, and no EBGP peer is configured as its client.


Format
------

**peer** *ipv4-address* **route-server-client**

**peer** *ipv4-address* **route-server-client** **disable**

**undo peer** *ipv4-address* **route-server-client**

**undo peer** *ipv4-address* **route-server-client** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is an IPv4 address, in dotted decimal notation. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In some scenarios on the live network, to achieve network traffic interworking, EBGP full-mesh connections may be required. However, establishing full-mesh connections among Routers that function as ASBRs is costly and places high requirements on the performance of the Routers, which adversely affects the network topology and Router expansion. The route server function is similar to the RR function in IBGP scenarios and allows Routers to advertise routes to their clients (ASBR Routers) without changing route attributes, such as AS\_Path, Nexthop, and MED. With the route server function, EBGP full-mesh connections are not required among the ASBR Routers, which reduces network resource consumption.




Example
-------

# Enable the route server function on a device and specify an EBGP peer as its client.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.2 route-server-client

```