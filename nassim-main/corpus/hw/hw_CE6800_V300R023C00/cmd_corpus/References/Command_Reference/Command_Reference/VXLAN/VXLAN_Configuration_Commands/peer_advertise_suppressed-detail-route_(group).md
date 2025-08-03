peer advertise suppressed-detail-route (group)
==============================================

peer advertise suppressed-detail-route (group)

Function
--------



The **peer advertise suppressed-detail-route** command enables the advertisement of locally suppressed specific routes to peers in a specified BGP EVPN peer group.

The **undo peer advertise suppressed-detail-route** command restores the default configuration.



By default, the locally suppressed specific routes are not advertised to peers in a specified BGP EVPN peer group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **advertise** **suppressed-detail-route**

**undo peer** *group-name* **advertise** **suppressed-detail-route**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP EVPN peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, route summarization is configured to control the scale of BGP routing tables. If route summarization is configured for a BGP-VPN instance address family, the locally suppressed specific routes are by default not advertised to peers in a BGP EVPN peer group. To enable the advertisement of specific routes to peers in a specified BGP EVPN peer group, run the peer advertise suppressed-detail-route command.

**Prerequisites**

The specified peer group has been enabled in the BGP-EVPN address family view.

**Precautions**

The priority of the peer group configuration method is higher than the priority of the global configuration method but lower than the priority of the peer configuration method.


Example
-------

# Enable the advertisement of locally suppressed specific routes to peers in a specified BGP EVPN peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group dcn internal
[*HUAWEI-bgp] peer 10.1.1.9 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer dcn enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 group dcn
[*HUAWEI-bgp-af-evpn] peer dcn advertise suppressed-detail-route

```