display bgp ipv6 routing-table unnumbered peer interface advertised-routes(Attribute Filter)
============================================================================================

display bgp ipv6 routing-table unnumbered peer interface advertised-routes(Attribute Filter)

Function
--------



The **display bgp ipv6 routing-table unnumbered peer interface advertised-routes** command allows you to specify different parameters to view the specified routes of BGP unnumbered peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } **advertised-routes** *ipv6-address* [ *mask-length* ] { **as-path** | **community-list** | **large-community** | **ext-community** | **cluster-list** | **advertised-peer** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies the type of an interface. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| *ipv6-address* | IPv6 network segment address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *mask-length* | Specifies the mask length of the network address. | The value is an integer ranging from 0 to 128. |
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

You can specify different parameters for BGP unnumbered peers to view specific routing information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the advertised-peer information of the routes of BGP unnumbered peers.
```
<HUAWEI> display bgp ipv6 routing-table unnumbered peer interface 100GE 1/0/1 advertised-routes 2001:DB8::55 advertised-peer
 
 BGP routing table entry information of 2001:DB8::55/128:
 From: 2001::DB8::66
 Advertised to such 3 peers:
     FE80::3AAE:90FF:FE11:309(100GE 1/0/1)
     2001::DB8::6
     10.1.1.2

```

**Table 1** Description of the **display bgp ipv6 routing-table unnumbered peer interface advertised-routes(Attribute Filter)** command output
| Item | Description |
| --- | --- |
| BGP routing table entry information | The following information is about a specified BGP routing entry. |
| Advertised to such 3 peers | Information about the sending peer. For an unnumbered peer, the outbound interface is also displayed. |
| From | IP address of the device that advertises the route. The outbound interface is also displayed for unnumbered neighbors. |