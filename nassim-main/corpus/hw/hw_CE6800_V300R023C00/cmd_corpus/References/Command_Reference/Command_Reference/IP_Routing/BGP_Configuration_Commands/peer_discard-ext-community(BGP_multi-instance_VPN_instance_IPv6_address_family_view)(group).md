peer discard-ext-community(BGP multi-instance VPN instance IPv6 address family view)(group)
===========================================================================================

peer discard-ext-community(BGP multi-instance VPN instance IPv6 address family view)(group)

Function
--------



The **peer discard-ext-community** command configures a device to discard the extended community attributes carried in routes of a specified peer.

The **undo peer discard-ext-community** command cancels the configuration.



By default, the extended community attributes in the routing information of peers are not discarded.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **discard-ext-community**

**undo peer** *group-name* **discard-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the device only needs to accept the routes received from a peer group but not the extended community attributes, you can run this command on the peer group to discard the extended community attributes in the received routing information.


Example
-------

# Configure the device to discard the extended community attributes carried in routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance aaa
[*HUAWEI-bgp-instance-aaa] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-instance-aaa-6-vpn1] group test external
[*HUAWEI-bgp-instance-aaa-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-instance-aaa-6-vpn1] peer test discard-ext-community

```