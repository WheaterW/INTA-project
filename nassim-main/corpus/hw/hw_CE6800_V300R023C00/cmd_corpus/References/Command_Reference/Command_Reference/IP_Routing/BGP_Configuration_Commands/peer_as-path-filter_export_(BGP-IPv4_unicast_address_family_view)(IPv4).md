peer as-path-filter export (BGP-IPv4 unicast address family view)(IPv4)
=======================================================================

peer as-path-filter export (BGP-IPv4 unicast address family view)(IPv4)

Function
--------



The **peer as-path-filter export** command applies a routing policy based on an AS\_Path list to filter BGP routes to be advertised to a specified peer.

The **undo peer as-path-filter export** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes to be advertised to a peer, and all the BGP routes will be advertised to the peer.


Format
------

**peer** *ipv4-address* **as-path-filter** { *number* | *name* } **export**

**undo peer** *ipv4-address* **as-path-filter** { *number* | *name* } **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| *number* | Specifies the number of the AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters. If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

BGP-IPv4 unicast address family view


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
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 as-path-filter 3 export

```