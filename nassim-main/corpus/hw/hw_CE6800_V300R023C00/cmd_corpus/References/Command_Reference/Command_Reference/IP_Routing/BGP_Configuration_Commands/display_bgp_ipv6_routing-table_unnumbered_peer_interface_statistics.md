display bgp ipv6 routing-table unnumbered peer interface statistics
===================================================================

display bgp ipv6 routing-table unnumbered peer interface statistics

Function
--------



The **display bgp ipv6 routing-table unnumbered peer interface advertised-routes statistics** command displays statistics about BGP IPv6 routes sent to unnumbered BGP peers.

The **display bgp ipv6 routing-table unnumbered peer interface received-routes statistics** command displays statistics about BGP IPv6 routes received from unnumbered BGP peers.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **advertised-routes** | **received-routes** | **received-routes** **active** } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies the type of an interface. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **advertised-routes** | Displays the routes advertised to a peer. | - |
| **received-routes** | Indicates the route from the peer. | - |
| **active** | Displays active routes from the peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Run the **display bgp ipv6 routing-table unnumbered peer interface advertised-routes statistics** command to check statistics about BGP IPv6 routes sent to unnumbered BGP peers.To check statistics about BGP IPv6 routes received from unnumbered BGP peers, run the **display bgp ipv6 routing-table unnumbered peer interface received-routes statistics** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP IPv6 routes received from unnumbered BGP peers.
```
<HUAWEI> display bgp ipv6 routing-table unnumbered peer interface 100GE 1/0/1  received-routes statistics
 Received routes total: 2

```

**Table 1** Description of the **display bgp ipv6 routing-table unnumbered peer interface statistics** command output
| Item | Description |
| --- | --- |
| Received routes total | Number of received routes. |