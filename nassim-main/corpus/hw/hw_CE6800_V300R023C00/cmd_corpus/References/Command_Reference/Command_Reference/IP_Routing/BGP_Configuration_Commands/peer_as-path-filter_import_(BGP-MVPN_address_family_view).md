peer as-path-filter import (BGP-MVPN address family view)
=========================================================

peer as-path-filter import (BGP-MVPN address family view)

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
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *number* | Specifies the number of the AS path filter. | The value is a decimal integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-MVPN address family view


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

Only one AS\_Path filter can be used to filter routes to be received from the same peer.The **peer as-path-filter import** command is mutually exclusive with the **peer route-filter import** commands.


Example
-------

# Configure an AS\_Path MBGP route filter for a peer 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 10
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 as-path-filter 3 import

```