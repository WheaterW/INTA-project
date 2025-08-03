display bgp routing-table unnumbered peer interface statistics
==============================================================

display bgp routing-table unnumbered peer interface statistics

Function
--------



The **display bgp routing-table unnumbered peer interface advertised-routes statistics** command displays statistics about BGP routes sent to unnumbered BGP peers.

The **display bgp routing-table unnumbered peer interface received-routes statistics** command displays statistics about BGP routes received from unnumbered BGP peers.




Format
------

**display bgp routing-table unnumbered peer interface** { *interface-name* | *IfType* *IFNum* } { **advertised-routes** | **received-routes** | **received-routes** **active** } **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies the number of an interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |
| **advertised-routes** | Displays the routes advertised to a peer. | - |
| **received-routes** | Indicates the routes from the peer. | - |
| **active** | Displays active route from the peer. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display bgp routing-table unnumbered peer interface advertised-routes statistics** command to view statistics about BGP routes sent to unnumbered BGP peers.To check statistics about BGP routes received from unnumbered BGP peers, run the **display bgp routing-table unnumbered peer interface received-routes statistics** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about BGP routes received from unnumbered BGP peers.
```
<HUAWEI> display bgp routing-table unnumbered peer interface 100GE 1/0/1 received-routes statistics
 Received routes total: 1

```

**Table 1** Description of the **display bgp routing-table unnumbered peer interface statistics** command output
| Item | Description |
| --- | --- |
| Received routes total | Number of received routes. |