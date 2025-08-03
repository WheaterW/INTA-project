peer as-path-filter import (BGP-VPN instance IPv6 address family view) (group)
==============================================================================

peer as-path-filter import (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer as-path-filter import** command configures a BGP route filtering policy based on the AS\_Path for the routes received from a peer group.

The **undo peer as-path-filter import** command cancels the existing configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes received from peers in a peer group, and all the received BGP routes will be permitted.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **as-path-filter** { *number* | *name* } **import**

**undo peer** *group-name* **as-path-filter** { *number* | *name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *number* | Specifies the number of the AS\_Path filter. | The value is a decimal integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the **peer as-path-filter import** command is run to apply a routing policy to BGP routes received from a specified peer group, the AS\_Path filter filters out unqualified routes.

**Prerequisites**

Before configuring a BGP route-filter based on the AS\_Path, you must run the **ip as-path-filter** command to define an AS\_Path filter first.

**Precautions**

Only one AS\_Path filter can be used to filter the routes received from the same peer. Similarly, only one AS\_Path filter can be used to filter routes to be received from the same peer.


Example
-------

# Configure an AS\_Path filter for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test external
[*HUAWEI-bgp-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-6-vpn1] peer test as-path-filter 3 import

```