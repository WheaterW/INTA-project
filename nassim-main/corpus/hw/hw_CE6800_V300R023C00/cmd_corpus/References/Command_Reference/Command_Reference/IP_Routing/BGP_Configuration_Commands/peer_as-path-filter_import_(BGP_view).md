peer as-path-filter import (BGP view)
=====================================

peer as-path-filter import (BGP view)

Function
--------



The **peer as-path-filter import** command configures a policy based on an AS\_Path list for filtering BGP routes received from a peer.

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
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *number* | Specifies the number of the AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP view


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



Only one AS\_Path filter can be used to filter the routes received from the same peer. Similarly, only one AS\_Path filter can be used to filter routes to be received from the same peer.




Example
-------

# Configure an AS\_Path filter for a peer.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] peer 10.1.1.1 as-path-filter 3 import

```