peer discard-ext-community(BGP-VPN instance IPv4 address family view/BGP-labeled VPN instance IPv4 address family view)
=======================================================================================================================

peer discard-ext-community(BGP-VPN instance IPv4 address family view/BGP-labeled VPN instance IPv4 address family view)

Function
--------



The **peer discard-ext-community** command configures a device to discard the extended community attributes carried by routes received from a specified peer.

The **undo peer discard-ext-community** command cancels the configuration.



By default, the extended community attributes in the routing information of peers are not discarded.


Format
------

**peer** *ipv4-address* **discard-ext-community**

**undo peer** *ipv4-address* **discard-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv4 address family view


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
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] peer 10.1.1.1 discard-ext-community

```