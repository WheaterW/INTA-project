display multicast routing-table static
======================================

display multicast routing-table static

Function
--------



The **display multicast routing-table static** command displays multicast static routes.




Format
------

**display multicast routing-table** [ **vpn-instance** *vpn-instance-name* ] **static** [ **config** ] [ *prefix4* { *masklength* | *mask4* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays multicast static routes of a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **config** | Displays the configuration of the multicast static routes. | - |
| *prefix4* | Displays multicast static routes of a specified multicast source address.  source-address specifies a multicast source address. | The address is in dotted decimal notation. |
| *masklength* | Specifies the mask length of the multicast source address. | The value is an integer ranging from 0 to 32. |
| *mask4* | Specifies the mask of the multicast source address. | The mask is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Before running the **display multicast routing-table static** command, note the following:

* If neither vpn-instance is specified, the command displays multicast static routes of the public network instance.
* If config is specified, the command displays all multicast static routes, including active routes and inactive routes.
* If the multicast static route configured on the local router cannot be displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of static routes in the multicast routing table.
```
<HUAWEI> display multicast routing-table static config
Multicast Routing Table
Routes : 1

 Mroute 10.1.0.0/24,     RPF neighbor = 10.1.2.2
 Matched routing protocol = ospf, process-id = 100, Route-policy = none
 Preference = 1, Order = 1

```

# Display the configuration of static routes in the multicast routing table.
```
<HUAWEI> display multicast routing-table static
Multicast Routing Table
Routes : 1

 Mroute 10.1.0.0/24
          Interface = 100GE1/0/1       RPF Neighbor = 10.1.2.2
          Matched routing protocol = ospf, process-id = 100, Route-policy = none
          Preference = 1, Order = 1
 Running Configuration = ip rpf-route-static 10.1.0.0 24 ospf 100 10.1.2.2 order 1

```

# Display all multicast static routes to multicast source 10.10.0.0/16 in the public network instance.
```
<HUAWEI> display multicast routing-table static 10.10.0.0 255.255.0.0
Multicast Routing Table
Routes : 1

 Mroute 10.1.0.0/24
          Interface = 100GE1/0/1       RPF Neighbor = 10.1.2.2
          Matched routing protocol = ospf, process-id = 100, Route-policy = none
          Preference = 1, Order = 1
 Running Configuration = ip rpf-route-static 10.1.0.0 24 ospf 100 10.1.2.2 order 1

```

**Table 1** Description of the **display multicast routing-table static** command output
| Item | Description |
| --- | --- |
| Multicast Routing Table | Multicast routing table. |
| Routes | Number of routes. |
| Mroute | Source address and mask length of a multicast route. |
| RPF Neighbor | Neighbor IP address through which the source address is reachable. |
| Matched routing protocol | Matching unicast route type. |
| process-id | Process ID of a routing protocol. |
| Route-policy | Routing policy. The source address of a route must match the routing policy. |
| Preference | Route priority. |
| Order | Order of a route. |
| Interface | Outbound interface of the reachable multicast source. |
| Running Configuration | Command line for configuring a static route. |