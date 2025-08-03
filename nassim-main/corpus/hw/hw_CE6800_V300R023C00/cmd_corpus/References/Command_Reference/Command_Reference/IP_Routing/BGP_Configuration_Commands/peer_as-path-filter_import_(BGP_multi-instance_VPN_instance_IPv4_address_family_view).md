peer as-path-filter import (BGP multi-instance VPN instance IPv4 address family view)
=====================================================================================

peer as-path-filter import (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **peer as-path-filter import** command applies a routing policy based on an AS\_Path list to filter BGP routes received from a specified peer.

The **undo peer as-path-filter import** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes received from a peer, and all the BGP routes will be received from the peer.


Format
------

**peer** *ipv4-address* **as-path-filter** { *number* | *name* } **import**

**undo peer** *ipv4-address* **as-path-filter** { *number* | *name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *number* | Specifies the number of the AS path filter. | The value is a decimal integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To apply a routing policy based on an AS\_Path list to filter BGP routes received from a specified peer, run the **peer as-path-filter import** command. This configuration allows the routes that do not match the policy to be filtered out.



**Prerequisites**



Before configuring a BGP route-filter based on the AS\_Path, you must run the **ip as-path-filter** command to define an AS\_Path filter first.



**Precautions**



Only one AS\_Path filter can be used to filter the routes received from the same peer. Similarly, only one AS\_Path filter can be used to filter routes to be received from the same peer.




Example
-------

# Configure an AS\_Path filter for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit 20
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-instance-a-vrf1] peer 10.1.1.1 as-path-filter 3 import

```