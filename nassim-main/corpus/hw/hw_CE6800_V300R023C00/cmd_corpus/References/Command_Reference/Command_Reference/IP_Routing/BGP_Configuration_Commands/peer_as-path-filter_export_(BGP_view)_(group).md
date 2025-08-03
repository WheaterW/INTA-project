peer as-path-filter export (BGP view) (group)
=============================================

peer as-path-filter export (BGP view) (group)

Function
--------



The **peer as-path-filter export** command configures a policy based on an AS\_Path list for filtering BGP routes to be advertised to a specified peer group.

The **undo peer as-path-filter export** command cancels this configuration.



By default, no policy based on an AS\_Path list is configured for filtering BGP routes to be advertised to a peer group, and all the BGP routes will be advertised to the peer group.


Format
------

**peer** *group-name* **as-path-filter** { *number* | *name* } **export**

**undo peer** *group-name* **as-path-filter** { *number* | *name* } **export**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *number* | Specifies the number of an AS\_Path filter. | The value is an integer ranging from 1 to 256. |
| *name* | Specifies the name of an AS\_Path filter. | The value is a string of 1 to 51 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the **peer as-path-filter export** command is used to apply a route filtering policy based on an AS\_Path list to BGP routes to be advertised to a specified peer group, the routers that do not match the policy are filtered out.

**Prerequisites**

The **ip as-path-filter** command has been run to define an AS-Path filter.

**Precautions**



Only one AS\_Path filter can be used to filter routes to be advertised to the same peer.




Example
-------

# Configure an AS\_Path filter for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip as-path-filter 3 permit ^10_
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test as-path-filter 3 export

```