display bgp routing-table cidr
==============================

display bgp routing-table cidr

Function
--------



The **display bgp routing-table cidr** command displays classless inter-domain routing (CIDR) information about BGP routes.




Format
------

**display bgp routing-table cidr**


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

To view the classless inter-domain routing (CIDR) information about BGP routes, run the display bgp routing-table cidr command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays classless inter-domain routing (CIDR) information about BGP routes.
```
<HUAWEI> display bgp routing-table cidr
 BGP Local router ID is 10.1.3.2
 Status codes: * - valid, > - best, d - damped, h - history,
               i - internal, s - suppressed, S - Stale
 Origin      : i - IGP, e - EGP, ? - incomplete


 Total Number of Routes: 2
        Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
 *>     10.1.3.1/32        0.0.0.0                        0                     0       ?
 *>     10.1.3.2/32        0.0.0.0                        0                     0       ?

```

**Table 1** Description of the **display bgp routing-table cidr** command output
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