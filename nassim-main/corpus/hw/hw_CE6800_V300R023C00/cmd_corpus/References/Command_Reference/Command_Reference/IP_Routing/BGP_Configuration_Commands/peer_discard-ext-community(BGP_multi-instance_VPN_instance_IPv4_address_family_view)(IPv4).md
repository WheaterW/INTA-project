peer discard-ext-community(BGP multi-instance VPN instance IPv4 address family view)(IPv4)
==========================================================================================

peer discard-ext-community(BGP multi-instance VPN instance IPv4 address family view)(IPv4)

Function
--------



The **peer discard-ext-community** command configures a BGP device to discard the extended community attributes carried by routes received from a specified peer.

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
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If a peer only needs to accepts routes but not extended community attributes, you can run this command on the peer to discard the extended community attributes from the received routes.




Example
-------

# Configure a BGP device to discard the extended community attribute carried by a route.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vpna] peer 10.1.1.1 discard-ext-community

```