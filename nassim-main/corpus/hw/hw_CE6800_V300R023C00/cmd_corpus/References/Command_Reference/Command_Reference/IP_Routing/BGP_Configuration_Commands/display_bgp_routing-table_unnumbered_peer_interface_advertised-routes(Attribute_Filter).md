display bgp routing-table unnumbered peer interface advertised-routes(Attribute Filter)
=======================================================================================

display bgp routing-table unnumbered peer interface advertised-routes(Attribute Filter)

Function
--------



The **display bgp routing-table unnumbered peer interface advertised-routes** command displays routes of BGP unnumbered peers.




Format
------

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **advertised-routes** *ipv4-address* [ *mask* | *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of an IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length. | The value is an integer ranging from 0 to 32. |
| **as-path** | Displays AS\_Path attribute information. | - |
| **community-list** | Displays the community attribute contained in a route. | - |
| **large-community** | Displays the routes with the specified BGP Large-Community in the routing table. | - |
| **ext-community** | Displays extcommunity attribute information. | - |
| **cluster-list** | Displays the cluster list of a route. | - |
| **advertised-peer** | Displays the list of the peers to which a route is advertised. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can specify different parameters for BGP unnumbered peers to view specific routing information.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the advertised-peer information of the routes of a specified BGP unnumbered peer.
```
<HUAWEI> display bgp routing-table unnumbered peer interface 100GE 1/0/1 advertised-routes 10.1.1.1 advertised-peer
 
 BGP routing table entry information of 10.1.1.1/32:
 From: FE80::3AAE:90FF:FE11:309(100GE 1/0/1)
 Advertised to such 2 peers:
     10.1.1.8
     FE80::3AAE:90FF:FE11:405(100GE 1/0/2)

```

**Table 1** Description of the **display bgp routing-table unnumbered peer interface advertised-routes(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| BGP routing table entry information | The following information is about a specified BGP routing entry. |
| Advertised to such 2 peers | Information about the sending peer. For an unnumbered peer, the outbound interface is also displayed. |
| From | IP address of the device that advertises the route. The outbound interface is also displayed for unnumbered neighbors. |