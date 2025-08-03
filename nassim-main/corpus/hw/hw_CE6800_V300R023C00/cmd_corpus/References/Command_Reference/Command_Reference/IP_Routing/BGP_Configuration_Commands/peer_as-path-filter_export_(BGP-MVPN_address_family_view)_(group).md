peer as-path-filter export (BGP-MVPN address family view) (group)
=================================================================

peer as-path-filter export (BGP-MVPN address family view) (group)

Function
--------



The **peer as-path-filter export** command configures a route-filter based on the AS\_Path for the routes to be advertised to a peer group.

The **undo peer as-path-filter export** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes to be advertised to peers in a peer group, and all the BGP routes will be advertised to the peer group.


Format
------

**peer** *group-name* **as-path-filter** { *number* | *name* } **export**

**undo peer** *group-name* **as-path-filter** { *number* | *name* } **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *number* | Specifies the number of the AS\_Path filter. | The value is an integer ranging from 1 to 256. |
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

When the **peer as-path-filter export** command is run to apply a routing policy to the BGP routes to be advertised to a specified peer group, the AS\_Path filter filters out unqualified routes.

**Prerequisites**

Before configuring a BGP route-filter based on the AS\_Path, you must run the **ip as-path-filter** command to define an AS\_Path filter first.

**Precautions**

Only one AS\_Path filter can be used to filter routes to be advertised to the same peer.The **peer as-path-filter export** command is mutually exclusive with the **peer route-filter export** commands.


Example
-------

# Configure an AS\_Path-based BGP MVPN route filtering policy for the peer group named test.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer test enable
[*HUAWEI-bgp-af-mvpn] peer test as-path-filter 3 export

```