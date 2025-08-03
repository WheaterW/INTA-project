peer as-path-filter import (BGP-IPv4 unicast address family view) (group)
=========================================================================

peer as-path-filter import (BGP-IPv4 unicast address family view) (group)

Function
--------



The **peer as-path-filter import** command configures a BGP route filtering policy based on the AS\_Path for the routes received from a peer group.

The **undo peer as-path-filter import** command cancels the existing configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes received from peers in a peer group, and all the received BGP routes will be permitted.


Format
------

**peer** *group-name* **as-path-filter** { *number* | *name* } **import**

**undo peer** *group-name* **as-path-filter** { *number* | *name* } **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *number* | Specifies the number of the AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-IPv4 unicast address family view


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
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer test as-path-filter 3 import

```