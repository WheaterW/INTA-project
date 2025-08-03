peer discard-ext-community(BGP-IPv4 unicast address family view)(IPv6)
======================================================================

peer discard-ext-community(BGP-IPv4 unicast address family view)(IPv6)

Function
--------



The **peer discard-ext-community** command configures a BGP device to discard the extended community attributes carried by routes received from a specified peer.

The **undo peer discard-ext-community** command cancels the configuration.



By default, the extended community attributes in the routing information of peers are not discarded.


Format
------

**peer** *peerIpv6Addr* **discard-ext-community**

**undo peer** *peerIpv6Addr* **discard-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a peer only needs to accepts routes but not extended community attributes, you can run this command on the peer to discard the extended community attributes from the received routes.


Example
-------

# Configure a BGP device to discard the extended community attribute carried by a route.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer fe80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer fe80::1 enable
[*HUAWEI-bgp-af-ipv4] peer fe80::1 discard-ext-community

```