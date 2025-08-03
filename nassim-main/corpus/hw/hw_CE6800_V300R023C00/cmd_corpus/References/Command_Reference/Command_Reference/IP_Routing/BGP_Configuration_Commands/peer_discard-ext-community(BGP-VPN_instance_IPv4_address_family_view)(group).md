peer discard-ext-community(BGP-VPN instance IPv4 address family view)(group)
============================================================================

peer discard-ext-community(BGP-VPN instance IPv4 address family view)(group)

Function
--------



The **peer discard-ext-community** command configures a device to discard the extended community attributes carried by routes received from a specified peer.

The **undo peer discard-ext-community** command cancels the configuration.



By default, the extended community attributes in the routing information of peers are not discarded.


Format
------

**peer** *group-name* **discard-ext-community**

**undo peer** *group-name* **discard-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the device only needs to accept the routes received from a peer group but not the extended community attributes, you can run this command on the peer group to discard the extended community attributes in the received routing information.


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
[*HUAWEI-bgp-vpna] group test
[*HUAWEI-bgp-vpna] peer test discard-ext-community

```