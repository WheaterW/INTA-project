display bgp routing-table relay-nexthop interface
=================================================

display bgp routing-table relay-nexthop interface

Function
--------



The **display bgp routing-table relay-nexthop interface** command displays information about the recursion of routes to a specified IP address.




Format
------

**display bgp routing-table** *ipv4-address* [ *mask-length* | *mask-ipv4* ] **relay-nexthop** **interface**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask of an IPv4 address. | The value is an integer ranging from 0 to 32. |
| *mask-ipv4* | Specifies the mask of an IPv4 address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Supernet routes are not delivered to the RM module. As a result, information about recursion of supernet routes is not displayed in the IP routing table. To check information about the recursion of supernet routes, run the **display bgp routing-table relay-nexthop interface** command. If the supernet routes recurse to IP routes and tunnels, information about both the IP routes and tunnels is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the recursion of routes to 6.6.6.6.
```
<HUAWEI> display bgp routing-table 10.6.6.6 relay-nexthop interface

 BGP routing table entry information of 10.6.6.6/32:
 From: 10.10.1.2 (10.5.1.2)
 Relay Type: Route Relay
 Relay Nexthop: 10.10.3.2
 Original nexthop: 10.6.6.6
 Relay Out Interface: Eth-trunk1.66

 From: 10.10.1.2 (10.5.1.2)
 Relay Type: Route Relay
 Relay Nexthop: 10.10.2.2
 Original nexthop: 10.6.6.6
 Relay Out Interface: Eth-trunk1.65

```

**Table 1** Description of the **display bgp routing-table relay-nexthop interface** command output
| Item | Description |
| --- | --- |
| Relay Type | Recursion type. |
| Relay Nexthop | Recursive next hop. |
| Relay Out Interface | Outbound interface used in the recursion. |
| Original nexthop | Original next hop of the route. |
| From | IP address of the peer from which the route is received. |