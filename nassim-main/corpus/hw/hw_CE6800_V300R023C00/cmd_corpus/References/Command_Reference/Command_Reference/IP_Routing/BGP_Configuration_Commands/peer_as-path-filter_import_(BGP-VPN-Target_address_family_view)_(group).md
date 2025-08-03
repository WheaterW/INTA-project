peer as-path-filter import (BGP-VPN-Target address family view) (group)
=======================================================================

peer as-path-filter import (BGP-VPN-Target address family view) (group)

Function
--------



The **peer as-path-filter import** command configures a policy based on an AS\_Path list for filtering BGP routes received from a peer group.

The **undo peer as-path-filter import** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes received from a peer group, and all the BGP routes will be received from the peer group.


Format
------

**peer** *group-name* **as-path-filter** { *number* | *name* } **import**

**undo peer** *group-name* **as-path-filter** { *number* | *name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
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



After the **peer as-path-filter import** command is used to apply a route filtering policy based on an AS\_Path list to BGP routes to be received from a specified peer group, the routers that do not match the policy are filtered out.



**Prerequisites**



The **ip as-path-filter** command has been run to define an AS-Path filter.



**Precautions**



Only one AS\_Path filter can be used to filter routes to be received from the same peer.The **peer as-path-filter import** command is mutually exclusive with the **peer route-filter import** commands.




Example
-------

# Configure an AS\_Path filter for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test as-path-filter 3 import

```