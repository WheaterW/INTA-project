peer as-path-filter import (BGP-IPv4 unicast address family view) (IPv6)
========================================================================

peer as-path-filter import (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer as-path-filter import** command configures a policy based on an AS\_Path list for filtering BGP routes received from a peer.

The **undo peer as-path-filter import** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes received from a peer, and all the BGP routes will be received from the peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **as-path-filter** { *number* | *name* } **import**

**undo peer** *peerIpv6Addr* **as-path-filter** { *number* | *name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *number* | Specifies the number of an AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **import** | Applies a filtering policy to the routes received from a peer. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **peer as-path-filter import** command is used to apply a route filtering policy based on an AS\_Path list to BGP routes to be received from a specified peer, the routers that do not match the policy are filtered out.

**Prerequisites**

The **ip as-path-filter** command has been run to define an AS-Path filter.

**Precautions**

Only one AS\_Path filter can be used to filter routes to be received from the same peer.The **peer as-path-filter import** command is mutually exclusive with the **peer route-filter import** commands.


Example
-------

# Configure an AS\_Path filter for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit 200
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 as-path-filter 3 import

```