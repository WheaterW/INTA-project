peer as-path-filter export (BGP-IPv6 unicast address family view)(IPv4)
=======================================================================

peer as-path-filter export (BGP-IPv6 unicast address family view)(IPv4)

Function
--------



The **peer as-path-filter export** command applies a routing policy based on an AS\_Path list to filter BGP routes to be advertised to a specified peer.

The **undo peer as-path-filter export** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes to be advertised to a peer, and all the BGP routes will be advertised to the peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **as-path-filter** { *number* | *name* } **export**

**undo peer** *ipv4-address* **as-path-filter** { *number* | *name* } **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *number* | Specifies the number of the AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To apply a routing policy based on an AS\_Path list to filter BGP routes to be advertised to a specified peer, run the **peer as-path-filter export** command. This configuration allows the routes that do not match the policy to be filtered out.

**Prerequisites**

Before configuring a BGP route-filter based on the AS\_Path, you must run the **ip as-path-filter** command to define an AS\_Path filter first.

**Precautions**

Only one AS\_Path filter can be used to filter routes to be advertised to the same peer.


Example
-------

# Configure an AS\_Path filter for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit 100
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 as-path-filter 3 export

```