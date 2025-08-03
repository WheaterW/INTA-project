display bgp routing-table (ipv4-address)
========================================

display bgp routing-table (ipv4-address)

Function
--------



The **display bgp routing-table** command displays information about BGP routes with specified destinations.




Format
------

**display bgp routing-table** *ipv4-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies a destination IPv4 address. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view the BGP routes with specified destinations, run the display bgp routing-table command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the routing information with specified destination in BGP public network.
```
<HUAWEI> display bgp routing-table 10.1.1.1
 BGP local router ID : 192.168.2.2
 Local AS number : 100
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 10.1.1.1/32:
 From: 10.1.3.1 (192.168.2.3)
 Route Duration: 0d00h01m33s
 Direct Out-interface: 100GE1/0/1
 Relay is delayed as nexthop flapped frequently
 Original nexthop: 10.1.3.1
 Qos information : 0x0
 Primary Routing Table: vrf1
 AS-path 200, origin incomplete, MED 0, pref-val 0, valid, external, best, select, active, pre 255
 Advertised to such 1 peers:
    10.1.3.1

```

**Table 1** Description of the **display bgp routing-table (ipv4-address)** command output
| Item | Description |
| --- | --- |
| BGP local router ID | Router ID of the local BGP device. |
| BGP routing table entry information of | Routing entry information. |
| Local AS number | Local AS number. |
| Route Duration | Route duration. |
| Relay is delayed as nexthop flapped frequently | Route recursion to a specified next hop is suppressed because the next hop flaps. If the number of routes is small, the suppression period may be too short. In this case, this field is not displayed in the command output. |
| Original nexthop | Original next hop. |
| Qos information | QoS information. |
| AS-path | AS\_Path attribute. Nil indicates that the attribute value is null. |
| MED | MED (Multi-Exit-Discriminator): determines the optimal route for traffic entering an AS. In the case of the same other conditions, the route with the smallest MED value is selected as the optimal route. |
| pref-val | PrefVal of a BGP route. |
| pre | BGP route priority. |
| Advertised to such 1 peers | Peers to which routes are advertised, The outbound interface is displayed for unnumbered peers. |
| Direct Out-interface | Directly connected outbound interface. |
| Primary Routing Table | Source routing table. |
| Paths | Route selection result. |
| From | IP address of the route advertiser. The outbound interface is displayed for unnumbered peers. |
| Origin | Origin attribute of a BGP route:   * IGP: indicates that the route is added to the BGP routing table using the network command. * EGP: indicates that the route is obtained using EGP. * Incomplete: indicates that the route source is unknown. For example a route is imported using the import-route command. |
| valid | Valid route. |
| best | The BGP route is an optimal route. |
| select | Preferred route. |
| active | Active route.  The field is displayed only after the active-route-advertise command is run. |
| external | External route. |