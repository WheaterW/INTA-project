peer as-path-filter import (BGP-VPN-Target address family view)
===============================================================

peer as-path-filter import (BGP-VPN-Target address family view)

Function
--------



The **peer as-path-filter import** command configures a policy based on an AS\_Path list for filtering BGP routes received from a peer.

The **undo peer as-path-filter import** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes received from a peer, and all the BGP routes will be received from the peer.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **as-path-filter** { *number* | *name* } **import**

**undo peer** { *ipv4-address* | *ipv6-address* } **as-path-filter** { *number* | *name* } **import**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **as-path-filter** { *number* | *name* } **import**

**undo peer** *ipv4-address* **as-path-filter** { *number* | *name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *number* | Specifies the number of an AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN-target address family view


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
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.1.1.2 as-path-filter 3 import

```