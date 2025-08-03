display bgp routing-table different-origin-as (public)
======================================================

display bgp routing-table different-origin-as (public)

Function
--------



The **display bgp routing-table different-origin-as** command displays BGP routes that have the same destination address but different source AS numbers.




Format
------

**display bgp routing-table different-origin-as**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the BGP routes that have the same destination address but different source AS numbers, run the display bgp routing-table different-origin-as command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display BGP routes that have the same destination address but different source AS numbers.
```
<HUAWEI> display bgp routing-table different-origin-as
 BGP Local router ID is 10.1.3.1
 Status codes: * - valid, > - best, d - damped, h - history,
               i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete


 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
 *>     10.2.1.0/24        0.0.0.0                        0                     0       i
 *                         10.17.1.1                      1                     0      300?

```

**Table 1** Description of the **display bgp routing-table different-origin-as (public)** command output
| Item | Description |
| --- | --- |
| BGP Local router ID is | Router ID of the local BGP device. |
| Status codes | The codes of status. |
| Origin | Origin attribute of a BGP route:   * IGP: indicates that the route is added to the BGP routing table using the network command. * EGP: indicates that the route is obtained using EGP. * Incomplete: indicates that the route source is unknown. For example a route is imported using the import-route command. |
| Total Number of Routes | The total number of BGP routes. |
| Network | Indicates the network address in the BGP routing table. |
| NextHop | Next hop address used to forward the packet. |
| MED | Indicates the MED of the route. |
| LocPrf | Local preference of a route. |
| PrefVal | PrefVal of a BGP route. |
| Path/Ogn | AS-Path number and the Origin attribute. |